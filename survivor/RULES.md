# >>> MASTER CHECKLIST — run EVERY item on EVERY post (user, Nov 7: "do checks on every single instruction I have given you")
# The detailed rules are below; this list is the gate. Silently fix anything that fails before sending.
# CONTENT
#  [ ] Core story: a man stuck at a job he can't leave, extremely burnt out, because he has to provide. Emotional first.
#  [ ] Explains WHY it matters (not what it is); simple, relatable words; makes him feel seen and heard; innovative angle
#  [ ] Self-diagnosis hook: names a symptom he feels now ("wait... I have that") -> hidden cause ("so THAT'S my problem")
#  [ ] Broad packaging + hyper-specific problem
#  [ ] 4-point hook check: hyper-specific person/moment, emotion-triggering, ONE clear promise, positioned for the ideal viewer
#  [ ] Uses a hook format from the user's lists (stakes, authority, blunt, mistake, storytelling, contrarian, labeling,
#      curiosity gap, "Nobody is more stressed than...", "For the sake of your mental health..."), different from the last post,
#      and the on-screen hook and the caption's first line use DIFFERENT formats
#  [ ] Real proof: a named, checkable source quoted exactly, or an undeniable everyday example. No invented stats/quotes
#  [ ] ONE problem, ONE fix; visual tie-in to the actual photo/video
#  [ ] "I" lines are honest (true for most viewers) - never invent a personal event for the user
#  [ ] On-screen text talks to "you"/"if you..."/"someone who...", not "dads"
#  [ ] New topic (check topics_used.txt); no copying other creators' wording
# CAPTION
#  [ ] Hook + 👇, scene, hidden cause, feel-seen line, proof, "Why it matters", the fix, visual tie-in,
#      question with one CAPS word + 👇, 'Comment "HELP" if ...' (NO "I'll reply" of any kind),
#      "Full videos on my YouTube channel. The link is in my bio.", exactly 5 hashtags; delivered in a code block
# VISUAL
#  [ ] Photos AND videos come back as 9:16 Reels (photo_reel.py / overlay_text.py); carousels 6 slides 4:5 when asked
#  [ ] Full hook text on screen from frame 1, 2-4 sentences
#  [ ] Viral font: bold white, thick black outline, soft dark glow behind (no boxes); MID-SCREEN (TEXT_Y ~0.45-0.52),
#      never in the bottom 25%
#  [ ] Every word readable on frame 1 (LOOK at it); flag any brand logos for cropping
#  [ ] NO generated music (silent track); 7-15 s so it loops
# DELIVERY
#  [ ] SendUserFile the finished file + caption; nothing auto-posted to @work_placesurvivor; sources listed for the user
#  [ ] Log topic in topics_used.txt; push files to the repo

# Workplace Survivor (@work_placesurvivor) — daily carousels (user, Nov 5 2026)

NOT auto-posted. Each morning: make 2 carousels x 6 slides and SEND them to the user (SendUserFile, all 12 jpgs)
plus the 2 paste-ready post captions (SendUserMessage). The user posts them by hand.

Audience: men stuck in jobs they can't leave (family to provide for, nobody else hiring), burnt out.
Topics: micromanaging, toxic bosses, toxic coworkers, not tying identity to work, not caring what bosses/coworkers
think, not thinking/stressing about work when off, regret of trading family time for reputation at work,
burnout from chasing workplace approval.

Slide plan (6):
1. HOOK: emotionally strong, urgent, curiosity-driven, scroll-stopping (big line + 1 short line). Swipe →
2. Relatable scene (specific details he lives every day)
3. The twist / hard truth (open loop starts paying off)
4. The cost (family, time, him)
5. PAYOFF: what to do — concrete, doable even if he can't quit
6. One action for tonight + save/send line + "Comment HELP below."

Post caption: hook line, 3-6 short lines, one question with one CAPS word + 👇,
"Comment "HELP" if ...." / "Full videos on my YouTube channel. The link is in my bio."
then exactly 5 hashtags. No invented stats or quotes. Never name real people or companies.

Hook formats to rotate (user's lists; never reuse the same one two posts in a row):
Stakes: One [mistake] is all it takes to lose [result] / Don't [decision] until you can answer these questions /
 Want to ruin your [thing]? Keep doing this / Never [risky action]. Here's why / [Thing] is already changing... /
 Every [time] you [delay], [consequence] / Skip [step] and [consequence] is basically guaranteed /
 The [thing] you never changed is costing you [result] / In [niche], [thing] is the one thing you can't afford to get wrong /
 Ignore [warning sign] and you'll pay for it in [cost]
Authority: After [time] in [niche], this is the one thing I'd keep / The best [role] all [action]. Here's why /
 Here's what [top performers] know about [topic] that you don't
Blunt: You're wasting your time doing __ / The problem isn't __. It's __ / You need to stop taking advice from people who __ /
 You're making this mistake without even realizing it / I hate to break it to you, but __ /
 You're not going to like hearing this, but __ / Respectfully, you're doing __ all wrong /
 Can we stop pretending that __ works? / This is exactly why you're struggling with __ / You might be sabotaging your own __
Mistake: You're probably making at least one of these mistakes / These habits are quietly ruining your __ /
 The reason you keep failing at __ might be this / Please stop doing this if you care about __ /
 You're overlooking the most important part of __ / If you want __, stop making these excuses

Backgrounds: the user's own photos in photos/ (rotate; never the one with the Target logo). New photos the user
sends in chat can be added to photos/.
Render: python3 render_carousel.py day_<date>.json out/<date> ; LOOK at a contact sheet of all 12 before sending.
Log every topic to topics_used.txt and never repeat one.

## STANDING POST FORMAT (user, Nov 6 2026) — applies to EVERY post, carousel and Reel
- Explain WHY the concept matters, not what it is.
- Simple, relatable words. No big words.
- Prove it to the audience (a real, checkable source or an undeniable everyday example; never invented stats).
- Make him feel seen and heard.
- Be innovative (fresh angle, tie the visual to the message).
- HOOK SYSTEM = Self-Diagnosis Hook: name a symptom he's feeling right now ("wait... I have that"),
  then connect it to a cause he never thought of ("so THAT'S my problem"). Naming the problem makes us the
  authority; then give the fix. Use it on the on-screen text / slide 1, combined with the hook formats below.
- (user, Nov 6) For every photo/video the user sends: BURN the on-screen text onto it with
  python3 overlay_text.py <input> "<text with \n between sentences>" ready/<name>.<mp4|jpg>  (Inter Bold white on black
  highlight boxes, IG Classic style; video 1080x1920 with original audio, photo 1080x1350), check a frame, SendUserFile it,
  and give only the paste-ready post caption.
- (user, Nov 6) PACKAGING: be very SPECIFIC with the problem, but package it BROADLY so more people click.
  e.g. specific "feeling guilty resting because your boss might text" -> broad "Why most hardworking dads can't relax,
  even on vacation." Lead the on-screen text with the broad package, then the specific symptom.
- (user, Nov 6) On-screen text: NO highlight boxes. Plain bold white letters over the image (strong shadow only).
  Place text over the darkest/busiest-free part of the image (TEXT_Y=0.3-0.6 env var) and check it reads.
- (user, Nov 6) Photos must FIT REEL SIZE. Default: turn every photo into a 9:16 Reel with
  TEXT_Y=0.25-0.35 python3 photo_reel.py <photo> "<text>" ready/<name>_reel.mp4  (text from frame 1, slow push-in,
  soft music, 7-13 s so it loops). Videos -> overlay_text.py (already 9:16). Check frame 1 before sending.
- (user, Nov 6) ADD these hook formats to the rotation:
  Storytelling: I almost didn't [action] because I was afraid [outcome] / Nobody warned me this would happen after I finally [result] /
   The advice that changed how I [activity] was the advice I ignored for years / I thought I needed [obvious fix]. Turns out, I needed [different fix] /
   The first time I [action], I made a mistake I still remember / I wish someone had told me this before I spent [time] trying to [goal]
  Contrarian: Can we stop pretending [popular method] is the best way to [result]? / The more you [seemingly helpful action], the harder it is to [goal] /
   [Popular advice] sounds great, but it can make [problem] worse / I'd choose [underrated option] over [popular option] every time
  First-person "I" stories must stay honest: the page is voiced by the user, so never invent a personal event for him.
  Use universal "I" lines that are true for most stuck, burnt-out dads (e.g. "I thought I needed a new job. Turns out, I needed
  to stop taking this one home."), or ask the user for his real story when a hook needs a specific personal event.
  Still combine with: self-diagnosis hook, broad packaging + specific problem, why-it-matters, simple words, proof, feel seen.
- (user, Nov 6) CTA wording: "Comment "HELP" if ...." with NO "I'll reply" of any kind.
- (user, Nov 7) EVERY hook must pass 4 checks before it ships:
  1. HYPER-SPECIFIC: calls out a real person with a real problem (a dad stuck in a job he can't leave, in one exact moment:
     the driveway, the 9 PM text, the meeting where a coworker took credit). Not "workers" in general.
  2. EMOTION-TRIGGERING: frustration, curiosity, or fear of missing out (missing his kids, his weekends, his life).
  3. CLEAR PROMISE: the post solves ONE problem, and the hook says so (one fix, one rule, one script). Never a grab bag.
  4. POSITIONED FOR THE IDEAL VIEWER: written so the burnt-out, stuck, family-providing man feels "this is for me", and
     everyone else scrolls past. That's who comments HELP and watches the YouTube channel.
  Pattern to model (structure only): "How I found [hidden thing] that [most people] still don't know about." ->
  e.g. "The 2-minute habit in the driveway most burnt-out dads still don't know about."
- (user, Nov 7) On-screen text: speak to the person ("you", "someone who...", "if you...") instead of labeling him a "dad".
- (user, Nov 7) NO generated background music on anything (Reels get a silent track; the user adds a sound in Instagram).
- (user, Nov 7) Font = Instagram viral look: bold white text with a thin black outline, large (64px), in the UPPER third of
  the screen (default TEXT_Y 0.48 for Reels: mid-screen, user Nov 7 "lower where people see it right away") where people see it immediately.
- (user, Nov 7) Text position: MID-SCREEN (TEXT_Y ~0.45-0.52), not the top, never in the bottom 25% (Reel UI).
- (user, Nov 7) ADD these hook formats (for on-screen text AND post captions), still passing the 4-point check:
  Labeling: If you [behavior] more than [number] times a [period], you're [label] / If you're [stage] and still [habit], this is for you /
   If your [thing] has [symptom], you have a [root cause] problem / If you've said "[excuse]" this week, watch this twice /
   If you're the [role] who [behavior], this is going to sting / If [tool] is your whole plan for [goal], you don't have a plan /
   If [result] matters to you, [uncomfortable action] has to come first / If you've been about to start [thing] for [time], here's your push
  Curiosity gap: There's a [noun] hiding in your [thing] that's costing you [result] / [Top performers] have a word for [thing]. Nobody else uses it /
   [Weird fact] explains why your [thing] isn't working / The second thing [top performers] do matters more than the first /
   Watch what happens when you [small change] in [area] / [Ordinary thing] and [impressive thing] run on the same principle /
   Most people never notice this about [topic]. You won't unsee it / There's a question that fixes [problem] every time. Ask it /
   The reason [thing] works has nothing to do with [assumed reason]
  Use a different format for the on-screen hook and the caption's opening line so they don't repeat each other.
- (user, Nov 7) VISIBILITY: text must pop on any photo: 6px black outline + soft dark radial glow behind the text block
  (not a box). Always check frame 1; if any word fades into the background, darken/move it.
- (user, Nov 7) CORE STORY for every caption: a man stuck at a job he can't leave, extremely burnt out, because he HAS to
  provide for his family. Lead with emotion (the weight he carries silently, what it costs him and his family), make him
  feel seen, then the one clear fix.
- (user, Nov 7) ADD these hook formats:
  Call-out: "Nobody is more stressed than a [specific person in the audience] who doesn't know how to [specific struggle / desired result]."
   e.g. "Nobody is more stressed than a man who can't quit because his family needs the paycheck, and doesn't know how to stop bringing work home."
  Distinction: "For the sake of your mental health, please know there is a difference between [thing people confuse] and [the thing they mix it up with]."
   e.g. "For the sake of your mental health, please know there is a difference between providing for your family and disappearing from it."
- (user, Nov 9) Don't center posts on kids anymore. Center the man himself: stuck at a job he can't afford to quit because he has
  to provide. Family can be the reason he stays, but the story and the fix are about HIM.

## GROWTH FIXES (Nov 10 audit of @work_placesurvivor: 17 posts in 9 days, 111 followers, 0-6 likes per post, 1 comment total)
- Posting: max 2 Reels/day, at least 4 hours apart, best windows 6-8 AM or 6-9 PM PT. Never 2 posts within the same hour
  (the page posted 3 in 81 minutes on Nov 1 and 2 in 13 minutes at 2 AM on Nov 6; they compete with each other).
- On-screen text: hook line max ~12 words, then ONE specific line, then a short pointer ("Full fix in the caption ↓").
  Readable in under 3 seconds. Hyper-specific, about HIM (the provider stuck at a job he can't afford to quit).
- Visuals: prefer images that LOOK like his life (truck dashboard at dawn, parking lot, time clock, boots, lunch in the car,
  hard hat, empty break room, steering wheel at night). Scenery only when the metaphor is obvious. Ask the user for these clips.
- Caption: 80-150 words max. First line = searchable keywords + hook (e.g. "Stuck in a job you hate but can't afford to quit?").
  Keep: why it matters, one proof, one fix, CAPS question, Comment "HELP" if ..., YouTube line. ADD a share line:
  "Send this to a man who needs to hear it." (shares/sends are what push Reels to new people). Hashtags: exactly 5, each with #.
- Every Reel needs sound: the user adds a trending sound in Instagram at low volume (we export silent).
- Repurpose the user's own YouTube videos (his voice/face) into 20-40 s captioned Reels whenever he sends clips.
