# Illan — links oficiais

Static, dependency-free personal links hub for Illan.

Current redesign direction:

- Comedy-fan / follower-first audience.
- Primary CTA: Open Mic RPG.
- Copy language: Portuguese (pt-BR).
- Visual identity: blue pixel/CRT system shared with the sibling developer portfolio.
- Intended future hostname: `links.sitedoillan.com.br`.

Important deployment note: this repository still contains the old `CNAME` until Illan explicitly authorizes DNS / GitHub Pages changes. Do not push, deploy, edit CNAME, or change DNS without approval.

## Local development

```bash
python3 -m http.server 4178 --bind 127.0.0.1
```

Then open `http://127.0.0.1:4178/`.

## Static checks

```bash
python3 scripts/static-checks.py
```
