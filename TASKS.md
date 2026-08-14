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

## Now — discovery before implementation

### A. Content and audience

- [ ] Confirm whether this page primarily serves comedy fans, general personal identity, or mixed creator/developer traffic.
- [ ] Confirm the single current priority CTA.
- [ ] Inventory the exact active links and desired order.
- [ ] Decide whether show listings remain dynamic/manual, become one generic ticket CTA, or are removed.
- [ ] Decide whether the two embedded stand-up videos stay, become thumbnails, or move behind one channel link.
- [ ] Confirm site language.

### B. Domain and deployment

- [ ] Decide between the existing `www.sitedoillan.com.br` and a dedicated links hostname such as `links.sitedoillan.com.br`.
- [ ] Preserve `sitedoillan.com.br` for the developer portfolio.
- [ ] Make no CNAME, DNS, Pages, push, or deployment changes until explicitly approved.

## Implementation after approval

### C. Identity and layout

- [ ] Build a compact mobile-first profile surface.
- [ ] Apply the portfolio’s blue pixel/CRT tokens.
- [ ] Adapt only useful components documented in `PORTFOLIO_REUSE_BRIEF.md`.
- [ ] Keep the link page visually related to the portfolio but compositionally distinct.

### D. Link system

- [ ] Create a clear hierarchy for priority, content, product, professional, and social links.
- [ ] Remove all stale dates, dead placeholders, and invalid URLs.
- [ ] Keep interactive controls at least 44px and keyboard accessible.

### E. Verification

- [ ] Add focused static checks for structure, URL safety, accessibility hooks, and local assets.
- [ ] Verify at true `390×844` and desktop.
- [ ] Verify every external URL and local resource.
- [ ] Check console errors, focus behavior, reduced motion, and content overflow.
- [ ] Commit verified changes locally.

## Explicitly out of scope until approved

- Deployment or DNS changes.
- Rebuilding the developer portfolio inside this repo.
- A CMS, analytics stack, framework migration, or backend.
- Automatic event scraping.
- Automatic audio.

## Next session start here

1. Load `marketing-page-visual-polish` and `hermes-hub`.
2. Work from this repository.
3. Read `.hermes.md`, `AGENTS.md`, this file, and `PORTFOLIO_REUSE_BRIEF.md`.
4. Inspect the current site and sibling portfolio.
5. Present a concise recommended link hierarchy and ask only for the missing content decisions.
6. Wait for Illan’s green light before changing UI code.
