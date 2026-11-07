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
  the screen (default TEXT_Y 0.26 for Reels) where people see it immediately.
