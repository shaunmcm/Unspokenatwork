"""Unspoken at Work - design engine.

Renders dark, cinematic, photo-free posts:
  * Reels  : 1080x1920 MP4, slow push-in, timed text frames, generated ambient music
  * Carousels: 1080x1350 JPG slides
Backgrounds are procedural "scenes" (rain window, glowing monitor, hallway, desk lamp,
office at night, empty conference room) built from blurred light, grain and vignette
so they read as moody atmosphere rather than illustration.

Usage:
  python3 engine.py reel   spec.json out_dir
  python3 engine.py carousel spec.json out_dir
"""
import json, math, os, random, subprocess, sys, wave, zlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_DIR = "/usr/share/fonts/opentype/inter"
F_HEAD = f"{FONT_DIR}/InterDisplay-Bold.otf"
F_BLACK = f"{FONT_DIR}/Inter-ExtraBold.otf"
F_MED = f"{FONT_DIR}/InterDisplay-Medium.otf"
F_SERIF_I = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
F_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

INK = (242, 240, 235)       # off-white text
AMBER = (217, 161, 91)      # brand accent
MUTED = (160, 166, 178)     # secondary text
HANDLE = "@unspokenatwork1"
THEMES = {"dark": ((242, 240, 235), (217, 161, 91), (160, 166, 178)),
          "paper": ((26, 26, 30), (178, 64, 34), (98, 94, 88))}


def set_theme(name):
    """Switch the text palette (dark = off-white on night scenes, paper = ink on cream)."""
    global INK, AMBER, MUTED
    INK, AMBER, MUTED = THEMES.get(name or "dark", THEMES["dark"])


def paper_bg(w, h, seed):
    """Light 'paper' look: warm cream gradient, faint ruled lines, soft grain. Breaks up the dark feed."""
    rnd = np.random.default_rng(seed)
    arr = _grad(w, h, (246, 241, 231), (230, 222, 207))
    yy = np.arange(h)[:, None]
    lines = ((yy % 64) < 2).astype(float) * 10
    arr = arr - lines[..., None] * np.array([0.2, 0.6, 1.0])
    arr += rnd.normal(0, 4, (h, w, 1))
    yy2, xx = np.mgrid[0:h, 0:w]
    v = np.sqrt(((xx - w / 2) / (w * 0.8)) ** 2 + ((yy2 - h / 2) / (h * 0.8)) ** 2)
    arr *= np.clip(1.06 - 0.16 * v ** 2, 0.8, 1)[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))

BRAND = "UNSPOKEN AT WORK"


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- scenes
def _grad(w, h, top, bottom):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(top, float)[None, None, :]
    b = np.array(bottom, float)[None, None, :]
    return np.repeat(a * (1 - t) + b * t, w, axis=1)


def _glow(arr, cx, cy, r, color, strength):
    h, w, _ = arr.shape
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    g = np.exp(-d ** 2)[..., None] * strength
    return arr + g * np.array(color, float)[None, None, :]


def scene(name, w, h, seed):
    rnd = random.Random(seed)
    if name == "rain_window":
        arr = _grad(w, h, (8, 12, 22), (18, 24, 38))
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        lights = Image.new("RGB", (w, h), (0, 0, 0))
        d = ImageDraw.Draw(lights)
        for _ in range(55):
            x, y = rnd.uniform(0, w), rnd.uniform(h * 0.6, h * 1.0)
            r = rnd.uniform(14, 60)
            c = rnd.choice([(230, 160, 80), (210, 140, 70), (90, 130, 200), (140, 170, 220), (240, 200, 140)])
            k = rnd.uniform(0.25, 0.7)
            d.ellipse([x - r, y - r, x + r, y + r], fill=tuple(int(v * k) for v in c))
        lights = lights.filter(ImageFilter.GaussianBlur(18))
        img = Image.fromarray(np.clip(np.asarray(img, float) + np.asarray(lights, float), 0, 255).astype("uint8"))
        rain = Image.new("L", (w, h), 0)
        dr = ImageDraw.Draw(rain)
        for _ in range(260):
            x = rnd.uniform(0, w); y = rnd.uniform(0, h); L = rnd.uniform(40, 220)
            dr.line([x, y, x + rnd.uniform(-6, 6), y + L], fill=rnd.randint(25, 70), width=rnd.choice([1, 2, 2, 3]))
        rain = rain.filter(ImageFilter.GaussianBlur(1.6))
        img = Image.composite(Image.new("RGB", (w, h), (170, 185, 210)), img, rain)
        d2 = ImageDraw.Draw(img)
        mx = int(w * rnd.uniform(0.62, 0.72))
        d2.rectangle([mx, 0, mx + 16, h], fill=(6, 8, 14))
        d2.rectangle([0, int(h * 0.64), w, int(h * 0.64) + 14], fill=(6, 8, 14))
        return img.filter(ImageFilter.GaussianBlur(1.2))

    if name == "monitor":
        arr = _grad(w, h, (6, 8, 14), (12, 14, 22))
        cx, cy = w * rnd.uniform(0.45, 0.6), h * 0.68
        mw, mh = w * 0.42, w * 0.26
        arr = _glow(arr, cx, cy, w * 0.55, (40, 80, 150), 0.9)
        arr = _glow(arr, cx, cy, w * 0.25, (80, 130, 210), 0.8)
        arr = _glow(arr, w * 0.12, h * 0.55, w * 0.25, (120, 80, 40), 0.5)
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        d = ImageDraw.Draw(img)
        d.rectangle([cx - mw / 2, cy - mh / 2, cx + mw / 2, cy + mh / 2], fill=(150, 190, 240))
        d.rectangle([cx - mw / 2 + 10, cy - mh / 2 + 10, cx + mw / 2 - 10, cy + mh / 2 - 10], fill=(110, 150, 215))
        d.rectangle([cx - 14, cy + mh / 2, cx + 14, cy + mh / 2 + 70], fill=(10, 12, 18))
        d.rectangle([0, cy + mh / 2 + 70, w, h], fill=(14, 16, 24))
        d.polygon([(cx - 150, cy + mh / 2 + 120), (cx + 150, cy + mh / 2 + 120), (cx + 175, cy + mh / 2 + 165), (cx - 175, cy + mh / 2 + 165)], fill=(30, 36, 52))
        return img.filter(ImageFilter.GaussianBlur(10))

    if name == "hallway":
        arr = _grad(w, h, (8, 10, 14), (16, 20, 24))
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        d = ImageDraw.Draw(img)
        vx, vy = w * rnd.uniform(0.45, 0.55), h * 0.66
        d.polygon([(0, h * 0.45), (vx - 30, vy - 30), (vx - 30, vy + 30), (0, h)], fill=(18, 22, 28))
        d.polygon([(w, h * 0.45), (vx + 30, vy - 30), (vx + 30, vy + 30), (w, h)], fill=(14, 18, 24))
        d.polygon([(0, h), (vx - 30, vy + 30), (vx + 30, vy + 30), (w, h)], fill=(22, 26, 30))
        d.rectangle([vx - 30, vy - 30, vx + 30, vy + 30], fill=(80, 96, 96))
        for i in range(7):
            t = (i + 1) / 8.0
            y = vy + 30 + (h - vy - 30) * t ** 1.7
            hw = 20 + (w * 0.18) * t ** 1.5
            d.rectangle([vx - hw, y - 4 - 10 * t, vx + hw, y + 4 + 10 * t], fill=(120 + int(60 * t), 140 + int(60 * t), 135 + int(55 * t)))
        img = img.filter(ImageFilter.GaussianBlur(9))
        arr = np.asarray(img, float)
        arr = _glow(arr, vx, vy, w * 0.35, (50, 70, 66), 0.6)
        return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))

    if name == "lamp":
        arr = _grad(w, h, (10, 9, 10), (20, 15, 12))
        lx, ly = w * rnd.uniform(0.15, 0.3), h * rnd.uniform(0.80, 0.84)
        arr = _glow(arr, lx, ly, w * 0.6, (150, 95, 40), 0.6)
        arr = _glow(arr, lx, ly, w * 0.2, (250, 190, 110), 0.6)
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        d = ImageDraw.Draw(img)
        d.rectangle([0, h * 0.88, w, h], fill=(30, 20, 14))
        d.rectangle([w * 0.42, h * 0.845, w * 0.80, h * 0.885], fill=(54, 40, 30))
        d.rectangle([w * 0.45, h * 0.825, w * 0.77, h * 0.845], fill=(70, 52, 38))
        return img.filter(ImageFilter.GaussianBlur(8))

    if name == "night_office":
        arr = _grad(w, h, (10, 14, 26), (24, 32, 52))
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        d = ImageDraw.Draw(img)
        bx0, bx1 = w * 0.08, w * 0.92
        top = h * 0.62
        d.rectangle([bx0, top, bx1, h], fill=(14, 16, 22))
        cols, rows = 9, 10
        cw, rh = (bx1 - bx0) / cols, (h - top) / rows
        for r in range(rows):
            for c in range(cols):
                if rnd.random() < 0.13:
                    col = rnd.choice([(170, 128, 75), (150, 158, 170), (160, 118, 66)])
                else:
                    col = (24, 28, 38)
                x = bx0 + c * cw + 6; y = top + r * rh + 6
                d.rectangle([x, y, x + cw - 14, y + rh - 14], fill=col)
        return img.filter(ImageFilter.GaussianBlur(5))

    if name == "conference":
        arr = _grad(w, h, (16, 20, 26), (8, 10, 14))
        arr = _glow(arr, w * 0.5, h * 0.62, w * 0.7, (70, 90, 100), 0.45)
        img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
        d = ImageDraw.Draw(img)
        d.polygon([(w * 0.12, h * 0.98), (w * 0.88, h * 0.98), (w * 0.62, h * 0.70), (w * 0.38, h * 0.70)], fill=(34, 38, 44))
        for i in range(5):
            t = i / 4
            yl = h * (0.72 + 0.22 * t)
            xl = w * (0.37 - 0.17 * t); xr = w * (0.63 + 0.17 * t)
            s = 22 + 26 * t
            d.rectangle([xl - s * 1.6, yl - s * 1.2, xl - s * 0.2, yl + s * 0.6], fill=(12, 14, 18))
            d.rectangle([xr + s * 0.2, yl - s * 1.2, xr + s * 1.6, yl + s * 0.6], fill=(12, 14, 18))
        return img.filter(ImageFilter.GaussianBlur(16))

    raise ValueError(name)


def finish(img, seed, darken_top=0.55):
    """Vignette, top-darkening for text, film grain."""
    w, h = img.size
    arr = np.asarray(img, float)
    yy, xx = np.mgrid[0:h, 0:w]
    v = np.sqrt(((xx - w / 2) / (w * 0.75)) ** 2 + ((yy - h / 2) / (h * 0.75)) ** 2)
    arr *= np.clip(1.15 - 0.55 * v ** 2, 0.25, 1)[..., None]
    t = np.clip(1 - yy / (h * 0.62), 0, 1)
    arr *= (1 - darken_top * t ** 1.4)[..., None]
    b = np.clip((yy - h * 0.84) / (h * 0.16), 0, 1)
    arr *= (1 - 0.7 * b ** 1.2)[..., None]
    rng = np.random.default_rng(seed)
    arr += rng.normal(0, 7, (h, w, 1))
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))


# ---------------------------------------------------------------- text
def parse(text):
    """'Your reward? *More work.*' -> [(word, accent)]"""
    out, acc = [], False
    for tok in text.split(" "):
        if not tok:
            continue
        start, end = tok.startswith("*"), tok.endswith("*") and len(tok) > 1
        if start:
            acc = True
        out.append((tok.strip("*"), acc))
        if end:
            acc = False
    return out


def wrap(words, fnt, maxw, draw):
    lines, cur = [], []
    for wd in words:
        trial = " ".join(x for x, _ in cur + [wd])
        if cur and draw.textlength(trial, font=fnt) > maxw:
            lines.append(cur); cur = [wd]
        else:
            cur.append(wd)
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, text, x, y, maxw, size, fpath=F_HEAD, color=None, accent=None, lh=1.18, max_lines=None, upto=None):
    color = INK if color is None else color
    accent = AMBER if accent is None else accent
    fnt = font(fpath, size)
    words = parse(text)
    lines = wrap(words, fnt, maxw, draw)
    while max_lines and len(lines) > max_lines and size > 30:
        size -= 4; fnt = font(fpath, size); lines = wrap(words, fnt, maxw, draw)
    k = 0
    for line in lines:
        cx = x
        for i, (wd, acc) in enumerate(line):
            s = wd + (" " if i < len(line) - 1 else "")
            k += 1
            if upto is not None and k > upto:
                continue
            draw.text((cx, y), s, font=fnt, fill=accent if acc else color)
            cx += draw.textlength(s, font=fnt)
        y += int(size * lh)
    return y


def block_height(text, maxw, size, fpath=F_HEAD, lh=1.18):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    return len(wrap(parse(text), font(fpath, size), maxw, d)) * int(size * lh)


def brand_marks(draw, w, h, series=None, top=150, show_handle=True, handle_y=None):
    f = font(F_BLACK, 26)
    x = 90
    spaced = "  ".join(BRAND.split(" "))
    draw.text((x, top), " ".join(spaced), font=f, fill=AMBER)
    draw.rectangle([x, top + 44, x + 70, top + 47], fill=AMBER)
    if series:
        draw.text((x, top + 64), series, font=font(F_SERIF_I, 34), fill=MUTED)
    if show_handle:
        draw.text((x, handle_y or h - 120), HANDLE, font=font(F_MED, 30), fill=MUTED)


# ---------------------------------------------------------------- music
def music(path, seconds, seed):
    sr = 44100
    rnd = random.Random(seed)
    n = int(sr * seconds)
    t = np.arange(n) / sr
    roots = [57, 55, 52, 50, 53, 48]       # A, G, E, D, F, C
    root = rnd.choice(roots)
    progs = [[0, -4, 3, -2], [0, 3, -4, -5], [0, -2, -4, -5], [0, 5, 3, -4]]
    prog = rnd.choice(progs)
    minor = [0, 3, 7, 10, 14]
    major = [0, 4, 7, 11, 14]
    bar = seconds / len(prog)
    out = np.zeros(n)
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    for i, step in enumerate(prog):
        quality = minor if step in (0, 5, -5 + 12) else rnd.choice([major, minor])
        s0 = int(i * bar * sr); s1 = min(n, int((i + 1) * bar * sr + sr * 1.5))
        tt = t[s0:s1] - t[s0]
        env = np.minimum(1, tt / 1.2) * np.exp(-np.maximum(0, tt - bar) * 1.8)
        for k, iv in enumerate(quality[:4]):
            f = hz(root + step - 12 + iv)
            det = 1 + rnd.uniform(-0.002, 0.002)
            tone = np.sin(2 * np.pi * f * det * tt) + 0.25 * np.sin(2 * np.pi * 2 * f * tt) + 0.08 * np.sin(2 * np.pi * 3 * f * tt)
            out[s0:s1] += 0.10 * tone * env * (0.8 if k else 1.0)
        # sparse piano notes
        beats = rnd.choice([2, 3, 4])
        for b in range(beats):
            ns = s0 + int((b / beats) * bar * sr + rnd.uniform(0, 0.15) * sr)
            if ns >= n:
                continue
            m = root + step + rnd.choice(quality[:5]) + 12
            f = hz(m)
            ln = min(n - ns, int(sr * 3))
            tp = np.arange(ln) / sr
            pen = np.exp(-tp * 1.6) * np.minimum(1, tp / 0.008)
            note = (np.sin(2 * np.pi * f * tp) + 0.4 * np.sin(2 * np.pi * 2 * f * tp) * np.exp(-tp * 3) + 0.15 * np.sin(2 * np.pi * 3 * f * tp) * np.exp(-tp * 5))
            out[ns:ns + ln] += 0.16 * note * pen
    # simple reverb: a few feedback delays
    wet = out.copy()
    for dl, g in [(0.113, 0.42), (0.197, 0.33), (0.291, 0.27), (0.43, 0.2)]:
        k = int(dl * sr)
        for _ in range(4):
            sh = np.zeros(n); sh[k:] = wet[:-k] * g
            wet += sh * 0.5
    mix = 0.6 * out + 0.4 * wet
    # gentle lowpass
    a = 0.15
    y = np.zeros(n); acc = 0.0
    for idx in range(0, n):
        acc += a * (mix[idx] - acc); y[idx] = acc
    fade = np.minimum(1, t / 0.6) * np.minimum(1, (seconds - t) / 1.5)
    y *= fade
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.55
    st = np.stack([y, np.roll(y, int(0.012 * sr))], 1)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((st * 32767).astype("<i2").tobytes())



# ---------------------------------------------------------------- props (literal, self-explanatory visuals)
def _rr(w, h, r, fill):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=fill)
    return im


def _ease(p):
    p = max(0.0, min(1.0, p))
    return 1 - (1 - p) ** 3


def _fade(im, a):
    if a >= 0.999:
        return im
    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    return im


def notification_card(p, W):
    """iPhone-style text notification: app row, sender, message."""
    cw, ch = W - 140, 250
    card = _rr(cw, ch, 44, (44, 48, 58, 238))
    d = ImageDraw.Draw(card)
    # app icon: green rounded square with a white speech bubble
    if p.get("app", "").lower() in ("mail", "email", "outlook", "gmail"):
        icon = _rr(76, 76, 18, (20, 122, 250, 255))
        di = ImageDraw.Draw(icon)
        di.rectangle([14, 22, 62, 56], fill=(255, 255, 255, 255))
        di.line([(14, 22), (38, 42), (62, 22)], fill=(20, 122, 250, 255), width=4)
    else:
        icon = _rr(76, 76, 18, (52, 199, 89, 255))
        di = ImageDraw.Draw(icon)
        di.ellipse([14, 16, 62, 52], fill=(255, 255, 255, 255))
        di.polygon([(22, 44), (18, 62), (36, 50)], fill=(255, 255, 255, 255))
    card.alpha_composite(icon, (34, 34))
    d.text((132, 36), p.get("app", "MESSAGES").upper(), font=font(F_MED, 28), fill=(170, 176, 188))
    tf = font(F_MED, 28)
    tm = p.get("time", "now")
    d.text((cw - 40 - d.textlength(tm, font=tf), 36), tm, font=tf, fill=(170, 176, 188))
    d.text((132, 78), p["sender"], font=font(F_HEAD, 46), fill=(255, 255, 255))
    draw_block(d, p["body"], 132, 140, cw - 132 - 40, 38, fpath=F_MED, color=(225, 228, 234), max_lines=2, lh=1.25)
    return card


def task_assets(p, W):
    pw = W - 140
    head = _rr(pw, 120, 36, (36, 40, 50, 240))
    d = ImageDraw.Draw(head)
    d.text((40, 36), p.get("title", "Your to-do list"), font=font(F_HEAD, 44), fill=(255, 255, 255))
    rows = []
    for it in p["items"]:
        r = _rr(pw, 84, 22, (30, 34, 44, 235))
        dr = ImageDraw.Draw(r)
        dr.rounded_rectangle([34, 24, 70, 60], 8, outline=(150, 156, 168), width=3)
        tag = it.get("tag", "from Manager")
        tf = font(F_MED, 26)
        tw = dr.textlength(tag, font=tf)
        avail = pw - 100 - tw - 70
        txt = it["text"]; f = font(F_MED, 36)
        while dr.textlength(txt, font=f) > avail and f.size > 26:
            f = font(F_MED, f.size - 2)
        dr.text((96, 22), txt, font=f, fill=(235, 236, 240))
        dr.text((pw - 36 - tw, 28), tag, font=tf, fill=AMBER)
        rows.append(r)
    return head, rows


def invite_card(p, W):
    """Calendar invite: date tile, title, time, organizer, Accept/Decline."""
    cw, ch = W - 140, 400
    card = _rr(cw, ch, 40, (44, 48, 58, 240))
    d = ImageDraw.Draw(card)
    tile = _rr(120, 130, 22, (250, 250, 252, 255))
    dt = ImageDraw.Draw(tile)
    dt.rounded_rectangle([0, 0, 119, 40], 22, fill=(220, 60, 55))
    dt.rectangle([0, 22, 119, 40], fill=(220, 60, 55))
    mf = font(F_BLACK, 24)
    m = p.get("month", "FRI").upper()
    dt.text(((120 - dt.textlength(m, font=mf)) / 2, 8), m, font=mf, fill=(255, 255, 255))
    df = font(F_HEAD, 60)
    dd = str(p.get("day", "24"))
    dt.text(((120 - dt.textlength(dd, font=df)) / 2, 50), dd, font=df, fill=(30, 30, 34))
    card.alpha_composite(tile, (34, 34))
    d.text((180, 34), p.get("app", "CALENDAR INVITE").upper(), font=font(F_MED, 26), fill=(170, 176, 188))
    d.text((180, 70), p["title"], font=font(F_HEAD, 48), fill=(255, 255, 255))
    d.text((180, 132), p["when"], font=font(F_MED, 34), fill=(225, 228, 234))
    d.text((180, 178), p.get("from", "From: Manager"), font=font(F_MED, 30), fill=AMBER)
    if p.get("note"):
        d.text((180, 220), p["note"], font=font(F_SERIF_I, 30), fill=(150, 156, 168))
    bw_, by = (cw - 34 * 3) // 2, ch - 34 - 10
    for i, (lab, col) in enumerate([("Accept", (52, 120, 246)), ("Decline", (70, 74, 86))]):
        x = 34 + i * (bw_ + 34)
        d.rounded_rectangle([x, by - 46, x + bw_, by + 10], 18, fill=col)
        f = font(F_HEAD, 30)
        d.text((x + (bw_ - d.textlength(lab, font=f)) / 2, by - 38), lab, font=f, fill=(255, 255, 255))
    return card


def reply_bubble(p, W):
    """Outgoing message bubble (what YOU say) - the solution script."""
    maxw = W - 260
    d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = font(F_MED, 42)
    lines = wrap(parse(p["text"]), f, maxw - 80, d0)
    bh = 48 + len(lines) * 56 + 20
    bw_ = int(max(d0.textlength(" ".join(w for w, _ in ln), font=f) for ln in lines)) + 80
    im = Image.new("RGBA", (W - 140, bh + 50), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0 = im.width - bw_
    d.rounded_rectangle([x0, 0, im.width - 1, bh], 40, fill=(52, 120, 246, 250))
    y = 30
    for ln in lines:
        d.text((x0 + 40, y), " ".join(w for w, _ in ln), font=f, fill=(255, 255, 255))
        y += 56
    lab = p.get("label", "You")
    lf = font(F_MED, 26)
    d.text((im.width - d.textlength(lab, font=lf) - 10, bh + 12), lab, font=lf, fill=(150, 156, 168))
    return im


def follow_button(p, W):
    """Profile-style follow row: avatar, handle, Follow pill."""
    cw, ch = W - 140, 170
    card = _rr(cw, ch, 40, (36, 40, 50, 235))
    d = ImageDraw.Draw(card)
    d.ellipse([34, 35, 134, 135], fill=(26, 28, 34), outline=AMBER, width=4)
    uf = font(F_BLACK, 34)
    d.text((84 - d.textlength("UW", font=uf) / 2, 64), "UW", font=uf, fill=AMBER)
    d.text((164, 44), HANDLE, font=font(F_HEAD, 40), fill=(255, 255, 255))
    d.text((164, 96), p.get("sub", "Unspoken at Work"), font=font(F_MED, 28), fill=(170, 176, 188))
    lab = "Follow"; f = font(F_HEAD, 34)
    bw_ = int(d.textlength(lab, font=f)) + 70
    bx = cw - 34 - bw_
    d.rounded_rectangle([bx, 52, bx + bw_, 118], 20, fill=(52, 120, 246))
    d.text((bx + 35, 62), lab, font=f, fill=(255, 255, 255))
    return card


def stat_card(p, W):
    """Proof card: big real number + label + on-screen source."""
    cw, ch = W - 140, 300
    card = _rr(cw, ch, 40, (36, 40, 50, 240))
    d = ImageDraw.Draw(card)
    d.text((44, 34), p.get("kicker", "THE NUMBERS").upper(), font=font(F_BLACK, 26), fill=AMBER)
    nf = font(F_BLACK, 110)
    d.text((40, 70), p["number"], font=nf, fill=(255, 255, 255))
    draw_block(d, p["label"], 44, 200, cw - 88, 34, fpath=F_MED, color=(225, 228, 234), max_lines=2, lh=1.2)
    sf = font(F_MED, 24)
    src = "Source: " + p["source"]
    d.text((cw - 40 - d.textlength(src, font=sf), 40), src, font=sf, fill=(150, 156, 168))
    return card


def thread_assets(p, W):
    """Full chat thread from the boss: header + incoming gray bubbles that pop in one by one."""
    pw = W - 140
    head = _rr(pw, 130, 36, (30, 32, 38, 245))
    d = ImageDraw.Draw(head)
    d.ellipse([30, 25, 110, 105], fill=(120, 126, 140))
    af = font(F_BLACK, 34)
    ini = p.get("initials", "B")
    d.text((70 - d.textlength(ini, font=af) / 2, 44), ini, font=af, fill=(255, 255, 255))
    d.text((134, 28), p.get("sender", "Boss"), font=font(F_HEAD, 44), fill=(255, 255, 255))
    d.text((134, 80), p.get("status", "iMessage"), font=font(F_MED, 26), fill=(160, 166, 178))
    d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = font(F_MED, 40)
    bubbles = []
    for m in p["messages"]:
        lines = wrap(parse(m["text"]), f, pw - 240, d0)
        bh = 40 + len(lines) * 52
        bw_ = int(max(d0.textlength(" ".join(w for w, _ in ln), font=f) for ln in lines)) + 76
        im = Image.new("RGBA", (pw, bh + (40 if m.get("time") else 0)), (0, 0, 0, 0))
        di = ImageDraw.Draw(im)
        di.rounded_rectangle([0, 0, bw_, bh], 36, fill=(58, 60, 68, 250))
        y = 22
        for ln in lines:
            di.text((38, y), " ".join(w for w, _ in ln), font=f, fill=(255, 255, 255))
            y += 52
        if m.get("time"):
            di.text((12, bh + 8), m["time"], font=font(F_MED, 24), fill=(150, 156, 168))
        bubbles.append(im)
    return head, bubbles


def prop_layer(p, W, H, tt, assets):
    """Return an RGBA layer with the prop drawn at time tt (None = nothing yet)."""
    if tt < p.get("start", 0) or tt > p.get("end", 1e9):
        return None
    out_a = 1.0
    if "end" in p and tt > p["end"] - 0.35:
        out_a = max(0.0, (p["end"] - tt) / 0.35)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x0, y0 = 70, p.get("y", 1080)
    if p["type"] in ("notification", "invite", "reply", "follow", "stat"):
        k = _ease((tt - p.get("start", 0)) / 0.4)
        layer.alpha_composite(_fade(assets, k * out_a), (x0, int(y0 + (1 - k) * 80)))
        return layer
    if p["type"] == "thread":
        head, bubs = assets
        k0 = _ease((tt - p.get("start", 0)) / 0.3)
        layer.alpha_composite(_fade(head, k0), (x0, y0))
        y = y0 + 150
        for i, b in enumerate(bubs):
            st = p.get("start", 0) + 0.15 + i * p.get("interval", 0.6)
            if tt < st:
                break
            k = _ease((tt - st) / 0.25)
            sc = 0.85 + 0.15 * k
            bb = b.resize((max(1, int(b.width * sc)), max(1, int(b.height * sc))), Image.BILINEAR)
            layer.alpha_composite(_fade(bb, k), (x0, int(y + (1 - k) * 20)))
            y += b.height + 18
        return _fade(layer, out_a)
    if p["type"] == "tasks":
        head, rows = assets
        layer.alpha_composite(head, (x0, y0))
        n_new = p.get("start_items", 0)
        y = y0 + 132
        for i, r in enumerate(rows):
            st = p.get("start", 0) + 0.3 + i * p.get("interval", 0.7)
            if tt < st:
                break
            k = _ease((tt - st) / 0.3)
            layer.alpha_composite(_fade(r, k), (x0, int(y + (1 - k) * 30)))
            y += 96
        # live counter badge
        shown = sum(1 for i in range(len(rows)) if tt >= p.get("start", 0) + 0.3 + i * p.get("interval", 0.7))
        d = ImageDraw.Draw(layer)
        badge = str(shown)
        bf = font(F_BLACK, 36)
        bw_ = max(64, int(d.textlength(badge, font=bf)) + 36)
        bx = x0 + head.width - 40 - bw_
        d.rounded_rectangle([bx, y0 + 30, bx + bw_, y0 + 90], 30, fill=(205, 70, 60))
        d.text((bx + (bw_ - d.textlength(badge, font=bf)) / 2, y0 + 38), badge, font=bf, fill=(255, 255, 255))
        return _fade(layer, out_a)
    return None


def prop_assets(p, W):
    if p["type"] == "notification":
        return notification_card(p, W)
    if p["type"] == "tasks":
        return task_assets(p, W)
    if p["type"] == "thread":
        return thread_assets(p, W)
    if p["type"] == "invite":
        return invite_card(p, W)
    if p["type"] == "reply":
        return reply_bubble(p, W)
    if p["type"] == "follow":
        return follow_button(p, W)
    if p["type"] == "stat":
        return stat_card(p, W)

def score(path, seconds, seed, cuts):
    """Story-synced emotional score. cuts = frame start times [hook, feeling, solution, follow].
    Hook: minor pad + slow heartbeat + a piano 'ping' on frame 0 (sound from the first instant).
    Feeling: chord drops to the sad VI, falling piano line.
    Riser into the SOLUTION, soft low hit on the cut, lift to the relative MAJOR (relief).
    Follow: warm major resolve, heartbeat gone. Every chord change lands on a text change."""
    sr = 44100
    rnd = random.Random(seed)
    n = int(sr * seconds)
    t = np.arange(n) / sr
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    root = rnd.choice([57, 55, 52, 50, 53])
    cuts = list(cuts) + [seconds]
    # (semitone offset from root, chord quality)
    minor = [0, 3, 7, 10]; major = [0, 4, 7, 11]; add9 = [0, 4, 7, 14]
    plan = [(0, minor), (-4, major), (3, add9), (-2, major)]
    if len(cuts) - 1 < 4:
        plan = plan[:len(cuts) - 1]
    out = np.zeros(n)

    def add(sig, s0):
        e = min(n, s0 + len(sig))
        if s0 < n:
            out[s0:e] += sig[:e - s0]

    def piano(m, s0, amp=0.16, length=3.0):
        ln = int(sr * length); tp = np.arange(ln) / sr; f = hz(m)
        env = np.exp(-tp * 1.5) * np.minimum(1, tp / 0.006)
        note = np.sin(2*np.pi*f*tp) + 0.45*np.sin(2*np.pi*2*f*tp)*np.exp(-tp*3) + 0.15*np.sin(2*np.pi*3*f*tp)*np.exp(-tp*6)
        add(amp * note * env, s0)

    for i, (step, q) in enumerate(plan):
        a, b = cuts[i], cuts[i + 1]
        s0 = int(a * sr); ln = int((b - a + 1.6) * sr)
        tp = np.arange(ln) / sr
        sec = b - a
        att = 0.05 if i else 0.02
        env = np.minimum(1, tp / max(att, 0.6 if i else 0.25)) * np.exp(-np.maximum(0, tp - sec) * 2.2)
        bright = 1.0 + 0.35 * (i >= 2)
        for k, iv in enumerate(q):
            f = hz(root + step - 12 + iv)
            tone = np.sin(2*np.pi*f*tp) + 0.22*bright*np.sin(2*np.pi*2*f*tp) + 0.07*np.sin(2*np.pi*3*f*tp)
            add(0.085 * tone * env * (1.0 if k == 0 else 0.75), s0)
        # bass
        add(0.10 * np.sin(2*np.pi*hz(root + step - 24)*tp) * env, s0)
        # piano line: hook = single ping then sparse; feeling = falling; solution = rising arpeggio
        scale = [0, 2, 3, 5, 7, 8, 10, 12] if i < 2 else [0, 2, 4, 5, 7, 9, 11, 12]
        if i == 0:
            piano(root + 12 + q[2], s0, 0.2)
            for j in range(1, int(sec // 1.4) + 1):
                piano(root + 12 + rnd.choice(q), s0 + int(j * 1.4 * sr), 0.11)
        elif i == 1:
            notes = sorted([root + step + 12 + x for x in rnd.sample(scale, 4)], reverse=True)
            for j, m in enumerate(notes):
                piano(m, s0 + int(j * sec / len(notes) * sr), 0.13)
        else:
            notes = [root + step + 12 + x for x in q] + [root + step + 24]
            for j, m in enumerate(notes):
                piano(m, s0 + int(j * min(0.42, sec / (len(notes) + 1)) * sr), 0.12 if i == 2 else 0.1)
    # heartbeat during hook + feeling (tension), gone at the solution (relief)
    if len(cuts) > 2:
        hb_end = cuts[2] - 0.4
        tb = 0.35
        while tb < hb_end:
            for off, amp in [(0, 0.5), (0.22, 0.32)]:
                ln = int(0.25 * sr); tp = np.arange(ln) / sr
                add(amp * 0.5 * np.sin(2*np.pi*(52 - 20*tp)*tp) * np.exp(-tp * 18), int((tb + off) * sr))
            tb += 1.05
        # riser into the solution + soft low hit on the cut
        r0 = max(0.0, cuts[2] - 0.9); ln = int((cuts[2] - r0) * sr); tp = np.arange(ln) / sr
        rng = np.random.default_rng(seed)
        noise = rng.normal(0, 1, ln)
        noise = np.convolve(noise, np.ones(8) / 8, mode="same")
        add(0.06 * noise * (tp / max(tp[-1], 1e-3)) ** 2, int(r0 * sr))
        add(0.05 * np.sin(2*np.pi*(300 + 500*tp/ max(tp[-1],1e-3))*tp) * (tp / max(tp[-1],1e-3)) ** 2, int(r0 * sr))
        ln = int(1.2 * sr); tp = np.arange(ln) / sr
        add(0.35 * np.sin(2*np.pi*(70 - 25*tp)*tp) * np.exp(-tp * 4), int(cuts[2] * sr))
    # reverb + gentle lowpass
    wet = out.copy()
    for dl, g in [(0.113, 0.42), (0.197, 0.33), (0.291, 0.27), (0.43, 0.2)]:
        k = int(dl * sr)
        for _ in range(4):
            sh = np.zeros(n); sh[k:] = wet[:-k] * g
            wet += sh * 0.5
    mix = 0.62 * out + 0.38 * wet
    a = 0.18; y = np.zeros(n); acc = 0.0
    for idx in range(n):
        acc += a * (mix[idx] - acc); y[idx] = acc
    fade = np.minimum(1, t / 0.05) * np.minimum(1, (seconds - t) / 1.2)
    y *= fade
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.6
    st = np.stack([y, np.roll(y, int(0.012 * sr))], 1)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(sr)
        wf.writeframes((st * 32767).astype("<i2").tobytes())


# ---------------------------------------------------------------- reel
def render_reel(spec, out_dir):
    W, H, FPS = 1080, 1920, 30
    dur = float(spec["duration"])
    seed = spec.get("seed", zlib.crc32(spec["id"].encode()) & 0xFFFF)
    bw, bh = int(W * 1.12), int(H * 1.12)
    look = spec.get("look", "dark")
    set_theme(look)
    if look == "paper":
        bg = paper_bg(bw, bh, seed)
    else:
        bg = finish(scene(spec["scene"], bw, bh, seed), seed, darken_top=0.5)
    frames = spec["frames"]  # [{text, start, end, size}]
    text_layers = []
    reveal_layers = {}
    for fi, fr in enumerate(frames):
        if fr.get("reveal"):
            nwords = len(parse(fr["text"]))
            seq = []
            for k in range(1, nwords + 1):
                lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                draw_block(ImageDraw.Draw(lay), fr["text"], 90, fr.get("y", 520), W - 180 - 60, fr.get("size", 84), max_lines=6, upto=k)
                seq.append(lay)
            reveal_layers[fi] = seq
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        size = fr.get("size", 84)
        top = fr.get("y", 520)
        if fr.get("style") == "quote":
            d.text((80, top - 40), "\u201c", font=font(F_SERIF_I, 200), fill=AMBER)
            yb = draw_block(d, fr["text"], 90, top + 120, W - 180 - 40, fr.get("size", 76), fpath=F_SERIF_I, max_lines=6, lh=1.25)
        else:
            yb = draw_block(d, fr["text"], 90, top, W - 180 - 60, size, max_lines=6)
        if fr.get("sub"):
            draw_block(d, fr["sub"], 90, yb + 30, W - 180 - 60, 40, fpath=F_MED, color=MUTED, max_lines=2, lh=1.3)
        text_layers.append(layer)
    chrome = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    brand_marks(ImageDraw.Draw(chrome), W, H, spec.get("series"), top=230, handle_y=360)
    props = spec.get("props", [])
    passets = [prop_assets(pp, W) for pp in props]
    wav = os.path.join(out_dir, spec["id"] + ".wav")
    if len(frames) >= 3:
        score(wav, dur, seed, [f['start'] for f in frames])
    else:
        music(wav, dur, seed)
    mp4 = os.path.join(out_dir, spec["id"] + ".mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "19",
           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    total = int(dur * FPS)
    zdir = spec.get("motion", "in")
    for i in range(total):
        tt = i / FPS
        k = tt / dur
        z = 1.0 + 0.06 * (k if zdir != "out" else 1 - k)
        if tt < 0.4:
            z += 0.05 * (1 - tt / 0.4) ** 2
        cw, ch = W * 1.12 / z / 1.12 * 1.0, H / z
        cw = W / z * 1.0
        ox = (bw - cw) / 2 + (k - 0.5) * (40 if zdir == "pan" else 0)
        oy = (bh - ch) / 2
        frame = bg.crop((int(ox), int(oy), int(ox + cw), int(oy + ch))).resize((W, H), Image.BILINEAR).convert("RGBA")
        frame.alpha_composite(chrome)
        for pp, pa in zip(props, passets):
            pl = prop_layer(pp, W, H, tt, pa)
            if pl is not None:
                frame.alpha_composite(pl)
        for fi, (fr, layer) in enumerate(zip(frames, text_layers)):
            s, e = fr["start"], fr["end"]
            rv = fr.get("reveal_time", 1.0)
            if fi in reveal_layers and s <= tt < s + rv:
                seq = reveal_layers[fi]
                idx = min(len(seq) - 1, int((tt - s) / rv * len(seq)))
                frame.alpha_composite(seq[idx])
                continue
            fade = fr.get("fade", 0.45)
            if tt < s or tt > e:
                continue
            a = 1.0
            if s > 0 and tt < s + fade:
                a = (tt - s) / fade
            if e < dur and tt > e - fade:
                a = min(a, (e - tt) / fade)
            if a >= 0.999:
                frame.alpha_composite(layer)
            else:
                l2 = layer.copy(); l2.putalpha(l2.getchannel("A").point(lambda v: int(v * a)))
                frame.alpha_composite(l2)
        p.stdin.write(frame.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    # cover image (first frame text) for checks / thumbnails
    cover = bg.crop((int((bw - W) / 2), int((bh - H) / 2), int((bw + W) / 2), int((bh + H) / 2))).convert("RGBA")
    cover.alpha_composite(chrome)
    for pp, pa in zip(props, passets):
        pl = prop_layer(pp, W, H, min(frames[0]['end'] - 0.6, dur), pa)
        if pl is not None:
            cover.alpha_composite(pl)
    cover.alpha_composite(text_layers[0])
    cover.convert("RGB").save(os.path.join(out_dir, spec["id"] + "_cover.jpg"), quality=92)
    os.remove(wav)
    set_theme("dark")
    return mp4


# ---------------------------------------------------------------- carousel
def render_carousel(spec, out_dir):
    W, H = 1080, 1350
    seed0 = spec.get("seed", zlib.crc32(spec["id"].encode()) & 0xFFFF)
    slides = spec["slides"]
    n = len(slides)
    paths = []
    for i, s in enumerate(slides):
        seed = seed0 + i
        lk = s.get("look", spec.get("look", "dark"))
        set_theme(lk)
        if lk == "paper":
            bg = paper_bg(W, H, seed).convert("RGBA")
        else:
            bg = finish(scene(s.get("scene", spec.get("scene", "lamp")), W, H, seed), seed, darken_top=0.72).convert("RGBA")
        d = ImageDraw.Draw(bg)
        first, last = i == 0, i == n - 1
        brand_marks(d, W, H, spec.get("series") if first else None, top=90, show_handle=False)
        y = 300 if first else 260
        if s.get("kicker"):
            d.text((90, y), s["kicker"].upper(), font=font(F_BLACK, 28), fill=AMBER)
            y += 64
        size = s.get("size", 88 if first else 70)
        fpath = F_MONO if s.get("mono") else F_HEAD
        if s.get("mono"):
            size = s.get("size", 46)
        y = draw_block(d, s["text"], 90, y, W - 180, size, fpath=fpath, max_lines=7, lh=1.22 if not s.get("mono") else 1.35)
        if s.get("sub"):
            y += 28
            draw_block(d, s["sub"], 90, y, W - 180, 40, fpath=F_SERIF_I, color=MUTED, max_lines=4, lh=1.3)
        # footer
        d.text((90, H - 100), HANDLE, font=font(F_MED, 28), fill=MUTED)
        lab = f"{i + 1}/{n}"
        f = font(F_MED, 28)
        d.text((W - 90 - d.textlength(lab, font=f), H - 100), lab, font=f, fill=MUTED)
        if first:
            sw = "Swipe  →"
            d.text((W - 90 - d.textlength(sw, font=f), H - 160), sw, font=f, fill=AMBER)
        out = os.path.join(out_dir, f"{spec['id']}_{i + 1}.jpg")
        bg.convert("RGB").save(out, quality=92)
        paths.append(out)
    set_theme("dark")
    return paths


if __name__ == "__main__":
    kind, sp, od = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(od, exist_ok=True)
    spec = json.load(open(sp))
    items = spec if isinstance(spec, list) else [spec]
    for it in items:
        print(render_reel(it, od) if kind == "reel" else render_carousel(it, od))


# ---------------------------------------------------------------- story (1080x1920 still)
def render_story(spec, out_dir):
    W, H = 1080, 1920
    seed = spec.get("seed", zlib.crc32(spec["id"].encode()) & 0xFFFF)
    set_theme(spec.get("look"))
    if spec.get("look") == "paper":
        bg = paper_bg(W, H, seed).convert("RGBA")
    else:
        bg = finish(scene(spec.get("scene", "rain_window"), W, H, seed), seed, darken_top=0.6).convert("RGBA")
    d = ImageDraw.Draw(bg)
    brand_marks(d, W, H, spec.get("series"), top=260, show_handle=False)
    y = 560
    if spec.get("kicker"):
        d.text((90, y), spec["kicker"].upper(), font=font(F_BLACK, 34), fill=AMBER); y += 80
    y = draw_block(d, spec["text"], 90, y, W - 180, spec.get("size", 92), max_lines=7)
    if spec.get("sub"):
        draw_block(d, spec["sub"], 90, y + 40, W - 180, 46, fpath=F_SERIF_I, color=MUTED, max_lines=4, lh=1.3)
    d.text((90, 400 if spec.get("series") else 340), HANDLE, font=font(F_MED, 32), fill=MUTED)
    out = os.path.join(out_dir, spec["id"] + ".jpg")
    bg.convert("RGB").save(out, quality=92)
    set_theme("dark")
    return out
