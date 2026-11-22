#!/usr/bin/env python3
"""Draw entry.png for news-image-20261122 from scratch.

Design (mine): dark navy broadsheet, crimson masthead, gold accents,
hero card on top, then a three-column grid of region sections. Every
story is one bold headline line plus one wrapped detail line and a
named source. The script measures every string in pixels and aborts
with an error instead of silently cutting any text.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

BG = (15, 27, 45)          # deep navy
PANEL = (23, 40, 61)       # card navy
PANEL_LINE = (48, 70, 96)  # card border
MASTHEAD = (176, 58, 46)   # crimson
GOLD = (232, 185, 60)
INK = (242, 244, 247)      # near-white
MUTED = (169, 183, 201)    # grey-blue
HERO_BG = (27, 46, 68)

REGION_COLORS = {
    "MIDDLE EAST": (192, 57, 43),
    "EUROPE": (36, 113, 163),
    "NORTH AMERICA": (30, 132, 73),
    "SOUTH AMERICA": (183, 149, 11),
    "AFRICA": (125, 60, 152),
    "ASIA": (202, 111, 30),
    "OCEANIA": (0, 131, 143),
}

# (headline, detail, source, region)
HERO = (
    "Iran hits Bahrain site; two tankers struck in Hormuz",
    "Tehran's Guards claim US bases hit; Bahrain says a civilian site was set ablaze.",
    "BBC / Reuters",
)

STORIES = [
    # MIDDLE EAST (7 more)
    ("Saudi jets strike Hodeidah port",
     "3 missiles aimed at Riyadh intercepted.",
     "Saudi coalition", "MIDDLE EAST"),
    ("COP31 in overtime as fossil-fuel text dropped",
     "Draft drops phaseout; EU wants a deal.",
     "BBC", "MIDDLE EAST"),
    ("Gaza storms flood shelters for 1m displaced",
     "Storms wreck tents; strike kills 3.",
     "UN", "MIDDLE EAST"),
    ("Aoun: Israel must quit south Lebanon",
     "President demands pullout, arms monopoly.",
     "Reports", "MIDDLE EAST"),
    ("Fire at Iraq power plant kills 4, injures 35",
     "Blaze at Hartha station near Basra.",
     "Iraqi state media", "MIDDLE EAST"),
    ("Iran FM: allies oppose nuclear doctrine shift",
     "Allies reject nuclear policy change.",
     "Reports", "MIDDLE EAST"),
    ("Palestinians protest as Gaza strikes intensify",
     "Displaced families rally amid bombing.",
     "Al Jazeera", "MIDDLE EAST"),
    # EUROPE (7)
    ("Russia hits Zelensky's hometown; 2 killed",
     "Strike wounds ~60; Kyiv hits Russian ship.",
     "France 24", "EUROPE"),
    ("Drone hits Russian cargo ship in Baltic",
     "Ship burns in Gulf of Finland.",
     "BBC", "EUROPE"),
    ("Denmark: Russia plotted to kill rapper",
     "Copenhagen accuses Russia of murder plot.",
     "BBC", "EUROPE"),
    ("Europe wins seat at Russia talks",
     "E5, NATO, EU join Berlin peace talks.",
     "Kyiv Independent", "EUROPE"),
    ("EU plastic-waste export ban takes effect",
     "735,000 tonnes a year rerouted to Turkey.",
     "EUobserver", "EUROPE"),
    ("German MP kicked at Berlin protest",
     "Preisler assaulted at Berlin rally.",
     "News Media House", "EUROPE"),
    ("French hopefuls clash in TV debate",
     "Five hopefuls spar over tax and housing.",
     "TF1", "EUROPE"),
    # NORTH AMERICA (7)
    ("FBI crime database hacked, Trump confirms",
     "Breach hits fingerprints, wanted records.",
     "CNBC", "NORTH AMERICA"),
    ("US stocks slide into correction",
     "AI sell-off drags Dow, S&P into correction.",
     "Market reports", "NORTH AMERICA"),
    ("Nvidia board probes CEO Huang",
     "Inquiry over affair tied to Chinese intel.",
     "Nexus Europa", "NORTH AMERICA"),
    ("US envoys head to Moscow and Dublin",
     "Envoys brief Putin after Abu Dhabi talks.",
     "Nexus Europa", "NORTH AMERICA"),
    ("Palisades fire arsonist convicted",
     "Man guilty of starting Los Angeles blaze.",
     "BBC", "NORTH AMERICA"),
    ("California braces for biggest waves in years",
     "Coastal towns on alert as huge surf hits.",
     "The Guardian", "NORTH AMERICA"),
    ("Florida river breaks 73-year flood record",
     "St. Johns floods towns Miami to Brevard.",
     "Reports", "NORTH AMERICA"),
    # SOUTH AMERICA (6)
    ("Mexico captures 'El Chapo Isidro'; 11 killed",
     "Forces seize Beltran Leyva boss.",
     "The Guardian", "SOUTH AMERICA"),
    ("Bolsonaro in intensive care",
     "Ex-president treated for bowel blockage.",
     "Reports", "SOUTH AMERICA"),
    ("Boca win Copa Sudamericana 2-0",
     "Boca beat Atletico Mineiro in final.",
     "Elbotola", "SOUTH AMERICA"),
    ("CONMEBOL backs Infantino re-election",
     "All 10 back FIFA chief for March vote.",
     "Al Jazeera", "SOUTH AMERICA"),
    ("Peru quake 6.7 blocks roads, damages homes",
     "Tremor cuts power in mountain towns.",
     "EIN News", "SOUTH AMERICA"),
    ("Hegseth signs Caracas defence pact",
     "Defence chief tours four capitals.",
     "Ace Dispatch", "SOUTH AMERICA"),
    # AFRICA (6)
    ("Nigeria boat capsizes; 24 dead",
     "Overcrowded boat sinks on funeral trip.",
     "Al Jazeera", "AFRICA"),
    ("Tinubu: decriminalise attempted suicide",
     "Tinubu asks parliament to change the law.",
     "TimesLIVE", "AFRICA"),
    ("Egypt seals $2.3bn IMF deal",
     "Growth at 5.1% as tourism and Suez recover.",
     "Africanews", "AFRICA"),
    ("Kenya gives $60bn minerals deal to US group",
     "US group wins Mrima Hill minerals deal.",
     "BBC", "AFRICA"),
    ("Amnesty: RSF drone strikes are war crimes",
     "9 strikes killed 37 civilians.",
     "Amnesty Intl", "AFRICA"),
    ("South Africa holds repo rate at 7.25%",
     "Reserve Bank holds rate despite inflation.",
     "Reports", "AFRICA"),
    # ASIA (7)
    ("Toxic alcohol kills 11 in Manipur",
     "180+ in hospital after illicit drink.",
     "Manipur CM", "ASIA"),
    ("Indonesia factory fire: 3 dead, 36 missing",
     "Rescuers search candy plant in Banten.",
     "Reuters", "ASIA"),
    ("Myanmar slams ASEAN ruling 'unfair'",
     "Junta protests exclusion from summits.",
     "Reuters", "ASIA"),
    ("EU-Indonesia sign trade deal",
     "Pact covers 730m people, in force 2027.",
     "Reports", "ASIA"),
    ("S. Korea education chief quits in AI scandal",
     "Minister resigns over AI cheating affair.",
     "Reports", "ASIA"),
    ("China renews UN bid to blacklist BLA",
     "Beijing pushes to list Baloch groups.",
     "Reports", "ASIA"),
    ("Amazon nears $7.5bn Decart deal",
     "Startup deal would boost Trainium chips.",
     "Crypto Briefing", "ASIA"),
    # OCEANIA (4)
    ("Australia crush NZ 34-10 in league final",
     "Jillaroos win 4th straight League Cup.",
     "Al Jazeera", "OCEANIA"),
    ("Australia edge Wales 29-26 in Cardiff",
     "Wallabies win Championship thriller.",
     "ESPN", "OCEANIA"),
    ("India post record 720/9 in NZ Test",
     "Pant hits 128; India declare 352 ahead.",
     "EIN Presswire", "OCEANIA"),
    ("Debate: should NZ join Australia?",
     "Old invite to become 7th state revives.",
     "The Post", "OCEANIA"),
]

REGION_ORDER = ["MIDDLE EAST", "EUROPE", "NORTH AMERICA",
                "SOUTH AMERICA", "AFRICA", "ASIA", "OCEANIA"]

# Columns keep regions together: (regions) per column.
COLUMNS = [
    ["MIDDLE EAST", "EUROPE"],
    ["NORTH AMERICA", "SOUTH AMERICA"],
    ["AFRICA", "ASIA", "OCEANIA"],
]

GRID_TOP = 244
GRID_BOTTOM = 990
FOOTER_Y = 996


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("DejaVuSans-Bold.ttf", 44)
F_DATE = font("DejaVuSans-Bold.ttf", 25)
F_HERO_HEAD = font("DejaVuSans-Bold.ttf", 23)
F_HERO_DET = font("DejaVuSans.ttf", 15)
F_HERO_SRC = font("DejaVuSans-Bold.ttf", 12)
F_CHIP = font("DejaVuSans-Bold.ttf", 13)
F_HEAD = font("DejaVuSans-Bold.ttf", 14)
F_DET = font("DejaVuSans.ttf", 11)
F_SRC = font("DejaVuSans.ttf", 10)
F_FOOT = font("DejaVuSans.ttf", 11)
F_TAG = font("DejaVuSans-Bold.ttf", 11)


def wrap(text, fnt, max_w):
    """Greedy word wrap by pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if not cur:
                raise ValueError(f"single word too wide: {w!r}")
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(text, fnt, max_w, sizes):
    """Shrink font until the text fits on one line; returns (font, text)."""
    for sz in sizes:
        f = font("DejaVuSans-Bold.ttf", sz)
        if f.getlength(text) <= max_w:
            return f, text
    raise ValueError(f"headline never fits: {text!r}")


def draw_globe(d, cx, cy, r):
    """Minimal globe: circle outline, meridians, equator."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=2)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=GOLD, width=1)
    d.line([cx - r, cy, cx + r, cy], fill=GOLD, width=1)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 200, 340, fill=GOLD, width=1)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 20, 160, fill=GOLD, width=1)


def main():
    assert len(STORIES) == 44, f"need 44 stories, have {len(STORIES)}"
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 92], fill=MASTHEAD)
    d.rectangle([0, 92, W, 95], fill=GOLD)
    draw_globe(d, 62, 46, 30)
    title = "WORLD NEWS"
    d.text((108, 8), title, font=F_TITLE, fill=INK)
    d.text((108, 58), "SUNDAY 22 NOVEMBER 2026", font=F_DATE, fill=GOLD)
    d.text((W - 14 - F_TAG.getlength("ONE IMAGE  •  45 STORIES"), 34),
           "ONE IMAGE  •  45 STORIES", font=F_TAG, fill=INK)

    # ---- Hero ----
    hx0, hx1, hy0, hy1 = 12, W - 12, 104, 232
    d.rectangle([hx0, hy0, hx1, hy1], fill=HERO_BG, outline=PANEL_LINE)
    d.rectangle([hx0, hy0, hx0 + 6, hy1], fill=GOLD)
    d.text((hx0 + 18, hy0 + 8), "TOP STORY", font=F_TAG, fill=GOLD)
    head, det, src = HERO
    hl = wrap(head, F_HERO_HEAD, hx1 - hx0 - 36)
    if len(hl) > 2:
        raise ValueError(f"hero headline wraps to {len(hl)} lines: {head!r}")
    y = hy0 + 28
    for line in hl:
        d.text((hx0 + 18, y), line, font=F_HERO_HEAD, fill=INK)
        y += 28
    dl = wrap(det, F_HERO_DET, hx1 - hx0 - 36)
    if len(dl) > 2:
        raise ValueError(f"hero detail wraps to {len(dl)} lines: {det!r}")
    for line in dl:
        d.text((hx0 + 18, y), line, font=F_HERO_DET, fill=MUTED)
        y += 19
    d.text((hx1 - 18 - F_HERO_SRC.getlength("Source: " + src), hy1 - 20),
           "Source: " + src, font=F_HERO_SRC, fill=GOLD)

    # ---- Grid ----
    col_w = 322
    col_x = [12, 351, 690]
    gutter = 17
    for ci, regions in enumerate(COLUMNS):
        x = col_x[ci]
        y = GRID_TOP
        for region in regions:
            stories = [s for s in STORIES if s[3] == region]
            # chip
            chip_w = 14 + F_CHIP.getlength(region) + 14
            d.rounded_rectangle([x, y, x + chip_w, y + 24],
                                radius=4, fill=REGION_COLORS[region])
            d.text((x + 14, y + 5), region, font=F_CHIP, fill=INK)
            d.text((x + chip_w + 8, y + 6),
                   f"{len(stories)} stories", font=F_SRC, fill=MUTED)
            y += 24 + 6
            for head, det, src, _ in stories:
                f_head, head_txt = fit_one_line(
                    head, F_HEAD, col_w, [14, 13, 12])
                d.text((x, y), head_txt, font=f_head, fill=INK)
                y += 17
                # The detail wraps inside (column width - source width),
                # so the gold source on the same row can never overlap it.
                # A detail must fit on ONE line there, or the script fails.
                sw = F_SRC.getlength(src)
                dl = wrap(det, F_DET, col_w - sw - 8)
                if len(dl) != 1:
                    raise ValueError(
                        f"detail must fit one line, got {len(dl)}: {det!r}")
                d.text((x, y), dl[0], font=F_DET, fill=MUTED)
                d.text((x + col_w - sw, y), src, font=F_SRC, fill=GOLD)
                y += 14
                y += 5
            y += 6  # gap between regions
        if y > GRID_BOTTOM:
            raise ValueError(f"column {ci} overflows: final y={y} > {GRID_BOTTOM}")
        print(f"column {ci}: final y={y}")

    # ---- Footer ----
    foot = ("45 sourced stories  •  7 regions  •  SUNDAY 22 NOVEMBER 2026  •  "
            "Sources: BBC, Reuters, AP, Al Jazeera, The Guardian, CNBC, France 24, ESPN")
    d.text(((W - F_FOOT.getlength(foot)) / 2, FOOTER_Y), foot,
           font=F_FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
