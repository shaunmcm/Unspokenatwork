"""Workplace Survivor carousels: 6 slides, 1080x1350, the user's own photo darkened behind
white Inter text (close to Instagram's Classic font). The photo pans a little across the slides
so the swipe feels like one continuous image.

Usage: python3 render_carousel.py carousels.json out_dir
item: {"id": "C001_name", "photo": "photos/xxx.jpg",
       "slides": [{"big": "...", "small": "..."}, ... 6 items]}
"big" = the main line(s) in bold; "small" = optional supporting text. Use \n for line breaks.
"""
import json, sys, os, base64, html
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HANDLE = "@work_placesurvivor"


def esc(t):
    return html.escape(t).replace("\n", "<br>")


def page(photo_b64, s, i, n):
    pos = 15 + (70 * i / max(1, n - 1))  # pan left -> right across the carousel
    first, last = i == 0, i == n - 1
    big_size = 92 if first else 70
    small = f'<div class="small">{esc(s["small"])}</div>' if s.get("small") else ""
    swipe = '<div class="swipe">Swipe →</div>' if first else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1080px;height:1350px;overflow:hidden;background:#000}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{photo_b64}) {pos}% 50%/cover no-repeat;
  filter:saturate(1.05)}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.68) 45%,rgba(0,0,0,.82) 100%)}}
.wrap{{position:absolute;left:90px;right:90px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;
  font-family:Inter;color:#fff}}
.big{{font-weight:800;font-size:{big_size}px;line-height:1.12;letter-spacing:-1px;text-shadow:0 2px 18px rgba(0,0,0,.5)}}
.small{{margin-top:40px;font-weight:500;font-size:44px;line-height:1.35;color:rgba(255,255,255,.92);text-shadow:0 2px 14px rgba(0,0,0,.6)}}
.count{{position:absolute;top:56px;right:64px;font:600 30px Inter;color:rgba(255,255,255,.85);
  background:rgba(0,0,0,.35);padding:8px 20px;border-radius:30px}}
.handle{{position:absolute;bottom:56px;left:90px;font:600 30px Inter;color:rgba(255,255,255,.8)}}
.swipe{{position:absolute;bottom:52px;right:80px;font:700 34px Inter;color:#fff}}
.bar{{width:120px;height:8px;background:#ff8a3d;border-radius:4px;margin-bottom:44px}}
</style></head><body><div class="bg"></div><div class="shade"></div>
<div class="count">{i+1}/{n}</div>
<div class="wrap"><div class="content">{'<div class="bar"></div>' if first or last else ''}<div class="big">{esc(s["big"])}</div>{small}</div></div>
<div class="handle">{HANDLE}</div>{swipe}</body></html>"""


def main():
    items = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for it in items:
            photo = it["photo"] if os.path.isabs(it["photo"]) else os.path.join(HERE, it["photo"])
            b64 = base64.b64encode(open(photo, "rb").read()).decode()
            n = len(it["slides"])
            for i, s in enumerate(it["slides"]):
                pg.set_content(page(b64, s, i, n))
                pg.evaluate("async () => { await document.fonts.ready; }")
                # shrink text if it would run off the slide
                pg.evaluate("""() => { const w = document.querySelector('.content'); const big = document.querySelector('.big');
                  const sm = document.querySelector('.small'); let k = 0;
                  while (w.getBoundingClientRect().height > 1050 && k < 30) { k++;
                    big.style.fontSize = (parseFloat(getComputedStyle(big).fontSize) - 3) + 'px';
                    if (sm) sm.style.fontSize = (parseFloat(getComputedStyle(sm).fontSize) - 1.5) + 'px'; } }""")
                pg.wait_for_timeout(60)
                path = os.path.join(out, f"{it['id']}_{i+1}.jpg")
                pg.screenshot(path=path, type="jpeg", quality=92)
                print(path)
        b.close()


if __name__ == "__main__":
    main()
