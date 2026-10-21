"""Outcome + Curiosity Loops QA for Unspoken at Work specs.

Usage: python3 qa.py specs/dayNN.json [post_id ...]
Prints PASS / FAIL with reasons for every Reel and carousel. Exit code 1 if anything fails.
"""
import json, re, sys

SEC_PER_WORD = 0.4
MIN_SCREEN = 2.5
MAX_GAP = 4.0
SUB_MAX = 7
SLIDE_MAX_WORDS = 15


def words(t):
    t = re.sub(r"[*]", "", t or "")
    return len([w for w in t.split() if re.search(r"[A-Za-z0-9]", w)])


def has_open_question(t):
    t = (t or "").replace("*", "")
    return "?" in t


def beats_ok(items, label, errs):
    seen = set()
    for i, it in enumerate(items):
        b = it.get("beat", "")
        tags = {x.strip() for x in b.split(",") if x.strip()}
        if not tags or not tags & {"emotion", "curiosity", "proof"}:
            errs.append(f"{label} {i + 1}: no beat tag (emotion/curiosity/proof) -> cut it or tag it")
        seen |= tags
    for need in ("emotion", "curiosity", "proof"):
        if need not in seen:
            errs.append(f"post has no '{need}' beat")


def common(post, errs):
    if not str(post.get("outcome", "")).startswith("By the end of this post, viewers will"):
        errs.append('missing outcome sentence ("By the end of this post, viewers will know/feel/be able to ...")')
    loops = post.get("loops") or []
    if len(loops) < 2:
        errs.append("needs at least 2 curiosity loops (open -> payoff)")
    for i, lp in enumerate(loops):
        if not lp.get("open") or not lp.get("payoff"):
            errs.append(f"loop {i + 1} needs both open and payoff")
    if loops and post.get("outcome") and not loops[-1].get("delivers_outcome"):
        errs.append('last loop must deliver the outcome (set "delivers_outcome": true)')


def qa_reel(r):
    errs = []
    common(r, errs)
    fr = r["frames"]
    if not has_open_question(fr[0]["text"]):
        errs.append("hook (frame 1) must contain an open question '?'")
    for i, f in enumerate(fr):
        dur = f["end"] - f["start"]
        need = max(MIN_SCREEN, SEC_PER_WORD * words(f["text"]))
        if dur + 1e-6 < need:
            errs.append(f"frame {i + 1}: {words(f['text'])} words need {need:.1f}s, has {dur:.1f}s -> cut words")
        if f.get("sub") and words(f["sub"]) > SUB_MAX:
            errs.append(f"frame {i + 1}: sub line has {words(f['sub'])} words (max {SUB_MAX})")
    beats_ok(fr, "frame", errs)
    if any("proof" in f.get("beat", "") for f in fr):
        stat_props = [p for p in r.get("props", []) if p["type"] == "stat"]
        if stat_props and not all(p.get("source") for p in stat_props):
            errs.append("stat prop needs an on-screen source")
        if stat_props and not r.get("sources"):
            errs.append('stat used but spec has no "sources" list (URL of the official figure)')
    # something new every <= 4 s
    events = set()
    for f in fr:
        events.add(round(f["start"], 2))
    for p in r.get("props", []):
        events.add(round(p.get("start", 0), 2))
        if p["type"] == "tasks":
            st = p.get("start", 0) + 0.3
            for k in range(len(p["items"])):
                events.add(round(st + k * p.get("interval", 0.7), 2))
    ev = sorted(events) + [r["duration"]]
    for a, b in zip(ev, ev[1:]):
        if b - a > MAX_GAP + 1e-6:
            errs.append(f"nothing new between {a:.1f}s and {b:.1f}s ({b - a:.1f}s > {MAX_GAP}s)")
    return errs


def qa_carousel(c):
    errs = []
    common(c, errs)
    sl = c["slides"]
    if not has_open_question(sl[0]["text"] + " " + sl[0].get("sub", "")):
        errs.append("slide 1 hook must contain an open question '?'")
    for i, s in enumerate(sl):
        if words(s["text"]) > SLIDE_MAX_WORDS:
            errs.append(f"slide {i + 1}: {words(s['text'])} words (max {SLIDE_MAX_WORDS})")
    beats_ok(sl, "slide", errs)
    if any("proof" in s.get("beat", "") and re.search(r"\d", s["text"] + s.get("sub", "")) and "example" not in s.get("beat", "") for s in sl):
        if not c.get("sources"):
            errs.append('a proof slide uses a number but spec has no "sources" list')
    return errs


def main():
    spec = json.load(open(sys.argv[1]))
    only = set(sys.argv[2:])
    bad = 0
    for r in spec.get("reels", []):
        if only and r["id"] not in only:
            continue
        e = qa_reel(r)
        print(("PASS " if not e else "FAIL ") + r["id"] + ("" if not e else "\n  - " + "\n  - ".join(e)))
        bad += bool(e)
    for c in spec.get("carousels", []):
        if only and c["id"] not in only:
            continue
        e = qa_carousel(c)
        print(("PASS " if not e else "FAIL ") + c["id"] + ("" if not e else "\n  - " + "\n  - ".join(e)))
        bad += bool(e)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
