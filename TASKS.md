# Illan Links — live ship board

Status legend: `[ ]` todo · `[~]` in progress · `[x]` done

## Done

- [x] Confirm target repository is `illanrego/Links` and clone it to `/home/illan/Documents/coding/Links`.
- [x] Preserve the blue pixel/CRT identity and compact stage portrait.
- [x] Replace the mini-portfolio layout with a true narrow link-in-bio flow.
- [x] Remove the fake ONLINE status and oversized profile hero treatment.
- [x] Keep Open Mic RPG as the single priority CTA.
- [x] Update creator links and channel roles.
- [x] Add current public projects/sites: Will's Locadora, Encounters Guide v1.0.1, CCAPP, and GitHub.
- [x] Omit the course until it has a real public landing/checkout URL.
- [x] Omit authenticated/personal-only Startpage from public links.
- [x] Verify static checks, local index/CSS/assets, and all 11 exposed external URLs.
- [x] Correct stale repo paths and baselines in README and `.hermes.md`.

## Awaiting Illan review

- [ ] Manual visual check at mobile 390×844 and desktop.
- [ ] Approve or edit link order/copy.
- [ ] Decide whether the current email remains the public contact.

## Deployment — not approved

- [ ] Decide final hostname. `links.sitedoillan.com.br` currently does not resolve; `CNAME` still says `www.sitedoillan.com.br`.
- [ ] Preserve `sitedoillan.com.br` for the developer portfolio.
- [ ] Do not change CNAME, DNS, Pages, push, or deploy until Illan explicitly says to.

## Next session start here

1. Run `python3 -m http.server 4178 --bind 127.0.0.1`.
2. Let Illan review the page visually.
3. Apply focused copy/order/spacing changes from that review.
4. Run `python3 scripts/static-checks.py` before commit.
5. Commit verified work locally; push only on explicit `push it`.
