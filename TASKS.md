# Illan Links — live ship board

Last updated: 2026-08-14
Status legend: `[ ]` todo · `[~]` in progress · `[x]` done

## Done

- [x] Identify the existing repository: `illanrego/illanrego.github.io`.
- [x] Clone it to `/home/illan/Documents/coding/illanrego.github.io`.
- [x] Audit the existing static HTML/CSS structure.
- [x] Confirm current `CNAME` is `www.sitedoillan.com.br`.
- [x] Confirm DNS points to GitHub Pages but the current site returns 404.
- [x] Map the portfolio visual tokens and reusable component candidates.
- [x] Add fresh-chat context files; no UI code changed.
- [x] Confirm audience, priority CTA, link inventory, site language, and future hostname.
- [x] Rebuild the links site as a compact pt-BR comedy-fan hub using the portfolio blue pixel/CRT identity.
- [x] Remove stale show cards, placeholder links, disabled Open Mic RPG card, old embeds, and unrelated README copy.
- [x] Add focused static checks, favicon, semantic/a11y improvements, and verified real links.
- [x] Verify static checks, URL checks, desktop/mobile screenshots, console/resources, no horizontal overflow, and 44px controls.

## Now — discovery before implementation

### A. Content and audience

- [x] Confirm whether this page primarily serves comedy fans, general personal identity, or mixed creator/developer traffic.
- [x] Confirm the single current priority CTA.
- [x] Inventory the exact active links and desired order.
- [x] Decide whether show listings remain dynamic/manual, become one generic ticket CTA, or are removed.
- [x] Decide whether the two embedded stand-up videos stay, become thumbnails, or move behind one channel link.
- [x] Confirm site language.

### B. Domain and deployment

- [x] Decide between the existing `www.sitedoillan.com.br` and a dedicated links hostname such as `links.sitedoillan.com.br`.
- [ ] Preserve `sitedoillan.com.br` for the developer portfolio.
- [ ] Make no CNAME, DNS, Pages, push, or deployment changes until explicitly approved.

## Implementation after approval

### C. Identity and layout

- [x] Build a compact mobile-first profile surface.
- [x] Apply the portfolio’s blue pixel/CRT tokens.
- [x] Adapt only useful components documented in `PORTFOLIO_REUSE_BRIEF.md`.
- [x] Keep the link page visually related to the portfolio but compositionally distinct.

### D. Link system

- [x] Create a clear hierarchy for priority, content, product, professional, and social links.
- [x] Remove all stale dates, dead placeholders, and invalid URLs.
- [x] Keep interactive controls at least 44px and keyboard accessible.

### E. Verification

- [x] Add focused static checks for structure, URL safety, accessibility hooks, and local assets.
- [x] Verify at true `390×844` and desktop.
- [x] Verify every external URL and local resource.
- [x] Check console errors, focus behavior, reduced motion, and content overflow.
- [x] Commit verified changes locally.

## Explicitly out of scope until approved

- Deployment or DNS changes.
- Rebuilding the developer portfolio inside this repo.
- A CMS, analytics stack, framework migration, or backend.
- Automatic event scraping.
- Automatic audio.

## Next session start here

1. Review the committed redesign locally with `python3 -m http.server 4178 --bind 127.0.0.1`.
2. If Illan wants deployment, ask for explicit authorization before changing `CNAME`, GitHub Pages, DNS, pushing, or deploying.
3. Intended future hostname decision is `links.sitedoillan.com.br`; current `CNAME` is intentionally still unchanged until authorized.
