"""Render raccoon quote posts (1080x1350) with headless Chromium.

Usage: python3 render_posts.py quotes.json out_dir
quotes.json: [{"id": "Q001_meeting", "text": "...", "bg": "#f25c3c"}, ...]
Text is plain; wrap a phrase in *asterisks* to put it in CAPS emphasis (optional).
"""
import json, sys, os, html, base64
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "fonts", "Anton-Regular.ttf")
SVG = open(os.path.join(HERE, "raccoon.svg")).read()
PALETTE = ["#f25c3c", "#f7d774", "#8fe8a4", "#ff5aa8", "#7cc8f5", "#c9a7f5", "#ffa35c", "#a8a46a"]


def page(text, bg, handle="@unspokenatwork1"):
    font64 = base64.b64encode(open(FONT, "rb").read()).decode()
    t = html.escape(text).replace("\n", "<br>")
    n = len(text)
    size = 78 if n < 50 else 68 if n < 90 else 60 if n < 130 else 52 if n < 170 else 44
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Anton; src: url(data:font/ttf;base64,{font64}); }}
html,body {{ margin:0; width:1080px; height:1350px; background:{bg}; overflow:hidden; }}
.wrap {{ position:relative; width:1080px; height:1350px;
  background: radial-gradient(ellipse at 50% 35%, rgba(255,255,255,.10), rgba(0,0,0,0) 60%), {bg}; }}
.q {{ position:absolute; top:120px; left:90px; right:90px; text-align:center;
  font-family: Anton; font-size:{size}px; line-height:1.18; color:#141414; letter-spacing:.3px; }}
.r {{ position:absolute; left:50%; bottom:-30px; width:820px; transform:translateX(-50%); }}
.r svg {{ width:100%; height:auto; display:block; }}
.h {{ position:absolute; right:34px; bottom:22px; font-family: Anton; font-size:22px; color:rgba(20,20,20,.55); letter-spacing:1px; }}
</style></head><body><div class="wrap">
<div class="q">{t}</div><div class="r">{SVG}</div><div class="h">{html.escape(handle)}</div>
</div></body></html>"""


def main():
    items = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, it in enumerate(items):
            bg = it.get("bg") or PALETTE[i % len(PALETTE)]
            pg.set_content(page(it["text"], bg))
            pg.wait_for_timeout(150)
            path = os.path.join(out, it["id"] + ".jpg")
            pg.screenshot(path=path, type="jpeg", quality=93)
            print(path)
        b.close()


if __name__ == "__main__":
    main()
