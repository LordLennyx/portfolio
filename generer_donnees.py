# Rassemble les projet.json + spot.json de chaque dossier en un fichier de données pour le hub portfolio.
import json, pathlib, re
R = pathlib.Path(__file__).resolve().parents[1]
out = []
for d in sorted(R.glob("[0-9][0-9]-*")):
    pj, sj = d / "projet.json", d / "spot.json"
    if not pj.exists() or d.name == "20-hub-portfolio":
        continue
    p = json.loads(pj.read_text(encoding="utf-8")); s = json.loads(sj.read_text(encoding="utf-8")) if sj.exists() else {}
    out.append({"n": int(d.name[:2]), "dir": d.name, "repo": p["repo"], "nom": p["nom"], "type": p["type"], "cat": p["categorie"], "resume": p["resume"],
                "fonctions": p["fonctions"], "stack": p["stack"], "couleur": s.get("couleur", "#222"),
                "accroche": re.sub("<[^>]+>", "", s.get("sous_titre", ""))})
autres = [
    {"nom": "Lennyx", "type": "To-do list gamifiée · Windows, Android, PWA", "url": "https://lordlennyx.github.io/lennyx/"},
    {"nom": "MboaLang", "type": "Application d'apprentissage des langues camerounaises", "url": "https://github.com/LordLennyx/mboalang-app"},
    {"nom": "K2DT Archives", "type": "Gestion électronique des archives · FastAPI, PostgreSQL, OCR", "url": "https://github.com/LordLennyx/k2dt-archives"},
    {"nom": "K2DT Project", "type": "Gestion de projets et facturation multi-sociétés · PHP, MySQL", "url": "https://github.com/LordLennyx/k2dt-project"},
    {"nom": "CleanSpot", "type": "Propreté urbaine · React, Firebase, Leaflet", "url": "https://github.com/LordLennyx/cleanspot"},
    {"nom": "TechFix", "type": "Gestion de réparations · Spring Boot, JWT, PDF", "url": "https://github.com/LordLennyx/techfix"},
]
(R / "20-hub-portfolio" / "donnees.js").write_text("window.PROJETS=" + json.dumps(out, ensure_ascii=False) + ";\nwindow.AUTRES=" + json.dumps(autres, ensure_ascii=False) + ";\n", encoding="utf-8")
print(len(out), "projets")
