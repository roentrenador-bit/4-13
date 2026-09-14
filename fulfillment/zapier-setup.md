# Fulfillment Setup — Stripe → Zapier → Email Delivery

This delivers the PDF automatically by email right after a successful Stripe payment, without exposing the files publicly. You'll do this in your own Stripe and Zapier accounts — the steps below are exact copy/paste values.

## 1. Host the 4 PDFs somewhere Zapier can fetch them

Zapier's email action attaches a file by URL, so the PDFs need a link — but NOT a public, linked-from-your-site URL (that would let anyone download without paying).

- Upload each PDF to Google Drive.
- Right-click → Share → "Anyone with the link" → Viewer. Copy the link.
- Convert each share link to a **direct-download** link: replace
  `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`
  with
  `https://drive.google.com/uc?export=download&id=FILE_ID`
- Do this for all 4 files:
  - `product/bible-in-a-year-english-men.pdf`
  - `product/bible-in-a-year-english-women.pdf`
  - `product/bible-in-a-year-spanish-men.pdf`
  - `product/bible-in-a-year-spanish-women.pdf`
- Keep these links out of the public repo/landing pages — they should only ever live inside the Zap.

## 2. In Stripe (dashboard.stripe.com)

For each of the 4 products' Payment Links:
- Under "After payment," set the confirmation message to something like: *"Thank you! Check your email in the next minute for your download link."* (No redirect needed — email handles delivery.)

## 3. In Zapier (zapier.com)

Connect your Stripe account to Zapier (OAuth login — Zapier never asks for your raw API key for this).

Create **4 separate Zaps**, one per product:

**Trigger:** Stripe → "New Payment" (or "Checkout Session Completed" if offered — test to see which fires for your Payment Links) → connect your Stripe account.

**Filter step:** Only continue if `Price ID` (or `Product Name`) equals the specific product for this Zap. (Get the exact Price ID from Stripe's product page — looks like `price_1AbC...`.)

**Action:** Gmail (or Zapier's built-in "Email") → Send Email
- To: `{{Customer Email}}` from the trigger
- Subject / Body: use the templates below
- Attachment: the direct-download Google Drive URL for the matching PDF

Test each Zap with a Stripe test-mode payment before turning it on live.

---

## Email Templates

### English (men's or women's edition — same template, different attachment)

**Subject:** Your Bible Reading Plan Is Here 📖

**Body:**
```
Hi {{Customer Name}},

Thank you for your purchase! Your journal is attached to this email.

Getting started:
1. Print it, or use it digitally on a tablet.
2. Open to today's date and start your first reading.
3. Use the weekly S.O.A.P. pages in the back any time a passage speaks to you.

If your download doesn't work, just reply to this email and we'll resend it.

Enjoy the journey through the Word.
```

### Spanish (ediciones para hombres o mujeres)

**Asunto:** Tu Plan de Lectura Bíblica Ya Está Aquí 📖

**Cuerpo:**
```
Hola {{Customer Name}},

¡Gracias por tu compra! Tu diario está adjunto a este correo.

Para comenzar:
1. Imprímelo, o úsalo digitalmente en una tablet.
2. Abre en la fecha de hoy y comienza tu primera lectura.
3. Usa las páginas semanales S.O.A.P. al final cuando un pasaje te hable de forma especial.

Si tu descarga no funciona, responde a este correo y te lo reenviamos.

Disfruta el viaje por la Palabra.
```

---

## Once this is live

Send me the 4 Stripe Payment Link URLs and I'll wire the "Get Instant Access" buttons on each landing page to the correct checkout link.
