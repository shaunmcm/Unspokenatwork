"""Turn a still photo into a short, loopable 9:16 Reel (1080x1920, 30 fps):
full hook text on screen from frame 1 (plain bold white, no boxes), slow push-in on the photo,
soft original music. Length = time to read the text twice (min 7 s), so it loops.

Usage: TEXT_Y=0.3 python3 photo_reel.py <photo> "<text with \\n>" out.mp4
"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from overlay_text import overlay_png
from render_reel import music

src, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
words = len(text.replace("\\n", " ").split())
secs = max(7.0, round(0.32 * words + 2.0, 1))
tmp = tempfile.mkdtemp()
ov = os.path.join(tmp, "ov.png"); overlay_png(text, 1080, 1920, ov)
wav = os.path.join(tmp, "m.wav"); music(wav, secs, [0])
n = int(secs * 30)
vf = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
      f"zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30[b];"
      f"[b][1:v]overlay=0:0,format=yuv420p[v]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", src, "-i", ov, "-i", wav,
                "-filter_complex", vf, "-map", "[v]", "-map", "2:a", "-t", str(secs), "-c:v", "libx264",
                "-preset", "medium", "-crf", "19", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out],
               check=True)
print(out, secs, "s")
