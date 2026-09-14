import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Flowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


class MountainGlyph(Flowable):
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.hAlign = "CENTER"

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.setStrokeColor(self.color)
        c.setLineWidth(1.6)
        cx, h = self.width / 2, self.height
        path = c.beginPath()
        path.moveTo(cx - 95, 2)
        path.lineTo(cx - 35, h * 0.72)
        path.lineTo(cx, h * 0.32)
        path.lineTo(cx + 35, h)
        path.lineTo(cx + 95, 2)
        c.drawPath(path, stroke=1, fill=0)


class FlowerGlyph(Flowable):
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.hAlign = "CENTER"

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    def draw(self):
        import math
        c = self.canv
        c.setStrokeColor(self.color)
        c.setLineWidth(1.6)
        cx, cy = self.width / 2, self.height / 2
        r_petal = min(self.width, self.height) * 0.30
        d_offset = r_petal * 0.85
        for i in range(6):
            angle = math.radians(i * 60)
            px = cx + d_offset * math.cos(angle)
            py = cy + d_offset * math.sin(angle)
            c.ellipse(px - r_petal, py - r_petal, px + r_petal, py + r_petal, stroke=1, fill=0)
        r_center = r_petal * 0.55
        c.ellipse(cx - r_center, cy - r_center, cx + r_center, cy + r_center, stroke=1, fill=0)

PRODUCT_DIR = r"C:\Users\julia\Desktop\4-13\product"

GENDERS = {
    "men": {
        "accent": colors.HexColor("#8C6A3F"),
        "dark": colors.HexColor("#1F2A38"),
        "light": colors.HexColor("#EDEAE3"),
    },
    "women": {
        "accent": colors.HexColor("#D68CA3"),
        "dark": colors.HexColor("#4F2D3D"),
        "light": colors.HexColor("#F7EDF1"),
    },
}

LANG = {
    "en": {
        "plan_csv": "reading-plan.csv",
        "translation_note": "Recommended translation: ESV (English Standard Version)",
        "tagline": "Old Testament &nbsp;&bull;&nbsp; New Testament &nbsp;&bull;&nbsp; Psalms &amp; Proverbs &mdash; every day",
        "subtitle": "A One-Year Bible Reading Plan &amp; Study Journal",
        "welcome_heading": "Welcome",
        "how_heading": "How This Journal Works",
        "how_body": (
            "Each day of the year has three short readings listed in the plan starting on page 3: "
            "one from the Old Testament, one from the New Testament, and one from Psalms or Proverbs. "
            "Check off each reading as you complete it."
        ),
        "soap_intro": "<b>The S.O.A.P. Method</b> &mdash; Use this simple method on your weekly reflection pages:",
        "soap_lines": [
            "<b>S</b>cripture &mdash; Write the verse that stood out to you.",
            "<b>O</b>bservation &mdash; What is this passage saying?",
            "<b>A</b>pplication &mdash; How does this apply to your life right now?",
            "<b>P</b>rayer &mdash; Write a short prayer in response.",
        ],
        "miss_day": (
            "If you miss a day, don't try to catch up all at once &mdash; just pick back up on today's date. "
            "This is a marathon, not a sprint."
        ),
        "plan_heading": "Your 365-Day Reading Plan",
        "table_headers": ["Day", "Old Testament", "New Testament", "Psalms / Proverbs"],
        "weekly_heading": "Weekly Reflection Pages",
        "weekly_sub": "One page per week &mdash; 52 in total. Use it any day that a reading especially speaks to you.",
        "week_label": "Week",
        "prompts": [
            "SCRIPTURE &mdash; a verse that stood out this week",
            "OBSERVATION &mdash; what is this passage saying?",
            "APPLICATION &mdash; how does this apply to your life right now?",
            "PRAYER &mdash; write a short prayer in response",
            "ONE THING I WANT TO REMEMBER THIS WEEK",
        ],
    },
    "es": {
        "plan_csv": "reading-plan-es.csv",
        "translation_note": "Traducción recomendada: LBLA (La Biblia de las Américas)",
        "tagline": "Antiguo Testamento &nbsp;&bull;&nbsp; Nuevo Testamento &nbsp;&bull;&nbsp; Salmos y Proverbios &mdash; cada día",
        "subtitle": "Un Plan de Lectura Bíblica de un Año y Diario de Estudio",
        "welcome_heading": "Bienvenido",
        "how_heading": "Cómo Funciona Este Diario",
        "how_body": (
            "Cada día del año tiene tres lecturas cortas en el plan que comienza en la página 3: "
            "una del Antiguo Testamento, una del Nuevo Testamento, y una de Salmos o Proverbios. "
            "Marca cada lectura al completarla."
        ),
        "soap_intro": "<b>El método S.O.A.P.</b> &mdash; Úsalo en tus páginas de reflexión semanal:",
        "soap_lines": [
            "<b>E</b>scritura &mdash; Escribe el versículo que más te impactó.",
            "<b>O</b>bservación &mdash; ¿Qué está diciendo este pasaje?",
            "<b>A</b>plicación &mdash; ¿Cómo se aplica esto a tu vida en este momento?",
            "<b>O</b>ración &mdash; Escribe una breve oración en respuesta.",
        ],
        "miss_day": (
            "Si te pierdes un día, no intentes ponerte al día de golpe &mdash; simplemente retoma en la fecha de hoy. "
            "Esto es una maratón, no una carrera corta."
        ),
        "plan_heading": "Tu Plan de Lectura de 365 Días",
        "table_headers": ["Día", "Antiguo Testamento", "Nuevo Testamento", "Salmos / Proverbios"],
        "weekly_heading": "Páginas de Reflexión Semanal",
        "weekly_sub": "Una página por semana &mdash; 52 en total. Úsala cualquier día en que una lectura te hable de forma especial.",
        "week_label": "Semana",
        "prompts": [
            "ESCRITURA &mdash; un versículo que te impactó esta semana",
            "OBSERVACIÓN &mdash; ¿qué dice este pasaje?",
            "APLICACIÓN &mdash; ¿cómo se aplica esto a tu vida ahora?",
            "ORACIÓN &mdash; escribe una breve oración en respuesta",
            "UNA COSA QUE QUIERO RECORDAR ESTA SEMANA",
        ],
    },
}

TITLES = {
    ("en", "men"): "A MAN'S JOURNEY THROUGH THE WORD",
    ("en", "women"): "A WOMAN'S JOURNEY THROUGH THE WORD",
    ("es", "men"): "EL VIAJE DE UN HOMBRE POR LA PALABRA",
    ("es", "women"): "EL VIAJE DE UNA MUJER POR LA PALABRA",
}

WELCOME = {
    ("en", "men"): (
        "This journal was built for one purpose: to help you build the daily habit of "
        "being in the Word for a full year. No guesswork, no getting lost trying to figure "
        "out where to start &mdash; just open to today's date and read.\n\n"
        "Each day you'll cover a short passage from the Old Testament, the New Testament, "
        "and a chapter of Psalms or Proverbs. That's it. About 10&ndash;15 minutes a day is "
        "enough to walk through the entire Bible in 365 days.\n\n"
        "Use the weekly pages in the back to slow down, take notes, and apply what you're "
        "reading. Consistency beats intensity. Show up daily, and let the plan do the rest."
    ),
    ("en", "women"): (
        "This journal was created to help you build a daily rhythm of time in God's Word "
        "&mdash; one that fits into real life, without overwhelm or guilt when a day gets away "
        "from you.\n\n"
        "Each day pairs a short reading from the Old Testament, the New Testament, and a "
        "chapter of Psalms or Proverbs. In about 10&ndash;15 minutes, you can walk through the "
        "whole Bible over the course of a year.\n\n"
        "The weekly pages in the back give you space to slow down, reflect, and write out what "
        "God is showing you. There's no perfect way to do this &mdash; just a next day, and a next "
        "page. Start where you are."
    ),
    ("es", "men"): (
        "Este diario fue creado con un solo propósito: ayudarte a construir el hábito diario "
        "de estar en la Palabra durante un año completo. Sin adivinar, sin perderte tratando de "
        "decidir por dónde empezar &mdash; solo abre en la fecha de hoy y lee.\n\n"
        "Cada día cubrirás un pasaje corto del Antiguo Testamento, del Nuevo Testamento, y un "
        "capítulo de Salmos o Proverbios. Eso es todo. Unos 10&ndash;15 minutos al día bastan "
        "para recorrer toda la Biblia en 365 días.\n\n"
        "Usa las páginas semanales al final para detenerte, tomar notas y aplicar lo que estás "
        "leyendo. La constancia vence a la intensidad. Preséntate cada día, y deja que el plan "
        "haga el resto."
    ),
    ("es", "women"): (
        "Este diario fue creado para ayudarte a construir un ritmo diario de tiempo en la "
        "Palabra de Dios &mdash; uno que encaje en la vida real, sin abrumarte ni sentir culpa "
        "cuando se te pase un día.\n\n"
        "Cada día combina una lectura corta del Antiguo Testamento, del Nuevo Testamento, y un "
        "capítulo de Salmos o Proverbios. En unos 10&ndash;15 minutos puedes recorrer toda la "
        "Biblia a lo largo de un año.\n\n"
        "Las páginas semanales al final te dan espacio para detenerte, reflexionar, y escribir "
        "lo que Dios te está mostrando. No hay una forma perfecta de hacerlo &mdash; solo un "
        "próximo día, y una próxima página. Comienza donde estás."
    ),
}

FOOTERS = {
    ("en", "men"): "A Man's Journey Through the Word",
    ("en", "women"): "A Woman's Journey Through the Word",
    ("es", "men"): "El Viaje de un Hombre por la Palabra",
    ("es", "women"): "El Viaje de una Mujer por la Palabra",
}


def load_plan(csv_name):
    rows = []
    with open(f"{PRODUCT_DIR}\\{csv_name}", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def build_styles(colorset):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverTitle", fontName="Helvetica-Bold", fontSize=26, leading=32,
        alignment=TA_CENTER, textColor=colorset["dark"], spaceAfter=14,
    ))
    styles.add(ParagraphStyle(
        name="CoverSubtitle", fontName="Helvetica", fontSize=14, leading=18,
        alignment=TA_CENTER, textColor=colorset["accent"], spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="CoverNote", fontName="Helvetica-Oblique", fontSize=10, leading=14,
        alignment=TA_CENTER, textColor=colors.HexColor("#888888"), spaceBefore=10,
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading", fontName="Helvetica-Bold", fontSize=17,
        textColor=colorset["dark"], spaceBefore=6, spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="Body", fontName="Helvetica", fontSize=10.5, leading=16,
        textColor=colors.HexColor("#2B2B2B"), spaceAfter=10, alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="WeekLabel", fontName="Helvetica-Bold", fontSize=13,
        textColor=colorset["dark"],
    ))
    styles.add(ParagraphStyle(
        name="PromptLabel", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=colorset["accent"], spaceBefore=8, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="TinyCenter", fontName="Helvetica", fontSize=8.5,
        alignment=TA_CENTER, textColor=colors.HexColor("#777777"),
    ))
    return styles


def cover_flowables(title, lang, colorset, styles, gender_key):
    title_light = ParagraphStyle(
        "TitleLight", parent=styles["CoverTitle"], textColor=colors.HexColor("#F2EFE9"),
    )
    tagline_on_dark = ParagraphStyle(
        "TaglineOnDark", parent=styles["TinyCenter"], textColor=colors.HexColor("#B9B6AE"),
    )
    note_on_dark = ParagraphStyle(
        "NoteOnDark", parent=styles["CoverNote"], textColor=colors.HexColor("#9E9B94"),
    )

    story = []
    story.append(Spacer(1, 0.85 * inch))
    story.append(HRFlowable(width="55%", thickness=1.2, color=colorset["accent"], spaceAfter=16, hAlign="CENTER"))
    story.append(Paragraph(title, title_light))
    story.append(Paragraph(lang["subtitle"], styles["CoverSubtitle"]))
    story.append(HRFlowable(width="55%", thickness=1.2, color=colorset["accent"], spaceBefore=16, hAlign="CENTER"))
    story.append(Spacer(1, 0.55 * inch))
    if gender_key == "women":
        story.append(FlowerGlyph(140, 100, colorset["accent"]))
    else:
        story.append(MountainGlyph(220, 78, colorset["accent"]))
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph(lang["tagline"], tagline_on_dark))
    story.append(Paragraph(lang["translation_note"], note_on_dark))
    story.append(PageBreak())
    return story


def welcome_flowables(lang, welcome_text, styles):
    story = []
    story.append(Paragraph(lang["welcome_heading"], styles["SectionHeading"]))
    for para in welcome_text.split("\n\n"):
        story.append(Paragraph(para, styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(lang["how_heading"], styles["SectionHeading"]))
    story.append(Paragraph(lang["how_body"], styles["Body"]))
    story.append(Paragraph(lang["soap_intro"], styles["Body"]))
    for line in lang["soap_lines"]:
        story.append(Paragraph(line, styles["Body"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(lang["miss_day"], styles["Body"]))
    story.append(PageBreak())
    return story


def plan_table_flowables(lang, colorset, styles, rows):
    story = []
    story.append(Paragraph(lang["plan_heading"], styles["SectionHeading"]))
    story.append(Spacer(1, 4))

    header = lang["table_headers"] + [""]
    data = [header]
    for r in rows:
        data.append([r["Day"], r["OldTestament"], r["NewTestament"], r["Wisdom"], "[  ]"])

    col_widths = [0.42 * inch, 2.15 * inch, 1.85 * inch, 1.3 * inch, 0.35 * inch]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colorset["dark"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.4),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colorset["light"]]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (4, 0), (4, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(table)
    story.append(PageBreak())
    return story


def weekly_pages_flowables(lang, colorset, styles):
    story = []
    story.append(Paragraph(lang["weekly_heading"], styles["SectionHeading"]))
    story.append(Paragraph(lang["weekly_sub"], styles["Body"]))
    story.append(PageBreak())

    for week in range(1, 53):
        story.append(Paragraph(f"{lang['week_label']} {week}", styles["WeekLabel"]))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colorset["accent"], spaceBefore=4, spaceAfter=10))
        for i, prompt in enumerate(lang["prompts"]):
            story.append(Paragraph(prompt, styles["PromptLabel"]))
            story.append(Spacer(1, 20 if i == len(lang["prompts"]) - 1 else 44))
        story.append(PageBreak())
    return story


def footer(text):
    def _footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#999999"))
        canvas.drawCentredString(letter[0] / 2, 0.5 * inch, text)
        canvas.restoreState()
    return _footer


def cover_page(colorset, footer_text):
    footer_fn = footer(footer_text)

    def _cover(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colorset["dark"])
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.restoreState()
        footer_fn(canvas, doc)
    return _cover


def build(lang_key, gender_key):
    lang = LANG[lang_key]
    colorset = GENDERS[gender_key]
    title = TITLES[(lang_key, gender_key)]
    welcome_text = WELCOME[(lang_key, gender_key)]
    footer_text = FOOTERS[(lang_key, gender_key)]

    styles = build_styles(colorset)
    rows = load_plan(lang["plan_csv"])

    lang_name = "english" if lang_key == "en" else "spanish"
    out_path = f"{PRODUCT_DIR}\\bible-in-a-year-{lang_name}-{gender_key}.pdf"
    doc = SimpleDocTemplate(
        out_path, pagesize=letter,
        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
        leftMargin=0.7 * inch, rightMargin=0.7 * inch,
        title=title, author="4-13 Bible Study Co.",
    )

    story = []
    story += cover_flowables(title, lang, colorset, styles, gender_key)
    story += welcome_flowables(lang, welcome_text, styles)
    story += plan_table_flowables(lang, colorset, styles, rows)
    story += weekly_pages_flowables(lang, colorset, styles)

    doc.build(story, onFirstPage=cover_page(colorset, footer_text), onLaterPages=footer(footer_text))
    print(f"Built {out_path}")


if __name__ == "__main__":
    for lang_key in ["en", "es"]:
        for gender_key in ["men", "women"]:
            build(lang_key, gender_key)
