import csv
import re

PRODUCT_DIR = r"C:\Users\julia\Desktop\4-13\product"

BOOK_ES = {
    "Genesis": "Génesis", "Exodus": "Éxodo", "Leviticus": "Levítico", "Numbers": "Números",
    "Deuteronomy": "Deuteronomio", "Joshua": "Josué", "Judges": "Jueces", "Ruth": "Rut",
    "1 Samuel": "1 Samuel", "2 Samuel": "2 Samuel", "1 Kings": "1 Reyes", "2 Kings": "2 Reyes",
    "1 Chronicles": "1 Crónicas", "2 Chronicles": "2 Crónicas", "Ezra": "Esdras", "Nehemiah": "Nehemías",
    "Esther": "Ester", "Job": "Job", "Ecclesiastes": "Eclesiastés", "Song of Solomon": "Cantar de los Cantares",
    "Isaiah": "Isaías", "Jeremiah": "Jeremías", "Lamentations": "Lamentaciones", "Ezekiel": "Ezequiel",
    "Daniel": "Daniel", "Hosea": "Oseas", "Joel": "Joel", "Amos": "Amós", "Obadiah": "Abdías",
    "Jonah": "Jonás", "Micah": "Miqueas", "Nahum": "Nahúm", "Habakkuk": "Habacuc",
    "Zephaniah": "Sofonías", "Haggai": "Hageo", "Zechariah": "Zacarías", "Malachi": "Malaquías",
    "Matthew": "Mateo", "Mark": "Marcos", "Luke": "Lucas", "John": "Juan", "Acts": "Hechos",
    "Romans": "Romanos", "1 Corinthians": "1 Corintios", "2 Corinthians": "2 Corintios",
    "Galatians": "Gálatas", "Ephesians": "Efesios", "Philippians": "Filipenses", "Colossians": "Colosenses",
    "1 Thessalonians": "1 Tesalonicenses", "2 Thessalonians": "2 Tesalonicenses",
    "1 Timothy": "1 Timoteo", "2 Timothy": "2 Timoteo", "Titus": "Tito", "Philemon": "Filemón",
    "Hebrews": "Hebreos", "James": "Santiago", "1 Peter": "1 Pedro", "2 Peter": "2 Pedro",
    "1 John": "1 Juan", "2 John": "2 Juan", "3 John": "3 Juan", "Jude": "Judas",
    "Revelation": "Apocalipsis", "Psalms": "Salmos", "Proverbs": "Proverbios",
}

# sort keys longest-first so "1 Corinthians" matches before "Corinthians"-style partials
BOOK_KEYS = sorted(BOOK_ES.keys(), key=len, reverse=True)

SEGMENT_RE = re.compile(r"^(.*\D)\s(\d+(?:-\d+)?)$")


def translate_segment(seg):
    m = SEGMENT_RE.match(seg.strip())
    if not m:
        return seg
    book, chnum = m.group(1), m.group(2)
    es = BOOK_ES.get(book)
    if es is None:
        raise ValueError(f"Unmapped book: {book!r}")
    return f"{es} {chnum}"


def translate_cell(cell):
    if not cell:
        return cell
    parts = [p.strip() for p in cell.split(";")]
    return "; ".join(translate_segment(p) for p in parts if p)


def main():
    rows = []
    with open(f"{PRODUCT_DIR}\\reading-plan.csv", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "Day": r["Day"],
                "OldTestament": translate_cell(r["OldTestament"]),
                "NewTestament": translate_cell(r["NewTestament"]),
                "Wisdom": translate_cell(r["Wisdom"]),
            })

    with open(f"{PRODUCT_DIR}\\reading-plan-es.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["Day", "OldTestament", "NewTestament", "Wisdom"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to reading-plan-es.csv")


if __name__ == "__main__":
    main()
