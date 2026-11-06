"""Burn the on-screen hook text onto the user's photo or video, Instagram "Classic" style:
bold white Inter text on a soft black highlight box, centered in the safe zone.

Usage: python3 overlay_text.py <input photo|video> "<text>" <output path>
- Video -> 1080x1920 (9:16) mp4, original audio kept, text from frame 1.
- Photo -> 1080x1350 (4:5) jpg.
Use \\n in the text to force a line break between sentences.
"""
import sys, os, subprocess, html, tempfile
from playwright.sync_api import sync_playwright

VIDEO_EXT = {".mov", ".mp4", ".m4v", ".webm"}


def overlay_png(text, w, h, path):
    paras = "".join(f"<p><span>{html.escape(p.strip())}</span></p>" for p in text.split("\\n") if p.strip())
    top = 0.36 if h > 1500 else 0.42  # center of text block (keeps clear of Reel buttons/caption)
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:{w}px;height:{h}px;background:transparent;overflow:hidden}}
.t{{position:absolute;left:70px;right:70px;top:{top*100}%;transform:translateY(-50%);text-align:center;font-family:Inter}}
p{{margin:0 0 22px;line-height:1.42}}
span{{font-weight:700;font-size:52px;color:#fff;background:rgba(0,0,0,.72);padding:6px 18px;border-radius:14px;
  -webkit-box-decoration-break:clone;box-decoration-break:clone;letter-spacing:-.3px}}
</style></head><body><div class="t">{paras}</div></body></html>"""
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.set_content(doc)
        pg.evaluate("async () => { await document.fonts.ready; }")
        pg.evaluate("""() => { const t=document.querySelector('.t'); const s=[...document.querySelectorAll('span')];
          let k=0; while (t.getBoundingClientRect().height > %d && k<25) { k++;
            s.forEach(e=>e.style.fontSize=(parseFloat(getComputedStyle(e).fontSize)-2)+'px'); } }""" % int(h * 0.5))
        pg.screenshot(path=path, omit_background=True)
        b.close()


def main():
    src, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
    is_video = os.path.splitext(src)[1].lower() in VIDEO_EXT
    w, h = (1080, 1920) if is_video else (1080, 1350)
    ov = os.path.join(tempfile.mkdtemp(), "ov.png")
    overlay_png(text, w, h, ov)
    fit = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"
    if is_video:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", ov,
                        "-filter_complex", f"[0:v]{fit}[b];[b][1:v]overlay=0:0,format=yuv420p[v]",
                        "-map", "[v]", "-map", "0:a:0?", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", ov,
                        "-filter_complex", f"[0:v]{fit}[b];[b][1:v]overlay=0:0", "-q:v", "2", out], check=True)
    print(out)


if __name__ == "__main__":
    main()
