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
- Captions: follow the CAPTION STRUCTURE section below (it replaces the old 4-paragraph rule); primary search phrase early (toxic boss,
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

## Emotional-page strategies (added Oct 19 after studying @brokenquotes.in-style pages + Reels ranking)
User asked to borrow the emotional music + hook strategies of quote pages like @brokenquotes.in.
(Their profile couldn't be opened directly; these are the shared patterns of big emotional quote
pages plus Instagram's stated Reels signals: watch time/completion, likes per reach, and DM
sends per reach.) Copy methods only, never their words, images or audio.
1. Instant hook: full hook text visible on frame 0 + motion within 0.5 s (engine punch-in) +
   a piano note on frame 0. No slow intros, no logo openers.
2. Music tells the story (engine `score`, used automatically for 3+ frame Reels): sad minor
   pad + slow heartbeat under the hook and feeling, a riser into the solution, then a lift to
   major (relief) for the solution and follow. Every chord change lands on a text change.
   All music is generated by us: original audio, no copyright or originality strikes.
3. One "screenshot line" per Reel: the feeling frame uses `"style": "quote"` (big serif quote
   mark, italic serif) so it reads like a quote card people save and send.
4. Built for sends: the follow frame carries a `sub` line like "Send this to the coworker who
   always says yes." Caption paragraph 4 also invites sending to a specific person.
5. Short, readable lines: <= 10 words per frame where possible, nothing that needs pausing.
6. Relatable specifics beat general statements (a real time, a real task, a real message).
7. Captions: first line = keyword + emotion; keep 5 hashtags (keywords in text matter more).

## Caption + hook formula (added Oct 19 from studying @corporateclarity.career, @ccjenniferbrick,
## @fearlessworkplace; user: use their formatting and structure, never copy their words)
What the top posts had in common (views/likes seen Oct 19):
- corporateclarity.career (171K followers): best Reels 903K "what happens behind closed doors when you
  report something to HR", 261K "the truth no one tells high performers", 250K "when a high
  performer stops doing this, they're already gone", 167K "coworker is smearing your name... do NOT
  do this", 139K "never ask a senior leader this, ask this instead".
- fearlessworkplace (73K): pinned 87K likes "competence is threatening in the wrong workplace",
  49K "leadership knows". Metaphor banner headlines ("they light the match, then blame the smoke").
- ccjenniferbrick (79K): one giant emphasized word in the hook, numbers ("3 microhabits"),
  "Can't quit your toxic job? Do this instead", short captions + comment-keyword CTA.

ON-SCREEN HOOK PATTERNS to rotate (write our own words):
 a) Insider reveal: "What really happens when ___" / "What your boss won't tell you about ___"
 b) Warning + swap: "Your boss does ___? Do NOT ___. Do this instead."
 c) Paradox truth: "In toxic workplaces, ___ is a threat." (the 87K / 261K style)
 d) Exit signal: "When someone stops ___, they're already gone."
 e) Can't-X? Do-Y: "Can't quit yet? Do this instead."
 f) Number promise: "3 things toxic bosses do in every meeting"
 g) Metaphor headline: "They make the mess. You get the cleanup."
 Plus our emotional-moment hooks ("Your boss texts at 9:47 PM...").

CAPTION STRUCTURE (every post, 90-160 words, one idea per line, blank line between blocks):
 1. HOOK LINE: one sentence that restates the on-screen hook as a bold truth, optional single
    emoji (👀). It must work on its own in the 2-line preview. Primary search phrase
    (toxic boss / toxic workplace / bad manager / burnout at work ...) in line 1 or 2.
 2. STAIRCASE: 3 short lines that build ("You stayed late. / You fixed the numbers. / You built
    every slide.") or a cause-effect chain ("Questions expose problems. / Problems expose
    leadership.").
 3. TWIST: the moment it turns ("Then in the meeting it became 'the plan I put together.'").
 4. CONTRAST PAIR: "In healthy workplaces, ___. / In toxic ones, ___." or "Now it's X... but Y."
 5. SOLUTION: what to do, with the exact words to say in quotes. One reframe line
    ("That's not bragging. It's a paper trail."). Never just validation.
 6. QUESTION + 👇: a specific yes/no-or-story question with ONE word in CAPS for emphasis
    ("Has a boss ever taken credit for YOUR work? 👇").
 7. SEND LINE: "Send this to the coworker who ___." (specific person).
 8. FOLLOW LINE with a value promise: "Follow @unspokenatwork1 for the workplace truths nobody
    says out loud, and what to do about them."
 9. 5 hashtags, lowercase, last line: mix #toxicboss #toxicworkplace #corporatelife
    #officepolitics #careeradvice #workplaceanxiety #burnout + #UnspokenAtWork.
 Emojis: 0-3 total, never decorative strings. No comment-keyword DM CTA until a real freebie and
 DM automation exist (then: "Comment SURVIVAL and I'll send it").

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
