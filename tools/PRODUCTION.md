# Unspoken at Work (@unspokenatwork1) — production rules

The user's MASTER_PROMPT.txt (in this folder) is the permanent framework. This file is how
we run it hands-off. If they disagree, the newest user instruction wins, then this file,
then MASTER_PROMPT.txt.

## Non-negotiables
- Niche never changes: toxic bosses, toxic workplaces, manipulation, burnout, workplace
  anxiety, micromanagement, favoritism, disrespect, leaving unhealthy jobs.
- **Every post opens on an EMOTIONAL hook** (user, Oct 19): under 10 words, visible on the
  first frame / slide 1, naming a feeling or moment the reader has lived ("Your stomach
  drops when their name pops up."). Not a dry tip, not a question with no feeling in it.
  Rotate the patterns: unspoken truth, emotional recognition, contrarian, curiosity gap,
  personal realization, pattern recognition. Never start with "POV", "Nobody talks about"
  or "Here are 5 signs". Write 5 options, keep the strongest, score it.
- **Every post ends with a SOLUTION, then a FOLLOW call to action** (user, Oct 19). Not just
  relatable: after the hook and the recognition, give one concrete thing to do, such as a
  boundary to set, an exact script to say or send, a way to protect your time, or a way to
  take care of yourself first. Then close with a follow CTA, e.g. "Follow so this finds you
  again when you need it." (honest, no fake urgency or threats).
  Reel structure (14-17 s, music throughout): 1) emotional hook + literal prop
  (0-4.6 s) 2) recognition/feeling (to ~8.3 s) 3) SOLUTION with a `reply` bubble prop
  showing the exact words, or a short action (to ~12.8 s) 4) FOLLOW frame with the `follow`
  prop (last ~3 s). Carousels: slides 5-6 are the solution, slide 7 is "Follow
  @unspokenatwork1 so this finds you again when you need it." + a save line. Captions end
  with the solution in paragraph 3 and "Follow @unspokenatwork1 ..." in paragraph 4.
- **Every post must make sense on its own in 2 seconds** (user, Oct 19: "make sure what
  you're creating makes sense"). A stranger who has never seen the page must instantly know
  WHO (say "your boss" / "your manager", never a vague "they" or "their name"), WHAT is
  happening, and WHY it hurts. Reels must SHOW the situation literally with an on-screen
  prop from engine.py: `notification` (a text/email from "Boss"), `tasks` (a to-do list
  filling up "from Manager"), or add a new literal prop (calendar invite, chat bubble,
  email subject line) when the topic needs it. No abstract-only visuals for Reels.
  Before scheduling, re-read every frame as a stranger: if anything is unclear, rewrite.
- Score every post on the 7 factors in MASTER_PROMPT section 12. Rewrite anything under 8
  on clarity or emotional relatability before rendering.
- Hands-off design only (user chose this Oct 19): procedural dark scenes from engine.py,
  no photos, no faces. Brand: off-white Inter Display Bold, amber #D9A15B accent words
  (wrap them in *asterisks* in specs), "UNSPOKEN AT WORK" tag, @unspokenatwork1.
- Text stays in the upper/middle area; bright scene parts are kept low by the engine.
  Reels: 4 frames (hook / feeling / solution / follow), 14-17 s, hook from 0 s, short lines.
  Carousels: 7 slides (hook / recognition / hidden pattern / mistake / solution / example /
  CTA), <= 15 words main copy per slide.
- Captions: 4 short paragraphs, primary search phrase in the first sentence (toxic boss,
  toxic workplace, bad manager, burnout at work, micromanaging boss, workplace favoritism,
  workplace anxiety, setting boundaries at work, leaving a toxic job...), 90-160 words,
  context-specific CTA, then exactly 5 hashtags with #UnspokenAtWork as one of them.
- Safety: no invented stats, quotes, laws or testimonials; never diagnose anyone
  ("narcissist"); never call something "hostile work environment" or "retaliation" as a
  legal conclusion; never promise auto-DMs or a freebie that doesn't exist yet; never ask
  viewers to name employers or coworkers; no guarantees of virality or legal outcomes.
  Legal-adjacent tips end with "general information, not legal advice".
- Anti-repetition: check content_log.tsv; no repeated hook, scene combo or main lesson
  within 30 days. Rotate scenes: rain_window, monitor, hallway, lamp, night_office,
  conference.
- Keep Unspoken at Work fully separate: never post its media to Odds Visualized, Money
  Mapped, Kids & Money or Warriors for Christ, and never post theirs here.

## Daily package (3 posts, MASTER_PROMPT section 5)
User, Oct 19: always exactly 3 posts per day = 2 Reels + 1 carousel. Keep this format:
very strong emotional hook, music under every Reel, very relatable human work situations.
1. Emotional Recognition Reel ("that is exactly what my boss does")
2. Uncomfortable Workplace Truth Reel (contrarian / curiosity gap, no invented facts)
3. Saveable Educational Carousel (specific steps)
Series rotate: Read This Before Your Next Shift · What Your Boss Won't Admit · Workplace Red
Flags · Things Toxic Bosses Say · Things Employees Wish They Could Say · The Workplace
Survival Files.
30-day phases from MASTER_PROMPT section 13 (days 1-7 test themes, 8-14 double down using
real insights, 15-21 series, 22-30 introduce a free resource only once it exists).

## Files
- specs/dayNN.json  -> render with `python3 render_day.py specs/dayNN.json out/dayNN`
- posts/dayNN.json  -> captions keyed by post id
- content_log.tsv   -> one row per post (add rows, set status posted after publishing)
- posted.log        -> one line per publish with permalink
- Check renders: contact-sheet every carousel slide and grab Reel frames at ~2 s and ~8 s.
  Nothing may overlap or cut off; text must be readable.

## Posting
- Instagram account: @unspokenatwork1, Zapier InstagramBusinessCLIAPI.
  instagramPageId 17841420504964559 ("Unspoken At Work | Toxic Bosses"; also in PAGE_ID.txt). Verify the label
  containing "Unspoken"). If it is not there, do not post anywhere; tell the user once.
- Media host: public repo shaunmcm/Unspokenatwork, cloned at /home/claude/unspokenatwork
  (folders r/ and c/, tools/), raw URLs
  https://raw.githubusercontent.com/shaunmcm/Unspokenatwork/main/<path>.
  Commit as Claude <noreply@anthropic.com>.
- Reels: publish_video (Reel). Carousels: publish_media_v2 with slide URLs in order.
- If Instagram says "still processing": wait 75 s, check the account's latest media
  (Make API GET Request: https://graph.facebook.com/v19.0/17841420504964559/media?fields=id,permalink,timestamp),
  retry only if it did not post. Never post twice. A successful publish returns a media id;
  GET https://graph.facebook.com/v19.0/<id>?fields=permalink for the link.
- Times (PT): Reel 1 at 12:00 PM, carousel at 5:30 PM, Reel 2 at 8:30 PM. Adjust from real
  Insights later; never claim a time is "optimal" without data.
- After each post: append to posted.log, set content_log status to posted, and
  SendUserMessage one line with the permalink.
- Tell the user right away about Zapier task limits, billing, throttling or expired
  connections.
