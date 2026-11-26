# REPORT — news-image-20261126 (morning edition)

## Title

Thursday 26 November 2026: 49 stories, 7 regions - Macy's 100th parade
postponed, Trump hits 14 economies with tariffs, India marks 18 years
since 26/11

## Counts

- 49 stories, 7 regions: North America 8, Latin America 7, Europe 7,
  Middle East 6, Africa 7, Asia-Pacific 8, Science & Culture 6.
- Every story has a written summary of 43-64 words (spec: 40-70).
- Tags: 42 CONFIRMED (C), 7 REPORTED (R).
- 5 illustrated lead stories with cards in `assets/`.

## Five illustrated leads

1. Macy's 100th parade postponed by storm (`assets/macys.png`) — Reuters
2. Trump unveils tariffs on 14 economies (`assets/tariffs.png`) — BBC
3. 76 hostages freed after 17 hours in Cartagena
   (`assets/cartagena.png`) — BBC
4. 31 killed as fuel tanker crashes in Cairo (`assets/cairo.png`) — BBC
5. India marks 18 years since 26/11 Mumbai attacks
   (`assets/mumbai.png`) — Observer Voice

## Date discipline

All 49 stories are dated 26 November 2026 (WIB/UTC) or first reported
overnight into the morning of 26 November 2026, verified against the
source article's own date — not aggregator headlines. Deliberately
excluded: the Hong Kong Wang Fuk Court fire as a fresh event (it was
26 November 2025; today's story is the one-year inquiry report), and
the US Q3 GDP release (published 25 November).

## Verification

- `python3 -P -s main.py` runs clean, stdlib only.
- `entry.png`: 1024x1024, 288,446 bytes (< 1 MiB).
- Determinism: two runs into different directories are byte-identical,
  sha256 `74c59ed72e9e7a0489c36de52f51983da6305c6568d4e97999ecfb363fd6633a`.
- Page visually checked: masthead, dateline, title formula, DATE CHECK
  box, 5-card photo strip, 4 dense columns with headlines, full
  summaries, sources and C/R tags all present.
- README badges: three live make.fun badge URLs included (see README);
  HTTP status checked separately.

## Story table

| # | Region | Headline | Source | Tag |
|---:|---|---|---|---|
| 1 | NA | Macy's 100th parade postponed by storm | Reuters | C |
| 2 | NA | Trump unveils tariffs on 14 economies | BBC | C |
| 3 | NA | Trump accounts traded Nvidia 44 times | BBC | C |
| 4 | NA | S and P puts Nvidia rating on downgrade watch | Reuters | R |
| 5 | NA | Iowa bomb-chemical detonation declared a success | AP | C |
| 6 | NA | Grizzly attack kills mother and daughter in BC | The Guardian | C |
| 7 | NA | Plane crashes into Gulf of Mexico, six aboard | AP | R |
| 8 | NA | Fort Hood survivors lose final execution appeal | AP | C |
| 9 | LATAM | 76 hostages freed after 17 hours in Cartagena | BBC | C |
| 10 | LATAM | Pope Leo returns to his second home in Peru | WH News | C |
| 11 | LATAM | Machado returns to Venezuela after exile | BBC | C |
| 12 | LATAM | Mexico ex-prosecutor charged with treason | BBC | C |
| 13 | LATAM | Argentina left stages March of Anger | Al Jazeera | C |
| 14 | LATAM | Millions without power in Cuba blackout | WH News | R |
| 15 | LATAM | Flavio Bolsonaro leaves Brazil amid passport row | WH News | R |
| 16 | EUR | Russia's own figures show 500,000 war dead | BBC | C |
| 17 | EUR | Russia approves $600bn military budget | EUR Radio | C |
| 18 | EUR | Five Russian jets hit in airfield strike | BBC | C |
| 19 | EUR | EU court rules on caged animals | EUR Radio | C |
| 20 | EUR | 3.7 million European industry jobs at risk | EUR Radio | R |
| 21 | EUR | UK sent sex offender to Eswatini in secret deal | BBC | C |
| 22 | EUR | Real Madrid thump PSV as Arsenal held | BBC Sport | C |
| 23 | ME | Houthis attack Saudi Arabia's Ras Tanura refinery | Observer Voice | C |
| 24 | ME | Two tankers hit mines in Strait of Hormuz | Observer Voice | C |
| 25 | ME | Israel kills Hamas security chief in Gaza | Observer Voice | C |
| 26 | ME | Judges urge dropping top Netanyahu charges | BBC | C |
| 27 | ME | Israel says Iran is building chemical weapons | The Daily Jagran | R |
| 28 | ME | India condemns Riyadh tower attack | SelfStudys | C |
| 29 | AFR | 31 killed as fuel tanker crashes in Cairo | BBC | C |
| 30 | AFR | Five Mexicans held over $227m Nigeria meth lab | BBC | C |
| 31 | AFR | Ramaphosa wins court battle over impeachment | BBC | C |
| 32 | AFR | Nollywood veteran Pete Edochie dies aged 79 | BBC | C |
| 33 | AFR | Zimbabwe warrant for Mugabe's son | BBC | C |
| 34 | AFR | DR Congo military plane missing, rebels claim hit | BBC | R |
| 35 | AFR | Senegal reinstated as Afcon winners by court | BBC | C |
| 36 | APAC | India marks 18 years since 26/11 Mumbai attacks | Observer Voice | C |
| 37 | APAC | India celebrates Constitution Day | SelfStudys | C |
| 38 | APAC | Gukesh faces Sindarov in world title game three | Jagran Josh | C |
| 39 | APAC | India unveils Rs 15,000 crore package for Nepal | SelfStudys | C |
| 40 | APAC | First Pakistani astronaut joins China mission | SelfStudys | C |
| 41 | APAC | Bangladesh garment workers win 36% pay rise | The Daily Jagran | C |
| 42 | APAC | North Korea orders Swiss office to close | SelfStudys | C |
| 43 | APAC | Hong Kong fire inquiry finds failures a year on | BBC | C |
| 44 | SCI | Duran Duran guitarist Andy Taylor dies at 65 | BBC | C |
| 45 | SCI | Gordon Ramsay to host revived Top Gear | BBC | C |
| 46 | SCI | Canadian astronaut welcomes baby from space | BBC | C |
| 47 | SCI | Jolie and Pitt settle winery legal battle | BBC | C |
| 48 | SCI | Wolbachia mosquitoes cut infections 68% in Brazil | StudMentor | C |
| 49 | SCI | India's space economy to hit $45bn in a decade | StudMentor | C |
