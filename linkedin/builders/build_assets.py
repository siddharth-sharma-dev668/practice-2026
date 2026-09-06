"""
Build LinkedIn assets for Week 1: two 7-slide carousels (PNG + PDF),
two single-image posts, and one animated GIF.

Design rules applied (from linkedin/VISUAL_RESEARCH_AND_DRAFTS.md):
  - Cover carries typography, never a chart (axis labels die first at thumbnail size).
  - Every small-text / data slide uses a light background, dark ink (light mode holds
    up better than light-on-dark as text shrinks). Dark is reserved for large type.
  - Before/after = 2 bars, value printed on the bar, no axis at all.
  - X-of-N = filled/unfilled dot grid, not a bar chart.
  - Page counter on every slide starting at 1/N (goal-gradient effect).
  - Exactly one deliberate mid-thought pivot per deck, never per-slide.
  - <= ~50 words per slide, one idea each.

Everything is drawn at 2x and downsampled with LANCZOS, because Pillow does not
antialias shape primitives.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageColor

SS = 2                      # supersample factor
W, H = 1080, 1350           # LinkedIn native document ratio (4:5)
GW, GH = 1080, 1080         # square, for the GIF

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "assets")

FONTS = {
    "black": r"C:\Windows\Fonts\seguibl.ttf",
    "bold":  r"C:\Windows\Fonts\segoeuib.ttf",
    "semi":  r"C:\Windows\Fonts\seguisb.ttf",
    "reg":   r"C:\Windows\Fonts\segoeui.ttf",
    "ital":  r"C:\Windows\Fonts\segoeuii.ttf",
    "mono":  r"C:\Windows\Fonts\consola.ttf",
    "monob": r"C:\Windows\Fonts\consolab.ttf",
}
_fcache = {}


def font(kind, size):
    key = (kind, size)
    if key not in _fcache:
        _fcache[key] = ImageFont.truetype(FONTS[kind], int(size * SS))
    return _fcache[key]


# ---- palettes -------------------------------------------------------------
# Three interchangeable themes. Rotate every 3-4 posts so the feed does not
# look templated, but keep the structural signature (typographic covers, page
# counters, dot grids, the honest-gap closer) constant so posts stay his.
#
# In every theme: "dark" is used only for covers and the one pivot slide, where
# type is large. "light" carries every small-text slide. Accents on light are
# picked to clear WCAG AA (4.5:1) for normal text as a floor, not a target.
THEMES = {
    # slate + orange
    "signal": (
        dict(bg="#0F141A", ink="#FFFFFF", dim="#9FB0BF", acc="#FF9152",
             ok="#6ED69B", bad="#FF8073", line="#2B3642", card="#1B2530",
             fillbad="#2A1614", fillok="#0F2A1D"),
        dict(bg="#F7F9FA", ink="#10161C", dim="#52606D", acc="#B8481A",
             ok="#1B7F4F", bad="#B3261E", line="#CBD4DB", card="#EDF1F4",
             fillacc="#FFE2D2", fillok="#DFF3E8", codebg="#101820",
             barbase="#7A8794", barlift="#B8481A"),
    ),
    # deep navy + sky
    "blueprint": (
        dict(bg="#0A1622", ink="#FFFFFF", dim="#93AFC6", acc="#4FC3F7",
             ok="#6EE7B7", bad="#FF9A8B", line="#1F3A52", card="#142838",
             fillbad="#2B1518", fillok="#0C2A22"),
        dict(bg="#EDF4FA", ink="#0B1620", dim="#47606F", acc="#0D6E88",
             ok="#14714F", bad="#A8261E", line="#B6CCDE", card="#DCE9F3",
             fillacc="#C9E4F2", fillok="#D3EDE1", codebg="#0B1A26",
             barbase="#6E8296", barlift="#0D6E88"),
    ),
    # warm paper + amber
    "press": (
        dict(bg="#14110C", ink="#FFFFFF", dim="#B8AA96", acc="#F0B849",
             ok="#8DD6A0", bad="#FF9384", line="#352E22", card="#201B13",
             fillbad="#2C1512", fillok="#12261A"),
        dict(bg="#F9F1E2", ink="#14110C", dim="#5C5240", acc="#8A5406",
             ok="#1B6B45", bad="#A6291D", line="#D9C9AC", card="#F0E4CE",
             fillacc="#F7DCAE", fillok="#DCEBD6", codebg="#17130D",
             barbase="#8A8172", barlift="#8A5406"),
    ),
}
DARK, LIGHT = THEMES["signal"]


def use_theme(name):
    """Rebind the module palettes. Builders read DARK/LIGHT at call time."""
    global DARK, LIGHT
    DARK, LIGHT = THEMES[name]


class Slide:
    def __init__(self, bg, w=W, h=H):
        self.w, self.h = w, h
        if isinstance(bg, (tuple, list)):
            # vertical gradient between two colors, built row-by-row at 1x
            # then scaled up - cheap, and a gradient doesn't need supersampling
            c1, c2 = [ImageColor.getrgb(c) for c in bg]
            small = Image.new("RGB", (1, h))
            for y in range(h):
                t = y / max(h - 1, 1)
                small.putpixel((0, y), tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
            self.im = small.resize((w * SS, h * SS), Image.BILINEAR)
        else:
            self.im = Image.new("RGB", (w * SS, h * SS), bg)
        self.d = ImageDraw.Draw(self.im)

    # -- primitives (all args in final 1080-space; SS applied internally) --
    @staticmethod
    def _norm(s, kind):
        """Typographic cleanup. A spaced hyphen becomes an em dash in prose and
        a middot in mono eyebrows/labels; apostrophes curl in prose only, so
        quotes inside code fragments render exactly as typed."""
        if kind in ("mono", "monob"):
            return s.replace(" - ", " · ")
        return s.replace(" - ", " — ").replace("'", "’")

    def text(self, x, y, s, kind, size, fill, anchor="ls", track=0):
        s = self._norm(s, kind)
        f = font(kind, size)
        if track:
            cx = x * SS
            for ch in s:
                self.d.text((cx, y * SS), ch, font=f, fill=fill, anchor=anchor)
                cx += self.d.textlength(ch, font=f) + track * SS
        else:
            self.d.text((x * SS, y * SS), s, font=f, fill=fill, anchor=anchor)

    def lines(self, x, y, arr, kind, size, fill, lh, track=0, anchor="ls"):
        for i, t in enumerate(arr):
            self.text(x, y + i * lh, t, kind, size, fill, anchor=anchor, track=track)

    def rect(self, x, y, w, h, fill=None, outline=None, width=2, r=0, dash=None):
        box = [x * SS, y * SS, (x + w) * SS, (y + h) * SS]
        if r:
            self.d.rounded_rectangle(box, radius=r * SS, fill=fill,
                                     outline=outline if not dash else None,
                                     width=int(width * SS))
        else:
            self.d.rectangle(box, fill=fill,
                             outline=outline if not dash else None,
                             width=int(width * SS))
        if dash and outline:
            self._dashed_round(x, y, w, h, r, outline, width, dash)

    def _dashed_round(self, x, y, w, h, r, col, width, dash):
        on, off = dash
        per = on + off
        # top and bottom edges only - enough to read as "dashed/absent"
        for (yy, x0, x1) in ((y, x + r, x + w - r), (y + h, x + r, x + w - r)):
            cx = x0
            while cx < x1:
                self.d.line([cx * SS, yy * SS, min(cx + on, x1) * SS, yy * SS],
                            fill=col, width=int(width * SS))
                cx += per
        for (xx, y0, y1) in ((x, y + r, y + h - r), (x + w, y + r, y + h - r)):
            cy = y0
            while cy < y1:
                self.d.line([xx * SS, cy * SS, xx * SS, min(cy + on, y1) * SS],
                            fill=col, width=int(width * SS))
                cy += per

    def circle(self, cx, cy, rad, fill=None, outline=None, width=3, dash=None):
        box = [(cx - rad) * SS, (cy - rad) * SS, (cx + rad) * SS, (cy + rad) * SS]
        if dash and outline:
            steps = 40
            on, off = dash
            for i in range(steps):
                a0 = 2 * math.pi * i / steps
                if (i % 2) == 0:
                    self.d.arc(box, math.degrees(a0),
                               math.degrees(a0 + 2 * math.pi / steps),
                               fill=outline, width=int(width * SS))
        else:
            self.d.ellipse(box, fill=fill, outline=outline,
                           width=int(width * SS) if outline else 0)

    def line(self, x1, y1, x2, y2, col, width=3):
        self.d.line([x1 * SS, y1 * SS, x2 * SS, y2 * SS], fill=col,
                    width=int(width * SS))

    def arrow(self, x1, y1, x2, y2, col, width=5, head=17):
        ang = math.atan2(y2 - y1, x2 - x1)
        bx = x2 - math.cos(ang) * head * 0.85
        by = y2 - math.sin(ang) * head * 0.85
        self.line(x1, y1, bx, by, col, width)
        n = ang + math.pi / 2
        p = [(x2 * SS, y2 * SS),
             ((x2 - math.cos(ang) * head + math.cos(n) * head * 0.6) * SS,
              (y2 - math.sin(ang) * head + math.sin(n) * head * 0.6) * SS),
             ((x2 - math.cos(ang) * head - math.cos(n) * head * 0.6) * SS,
              (y2 - math.sin(ang) * head - math.sin(n) * head * 0.6) * SS)]
        self.d.polygon(p, fill=col)

    def check(self, cx, cy, size, col, width=6):
        """Drawn, not a glyph - no dependency on font coverage."""
        self.line(cx - size * .45, cy + size * .05, cx - size * .1, cy + size * .4, col, width)
        self.line(cx - size * .1, cy + size * .4, cx + size * .48, cy - size * .42, col, width)

    def cross(self, cx, cy, size, col, width=8):
        self.line(cx - size * .4, cy - size * .4, cx + size * .4, cy + size * .4, col, width)
        self.line(cx + size * .4, cy - size * .4, cx - size * .4, cy + size * .4, col, width)

    def tri_right(self, x, y, size, col):
        self.d.polygon([(x * SS, (y - size * .5) * SS),
                        (x * SS, (y + size * .5) * SS),
                        ((x + size * .8) * SS, y * SS)], fill=col)

    # -- composed furniture --
    def eyebrow(self, t, P):
        self.text(72, 104, t, "mono", 25, P["acc"], track=3)

    def counter(self, n, total, P):
        self.text(1008, 1288, f"{n}/{total}", "mono", 25, P["dim"], anchor="rs")

    def swipe(self, P):
        self.text(72, 1288, "swipe", "mono", 24, P["acc"])
        self.tri_right(168, 1280, 20, P["acc"])

    def rule(self, y, P, x=72, w=936, h=2):
        self.rect(x, y, w, h, fill=P["line"])

    def box(self, x, y, w, h, label, P, fill=None, txt=None, size=32, r=14,
            outline=None, dash=None, sub=None, subcol=None):
        self.rect(x, y, w, h, fill=fill or P["card"],
                  outline=outline or P["line"], width=2, r=r, dash=dash)
        ty = y + h / 2 + (0 if sub else 11)
        self.text(x + w / 2, ty, label, "bold", size, txt or P["ink"], anchor="ms")
        if sub:
            self.text(x + w / 2, y + h / 2 + 38, sub, "mono", 21,
                      subcol or P["dim"], anchor="ms")

    # -- glow / icon-badge system (infographic-style single images) --
    def glow(self, cx, cy, w, h, color, blur=16, alpha=150, r=26):
        """A soft blurred rounded-rect behind a badge. Paste order matters:
        call this BEFORE drawing the crisp badge on top of it."""
        pad = blur * 3
        lw, lh = int((w + pad * 2) * SS), int((h + pad * 2) * SS)
        layer = Image.new("RGBA", (lw, lh), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        rgb = ImageColor.getrgb(color)
        ld.rounded_rectangle([pad * SS, pad * SS, lw - pad * SS, lh - pad * SS],
                             radius=int(r * SS), fill=rgb + (alpha,))
        layer = layer.filter(ImageFilter.GaussianBlur(blur * SS / 2))
        px = int((cx - w / 2 - pad) * SS)
        py = int((cy - h / 2 - pad) * SS)
        self.im.paste(layer, (px, py), layer)

    def badge(self, cx, cy, size, icon_fn, label, col, P, glow_col=None):
        """Glowing rounded-square icon badge with a caption below - the unit
        Hritika's infographics repeat for producers/capabilities/consumers."""
        self.glow(cx, cy - 6, size * 0.85, size * 0.85, glow_col or col, blur=14, alpha=110)
        self.rect(cx - size / 2, cy - size / 2 - 6, size, size, fill=P["card"],
                  outline=col, width=2, r=16)
        icon_fn(cx, cy - 6, size * 0.42, col)
        if label:
            self.lines(cx, cy + size / 2 + 30, label if isinstance(label, list) else [label],
                       "bold", 22, P["ink"], 27, anchor="ms")

    def quote_box(self, x, y, w, h, lines_, P, accent=None):
        accent = accent or P["acc"]
        self.rect(x, y, w, h, fill=P["card"], outline=P["line"], width=2, r=16)
        self.text(x + 30, y + 56, "“", "black", 60, accent)
        self.lines(x + 70, y + 58, lines_, "bold", 27, P["ink"], 37)

    # -- icon glyphs, drawn (no font glyph coverage dependency) --
    def icon_bolt(self, cx, cy, s, col):
        pts = [(cx + s*.12, cy - s*.85), (cx - s*.55, cy + s*.1), (cx - s*.05, cy + s*.1),
               (cx - s*.22, cy + s*.85), (cx + s*.55, cy - s*.15), (cx + s*.05, cy - s*.15)]
        self.d.polygon([(px * SS, py * SS) for px, py in pts], fill=col)

    def icon_clock(self, cx, cy, s, col):
        self.circle(cx, cy, s, outline=col, width=int(s * .16))
        self.line(cx, cy, cx, cy - s * .55, col, int(s * .14))
        self.line(cx, cy, cx + s * .4, cy + s * .12, col, int(s * .14))

    def icon_chart(self, cx, cy, s, col):
        bw = s * .42
        for i, hh in enumerate([.6, 1.0, .78]):
            bx = cx - s * .8 + i * bw * 1.15
            self.rect(bx, cy + s * .8 - s * 1.6 * hh, bw * .8, s * 1.6 * hh, fill=col, r=4)

    def icon_lock(self, cx, cy, s, col):
        self.d.arc([(cx - s*.4) * SS, (cy - s*.9) * SS, (cx + s*.4) * SS, (cy + s*.1) * SS],
                   180, 360, fill=col, width=int(s * .16 * SS))
        self.rect(cx - s * .5, cy - s * .05, s, s * .85, fill=col, r=8)

    def icon_db(self, cx, cy, s, col):
        for dy in (-s * .5, 0, s * .5):
            self.d.ellipse([(cx - s*.55)*SS, (cy+dy-s*.18)*SS, (cx+s*.55)*SS, (cy+dy+s*.18)*SS],
                           outline=col, width=int(s * .1 * SS))
        self.line(cx - s * .55, cy - s * .5, cx - s * .55, cy + s * .5, col, int(s * .1))
        self.line(cx + s * .55, cy - s * .5, cx + s * .55, cy + s * .5, col, int(s * .1))

    def icon_code(self, cx, cy, s, col):
        self.d.polygon([((cx-s*.15)*SS,(cy-s*.7)*SS),((cx-s*.75)*SS,cy*SS),((cx-s*.15)*SS,(cy+s*.7)*SS)],
                       outline=col, width=int(s*.14*SS))
        self.d.line([((cx+s*.15)*SS,(cy-s*.7)*SS),((cx+s*.75)*SS,cy*SS),((cx+s*.15)*SS,(cy+s*.7)*SS)],
                    fill=col, width=int(s*.14*SS), joint="curve")

    def icon_warn(self, cx, cy, s, col):
        self.d.polygon([(cx*SS,(cy-s*.85)*SS), ((cx-s*.85)*SS,(cy+s*.65)*SS), ((cx+s*.85)*SS,(cy+s*.65)*SS)],
                       outline=col, width=int(s*.14*SS))
        self.line(cx, cy - s * .25, cx, cy + s * .18, col, int(s * .14))
        self.circle(cx, cy + s * .48, s * .06, fill=col)

    def finish(self):
        return self.im.resize((self.w, self.h), Image.LANCZOS)


# ==================== DECK A - the interview shift ========================
def deck_a():
    S, D, L = [], DARK, LIGHT

    # 1 cover - thesis stated with confidence, typography only, no personal score
    s = Slide(D["bg"]); s.eyebrow("HIRING TRENDS", D)
    s.lines(66, 440, ["Reading beats", "writing now."],
            "black", 108, D["ink"], 128, track=-4)
    s.rect(72, 700, 936, 3, fill=D["line"])
    s.lines(72, 800, ["The technical interview is quietly", "changing. Here's why it should."],
            "bold", 44, D["acc"], 56)
    s.swipe(D); s.counter(1, 6, D); S.append(s.finish())

    # 2 the shift - hedge visible on the slide itself
    s = Slide(L["bg"]); s.eyebrow("THE SHIFT", L)
    s.lines(72, 290, ["A few large companies are", "reportedly grading code",
                      "reading, not code writing."], "black", 54, L["ink"], 66, track=-1)
    s.rule(540, L)
    s.lines(72, 630, ["Reading and debugging an existing", "codebase, with an AI assistant",
                      "available - instead of writing", "from a blank file."],
            "reg", 36, L["dim"], 48)
    s.rect(72, 900, 936, 122, fill=L["card"], outline=L["line"], width=2, r=12)
    s.lines(102, 958, ["Per a few interview-prep sources I've read.",
                       "Not a round I've sat myself."], "ital", 29, L["dim"], 40)
    s.swipe(L); s.counter(2, 6, L); S.append(s.finish())

    # 3 why it holds up - two skills contrasted, no personal score anywhere
    s = Slide(L["bg"]); s.eyebrow("WHY IT HOLDS UP", L)
    s.text(72, 260, "Two different skills.", "black", 54, L["ink"], track=-1)
    s.rect(72, 340, 936, 300, fill=L["card"], outline=L["line"], width=2, r=14)
    s.text(104, 415, "WRITING FROM SCRATCH", "mono", 25, L["dim"], track=1)
    s.text(104, 470, "Rewards recall.", "bold", 38, L["ink"])
    s.text(104, 520, "Syntax, algorithms, a solution", "reg", 30, L["dim"])
    s.text(104, 558, "shape held in your head.", "reg", 30, L["dim"])
    s.rect(72, 660, 936, 300, fill=L["fillacc"], outline=L["acc"], width=2, r=14)
    s.text(104, 735, "READING + VERIFYING", "mono", 25, L["acc"], track=1)
    s.text(104, 790, "Rewards judgment.", "bold", 38, L["ink"])
    s.text(104, 840, "Holding someone else's logic fast", "reg", 30, L["ink"])
    s.text(104, 878, "enough to catch what's wrong.", "reg", 30, L["ink"])
    s.swipe(L); s.counter(3, 6, L); S.append(s.finish())

    # 4 the real reason - AI closes the writing gap, not the judgment gap
    s = Slide(D["bg"]); s.eyebrow("THE REAL REASON", D)
    s.lines(72, 300, ["An assistant can write", "a working function in", "seconds now."],
            "bold", 56, D["ink"], 70)
    s.rect(72, 610, 936, 3, fill=D["line"])
    s.lines(72, 720, ["It still can't tell you", "whether what it wrote", "is actually correct."],
            "black", 56, D["acc"], 70, track=-1)
    s.swipe(D); s.counter(4, 6, D); S.append(s.finish())

    # 5 what changes in prep - contrast, not confession
    s = Slide(L["bg"]); s.eyebrow("WHAT CHANGES IN PREP", L)
    s.text(72, 245, "Closer to the actual job.", "black", 48, L["ink"], track=-1)
    s.text(72, 340, "PR review. A diff. A service", "reg", 32, L["dim"])
    s.text(72, 378, "someone else wrote 6 months ago.", "reg", 32, L["dim"])
    s.rule(450, L)
    old = [("Fewer", "blank-file algorithm drills.")]
    new = [("More", "“find the bug in this file.”")]
    s.text(72, 560, "FEWER", "monob", 30, L["dim"])
    s.text(280, 560, "blank-file algorithm drills.", "reg", 34, L["ink"])
    s.text(72, 630, "MORE", "monob", 30, L["acc"])
    s.text(250, 630, "“find the bug in this file.”", "bold", 34, L["ink"])
    s.rect(72, 760, 936, 260, fill=L["card"], outline=L["line"], width=2, r=14)
    s.lines(104, 835, ["Writing-from-scratch was always", "a slightly artificial proxy for",
                       "what backend engineers actually do."], "reg", 32, L["dim"], 46)
    s.swipe(L); s.counter(5, 6, L); S.append(s.finish())

    # 6 close - the question, no personal score anywhere
    s = Slide(L["bg"]); s.eyebrow("YOUR TURN", L)
    s.lines(72, 300, ["I'd take this interview", "over the whiteboard",
                      "version any day."], "black", 54, L["ink"], 68, track=-1)
    s.lines(72, 540, ["Not because it's easier.", "Because it's closer to", "the real job."],
            "bold", 40, L["acc"], 52)
    s.rect(72, 780, 936, 240, fill=L["card"], outline=L["acc"], width=3, r=14)
    s.lines(104, 850, ["Have you sat a comprehension-", "style round? What did it feel",
                       "like against the classic algorithm", "interview?"],
            "bold", 33, L["ink"], 44)
    s.counter(6, 6, L); S.append(s.finish())
    return S


# ======================= DECK B - cache-aside / p95 =======================
def deck_b():
    S, D, L = [], DARK, LIGHT

    # 1 cover
    s = Slide(D["bg"]); s.eyebrow("A NUMBER I ACTUALLY MEASURED", D)
    s.text(66, 470, "~20%", "black", 290, D["ink"], track=-16)
    s.rect(72, 560, 936, 3, fill=D["line"])
    s.text(72, 670, "faster p95 from one cache.", "bold", 60, D["acc"])
    s.lines(72, 820, ["The pattern - and the one", "failure mode I still",
                      "haven't tested."], "reg", 42, D["dim"], 54)
    s.swipe(D); s.counter(1, 7, D); S.append(s.finish())

    # 2 context + what p95 means (the explainer Sid asked for)
    s = Slide(L["bg"]); s.eyebrow("CONTEXT", L)
    s.lines(72, 270, ["A system moving 10M+", "messages a month."],
            "black", 54, L["ink"], 66, track=-1)
    s.lines(72, 440, ["Every millisecond on the read", "path multiplies."],
            "reg", 36, L["dim"], 46)
    s.rule(580, L)
    s.text(72, 670, "WHAT p95 MEANS", "mono", 27, L["acc"], track=2)
    s.lines(72, 750, ["The response time that 95%", "of requests come in under."],
            "bold", 42, L["ink"], 54)
    s.lines(72, 900, ["Not the average. Averages hide", "the worst realistic case - p95 is",
                      "closer to what your slowest", "real users actually feel."],
            "reg", 34, L["dim"], 44)
    s.swipe(L); s.counter(2, 7, L); S.append(s.finish())

    # 3 the pattern - flow diagram carries it.
    # One downward column = the miss path; the single right branch = the hit path.
    s = Slide(L["bg"]); s.eyebrow("THE PATTERN - CACHE-ASIDE", L)
    s.box(330, 240, 420, 105, "Request", L)
    s.arrow(540, 345, 540, 425, L["ink"])
    s.box(330, 432, 420, 105, "Redis", L, fill=L["fillacc"])
    # hit: branch right and stop
    s.arrow(750, 484, 838, 484, L["ok"])
    s.text(852, 476, "HIT", "monob", 27, L["ok"])
    s.text(852, 512, "return", "reg", 25, L["dim"])
    # miss: keep going down
    s.arrow(540, 537, 540, 617, L["bad"])
    s.text(566, 588, "MISS", "monob", 27, L["bad"])
    s.box(330, 624, 420, 105, "Postgres", L)
    s.arrow(540, 729, 540, 809, L["ok"])
    s.box(330, 816, 420, 105, "write back to Redis", L, fill=L["fillok"], size=29)
    s.rule(990, L)
    s.lines(72, 1060, ["Hit? Skip the database entirely.", "Miss? Pay once, then cache it."],
            "bold", 38, L["ink"], 50)
    s.swipe(L); s.counter(3, 7, L); S.append(s.finish())

    # 4 result - 2 bars, values ON the bars, no axis
    s = Slide(L["bg"]); s.eyebrow("THE RESULT", L)
    s.text(72, 265, "p95 on that endpoint", "black", 54, L["ink"], track=-1)
    s.text(72, 400, "BEFORE", "mono", 28, L["dim"], track=2)
    s.rect(72, 425, 936, 130, fill=L["barbase"], r=12)
    s.text(110, 510, "baseline", "black", 56, "#FFFFFF")
    s.text(72, 660, "AFTER - REDIS CACHE-ASIDE", "mono", 28, L["dim"], track=2)
    s.rect(72, 685, 749, 130, fill=L["barlift"], r=12)
    s.text(110, 770, "~20% lower", "black", 56, "#FFFFFF")
    s.rule(925, L)
    s.lines(72, 1010, ["One hot read endpoint was hitting", "Postgres directly - for data that",
                       "barely changed request to request."], "reg", 36, L["dim"], 46)
    s.swipe(L); s.counter(4, 7, L); S.append(s.finish())

    # 5 the turn - the single deliberate mid-thought pivot in this deck
    s = Slide(D["bg"]); s.eyebrow("BUT", D)
    s.lines(72, 480, ["Cache-aside", "doesn't protect", "you from this."],
            "black", 84, D["ink"], 102, track=-3)
    s.text(72, 900, "One expiring key. Same second.", "reg", 46, D["acc"])
    s.swipe(D); s.counter(5, 7, D); S.append(s.finish())

    # 6 the stampede
    s = Slide(L["bg"]); s.eyebrow("CACHE STAMPEDE", L)
    s.box(340, 235, 400, 105, "hot key expires", L, fill=L["fillacc"],
          txt=L["bad"], size=32)
    s.arrow(540, 342, 540, 424, L["dim"], 4)
    s.text(72, 480, "500 REQUESTS, ALL MISS", "mono", 27, L["dim"], track=2)
    for i in range(9):
        s.rect(88 + i * 104, 520, 76, 76, fill=L["bad"], r=10)
        s.arrow(126 + i * 104, 602, 126 + i * 104, 686, L["bad"], 4, 13)
    s.box(240, 690, 600, 115, "Postgres - all at once", L, size=34)
    s.rule(890, L)
    s.text(72, 975, "No fix tested yet.", "bold", 40, L["acc"])
    s.lines(72, 1060, ["TTL jitter and request coalescing are",
                       "the two I'd want to measure first."], "reg", 34, L["dim"], 44)
    s.swipe(L); s.counter(6, 7, L); S.append(s.finish())

    # 7 close
    s = Slide(L["bg"]); s.eyebrow("WHERE I ACTUALLY AM", L)
    s.text(72, 275, "The 20% is real.", "black", 52, L["ink"], track=-1)
    s.lines(72, 400, ["The stampede question", "isn't answered yet."],
            "black", 52, L["acc"], 66, track=-1)
    s.rule(540, L)
    s.lines(72, 630, ["I'd rather post it that way than",
                      "pretend the second part is solved."], "reg", 36, L["dim"], 46)
    s.rect(72, 820, 936, 240, fill=L["card"], outline=L["acc"], width=3, r=14)
    s.lines(104, 890, ["If you've hit cache stampede in", "production - jitter, locking,",
                       "request coalescing, or something", "else? What actually worked?"],
            "bold", 35, L["ink"], 46)
    s.counter(7, 7, L); S.append(s.finish())
    return S


# =================== DECK C - MCP's default token cost ====================
def deck_c():
    S, D, L = [], DARK, LIGHT

    # 1 cover - thesis, typography only
    s = Slide(D["bg"]); s.eyebrow("AGENT TOOLING", D)
    s.lines(66, 400, ["MCP's default costs", "10-30x more than", "it needs to."],
            "black", 92, D["ink"], 108, track=-3)
    s.rect(72, 830, 936, 3, fill=D["line"])
    s.lines(72, 920, ["Two independent sources landed on", "the same number this year."],
            "reg", 38, D["dim"], 48)
    s.swipe(D); s.counter(1, 6, D); S.append(s.finish())

    # 2 Anthropic's own finding
    s = Slide(L["bg"]); s.eyebrow("THE FIRST SOURCE", L)
    s.lines(72, 260, ["Anthropic's own engineering", "team found this."],
            "black", 50, L["ink"], 62, track=-1)
    s.rule(460, L)
    s.text(72, 560, "150,000 → 2,000 tokens.", "black", 62, L["acc"], track=-2)
    s.text(72, 630, "98.7% cut, one real example.", "bold", 34, L["ink"])
    s.lines(72, 760, ["The fix: have the agent write code", "against MCP servers exposed as a",
                      "filesystem, instead of loading every", "tool schema and result through itself."],
            "reg", 34, L["dim"], 46)
    s.swipe(L); s.counter(2, 6, L); S.append(s.finish())

    # 3 independent benchmark corroborates - tokens, 2 bars no axis
    s = Slide(L["bg"]); s.eyebrow("THE SECOND SOURCE", L)
    s.lines(72, 245, ["A third party benchmarked it", "independently. Same result."],
            "black", 44, L["ink"], 54, track=-1)
    s.text(72, 400, "CLI, PER TASK", "mono", 27, L["dim"], track=2)
    s.rect(72, 425, 320, 100, fill=L["barbase"], r=12)
    s.text(96, 490, "1.3k-9.4k", "bold", 38, "#FFFFFF")
    s.text(72, 600, "MCP, PER TASK", "mono", 27, L["dim"], track=2)
    s.rect(72, 625, 936, 100, fill=L["barlift"], r=12)
    s.text(96, 690, "32k-82k tokens", "bold", 38, "#FFFFFF")
    s.rule(790, L)
    s.text(72, 870, "~$3.20/mo → ~$55.20/mo", "black", 42, L["ink"], track=-1)
    s.text(72, 925, "projected cost, 10k ops/month.", "reg", 30, L["dim"])
    s.swipe(L); s.counter(3, 6, L); S.append(s.finish())

    # 4 same benchmark - reliability, dot grid on real data
    s = Slide(L["bg"]); s.eyebrow("THE SAME BENCHMARK", L)
    s.text(72, 255, "Reliability took a hit too.", "black", 48, L["ink"], track=-1)
    for i in range(10):
        cx = 132 + i * 91
        if i < 7:
            s.circle(cx, 420, 38, fill=L["ok"])
        else:
            s.circle(cx, 420, 38, outline=L["bad"], width=6, dash=(10, 8))
    s.text(72, 520, "MCP: 72% success - TCP timeouts.", "bold", 32, L["bad"])
    for i in range(10):
        cx = 132 + i * 91
        s.circle(cx, 660, 38, fill=L["ok"])
    s.text(72, 760, "CLI: 100% success.", "bold", 32, L["ok"])
    s.rule(870, L)
    s.lines(72, 950, ["Same 5 real GitHub tasks,", "same agent, same model."],
            "reg", 32, L["dim"], 42)
    s.swipe(L); s.counter(4, 6, L); S.append(s.finish())

    # 5 why - the mechanism, dark pivot
    s = Slide(D["bg"]); s.eyebrow("WHY THIS HAPPENS", D)
    s.lines(72, 300, ["Every call injects the full", "tool schema list - whether", "the task needs it or not."],
            "bold", 48, D["ink"], 60)
    s.rect(72, 590, 936, 3, fill=D["line"])
    s.lines(72, 700, ["Every intermediate result", "routes back through the", "model instead of being",
                      "handled directly."], "black", 48, D["acc"], 60, track=-1)
    s.swipe(D); s.counter(5, 6, D); S.append(s.finish())

    # 6 close - his take + question, no overclaimed authority
    s = Slide(L["bg"]); s.eyebrow("MY TAKE", L)
    s.lines(72, 280, ["I've spent time this year", "evaluating MCP-based tooling", "at work."],
            "black", 48, L["ink"], 60, track=-1)
    s.rule(500, L)
    s.lines(72, 590, ["The protocol isn't the problem.", "Eager-loading everything by",
                      "default is."], "bold", 40, L["acc"], 52)
    s.rect(72, 780, 936, 240, fill=L["card"], outline=L["acc"], width=3, r=14)
    s.lines(104, 850, ["If you're running MCP in prod -", "loading full schemas every call,",
                       "or lazy-loading? What did the", "eager version cost you?"],
            "bold", 33, L["ink"], 44)
    s.counter(6, 6, L); S.append(s.finish())
    return S


# ================ DECK D - Postgres isn't slow, storage is ================
# First carousel built with the glow/icon toolkit instead of flat boxes -
# a real flow diagram (write -> WAL -> fsync, forking at the storage layer)
# replaces the old text-only "the pattern" slides.
def deck_d():
    S, D, L = [], DARK, LIGHT

    # 1 cover - thesis, gradient + glow already reads like the reference bar
    s = Slide(("#0A0E14", "#161F2A"), W, H)
    s.eyebrow("DATABASE INTERNALS", D)
    s.lines(60, 340, ["Postgres isn't slow.", "Your storage is."],
            "black", 82, D["ink"], 96, track=-3)
    s.rect(60, 560, 960, 3, fill=D["line"])
    s.lines(60, 650, ["Most 'Postgres is slow' complaints", "trace back to one layer nobody blames."],
            "reg", 34, D["dim"], 46)
    s.swipe(D); s.counter(1, 7, D); S.append(s.finish())

    # 2 the claim, sourced
    s = Slide(L["bg"]); s.eyebrow("THE SOURCE", L)
    s.lines(60, 260, ["A POSETTE 2026 talk made", "the case directly."],
            "black", 48, L["ink"], 60, track=-1)
    s.rule(460, L)
    s.lines(60, 550, ["P95 spikes. Autovacuum falling behind.", "Checkpoint stalls. Replication lag.",
                      "The usual complaint list -", "mostly one layer underneath it all."],
            "reg", 36, L["dim"], 48)
    s.rect(60, 850, 960, 130, fill=L["card"], outline=L["line"], width=2, r=16)
    s.text(90, 900, "Sai Srirampur, POSETTE 2026", "bold", 30, L["ink"])
    s.text(90, 945, "recapped by ClickHouse, 1 Sep 2026", "reg", 26, L["dim"])
    s.swipe(L); s.counter(2, 7, L); S.append(s.finish())

    # 3 the flow diagram - same write path, forking at the storage layer
    s = Slide(("#0A0E14", "#161F2A"), W, H)
    s.eyebrow("THE SAME WRITE, TWO STORAGE LAYERS", D)
    s.badge(190, 280, 120, s.icon_code, ["Write", "issued"], D["ink"], D)
    s.arrow(190, 350, 190, 410, D["dim"], 4, 14)
    s.badge(190, 480, 120, s.icon_db, ["WAL", "fsync"], D["ink"], D)
    s.arrow(230, 500, 380, 380, D["bad"], 4, 14)
    s.arrow(230, 560, 380, 680, D["ok"], 4, 14)

    s.rect(400, 240, 620, 260, fill="#241318", outline=D["bad"], width=2, r=20)
    s.text(430, 300, "NETWORK BLOCK STORAGE", "monob", 24, D["bad"], track=1)
    s.badge(560, 400, 90, s.icon_clock, ["fsync", "latency"], D["bad"], D)
    s.badge(760, 400, 90, s.icon_warn, ["Checkpoint", "stalls"], D["bad"], D)

    s.rect(400, 560, 620, 260, fill="#0F241C", outline=D["ok"], width=2, r=20)
    s.text(430, 620, "LOCAL NVMe", "monob", 24, D["ok"], track=1)
    s.badge(560, 720, 90, s.icon_bolt, ["Overhead", "disappears"], D["ok"], D)
    s.badge(760, 720, 90, s.icon_chart, ["Scales", "linearly"], D["ok"], D)

    s.text(60, 900, "Same workload. Same query. Different floor under it.", "reg", 32, D["dim"])
    s.swipe(D); s.counter(3, 7, D); S.append(s.finish())

    # 4 what changes at each layer - two-column, matches the token-cost deck
    colY = 260; colH = 380
    s = Slide(L["bg"]); s.eyebrow("WHAT ACTUALLY HAPPENS", L)
    s.rect(60, colY, 450, colH, fill="#241318", outline=L["bad"], width=2, r=20)
    s.text(90, colY + 60, "NETWORK STORAGE", "monob", 23, L["bad"], track=1)
    s.text(90, colY + 140, "WAL fsync", "bold", 32, "#FFFFFF")
    s.text(90, colY + 185, "waits on a network round trip", "reg", 24, "#D8C4C4")
    s.rect(90, colY + 230, 390, 1, fill="#4A2E33")
    s.text(90, colY + 280, "Checkpoint stalls", "bold", 28, "#FFFFFF")
    s.text(90, colY + 320, "under sustained write pressure", "reg", 24, "#D8C4C4")

    rx = 570
    s.rect(rx, colY, 450, colH, fill="#0F241C", outline=L["ok"], width=2, r=20)
    s.text(rx + 30, colY + 60, "LOCAL NVMe", "monob", 23, L["ok"], track=1)
    s.text(rx + 30, colY + 140, "WAL fsync", "bold", 32, "#FFFFFF")
    s.text(rx + 30, colY + 185, "resolves at local disk speed", "reg", 24, "#C4D8CC")
    s.rect(rx + 30, colY + 230, 390, 1, fill="#2E4A3A")
    s.text(rx + 30, colY + 280, "OLTP latency", "bold", 28, "#FFFFFF")
    s.text(rx + 30, colY + 320, "stays flat under the same load", "reg", 24, "#C4D8CC")
    s.arrow(510, colY + colH / 2 - 10, 565, colY + colH / 2 - 10, L["dim"], 5, 16)

    s.rule(colY + colH + 60, L)
    s.lines(60, colY + colH + 130, ["That reframes the debugging question:",
                                     "not 'why is Postgres slow,' but", "'what's under my WAL writes.'"],
            "bold", 34, L["ink"], 46)
    s.swipe(L); s.counter(4, 7, L); S.append(s.finish())

    # 5 the honest gap - hasn't run this himself
    s = Slide(D["bg"]); s.eyebrow("THE HONEST GAP", D)
    s.lines(60, 300, ["I haven't run this", "comparison myself."],
            "black", 58, D["ink"], 70, track=-2)
    s.rect(60, 520, 960, 3, fill=D["line"])
    s.lines(60, 610, ["No local-NVMe box to test against", "a managed network-storage instance",
                      "side by side."], "reg", 36, D["dim"], 48)
    s.lines(60, 800, ["But fsync and checkpoint I/O are", "exactly the operations most sensitive",
                      "to storage latency - the mechanism", "holds without needing to re-run it."],
            "bold", 34, D["acc"], 46)
    s.swipe(D); s.counter(5, 7, D); S.append(s.finish())

    # 6 sources / who this is for
    s = Slide(L["bg"]); s.eyebrow("WHO THIS CHANGES THINGS FOR", L)
    s.text(60, 255, "Anyone debugging Postgres", "black", 44, L["ink"], track=-1)
    s.text(60, 305, "on managed cloud storage.", "black", 44, L["ink"], track=-1)
    causes = [(s.icon_db, ["Cloud-managed", "Postgres, default"]),
              (s.icon_warn, ["Checkpoint tuning", "before storage swap"]),
              (s.icon_chart, ["Benchmarking the", "wrong layer"])]
    for i, (fn, lbl) in enumerate(causes):
        cx = 190 + i * 350
        s.badge(cx, 480, 120, fn, lbl, L["acc"], L, glow_col=L["acc"])
    s.rule(660, L)
    s.lines(60, 740, ["Most teams tune Postgres knobs", "before ever checking what's",
                      "underneath the WAL."], "reg", 34, L["dim"], 46)
    s.swipe(L); s.counter(6, 7, L); S.append(s.finish())

    # 7 close - question
    s = Slide(L["bg"]); s.eyebrow("YOUR TURN", L)
    s.lines(60, 280, ["If you've moved a Postgres", "workload between storage",
                      "layers -"], "black", 48, L["ink"], 60, track=-1)
    s.rule(500, L)
    s.lines(60, 590, ["What actually changed,", "and was it what you expected?"],
            "bold", 40, L["acc"], 52)
    s.rect(60, 780, 960, 200, fill=L["card"], outline=L["acc"], width=3, r=14)
    s.lines(92, 850, ["Network block storage vs. local NVMe -", "same workload, different floor."],
            "bold", 33, L["ink"], 44)
    s.counter(7, 7, L); S.append(s.finish())
    return S


# ================= INFOGRAPHIC - MCP token cost, single image =============
# Matches the reference bar we're building to: one dense poster (gradient
# ground, glowing icon badges, side stat columns, a pull-quote) instead of
# a swipeable multi-slide deck.
IW, IH = 1080, 1850


def infographic_mcp():
    D = DARK
    s = Slide(("#0A0E14", "#161F2A"), IW, IH)

    s.text(60, 100, "AGENT TOOLING - COST", "mono", 26, D["acc"], track=3)
    s.lines(60, 200, ["MCP's default costs", "10-30x more than it needs to."],
            "black", 62, D["ink"], 74, track=-2)
    s.text(60, 350, "Two independent sources found the exact same thing.", "reg", 30, D["dim"])

    # -- row: why it happens, 3 icon badges --
    s.text(60, 430, "WHY IT HAPPENS", "mono", 24, D["dim"], track=2)
    causes = [(s.icon_code, ["Full schema,", "every call"]),
              (s.icon_bolt, ["Every result", "round-trips back"]),
              (s.icon_clock, ["Nothing is", "lazy-loaded"])]
    for i, (fn, lbl) in enumerate(causes):
        cx = 190 + i * 350
        s.badge(cx, 540, 130, fn, lbl, D["acc"], D)

    # -- two-column comparison: eager (default) vs lazy (fix) --
    colY = 730
    colH = 430
    # left: eager / default - red-tinted
    s.rect(60, colY, 450, colH, fill="#241318", outline=D["bad"], width=2, r=20)
    s.text(60 + 30, colY + 60, "EAGER - DEFAULT", "monob", 25, D["bad"], track=1)
    s.text(60 + 30, colY + 140, "150,000 tokens", "bold", 36, D["ink"])
    s.text(60 + 30, colY + 195, "one real example", "reg", 24, D["dim"])
    s.rule(colY + 230, D, x=60 + 30, w=390, h=1)
    s.text(60 + 30, colY + 280, "32k-82k / task", "bold", 32, D["ink"])
    s.text(60 + 30, colY + 330, "72% success - TCP timeouts", "reg", 24, D["bad"])
    s.text(60 + 30, colY + 390, "~$55.20/mo, 10k ops", "bold", 28, D["ink"])

    # right: lazy / fix - green-tinted
    rx = 570
    s.rect(rx, colY, 450, colH, fill="#0F241C", outline=D["ok"], width=2, r=20)
    s.text(rx + 30, colY + 60, "LAZY - THE FIX", "monob", 25, D["ok"], track=1)
    s.text(rx + 30, colY + 140, "2,000 tokens", "bold", 36, D["ink"])
    s.text(rx + 30, colY + 195, "98.7% cut, same task", "reg", 24, D["dim"])
    s.rule(colY + 230, D, x=rx + 30, w=390, h=1)
    s.text(rx + 30, colY + 280, "1.3k-9.4k / task", "bold", 32, D["ink"])
    s.text(rx + 30, colY + 330, "100% success", "reg", 24, D["ok"])
    s.text(rx + 30, colY + 390, "~$3.20/mo, 10k ops", "bold", 28, D["ink"])

    # arrow between columns
    s.arrow(510, colY + colH / 2 - 10, 565, colY + colH / 2 - 10, D["dim"], 5, 16)

    # -- quote, full width so long lines never clip the canvas edge --
    qy = colY + colH + 60
    s.quote_box(60, qy, 960, 190,
                ["The protocol isn't the problem.", "Loading everything eagerly,",
                 "by default, is."], D)

    # -- sources row --
    sy = qy + 190 + 70
    s.text(60, sy, "SOURCES", "mono", 24, D["dim"], track=2)
    srcs = [(s.icon_db, ["Anthropic's own", "engineering blog"]),
            (s.icon_chart, ["Scalekit benchmark,", "5 real GitHub tasks"])]
    for i, (fn, lbl) in enumerate(srcs):
        cx = 190 + i * 350
        s.badge(cx, sy + 130, 120, fn, lbl, D["ink"], D, glow_col=D["acc"])

    s.text(60, sy + 280, "Evaluated MCP-based tooling at work this year.",
           "ital", 24, D["dim"])
    return s.finish()


# ============================== SINGLES ==================================
def singles():
    out, D, L = {}, DARK, LIGHT

    # MCP stateful -> stateless, one image
    s = Slide(D["bg"]); s.eyebrow("MCP SPEC - 28 JULY 2026", D)
    s.text(72, 250, "STATEFUL", "black", 86, D["dim"], track=-3)
    s.line(66, 222, 636, 222, D["bad"], 9)          # struck through
    s.text(72, 370, "STATELESS.", "black", 96, D["acc"], track=-4)
    s.rect(72, 440, 936, 3, fill=D["line"])

    s.text(72, 530, "BEFORE - SESSION IN SERVER MEMORY", "mono", 26, D["dim"], track=2)
    s.box(72, 560, 230, 96, "Client", D)
    s.arrow(302, 608, 464, 608, D["dim"])
    s.text(386, 588, "session", "mono", 21, D["dim"], anchor="ms")
    s.box(470, 560, 230, 96, "Server A", D)
    s.box(748, 560, 230, 96, "Server B", D, fill=D["fillbad"], txt=D["bad"],
          size=28, outline=D["bad"], dash=(9, 7), sub="no session",
          subcol=D["bad"])

    s.text(72, 770, "AFTER - CONTEXT TRAVELS WITH THE REQUEST", "mono", 26,
           D["acc"], track=2)
    s.box(72, 800, 230, 96, "Client", D)
    s.arrow(302, 848, 464, 848, D["acc"])
    s.box(470, 800, 230, 96, "Balancer", D, size=27)
    s.arrow(702, 830, 786, 784, D["ok"])
    s.arrow(702, 866, 786, 912, D["ok"])
    for yy, lbl in ((736, "A"), (878, "B")):
        s.rect(790, yy, 196, 82, fill=D["fillok"], outline=D["ok"], width=2, r=12)
        s.text(862, yy + 52, lbl, "bold", 30, D["ok"], anchor="ms")
        s.check(922, yy + 41, 34, D["ok"], 5)
    s.rect(72, 1030, 936, 3, fill=D["line"])
    s.lines(72, 1120, ["Any instance answers any request.",
                       "The same trade REST already made."], "bold", 44, D["ink"], 56)
    out["mcp-architecture"] = s.finish()

    # cache-aside code reference card
    s = Slide(L["bg"]); s.eyebrow("CACHE-ASIDE, IN 6 LINES", L)
    s.lines(72, 265, ["The pattern that cut", "our p95 by ~20%."],
            "black", 58, L["ink"], 72, track=-2)
    s.rect(72, 400, 936, 470, fill=L["codebg"], outline=L["line"], width=2, r=16)
    code = ["val = redis.get(key)", "", "if val is None:",
            "    val = db.query(key)", "    redis.setex(key, ttl, val)", "", "return val"]
    for i, ln in enumerate(code):
        s.text(112, 475 + i * 58, ln, "mono", 37, "#E6EBEF")
    s.text(72, 960, "Simple to describe.", "bold", 38, L["acc"])
    s.text(72, 1015, "Easy to get wrong in one specific way:", "bold", 38, L["ink"])
    s.lines(72, 1085, ["what happens when a hot key expires",
                       "and 500 requests land in one second?"], "reg", 34, L["dim"], 44)
    out["cache-aside-code"] = s.finish()
    out["mcp-token-cost-infographic"] = infographic_mcp()
    return out


# ============================== BANNER ====================================
# LinkedIn cover photo, 1584x396 (4:1). The profile photo overlaps roughly the
# bottom-left ~430px as a circle, so keep that corner clear and put the
# tagline where it reads clean regardless of theme - top area, right-weighted,
# matching the "dark ground, one confident line, small flourish" shape that
# reads as designed rather than default.
BW, BH = 1584, 396


def banner(tagline, sub=None):
    D = DARK
    s = Slide(D["bg"], BW, BH)
    s.text(BW - 60, 90, tagline, "black", 52, D["ink"], anchor="rs")
    tw = s.d.textlength(tagline, font=font("black", 52)) / SS
    s.line(BW - 60 - tw, 135, BW - 60, 135, D["acc"], 4)
    if sub:
        s.text(BW - 60, 180, sub, "reg", 24, D["dim"], anchor="rs")
    return s.finish()


# ============================== GIF ======================================
def gif_frames():
    D = DARK
    F = []

    def frame():
        return Slide(D["bg"], GW, GH)

    def foot(s, t, col=None):
        s.text(70, 1010, t, "mono", 25, col or D["dim"], track=1)

    # 1 title
    s = frame()
    s.text(70, 300, "MCP just went", "black", 84, D["ink"], track=-2)
    s.text(70, 400, "stateless.", "black", 84, D["acc"], track=-2)
    s.rect(70, 450, 940, 3, fill=D["line"])
    s.lines(70, 530, ["If you've scaled a REST API behind",
                      "a load balancer, you already know",
                      "why that matters."], "reg", 38, D["dim"], 48)
    foot(s, "SPEC UPDATE - 28 JULY 2026", D["acc"]); F.append(s.finish())

    # 2 before
    s = frame()
    s.text(70, 150, "Before", "black", 60, D["dim"], track=-1)
    s.box(70, 500, 250, 110, "Client", D)
    s.arrow(320, 555, 494, 555, D["dim"])
    s.text(410, 530, "session", "mono", 22, D["dim"], anchor="ms")
    s.box(500, 500, 250, 110, "Server A", D)
    foot(s, "ONE INSTANCE. SESSION LIVES IN ITS MEMORY."); F.append(s.finish())

    # 3 add a second instance
    s = frame()
    s.text(70, 150, "Now add a second instance", "black", 54, D["dim"], track=-1)
    s.box(70, 420, 230, 105, "Client", D)
    s.arrow(300, 472, 464, 472, D["dim"])
    s.box(470, 420, 230, 105, "Server A", D, outline=D["ok"], sub="has session",
          subcol=D["ok"])
    s.box(470, 610, 230, 105, "Server B", D, fill=D["fillbad"], txt=D["bad"],
          outline=D["bad"], dash=(9, 7), sub="no session", subcol=D["bad"])
    foot(s, "THE SESSION ONLY EXISTS ON A."); F.append(s.finish())

    # 4 request lands on B -> breaks
    s = frame()
    s.text(70, 150, "Request lands on B", "black", 58, D["bad"], track=-1)
    s.box(70, 420, 230, 105, "Client", D)
    s.arrow(300, 540, 464, 655, D["bad"])
    s.box(470, 420, 230, 105, "Server A", D, outline=D["ok"], sub="has session",
          subcol=D["ok"])
    s.box(470, 610, 230, 105, "Server B", D, fill=D["fillbad"], txt=D["bad"],
          outline=D["bad"], dash=(9, 7), sub="no session", subcol=D["bad"])
    s.cross(810, 662, 90, D["bad"], 10)
    foot(s, "STICKY SESSIONS, OR IT BREAKS.", D["bad"]); F.append(s.finish())

    # 5 the change
    s = frame()
    s.text(70, 150, "The spec change", "black", 54, D["dim"], track=-1)
    s.text(70, 300, "Stateless", "black", 80, D["acc"], track=-3)
    s.text(70, 395, "per request.", "black", 80, D["acc"], track=-3)
    s.rect(70, 460, 940, 3, fill=D["line"])
    s.lines(70, 540, ["No session handshake.", "Cacheable list results.",
                      "Header-based routing.", "Multi-round-trip, natively."],
            "reg", 35, D["dim"], 52)
    foot(s, "CONTEXT TRAVELS WITH EVERY REQUEST", D["acc"]); F.append(s.finish())

    # 6 after
    s = frame()
    s.text(70, 150, "After", "black", 60, D["acc"], track=-1)
    s.box(70, 470, 215, 105, "Client", D)
    s.arrow(285, 522, 434, 522, D["acc"])
    s.box(440, 470, 215, 105, "Balancer", D, size=29)
    s.arrow(655, 500, 794, 425, D["ok"])
    s.arrow(655, 545, 794, 620, D["ok"])
    for yy, lbl in ((365, "Server A"), (575, "Server B")):
        s.rect(800, yy, 200, 105, fill=D["fillok"], outline=D["ok"], width=3, r=14)
        s.text(880, yy + 52, lbl, "bold", 28, D["ok"], anchor="ms")
        s.check(956, yy + 44, 34, D["ok"], 5)
    foot(s, "ANY INSTANCE ANSWERS ANY REQUEST.", D["ok"]); F.append(s.finish())

    # 7 close
    s = frame()
    s.text(70, 290, "The same trade", "black", 74, D["ink"], track=-2)
    s.text(70, 385, "REST already made.", "black", 74, D["acc"], track=-2)
    s.rect(70, 450, 940, 3, fill=D["line"])
    s.lines(70, 530, ["What I haven't done yet: run two",
                      "instances behind a balancer and",
                      "watch it behave."], "reg", 36, D["dim"], 48)
    foot(s, "FULL POST BELOW", D["acc"]); F.append(s.finish())
    return F


# ==================== GIF 2 - prompt caching, verified ====================
# Sequel to the MCP token-cost post. Built with the gradient/glow toolkit
# throughout (the MCP-stateless GIF above predates it and stays flat).
def gif_frames_promptcache():
    D = DARK
    F = []

    def frame():
        return Slide(("#0A0E14", "#161F2A"), GW, GH)

    def foot(s, t, col=None):
        s.text(70, 1010, t, "mono", 24, col or D["dim"], track=1)

    def stack(s, x, y, w, rowh, rows, dim_from=None):
        """rows: list of (label, color). dim_from grays out rows at/after
        that index, to show a cache hit skipping the already-processed part."""
        for i, (label, col) in enumerate(rows):
            active = dim_from is None or i < dim_from
            fill = D["card"] if active else "#12181F"
            txt = D["ink"] if active else "#3D4753"
            s.rect(x, y + i * rowh, w, rowh - 10, fill=fill, outline=col if active else "#232B35",
                  width=2, r=10)
            s.text(x + 24, y + i * rowh + rowh / 2 - 5, label, "bold", 26, txt, anchor="ls")

    # 1 title
    s = frame()
    s.eyebrow("AI ENGINEERING - CONCEPT", D)
    s.lines(70, 340, ["Prompt caching,", "in 8 frames."], "black", 84, D["ink"], 98, track=-3)
    s.rect(70, 560, 940, 3, fill=D["line"])
    s.lines(70, 640, ["The mechanism MCP's own spec", "just leaned on to fix the token-",
                      "cost problem I posted last week."], "reg", 34, D["dim"], 46)
    foot(s, "VERIFIED AGAINST ANTHROPIC'S DOCS", D["acc"]); F.append(s.finish())

    # 2 every call ships the full context
    s = frame()
    s.text(70, 140, "Every call ships this, in full.", "black", 46, D["ink"], track=-1)
    rows = [("System prompt", D["line"]), ("Tools", D["line"]), ("History", D["line"]),
            ("New message", D["acc"])]
    stack(s, 70, 230, 560, 130, rows)
    s.arrow(650, 420, 780, 420, D["dim"], 5, 16)
    s.badge(900, 420, 140, s.icon_bolt, ["Model"], D["ink"], D)
    foot(s, "SYSTEM + TOOLS + HISTORY + MESSAGE"); F.append(s.finish())

    # 3 most of it is identical call to call
    s = frame()
    s.text(70, 140, "Call after call, most of", "black", 44, D["ink"], track=-1)
    s.text(70, 195, "that stack never changes.", "black", 44, D["ink"], track=-1)
    s.rect(60, 270, 580, 340, outline=D["ok"], width=3, r=16)
    rows = [("System prompt", D["line"]), ("Tools", D["line"]), ("History", D["line"])]
    stack(s, 90, 300, 520, 100, rows)
    s.text(90, 630, "IDENTICAL, EVERY CALL", "monob", 24, D["ok"], track=1)
    s.rect(60, 690, 580, 90, fill=D["fillbad"], outline=D["bad"], width=2, r=14)
    s.text(90, 745, "New message - the only part that changes", "bold", 24, D["ink"])
    foot(s, "ONE SMALL TAIL IS ACTUALLY NEW"); F.append(s.finish())

    # 4 without caching - full reprocess every time
    s = frame()
    s.text(70, 140, "Without caching:", "black", 50, D["bad"], track=-1)
    for i, cx in enumerate((280, 640)):
        s.rect(cx - 130, 260, 260, 380, fill=D["fillbad"], outline=D["bad"], width=2, r=16)
        s.text(cx, 300, f"CALL {i+1}", "monob", 24, D["bad"], anchor="ms")
        s.icon_clock(cx, 440, 60, D["bad"])
        s.lines(cx, 560, ["full cost,", "full latency"], "bold", 24, D["ink"], 32, anchor="ms")
    s.text(70, 720, "Reprocessed from scratch, every call.", "reg", 32, D["dim"])
    foot(s, "THE EXPENSIVE DEFAULT", D["bad"]); F.append(s.finish())

    # 5 with caching - call 1 writes
    s = frame()
    s.text(70, 140, "With caching - call 1", "black", 46, D["ink"], track=-1)
    rows = [("System prompt", D["line"]), ("Tools", D["line"]), ("History", D["line"])]
    stack(s, 70, 230, 560, 100, rows)
    s.rect(70, 530, 560, 3, fill=D["acc"])
    s.text(650, 545, "breakpoint", "mono", 22, D["acc"], anchor="lm")
    s.badge(850, 300, 160, s.icon_lock, ["CACHE", "WRITE"], D["acc"], D)
    s.text(70, 620, "Hashes the prefix, stores its state.", "reg", 32, D["dim"])
    s.text(70, 680, "Costs slightly MORE than normal - once.", "bold", 30, D["acc"])
    foot(s, "1.25x-2x, ONE TIME"); F.append(s.finish())

    # 6 call 2 - cache hit
    s = frame()
    s.text(70, 140, "Call 2, same prefix,", "black", 46, D["ink"], track=-1)
    s.text(70, 195, "inside the TTL window", "black", 46, D["ink"], track=-1)
    rows = [("System prompt", D["line"]), ("Tools", D["line"]), ("History", D["line"])]
    stack(s, 70, 260, 560, 90, rows, dim_from=0)
    s.badge(850, 340, 160, s.icon_bolt, ["CACHE", "HIT"], D["ok"], D)
    s.rect(70, 560, 560, 90, fill=D["fillok"], outline=D["ok"], width=2, r=14)
    s.text(100, 615, "Only the new tail gets processed", "bold", 24, D["ink"])
    foot(s, "HASH MATCH -> REUSE, DON'T REPROCESS", D["ok"]); F.append(s.finish())

    # 7 payoff - 2 bars, no axis
    s = frame()
    s.text(70, 140, "The payoff", "black", 54, D["ink"], track=-1)
    s.text(70, 320, "NORMAL PRICE", "mono", 26, D["dim"], track=2)
    s.rect(70, 350, 940, 110, fill=D["line"], r=12)
    s.text(100, 425, "100%", "bold", 44, "#12181F")
    s.text(70, 520, "CACHED PREFIX", "mono", 26, D["ok"], track=2)
    s.rect(70, 550, 110, 110, fill=D["ok"], r=12)
    s.text(70, 705, "~10% of the price. Faster, too.", "bold", 34, D["ink"])
    foot(s, "SAME OUTPUT, EVERY TIME", D["ok"]); F.append(s.finish())

    # 8 the catch + tie-back
    s = frame()
    s.icon_warn(120, 175, 55, D["acc"])
    s.text(210, 195, "Edit anything upstream, or let the", "bold", 32, D["ink"])
    s.text(210, 235, "TTL lapse - back to full price.", "bold", 32, D["acc"])
    s.rect(70, 300, 940, 3, fill=D["line"])
    s.lines(70, 400, ["MCP's July 2026 spec update leans on", "this exact mechanism - tool-list",
                      "responses now carry ttlMs/cacheScope,", "so clients cache catalogs instead of",
                      "refetching them every call."], "reg", 34, D["dim"], 46)
    s.text(70, 900, "Same fix, different layer.", "black", 42, D["acc"], track=-1)
    foot(s, "FULL POST BELOW", D["acc"]); F.append(s.finish())
    return F


# ============================== main =====================================
def save_deck(name, imgs, out):
    d = os.path.join(out, name)
    os.makedirs(d, exist_ok=True)
    for i, im in enumerate(imgs, 1):
        im.save(os.path.join(d, f"{i}.png"), optimize=True)
    pdf = os.path.join(out, name + ".pdf")
    imgs[0].save(pdf, save_all=True, append_images=imgs[1:], resolution=150.0)
    print(f"  {name}: {len(imgs)} PNG + {os.path.basename(pdf)} "
          f"({os.path.getsize(pdf)/1024:.0f} KB)")


def save_gif(name, frames, durations, out, frames_dirname):
    pal = [f.convert("P", palette=Image.ADAPTIVE, colors=64) for f in frames]
    gp = os.path.join(out, name + ".gif")
    pal[0].save(gp, save_all=True, append_images=pal[1:], duration=durations,
                loop=0, optimize=True)
    print("  %s.gif: %d frames, %.0f KB" % (name, len(frames), os.path.getsize(gp) / 1024))
    d = os.path.join(out, frames_dirname)
    os.makedirs(d, exist_ok=True)
    for i, f in enumerate(frames, 1):
        f.save(os.path.join(d, "%d.png" % i), optimize=True)
    print("  %s: %d PNG" % (frames_dirname, len(frames)))


def build_all(theme, out):
    os.makedirs(out, exist_ok=True)
    print("Building assets (theme: %s) -> %s" % (theme, os.path.abspath(out)))

    save_deck("deck-interview-shift", deck_a(), out)
    save_deck("deck-cache-aside", deck_b(), out)
    save_deck("deck-mcp-token-cost", deck_c(), out)
    save_deck("deck-postgres-storage", deck_d(), out)

    d = os.path.join(out, "singles")
    os.makedirs(d, exist_ok=True)
    for k, im in singles().items():
        f = os.path.join(d, k + ".png")
        im.save(f, optimize=True)
        print("  singles/%s.png (%.0f KB)" % (k, os.path.getsize(f) / 1024))

    # hold title/payoff frames longer than the build-up, for both GIFs
    save_gif("mcp-stateless", gif_frames(), [2300, 1500, 1800, 2000, 2400, 2200, 2600],
             out, "mcp-gif-frames")
    save_gif("prompt-caching", gif_frames_promptcache(),
             [2600, 1700, 1900, 1900, 2000, 2000, 2200, 2800],
             out, "prompt-caching-frames")


def preview(path, picks=(0, 2, 3)):
    """One sheet: the same three slides rendered in every theme, one row each.
    Cheapest way to judge a rotation before committing a post to it."""
    rows, names = [], list(THEMES)
    for name in names:
        use_theme(name)
        deck = deck_b()
        rows.append([deck[i] for i in picks])
    use_theme("signal")

    cw = 330
    ch = int(cw * H / W)
    lab = 46
    pad = 12
    cols = len(picks)
    sheet = Image.new("RGB", (cols * cw + pad * (cols + 1),
                              len(rows) * (ch + lab) + pad * (len(rows) + 1)),
                      "#39434D")
    dr = ImageDraw.Draw(sheet)
    for r, (name, row) in enumerate(zip(names, rows)):
        y = pad + r * (ch + lab + pad)
        dr.text((pad + 4, y + 12), name.upper(), font=font("monob", 15),
                fill="#FFFFFF")
        for c, im in enumerate(row):
            sheet.paste(im.resize((cw, ch), Image.LANCZOS),
                        (pad + c * (cw + pad), y + lab))
    sheet.save(path)
    print("preview ->", path, sheet.size)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--theme", default="signal", choices=list(THEMES),
                    help="palette to build with (rotate every 3-4 posts)")
    ap.add_argument("--preview", metavar="PNG",
                    help="write a theme-comparison sheet and exit")
    a = ap.parse_args()

    if a.preview:
        preview(a.preview)
    else:
        use_theme(a.theme)
        # the default theme keeps the stable asset paths; others get a subfolder
        out = (os.path.join(ROOT, "assets") if a.theme == "signal"
               else os.path.join(ROOT, "assets", "theme-" + a.theme))
        build_all(a.theme, out)
        print("done")
