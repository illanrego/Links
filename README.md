# Illan Carvalho — links oficiais

Static, dependency-free personal links hub for Illan Carvalho.

## Current direction

- Creator/follower-first, with a compact link-in-bio information hierarchy.
- Primary CTA: Open Mic RPG.
- Portuguese (pt-BR) copy.
- Blue pixel/CRT identity shared with the sibling developer portfolio.
- One narrow vertical flow: compact profile → priority CTA → main links → secondary comedy channels → current projects/sites → contact.
- Current public project links include Will's Locadora, Encounters Guide v1.0.1, CCAPP, and GitHub.

## Repository

- GitHub: https://github.com/illanrego/Links
- Static implementation: `index.html` + `styles.css`
- No build step or client-side JavaScript.

## Local development

```bash
python3 -m http.server 4178 --bind 127.0.0.1
```

Then open `http://127.0.0.1:4178/`.

## Static checks

```bash
python3 scripts/static-checks.py
```

## Deployment note

`CNAME` still contains the historical `www.sitedoillan.com.br`. The intended links hostname remains unresolved. Do not change CNAME, DNS, GitHub Pages, push, or deploy without Illan's explicit approval.
