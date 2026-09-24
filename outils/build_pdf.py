import markdown, re, sys, pathlib
R = pathlib.Path("/home/user/Mon-projet-")
sections = [
    ("Prospects du jour — Gardanne", R/"prospects/2026-09-24-gardanne.md"),
    ("Argumentaires par prospect", R/"prospects/2026-09-24-gardanne-argumentaires.md"),
    ("Profils cibles par formation", R/"ciblage/profils-cibles.md"),
    ("Argumentaires généraux et objections", R/"ciblage/argumentaires.md"),
    ("Modèles de prise de contact", R/"modeles/messages.md"),
]
md = markdown.Markdown(extensions=["tables", "sane_lists"])
parts = []
toc = []
for i, (title, path) in enumerate(sections, 1):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^# .*\n", "", text, count=1)  # drop file H1, we set our own
    # python-markdown needs a blank line before a list that follows a paragraph
    lines = text.split("\n"); fixed = []
    for j, ln in enumerate(lines):
        if re.match(r"^\s*[-*] ", ln) and j > 0 and lines[j-1].strip() and not re.match(r"^\s*[-*] |^\s*\d+\. ", lines[j-1]):
            fixed.append("")
        fixed.append(ln)
    text = "\n".join(fixed)
    html = md.convert(text); md.reset()
    parts.append(f'<section class="part" id="p{i}"><h1><span class="num">{i}</span>{title}</h1>{html}</section>')
    toc.append(f'<li><span class="num">{i}</span>{title}</li>')

css = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; margin: 0; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.cover .kicker { font-size: 11pt; letter-spacing: .18em; text-transform: uppercase; color: #b3541e; font-weight: 700; }
.cover h1 { font-size: 34pt; line-height: 1.1; margin: 8mm 0 4mm; color: #14213d; }
.cover .sub { font-size: 14pt; color: #444; margin-bottom: 14mm; }
.cover ol { list-style: none; padding: 0; margin: 0; font-size: 12.5pt; }
.cover ol li { padding: 3mm 0; border-top: 1px solid #ddd; }
.cover ol li:last-child { border-bottom: 1px solid #ddd; }
.cover .foot { margin-top: 16mm; font-size: 9.5pt; color: #666; }
.num { display: inline-block; min-width: 9mm; color: #b3541e; font-weight: 700; }
.part { page-break-before: always; }
.part h1 { font-size: 22pt; color: #14213d; border-bottom: 3px solid #b3541e; padding-bottom: 2mm; margin: 0 0 6mm; }
h2 { font-size: 15pt; color: #14213d; margin: 9mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 12pt; color: #b3541e; margin: 6mm 0 2mm; page-break-after: avoid; }
h3 + p, h3 + ul { page-break-before: avoid; }
p { margin: 0 0 2.2mm; }
ul, ol { margin: 0 0 2.5mm; padding-left: 5mm; }
li { margin-bottom: 1mm; }
strong { color: #14213d; }
blockquote { margin: 2mm 0 3mm; padding: 2.5mm 4mm; border-left: 3px solid #b3541e; background: #faf5f0; font-style: italic; page-break-inside: avoid; }
blockquote p { margin: 0 0 1.5mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm; font-size: 9.5pt; page-break-inside: auto; }
th, td { border: 1px solid #cfcfcf; padding: 1.6mm 2.2mm; vertical-align: top; text-align: left; }
th { background: #14213d; color: #fff; font-weight: 600; }
tr { page-break-inside: avoid; }
hr { border: 0; border-top: 1px solid #ddd; margin: 5mm 0; }
code { font-family: Menlo, Consolas, monospace; font-size: 9pt; background: #f2f2f2; padding: 0 1mm; }
/* each prospect block: keep heading with its first lines */
section#p2 h3 { page-break-before: auto; margin-top: 7mm; }
"""
cover = f"""
<div class="cover">
  <div class="kicker">Digit Formations · Prospection locale</div>
  <h1>Gardanne<br>24 septembre 2026</h1>
  <div class="sub">22 prospects qualifiés, argumentaires individuels, ciblage et modèles de contact</div>
  <ol>{''.join(toc)}</ol>
  <div class="foot">Sources : Registre National des Entreprises (infosociétés by Contract-Factory), Pages Jaunes, Mappy, sites des entreprises. Coordonnées = numéros professionnels publics.<br>Contact Digit Formations : Adrien Montier · 06 66 09 80 20 · adrien@digit-formations.fr</div>
</div>"""
doc = f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Prospection Gardanne 24-09-2026</title><style>{css}</style></head><body>{cover}{''.join(parts)}</body></html>"
out = pathlib.Path(sys.argv[1]); out.write_text(doc, encoding="utf-8"); print("html", out, len(doc))
