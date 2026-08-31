# CT Private Office / Tax 4 Pros — funnel pages

Static pages served behind `apply.ctprivateoffice.com` (GHL 301s to here).

See [`FUNNEL.md`](FUNNEL.md) for the funnel map, the target maths, and the five
things that have to be configured outside this repo before it runs.

## Capture pages

- `index.html` — Director's Take-Home Calculator 2026/27 (+ GHL lead capture)
- `pay-calculator.html` — pay structure gap, the strongest hook for switchers
- `whats-at-stake.html` — estate and exit exposure (CT Private Office)

All three post to the GHL "Calculator Lead Capture" webhook and send a
`segment` field (`t4p-director` or `ctpo-hnw`) that selects the nurture sequence.

## Conversion pages

- `plans.html` — Tax 4 Pros plans and pricing, price on the page
- `why-us.html` — what switching involves (the main objection)
- `who-is-sarah.html` — CT Private Office trust page

## Articles (organic search)

- `accountant-cost-limited-company.html`
- `changing-accountants.html`
- `salary-vs-dividends.html`
- `how-much-to-pay-yourself.html`

## Not served

- `FUNNEL.md` — the map, the maths, the config checklist
- `nurture-emails.md` — the two GHL email sequences
- `gbp-posts.md` — Google Business Profile setup, review asks, twelve weeks of posts

## Before publishing

Prices in `plans.html` are placeholders pending confirmation against the real
rate card.

Source of truth mirrors `content/funnel/site/` in the youtube-autopilot repo.
Tax figures must match `content/TAX_FIGURES_LIVE.md` — re-check after any Budget.
Run `check_figures.py` over the articles and the email sequences before they ship.
