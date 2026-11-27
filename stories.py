# stories.py -- data for THE WORLD IN ONE DAY, Thursday 26 November 2026.
# Every story below was published or reported on 26 November 2026.
# Each summary is 40-55 words, written from the original reporting.
# Tags: CONFIRMED = confirmed by officials or several outlets;
#       REPORTED = reported by one outlet or still developing.

TITLE = ("Thursday 26 November 2026: 54 stories, 11 regions -- "
         "Macy's 100th parade postponed, Riyadh missiles downed, "
         "Tokayev in Moscow, Fiji defence treaties in force")

EDITION_DATE = "Thursday 26 November 2026"
STORY_COUNT = 54
REGION_COUNT = 11

REGIONS = [
    "NORTH AMERICA",
    "CENTRAL AMERICA & CARIBBEAN",
    "SOUTH AMERICA",
    "EUROPE",
    "MIDDLE EAST",
    "AFRICA",
    "CENTRAL ASIA",
    "SOUTH ASIA",
    "EAST ASIA",
    "SOUTHEAST ASIA",
    "OCEANIA & PACIFIC",
]

# Fields: region, headline, source, tag, summary, scene.
# scene names a drawn illustration; "" means no illustration.
STORIES = [
    {
        "region": "NORTH AMERICA",
        "headline": "MACY'S 100TH PARADE POSTPONED BY STORM",
        "source": "REUTERS / CNN",
        "tag": "CONFIRMED",
        "summary": (
            "The 100th Macy's Thanksgiving Day Parade in New York was "
            "postponed for the first time in its history because a major "
            "storm was forecast for Thanksgiving Day. Heavy rain, strong "
            "winds and coastal flooding were expected, with gusts up to 60 "
            "mph. Organisers moved the parade to Saturday 28 November."
        ),
        "scene": "parade",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "TRUMP PROPOSES TARIFFS ON 14 ECONOMIES",
        "source": "REUTERS / USTR",
        "tag": "CONFIRMED",
        "summary": (
            "The Trump administration proposed tariffs on 14 trading "
            "partners, including China, the European Union, Japan, India "
            "and Indonesia, citing excess industrial capacity. Proposed "
            "rates run from 15 percent to 40 percent, with China facing up "
            "to 20 percent, or 40 percent if the trade truce collapses. "
            "A public hearing is set for 25 January 2027."
        ),
        "scene": "tariffs",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "KING TIDES BATTER CALIFORNIA COAST",
        "source": "THE GUARDIAN",
        "tag": "REPORTED",
        "summary": (
            "Exceptional tides and waves nearly nine metres high battered "
            "the California coast on Thursday, flooding low-lying roads "
            "and beaches. The king tides, driven by the alignment of the "
            "moon and sun, coincided with a powerful Pacific swell. "
            "Officials warned beachgoers and drivers to stay clear of "
            "piers and flooded coastal routes as the surge peaked."
        ),
        "scene": "waves",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "FAA GROUND STOP AT MIAMI AFTER FEDEX JET",
        "source": "ASSOCIATED PRESS",
        "tag": "REPORTED",
        "summary": (
            "The Federal Aviation Administration issued a ground stop at "
            "Miami International Airport after an incident involving a "
            "FedEx cargo jet. Departures were held while crews assessed "
            "the aircraft and the runway. The stop rippled through "
            "Thanksgiving holiday schedules, one of the busiest travel "
            "periods of the year in the United States."
        ),
        "scene": "",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "JUDGE: FCC MUST STOP ABC LICENCE REVIEW",
        "source": "DOW JONES / MORNINGSTAR",
        "tag": "REPORTED",
        "summary": (
            "A judge ruled that the Federal Communications Commission "
            "must stop its review of ABC's broadcast licence. The "
            "decision was among the day's top company headlines and "
            "marked a setback for the regulator's attempt to examine the "
            "network. The ruling drew attention because the review had "
            "become entangled in political debate over broadcasters."
        ),
        "scene": "",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "FINCEN SYSTEMS HIT BY CYBER INCIDENT",
        "source": "FINCEN / REPORTS",
        "tag": "REPORTED",
        "summary": (
            "The US Financial Crimes Enforcement Network said a "
            "restricted subset of its systems was affected by a "
            "cybersecurity incident. FinCEN, part of the Treasury, "
            "collects the anti-money-laundering reports filed by banks "
            "and other firms. Officials gave no detail on what was "
            "accessed, and the disclosure added to a year of breaches "
            "across US government systems."
        ),
        "scene": "",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "BLACK FRIDAY DEALS LIVE AS CHIP DASH BITES",
        "source": "DOW JONES / MORNINGSTAR",
        "tag": "REPORTED",
        "summary": (
            "Black Friday deals went live across US retailers as "
            "shoppers faced a shortage of memory chips that is pushing "
            "up prices of phones, laptops and gadgets. Demand for AI "
            "data centres has absorbed chip supply, leaving holiday "
            "buyers competing for scarce stock. Retailers warned that "
            "some popular electronics could sell out early."
        ),
        "scene": "",
    },
    {
        "region": "NORTH AMERICA",
        "headline": "TRUMP AND RUTTE: DO NOT WIDEN UKRAINE WAR",
        "source": "TRUTH SOCIAL / NATO",
        "tag": "CONFIRMED",
        "summary": (
            "President Donald Trump said he told Vladimir Putin during "
            "talks in China that he wants Russia to pull back all "
            "military aggression across Europe so a deal can be reached "
            "quickly. Trump spoke after meeting NATO chief Mark Rutte "
            "at Mar-a-Lago on Wednesday. The two urged Russia to avoid "
            "actions that could expand the war."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "CENTRAL AMERICA & CARIBBEAN",
        "headline": "MEXICO SEEKS TALKS ON SPACEX AIRSPACE USE",
        "source": "REUTERS",
        "tag": "CONFIRMED",
        "summary": (
            "Mexico is seeking a meeting with US aviation authorities "
            "to discuss permits for SpaceX to use Mexican airspace and "
            "potentially relocate its launch activities, President "
            "Claudia Sheinbaum said on Thursday. The request comes amid "
            "growing tensions between Mexico City and Elon Musk's "
            "company over how its rockets cross Mexican skies."
        ),
        "scene": "",
    },
    {
        "region": "CENTRAL AMERICA & CARIBBEAN",
        "headline": "SHEINBAUM BLASTS DEA OVER FENTANYL TIP LINES",
        "source": "ASSOCIATED PRESS",
        "tag": "CONFIRMED",
        "summary": (
            "President Claudia Sheinbaum blasted the US Drug "
            "Enforcement Administration for setting up anonymous tip "
            "lines in Mexico, calling it interference. Citing an AP "
            "investigation, she said the DEA let at least 1.4 million "
            "counterfeit fentanyl pills go unseized during an "
            "eight-month tracking operation, dubbing it the Fast and "
            "Furious of Fentanyl."
        ),
        "scene": "",
    },
    {
        "region": "CENTRAL AMERICA & CARIBBEAN",
        "headline": "JAMAICA CHURCHES CHALLENGE CUBA VOTE SHIFT",
        "source": "CMC / CATHOLICTT",
        "tag": "CONFIRMED",
        "summary": (
            "Jamaica's churches joined criticism of the government's "
            "abstention on the United Nations vote to end the US "
            "embargo on Cuba, breaking more than 30 years of yes votes. "
            "Prime Minister Andrew Holness told Parliament that "
            "Washington sought Jamaica's support but denied any "
            "pressure. Antigua's leader said a US warning changed his "
            "country's position."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "SOUTH AMERICA",
        "headline": "CARTAGENA SIEGE ENDS: 76 HOSTAGES FREED",
        "source": "AFP / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "Colombian security forces stormed an Exito supermarket in "
            "Cartagena and freed all 76 shoppers and staff held for "
            "about 17 hours. One gunman was killed and four arrested. "
            "A rescued hostage told AFP the gunmen drank whisky and "
            "played music while holding the group after a failed "
            "attempt to rob an armoured cash vehicle."
        ),
        "scene": "rescue",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "BRAZIL VOWS NO YIELD TO US TARIFFS",
        "source": "REUTERS / WTO",
        "tag": "CONFIRMED",
        "summary": (
            "Brazil said it will not yield to threats after Washington "
            "proposed new tariffs on Brazilian sugar and aircraft, and "
            "it asked the World Trade Organization for a dispute panel "
            "to review extra US duties. Brasilia said it seeks a "
            "negotiated resolution. Coffee rose more than 6 percent "
            "while Brazil's Bovespa index gained 1.58 percent."
        ),
        "scene": "",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "DOLLAR HITS 19-MONTH HIGH AGAINST BRAZIL REAL",
        "source": "THE RIO TIMES",
        "tag": "REPORTED",
        "summary": (
            "The dollar rose against the Brazilian real for five "
            "straight sessions and reached 5.91 reais on 19 November, "
            "a 19-month high, the day after Brazil's Senate passed the "
            "government's spending package. The bill lowers the cap on "
            "real spending growth from 2.5 percent to 2 percent in "
            "years when spending must be frozen."
        ),
        "scene": "",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "CHILE SENATE APPROVES 2027 BUDGET SECTION",
        "source": "EMOL",
        "tag": "REPORTED",
        "summary": (
            "Chile's Senate approved the Finance Ministry's section of "
            "the 2027 budget by 14 votes to 6 and refused the "
            "government's request to delete one clause. The lower house "
            "had sent the budget to the Senate after rejecting at "
            "least six sections, including Interior, Education and "
            "Culture, three of them on tied votes."
        ),
        "scene": "",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "ARGENTINA BANK LOST $1BN ON GOLD DEALS",
        "source": "THE RIO TIMES",
        "tag": "REPORTED",
        "summary": (
            "Argentina's state audit office says the central bank lost "
            "1.023 billion US dollars on contracts meant to protect "
            "the value of its gold. The figures were carried by The "
            "Rio Times on Thursday. The loss added to scrutiny of the "
            "bank's reserves management as President Javier Milei "
            "pushes a 2027 budget through Congress."
        ),
        "scene": "",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "LATAM STEEL OUTPUT TO RECOVER IN 2026",
        "source": "ALACERO / STEELORBIS",
        "tag": "CONFIRMED",
        "summary": (
            "Latin American crude steel production is expected to rise "
            "3.6 percent to 57.7 million tonnes in 2026 after two "
            "years of decline, the Alacero association said in its "
            "November report. Steel imports are set to hit a record "
            "high despite stronger trade defences. Mexico is forecast "
            "to lead the recovery, with output up 12.5 percent."
        ),
        "scene": "",
    },
    {
        "region": "SOUTH AMERICA",
        "headline": "PERU CONGRESS RATIFIES 2027 BUDGET",
        "source": "MERCO PRESS",
        "tag": "REPORTED",
        "summary": (
            "Peru's two-chamber Congress ratified its 2027 budget of "
            "1,405.4 million soles, close to 450 million soles below "
            "the original proposal. The vote came as Peru's Senate "
            "also elected three directors to the central bank's board. "
            "The budget sets the government's spending plans as the "
            "country heads into an election cycle and slower growth."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "EUROPE",
        "headline": "SPANIARD PICKED TO LEAD EUROPEAN CENTRAL BANK",
        "source": "EUROZONE LEADERS / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "Eurozone leaders chose Spanish economist Pablo Hernandez "
            "de Cos to succeed Christine Lagarde as president of the "
            "European Central Bank. Described as a consensus-builder, "
            "he will take over the institution that sets interest "
            "rates for the euro area. The choice came as EU leaders "
            "also argued in Brussels over the bloc's next budget."
        ),
        "scene": "bank",
    },
    {
        "region": "EUROPE",
        "headline": "UK NET MIGRATION LOWEST SINCE 1997",
        "source": "ONS / THE GUARDIAN",
        "tag": "CONFIRMED",
        "summary": (
            "Net migration to the United Kingdom fell to its lowest "
            "level since 1997, official figures showed. Indians were "
            "the largest foreign group both entering and leaving the "
            "country. The drop reflects tighter visa rules and weaker "
            "demand for overseas workers and students, handing the "
            "government a headline figure it has long promised."
        ),
        "scene": "",
    },
    {
        "region": "EUROPE",
        "headline": "DEPARDIEU TO STAND TRIAL OVER RAPE CLAIM",
        "source": "BBC / COURT",
        "tag": "CONFIRMED",
        "summary": (
            "French actor Gerard Depardieu will stand trial for the "
            "alleged rape of an actress in 2018, a court ruled on "
            "Thursday. The decision sends one of France's most famous "
            "film stars to a criminal trial in a case that has "
            "shadowed his career for years. Depardieu has denied a "
            "string of sexual assault allegations."
        ),
        "scene": "",
    },
    {
        "region": "EUROPE",
        "headline": "DIESEL TANKER CAPSIZES OFF IBIZA, ONE DEAD",
        "source": "ONETURN / SPAIN",
        "tag": "CONFIRMED",
        "summary": (
            "A tanker carrying about 7,000 tonnes of diesel capsized "
            "off Ibiza early on Thursday, and one crew member died. "
            "The Maltese-flagged tanker Med Emre went down in the "
            "Balearic Sea, raising fears of a fuel spill near the "
            "island's coast. Spanish maritime crews worked to contain "
            "the diesel and recover the vessel."
        ),
        "scene": "tanker",
    },
    {
        "region": "EUROPE",
        "headline": "EU LEADERS CLASH OVER 2 TRILLION BUDGET",
        "source": "ONETURN / BRUSSELS",
        "tag": "REPORTED",
        "summary": (
            "European Union leaders met in Brussels and clashed over "
            "the bloc's next long-term budget, which could reach "
            "about 2 trillion euros. The seven-year spending plan "
            "divides richer and poorer members and pits farm and "
            "regional aid against new priorities such as defence and "
            "competitiveness. No deal was expected from the first "
            "round of talks."
        ),
        "scene": "",
    },
    {
        "region": "EUROPE",
        "headline": "NEW UK-EU TREATY HAS 10-YEAR EXIT CLAUSE",
        "source": "BBC",
        "tag": "REPORTED",
        "summary": (
            "A new treaty between the United Kingdom and the European "
            "Union includes a 10-year termination clause, reports "
            "said on Thursday. The clause gives either side a route "
            "out of the agreement after a decade. The treaty is part "
            "of the slow reset of relations since Brexit, covering "
            "trade, security and cooperation between London and "
            "Brussels."
        ),
        "scene": "",
    },
    {
        "region": "EUROPE",
        "headline": "BABCOCK SIGNS RECORD $11.4BN SUB DEAL",
        "source": "DOW JONES / MORNINGSTAR",
        "tag": "CONFIRMED",
        "summary": (
            "Babcock signed a record 11.4 billion dollar contract for "
            "British submarines, the biggest deal in the company's "
            "history. The agreement underpins work at its yards and "
            "the supply chain for the Royal Navy's submarine "
            "programme. It was the standout company headline of the "
            "day as defence spending rose across Europe over the war "
            "in Ukraine."
        ),
        "scene": "",
    },
    {
        "region": "EUROPE",
        "headline": "GERMAN BOAT DEALER FED CHANNEL GANGS: BBC",
        "source": "BBC",
        "tag": "REPORTED",
        "summary": (
            "A German boat dealer is suspected of supplying small "
            "boats to gangs smuggling migrants across the English "
            "Channel, a BBC investigation found. Reporters confronted "
            "the man, who is accused of selling the inflatable boats "
            "used in crossings. The finding puts pressure on German "
            "and British authorities to cut the supply chain."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "MIDDLE EAST",
        "headline": "SAUDI AIR DEFENCES DOWN RIYADH MISSILES",
        "source": "REUTERS / COALITION",
        "tag": "CONFIRMED",
        "summary": (
            "Saudi-led coalition air defences intercepted and "
            "destroyed two ballistic missiles launched toward the "
            "capital Riyadh early on Thursday, and a cruise missile "
            "and drones were also downed. Loud booms were heard "
            "across Riyadh and civil defence issued an alert before "
            "lifting it. The Houthis said they had also struck the "
            "ports of Jeddah and Jazan."
        ),
        "scene": "missile",
    },
    {
        "region": "MIDDLE EAST",
        "headline": "IRAN DRONE ATTACK KILLS TWO ITALIANS IN KUWAIT",
        "source": "BBC / AL JAZEERA",
        "tag": "CONFIRMED",
        "summary": (
            "Two Italian technicians were killed in a drone attack "
            "in Kuwait that Italy and Kuwait blame on Iran, which "
            "denies any role. Italy's foreign ministry confirmed the "
            "deaths on Thursday. The strike raised fears of a "
            "widening conflict as Iran kept threatening the "
            "Strait of Hormuz and the Houthis stepped up attacks on "
            "Saudi Arabia."
        ),
        "scene": "",
    },
    {
        "region": "MIDDLE EAST",
        "headline": "ISRAELI STRIKES KILL NINE IN GAZA",
        "source": "OFFICIALS / AGENCIES",
        "tag": "REPORTED",
        "summary": (
            "Israeli strikes killed nine people in Gaza, including a "
            "Hamas-appointed deputy education minister, officials "
            "said. A Hamas political official and his wife were also "
            "among eight Palestinians killed in separate strikes, "
            "according to reports. The deaths came as US envoy Jared "
            "Kushner urged Israel to move from a wartime mindset "
            "toward economic diplomacy."
        ),
        "scene": "",
    },
    {
        "region": "MIDDLE EAST",
        "headline": "OIL EDGES UP AS HOUTHI THREATS GROW",
        "source": "ONETURN / MARKETS",
        "tag": "REPORTED",
        "summary": (
            "Oil prices edged up as the Houthis stepped up attacks "
            "on Saudi Arabia and Iran kept threatening the Strait of "
            "Hormuz. The Houthis claimed a strike on Ras Tanura, "
            "Saudi Arabia's largest oil refinery, saying it caused "
            "fires at the site, which can process 550,000 barrels a "
            "day. Traders watched the Red Sea for disruption."
        ),
        "scene": "",
    },
    {
        "region": "MIDDLE EAST",
        "headline": "PROTESTS IN IRAQI KURDISTAN OVER OIL PLAN",
        "source": "DEUTSCHE WELLE",
        "tag": "REPORTED",
        "summary": (
            "Protests broke out in Iraqi Kurdistan at plans for the "
            "government in Baghdad to take over oil and border "
            "crossings in the region. Demonstrators said the move "
            "would strip the Kurdish region of its main source of "
            "income and autonomy. The dispute over oil revenue has "
            "long strained relations between Erbil and Baghdad."
        ),
        "scene": "",
    },
    {
        "region": "MIDDLE EAST",
        "headline": "ISRAEL WARNS IRAN BUILDS CHEMICAL ARMS",
        "source": "ISRAEL / REPORTS",
        "tag": "REPORTED",
        "summary": (
            "Israel warned that Iran is crafting a chemical weapons "
            "programme, adding to the drumbeat of accusations between "
            "the two rivals. The warning came amid rising "
            "tension, with Iran blamed for a deadly drone attack in "
            "Kuwait and the Houthis firing missiles at Riyadh. Iran "
            "denies the claims, and no independent evidence was "
            "published."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "AFRICA",
        "headline": "CAIRO TANKER DRIVER HELD AS TOLL HITS 31",
        "source": "REUTERS / FOX NEWS",
        "tag": "CONFIRMED",
        "summary": (
            "Egyptian authorities arrested the driver suspected of "
            "causing a fuel tanker crash in Cairo that killed 31 "
            "people and injured 21. The tanker overturned on the "
            "Ring Road in Giza's Warraq district on Wednesday evening "
            "and burst into flames, destroying 27 vehicles. Lawmakers "
            "demanded accountability as residents mourned the dead."
        ),
        "scene": "fire",
    },
    {
        "region": "AFRICA",
        "headline": "DR CONGO EBOLA CASES PASS 12,000",
        "source": "ONETURN / HEALTH",
        "tag": "CONFIRMED",
        "summary": (
            "Confirmed Ebola cases in the Democratic Republic of "
            "Congo exceeded 12,000, the second-largest outbreak on "
            "record, with deaths near 5,900. Health workers said the "
            "fight is running up against local customs and rites in "
            "remote areas. Kenya's High Court separately ordered a "
            "halt to a US-built Ebola quarantine centre."
        ),
        "scene": "",
    },
    {
        "region": "AFRICA",
        "headline": "DRONE ATTACKS KILL 15 IN SUDAN'S BLUE NILE",
        "source": "ONETURN / SUDAN",
        "tag": "REPORTED",
        "summary": (
            "Drone attacks killed at least 15 people in Sudan's Blue "
            "Nile state, reports said on Thursday. The strikes added "
            "to the misery of a war that has displaced millions and "
            "left the country facing one of the world's worst "
            "humanitarian crises. The African Union backed Ethiopia's "
            "proposal for an inclusive dialogue on the conflict."
        ),
        "scene": "",
    },
    {
        "region": "AFRICA",
        "headline": "CHEAPER HIV PREVENTION JAB REACHES AFRICA",
        "source": "ONETURN / HEALTH",
        "tag": "CONFIRMED",
        "summary": (
            "Cheaper twice-yearly HIV prevention injections are now "
            "reaching Africa, offering hope to millions. Lenacapavir, "
            "given just twice a year, protects against infection and "
            "had been priced out of reach for most African health "
            "systems. Lower-cost supplies mean clinics can now offer "
            "the jab more widely, a step campaigners called a "
            "turning point."
        ),
        "scene": "",
    },
    {
        "region": "AFRICA",
        "headline": "DR CONGO TRIMS COBALT SUPPLY SALES",
        "source": "REPORTS / KINSHASA",
        "tag": "REPORTED",
        "summary": (
            "The Democratic Republic of Congo moved to reduce its "
            "cobalt supply sales, tightening the market for the metal "
            "used in electric vehicle batteries. Congo is the world's "
            "biggest cobalt producer, so any curb ripples through "
            "battery and car supply chains. Traders watched for "
            "detail on how long the limits will last."
        ),
        "scene": "",
    },
    {
        "region": "AFRICA",
        "headline": "RAMAPHOSA WINS COURT BID OVER IMPEACHMENT",
        "source": "EAST AFRICAN REPORT",
        "tag": "REPORTED",
        "summary": (
            "South Africa's President Cyril Ramaphosa won a court "
            "bid over the impeachment report into the 2020 robbery "
            "at his Phala Phala farm. The Western Cape High Court "
            "ruled that the independent panel appointed by parliament "
            "had acted outside its legal authority, rendering its "
            "findings invalid. The ruling handed Ramaphosa a fresh "
            "lifeline."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "CENTRAL ASIA",
        "headline": "TOKAYEV MEETS PUTIN IN MOSCOW, PUSHES AI TIES",
        "source": "VRK / MREAST",
        "tag": "CONFIRMED",
        "summary": (
            "Kazakh President Kassym-Jomart Tokayev met Vladimir "
            "Putin at the Kremlin on Thursday during a working visit "
            "to Moscow, with talks covering trade, investment and "
            "joint projects. Annual trade between the two neighbours "
            "is heading toward 30 billion dollars. Tokayev is also "
            "attending the AI Journey 2026 conference organised by "
            "Sberbank."
        ),
        "scene": "",
    },
    {
        "region": "CENTRAL ASIA",
        "headline": "DEVELOPMENT BANK EYES $3BN FOR UZBEKISTAN",
        "source": "INTERFAX / EDB",
        "tag": "CONFIRMED",
        "summary": (
            "The Eurasian Development Bank could invest up to 3 "
            "billion dollars in Uzbekistan by 2031, including at "
            "least 500 million in 2027, Deputy Prime Minister Jamshid "
            "Khodjaev said on Thursday. The bank signed a memorandum "
            "in Tashkent on developing the New Tashkent district, "
            "with 100 million dollars of projects considered at the "
            "first stage."
        ),
        "scene": "",
    },
    {
        "region": "CENTRAL ASIA",
        "headline": "803 FORGED OFFICIAL IDS SEIZED IN KAZAKHSTAN",
        "source": "VRK / INTERIOR MINISTRY",
        "tag": "REPORTED",
        "summary": (
            "Police in Kazakhstan's Atyrau region seized 803 forged "
            "state agency IDs from a 39-year-old local man, the "
            "Interior Ministry said. Of the fakes, 606 were National "
            "Security Committee IDs and 95 Interior Ministry IDs, "
            "with the rest from the tax service and prosecutors. The "
            "trail began when police stopped a Lexus carrying a "
            "replica pistol."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "SOUTH ASIA",
        "headline": "INDIA MARKS 18 YEARS SINCE 26/11 ATTACKS",
        "source": "IANS / AIR NEWS",
        "tag": "CONFIRMED",
        "summary": (
            "India marked the 18th anniversary of the 26/11 Mumbai "
            "terror attacks, in which 166 people were killed and "
            "more than 300 injured in 2008. President Droupadi Murmu "
            "and minister S. Jaishankar paid tribute, and Mumbai was "
            "placed on high alert. France, Iran and Argentina "
            "expressed solidarity, and Israel's consul general laid "
            "a wreath."
        ),
        "scene": "memorial",
    },
    {
        "region": "SOUTH ASIA",
        "headline": "GUKESH AND SINDAROV DRAW 60-MOVE MARATHON",
        "source": "THE GUARDIAN / FIDE",
        "tag": "CONFIRMED",
        "summary": (
            "Defending champion D. Gukesh and challenger Javokhir "
            "Sindarov drew a 60-move marathon in game three of the "
            "world chess championship in Geneva, leaving the match "
            "level at 1.5-1.5. Sindarov, down to eight seconds at "
            "one point, fought back after nearly five hours. The "
            "youngest title match in history resumes on Saturday."
        ),
        "scene": "chess",
    },
    {
        "region": "SOUTH ASIA",
        "headline": "KARACHI BUILDING COLLAPSE KILLS AT LEAST THREE",
        "source": "NEWSORA24 / AZAAD DIGITAL",
        "tag": "CONFIRMED",
        "summary": (
            "An under-construction building collapsed in Karachi's "
            "Admin Society area, killing at least three people and "
            "injuring 14, with 17 people still missing, Pakistani "
            "outlets reported on Thursday. Sindh Chief Minister Murad "
            "Ali Shah ordered the suspension of eight building "
            "control officials as rescuers searched the rubble for "
            "survivors."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "EAST ASIA",
        "headline": "HONG KONG FIRE: ONE YEAR ON, REPORT SUBMITTED",
        "source": "BBC / SCMP",
        "tag": "CONFIRMED",
        "summary": (
            "A year after the Wang Fuk Court fire killed 168 people, "
            "the independent committee submitted its final report, "
            "finding the blaze was preventable and blaming human "
            "error, safety failures and suspected corruption. The "
            "fire spread at 10 metres a second through "
            "non-fire-retardant scaffolding nets. Two companies and "
            "seven people face 25 charges."
        ),
        "scene": "fire2",
    },
    {
        "region": "EAST ASIA",
        "headline": "ASEAN+3 SET UP DIGITAL PAYMENTS WORKING GROUP",
        "source": "REUTERS",
        "tag": "CONFIRMED",
        "summary": (
            "China, Japan, South Korea and the ASEAN states agreed "
            "in Kyoto to set up a working group on cross-border "
            "payments and digital asset regulation, Reuters reported "
            "on Thursday. Deputies also noted a new emergency "
            "financing mechanism under the Chiang Mai Initiative, "
            "the region's 240 billion dollar currency swap safety "
            "net."
        ),
        "scene": "",
    },
    {
        "region": "EAST ASIA",
        "headline": "CHINA AND JAPAN TRADE SEA WARNINGS",
        "source": "REPORTS / BEIJING",
        "tag": "REPORTED",
        "summary": (
            "China's defence ministry urged Japan to stop stirring "
            "up South China Sea disputes, while Japan called on "
            "Chinese vessels to leave waters near the disputed "
            "Senkaku islands. The exchange underlined how quickly "
            "the two neighbours' maritime rivalry can flare. Both "
            "sides have stepped up patrols around the islands, which "
            "Japan administers and China claims."
        ),
        "scene": "",
    },
]

STORIES += [
    {
        "region": "SOUTHEAST ASIA",
        "headline": "BANGKOK REFINERY BLAST INJURES NINE",
        "source": "AP / CNN",
        "tag": "CONFIRMED",
        "summary": (
            "An explosion and fire at a Bangchak oil refinery in "
            "Bangkok injured at least nine people, three critically, "
            "and forced nearby residents to evacuate briefly. The "
            "blast struck the hydrocracking unit at about 2:45 p.m. "
            "local time and was under control within an hour. "
            "Bangchak shut all units at the 120,000 "
            "barrel a day plant."
        ),
        "scene": "refinery",
    },
    {
        "region": "SOUTHEAST ASIA",
        "headline": "NVIDIA HALTS AI SERVER SHIPMENTS TO SE ASIA",
        "source": "FINANCIAL TIMES / REUTERS",
        "tag": "REPORTED",
        "summary": (
            "Nvidia told manufacturing partners including Dell and "
            "Supermicro to stop shipping AI servers to Malaysia, "
            "Singapore, Thailand and Indonesia, the Financial Times "
            "reported. A new US Commerce rule that took effect on "
            "19 November requires a licence for advanced chip exports "
            "to the four countries. It was unclear whether the halt "
            "is temporary."
        ),
        "scene": "chips",
    },
    {
        "region": "SOUTHEAST ASIA",
        "headline": "MYANMAR SNUBS PARTS OF ICJ GENOCIDE RULING",
        "source": "BBC",
        "tag": "REPORTED",
        "summary": (
            "Myanmar refused to comply with parts of an International "
            "Court of Justice ruling on the genocide case over the "
            "Rohingya, reports said on Thursday. The court's measures "
            "were meant to protect the Rohingya minority after the "
            "2017 crackdown that drove hundreds of thousands into "
            "Bangladesh. The refusal drew criticism from rights "
            "groups."
        ),
        "scene": "",
    },
    {
        "region": "SOUTHEAST ASIA",
        "headline": "13 DEAD AS ILLEGAL GOLD MINE FLOODS IN JAVA",
        "source": "REUTERS / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "Thirteen miners were found dead and 13 more were "
            "trapped after heavy rain flooded an illegal gold mine "
            "in Bogor, West Java. Twenty-six workers were underground "
            "on Monday when a river overflowed into shafts 100 "
            "metres deep. Rescuers resumed the search on Thursday "
            "but heavy rain forced a temporary halt."
        ),
        "scene": "mine",
    },
]

STORIES += [
    {
        "region": "OCEANIA & PACIFIC",
        "headline": "AUSTRALIA-SOLOMONS PACT BLOCKS FOREIGN BASES",
        "source": "THE ASIA LIVE / ABC",
        "tag": "CONFIRMED",
        "summary": (
            "Australia and the Solomon Islands signed a sweeping "
            "security treaty making Australia the island nation's "
            "primary security partner and ruling out foreign military "
            "bases. Honiara must consult Canberra before security "
            "deals with countries outside the Pacific Islands Forum. "
            "Australia committed 740 million Australian dollars over "
            "a decade to health, education and policing."
        ),
        "scene": "treaty",
    },
    {
        "region": "OCEANIA & PACIFIC",
        "headline": "FIJI-AUSTRALIA DEFENCE TREATIES ENTER INTO FORCE",
        "source": "DFAT / AIIA",
        "tag": "CONFIRMED",
        "summary": (
            "Australia and Fiji brought two treaties into force, "
            "announced jointly by prime ministers Anthony Albanese "
            "and Sitiveni Rabuka on Thursday. The Veitacini Treaty "
            "is a mutual defence pact, Fiji's first alliance and "
            "Australia's fourth formal ally. The Vuvale Union, "
            "signed in Suva in July, is backed by more than 1 "
            "billion dollars over a decade."
        ),
        "scene": "",
    },
    {
        "region": "OCEANIA & PACIFIC",
        "headline": "NZ MARCHERS: HANDS OFF CONSERVATION LAND",
        "source": "IPS / GLOBAL ISSUES",
        "tag": "REPORTED",
        "summary": (
            "New Zealanders marched under the slogan Hands off "
            "conservation land, part of a year in which hundreds of "
            "millions of people protested across several continents, "
            "Inter Press Service reported on Thursday. The 2026 wave "
            "of marches was driven by the cost of living, austerity, "
            "the war in Gaza and climate justice."
        ),
        "scene": "",
    },
]

# Timeline of the day, UTC, times verified from the reporting.
TIMELINE = [
    ("03:43", "BBC publishes Wang Fuk Court findings"),
    ("07:45", "Bangkok refinery blast, 2:45 p.m. local"),
    ("08:43", "ASEAN+3 agree payments group in Kyoto"),
    ("13:30", "Macy's step-off time passes; NBC airs rerun"),
    ("14:00", "Gukesh-Sindarov game 3 begins in Geneva"),
    ("16:11", "Mexico seeks talks on SpaceX airspace use"),
    ("19:28", "Trump posts: Putin must pull back in Europe"),
]

# World-map dots: (name, x fraction, y fraction) on the map panel.
MAP_DOTS = [
    ("New York", 0.24, 0.34),
    ("Miami", 0.27, 0.50),
    ("Mexico City", 0.19, 0.52),
    ("Kingston", 0.25, 0.57),
    ("Cartagena", 0.30, 0.62),
    ("Sao Paulo", 0.36, 0.74),
    ("London", 0.47, 0.26),
    ("Madrid", 0.45, 0.36),
    ("Ibiza", 0.47, 0.40),
    ("Kyiv", 0.56, 0.24),
    ("Riyadh", 0.60, 0.46),
    ("Kuwait", 0.62, 0.42),
    ("Cairo", 0.57, 0.44),
    ("Khartoum", 0.59, 0.58),
    ("Kinshasa", 0.56, 0.68),
    ("Astana", 0.69, 0.27),
    ("Tashkent", 0.67, 0.32),
    ("Karachi", 0.66, 0.44),
    ("Mumbai", 0.70, 0.50),
    ("Bangkok", 0.76, 0.54),
    ("Bogor", 0.78, 0.64),
    ("Hong Kong", 0.81, 0.46),
    ("Kyoto", 0.84, 0.33),
    ("Canberra", 0.88, 0.80),
    ("Suva", 0.96, 0.70),
]


def validate():
    """Guard the data contract the renderer relies on."""
    assert len(STORIES) == STORY_COUNT, len(STORIES)
    assert len(REGIONS) == REGION_COUNT, len(REGIONS)
    seen_regions = set()
    confirmed = 0
    for story in STORIES:
        seen_regions.add(story["region"])
        assert story["region"] in REGIONS
        assert story["tag"] in ("CONFIRMED", "REPORTED")
        assert story["source"], story["headline"]
        words = story["summary"].split()
        assert 40 <= len(words) <= 55, (story["headline"], len(words))
        assert story["summary"].isascii(), story["headline"]
        assert story["headline"].isascii()
        if story["tag"] == "CONFIRMED":
            confirmed += 1
    assert seen_regions == set(REGIONS), seen_regions
    return confirmed, len(STORIES) - confirmed
