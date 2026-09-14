# -*- coding: utf-8 -*-
import os

OUT_DIR = r"C:\Users\julia\Desktop\4-13\landing-page"

TEMPLATE = """<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --dark: {dark};
    --accent: {accent};
    --light: {light};
    --bg: #FAFAF8;
    --text: #2B2B2B;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: Georgia, 'Times New Roman', serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
  }}
  .wrap {{ max-width: 880px; margin: 0 auto; padding: 0 20px; }}
  header.hero {{
    background: var(--dark);
    color: #fff;
    padding: 70px 0 60px;
    text-align: center;
  }}
  header.hero .tag {{
    letter-spacing: 3px;
    text-transform: uppercase;
    font-size: 13px;
    color: var(--accent);
    font-family: Arial, sans-serif;
    margin-bottom: 18px;
  }}
  header.hero h1 {{ font-size: 38px; margin: 0 0 16px; line-height: 1.25; }}
  header.hero p.sub {{
    font-size: 18px; color: #D8D3C8; max-width: 560px; margin: 0 auto 22px;
  }}
  header.hero p.translation {{
    font-size: 13px; color: #A8A296; font-family: Arial, sans-serif; margin-bottom: 26px;
  }}
  .btn {{
    display: inline-block; background: var(--accent); color: #fff; text-decoration: none;
    font-family: Arial, sans-serif; font-weight: bold; padding: 16px 36px;
    border-radius: 4px; font-size: 16px; letter-spacing: 0.5px;
  }}
  section {{ padding: 56px 0; }}
  section.alt {{ background: var(--light); }}
  h2 {{ font-size: 27px; text-align: center; color: var(--dark); margin-bottom: 10px; }}
  p.center-sub {{
    text-align: center; color: #666; font-family: Arial, sans-serif;
    max-width: 560px; margin: 0 auto 36px;
  }}
  .grid3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
  @media (max-width: 700px) {{ .grid3 {{ grid-template-columns: 1fr; }} }}
  .card {{
    background: #fff; border: 1px solid #e2e2e2; border-radius: 6px;
    padding: 24px; font-family: Arial, sans-serif;
  }}
  .card h3 {{ color: var(--dark); font-size: 17px; margin-top: 0; }}
  .card p {{ color: #555; font-size: 14.5px; }}
  .plan-preview {{
    background: #fff; border: 1px solid #ddd; border-radius: 6px;
    overflow: hidden; font-family: Arial, sans-serif; font-size: 13.5px;
  }}
  .plan-preview table {{ width: 100%; border-collapse: collapse; }}
  .plan-preview th {{ background: var(--dark); color: #fff; text-align: left; padding: 10px 12px; }}
  .plan-preview td {{ padding: 8px 12px; border-top: 1px solid #eee; }}
  .plan-preview tr:nth-child(even) td {{ background: var(--light); }}
  .price-box {{
    max-width: 420px; margin: 0 auto; background: #fff; border: 2px solid var(--accent);
    border-radius: 10px; padding: 34px 28px; text-align: center; font-family: Arial, sans-serif;
  }}
  .price-box .price {{ font-size: 42px; color: var(--dark); font-weight: bold; margin: 10px 0; }}
  .price-box .was {{ color: #999; text-decoration: line-through; font-size: 16px; }}
  .price-box ul {{ text-align: left; color: #444; font-size: 14.5px; padding-left: 20px; }}
  footer {{ text-align: center; padding: 30px 20px; font-family: Arial, sans-serif; font-size: 12.5px; color: #999; }}
  .faq-item {{ max-width: 680px; margin: 0 auto 20px; font-family: Arial, sans-serif; }}
  .faq-item h4 {{ margin-bottom: 4px; color: var(--dark); }}
  .faq-item p {{ color: #555; font-size: 14.5px; margin-top: 0; }}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <div class="tag">{tag}</div>
    <h1>{h1}</h1>
    <p class="sub">{hero_sub}</p>
    <p class="translation">{translation_note}</p>
    <a class="btn" href="#pricing">{cta_hero}</a>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>{section1_h2}</h2>
    <p class="center-sub">{section1_sub}</p>
    <div class="grid3">
      <div class="card"><h3>{card1_h}</h3><p>{card1_p}</p></div>
      <div class="card"><h3>{card2_h}</h3><p>{card2_p}</p></div>
      <div class="card"><h3>{card3_h}</h3><p>{card3_p}</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>{inside_h2}</h2>
    <p class="center-sub">{inside_sub}</p>
    <div class="plan-preview">
      <table>
        <tr><th>{th_day}</th><th>{th_ot}</th><th>{th_nt}</th><th>{th_wisdom}</th></tr>
        <tr><td>1</td><td>{row1_ot}</td><td>{row1_nt}</td><td>{row1_wisdom}</td></tr>
        <tr><td>2</td><td>{row2_ot}</td><td>{row2_nt}</td><td></td></tr>
        <tr><td>3</td><td>{row3_ot}</td><td>{row3_nt}</td><td>{row3_wisdom}</td></tr>
        <tr><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td></tr>
      </table>
    </div>
  </div>
</section>

<section id="pricing">
  <div class="wrap">
    <h2>{pricing_h2}</h2>
    <div class="price-box">
      <div class="was">{was_price}</div>
      <div class="price">{price}</div>
      <ul>
        <li>{feature1}</li>
        <li>{feature2}</li>
        <li>{feature3}</li>
      </ul>
      <a class="btn" href="#" style="margin-top:14px;">{cta_price}</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>{faq_h2}</h2>
    <div class="faq-item"><h4>{faq1_q}</h4><p>{faq1_a}</p></div>
    <div class="faq-item"><h4>{faq2_q}</h4><p>{faq2_a}</p></div>
    <div class="faq-item"><h4>{faq3_q}</h4><p>{faq3_a}</p></div>
  </div>
</section>

<footer>{footer}</footer>

</body>
</html>
"""

VARIANTS = {
    "english-men": dict(
        html_lang="en",
        title="A Man's Journey Through the Word",
        dark="#1F2A38", accent="#8C6A3F", light="#EDEAE3",
        tag="365-Day Bible Reading Plan &amp; Journal",
        h1="A Man's Journey Through the Word",
        hero_sub="A simple, no-excuses way to read through the entire Bible in one year &mdash; 10&ndash;15 minutes a day, with a guided journal built for consistency.",
        translation_note="Recommended translation: ESV (English Standard Version)",
        cta_hero="Get the Journal &mdash; $12",
        section1_h2="Stop starting over in Genesis 3.",
        section1_sub="You don't need more willpower. You need a plan you'll actually finish.",
        card1_h="No guesswork", card1_p="Every day is mapped out for you &mdash; Old Testament, New Testament, and Psalms or Proverbs. Just open to today's date.",
        card2_h="Built for busy men", card2_p="Each day's reading takes 10&ndash;15 minutes. No perfect quiet morning required &mdash; just consistency.",
        card3_h="52 reflection pages", card3_p="A simple weekly S.O.A.P. study page to actually apply what you're reading, not just check a box.",
        inside_h2="What's Inside", inside_sub="A 66-page printable/digital journal, instantly downloadable.",
        th_day="Day", th_ot="Old Testament", th_nt="New Testament", th_wisdom="Psalms / Proverbs",
        row1_ot="Genesis 1-3", row1_nt="Matthew 1", row1_wisdom="Psalms 1",
        row2_ot="Genesis 4-5", row2_nt="Matthew 2",
        row3_ot="Genesis 6-7", row3_nt="Matthew 3", row3_wisdom="Psalms 2",
        pricing_h2="Get Your Journal", was_price="$19", price="$12",
        feature1="365-day reading plan (OT + NT + Psalms/Proverbs)",
        feature2="52 weekly S.O.A.P. reflection pages",
        feature3="Instant digital download (PDF, print or use on tablet)",
        cta_price="Get Instant Access",
        faq_h2="FAQ",
        faq1_q="What Bible translation do I need?", faq1_a="We recommend the ESV, but any translation works &mdash; the plan lists book and chapter only, so use whatever Bible or app you already have.",
        faq2_q="Is this printable?", faq2_a="Yes. It's a standard letter-size PDF you can print at home or at a print shop, or use digitally on a tablet.",
        faq3_q="What if I fall behind?", faq3_a="The plan is built by calendar day, not sequential pressure &mdash; just pick back up on today's date, no catch-up required.",
        footer="&copy; 4-13 Bible Study Co. &middot; This is a digital download, delivered instantly after purchase.",
    ),
    "english-women": dict(
        html_lang="en",
        title="A Woman's Journey Through the Word",
        dark="#4A3B3B", accent="#B48A78", light="#F5EDE8",
        tag="365-Day Bible Reading Plan &amp; Journal",
        h1="A Woman's Journey Through the Word",
        hero_sub="A gentle, realistic way to read through the whole Bible in a year &mdash; 10&ndash;15 minutes a day, with a guided journal that fits real life.",
        translation_note="Recommended translation: ESV (English Standard Version)",
        cta_hero="Get the Journal &mdash; $12",
        section1_h2="No guilt. No falling behind. Just a next page.",
        section1_sub="A rhythm you can actually keep, even on the busy, imperfect days.",
        card1_h="No guesswork", card1_p="Every day is mapped out &mdash; Old Testament, New Testament, and Psalms or Proverbs. Just open to today's date.",
        card2_h="Fits real life", card2_p="Each day's reading takes 10&ndash;15 minutes, built to fit around work, kids, and everything in between.",
        card3_h="52 reflection pages", card3_p="A simple weekly S.O.A.P. page to slow down and write out what God is showing you.",
        inside_h2="What's Inside", inside_sub="A 66-page printable/digital journal, instantly downloadable.",
        th_day="Day", th_ot="Old Testament", th_nt="New Testament", th_wisdom="Psalms / Proverbs",
        row1_ot="Genesis 1-3", row1_nt="Matthew 1", row1_wisdom="Psalms 1",
        row2_ot="Genesis 4-5", row2_nt="Matthew 2",
        row3_ot="Genesis 6-7", row3_nt="Matthew 3", row3_wisdom="Psalms 2",
        pricing_h2="Get Your Journal", was_price="$19", price="$12",
        feature1="365-day reading plan (OT + NT + Psalms/Proverbs)",
        feature2="52 weekly S.O.A.P. reflection pages",
        feature3="Instant digital download (PDF, print or use on tablet)",
        cta_price="Get Instant Access",
        faq_h2="FAQ",
        faq1_q="What Bible translation do I need?", faq1_a="We recommend the ESV, but any translation works &mdash; the plan lists book and chapter only, so use whatever Bible or app you already have.",
        faq2_q="Is this printable?", faq2_a="Yes. It's a standard letter-size PDF you can print at home, in a planner, or use digitally on a tablet.",
        faq3_q="What if I fall behind?", faq3_a="There's no catching up required &mdash; the plan is built by calendar day, so you just pick back up on today's date.",
        footer="&copy; 4-13 Bible Study Co. &middot; This is a digital download, delivered instantly after purchase.",
    ),
    "spanish-men": dict(
        html_lang="es",
        title="El Viaje de un Hombre por la Palabra",
        dark="#1F2A38", accent="#8C6A3F", light="#EDEAE3",
        tag="Plan de Lectura B\u00edblica de 365 D\u00edas",
        h1="El Viaje de un Hombre por la Palabra",
        hero_sub="Una forma simple y sin excusas de leer toda la Biblia en un a\u00f1o &mdash; 10 a 15 minutos al d\u00eda, con un diario gu\u00eda hecho para la constancia.",
        translation_note="Traducci\u00f3n recomendada: LBLA (La Biblia de las Am\u00e9ricas)",
        cta_hero="Consigue el Diario &mdash; $12",
        section1_h2="Deja de empezar de nuevo en G\u00e9nesis 3.",
        section1_sub="No necesitas m\u00e1s fuerza de voluntad. Necesitas un plan que realmente termines.",
        card1_h="Sin adivinar", card1_p="Cada d\u00eda est\u00e1 planificado para ti &mdash; Antiguo Testamento, Nuevo Testamento, y Salmos o Proverbios. Solo abre en la fecha de hoy.",
        card2_h="Hecho para hombres ocupados", card2_p="Cada lectura diaria toma de 10 a 15 minutos. No necesitas una ma\u00f1ana perfecta &mdash; solo constancia.",
        card3_h="52 p\u00e1ginas de reflexi\u00f3n", card3_p="Una p\u00e1gina semanal con el m\u00e9todo S.O.A.P. para aplicar de verdad lo que est\u00e1s leyendo.",
        inside_h2="Qu\u00e9 Incluye", inside_sub="Un diario digital/imprimible de 66 p\u00e1ginas, de descarga instant\u00e1nea.",
        th_day="D\u00eda", th_ot="Antiguo Testamento", th_nt="Nuevo Testamento", th_wisdom="Salmos / Proverbios",
        row1_ot="G\u00e9nesis 1-3", row1_nt="Mateo 1", row1_wisdom="Salmos 1",
        row2_ot="G\u00e9nesis 4-5", row2_nt="Mateo 2",
        row3_ot="G\u00e9nesis 6-7", row3_nt="Mateo 3", row3_wisdom="Salmos 2",
        pricing_h2="Consigue Tu Diario", was_price="$19", price="$12",
        feature1="Plan de lectura de 365 d\u00edas (AT + NT + Salmos/Proverbios)",
        feature2="52 p\u00e1ginas semanales de reflexi\u00f3n S.O.A.P.",
        feature3="Descarga digital instant\u00e1nea (PDF, para imprimir o usar en tablet)",
        cta_price="Obtener Acceso Instant\u00e1neo",
        faq_h2="Preguntas Frecuentes",
        faq1_q="\u00bfQu\u00e9 traducci\u00f3n de la Biblia necesito?", faq1_a="Recomendamos la LBLA, pero cualquier traducci\u00f3n funciona &mdash; el plan solo indica libro y cap\u00edtulo, as\u00ed que puedes usar la Biblia o app que ya tengas.",
        faq2_q="\u00bfEsto se puede imprimir?", faq2_a="S\u00ed. Es un PDF tama\u00f1o carta est\u00e1ndar que puedes imprimir en casa o en una imprenta, o usar digitalmente en una tablet.",
        faq3_q="\u00bfY si me atraso?", faq3_a="El plan est\u00e1 organizado por fecha del calendario, no por presi\u00f3n secuencial &mdash; solo retoma en la fecha de hoy, sin necesidad de ponerte al d\u00eda.",
        footer="&copy; 4-13 Bible Study Co. &middot; Esta es una descarga digital, entregada al instante tras la compra.",
    ),
    "spanish-women": dict(
        html_lang="es",
        title="El Viaje de una Mujer por la Palabra",
        dark="#4A3B3B", accent="#B48A78", light="#F5EDE8",
        tag="Plan de Lectura B\u00edblica de 365 D\u00edas",
        h1="El Viaje de una Mujer por la Palabra",
        hero_sub="Una forma realista y sin culpa de leer toda la Biblia en un a\u00f1o &mdash; 10 a 15 minutos al d\u00eda, con un diario gu\u00eda que se adapta a la vida real.",
        translation_note="Traducci\u00f3n recomendada: LBLA (La Biblia de las Am\u00e9ricas)",
        cta_hero="Consigue el Diario &mdash; $12",
        section1_h2="Sin culpa. Sin atrasos. Solo una pr\u00f3xima p\u00e1gina.",
        section1_sub="Un ritmo que realmente puedas mantener, incluso en los d\u00edas ocupados e imperfectos.",
        card1_h="Sin adivinar", card1_p="Cada d\u00eda est\u00e1 planificado &mdash; Antiguo Testamento, Nuevo Testamento, y Salmos o Proverbios. Solo abre en la fecha de hoy.",
        card2_h="Se adapta a tu vida", card2_p="Cada lectura diaria toma de 10 a 15 minutos, pensada para encajar entre el trabajo, los hijos y todo lo dem\u00e1s.",
        card3_h="52 p\u00e1ginas de reflexi\u00f3n", card3_p="Una p\u00e1gina semanal con el m\u00e9todo S.O.A.P. para detenerte y escribir lo que Dios te est\u00e1 mostrando.",
        inside_h2="Qu\u00e9 Incluye", inside_sub="Un diario digital/imprimible de 66 p\u00e1ginas, de descarga instant\u00e1nea.",
        th_day="D\u00eda", th_ot="Antiguo Testamento", th_nt="Nuevo Testamento", th_wisdom="Salmos / Proverbios",
        row1_ot="G\u00e9nesis 1-3", row1_nt="Mateo 1", row1_wisdom="Salmos 1",
        row2_ot="G\u00e9nesis 4-5", row2_nt="Mateo 2",
        row3_ot="G\u00e9nesis 6-7", row3_nt="Mateo 3", row3_wisdom="Salmos 2",
        pricing_h2="Consigue Tu Diario", was_price="$19", price="$12",
        feature1="Plan de lectura de 365 d\u00edas (AT + NT + Salmos/Proverbios)",
        feature2="52 p\u00e1ginas semanales de reflexi\u00f3n S.O.A.P.",
        feature3="Descarga digital instant\u00e1nea (PDF, para imprimir o usar en tablet)",
        cta_price="Obtener Acceso Instant\u00e1neo",
        faq_h2="Preguntas Frecuentes",
        faq1_q="\u00bfQu\u00e9 traducci\u00f3n de la Biblia necesito?", faq1_a="Recomendamos la LBLA, pero cualquier traducci\u00f3n funciona &mdash; el plan solo indica libro y cap\u00edtulo, as\u00ed que puedes usar la Biblia o app que ya tengas.",
        faq2_q="\u00bfEsto se puede imprimir?", faq2_a="S\u00ed. Es un PDF tama\u00f1o carta est\u00e1ndar que puedes imprimir en casa, guardar en tu planner, o usar digitalmente en una tablet.",
        faq3_q="\u00bfY si me atraso?", faq3_a="No hay que ponerse al d\u00eda &mdash; el plan est\u00e1 organizado por fecha del calendario, as\u00ed que solo retomas en la fecha de hoy.",
        footer="&copy; 4-13 Bible Study Co. &middot; Esta es una descarga digital, entregada al instante tras la compra.",
    ),
}

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, ctx in VARIANTS.items():
        html = TEMPLATE.format(**ctx)
        path = os.path.join(OUT_DIR, f"{name}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote {path}")

