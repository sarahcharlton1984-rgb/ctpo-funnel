# Calculator nurture sequences

Email follow up for leads captured by the calculator pages. Written to the house rules:
no dashes anywhere, short declarative sentences, numbers stated plainly, never "chartered",
and no specific tax advice in writing (that is what the call is for).

Two sequences, chosen by the segment tag set at the moment of capture.

| Tag | Who | Sequence | Destination |
|---|---|---|---|
| `t4p-director` | Profit under roughly £300k, taking money out of a limited company | A, five emails over twelve days | 15 minute review, Tax 4 Pros |
| `ctpo-hnw` | £1m+ business, a sale in view, or an estate problem | B, three emails over sixteen days | Tax Strategy Review, CT Private Office |

Everyone lands on the monthly note afterwards, whichever sequence they came through.

Merge fields are GoHighLevel format. `{{contact.first_name}}` falls back to "there".

---

## Sequence A: director path

The one that gets to £15k MRR. Sent from Sarah, plain text, no header image, no template
furniture. It should look like an email a person wrote.

---

### A1 · Day 0 · The result

**Subject:** Your numbers, {{contact.first_name}}
**Preview:** Plus the one thing that stood out.

> Right. Here is what the calculator worked out for you.
>
> **{{contact.calc_result}}**
>
> One thing worth saying about that figure.
>
> Most directors look at the total and assume the gap is the price of doing business. It usually is not. The gap is almost always made of three things: the split between salary and dividends, the timing of when profit comes out, and whether anyone has looked at the structure since the company was set up.
>
> The third one is where the real money sits, and it is the one nobody checks.
>
> I will send you something on that in a couple of days.
>
> Sarah
>
> Sarah Charlton
> Tax strategist and founder, Tax 4 Pros

**Notes:** send within five minutes of capture. The single observation matters more than the number, which they already saw on screen.

---

### A2 · Day 2 · Teach one thing

**Subject:** The question your accountant has never asked you
**Preview:** It takes about four minutes to answer and it changes the number.

> {{contact.first_name}},
>
> Here is the question.
>
> "How much do you actually need to take out of the business this year?"
>
> Not how much profit did you make. Not what did you take last year. How much do you need.
>
> Almost nobody gets asked it. The default is to extract whatever is there, in whatever way the software suggests, and find out what it cost the following January.
>
> It matters because the tax on money you take out and the tax on money you leave in are two completely different numbers. Once you know the figure you genuinely need, the order of everything else changes. What comes out as salary. What comes out as dividend. What is better left in the company for now. Whether a pension contribution does more work than a dividend.
>
> None of that is clever or aggressive. It is just sequencing, and it only works if somebody asks the question first.
>
> If your accountant has never asked you that, it is worth knowing why.
>
> Sarah

**Notes:** no pitch, no link, no ask. This email is the proof that you do a different job from their current firm.

---

### A3 · Day 5 · The receipt

Two versions. The first is ready to send from a case study already published on
the site. The second converts harder but needs one number from you.

---

#### A3a · Ready to send, from the childcare case

Source: `tax4pros.co.uk/case-studies/childcare-business-vat-structure-planning`.
Already anonymised and already public, so nothing new is being disclosed.

**Subject:** Two founders, one question nobody had answered
**Preview:** They had premises, staff and a plan. Nobody had told them how to pay themselves.

> {{contact.first_name}},
>
> Two people came to us launching a childcare business in London. Premises signed, staff lined up, commercial plan done properly.
>
> What they did not have was any idea how the tax side worked. Whether to register for VAT. How to pay themselves. How to set the company up so it could grow later.
>
> Reasonable questions. Nobody had answered any of them, because nobody had been asked to.
>
> Here is what that would have cost if they had carried on. Charging VAT they did not need to charge. Missing the reclaim on their set up costs, which were substantial. Paying themselves in the way that felt normal rather than the way that worked. And a company structure that would have quietly blocked a second site, a franchise or a sale, years before anyone noticed.
>
> None of that is exotic. It is the ordinary set of decisions every company makes in its first year, made once, and then lived with for a decade.
>
> We ran the VAT position, the pay structure and the company setup together rather than one at a time. They are now on a platform that can take a second site and an investor, instead of becoming another over taxed small business that has to be unpicked later.
>
> Most childcare businesses do not fail because of demand. They fail because they were badly structured on day one.
>
> The same is true of most companies. It is just less obvious when you are five years in.
>
> Sarah

**Notes:** works without a figure because the punchline is the structural mistake
rather than a saving. Slightly softer than A3b. Send this one until you have
supplied a number for the other.

---

#### A3b · The stronger version, needs one number from you

This is the higher converting email and it is one figure away from being
finished. Everything below is written. Fill the four brackets from a real client
and it sends.

**Subject:** A {{trade}} doing £{{turnover}} was overpaying by £{{amount}}
**Preview:** Nothing clever. Nobody had looked.

> {{contact.first_name}},
>
> A client came to us last year. [TRADE] business, [TURNOVER] through the company, one director taking money out of it.
>
> He was paying [OLD FIGURE] a year in tax and he assumed that was simply what it cost. Everything had been filed correctly and on time for years. Nothing was wrong.
>
> What nobody had done was ask him how much he actually needed to take out of the business. So every year the profit came out the way it had always come out, and every year it cost him [DIFFERENCE] more than it needed to.
>
> We changed [WHAT CHANGED. One sentence. The structural fix, not a trick.] He now pays [NEW FIGURE].
>
> That is [DIFFERENCE] a year. Every year, for as long as the business runs.
>
> His words when we showed him: "[VERBATIM QUOTE. Leave it exactly as he said it. The quote is the punchline.]"
>
> Sarah

**What to supply:** trade, turnover band, old tax figure, new tax figure, the one
sentence on what changed, and his actual words. Alter anything identifying, keep
the numbers true. Rotate three or four of these so the sequence stays fresh, and
run each past the client-output-reviewer before it goes live.

---

### A4 · Day 8 · The offer, with the price in it

**Subject:** What we charge
**Preview:** All of it, on one page, before you speak to anyone.

> {{contact.first_name}},
>
> You have had a few emails from me now, so here is the commercial bit, plainly.
>
> We do fixed monthly accountancy for limited company directors. One price, agreed before we start. Everything on the list is included. There is no invoice at the year end that you were not expecting, and there is no charge for asking a question.
>
> There are four packages, from £125 a month if you keep your own books and just want the filings done properly, up to £395 for Gold, which is the one where somebody is looking at next year rather than only reporting on last year. Most directors in your position land on Silver at £295, which covers the accounts, the corporation tax return, your self assessment, payroll and monthly numbers.
>
> Pricing is banded by turnover, because the workload is. It is all published, so you can work out which one you are without speaking to anybody:
>
> **https://tax4pros.co.uk/packages**
>
> Two other things worth knowing.
>
> You are live inside a week. We handle the clearance, the records and the software. You sign two things.
>
> And if something bigger ever comes up, a sale, a restructure, a move abroad, an inheritance tax problem, we have a specialist advisory arm and you stay with us.
>
> Sarah

**Notes:** the price goes in the email. Hiding it only filters out people who would have said yes.

---

### A5 · Day 12 · The ask

**Subject:** Fifteen minutes
**Preview:** You will know where you stand either way.

> {{contact.first_name}},
>
> Last one from me on this.
>
> Fifteen minutes on a call and you will know three things. What your current setup is costing you. Whether there is anything meaningful to change. Whether we are worth moving for.
>
> If the answer to the last one is no, I will tell you. Plenty of directors are already set up sensibly and do not need us, and I would rather say so than sell you something.
>
> **{{booking_url}}**
>
> If the timing is wrong, ignore this. I send one useful thing a month and you will stay on that list either way.
>
> Sarah

**Notes:** one ask, one link, no countdown, no false scarcity. It is a professional service.

---

### A6 · Monthly · The note

**Subject:** varies. One specific thing, never "Newsletter".
**Preview:** varies.

One genuinely useful thing a month. A rule that changed, a deadline worth knowing, a
mistake you keep seeing. Two hundred words. One soft line at the bottom.

By month six this list will produce more clients than any single post, because it reaches
people at the moment their circumstances change rather than the moment you published.
Never stop sending it.

---

## Sequence B: high net worth path

Slower, fewer emails, CT Private Office branding. These people are not buying a monthly
retainer. They are deciding whether to trust you with something large.

---

### B1 · Day 0 · The result

**Subject:** Your exposure, {{contact.first_name}}
**Preview:** The number, and what actually drives it.

> {{contact.first_name}},
>
> Here is what the calculator produced.
>
> **{{contact.calc_result}}**
>
> Worth being straight about what that figure is and is not. It is your exposure on today's rules, on the assumptions you entered. It is not a plan and it is not advice.
>
> What it does tell you is the size of the thing. When the number is that large, the cost of leaving it unexamined for another year is usually far bigger than the cost of examining it.
>
> More in a few days on the routes that genuinely apply to a situation like yours, and the conditions attached to each.
>
> Sarah Charlton
> CT Private Office

---

### B2 · Day 6 · The mechanism

**Subject:** The three routes, and what each one actually requires
**Preview:** Every structure has a cost, a condition or a catch.

> {{contact.first_name}},
>
> There are broadly three directions people in your position take. Each has a real condition attached, and anyone who tells you otherwise is selling something.
>
> [ROUTE ONE]. What it does. What it requires. What it costs you in flexibility.
>
> [ROUTE TWO]. Same three.
>
> [ROUTE THREE]. Same three.
>
> Which one fits depends entirely on facts I do not have. Timing, shareholdings, what you want the business to look like in five years, and whether anyone in the family is staying.
>
> That is the conversation, and it is not one to have by email.
>
> Sarah

**Notes:** fill the routes per the standing accuracy rules. Every figure checked before it ships. State the limits. Never free money framing.

---

### B3 · Day 16 · The review

**Subject:** A Tax Strategy Review
**Preview:** Ninety minutes, properly prepared, and you keep the work.

> {{contact.first_name}},
>
> When the number is the size of yours, the useful next step is a proper piece of work rather than a chat.
>
> A Tax Strategy Review is ninety minutes, prepared in advance from your actual position. You leave with the structure that fits, what it would save, what it would cost, and what the conditions are. You keep that whether or not you go any further with us.
>
> **{{ctpo_booking_url}}**
>
> By application, and I only take a small number at a time.
>
> Sarah

---

## Build notes

1. **The segment tag is the dependency.** Set `t4p-director` or `ctpo-hnw` at capture, from the profit band and business value already entered into the calculator. Without it, both sequences fire at the wrong people.
2. **Package names and prices in A4 are the live ones** from `tax4pros.co.uk/packages`: Compliance £125, Bronze £195, Silver £295, Gold £395 at up to £500k turnover, FD Lite from £795. Re-check them against the page before switching the sequence on, and again whenever the price list changes.
2. **Plain text, from a person.** No banner, no template chrome, no unsubscribe language beyond the legal minimum. It should read like Sarah wrote it that morning.
3. **Send from her real address** so replies land somewhere a human reads. Several will reply instead of booking, and those are the best leads in the sequence.
4. **Every figure** goes through `check_figures.py` against the live figures file before the sequence is switched on, and again after any Budget.
5. **Never mass send.** These are automated on capture only. Anything going to the existing list goes out one approved batch at a time.
6. **Measure two things per email:** open rate tells you the subject line worked, reply rate tells you the email worked. Clicks matter only on A4 and A5.
