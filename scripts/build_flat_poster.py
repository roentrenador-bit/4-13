# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
CREAM = (237, 234, 227)
NAVY = (31, 42, 56)
NAVY_DARK = (17, 24, 33)
GOLD = (140, 106, 63)
GOLD_LIGHT = (196, 168, 122)
WHITE = (255, 255, 255)
TEXT_DARK = (43, 43, 43)
TEXT_MUTED = (150, 150, 150)

FONTS = r"C:\Windows\Fonts"


def f(name, size):
    return ImageFont.truetype(f"{FONTS}\\{name}", size)

georgia_b_54 = f("georgiab.ttf", 54)
georgia_b_36 = f("georgiab.ttf", 40)
georgia_i_26 = f("georgiai.ttf", 26)
arial_14 = f("arial.ttf", 14)
arial_bd_14 = f("arialbd.ttf", 14)
arial_11 = f("arial.ttf", 11)
arial_bd_16 = f("arialbd.ttf", 16)
arial_bd_20 = f("arialbd.ttf", 20)
georgia_18 = f("georgia.ttf", 18)
arial_10 = f("arial.ttf", 10)
arial_bd_11 = f("arialbd.ttf", 11)


def center_text(draw, cx, y, text, font, fill, letter_spacing=0):
    if letter_spacing:
        text = (" " * 0).join(text)
        widths = [draw.textlength(c, font=font) for c in text]
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2, y), text, font=font, fill=fill)
    return w


def spaced(text, n=1):
    return (" " * n).join(list(text))


def rounded_card(size, radius, fill, outline=None, outline_w=0):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=fill,
                         outline=outline, width=outline_w)
    return img, d


def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- Top section ----
    tag = spaced("BIBLE READING PLAN + GUIDED JOURNAL", 1)
    center_text(d, W / 2, 56, tag, arial_bd_14, GOLD)

    d.line([(W / 2 - 120, 100), (W / 2 + 120, 100)], fill=GOLD, width=2)

    center_text(d, W / 2, 118, "A Man's Journey", georgia_b_54, NAVY)
    center_text(d, W / 2, 178, "Through the Word", georgia_b_54, NAVY)

    d.line([(W / 2 - 120, 260), (W / 2 + 120, 260)], fill=GOLD, width=2)

    center_text(d, W / 2, 282, spaced("365 DAYS OF READING. A LIFETIME OF IMPACT.", 1), arial_bd_11, (90, 90, 90))
    center_text(d, W / 2, 306, "Read.  Reflect.  Grow.", georgia_i_26, GOLD)

    # ---- Middle section (dark) ----
    mid_top = 360
    mid_bottom = 1120
    d.rectangle([0, mid_top, W, mid_bottom], fill=NAVY)

    # simple mountain line art silhouette across the dark band (subtle, behind cards)
    mtn_color = (46, 58, 74)
    d.polygon([(0, mid_top + 210), (140, mid_top + 90), (260, mid_top + 210),
               (420, mid_top + 40), (620, mid_top + 210), (780, mid_top + 110),
               (W, mid_top + 210), (W, mid_bottom), (0, mid_bottom)], fill=mtn_color)

    # ---- Left card: Daily Reading ----
    lc_w, lc_h = 280, 470
    left_card, ld = rounded_card((lc_w, lc_h), 10, WHITE)
    ld.text((26, 28), spaced("DAILY READING", 1), font=arial_bd_14, fill=NAVY)
    ld.line([(26, 54), (lc_w - 26, 54)], fill=(220, 220, 220), width=1)
    ld.text((26, 78), "DAY 1", font=arial_bd_16, fill=GOLD)

    rows = [
        ("OLD TESTAMENT", "Genesis 1:1-2:3"),
        ("NEW TESTAMENT", "Matthew 1:1-17"),
        ("PSALMS & PROVERBS", "Psalm 1 | Proverbs 1:1-6"),
    ]
    y = 118
    for label, val in rows:
        ld.text((26, y), label, font=arial_10, fill=TEXT_MUTED)
        ld.text((26, y + 15), val, font=georgia_18, fill=TEXT_DARK)
        y += 62

    ld.line([(26, y + 6), (lc_w - 26, y + 6)], fill=(220, 220, 220), width=1)
    y += 26
    ld.text((26, y), "REFLECTION", font=arial_bd_14, fill=NAVY)
    y += 26
    refl = ["What does this passage teach", "me about God, myself, and", "the life He calls me to live?"]
    for line in refl:
        ld.text((26, y), line, font=arial_11, fill=TEXT_MUTED)
        y += 18
    y += 10
    for _ in range(4):
        ld.line([(26, y), (lc_w - 26, y)], fill=(230, 230, 230), width=1)
        y += 26

    left_card = left_card.rotate(-6, expand=True, resample=Image.BICUBIC)
    img.paste(left_card, (20, 470), left_card)

    # ---- Right card: S.O.A.P. Journal ----
    rc_w, rc_h = 280, 470
    right_card, rd = rounded_card((rc_w, rc_h), 10, WHITE)
    rd.text((26, 28), spaced("S.O.A.P. JOURNAL", 1), font=arial_bd_14, fill=NAVY)
    rd.line([(26, 54), (rc_w - 26, 54)], fill=(220, 220, 220), width=1)
    rd.text((26, 66), "WEEK 1  /  DAY 1", font=arial_10, fill=TEXT_MUTED)

    items = [
        ("S", "SCRIPTURE", "What does this passage say?"),
        ("O", "OBSERVATION", "What do I notice about God,"),
        ("A", "APPLICATION", "How can I apply this to my life?"),
        ("P", "PRAYER", "What do I want to pray about?"),
    ]
    y = 100
    for letter, label, sub in items:
        rd.ellipse([26, y, 46, y + 20], fill=GOLD)
        bbox = rd.textbbox((0, 0), letter, font=arial_bd_11)
        lw = bbox[2] - bbox[0]
        rd.text((36 - lw / 2, y + 4), letter, font=arial_bd_11, fill=WHITE)
        rd.text((56, y), label, font=arial_bd_14, fill=NAVY)
        rd.text((56, y + 18), sub, font=arial_10, fill=TEXT_MUTED)
        y += 46
        rd.line([(26, y), (rc_w - 26, y)], fill=(230, 230, 230), width=1)
        y += 24

    right_card = right_card.rotate(6, expand=True, resample=Image.BICUBIC)
    img.paste(right_card, (W - 20 - right_card.width, 470), right_card)

    # ---- Center book mockup ----
    bc_w, bc_h = 380, 610
    bx, by = int((W - bc_w) / 2), 380
    book, bd = rounded_card((bc_w, bc_h), 14, NAVY_DARK, outline=GOLD, outline_w=3)
    center_text(bd, bc_w / 2, 70, "A MAN'S JOURNEY", arial_bd_20, (235, 231, 224))
    center_text(bd, bc_w / 2, 98, "THROUGH THE WORD", arial_bd_20, (235, 231, 224))
    bd.line([(bc_w / 2 - 60, 138), (bc_w / 2 + 60, 138)], fill=GOLD, width=2)
    center_text(bd, bc_w / 2, 156, "365-DAY BIBLE READING PLAN", arial_11, GOLD_LIGHT)
    center_text(bd, bc_w / 2, 174, "AND GUIDED JOURNAL", arial_11, GOLD_LIGHT)

    # simple mountain glyph
    mx, my = bc_w / 2, 330
    bd.polygon([(mx - 110, my + 60), (mx - 40, my - 30), (mx, my + 10),
                (mx + 40, my - 60), (mx + 110, my + 60)], outline=GOLD, width=3)

    center_text(bd, bc_w / 2, bc_h - 70, "ESV", arial_bd_14, GOLD)
    center_text(bd, bc_w / 2, bc_h - 46, spaced("READ / REFLECT / GROW", 1), arial_10, (180, 180, 180))

    img.paste(book, (bx, by))

    # ---- Bottom bar ----
    d.rectangle([0, mid_bottom, W, H], fill=NAVY_DARK)
    features = [
        ("365-DAY", "READING PLAN", "Old Testament, New Testament,", "Psalms or Proverbs"),
        ("52 WEEKLY", "S.O.A.P. PAGES", "Simple, powerful", "reflection for real life."),
        ("JUST 10-15", "MINUTES A DAY", "Build a lasting habit,", "not just motivation."),
        ("INSTANT", "DIGITAL DOWNLOAD", "PDF", "66 pages"),
    ]
    col_w = W / 4
    for i, (h1, h2, s1, s2) in enumerate(features):
        cx = col_w * i + col_w / 2
        icon_cy = mid_bottom + 55
        # simple icon shapes per column
        if i == 0:
            d.rounded_rectangle([cx - 18, icon_cy - 16, cx + 18, icon_cy + 16], radius=3, outline=GOLD, width=2)
            d.line([(cx - 18, icon_cy - 6), (cx + 18, icon_cy - 6)], fill=GOLD, width=2)
        elif i == 1:
            d.rounded_rectangle([cx - 16, icon_cy - 18, cx + 16, icon_cy + 18], radius=3, outline=GOLD, width=2)
            for yy in (icon_cy - 8, icon_cy, icon_cy + 8):
                d.line([(cx - 8, yy), (cx + 8, yy)], fill=GOLD, width=1)
        elif i == 2:
            d.ellipse([cx - 18, icon_cy - 18, cx + 18, icon_cy + 18], outline=GOLD, width=2)
            d.line([(cx, icon_cy), (cx, icon_cy - 10)], fill=GOLD, width=2)
            d.line([(cx, icon_cy), (cx + 8, icon_cy + 4)], fill=GOLD, width=2)
        else:
            d.line([(cx, icon_cy - 16), (cx, icon_cy + 10)], fill=GOLD, width=2)
            d.line([(cx - 8, icon_cy + 2), (cx, icon_cy + 10)], fill=GOLD, width=2)
            d.line([(cx + 8, icon_cy + 2), (cx, icon_cy + 10)], fill=GOLD, width=2)
            d.line([(cx - 12, icon_cy + 18), (cx + 12, icon_cy + 18)], fill=GOLD, width=2)

        center_text(d, cx, icon_cy + 34, h1, arial_bd_14, WHITE)
        center_text(d, cx, icon_cy + 52, h2, arial_bd_14, WHITE)
        center_text(d, cx, icon_cy + 78, s1, arial_10, (170, 170, 170))
        center_text(d, cx, icon_cy + 92, s2, arial_10, (170, 170, 170))

        if i > 0:
            d.line([(col_w * i, mid_bottom + 20), (col_w * i, H - 20)], fill=(60, 60, 60), width=1)

    d.line([(W / 2 - 160, H - 44), (W / 2 - 20, H - 44)], fill=(90, 90, 90), width=1)
    d.line([(W / 2 + 20, H - 44), (W / 2 + 160, H - 44)], fill=(90, 90, 90), width=1)
    center_text(d, W / 2, H - 52, spaced("READ. REFLECT. GROW.", 1), arial_bd_14, GOLD_LIGHT)

    out_path = r"C:\Users\julia\Desktop\4-13\ads\creative\english-men-flat-poster.png"
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    build()
