"""v2 raccoon Reels: all-caps condensed text (Bebas Neue), pastel background, lines revealed one by one
so the punchline lands last (more watch time), raccoon at the bottom, original upbeat music.

Usage: python3 render_reels2.py batch.json out_dir
batch item: {"id": "...", "lines": ["LINE 1", "LINE 2", ...], "bg": "#fcf0cf"}
"""
import json, sys, os, base64, html, subprocess
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_reels import upbeat

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "fonts", "BebasNeue-Regular.ttf")
SVG = open(os.path.join(HERE, "raccoon.svg")).read()
PASTELS = ["#fcf0cf", "#fbe9e9", "#e3f4e1", "#e2eef9", "#ece6f7", "#fde5d3"]


def page(lines, shown, bg):
    font64 = base64.b64encode(open(FONT, "rb").read()).decode()
    words = sum(len(l.split()) for l in lines)
    size = 132 if words <= 14 else 120 if words <= 20 else 108 if words <= 28 else 96
    rows = "".join(f'<div style="visibility:{"visible" if i < shown else "hidden"}">{html.escape(l)}</div>'
                   for i, l in enumerate(lines))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Bebas; src: url(data:font/ttf;base64,{font64}); }}
html,body {{ margin:0; width:1080px; height:1920px; background:{bg}; overflow:hidden; }}
.q {{ position:absolute; top:250px; left:50px; right:50px; text-align:center; font-family: Bebas;
  font-size:{size}px; line-height:1.08; color:#151515; letter-spacing:.5px; }}
.r {{ position:absolute; left:50%; bottom:-140px; width:1040px; transform:translateX(-50%); }}
.r svg {{ width:100%; height:auto; display:block; }}
</style></head><body><div class="q">{rows}</div><div class="r">{SVG}</div>
</body></html>"""


def timings(lines):
    """ALL text on screen from frame 1 (user, Oct 30: viewers decide in one second). One still, long enough
    to read twice: ~0.35 s per word + 3 s, never under 7 s."""
    w = sum(len(l.split()) for l in lines)
    return [max(5.0, 0.28 * w + 1.8)]  # short enough to finish and loop (user, Oct 30 7:56 AM)


def main():
    items = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for k, it in enumerate(items):
            bg = it.get("bg") or PASTELS[k % len(PASTELS)]
            lines = it["lines"]
            durs = timings(lines)
            lst = os.path.join(out, it["id"] + "_list.txt")
            with open(lst, "w") as f:
                for i, d in enumerate(durs):
                    png = os.path.join(out, f"{it['id']}_{i}.png")
                    pg.set_content(page(lines, len(lines), bg))
                    pg.evaluate("""async () => { await document.fonts.ready;
                      const q = document.querySelector('.q'); let s = parseFloat(getComputedStyle(q).fontSize);
                      while (q.getBoundingClientRect().bottom > 1000 && s > 60) { s -= 4; q.style.fontSize = s + 'px'; } }""")
                    pg.wait_for_timeout(80)
                    pg.screenshot(path=png)
                    f.write(f"file '{os.path.abspath(png)}'\nduration {d}\n")
                f.write(f"file '{os.path.abspath(png)}'\n")
            total = sum(durs)
            wav = os.path.join(out, it["id"] + ".wav")
            upbeat(wav, total, k * 11 + 5)
            mp4 = os.path.join(out, it["id"] + ".mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
                            "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                            "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4], check=True)
            for i in range(len(durs)):
                os.remove(os.path.join(out, f"{it['id']}_{i}.png")) if i < len(durs) - 1 else None
            os.remove(wav); os.remove(lst)
            print(mp4, round(total, 1), "s")
        b.close()


if __name__ == "__main__":
    main()
