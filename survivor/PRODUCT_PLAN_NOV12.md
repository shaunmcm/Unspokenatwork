# @work_placesurvivor — sales audit + product proposal (Nov 12, 2026)

## UPDATE Nov 12, later: paywall + PDF + own hosting
- Flow: free quiz -> free top 3 -> $20 paywall -> full plan (90-day daily planner, guide, costs/goal math, exit numbers, all 3 businesses) + PDF download.
- PDF is generated inside the page (no outside services). Sample: 11 pages.
- Payment: Stripe Payment Link ($20). The after-payment redirect goes to <site>/?paid=<unlock code>. The page checks the code's SHA-256 and unlocks on that browser. The unlock code is kept private, not in the repo.
- Hosting: Netlify (free), e.g. exitblueprint.netlify.app. GitHub Pages can't be switched on from this workspace.
- Waiting on the user: Netlify site address + Stripe Payment Link URL -> put into PAY_LINK in index.html.
- Limit: a static paywall can be bypassed by someone tech-savvy or by sharing the unlock link. A Netlify function that checks Stripe would close that.

## UPDATE Nov 12 (user's direction): "The Exit Blueprint", $24.99 (changed to $20 the same night)
- User's concept: page explaining the exit plan -> skills quiz -> top side businesses -> tailored plan to build that side business.
- Prototype built (private): https://claude.ai/artifact/EiQik4fTMx3ovM9XK5hWrj (source: survivor/product/exit_blueprint.html)
  - 15 questions: name, day job, skills, what people already ask for help with, tools owned, hours, schedule, budget, hands vs screen,
    physical energy, comfort selling, local vs online, network, monthly must-pays, savings months.
  - Scores 12 side-business paths. Shows the top 3 with reasons taken from the person's own answers.
  - Startup kit priced to their budget, minus tools they already own.
  - 90-day plan sized to their hours and schedule, scripts matched to their network and how comfortable they are selling, plus a local-rules check.
  - Exit numbers: milestones at 25%, 50% and 100% of must-pays, and a 6-month safety net.
  - No income promises.
- Delivery: sell on Gumroad or Stan Store at $24.99 and deliver the HTML file itself (it opens in any browser). Alternatively, host it on the user's own site behind the purchase.


## What the page data shows (Instagram API, Nov 12)
- 122 followers (111 on Nov 10), 18 posts. Views/reach/saves/shares are not available through this connection.
- Best post by far: the river-rock Reel (Nov 10) — 9 likes, 5 comments. Hook: "You'd walk out tomorrow if you could afford to. But somebody has to pay the bills, so you walk back in." Caption gave a money way-out step (a "freedom fund").
  - Honest caveat: the 5 comments were one person objecting to "a man" plus replies. Debate drove the comments, not buyer intent.
- Everything else: 0-6 likes, 0-1 comments. Topics about sleep, vacation, gratitude, nature got the least.
- Bio links only to YouTube. There is no free offer, no product, and no link hub.
- "Comment HELP" has produced almost no comments.

## Competitors (what I could check)
- Instagram competitor pages could not be opened from here. Paste 3-5 page names or screenshots to compare.
- Gumroad has many "escape plan" products at $7-$147, most at $12-$39 (e.g. Exit Plan Blueprint $39, 72-Hour Toxic Job Escape Kit £29, Burnout Survival Toolkit $19+, Escape Plan Builder $18.99).
- Nearly all of them are about quitting to start an online business, or about generic burnout. Almost none are for a man with a family who cannot miss one paycheck. That is the gap.

## Three biggest sales opportunities
1. A safe way out. The page's best post is about leaving safely, and it's the problem the whole niche is built on.
2. A comment-to-DM funnel. Turn "Comment HELP" into "Comment PLAN" with a free tool sent by DM (ManyChat or by hand). The free tool proves demand before anything is built.
3. The bio. Add a link hub (Stan Store, Beacons or Linktree) with a free tool on top, then the product, then YouTube.

## Recommended product: "The Provider's Exit Plan"
Promise: a 90-day plan to move to a better job without missing a paycheck.
- Format: a PDF of about 30 pages plus a fillable Google Sheet. Sold through Stan Store or Gumroad. Nothing to maintain.
- Price: $27, in the middle of the $12-$39 range. No fake countdowns.
- Inside:
  1. Your "safe to leave" number: monthly must-pays, months of runway, and the lowest pay a new job can offer. The calculator is in the Sheet.
  2. Survive while you plan: 10-minute after-work resets and word-for-word scripts for a toxic boss (confirm-by-email, saying no, staying calm).
  3. The 90-day switch while employed: 15 minutes a day, a resume template for hands-on and shift workers, interviewing around your shifts, and leaving without burning bridges.
  4. The talk at home: how to raise the plan with your partner without scaring them.
  5. A 90-day tracker.
- Free lead magnet: the "Safe to Leave" calculator by itself (one page), sent by DM to anyone who comments PLAN.

## Validation before building (actual demand, not assumptions)
- Week 1: make the free calculator and post 2 Reels about it with the CTA "Comment PLAN."
- If 10+ people ask for it, or the YouTube audience responds to a community post, build the full product.
- If not, test the second idea: a toxic-boss script pack.

## On-screen hook upgrade (approved by the user Nov 12)
See RULES.md, "ON-SCREEN HOOK UPGRADE".

## Captions after launch
Follow the existing structure, then one product line, with a rotating CTA. Never mention the product before it exists.

## What's needed from the user
- Approval, edits or rejection of the product.
- Weekly Insights screenshots (reach, shares, saves, profile visits, link clicks).
- Real experiences of his own for captions. Personal stories won't be invented.
