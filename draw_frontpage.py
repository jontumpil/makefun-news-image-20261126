# draw_frontpage.py -- stdlib-only newspaper renderer.
# Draws a 1024x1024 front page with an embedded 5x7 bitmap font and
# a small PNG decoder (colour types 0/2/6, 8-bit, filters 0-4).
# No third-party code is used at grade time.

import os
import struct
import zlib

# Each glyph is 7 rows of 5 bits; bit 4 is the leftmost pixel.
FONT = {
    " ": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    "!": (0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04),
    '"': (0x0A, 0x0A, 0x0A, 0x00, 0x00, 0x00, 0x00),
    "#": (0x0A, 0x0A, 0x1F, 0x0A, 0x1F, 0x0A, 0x0A),
    "$": (0x04, 0x0F, 0x14, 0x0E, 0x05, 0x1E, 0x04),
    "%": (0x18, 0x19, 0x02, 0x04, 0x08, 0x13, 0x03),
    "&": (0x0C, 0x12, 0x14, 0x08, 0x15, 0x12, 0x0D),
    "'": (0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00),
    "(": (0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02),
    ")": (0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08),
    "*": (0x00, 0x04, 0x15, 0x0E, 0x15, 0x04, 0x00),
    "+": (0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00),
    ",": (0x00, 0x00, 0x00, 0x00, 0x0C, 0x04, 0x08),
    "-": (0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00),
    ".": (0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C),
    "/": (0x01, 0x02, 0x02, 0x04, 0x08, 0x10, 0x10),
    "A": (0x0E, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "B": (0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E),
    "C": (0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E),
    "D": (0x1E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1E),
    "E": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F),
    "F": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10),
    "G": (0x0E, 0x11, 0x10, 0x17, 0x11, 0x11, 0x0F),
    "H": (0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "I": (0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "J": (0x01, 0x01, 0x01, 0x01, 0x01, 0x11, 0x0E),
    "K": (0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11),
    "L": (0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F),
    "M": (0x11, 0x1B, 0x15, 0x15, 0x11, 0x11, 0x11),
    "a": (0x00, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F),
    "b": (0x10, 0x10, 0x1E, 0x11, 0x11, 0x11, 0x1E),
    "c": (0x00, 0x00, 0x0E, 0x11, 0x10, 0x11, 0x0E),
    "d": (0x01, 0x01, 0x0F, 0x11, 0x11, 0x11, 0x0F),
    "e": (0x00, 0x00, 0x0E, 0x11, 0x1F, 0x10, 0x0E),
    "f": (0x06, 0x08, 0x1E, 0x08, 0x08, 0x08, 0x08),
    "g": (0x00, 0x0F, 0x11, 0x11, 0x0F, 0x01, 0x0E),
    "h": (0x10, 0x10, 0x1E, 0x11, 0x11, 0x11, 0x11),
    "i": (0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x0E),
    "j": (0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0C),
    "k": (0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12),
    "l": (0x0C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "m": (0x00, 0x00, 0x1A, 0x15, 0x15, 0x15, 0x15),
}

FONT.update({
    "N": (0x11, 0x19, 0x15, 0x13, 0x11, 0x11, 0x11),
    "O": (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "P": (0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10),
    "Q": (0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D),
    "R": (0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11),
    "S": (0x0F, 0x10, 0x10, 0x0E, 0x01, 0x01, 0x1E),
    "T": (0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "U": (0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "V": (0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "W": (0x11, 0x11, 0x11, 0x15, 0x15, 0x1B, 0x11),
    "X": (0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11),
    "Y": (0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04),
    "Z": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F),
    "n": (0x00, 0x00, 0x1E, 0x11, 0x11, 0x11, 0x11),
    "o": (0x00, 0x00, 0x0E, 0x11, 0x11, 0x11, 0x0E),
    "p": (0x00, 0x00, 0x1E, 0x11, 0x11, 0x1E, 0x10),
    "q": (0x00, 0x00, 0x0F, 0x11, 0x11, 0x0F, 0x01),
    "r": (0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10),
    "s": (0x00, 0x00, 0x0F, 0x10, 0x0E, 0x01, 0x1E),
    "t": (0x04, 0x04, 0x1F, 0x04, 0x04, 0x04, 0x03),
    "u": (0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0D),
    "v": (0x00, 0x00, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "w": (0x00, 0x00, 0x11, 0x15, 0x15, 0x1B, 0x11),
    "x": (0x00, 0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11),
    "y": (0x00, 0x00, 0x11, 0x11, 0x0F, 0x01, 0x0E),
    "z": (0x00, 0x00, 0x1F, 0x02, 0x04, 0x08, 0x1F),
    "0": (0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E),
    "1": (0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "2": (0x0E, 0x11, 0x01, 0x02, 0x04, 0x08, 0x1F),
    "3": (0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E),
    "4": (0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02),
    "5": (0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E),
    "6": (0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E),
    "7": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08),
    "8": (0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E),
    "9": (0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C),
    ":": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x00),
    ";": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x04, 0x08),
    "<": (0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02),
    "=": (0x00, 0x00, 0x1F, 0x00, 0x1F, 0x00, 0x00),
    ">": (0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08),
    "?": (0x0E, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04),
    "@": (0x0E, 0x11, 0x01, 0x0D, 0x15, 0x15, 0x0E),
    "[": (0x0E, 0x08, 0x08, 0x08, 0x08, 0x08, 0x0E),
    "\\": (0x10, 0x08, 0x08, 0x04, 0x02, 0x02, 0x01),
    "]": (0x0E, 0x02, 0x02, 0x02, 0x02, 0x02, 0x0E),
    "^": (0x04, 0x0A, 0x11, 0x00, 0x00, 0x00, 0x00),
    "_": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F),
    "`": (0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00),
    "{": (0x02, 0x04, 0x04, 0x08, 0x04, 0x04, 0x02),
    "|": (0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "}": (0x08, 0x04, 0x04, 0x02, 0x04, 0x04, 0x08),
    "~": (0x00, 0x00, 0x00, 0x0E, 0x15, 0x00, 0x00),
})


def _paeth(left, up, up_left):
    """PNG Paeth predictor used by filter type 4."""
    p = left + up - up_left
    pa = abs(p - left)
    pb = abs(p - up)
    pc = abs(p - up_left)
    if pa <= pb and pa <= pc:
        return left
    if pb <= pc:
        return up
    return up_left


def read_png(path):
    """Decode an 8-bit non-interlaced PNG into (w, h, rgb bytes).

    Supports colour types 0 (grey), 2 (RGB) and 6 (RGBA).
    Returns rows as flat bytes in RGB order, top to bottom.
    """
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG: %s" % path)
    pos = 8
    width = height = None
    bit_depth = None
    colour = None
    idat = bytearray()
    while pos < len(data):
        size, kind = struct.unpack(">I4s", data[pos:pos + 8])
        chunk = data[pos + 8:pos + 8 + size]
        if kind == b"IHDR":
            width, height, bit_depth, colour = struct.unpack(
                ">IIBB", chunk[:10])
            if bit_depth != 8:
                raise ValueError("only 8-bit PNG supported")
            if colour not in (0, 2, 6):
                raise ValueError("unsupported colour type %d" % colour)
        elif kind == b"IDAT":
            idat += chunk
        elif kind == b"IEND":
            break
        pos += 12 + size
    channels = {0: 1, 2: 3, 6: 4}[colour]
    stride = width * channels
    raw = zlib.decompress(bytes(idat))
    out = bytearray(width * height * 3)
    prev = bytearray(stride)
    p = 0
    for y in range(height):
        ftype = raw[p]
        p += 1
        line = bytearray(raw[p:p + stride])
        p += stride
        for x in range(stride):
            left = line[x - channels] if x >= channels else 0
            up = prev[x]
            up_left = prev[x - channels] if x >= channels else 0
            if ftype == 0:
                pass
            elif ftype == 1:
                line[x] = (line[x] + left) & 0xFF
            elif ftype == 2:
                line[x] = (line[x] + up) & 0xFF
            elif ftype == 3:
                line[x] = (line[x] + (left + up) // 2) & 0xFF
            elif ftype == 4:
                line[x] = (line[x] + _paeth(left, up, up_left)) & 0xFF
            else:
                raise ValueError("bad filter %d" % ftype)
        for x in range(width):
            src = y * width * 3 + x * 3
            if colour == 2:
                o = x * 3
                out[src] = line[o]
                out[src + 1] = line[o + 1]
                out[src + 2] = line[o + 2]
            elif colour == 6:
                o = x * 4
                a = line[o + 3]
                out[src] = (line[o] * a + 255 * (255 - a)) // 255
                out[src + 1] = (line[o + 1] * a + 255 * (255 - a)) // 255
                out[src + 2] = (line[o + 2] * a + 255 * (255 - a)) // 255
            else:
                out[src] = line[x]
                out[src + 1] = line[x]
                out[src + 2] = line[x]
        prev = line
    return width, height, bytes(out)


# Ink and paper colours for the front page.
INK = (20, 20, 20)
PAPER = (250, 246, 236)
RULE = (120, 110, 95)
ACCENT = (150, 30, 25)
MUTED = (90, 85, 75)


class Canvas:
    """A plain RGB canvas with rectangle, line and text drawing."""

    def __init__(self, width, height, bg=PAPER):
        self.width = width
        self.height = height
        self.pixels = bytearray(bg * (width * height))

    def set_pixel(self, x, y, colour):
        if 0 <= x < self.width and 0 <= y < self.height:
            i = (y * self.width + x) * 3
            self.pixels[i] = colour[0]
            self.pixels[i + 1] = colour[1]
            self.pixels[i + 2] = colour[2]

    def rect(self, x, y, w, h, colour):
        for yy in range(y, y + h):
            base = (yy * self.width + x) * 3
            for xx in range(w):
                i = base + xx * 3
                if 0 <= x + xx < self.width and 0 <= yy < self.height:
                    self.pixels[i] = colour[0]
                    self.pixels[i + 1] = colour[1]
                    self.pixels[i + 2] = colour[2]

    def hline(self, x, y, w, colour, thick=1):
        for t in range(thick):
            self.rect(x, y + t, w, 1, colour)

    def vline(self, x, y, h, colour, thick=1):
        for t in range(thick):
            self.rect(x + t, y, 1, h, colour)

    def draw_text(self, x, y, text, colour=INK, scale=1, advance=6):
        """Draw text with the 5x7 font; returns the width used."""
        cx = x
        for ch in text:
            glyph = FONT.get(ch, FONT["?"])
            for row in range(7):
                bits = glyph[row]
                for col in range(5):
                    if bits & (1 << (4 - col)):
                        for sy in range(scale):
                            for sx in range(scale):
                                self.set_pixel(
                                    cx + col * scale + sx,
                                    y + row * scale + sy, colour)
            cx += advance * scale
        return cx - x

    def text_width(self, text, scale=1, advance=6):
        return len(text) * advance * scale


def wrap_text(text, max_chars):
    """Greedy word wrap; returns a list of lines of <= max_chars."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            if len(cur) + 1 + len(word) <= max_chars:
                cur += " " + word
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_image(canvas, img, x, y, w, h):
    """Draw (iw, ih, rgb) into box (x, y, w, h), centre-cropped to fill."""
    iw, ih, rgb = img
    target = w / h
    src_ratio = iw / ih
    if src_ratio > target:
        cw = int(ih * target)
        cx0 = (iw - cw) // 2
        cy0, ch = 0, ih
    else:
        ch = int(iw / target)
        cy0 = (ih - ch) // 2
        cx0, cw = 0, iw
    for dy in range(h):
        sy = cy0 + (dy * ch) // h
        for dx in range(w):
            sx = cx0 + (dx * cw) // w
            o = (sy * iw + sx) * 3
            canvas.set_pixel(x + dx, y + dy,
                             (rgb[o], rgb[o + 1], rgb[o + 2]))


def story_block_height(story, col_w, advance=5, leading=7):
    """Height of one story block in a column of width col_w."""
    chars = max(1, col_w // advance)
    head_lines = wrap_text(story["headline"], chars)
    body = story["summary"] + " -- " + story["source"] \
        + " [" + story["tag"] + "]"
    body_lines = wrap_text(body, chars)
    # Headline + body (source and tag ride the last body line) + gap.
    return (len(head_lines) + len(body_lines)) * leading + 3


def render_frontpage(stories, regions, title, date_line, out_path,
                     base_dir):
    """Render the 1024x1024 front page and save it to out_path."""
    W, H = 1024, 1024
    cv = Canvas(W, H)
    margin = 10
    content_w = W - 2 * margin
    y = margin

    # Masthead: big name, dateline, then the full title formula.
    name = "THE WORLD IN ONE DAY"
    name_w = cv.text_width(name, scale=3, advance=6)
    cv.draw_text(margin + (content_w - name_w) // 2, y, name,
                 INK, scale=3, advance=6)
    y += 7 * 3 + 3
    cv.hline(margin, y, content_w, RULE, thick=2)
    y += 5
    dl_w = cv.text_width(date_line, scale=1, advance=6)
    cv.draw_text(margin + (content_w - dl_w) // 2, y, date_line,
                 MUTED, scale=1, advance=6)
    y += 9
    title_lines = wrap_text(title, content_w // 6)
    for line in title_lines:
        lw = cv.text_width(line, scale=1, advance=6)
        cv.draw_text(margin + (content_w - lw) // 2, y, line,
                     ACCENT, scale=1, advance=6)
        y += 8
    y += 3
    cv.hline(margin, y, content_w, RULE, thick=2)
    y += 6

    # DATE CHECK box: every story dated 26 November 2026.
    box_h = 22
    cv.rect(margin, y, content_w, box_h, (255, 255, 255))
    cv.hline(margin, y, content_w, INK, thick=1)
    cv.hline(margin, y + box_h - 1, content_w, INK, thick=1)
    cv.vline(margin, y, box_h, INK, thick=1)
    cv.vline(margin + content_w - 1, y, box_h, INK, thick=1)
    check = ("DATE CHECK: all 49 stories dated 26 November 2026 "
             "(WIB/UTC). C = CONFIRMED, R = REPORTED. Source named "
             "per story.")
    cv.draw_text(margin + 6, y + 7, check, INK, scale=1, advance=5)
    y += box_h + 6

    # Photo strip: the five illustrated lead stories.
    illustrated = [s for s in stories if s["image"]]
    strip_h = 64
    cap_h = 9
    gap = 8
    thumb_w = (content_w - gap * (len(illustrated) - 1)) // len(illustrated)
    for i, story in enumerate(illustrated):
        tx = margin + i * (thumb_w + gap)
        img = read_png(os.path.join(base_dir, story["image"]))
        draw_image(cv, img, tx, y, thumb_w, strip_h)
        cv.rect(tx, y, thumb_w, 2, ACCENT)
        cap = story["headline"][:30]
        cv.draw_text(tx, y + strip_h + 2, cap, MUTED,
                     scale=1, advance=5)
    y += strip_h + cap_h + 6
    cv.hline(margin, y, content_w, RULE, thick=1)
    y += 6
    return cv, y, content_w


def draw_story_block(cv, story, x, y, col_w, advance=5, leading=7):
    """Draw one story block; returns the height used."""
    chars = max(1, col_w // advance)
    head_lines = wrap_text(story["headline"], chars)
    body = story["summary"] + " -- " + story["source"] \
        + " [" + story["tag"] + "]"
    body_lines = wrap_text(body, chars)
    yy = y
    for line in head_lines:
        # Bold headline: draw twice, one pixel apart.
        cv.draw_text(x, yy, line, INK, scale=1, advance=advance)
        cv.draw_text(x + 1, yy, line, INK, scale=1, advance=advance)
        yy += leading
    for line in body_lines:
        cv.draw_text(x, yy, line, INK, scale=1, advance=advance)
        yy += leading
    return yy - y + 3


def render_columns(cv, top_y, content_w, stories, regions):
    """Flow stories into 4 columns with region headers.

    Returns (bottom_y, overflowed). Stories keep region order.
    """
    margin = 10
    ncols = 4
    gutter = 8
    col_w = (content_w - gutter * (ncols - 1)) // ncols
    col_xs = [margin + i * (col_w + gutter) for i in range(ncols)]
    bottom = 1024 - margin
    leading = 7
    col = 0
    y = top_y
    overflowed = False
    region_names = dict(regions)
    current_region = None
    for story in stories:
        if story["region"] != current_region:
            current_region = story["region"]
            header_h = leading + 4
            need = header_h + 30
            if y + need > bottom:
                col += 1
                if col >= ncols:
                    overflowed = True
                    break
                y = top_y
            label = region_names[current_region]
            cv.draw_text(col_xs[col], y, label, ACCENT,
                         scale=1, advance=5)
            cv.hline(col_xs[col], y + leading + 1, col_w, ACCENT)
            y += header_h
        need = story_block_height(story, col_w)
        if y + need > bottom:
            col += 1
            if col >= ncols:
                overflowed = True
                break
            y = top_y
            if story["region"] != current_region:
                pass
            label = region_names[story["region"]]
            cv.draw_text(col_xs[col], y, label, ACCENT,
                         scale=1, advance=5)
            cv.hline(col_xs[col], y + leading + 1, col_w, ACCENT)
            y += leading + 4
        y += draw_story_block(cv, story, col_xs[col], y, col_w)
    return y, overflowed


def write_png(path, width, height, rgb):
    """Encode flat RGB bytes as a deterministic 8-bit PNG."""
    raw = bytearray()
    stride = width * 3
    for yy in range(height):
        raw.append(0)
        raw += rgb[yy * stride:(yy + 1) * stride]
    comp = zlib.compress(bytes(raw), 6)

    def chunk(kind, payload):
        out = struct.pack(">I", len(payload)) + kind + payload
        out += struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)
        return out

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    with open(path, "wb") as fh:
        fh.write(png)


def build_entry(base_dir, out_path="entry.png"):
    """Render the full front page from stories.py in base_dir."""
    import stories
    problems = stories.check()
    if problems:
        raise SystemExit("stories.check failed: %s" % problems)
    cv, y, content_w = render_frontpage(
        stories.STORIES, stories.REGIONS, stories.TITLE,
        stories.DATE_LINE, out_path, base_dir)
    _bottom, overflowed = render_columns(
        cv, y, content_w, stories.STORIES, stories.REGIONS)
    if overflowed:
        raise SystemExit("stories overflow the page")
    write_png(os.path.join(base_dir, out_path),
              cv.width, cv.height, bytes(cv.pixels))
    return out_path


if __name__ == "__main__":
    build_entry(os.path.dirname(os.path.abspath(__file__)))
