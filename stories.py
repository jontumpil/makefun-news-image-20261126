# stories.py -- data for THE WORLD IN ONE DAY, 26 November 2026.
# Every story is dated 26 November 2026 (WIB/UTC) or first reported
# overnight into the morning of 26 November 2026. Each story carries a
# written summary of 40-70 words drawn from its source article.
# Tags: C = CONFIRMED, R = REPORTED.

TITLE = ("Thursday 26 November 2026: 49 stories, 7 regions - "
         "Macy's 100th parade postponed, Trump hits 14 economies "
         "with tariffs, India marks 18 years since 26/11")

DATE_LINE = "Thursday 26 November 2026 | Morning edition | 49 stories"

REGIONS = [
    ("NA", "NORTH AMERICA"),
    ("LATAM", "LATIN AMERICA"),
    ("EUR", "EUROPE"),
    ("ME", "MIDDLE EAST"),
    ("AFR", "AFRICA"),
    ("APAC", "ASIA-PACIFIC"),
    ("SCI", "SCIENCE & CULTURE"),
]

# Each story: region, headline, summary, source, tag, image or "".
STORIES = [
    {
        "region": "NA",
        "headline": "Macy's 100th parade postponed by storm",
        "summary": ("The 100th Macy's Thanksgiving Day Parade in New York "
                    "will move to Saturday, November 28, after forecasters "
                    "warned of heavy rain and winds gusting to 60 mph. It "
                    "is the first weather postponement in the parade's "
                    "century-long history; it was only suspended during "
                    "World War Two from 1942 to 1944. Balloons will be "
                    "deflated on Wednesday night and re-inflated for "
                    "Saturday's 8:30 a.m. step-off."),
        "source": "Reuters",
        "tag": "C",
        "image": "assets/macys.png",
    },
    {
        "region": "NA",
        "headline": "Trump unveils tariffs on 14 economies",
        "summary": ("President Donald Trump announced proposed tariffs on "
                    "14 economies, including China, the European Union and "
                    "India, in a Thanksgiving-eve move to replace levies "
                    "struck down by the Supreme Court. China faces 20 "
                    "percent, rising to 40 percent if trade talks "
                    "collapse; the EU faces 15 percent and India 25 "
                    "percent. The measures could take effect in January."),
        "source": "BBC",
        "tag": "C",
        "image": "assets/tariffs.png",
    },
    {
        "region": "NA",
        "headline": "Trump accounts traded Nvidia 44 times",
        "summary": ("Records show accounts linked to President Donald "
                    "Trump traded Nvidia shares 44 times this year, "
                    "raising fresh questions about conflicts of interest "
                    "as the White House weighs chip policy. The trades "
                    "came as Nvidia stock swung sharply and the "
                    "administration debated export controls. The White "
                    "House has not explained the timing of the "
                    "transactions."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "NA",
        "headline": "S and P puts Nvidia rating on downgrade watch",
        "summary": ("S and P warned that Nvidia's board may be "
                    "compromised and placed the chipmaker's credit rating "
                    "on downgrade watch, rattling investors already "
                    "nervous about artificial intelligence valuations. "
                    "Shares fell in early trading as all three main US "
                    "stock indexes declined. Nvidia is the world's most "
                    "valuable company and a bellwether for the AI boom."),
        "source": "Reuters",
        "tag": "R",
        "image": "",
    },
]

STORIES += [
    {
        "region": "NA",
        "headline": "Iowa bomb-chemical detonation declared a success",
        "summary": ("The US Army said the controlled detonation of bomb "
                    "chemicals in Iowa was a success, after earlier fears "
                    "that the blast could release a toxic plume over "
                    "nearby communities. Engineers had warned residents "
                    "to stay indoors while the ageing stockpile was "
                    "destroyed. Officials said air monitoring showed no "
                    "dangerous release during the operation."),
        "source": "AP",
        "tag": "C",
        "image": "",
    },
    {
        "region": "NA",
        "headline": "Grizzly attack kills mother and daughter in BC",
        "summary": ("A 20-year-old woman and her mother were killed in a "
                    "suspected grizzly bear attack in British Columbia, "
                    "conservation officers confirmed. Multiple bears were "
                    "involved in the attack, which took place in a remote "
                    "area of the province. Officers are tracking the "
                    "animals and have warned residents to avoid the "
                    "region while the investigation continues."),
        "source": "The Guardian",
        "tag": "C",
        "image": "",
    },
    {
        "region": "NA",
        "headline": "Plane crashes into Gulf of Mexico, six aboard",
        "summary": ("Crews are searching for six people aboard a small "
                    "plane that crashed into the Gulf of Mexico, the US "
                    "Coast Guard said. The aircraft went down off the "
                    "coast and rescue boats and aircraft were sent to the "
                    "area. Officials have not said what caused the crash "
                    "or released the identities of those on board."),
        "source": "AP",
        "tag": "R",
        "image": "",
    },
    {
        "region": "NA",
        "headline": "Fort Hood survivors lose final execution appeal",
        "summary": ("Three survivors of the Fort Hood shooting lost their "
                    "final appeal to witness the execution of gunman "
                    "Nidal Hasan, a court ruled. The survivors had asked "
                    "to be present when the sentence is carried out, "
                    "arguing they had a right to see justice done. The "
                    "ruling ends a long legal battle over victim access "
                    "to military executions."),
        "source": "AP",
        "tag": "C",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "76 hostages freed after 17 hours in Cartagena",
        "summary": ("Colombian police stormed a supermarket in Cartagena "
                    "and freed 76 people held hostage for 17 hours after "
                    "an armed gang's attempt to rob an armoured cash "
                    "truck went wrong. One gunman was killed in the "
                    "operation, which the president described as a "
                    "robbery gone wrong. The hostages were released "
                    "unharmed after a tense overnight standoff."),
        "source": "BBC",
        "tag": "C",
        "image": "assets/cartagena.png",
    },
    {
        "region": "LATAM",
        "headline": "Pope Leo returns to his second home in Peru",
        "summary": ("Pope Leo made an emotional return to his former "
                    "diocese of Chiclayo in Peru, where large crowds "
                    "welcomed their former bishop exactly one month after "
                    "he had lung cancer surgery. He thanked the crowds "
                    "for their support during his recovery. The visit to "
                    "the city he calls his second home was his first "
                    "major trip since the operation."),
        "source": "WH News",
        "tag": "C",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "Machado returns to Venezuela after exile",
        "summary": ("Venezuelan opposition leader Maria Corina Machado "
                    "returned to the country after nearly a year in "
                    "exile, announcing her arrival with the message, I "
                    "am here. With you. The Nobel laureate returns to a "
                    "country transformed by the Trump administration's "
                    "policies. Supporters gathered to welcome her back "
                    "after ten months away."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "Mexico ex-prosecutor charged with treason",
        "summary": ("Federal prosecutors in Mexico charged a former state "
                    "prosecutor with treason for allowing US agents to "
                    "join a raid on a suspected drugs lab in April "
                    "without proper authorisation. The case tests the "
                    "limits of security cooperation between the two "
                    "countries. Officials said the unauthorised raid "
                    "breached Mexican sovereignty."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "Argentina left stages March of Anger",
        "summary": ("Thousands of protesters marched through Buenos Aires "
                    "as Argentina's left-wing groups demonstrated against "
                    "President Javier Milei's austerity measures. The "
                    "March of Anger brought unions and social movements "
                    "together in the capital's streets. Organisers said "
                    "spending cuts have pushed more families into "
                    "poverty across the country."),
        "source": "Al Jazeera",
        "tag": "C",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "Millions without power in Cuba blackout",
        "summary": ("Millions of Cubans remain without electricity after "
                    "a nationwide blackout triggered by fuel shortages "
                    "and an ageing power grid. The outage is the latest "
                    "in a series of major failures that have hit the "
                    "island this year. Authorities are working to restore "
                    "power, but have given no timetable for full "
                    "recovery."),
        "source": "WH News",
        "tag": "R",
        "image": "",
    },
    {
        "region": "LATAM",
        "headline": "Flavio Bolsonaro leaves Brazil amid passport row",
        "summary": ("Flavio Bolsonaro, the defeated Brazilian presidential "
                    "candidate, has left Brazil for the United States "
                    "after his passport was cancelled. US officials said "
                    "they will issue visas to him and his family. His "
                    "departure follows his election loss and deepens the "
                    "political crisis in Latin America's largest "
                    "economy."),
        "source": "WH News",
        "tag": "R",
        "image": "",
    },
]

STORIES += [
    {
        "region": "EUR",
        "headline": "Russia's own figures show 500,000 war dead",
        "summary": ("Russia's own official figures show it has lost "
                    "nearly 500,000 people in the war in Ukraine, a "
                    "staggering toll that underlines the human cost of "
                    "the conflict. The numbers, drawn from state records, "
                    "are far higher than Moscow has publicly admitted. "
                    "Analysts say the true figure may be higher still, "
                    "as many deaths go unrecorded."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "Russia approves $600bn military budget",
        "summary": ("Russia has approved a military budget exceeding 600 "
                    "billion dollars for the 2027-29 period, signalling "
                    "President Vladimir Putin's ongoing commitment to the "
                    "war in Ukraine. The huge allocation dwarfs spending "
                    "on health and education. Western officials say the "
                    "budget shows Moscow is preparing for a long "
                    "conflict."),
        "source": "EUR Radio",
        "tag": "C",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "Five Russian jets hit in airfield strike",
        "summary": ("Ukraine said five Russian military jets were hit in "
                    "a strike on an airfield, in the latest long-range "
                    "attack on Russian air power. Kyiv has stepped up "
                    "strikes on airbases used to launch attacks on "
                    "Ukrainian cities. Russia has not confirmed the "
                    "losses, but satellite images are expected to show "
                    "the damage."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "EU court rules on caged animals",
        "summary": ("The EU Court issued a ruling on caged animals that "
                    "could reshape farming across the bloc, in a case "
                    "closely watched by animal welfare groups. The court "
                    "weighed the welfare of farm animals against the "
                    "costs faced by producers. Campaigners called the "
                    "decision a step towards ending cages, while farming "
                    "lobbies warned of higher food prices."),
        "source": "EUR Radio",
        "tag": "C",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "3.7 million European industry jobs at risk",
        "summary": ("Some 3.7 million jobs are at risk in European "
                    "industry as factories face high energy costs, "
                    "competition from China and new US tariffs, a report "
                    "warns. Steel, chemicals and carmaking are among the "
                    "hardest-hit sectors. Unions are demanding state aid "
                    "and cheaper power to keep plants open."),
        "source": "EUR Radio",
        "tag": "R",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "UK sent sex offender to Eswatini in secret deal",
        "summary": ("The UK sent a sex offender refugee to Eswatini under "
                    "an undisclosed deal, it has emerged, raising "
                    "questions about Britain's use of third countries to "
                    "remove migrants. The arrangement was not announced "
                    "to parliament. Critics called it a secret "
                    "deportation pipeline, while ministers defended the "
                    "deal as lawful."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "EUR",
        "headline": "Real Madrid thump PSV as Arsenal held",
        "summary": ("Jude Bellingham scored a wondergoal as Real Madrid "
                    "thumped PSV in the Champions League, while Arsenal "
                    "and Manchester City were both held on a dramatic "
                    "night. Liverpool beat Club Brugge as Alexander Isak "
                    "scored twice, and Roma held Paris St-Germain thanks "
                    "to Donyell Malen's fourth straight game with a "
                    "goal."),
        "source": "BBC Sport",
        "tag": "C",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "Houthis attack Saudi Arabia's Ras Tanura refinery",
        "summary": ("Yemen's Iran-aligned Houthis said they had attacked "
                    "Saudi Arabia's Ras Tanura oil refinery, with the "
                    "attack causing fires at the giant export terminal. "
                    "The strike is the latest escalation in the region's "
                    "shadow war over shipping and energy. Saudi "
                    "authorities have not confirmed the scale of the "
                    "damage."),
        "source": "Observer Voice",
        "tag": "C",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "Two tankers hit mines in Strait of Hormuz",
        "summary": ("Iran's Islamic Revolutionary Guard Corps Navy said "
                    "two oil tankers struck naval mines and exploded "
                    "while attempting to cross the Strait of Hormuz "
                    "through an unauthorised route, with the tankers "
                    "catching fire in their engine rooms. The strait "
                    "carries a fifth of the world's oil, and any "
                    "closure would send prices soaring."),
        "source": "Observer Voice",
        "tag": "C",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "Israel kills Hamas security chief in Gaza",
        "summary": ("Israel's military killed Mohammad Abuelouf, a Hamas "
                    "colonel who heads the militants' interior security "
                    "service, as well as Abuelouf's wife and two "
                    "children, according to Gaza's Hamas-run interior "
                    "ministry and medics. The strike puts the fragile "
                    "ceasefire under fresh strain as mediators scramble "
                    "to keep the truce alive."),
        "source": "Observer Voice",
        "tag": "C",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "Judges urge dropping top Netanyahu charges",
        "summary": ("Israeli judges recommended dropping the most serious "
                    "charges against Prime Minister Benjamin Netanyahu in "
                    "his long-running corruption trial, in a major "
                    "development for the embattled leader. Prosecutors "
                    "have yet to say whether they will accept the "
                    "recommendation. The trial has divided Israeli "
                    "politics for years."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "Israel says Iran is building chemical weapons",
        "summary": ("Israel's defence minister said Iran is developing "
                    "chemical weapons, in a claim that adds to tensions "
                    "between the two rivals. Tehran denies pursuing "
                    "weapons of mass destruction and says its programme "
                    "is peaceful. The accusation comes as regional "
                    "powers trade warnings over the Strait of Hormuz and "
                    "the war in Gaza."),
        "source": "The Daily Jagran",
        "tag": "R",
        "image": "",
    },
    {
        "region": "ME",
        "headline": "India condemns Riyadh tower attack",
        "summary": ("India's foreign ministry condemned an attack on a "
                    "tower in Riyadh's financial district in Saudi "
                    "Arabia after two Indians were injured. The ministry "
                    "said it was in close contact with Saudi authorities "
                    "and the injured citizens. The attack is the latest "
                    "sign of rising regional tensions spilling into Gulf "
                    "cities."),
        "source": "SelfStudys",
        "tag": "C",
        "image": "",
    },
]

STORIES += [
    {
        "region": "AFR",
        "headline": "31 killed as fuel tanker crashes in Cairo",
        "summary": ("Thirty-one people were killed in a massive fire "
                    "after a fuel tanker crashed on a highway in Cairo, "
                    "officials said. The tanker overturned and exploded, "
                    "engulfing nearby vehicles in flames. Emergency "
                    "crews battled the blaze for hours, and hospitals "
                    "treated dozens of injured survivors."),
        "source": "BBC",
        "tag": "C",
        "image": "assets/cairo.png",
    },
    {
        "region": "AFR",
        "headline": "Five Mexicans held over $227m Nigeria meth lab",
        "summary": ("Five Mexicans were arrested in Nigeria over a meth "
                    "laboratory worth 227 million dollars, in one of the "
                    "country's biggest drug busts. The lab was producing "
                    "methamphetamine for export, officials said. The "
                    "arrests highlight the growing role of Mexican "
                    "cartels in West African drug trafficking."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "AFR",
        "headline": "Ramaphosa wins court battle over impeachment",
        "summary": ("South Africa's President Cyril Ramaphosa won a court "
                    "battle over an impeachment threat, removing a major "
                    "political risk for his government. The court ruled "
                    "against the attempt to force a vote on his removal. "
                    "Ramaphosa has faced sustained pressure over "
                    "corruption allegations, which he denies."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "AFR",
        "headline": "Nollywood veteran Pete Edochie dies aged 79",
        "summary": ("Veteran Nigerian Nollywood actor Pete Edochie has "
                    "died aged 79, his family confirmed. Edochie was one "
                    "of the founding stars of Nollywood, famous for "
                    "roles as a king and elder statesman in films that "
                    "reached audiences across Africa. Tributes poured in "
                    "from actors, fans and politicians."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "AFR",
        "headline": "Zimbabwe warrant for Mugabe's son",
        "summary": ("Zimbabwe issued an arrest warrant for Robert "
                    "Mugabe's son over a missed court date, in the latest "
                    "legal trouble for the former president's family. The "
                    "warrant was issued after he failed to appear for a "
                    "hearing. His lawyers said they would challenge the "
                    "order and seek to have it set aside."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "AFR",
        "headline": "DR Congo military plane missing, rebels claim hit",
        "summary": ("DR Congo said a military aircraft is missing after "
                    "rebels claimed to have shot down the plane. The "
                    "aircraft was on a mission in the east of the "
                    "country, where M23 rebels have seized territory. "
                    "The army said a search was under way, while the "
                    "rebels released footage they say shows the "
                    "wreckage."),
        "source": "BBC",
        "tag": "R",
        "image": "",
    },
    {
        "region": "AFR",
        "headline": "Senegal reinstated as Afcon winners by court",
        "summary": ("Senegal were reinstated as Africa Cup of Nations "
                    "2025 winners by a court ruling, after the Court of "
                    "Arbitration for Sport upheld their appeal. The "
                    "decision reverses a ruling that had stripped them "
                    "of the title and restores the trophy to the "
                    "Teranga Lions. Fans celebrated the verdict across "
                    "Dakar."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "India marks 18 years since 26/11 Mumbai attacks",
        "summary": ("India marked the 18th anniversary of the 26/11 "
                    "Mumbai terror attacks, in which 166 people were "
                    "killed by gunmen who struck hotels, a station and "
                    "a Jewish centre in 2008. Tributes were paid across "
                    "the country to the victims and to the security "
                    "forces who fought the attackers. The anniversary "
                    "falls on Constitution Day in India."),
        "source": "Observer Voice",
        "tag": "C",
        "image": "assets/mumbai.png",
    },
    {
        "region": "APAC",
        "headline": "India celebrates Constitution Day",
        "summary": ("India celebrated Constitution Day, also known as "
                    "Samvidhan Divas, marking 77 years since the "
                    "adoption of its constitution on November 26, 1949. "
                    "Ceremonies were held in Delhi and state capitals, "
                    "with leaders reading the Preamble. Schools and "
                    "colleges organised debates on the values of the "
                    "constitution."),
        "source": "SelfStudys",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "Gukesh faces Sindarov in world title game three",
        "summary": ("India's reigning world chess champion D Gukesh is "
                    "competing against Uzbekistan's Javokhir Sindarov in "
                    "the 2026 World Chess Championship in Geneva. The "
                    "third game of the 14-game match is scheduled for "
                    "November 26. Gukesh said after game two that he "
                    "felt he was always under control."),
        "source": "Jagran Josh",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "India unveils Rs 15,000 crore package for Nepal",
        "summary": ("India announced development assistance worth 15,000 "
                    "crore rupees for Nepal following talks between Prime "
                    "Minister Narendra Modi and Nepal's Prime Minister "
                    "Balendra Shah. The package will fund roads, power "
                    "and health projects. The two leaders also discussed "
                    "trade, border security and energy cooperation."),
        "source": "SelfStudys",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "First Pakistani astronaut joins China mission",
        "summary": ("Pakistan's Muhammad Zeeshan Ali has become the first "
                    "foreign astronaut to travel to China's Tiangong "
                    "space station, as part of the Shenzhou-24 mission. "
                    "The payload specialist will carry out experiments "
                    "in orbit. The flight marks a milestone in "
                    "China-Pakistan space cooperation and Beijing's "
                    "effort to open its station to partners."),
        "source": "SelfStudys",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "Bangladesh garment workers win 36% pay rise",
        "summary": ("Bangladesh announced a 36 percent increase in the "
                    "minimum monthly wage for entry-level garment "
                    "workers, a victory for the millions who sew clothes "
                    "for global brands. Unions had demanded a bigger "
                    "rise, but welcomed the deal. The garment sector "
                    "employs four million people and drives the "
                    "country's exports."),
        "source": "The Daily Jagran",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "North Korea orders Swiss office to close",
        "summary": ("North Korea directed Switzerland to close its newly "
                    "opened diplomatic office in Pyongyang, in a row "
                    "over sanctions. Swiss officials said diplomatic "
                    "relations would be maintained through the Norwegian "
                    "embassy. The expulsion of the Swiss diplomat is the "
                    "latest sign of Pyongyang's isolation from the "
                    "West."),
        "source": "SelfStudys",
        "tag": "C",
        "image": "",
    },
    {
        "region": "APAC",
        "headline": "Hong Kong fire inquiry finds failures a year on",
        "summary": ("A year after the Wang Fuk Court fire killed 168 "
                    "people in Hong Kong, an independent committee found "
                    "the blaze was preventable, blaming fire-safety "
                    "failures, alleged fraud and suspected corruption. "
                    "The fire spread at an unprecedented 10 metres per "
                    "second through scaffolding and non-fire-retardant "
                    "netting. Alarms had been switched off in all eight "
                    "blocks."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
]

STORIES += [
    {
        "region": "SCI",
        "headline": "Duran Duran guitarist Andy Taylor dies at 65",
        "summary": ("Duran Duran guitarist Andy Taylor has died aged 65, "
                    "the band confirmed. Taylor was a founding member of "
                    "the Birmingham group whose hits, including Rio and "
                    "Hungry Like the Wolf, defined 1980s pop. He left "
                    "the band in 1986, returned in 2001, and had been "
                    "living with prostate cancer. Tributes came from "
                    "across the music world."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "SCI",
        "headline": "Gordon Ramsay to host revived Top Gear",
        "summary": ("Gordon Ramsay will host Top Gear as the show is "
                    "revived after the Flintoff crash that halted "
                    "production. Ramsay will take the driving seat "
                    "alongside as yet unnamed co-presenters when filming "
                    "starts next year. The BBC hopes the chef's star "
                    "power can rebuild the motoring show's "
                    "audience."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "SCI",
        "headline": "Canadian astronaut welcomes baby from space",
        "summary": ("A Canadian astronaut welcomed a baby girl from the "
                    "space station, in a first for the country's space "
                    "programme. The astronaut spoke to family on Earth "
                    "from orbit to mark the birth. The moment was shared "
                    "by the Canadian Space Agency, which called it a "
                    "joyful day for the crew and their families."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "SCI",
        "headline": "Jolie and Pitt settle winery legal battle",
        "summary": ("Angelina Jolie and Brad Pitt settled their legal "
                    "battle over the French winery they once owned "
                    "together, ending years of court fights over the "
                    "Chateau Miraval estate. The dispute over the sale "
                    "of Jolie's stake had become one of the most bitter "
                    "legacies of their divorce. Terms of the settlement "
                    "were not disclosed."),
        "source": "BBC",
        "tag": "C",
        "image": "",
    },
    {
        "region": "SCI",
        "headline": "Wolbachia mosquitoes cut infections 68% in Brazil",
        "summary": ("Releasing Wolbachia-infected mosquitoes helped slash "
                    "mosquito-borne viral infections by 68 percent in "
                    "Brazil, researchers reported. The bacteria block "
                    "viruses such as dengue inside the insects. The "
                    "programme is now one of the largest of its kind in "
                    "the world, and other countries are studying the "
                    "results."),
        "source": "StudMentor",
        "tag": "C",
        "image": "",
    },
    {
        "region": "SCI",
        "headline": "India's space economy to hit $45bn in a decade",
        "summary": ("Union Minister Jitendra Singh said India's space "
                    "economy will grow from 9 billion dollars to 45 "
                    "billion dollars within a decade. The government is "
                    "opening the sector to private firms and has set "
                    "ambitious launch targets. India has already become "
                    "a low-cost launch provider for satellites from "
                    "around the world."),
        "source": "StudMentor",
        "tag": "C",
        "image": "",
    },
]


def story_count():
    """Number of stories in this edition."""
    return len(STORIES)


def region_counts():
    """Story count per region code, in REGIONS order."""
    out = {code: 0 for code, _name in REGIONS}
    for story in STORIES:
        out[story["region"]] += 1
    return out


def check():
    """Validate the edition: counts, summaries, tags, dates."""
    problems = []
    if len(STORIES) != 49:
        problems.append("story count is %d, want 49" % len(STORIES))
    for i, story in enumerate(STORIES):
        words = len(story["summary"].split())
        if words < 40 or words > 70:
            problems.append("story %d summary has %d words"
                            % (i, words))
        if story["tag"] not in ("C", "R"):
            problems.append("story %d bad tag" % i)
        if not story["source"] or not story["headline"]:
            problems.append("story %d missing field" % i)
    counts = region_counts()
    for code, _name in REGIONS:
        if counts[code] == 0:
            problems.append("region %s empty" % code)
    return problems
