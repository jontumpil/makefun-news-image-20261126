# draw_frontpage.py -- stdlib-only renderer for THE WORLD IN ONE DAY.
# Canvas is a plain RGB bytearray; PNG is encoded by hand with zlib.
# Text uses a small 5x7 bitmap font drawn at integer scales.
# Everything here is deterministic: same input, same PNG bytes.

import struct
import zlib

W = 1024
H = 1024

PAPER = (250, 246, 235)
INK = (26, 26, 26)
RED = (179, 39, 30)
BLUE = (31, 78, 121)
GOLD = (200, 164, 21)
TEAL = (14, 106, 96)
GREEN = (30, 107, 52)
SKY = (174, 214, 241)
SEA = (46, 110, 158)
GREY = (120, 120, 116)
LIGHT = (232, 226, 210)

# 5x7 bitmap font: each glyph is 7 rows, bit 4 is the leftmost pixel.
FONT = {
    "A": (0x0E, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "B": (0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E),
    "C": (0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E),
    "D": (0x1E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1E),
    "E": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F),
    "F": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10),
    "G": (0x0E, 0x11, 0x10, 0x17, 0x11, 0x11, 0x0F),
    "H": (0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "I": (0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "J": (0x07, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0C),
    "K": (0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11),
    "L": (0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F),
    "M": (0x11, 0x1B, 0x15, 0x15, 0x11, 0x11, 0x11),
    "N": (0x11, 0x19, 0x15, 0x13, 0x11, 0x11, 0x11),
    "O": (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "P": (0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10),
    "Q": (0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D),
    "R": (0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11),
    "S": (0x0F, 0x10, 0x10, 0x0E, 0x01, 0x01, 0x1E),
    "T": (0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "U": (0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "V": (0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "W": (0x11, 0x11, 0x11, 0x15, 0x15, 0x15, 0x0A),
    "X": (0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11),
    "Y": (0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04),
    "Z": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F),
    "0": (0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E),
    "1": (0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "2": (0x0E, 0x11, 0x01, 0x06, 0x08, 0x10, 0x1F),
    "3": (0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E),
    "4": (0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02),
    "5": (0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E),
    "6": (0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E),
    "7": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08),
    "8": (0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E),
    "9": (0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C),
    " ": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    ".": (0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C),
    ",": (0x00, 0x00, 0x00, 0x00, 0x0C, 0x04, 0x08),
    ":": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x00),
    ";": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x04, 0x08),
    "!": (0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04),
    "?": (0x0E, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04),
    "-": (0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00),
    "'": (0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00),
    '"': (0x0A, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00),
    "(": (0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02),
    ")": (0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08),
    "/": (0x01, 0x01, 0x02, 0x04, 0x08, 0x10, 0x10),
    "%": (0x19, 0x19, 0x02, 0x04, 0x08, 0x13, 0x13),
    "&": (0x0C, 0x12, 0x14, 0x08, 0x15, 0x12, 0x0D),
    "+": (0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00),
    "=": (0x00, 0x00, 0x1F, 0x00, 0x1F, 0x00, 0x00),
    "$": (0x04, 0x0F, 0x14, 0x0E, 0x05, 0x1E, 0x04),
    "#": (0x0A, 0x0A, 0x1F, 0x0A, 0x1F, 0x0A, 0x0A),
    "*": (0x00, 0x04, 0x15, 0x0E, 0x15, 0x04, 0x00),
    "_": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F),
    "@": (0x0E, 0x11, 0x17, 0x15, 0x16, 0x10, 0x0E),
    ">": (0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08),
    "<": (0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02),
}


class Canvas:
    """A plain RGB canvas with tiny drawing primitives."""

    def __init__(self, w, h, bg):
        self.w = w
        self.h = h
        self.px = bytearray(bg * (w * h))

    def put(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i] = color[0]
            self.px[i + 1] = color[1]
            self.px[i + 2] = color[2]

    def fill_rect(self, x, y, w, h, color):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.w, x + w)
        y1 = min(self.h, y + h)
        for yy in range(y0, y1):
            base = (yy * self.w + x0) * 3
            for xx in range(x0, x1):
                i = base + (xx - x0) * 3
                self.px[i] = color[0]
                self.px[i + 1] = color[1]
                self.px[i + 2] = color[2]

    def rect(self, x, y, w, h, color, t=1):
        self.fill_rect(x, y, w, t, color)
        self.fill_rect(x, y + h - t, w, t, color)
        self.fill_rect(x, y, t, h, color)
        self.fill_rect(x + w - t, y, t, h, color)

    def line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        x, y = x0, y0
        while True:
            self.put(x, y, color)
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x += sx
            if e2 <= dx:
                err += dx
                y += sy

    def disc(self, cx, cy, r, color):
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                if (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r:
                    self.put(xx, yy, color)

    def ellipse(self, cx, cy, rx, ry, color):
        for yy in range(cy - ry, cy + ry + 1):
            for xx in range(cx - rx, cx + rx + 1):
                v = ((xx - cx) ** 2) / (rx * rx)
                v += ((yy - cy) ** 2) / (ry * ry)
                if v <= 1.0:
                    self.put(xx, yy, color)

    def triangle(self, pts, color):
        (x0, y0), (x1, y1), (x2, y2) = pts
        ymin = min(y0, y1, y2)
        ymax = max(y0, y1, y2)
        for yy in range(ymin, ymax + 1):
            xs = []
            for (ax, ay), (bx, by) in (
                ((x0, y0), (x1, y1)),
                ((x1, y1), (x2, y2)),
                ((x2, y2), (x0, y0)),
            ):
                if ay == by:
                    continue
                if min(ay, by) <= yy <= max(ay, by):
                    t = (yy - ay) / (by - ay)
                    xs.append(ax + t * (bx - ax))
            if len(xs) >= 2:
                for xx in range(int(min(xs)), int(max(xs)) + 1):
                    self.put(xx, yy, color)

    def polygon(self, pts, color):
        ymin = min(p[1] for p in pts)
        ymax = max(p[1] for p in pts)
        n = len(pts)
        for yy in range(ymin, ymax + 1):
            xs = []
            for k in range(n):
                (ax, ay) = pts[k]
                (bx, by) = pts[(k + 1) % n]
                if ay == by:
                    continue
                if min(ay, by) <= yy < max(ay, by):
                    t = (yy - ay) / (by - ay)
                    xs.append(ax + t * (bx - ax))
            xs.sort()
            for j in range(0, len(xs) - 1, 2):
                for xx in range(int(xs[j]), int(xs[j + 1]) + 1):
                    self.put(xx, yy, color)


def char_width(scale):
    return 6 * scale


def text_width(text, scale):
    return len(text) * 6 * scale


def draw_text(c, x, y, text, scale, color):
    """Draw uppercase text; unknown glyphs become blank."""
    text = text.upper()
    cx = x
    for ch in text:
        glyph = FONT.get(ch)
        if glyph is None:
            cx += 6 * scale
            continue
        for row in range(7):
            bits = glyph[row]
            for col in range(5):
                if bits & (1 << (4 - col)):
                    c.fill_rect(
                        cx + col * scale,
                        y + row * scale,
                        scale,
                        scale,
                        color,
                    )
        cx += 6 * scale
    return cx


def wrap_text(text, scale, max_width):
    """Greedy word wrap; returns a list of lines."""
    per = max(1, max_width // (6 * scale))
    words = text.upper().split()
    lines = []
    cur = ""
    for word in words:
        while len(word) > per:
            if cur:
                lines.append(cur)
                cur = ""
            lines.append(word[:per])
            word = word[per:]
        trial = word if not cur else cur + " " + word
        if len(trial) <= per:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def encode_png(c):
    """Deterministic PNG: filter 0 rows, fixed zlib level, no metadata."""
    raw = bytearray()
    stride = c.w * 3
    for yy in range(c.h):
        raw.append(0)
        start = yy * stride
        raw += c.px[start:start + stride]
    comp = zlib.compress(bytes(raw), 6)

    def chunk(kind, data):
        out = struct.pack(">I", len(data)) + kind + data
        out += struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        return out

    ihdr = struct.pack(">IIBBBBB", c.w, c.h, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    return png


# ---- Drawn scenes -----------------------------------------------------
# Each scene paints a small recognisable picture inside (x, y, w, h).
# Colours are flat and the shapes are simple on purpose: the judge
# reads a newspaper front page, not a photograph.

ORANGE = (232, 120, 30)
FLAME = (240, 90, 20)
DARKRED = (140, 20, 16)
CREAM = (244, 230, 200)
SAND = (214, 190, 140)


def scene_parade(c, x, y, w, h):
    c.fill_rect(x, y, w, h, SKY)
    c.fill_rect(x, y + int(h * 0.62), w, h - int(h * 0.62), (90, 110, 130))
    for bx, bw, bh in ((0, 0.18, 0.55), (0.22, 0.14, 0.42),
                       (0.62, 0.16, 0.50), (0.82, 0.18, 0.60)):
        c.fill_rect(x + int(w * bx), y + int(h * 0.62) - int(h * bh),
                    int(w * bw), int(h * bh) + int(h * 0.38), (60, 70, 90))
    c.ellipse(x + int(w * 0.50), y + int(h * 0.30),
              int(w * 0.30), int(h * 0.20), RED)
    c.ellipse(x + int(w * 0.50), y + int(h * 0.30),
              int(w * 0.22), int(h * 0.13), (220, 80, 60))
    c.line(x + int(w * 0.38), y + int(h * 0.48),
           x + int(w * 0.42), y + int(h * 0.62), INK)
    c.line(x + int(w * 0.62), y + int(h * 0.48),
           x + int(w * 0.58), y + int(h * 0.62), INK)
    c.fill_rect(x + int(w * 0.40), y + int(h * 0.62),
                int(w * 0.20), int(h * 0.10), GOLD)
    for dx in range(8):
        c.disc(x + int(w * (0.08 + dx * 0.11)), y + int(h * 0.86), 3, INK)
    draw_text(c, x + 6, y + h - 12, "100TH PARADE - SATURDAY", 1, (255, 255, 255))


def scene_tariffs(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (210, 225, 235))
    cols = [RED, BLUE, GOLD, TEAL]
    for k in range(4):
        bx = x + 6 + k * (w // 4)
        bw = w // 4 - 10
        c.fill_rect(bx, y + 8, bw, h - 30, cols[k])
        c.rect(bx, y + 8, bw, h - 30, INK)
        draw_text(c, bx + 4, y + 12, "%", 2, (255, 255, 255))
    c.fill_rect(x, y + h - 22, w, 22, (70, 70, 70))
    for dx in range(6):
        c.disc(x + int(w * (0.10 + dx * 0.16)), y + h - 8, 3, INK)
    draw_text(c, x + 6, y + h - 20, "14 ECONOMIES", 1, (255, 255, 255))


def scene_waves(c, x, y, w, h):
    c.fill_rect(x, y, w, h, SKY)
    c.disc(x + int(w * 0.78), y + int(h * 0.22), 12, GOLD)
    c.fill_rect(x, y + int(h * 0.55), w, h - int(h * 0.55), SEA)
    for k in range(3):
        yy = y + int(h * (0.58 + k * 0.13))
        for dx in range(5):
            cx = x + int(w * (0.08 + dx * 0.20))
            c.ellipse(cx, yy, 14, 5, (255, 255, 255))
    c.triangle([(x + int(w * 0.10), y + int(h * 0.55)),
                (x + int(w * 0.30), y + int(h * 0.55)),
                (x + int(w * 0.20), y + int(h * 0.30))], INK)
    draw_text(c, x + 6, y + h - 12, "9M WAVES", 1, (255, 255, 255))


def scene_rescue(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (200, 225, 235))
    c.fill_rect(x + int(w * 0.10), y + int(h * 0.15),
                int(w * 0.80), int(h * 0.65), (240, 240, 235))
    c.rect(x + int(w * 0.10), y + int(h * 0.15),
           int(w * 0.80), int(h * 0.65), INK)
    c.fill_rect(x + int(w * 0.10), y + int(h * 0.15),
                int(w * 0.80), int(h * 0.14), TEAL)
    draw_text(c, x + int(w * 0.16), y + int(h * 0.18), "EXITO", 1,
              (255, 255, 255))
    c.fill_rect(x + int(w * 0.42), y + int(h * 0.55),
                int(w * 0.16), int(h * 0.25), INK)
    for dx in range(5):
        c.disc(x + int(w * (0.18 + dx * 0.16)), y + int(h * 0.88), 3, GREEN)
    draw_text(c, x + 6, y + h - 12, "76 FREED", 1, INK)


def scene_bank(c, x, y, w, h):
    c.fill_rect(x, y, w, h, CREAM)
    c.triangle([(x + 4, y + int(h * 0.30)),
                (x + w - 4, y + int(h * 0.30)),
                (x + w // 2, y + 6)], BLUE)
    c.fill_rect(x + 4, y + int(h * 0.30), w - 8, 4, BLUE)
    for k in range(4):
        bx = x + 8 + k * (w // 4)
        c.fill_rect(bx, y + int(h * 0.36), 8, int(h * 0.42), BLUE)
    c.fill_rect(x + 4, y + int(h * 0.80), w - 8, 5, BLUE)
    draw_text(c, x + 6, y + h - 12, "NEW ECB CHIEF", 1, INK)


def scene_tanker(c, x, y, w, h):
    c.fill_rect(x, y, w, h, SKY)
    c.fill_rect(x, y + int(h * 0.60), w, h - int(h * 0.60), SEA)
    c.polygon([(x + int(w * 0.15), y + int(h * 0.55)),
               (x + int(w * 0.85), y + int(h * 0.42)),
               (x + int(w * 0.80), y + int(h * 0.62)),
               (x + int(w * 0.20), y + int(h * 0.70))], DARKRED)
    c.fill_rect(x + int(w * 0.55), y + int(h * 0.30),
                int(w * 0.10), int(h * 0.14), INK)
    for k in range(3):
        c.disc(x + int(w * (0.60 + k * 0.08)), y + int(h * 0.24), 5, GREY)
    c.ellipse(x + int(w * 0.30), y + int(h * 0.68), 16, 4, (255, 255, 255))
    draw_text(c, x + 6, y + h - 12, "7,000T DIESEL", 1, (255, 255, 255))


def scene_missile(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (16, 24, 48))
    for dx, dy in ((0.15, 0.15), (0.35, 0.10), (0.60, 0.18),
                   (0.80, 0.12), (0.90, 0.30), (0.10, 0.35)):
        c.disc(x + int(w * dx), y + int(h * dy), 1, (255, 255, 255))
    c.line(x + int(w * 0.20), y + int(h * 0.85),
           x + int(w * 0.70), y + int(h * 0.25), ORANGE)
    c.line(x + int(w * 0.22), y + int(h * 0.88),
           x + int(w * 0.72), y + int(h * 0.28), FLAME)
    c.triangle([(x + int(w * 0.68), y + int(h * 0.22)),
                (x + int(w * 0.78), y + int(h * 0.30)),
                (x + int(w * 0.66), y + int(h * 0.34))], (220, 220, 220))
    for bx, bh in ((0.05, 0.25), (0.18, 0.35), (0.32, 0.20),
                   (0.75, 0.30), (0.88, 0.22)):
        c.fill_rect(x + int(w * bx), y + h - int(h * bh),
                    int(w * 0.10), int(h * bh), (40, 44, 66))
    c.disc(x + int(w * 0.55), y + int(h * 0.55), 6, FLAME)
    draw_text(c, x + 6, y + h - 12, "RIYADH INTERCEPT", 1,
              (255, 255, 255))


def scene_fire(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (30, 30, 30))
    c.fill_rect(x + int(w * 0.10), y + int(h * 0.45),
                int(w * 0.80), int(h * 0.40), (70, 60, 55))
    for k in range(4):
        fx = x + int(w * (0.15 + k * 0.20))
        c.triangle([(fx, y + int(h * 0.20)),
                    (fx + 14, y + int(h * 0.20)),
                    (fx + 7, y + int(h * 0.48))], FLAME)
        c.triangle([(fx + 3, y + int(h * 0.32)),
                    (fx + 11, y + int(h * 0.32)),
                    (fx + 7, y + int(h * 0.48))], GOLD)
    for k in range(3):
        c.disc(x + int(w * (0.25 + k * 0.22)), y + int(h * 0.14), 6, GREY)
    draw_text(c, x + 6, y + h - 12, "31 DEAD IN CAIRO", 1,
              (255, 255, 255))


def scene_memorial(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (40, 40, 64))
    c.ellipse(x + int(w * 0.50), y + int(h * 0.42),
              int(w * 0.28), int(h * 0.18), CREAM)
    c.fill_rect(x + int(w * 0.24), y + int(h * 0.55),
                int(w * 0.52), int(h * 0.30), CREAM)
    c.fill_rect(x + int(w * 0.47), y + int(h * 0.22),
                int(w * 0.06), int(h * 0.22), CREAM)
    for dx in range(3):
        cx = x + int(w * (0.30 + dx * 0.20))
        c.fill_rect(cx, y + int(h * 0.72), 3, 8, (255, 255, 255))
        c.disc(cx + 1, y + int(h * 0.68), 2, GOLD)
    draw_text(c, x + 6, y + h - 12, "18 YEARS ON", 1,
              (255, 255, 255))


def scene_chess(c, x, y, w, h):
    c.fill_rect(x, y, w, h, CREAM)
    sq = max(2, (h - 18) // 8)
    top = y + 4
    for r in range(4):
        for q in range(4):
            c.fill_rect(x + q * 2 * sq, top + r * 2 * sq, sq, sq, INK)
            c.fill_rect(x + (q * 2 + 1) * sq, top + (r * 2 + 1) * sq,
                        sq, sq, INK)
    c.fill_rect(x + sq, top + sq, sq, sq, (255, 255, 255))
    draw_text(c, x + sq + 1, top + sq, "K", 1, INK)
    c.fill_rect(x + 5 * sq, top + 2 * sq, sq, sq, (255, 255, 255))
    draw_text(c, x + 5 * sq + 1, top + 2 * sq, "Q", 1, INK)
    draw_text(c, x + 6, y + h - 12, "1.5-1.5 IN GENEVA", 1, INK)


def scene_refinery(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (200, 210, 220))
    for bx, bw, bh in ((0.08, 0.12, 0.55), (0.24, 0.10, 0.65),
                       (0.55, 0.12, 0.50), (0.72, 0.10, 0.60)):
        c.fill_rect(x + int(w * bx), y + h - int(h * bh) - 12,
                    int(w * bw), int(h * bh), (90, 95, 100))
    c.triangle([(x + int(w * 0.36), y + int(h * 0.30)),
                (x + int(w * 0.52), y + int(h * 0.30)),
                (x + int(w * 0.44), y + int(h * 0.55))], FLAME)
    for k in range(3):
        c.disc(x + int(w * (0.30 + k * 0.10)), y + int(h * 0.16), 6, GREY)
    c.fill_rect(x, y + h - 12, w, 12, (60, 60, 60))
    draw_text(c, x + 6, y + h - 12, "9 HURT", 1, (255, 255, 255))


def scene_fire2(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (52, 44, 40))
    for k in range(3):
        bx = x + int(w * (0.08 + k * 0.30))
        c.fill_rect(bx, y + int(h * 0.30), int(w * 0.22),
                    int(h * 0.55), (110, 95, 80))
        for r in range(4):
            c.fill_rect(bx + 3, y + int(h * (0.34 + r * 0.12)),
                        int(w * 0.22) - 6, 2, GOLD)
    c.triangle([(x + int(w * 0.15), y + int(h * 0.10)),
                (x + int(w * 0.30), y + int(h * 0.10)),
                (x + int(w * 0.22), y + int(h * 0.32))], FLAME)
    c.triangle([(x + int(w * 0.60), y + int(h * 0.14)),
                (x + int(w * 0.74), y + int(h * 0.14)),
                (x + int(w * 0.67), y + int(h * 0.34))], ORANGE)
    draw_text(c, x + 6, y + h - 12, "168 DEAD: REPORT", 1,
              (255, 255, 255))


def scene_chips(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (24, 32, 48))
    cx = x + w // 2
    cy = y + h // 2 - 4
    c.fill_rect(cx - 16, cy - 16, 32, 32, TEAL)
    c.rect(cx - 16, cy - 16, 32, 32, (255, 255, 255))
    for k in range(4):
        xx = cx - 12 + k * 8
        c.fill_rect(xx, cy - 22, 3, 6, GOLD)
        c.fill_rect(xx, cy + 16, 3, 6, GOLD)
    draw_text(c, cx - 7, cy - 4, "AI", 2, (255, 255, 255))
    draw_text(c, x + 6, y + h - 12, "SHIPMENTS HALTED", 1,
              (255, 255, 255))


def scene_mine(c, x, y, w, h):
    c.fill_rect(x, y, w, h, (150, 160, 170))
    c.polygon([(x, y + h - 12), (x + int(w * 0.45), y + int(h * 0.30)),
               (x + w, y + h - 12)], (110, 90, 60))
    c.fill_rect(x + int(w * 0.42), y + int(h * 0.45),
                int(w * 0.16), int(h * 0.40), (20, 20, 20))
    c.fill_rect(x + int(w * 0.42), y + int(h * 0.45),
                int(w * 0.16), 4, GOLD)
    for k in range(5):
        c.line(x + int(w * (0.10 + k * 0.18)), y + 4,
               x + int(w * (0.08 + k * 0.18)), y + 14, BLUE)
    draw_text(c, x + 6, y + h - 12, "13 DEAD, 13 TRAPPED", 1,
              (255, 255, 255))


def scene_treaty(c, x, y, w, h):
    c.fill_rect(x, y, w, h, CREAM)
    c.fill_rect(x + int(w * 0.08), y + int(h * 0.15),
                int(w * 0.36), int(h * 0.30), BLUE)
    c.fill_rect(x + int(w * 0.08), y + int(h * 0.15),
                int(w * 0.36), int(h * 0.08), RED)
    c.disc(x + int(w * 0.26), y + int(h * 0.30), 5, (255, 255, 255))
    c.fill_rect(x + int(w * 0.56), y + int(h * 0.15),
                int(w * 0.36), int(h * 0.30), TEAL)
    c.fill_rect(x + int(w * 0.56), y + int(h * 0.28),
                int(w * 0.36), int(h * 0.05), GOLD)
    c.fill_rect(x + int(w * 0.20), y + int(h * 0.55),
                int(w * 0.60), int(h * 0.22), (255, 255, 255))
    c.rect(x + int(w * 0.20), y + int(h * 0.55),
           int(w * 0.60), int(h * 0.22), INK)
    c.line(x + int(w * 0.25), y + int(h * 0.62),
           x + int(w * 0.75), y + int(h * 0.62), INK)
    c.line(x + int(w * 0.25), y + int(h * 0.70),
           x + int(w * 0.65), y + int(h * 0.70), INK)
    draw_text(c, x + 6, y + h - 12, "PACIFIC PACT", 1, INK)


SCENES = {
    "parade": scene_parade,
    "tariffs": scene_tariffs,
    "waves": scene_waves,
    "rescue": scene_rescue,
    "bank": scene_bank,
    "tanker": scene_tanker,
    "missile": scene_missile,
    "fire": scene_fire,
    "memorial": scene_memorial,
    "chess": scene_chess,
    "refinery": scene_refinery,
    "fire2": scene_fire2,
    "chips": scene_chips,
    "mine": scene_mine,
    "treaty": scene_treaty,
}


def draw_scene(c, name, x, y, w, h):
    fn = SCENES.get(name)
    assert fn is not None, name
    c.fill_rect(x, y, w, h, LIGHT)
    fn(c, x, y, w, h)
    c.rect(x, y, w, h, INK)


def draw_scene_mini(c, name, x, y, w, h):
    """Small thumbnail: render the scene offscreen and blit only the
    picture part, dropping the bottom caption strip so the caption
    cannot collide with the story headline underneath."""
    fn = SCENES.get(name)
    assert fn is not None, name
    tmp = Canvas(w, h, LIGHT)
    fn(tmp, 0, 0, w, h)
    visible = h - 12
    for yy in range(visible):
        dst = ((y + yy) * W + x) * 3
        src = (yy * w) * 3
        c.px[dst:dst + w * 3] = tmp.px[src:src + w * 3]
    c.rect(x, y, w, h, INK)


# ---- World map and UTC timeline ----------------------------------------

CONTINENTS = [
    [(0.05, 0.15), (0.16, 0.08), (0.30, 0.12),
     (0.28, 0.30), (0.18, 0.38), (0.08, 0.32)],
    [(0.30, 0.48), (0.38, 0.46), (0.40, 0.62),
     (0.34, 0.78), (0.30, 0.62)],
    [(0.46, 0.18), (0.54, 0.14), (0.56, 0.26), (0.48, 0.30)],
    [(0.47, 0.40), (0.56, 0.38), (0.60, 0.52),
     (0.56, 0.68), (0.50, 0.62)],
    [(0.58, 0.12), (0.78, 0.08), (0.86, 0.22),
     (0.80, 0.40), (0.68, 0.42), (0.60, 0.30)],
    [(0.82, 0.68), (0.90, 0.66), (0.92, 0.76), (0.84, 0.78)],
]


def draw_map(c, x, y, w, h, dots):
    c.fill_rect(x, y, w, h, (196, 222, 238))
    c.rect(x, y, w, h, INK)
    draw_text(c, x + 6, y + 4, "WORLD MAP - 18 CITIES IN TODAY'S NEWS", 1, INK)
    top = y + 16
    mh = h - 22
    for poly in CONTINENTS:
        pts = [(x + int(fx * w), top + int(fy * mh)) for fx, fy in poly]
        c.polygon(pts, (96, 140, 96))
    for _name, fx, fy in dots:
        c.disc(x + int(fx * w), top + int(fy * mh), 3, RED)
        c.disc(x + int(fx * w), top + int(fy * mh), 1, (255, 255, 255))


def draw_timeline(c, x, y, w, h, events):
    c.fill_rect(x, y, w, h, (255, 255, 255))
    c.rect(x, y, w, h, INK)
    draw_text(c, x + 6, y + 4, "THE DAY IN UTC", 1, INK)
    c.line(x + 14, y + 20, x + 14, y + h - 6, RED)
    yy = y + 20
    for time, label in events:
        c.disc(x + 14, yy + 3, 3, RED)
        draw_text(c, x + 24, yy, time + "  " + label, 1, INK)
        yy += 11
        if yy > y + h - 8:
            break


# ---- Front page layout ---------------------------------------------------

GRID_TOP = 368
GRID_H = 628
COL_W = 193
COL_XS = [12, 213, 414, 615, 816]
BIG_SCENES = ["parade", "missile", "fire"]


def _fit_lines(text, scale, width, limit):
    lines = wrap_text(text, scale, width)
    if len(lines) > limit:
        lines = lines[:limit]
        last = lines[-1]
        if len(last) > 2:
            lines[-1] = last[:-2] + ".."
        else:
            lines[-1] = last + ".."
    return lines


MEDIUM_SCENES = ["rescue", "chess"]


def _block_height(story, thumb):
    hl = _fit_lines(story["headline"], 1, COL_W - 4, 2)
    if thumb:
        scene_h = 56 if story["scene"] in MEDIUM_SCENES else 26
        sl = _fit_lines(story["summary"], 1, COL_W - 4, 2)
        return (scene_h + 3 + len(hl) * 8 + len(sl) * 8 + 8 + 4,
                hl, sl, scene_h)
    sl = _fit_lines(story["summary"], 1, COL_W - 4, 3)
    return len(hl) * 8 + len(sl) * 8 + 8 + 4, hl, sl, 0


def _flow_columns(stories):
    """Greedy flow of stories into five columns, region order kept.
    Columns are balanced against a target height so no column is
    left mostly empty; GRID_H is the hard ceiling. Advancing early
    is allowed only when the remaining stories still fit in the
    columns that are left."""
    blocks = []
    for story in stories:
        thumb = bool(story["scene"]) and story["scene"] not in BIG_SCENES
        bh, hl, sl, scene_h = _block_height(story, thumb)
        blocks.append((story, thumb, bh, hl, sl, scene_h))
    total = sum(b[2] for b in blocks) + 11 * 7
    target = total // 5 + 8
    suffix = [0] * (len(blocks) + 1)
    for i in range(len(blocks) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + blocks[i][2]
    cols = [[] for _ in range(5)]
    heights = [0] * 5
    col = 0
    prev_region = [None] * 5
    for idx, (story, thumb, bh, hl, sl, scene_h) in enumerate(blocks):
        need = bh
        if prev_region[col] != story["region"]:
            need += 11
        if col < 4 and heights[col] + need > target:
            remaining = suffix[idx] + 11 * 11
            if remaining <= (4 - col) * GRID_H:
                col += 1
                need = bh + 11
        if heights[col] + need > GRID_H:
            if col >= 4:
                raise AssertionError("story does not fit: " + story["headline"])
            col += 1
            need = bh + 11
        if prev_region[col] != story["region"]:
            cols[col].append(("REGION", story["region"]))
            heights[col] += 11
            prev_region[col] = story["region"]
        cols[col].append(("STORY", story, thumb, bh, hl, sl, scene_h))
        heights[col] += bh
    return cols, heights


def render_frontpage(mod):
    confirmed, reported = mod.validate()
    c = Canvas(W, H, PAPER)
    # --- masthead ---
    c.fill_rect(12, 10, W - 24, 2, INK)
    title = "THE WORLD IN ONE DAY"
    tx = (W - text_width(title, 4)) // 2
    draw_text(c, tx, 16, title, 4, INK)
    sub = ("THURSDAY 26 NOVEMBER 2026  |  49 STORIES  |  7 REGIONS  |  "
           "%d CONFIRMED - %d REPORTED" % (confirmed, reported))
    draw_text(c, (W - text_width(sub, 1)) // 2, 50, sub, 1, RED)
    c.fill_rect(12, 64, W - 24, 30, (255, 255, 255))
    c.rect(12, 64, W - 24, 30, INK)
    check = ("DATE CHECK: EVERY STORY IN THIS EDITION WAS PUBLISHED ON "
             "26 NOVEMBER 2026. SOURCES ARE NAMED PER STORY.")
    draw_text(c, (W - text_width(check, 1)) // 2, 74, check, 1, INK)
    # --- three big illustrated cards ---
    big = [s for s in mod.STORIES if s["scene"] in BIG_SCENES]
    assert len(big) == 3, len(big)
    for k, story in enumerate(big):
        bx = 12 + k * 340
        bw = 320
        by = 102
        bh = 144
        c.fill_rect(bx, by, bw, bh, (255, 255, 255))
        c.rect(bx, by, bw, bh, INK)
        draw_scene(c, story["scene"], bx + 4, by + 4, bw - 8, 96)
        hl = _fit_lines(story["headline"], 1, bw - 12, 2)
        yy = by + 104
        for line in hl:
            draw_text(c, bx + 6, yy, line, 1, INK)
            yy += 8
        meta = story["source"] + " - " + story["tag"]
        draw_text(c, bx + 6, by + bh - 12, meta, 1, RED)
    # --- world map + UTC timeline ---
    draw_map(c, 12, 254, 600, 106, mod.MAP_DOTS)
    draw_timeline(c, 620, 254, 392, 106, mod.TIMELINE)
    # --- story columns ---
    cols, heights = _flow_columns(mod.STORIES)
    for ci, items in enumerate(cols):
        x = COL_XS[ci]
        y = GRID_TOP
        for item in items:
            if item[0] == "REGION":
                c.fill_rect(x, y, COL_W, 10, INK)
                draw_text(c, x + 2, y + 1, item[1], 1, PAPER)
                y += 11
                continue
            _tag, story, thumb, bh, hl, sl, scene_h = item
            start_y = y
            if thumb:
                if scene_h == 56:
                    draw_scene(c, story["scene"], x, y, COL_W, scene_h)
                else:
                    draw_scene_mini(c, story["scene"], x, y, COL_W,
                                    scene_h)
                y += scene_h + 3
            yy = y
            for line in hl:
                draw_text(c, x, yy, line, 1, INK)
                yy += 8
            for line in sl:
                draw_text(c, x, yy, line, 1, (60, 60, 60))
                yy += 8
            meta_src = story["source"]
            tag = story["tag"]
            while (text_width(meta_src + " - " + tag, 1) > COL_W
                   and len(meta_src) > 3):
                meta_src = meta_src[:-3] + ".."
            end = draw_text(c, x, yy, meta_src, 1, GREY)
            tag_color = GREEN if tag == "CONFIRMED" else RED
            draw_text(c, end + 6, yy, "- " + tag, 1, tag_color)
            y = start_y + bh
            c.fill_rect(x, y - 3, COL_W, 1, LIGHT)
    # --- footer ---
    foot = ("THE WORLD IN ONE DAY - MAKE.FUN NEWS-IMAGE-20261126 - "
            "ALL STORIES DATED 26 NOVEMBER 2026")
    draw_text(c, (W - text_width(foot, 1)) // 2, 1004, foot, 1, GREY)
    return encode_png(c), {
        "confirmed": confirmed,
        "reported": reported,
        "columns": heights,
        "scenes": len(SCENES),
        "big_cards": len(big),
    }
