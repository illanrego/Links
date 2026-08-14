# AGENTS.md

## Mission

Modernize this existing static personal-links site into a fast, mobile-first hub that shares Illan’s developer portfolio identity while retaining link-page information architecture.

## Architecture

- `index.html` — all content and semantic structure.
- `styles.css` — all visual and responsive behavior.
- `imagens/` — existing local imagery and icons.
- `CNAME` — deployment hostname; do not change without explicit approval.
- `PORTFOLIO_REUSE_BRIEF.md` — exact visual/component adaptation guide.
- `TASKS.md` — live project board.
- Sibling visual reference: `../portfolio/`.

## Design rules

- Reuse visual grammar, not page choreography.
- Preserve the portfolio palette, pixel typography, hard square borders, zero-blur shadows, sparse scanlines, and tactile pressed states.
- Keep this narrower, simpler, and more thumb-friendly than the portfolio.
- Reuse/adapt small components such as terminal bars, square icon controls, pixel buttons, and compact card shells.
- Do not copy the portfolio’s large hero, project grid, proof panels, or recruiter-oriented section structure.
- Avoid rounded glass cards, blur halos, generic gradients, fake live indicators, pills, and ornamental AI-template styling.

## Content and safety rules

- Verify every URL before exposing it.
- Remove stale show dates and `href="#"` placeholders rather than disguising them as active links.
- Ask Illan to confirm the current priority CTA and final link order before implementation.
- Keep site copy audience-appropriate; do not force developer-portfolio wording into a creator-facing links page.
- No automatic audio. Any SFX must be optional, off by default, and accessible.
- Do not change CNAME, DNS, GitHub Pages settings, push, or deploy without explicit approval.

## Accessibility and responsive baseline

- Semantic landmarks and one clear H1.
- Skip link and visible `:focus-visible` treatment.
- Minimum 44px interactive targets.
- Descriptive accessible labels; decorative imagery hidden from assistive tech.
- `target="_blank"` links use `rel="noreferrer"`.
- Respect `prefers-reduced-motion`.
- Verify at a real `390×844` viewport and on desktop.

## Development

```bash
python3 -m http.server 4178 --bind 127.0.0.1
```

Keep the site static and dependency-free unless a real requirement justifies additional tooling. Add focused automated static checks during implementation.
