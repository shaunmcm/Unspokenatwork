# >>> DEADPAN CLEVER (user, Oct 30 8:07 AM, example: "I already reviewed my budget... I can only afford to breathe and look
#   at the sun"): the target joke shape is a FORMAL, serious setup (reviewed / calculated / according to my calendar /
#   I'm pleased to report) that lands on a bleak, oddly specific, understated punchline ("I can afford to care until
#   about 10:45 AM"). RESEARCH EVERY RUN: before posting, run one web search for this week's workplace news/trends
#   (layoffs, return-to-office, AI at work, raises, holidays, review season) and write fresh topical jokes from it.
#   Use real trends as topics only; never present a joke as a fact or statistic. Never copy or lightly reword
#   another page's posts or the user's examples; write original jokes. Approved set: raccoon/batch06.json.
# >>> 1,000-VIEW PUSH (user, Oct 30 7:56 AM: last Reels stuck around 131 views; "do whatever you need"): Reels are 5 to 8 s
#   (0.28 s per word + 1.8 s) so they get finished and replayed; captions open with a searchable phrase ("work humor",
#   "office humor"), keep one comment question, and always ask to "Send this to your work bestie" (sends drive reach);
#   hashtags #workhumor #officehumor #corporatehumor #worklife #relatablememes. Strongest, shortest jokes go first.
# >>> ALL TEXT AT ONCE (user, Oct 30 2:29 AM): never reveal lines one by one. Every word is on screen from the very
#   first frame (viewers decide in about one second). One still per Reel, held ~0.35 s per word + 3 s (min 7 s),
#   so it can be read twice. render_reels2.py already does this.
# >>> STYLE V2 (user, Oct 30 2:20 AM, shared two example posts): make posts catchy and memorable with MORE text so
#   people stay longer. Format now: pastel background, ALL-CAPS Bebas Neue text, 3 to 5 short lines, ALL visible from frame 1 (punchline is the last line), raccoon at the bottom, music. Renderer: raccoon/render_reels2.py, batch items
#   {"id","lines":[...]}. Joke mechanics to use: escalation that builds to an unexpected last line ("about a raise?
#   about a promotion? about my attitude? it was the attitude."), treating work/job like a relationship or person,
#   wordplay twists ("not circling. he's in orbit."), "WHEN MY BOSS SAYS X, I ...". Original wording only; never
#   copy or lightly reword another page's posts. Approved set: raccoon/batch05.json.
# >>> CLARITY RULE (user, Oct 30 12:56 AM: "didn't make sense"): every joke must be an everyday work situation anyone gets on first read (raise, meetings, PTO, boss at 4:55, "we're a family"), with a plain punchline. No internet slang ("perceived", "locked in"), no inside references. Write original jokes in these proven shapes; never copy or lightly reword another page's posts. Approved set: raccoon/batch04.json.
# >>> REELS ONLY (user, Oct 30 12:52 AM): post every raccoon quote ONLY as a Reel (the image turned into a short video). Never publish a photo or carousel post.
# >>> REELS, NOT PHOTOS (Oct 30, after the user asked why the raccoon photo got 3 views): the reference page
#   (beak.manifesto) posts every quote as a REEL (still image + music, its Reels tab shows 788K to 3.7M views).
#   Photo posts only reach followers (we have 2). Every raccoon post is now a 7 s 9:16 Reel made with
#   raccoon/render_reels.py (quote at top, big raccoon at bottom, slow push-in, original upbeat music),
#   posted with publish_video. Trending/licensed songs cannot be added through the API.
# >>> RESEARCHED JOKE SHAPES (user, Oct 29 9:32 PM: earlier quotes were "unfunny and don't make sense"; researched
#   viral workplace humor: Corporate Humor, When's Happy Hour (714K), Corporate Natalie (859K), Bored Panda/BuzzFeed
#   work-tweet roundups). Use ONLY these proven shapes, rewritten in fresh words (never copy a real post):
#   1. "Apparently [honest feeling] is not a valid reason to [skip work thing]."
#   2. Interview/boss question -> brutally honest answer ("strong interest in paying rent").
#   3. Tiny exaggeration ("Locked in. Do not contact me for the next 12 minutes." / "make it to lunch").
#   4. Polite corporate translation ("I can't say X, so I say 'let's take that offline.'").
#   5. Percentage truth ("My job is 90% saying 'happy to help' to things that make me unhappy").
#   6. Yes/yes/... "Next question." list (beak style).
#   7. Short setup -> 2-to-5-word twist ("She's a witness." / "So I thought about leaving.").
#   8. Job-ad / corporate-phrase translation ("fast-paced environment means...").
#   Must make sense to anyone with a job on first read; the twist must be a real punchline. Approved set: raccoon/batch03.json.
#   Avoid: "Nobody:/Absolutely nobody:", "Dear boss", "Me at 9 AM", weak puns, anything that needs explaining.
# >>> CATCHIER HOOKS (user, Oct 29 9:24 PM): every quote opens with a tense, instantly familiar first line
#   (a boss phrase in quotes, "Nobody: / My boss at 4:58 PM:", "Dear boss,", "Me at 9:00 AM:", "Rule #N")
#   and ends on a short twist punchline after a line break. Under 25 words when possible. Test: would someone
#   tag a coworker? If not, rewrite. Reference set: raccoon/batch02.json.
# >>> RACCOON QUOTE RULES (user, Oct 29): sarcastic, hook-based, viral-curiosity, emotionally driven, urgent but
#   funny quotes about workplace drama and difficult bosses/coworkers. Original wording only (never copy another
#   page's lines). Formats that work: "Rule #N" + a rule; "Boss says X. / Sarcastic reply"; "Do I...? Yes." list;
#   "TODAY IS NATIONAL ... DAY"; "Me: ... / My boss: ..."; corporate-phrase translations. 8 to 35 words per quote,
#   rotate the 8 background colors, never two of the same color in a row. Caption = one short sarcastic line + emoji,
#   a comment question with one CAPS word + down arrow, the follow line, 5 hashtags. Nothing cruel about
#   groups of people, no real names or companies, no claims presented as facts.
# >>> NEW FORMAT (user, Oct 29 9:17 PM): the page is being rebranded to single-image quote posts modeled on
#   the format of @beak.manifesto (format only, never its wording): solid bright background, a short sarcastic,
#   hook-driven, funny quote in heavy condensed black type (Anton) at the top, and a cartoon RACCOON in black
#   sunglasses in the bottom half. Topic stays workplace drama and difficult bosses/coworkers.
#   Renderer: raccoon/render_posts.py (1080x1350, Chromium), character: raccoon/raccoon.svg,
#   first batch: raccoon/batch01.json -> raccoon/out_batch01/. User approved 3 posts/day on Oct 29.
# >>> POSTING (user, Oct 29 9:25 PM PT): ONLY raccoon quote image posts, 3/day (12:00 PM, 5:30 PM, 8:30 PM PT) from raccoon/queue.json.
#   No old-format Reels/carousels, no Stories, no first comments, no comment checks. See STOP_ALL_POSTING.md.
# >>> COMMENT CHECKS STOPPED (user, Oct 27 11:13 AM: "Stop checking comment"). Do NOT run, restart or
#   reschedule the "Unspoken at Work: comment replies" chain, and ignore the nightly step that restarts it.
#   If a comment-check task fires anyway, do nothing and do not schedule another. First comments on new
#   posts are not comment checks and continue.
# >>> HOOK MASTER (user, Oct 27: installed the 9-skill Hook Master suite and ran it). Before rendering,
#   check every Reel hook against the four failures (delay, confusion, irrelevance, DISINTEREST):
#   the hook question must not have an obvious answer the viewer can give and swipe; text must ADD to the
#   on-screen prop, not repeat it; max ~15 words readable in the first 3.6 s (hook + prop together);
#   the payoff (reply bubble / exact words) must appear by ~4 s, not 8 s; never blame the viewer
#   ("because you always answer"); a stat card must support the exact line it sits under.
#   If the hook-master skills are installed (~/.claude/skills), run them on Reel 1 each night.
# >>> CAROUSELS (user, Oct 22 12:59 AM; PERMANENT): EVERY carousel uses the light background:
#   spec "look": "paper" on the carousel (all 7 slides). Reels keep rotating dark / paper / thread.
#   Hooks must be MORE curiosity-driven and built on RELATABLE things people go through at work,
#   and the carousel must show HOW TO DEAL WITH IT.
#   Slide 1 formula: a specific moment the reader has lived + a question they need answered,
#   and the sub line promises the fix ("Swipe for what to say." / "Here's how to handle it.").
#   Make the answer impossible to guess from slide 1 (curiosity gap); pay it off on slides 2-5,
#   slide 6 = exactly what to say or do, slide 7 = follow.
#   Idea bank (rotate; never repeat a used one; stats only from verified sources):
#   - "Your boss is nice to everyone but you. Why?"
#   - "You got 'feedback' in front of the whole team. What do you say next?"
#   - "Why does one coworker get away with everything?" (favoritism)
#   - [USED Oct 28 C007] "Your boss keeps 'forgetting' what they promised. Accident or pattern?"
#   - "Your boss changed the story. Which email saves you?"
#   - [USED Oct 22 C005] "Why are you exhausted after a day you did nothing?"
#   - [USED Oct 28 R014 reel] "'Got a minute?' Why does your heart race?"
#   - "Your coworker took credit in the meeting. Do you speak up?"
#   - "Doing two jobs for one paycheck. How did that happen?"
#   - "Why do the best employees quit first?"
#   - [USED Oct 23 C006] "Your 1:1 got canceled again. What is it telling you?"
#   - "'We're a family here.' So why do you feel replaceable?"
#   - [USED Oct 28 R015 reel] "Your boss only notices your mistakes. Why?"
#   - "You're dreading tomorrow already. Is it you, or the job?"
# >>> REACH FIX (user, Oct 22 12:46 AM: "do what you need to do to fix this"; PERMANENT).
# Views were low and every post used the same dark template. From now on:
# 1. LOOK ROTATION: never run a whole day (or 3 feed posts in a row) in one look. Looks in engine.py:
#    "dark" (night scenes, default) and "paper" (spec "look": "paper": ink on cream, rust accent).
#    Each day: at least one Reel or the carousel in "paper"; at least one Reel opening on the
#    "thread" prop (full chat from Boss, 2-3 messages popping in from 0.0 s, interval ~0.55, y ~980).
# 2. HOOK MOTION: Reel hook frame uses "reveal": true, "reveal_time": 0.9 (word-by-word in the first
#    second) so something moves instantly; the prop must be on screen by 0.15 s.
# 3. FIRST COMMENT: every feed post gets "first_comment" in posts/dayNN.json: a one-line question
#    with a one-word answer (YES/NO, STAY/GO, JOB/BOSS) + one emoji, no hearts. The posting task
#    POSTs it right after publishing: POST /<new media id>/comments?message=<first_comment>
#    (Make API Mutating Request). Pinning is not possible through the API.
# 4. LIMITS FOUND Oct 22: insights (#10) are blocked on all 3 Zapier Instagram connections (it's the
#    Zapier app's permission, reconnecting won't fix it). Trial Reels work through the API
#    (POST /media media_type=REELS video_url=... trial_params={"graduation_strategy":"SS_PERFORMANCE"},
#    then /media_publish) but Instagram refuses them below its follower minimum. Re-test once
#    followers >= 1,000 and switch one Reel a day to trial if accepted. Library/trending audio
#    cannot be added through this API.
# Keep all user timing, CTA and loop rules unchanged.
# >>> NO HEART SYMBOLS (user, Oct 20 10:52 PM): never use heart emojis/symbols (❤ 🤍 💙 ♥ <3 etc.) anywhere: captions, on-screen text, Stories, comment replies, DM texts.
# >>> COMMENTS + DMs (user, Oct 20 10:49 PM): auto-reply to every comment per COMMENTS.md (kind, general
# niche info backed by the FACT BANK, nothing secret, nothing offensive). A separate send_later chain
# "Unspoken at Work: comment replies" checks every 2 h, 8 AM-10:30 PM PT. Instagram DMs can't be sent
# through this Zapier connection (missing instagram_manage_messages); DM auto-replies live in Meta
# Business Suite (Inbox > Automations), set up by the user with text from DM_REPLIES.md.
# >>> OUTCOME + CURIOSITY LOOPS (user, Oct 20 5:05 PM; PERMANENT; applies to EVERY Reel and carousel).
# Keep niche, style, visuals, pacing, CTAs, hashtags and post counts the same. This block overrides
# any older wording/timing below where they conflict.
# 1. OUTCOME FIRST: before writing, put one sentence in the spec field "outcome":
#    "By the end of this post, viewers will know / feel / be able to ___." Cut anything that doesn't serve it.
# 2. HOOK = strong emotion built around an OPEN QUESTION (literal "?" or an obvious unanswered why/what/how).
# 3. LOOPS ALL THE WAY THROUGH: open a question -> pay it off -> open the next question. The LAST payoff
#    delivers the outcome (the solution), then the usual ending (follow frame / follow slide + CTA).
#    Record them in the spec field "loops": [{"open": "...", "payoff": "..."}, ...].
#    Reel shape: F1 hook opens Q1 -> F2 pays off Q1 + opens Q2 -> F3 pays off Q2 = outcome/solution -> F4 follow.
#    Carousel shape: each slide pays off the previous slide's question and opens the next; slide 6 = outcome.
# 4. SOMETHING NEW EVERY 2-4 SECONDS on Reels: a number, an example, a screenshot-style visual (notification,
#    mail, invite, task list, reply bubble, stat card) or a short story beat. Use prop timings to guarantee it.
# 5. EMOTION + CURIOSITY + PROOF in every post. Tag every frame/slide "beat": emotion | curiosity | proof
#    (can be several, e.g. "emotion,curiosity"). Cut any beat that gives none. PROOF = real numbers only:
#    a stat from an official/reputable source with the source on screen (engine `stat` prop, e.g. BLS) and
#    recorded in the spec field "sources", or concrete on-screen evidence (the actual message/invite).
#    Never invent statistics. Scenario details (a time on a text) are examples, not stats.
# 6. READABILITY: on-screen time >= 0.4 s per word of the main text AND >= 2.5 s per screen; sub lines <= 7
#    words; simple words. If it doesn't fit, CUT WORDS OR BEATS, don't speed up. Current 15-16 s Reel slots:
#    hook 0-3.6 s (<= 9 words), F2 3.9-7.2 s (<= 8 words), F3 7.5-11.8 s (<= 10 words),
#    follow 12.1-16.1 s (the fixed 10-word follow line needs 4.0 s, so Reels run ~16 s).
#    Carousels: <= 15 words main copy per slide (readability is per-swipe).
# 7. QA: run `python3 qa.py specs/dayNN.json` before rendering/scheduling. It must print PASS for every
#    post (outcome present, hook has an open question, loops present, last loop = outcome, beat tags on
#    every frame/slide with emotion+curiosity+proof all present, proof has a source, 0.4 s/word + 2.5 s
#    minimum, sub lines <= 7 words, a new visual at least every 4 s). Fix and re-run until all PASS.

# >>> USER UPDATE Oct 20, 3:15 AM (overrides older timing/CTA wording below):
# - Hook is 1 second faster. Reel timing (15 s total): hook frame 0-3.6 s (prop appears at 0.15 s),
#   feeling/quote 3.9-7.2, SOLUTION 7.5-11.8 (reply bubble 7.8-11.8), FOLLOW 12.1-15.
# - Hooks must be STRONGER and more emotional: a vivid, painful, specific moment
#   ("You're burning with fever. Your boss asks for proof." / "You gave them six years. They gave
#   you 15 minutes." / "You got written up. They got a laugh."), leading straight into the solution.
# - Follow ending wording (Reels, carousel last slide, captions): "Follow now, or you might never see
#   this page again." (Reel frame: "Follow now, or you might *never see this page again.*" + the
#   "Send this to..." sub line; caption: "Follow @unspokenatwork1 now, or you might never see this
#   page again."). This replaces the older "finds you again" / value-promise follow lines.
# >>> PERMANENT GROWTH SYSTEM (user, Oct 19 evening): GROWTH_SYSTEM.md in this folder is now the
# top-level operating system for @unspokenatwork1. It ADDS to everything below (keep: emotional
# hooks, literal props, solution + follow endings, 9-part captions, music). Key additions:
# - 30-day mission: 10,000 followers (target, not promise). Baseline Oct 19: 1 follower.
#   Track daily in growth_log.tsv: followers, net gain, avg daily gain, days left, needed/day, projection.
# - Adaptive volume: start 2 Reels + 1 carousel (+ 5-8 Story frames if publishing allows). Scale Reels
#   to 3-4/day only when real reach/shares/follows support it; scale back if quality drops.
# - Recurring series: What Your Boss Really Means (satire translations, labelled as commentary),
#   Toxic Boss Red Flags, Things Employees Are Afraid to Say, The Employee Survival Playbook,
#   The Workplace Double Standard, Burnout Nobody Talks About, Workplace Confessions (hypothetical,
#   labelled), Would You Quit?. Voice: blunt r/antiwork-style relatability, defensible opinions.
# - One CTA per post matched to its goal (share / save / comment / follow) in the caption; the Reel
#   itself still ends with the follow frame.
# - Evaluate posts at ~24/48/72 h with real insights; replicate winners' insight (never repost).
# - Daily report (actual metrics only, mark unavailable): followers, net growth, progress, needed/day,
#   Reels/carousels/Stories published, top post, key insight, tomorrow's adjustments.
# - Stories: Zapier has no Story action and the API cannot add poll/question stickers. Try image
#   Stories via the Make API Mutating Request (POST /{ig-id}/media media_type=STORIES image_url=...,
#   then /media_publish); if refused, report the limitation once and skip Stories.

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
