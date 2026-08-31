# Tax 4 Pros funnel

Built for one sale a week. Everything here is static and lives in this repo,
served behind `apply.ctprivateoffice.com`.

## The target, worked backwards

One sale a week is roughly four clients a month. At a £295 average fee that is
about £1,180 of new MRR every month, so £8k becomes £15k in six months.

| Stage | Rate assumed | Needed per month |
|---|---|---|
| New clients | — | 4 |
| Qualified calls | 30% close | 13 |
| Email leads | 12% book a call | 110 |
| Calculator visits | 25% give an email | 440 |

**440 visits a month is about 15 a day.** That is the whole job. It is not a
reach problem and it does not need a large audience. Every rate above is a
planning assumption. Replace each one with your own after thirty days of real
data, because if capture runs at 40% the traffic target nearly halves.

## The map

```
    CONTENT                 SEARCH                GOOGLE BUSINESS
  reels, YouTube        4 blog articles          profile + reviews
        |                     |                        |
        +----------+----------+------------------------+
                   |
                   v
        CALCULATOR (email gate)          <-- the only capture point that matters
        /  index.html         take home, directors
        /  pay-calculator     pay structure gap, directors
        /  whats-at-stake     estate and exit, HNW
                   |
                   v
        GHL webhook, tagged t4p-director or ctpo-hnw
                   |
          +--------+--------+
          |                 |
          v                 v
    SEQUENCE A          SEQUENCE B
    5 emails/12 days    3 emails/16 days
          |                 |
          v                 v
    15 min review      Tax Strategy Review
          |                 |
          v                 v
    TAX 4 PROS          CT PRIVATE OFFICE
    £295/month          advisory fees
```

The close is **`tax4pros.co.uk/packages`**, which already exists and already does
the job: four packages priced on the page, banded by turnover, AML supervision and
PI insurance stated, and a self-selection block that routes the leaving-the-UK case
to CT Private Office. Nothing here duplicates it. Every CTA points at it.

## Pages

| Page | Job | Segment |
|---|---|---|
| `index.html` | Take home calculator. Main capture. | director, or HNW above £300k |
| `pay-calculator.html` | Pay structure gap. Strongest hook for switchers. | director, or HNW above £300k profit |
| `whats-at-stake.html` | Estate and exit exposure. | always HNW |
| `accountant-cost-limited-company.html` | Ranks for "how much does an accountant cost". High buying intent. | — |
| `changing-accountants.html` | Ranks for "changing accountants". Highest buying intent of the four. | — |
| `salary-vs-dividends.html` | High volume informational. Feeds the calculator. | — |
| `how-much-to-pay-yourself.html` | High volume informational. Feeds the calculator. | — |
| `who-is-sarah.html` | CT Private Office trust page. | — |

The four articles are published on **`tax4pros.co.uk`** (WordPress, Elementor,
GoDaddy) via `tax4pros-wordpress-import.xml`, not served from this repo. They land
in the theme with the site nav intact, which is what they need: these are organic
search pages, so internal linking and a real site structure help them rank and help
the reader trust them. They are not closed landing pages.

`tax4pros.co.uk` already has `/packages` (the price list), `/case-studies`,
`/meet-the-team`, `/insights` (the blog these posts join), `/services` and
`/skool-community`. Check what exists there before building anything new.

Every article carries a calculator CTA mid way and a booking CTA at the end,
with UTMs already set so you can see which article produces leads.

## What you have to configure

Nothing below is code. These are the five things that have to happen outside
this repo before the funnel runs.

1. **Import the articles.** WordPress admin → Tools → Import → WordPress, upload
   `tax4pros-wordpress-import.xml`. Four drafts land in Insights. Review, set a
   featured image, publish.
2. **Build the two GHL sequences** from `nurture-emails.md`, and split them on
   the `segment` field the calculators now send. Without the split, both
   sequences fire at the wrong people.
3. **Point the booking CTAs at the real GHL calendar.** They currently go to
   `apply.ctprivateoffice.com`. The `/packages` page already has a "Book a 15
   minute fit call" link; use that same calendar so everything lands in one place.
4. **Claim and populate the Google Business Profile,** and link it to
   `/pay-calculator` rather than the homepage. See `gbp-posts.md`.
5. **Run `check_figures.py`** over the four articles and the email sequences
   against `content/TAX_FIGURES_LIVE.md` before any of it is published. The
   figures used here match the `current-tax-year` skill and the live calculator
   JS, but that file is the source of truth and it is not in this repo.

## The weekly rhythm

Once it is running, this is the whole operating loop.

- **One recording session.** One long form video plus six verticals.
- **Verticals to four platforms.** TikTok, Reels, Facebook, Shorts. Same file.
- **One Google Business post.** Pull the hook from the week's video.
- **Two review requests.** Personally, to real clients, one at a time.
- **One blog article a fortnight.** Written from the long form transcript.
- **Friday: five numbers.** Below.

## What to measure

Every Friday, five numbers. Not followers, not views, not impressions.

| Number | From | Healthy at day 90 |
|---|---|---|
| Calculator visits | Site analytics | 440/month |
| Email captures | GHL | 110/month |
| Calls booked | GHL calendar | 13/month |
| Clients won | You | 4/month |
| MRR | You | Up, every month |

If a number is short, fix the stage above it, never the strategy. Low captures
is a page problem. Low bookings is an email problem. Low closes is an offer
problem. None of those is solved by a new business model.
