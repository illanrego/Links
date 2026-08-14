# Portfolio identity reuse brief

## Purpose

Make the links site and developer portfolio feel like parts of the same Illan Rego system without making them the same page.

Source of truth:

- `/home/illan/Documents/coding/portfolio`
- Reference commit: `d385dfe Use existing Startpage screenshot`
- Main files: `index.html`, `styles.css`, `script.js`, `DESIGN_SPEC.md`

The portfolio uses retro hardware as visual grammar. The links site should reuse that grammar in a compact personal-hub composition.

## Exact token baseline

Start from the portfolio’s CSS variables:

```css
--ink: #08111f;
--navy: #071a33;
--navy-deep: #04101f;
--navy-mid: #0b2b55;
--paper: #eaf3ff;
--panel: #f7fbff;
--grid: #c6d9f5;
--blue: #2f6bff;
--blue-dark: #183b8f;
--cyan: #8ce8ff;
--cyan-dark: #2b7f9d;
--border: 3px solid var(--ink);
--shadow: 7px 7px 0 var(--ink);
```

Typography:

- `Press Start 2P` — identity display type; use sparingly because this page is narrow.
- `Silkscreen` — controls, labels, kickers, status text.
- `VT323` — readable body copy.

Keep square geometry, 3–4px dark borders, and hard zero-blur shadows. Avoid the old site’s rounded glass cards, backdrop blur, soft glow halos, and generic cyberpunk gradients.

## Good component candidates

### 1. Brand indicator

Portfolio selectors: `.brand`, `.brand-light`, `.brand-light::after`.

Adaptation: use the square blue/cyan status light beside `ILLAN.REGO` or `ILLAN` in the profile header. A full sticky portfolio header is unnecessary on a short links page.

### 2. Pixel action controls

Portfolio selectors: `.pixel-button`, `.pixel-button-primary`, `.pixel-button-secondary`, plus the shared active pressed state.

Adaptation: use for one primary CTA and perhaps one secondary professional/contact action. Do not turn every link into a giant button with equal emphasis.

### 3. Terminal framing

Portfolio selectors: `.profile-terminal`, `.terminal-bar`, `.terminal-status`, `.terminal-body`.

Adaptation: reuse the striped terminal bar and hard frame around the profile/identity panel or around one priority module. Simplify the content; do not import the portfolio’s developer skill table.

### 4. Compact card shell

Portfolio selectors: `.project-card`, `.project-card-media`, `.project-card-body`, `.project-links`.

Adaptation: strip the screenshot/proof structure and use the shell for compact link modules with:

- Small category label.
- Clear link title.
- One short purpose line.
- Square arrow/status affordance.

The links page should stay one narrow column on mobile, potentially two columns for secondary links on wider screens.

### 5. Section kicker

Portfolio selector: `.section-kicker` and its `Silkscreen` treatment.

Adaptation: use short labels such as `WATCH`, `FOLLOW`, `PLAY / USE`, or `WORK / CONTACT` only if those groups survive content discovery.

### 6. Texture and decoration

Portfolio selectors: `.intro-scanlines`, `.contact-scanlines`, `.float-tile`, `.tile-code`, `.tile-ai`.

Adaptation:

- Use sparse CRT scanlines at low opacity.
- Use the navy/pixel-dot or grid background.
- At most one or two small floating tiles near the profile frame.
- Never let decoration collide with portrait, text, or controls.

### 7. Optional SFX

Portfolio source: `script.js`, `.sfx-control`, `.sfx-screen`.

Do not copy by default. Only add if Illan explicitly wants continuity with the portfolio. If used: off by default, user-controlled, `aria-pressed`, persisted under a links-specific storage key, and no autoplay.

## Composition differences from the portfolio

The links site should not reuse:

- The sticky three-column header.
- The giant two-column developer hero.
- The six-project grid.
- Engineering proof boxes.
- The introduction → projects → contact architecture.
- Recruiter-specific availability and stack copy.

Instead, use a narrow personal-hub composition optimized for one-handed mobile use:

1. Profile identity surface.
2. One current priority item.
3. Compact grouped links.
4. Social/contact controls.
5. Optional media preview/footer.

## Existing content requiring decisions

Current `index.html` contains:

- Instagram: `https://instagram.com/instadoillan`
- X/Twitter: `https://twitter.com/tuiterdoillan`
- YouTube currently written as `https://youtube.com/canaldoillan`
- Two June show cards with date-specific URLs.
- `Canal do Illan` with `href="#"`.
- Disabled Open Mic RPG card.
- Two YouTube embeds.
- A short comedian/developer about paragraph.

Treat all of these as candidates, not guaranteed final content. Verify URLs and ask Illan for current priorities before editing.

## Responsive and accessibility acceptance

- Mobile reference viewport: true `390×844`.
- No horizontal overflow.
- 44px minimum interactive targets.
- Visible focus indicators using cyan.
- One descriptive H1.
- Semantic sections and navigation labels.
- External blank-target links use `rel="noreferrer"`.
- Respect `prefers-reduced-motion` and remove decorative animation/scanlines there.
- No automatic audio.

## Deployment warning

The current repo includes `CNAME` = `www.sitedoillan.com.br`, while the apex domain is intended for the portfolio. As of 2026-08-14, `www.sitedoillan.com.br` resolves to GitHub Pages but returns 404. Do not treat hostname/deployment as solved and do not change it without explicit approval.
