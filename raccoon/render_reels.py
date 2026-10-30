"""Turn raccoon quotes into 9:16 Reels (still image + slow push-in + upbeat music), like the
beak.manifesto format (their posts are Reels, not photos, which is where the views come from).

Usage: python3 render_reels.py batch.json out_dir [seconds]
"""
import json, sys, os, base64, html, subprocess, wave
import numpy as np
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "fonts", "Anton-Regular.ttf")
SVG = open(os.path.join(HERE, "raccoon.svg")).read()


def page(text, bg):
    font64 = base64.b64encode(open(FONT, "rb").read()).decode()
    t = html.escape(text).replace("\n", "<br>")
    n = len(text)
    size = 80 if n < 50 else 70 if n < 90 else 62 if n < 130 else 54 if n < 170 else 46
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Anton; src: url(data:font/ttf;base64,{font64}); }}
html,body {{ margin:0; width:1080px; height:1920px; background:{bg}; overflow:hidden; }}
.wrap {{ position:relative; width:1080px; height:1920px;
  background: radial-gradient(ellipse at 50% 30%, rgba(255,255,255,.10), rgba(0,0,0,0) 60%), {bg}; }}
.q {{ position:absolute; top:250px; left:90px; right:90px; text-align:center;
  font-family: Anton; font-size:{size}px; line-height:1.18; color:#141414; letter-spacing:.3px; }}
.r {{ position:absolute; left:50%; bottom:-110px; width:1120px; transform:translateX(-50%); }}
.r svg {{ width:100%; height:auto; display:block; }}
</style></head><body><div class="wrap"><div class="q">{t}</div><div class="r">{SVG}</div></div></body></html>"""


def upbeat(path, seconds, seed):
    """Light, bouncy 118 BPM loop: kick, clap, bass and major chord stabs. Original, generated here."""
    sr = 44100
    n = int(sr * seconds)
    t = np.arange(n) / sr
    rng = np.random.default_rng(seed)
    bpm = 118
    beat = 60 / bpm
    y = np.zeros(n)
    roots = [[60, 64, 67], [57, 60, 64], [65, 69, 72], [67, 71, 74]]  # C, Am, F, G
    off = int(rng.integers(0, 4))
    def note(m): return 440 * 2 ** ((m - 69) / 12)
    for b in range(int(seconds / beat) + 1):
        s = int(b * beat * sr)
        if s >= n:
            break
        L = min(n - s, int(0.25 * sr))
        tt = np.arange(L) / sr
        y[s:s + L] += 0.55 * np.sin(2 * np.pi * (55 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9)  # kick
        if b % 2 == 1:
            Lc = min(n - s, int(0.15 * sr))
            y[s:s + Lc] += 0.18 * rng.standard_normal(Lc) * np.exp(-np.arange(Lc) / sr * 28)  # clap
        chord = roots[((b // 4) + off) % 4]
        for half in (0, 0.5):
            s2 = int((b + half) * beat * sr)
            if s2 >= n:
                continue
            L2 = min(n - s2, int(0.22 * sr))
            tt2 = np.arange(L2) / sr
            env = np.exp(-tt2 * 10)
            for m in chord:
                y[s2:s2 + L2] += 0.06 * np.sign(np.sin(2 * np.pi * note(m + 12) * tt2)) * env * 0.6
            y[s2:s2 + L2] += 0.16 * np.sin(2 * np.pi * note(chord[0] - 24) * tt2) * np.exp(-tt2 * 4)
    fade = np.minimum(1, np.minimum(t / 0.3, (seconds - t) / 0.6))
    y = np.tanh(y * 1.2) * fade * 0.8
    st = np.stack([y, np.roll(y, 300)], 1)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((st * 32767).astype("<i2").tobytes())


def main():
    items = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    secs = float(sys.argv[3]) if len(sys.argv) > 3 else 7.0
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, it in enumerate(items):
            png = os.path.join(out, it["id"] + "_still.png")
            pg.set_content(page(it["text"], it["bg"]))
            pg.wait_for_timeout(150)
            pg.screenshot(path=png)
            wav = os.path.join(out, it["id"] + ".wav")
            upbeat(wav, secs, i * 7 + 3)
            mp4 = os.path.join(out, it["id"] + ".mp4")
            frames = int(secs * 30)
            vf = (f"scale=2160:-1,zoompan=z='1+0.035*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                  f":d={frames}:s=1080x1920:fps=30,format=yuv420p")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-i", wav,
                            "-vf", vf, "-t", str(secs), "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                            "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4], check=True)
            os.remove(wav)
            print(mp4)
        b.close()


if __name__ == "__main__":
    main()
