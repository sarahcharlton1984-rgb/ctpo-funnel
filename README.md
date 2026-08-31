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

- `who-is-sarah.html` — CT Private Office trust page

Tax 4 Pros pricing lives at `tax4pros.co.uk/packages`, which already exists.
Nothing in this repo duplicates it; every T4P CTA points at it.

## Articles (for tax4pros.co.uk, not served from here)

- `accountant-cost-limited-company.html`
- `changing-accountants.html`
- `salary-vs-dividends.html`
- `how-much-to-pay-yourself.html`

`tax4pros.co.uk` is WordPress, so these are published by importing
`tax4pros-wordpress-import.xml` (Tools → Import → WordPress). They arrive as
drafts in Insights and render inside the theme with the site nav intact.
`build-wordpress-import.py` regenerates the XML from the HTML.

## Not served

- `FUNNEL.md` — the map, the maths, the config checklist
- `nurture-emails.md` — the two GHL email sequences
- `gbp-posts.md` — Google Business Profile setup, review asks, twelve weeks of posts

## Before publishing

Source of truth mirrors `content/funnel/site/` in the youtube-autopilot repo.
Tax figures must match `content/TAX_FIGURES_LIVE.md` — re-check after any Budget.
Run `check_figures.py` over the articles and the email sequences before they ship.
