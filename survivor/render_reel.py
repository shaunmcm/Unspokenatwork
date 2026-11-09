"""Workplace Survivor kinetic-text Reels (1080x1920, 30 fps).

- Frame 1 already shows the full hook (viewers decide in a second).
- A teaser line on the hook opens a loop that the last scene pays off.
- Lines pop in word by word; key words turn orange.
- Slow continuous zoom and pan on the user's photo, a small punch-in on every scene change,
  and a switch to a calmer photo at the payoff (pattern interrupt).
- Progress bar across the top. The last scene sets up a rewatch loop.
- Original generated ambient music with a soft pulse and whooshes on scene changes.

Usage: python3 render_reel.py reel.json out_dir
"""
import json, sys, os, base64, html, subprocess, wave, math, shutil
import numpy as np
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
W, H = 1080, 1920
HANDLE = "@work_placesurvivor"


def word_time(text):
    return 0.30 * len(text.split()) + 0.45


def plan(reel):
    """Give every item an absolute appear time and every scene start/end."""
    t = 0.0
    out = []
    for si, sc in enumerate(reel["scenes"]):
        start = t
        items = []
        local = 0.0 if si else 0.0
        for k, it in enumerate(sc["items"]):
            if si == 0:
                at = 0.0  # hook is fully on screen at frame 1
            else:
                at = start + 0.25 + local
                local += 0.12 * len(it["text"].split()) + 0.35 + it.get("pause", 0)
            items.append(dict(it, at=at))
        if si == 0:
            dur = sc.get("hold", 3.0)
        else:
            last = items[-1]
            dur = (last["at"] - start) + word_time(last["text"]) + sc.get("hold", 0.6)
        end = start + dur
        out.append({"start": start, "end": end, "items": items, "photo": sc.get("photo", 0),
                    "teaser": sc.get("teaser")})
        t = end
    return out, t


def build_html(reel, scenes, total, photos_b64):
    imgs = "".join(
        f'<img class="bg" id="bg{i}" src="data:image/jpeg;base64,{b}">' for i, b in enumerate(photos_b64))
    sc_html = []
    for si, sc in enumerate(scenes):
        rows = []
        for k, it in enumerate(sc["items"]):
            hl = set(w.lower().strip(".,:'\"!?") for w in it.get("hl", []))
            words = []
            for wi, w in enumerate(it["text"].split()):
                cls = "w hl" if w.lower().strip(".,:'\"!?") in hl else "w"
                words.append(f'<span class="{cls}" data-at="{it["at"] + 0.06 * wi:.3f}">{html.escape(w)}</span>')
            rows.append(f'<div class="row {it.get("size","mid")}">{" ".join(words)}</div>')
        teaser = (f'<div class="teaser"><span class="w" data-at="0">{html.escape(sc["teaser"])}</span></div>'
                  if sc.get("teaser") else "")
        sc_html.append(f'<div class="scene" id="s{si}" data-start="{sc["start"]:.3f}" data-end="{sc["end"]:.3f}" '
                       f'data-photo="{sc["photo"]}">{teaser}<div class="stack">{"".join(rows)}</div></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#000;font-family:Inter}}
.bg{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;object-fit:cover;opacity:0;will-change:transform}}
.shade{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,.45),rgba(0,0,0,.78) 75%),
  linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.15) 40%,rgba(0,0,0,.6))}}
.scene{{position:absolute;inset:0;display:none}}
.stack{{position:absolute;left:84px;right:84px;top:50%;transform:translateY(-50%);color:#fff;text-align:center}}
.row{{margin:0 0 30px;-webkit-text-stroke:6px #000;paint-order:stroke fill;text-shadow:0 3px 12px rgba(0,0,0,.6)}}
.big{{font-weight:800;font-size:96px;line-height:1.1;letter-spacing:-1.5px}}
.mid{{font-weight:800;font-size:74px;line-height:1.14;letter-spacing:-1px}}
.small{{font-weight:500;font-size:50px;line-height:1.3;color:rgba(255,255,255,.92)}}
.w{{display:inline-block;opacity:0}}
.hl{{color:#ff8a3d}}
.teaser{{position:absolute;top:470px;left:0;right:0;text-align:center}}
.teaser .w{{font:800 44px Inter;color:#ff8a3d;-webkit-text-stroke:5px #000;paint-order:stroke fill}}
.bar{{position:absolute;top:0;left:0;height:10px;background:#ff8a3d;width:0}}
.track{{position:absolute;top:0;left:0;right:0;height:10px;background:rgba(255,255,255,.18)}}
.handle{{position:absolute;bottom:330px;left:0;right:0;text-align:center;font:600 34px Inter;color:rgba(255,255,255,.7)}}
.flash{{position:absolute;inset:0;background:#fff;opacity:0}}
</style></head><body>{imgs}<div class="shade"></div>{"".join(sc_html)}
<div class="track"></div><div class="bar"></div><div class="handle">{HANDLE}</div><div class="flash"></div>
<script>
const TOTAL={total:.3f};
const scenes=[...document.querySelectorAll('.scene')].map(e=>({{e,s:+e.dataset.start,end:+e.dataset.end,p:+e.dataset.photo,
  ws:[...e.querySelectorAll('.w')].map(w=>({{w,at:+w.dataset.at}}))}}));
const bgs=[...document.querySelectorAll('.bg')];
const bar=document.querySelector('.bar'), flash=document.querySelector('.flash');
function ease(x){{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}}
window.setT=function(t){{
  let cur=scenes.length-1; for(let i=0;i<scenes.length;i++){{ if(t<scenes[i].end){{cur=i;break}} }}
  scenes.forEach((s,i)=>{{ s.e.style.display = i===cur?'block':'none'; }});
  const sc=scenes[cur];
  for(const o of sc.ws){{ const k=cur===0?1:ease((t-o.at)/0.22);
    o.w.style.opacity=k; o.w.style.transform=`translateY(${{(1-k)*28}}px) scale(${{0.94+0.06*k}})`; }}
  // background: slow zoom/pan over the whole reel + punch-in at each scene change
  const since=t-sc.s, punch=cur===0?0:0.05*(1-ease(since/0.45));
  bgs.forEach((b,i)=>{{ b.style.opacity = i===sc.p?1:0;
    const z=1.08+0.14*(t/TOTAL)+punch, x=-30+60*(t/TOTAL);
    b.style.transform=`translateX(${{x}}px) scale(${{z}})`; }});
  bar.style.width=(100*t/TOTAL)+'%';
  flash.style.opacity = (cur>0 && since<0.12) ? 0.10*(1-since/0.12) : 0;
}};
</script></body></html>"""


def music(path, seconds, scene_starts, seed=3):
    sr = 44100
    n = int(sr * seconds)
    t = np.arange(n) / sr
    y = np.zeros(n)
    def f(m): return 440 * 2 ** ((m - 69) / 12)
    prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G
    bar_len = 60 / 72 * 4
    for b in range(int(seconds / bar_len) + 1):
        s = int(b * bar_len * sr)
        if s >= n: break
        L = min(n - s, int(bar_len * sr * 1.15))
        tt = np.arange(L) / sr
        env = np.minimum(1, tt / 0.6) * np.exp(-tt * 0.5)
        for m in prog[b % 4]:
            y[s:s + L] += 0.05 * (np.sin(2 * np.pi * f(m) * tt) + 0.3 * np.sin(2 * np.pi * f(m + 12) * tt)) * env
        y[s:s + L] += 0.07 * np.sin(2 * np.pi * f(prog[b % 4][0] - 24) * tt) * env
        # soft piano-ish notes on top
        for q in range(4):
            s2 = s + int(q * bar_len / 4 * sr)
            if s2 >= n: continue
            L2 = min(n - s2, int(0.9 * sr)); t2 = np.arange(L2) / sr
            m = prog[b % 4][q % 3] + 12
            y[s2:s2 + L2] += 0.045 * np.sin(2 * np.pi * f(m) * t2) * np.exp(-t2 * 3.5)
    beat = 60 / 72
    for k in range(int(seconds / beat) + 1):  # low heartbeat-like pulse
        s = int(k * beat * sr)
        if s >= n: break
        L = min(n - s, int(0.3 * sr)); tt = np.arange(L) / sr
        y[s:s + L] += 0.18 * np.sin(2 * np.pi * (48 + 40 * np.exp(-tt * 25)) * tt) * np.exp(-tt * 12)
    rng = np.random.default_rng(seed)
    for st in scene_starts[1:]:  # whoosh into each new scene
        s = int(max(0, st - 0.25) * sr); L = min(n - s, int(0.45 * sr))
        if L <= 0: continue
        noise = rng.standard_normal(L)
        noise = np.convolve(noise, np.ones(40) / 40, mode="same")
        tt = np.arange(L) / L
        y[s:s + L] += 0.35 * noise * np.sin(np.pi * tt) ** 2
    fade = np.minimum(1, np.minimum(t / 0.4, (seconds - t) / 0.8))
    y = np.tanh(y * 1.3) * fade * 0.85
    st = np.stack([y, np.roll(y, 220)], 1)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((st * 32767).astype("<i2").tobytes())


def main():
    reel = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    scenes, total = plan(reel)
    photos = [base64.b64encode(open(os.path.join(HERE, p), "rb").read()).decode() for p in reel["photos"]]
    doc = build_html(reel, scenes, total, photos)
    frames = os.path.join(out, reel["id"] + "_frames")
    shutil.rmtree(frames, ignore_errors=True); os.makedirs(frames)
    nf = int(math.ceil(total * FPS))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(doc)
        pg.evaluate("async () => { await document.fonts.ready; }")
        pg.wait_for_timeout(300)
        for i in range(nf):
            pg.evaluate(f"setT({i / FPS:.4f})")
            pg.screenshot(path=os.path.join(frames, f"{i:05d}.jpg"), type="jpeg", quality=88)
        b.close()
    wav = os.path.join(out, reel["id"] + ".wav")
    if reel.get("silent", True):  # user, Nov 7: no generated music
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                        "-t", str(total), wav], check=True)
    else:
        music(wav, total, [s["start"] for s in scenes])
    mp4 = os.path.join(out, reel["id"] + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(frames, "%05d.jpg"),
                    "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4], check=True)
    os.remove(wav)
    print(mp4, round(total, 1), "s", nf, "frames")
    print(json.dumps([[round(s["start"], 2), round(s["end"], 2)] for s in scenes]))


if __name__ == "__main__":
    main()
