"""
Trying basic mel diagram
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

PI = np.pi
DEBUG = False


tran = str.maketrans("#b=0123456789-", "♯♭♮₀₁₂₃₄₅₆₇₈₉−")


def plot_button(
    pos: tuple[float, float],
    notes: tuple[str, str],
    *,
    ax,
    radius: float = 0.02,
    rotation: float = 0,
):
    """
    Parameters
    ----------
    rotation
        Rotation of the push/pull separation line (degrees). Positive is anti-clockwise.
    """
    xc, yc = pos
    r = radius
    note_push, note_pull = (note.translate(tran) for note in notes)

    # Button edge (circle)
    p = mpl.patches.Circle(pos, radius=radius, facecolor="none", edgecolor="blue")
    ax.add_patch(p)

    # Label push and pull notes
    t0 = PI / 2
    rot = np.deg2rad(rotation)
    ax.plot(
        [xc + r * np.cos(t0 + rot), xc + r * np.cos(t0 - rot)],
        [yc + r * np.sin(t0 + rot), yc - r * np.sin(t0 - rot)],
        "-",
        color="forestgreen",
        solid_capstyle="butt",
        zorder=0,
    )
    r2 = r / 2
    text_kwargs = dict(
        va="center", ha="center", fontfamily="sans-serif", color="darkgoldenrod", size=12
    )
    ax.text(
        xc + r2 * np.cos(PI + rot),
        yc + r2 * np.sin(PI + rot),
        note_push.rstrip("*"),
        **text_kwargs,
        weight="bold" if note_push.endswith("*") else None,
    )
    ax.text(xc + r2 * np.cos(rot), yc + r2 * np.sin(rot), note_pull, **text_kwargs)


# TODO: look into PolyCollection instead individual patches for speed?

# Standard 21-key D/G
dg21 = """\
D+|A+ D|A G+|D+ G|D
B+|E- B|E C+|C+ C|C
---
F5|Eb5 D4|F#4 G4|A B|C D|E G5|F# B|A D|C G6|E B|F#
G#4|Bb4 A3|C#4 D4|E F#|G A|B D5|C# F#|E A|G D6|B F#|C# A|E
"""

dg21_treb_only = "\n".join(dg21.splitlines()[3:])

elye_new = """\
Eb+|F#- Eb|F# D+|A+ D|A G+|D+ G|D
Bb+|F+  Bb|F  B-|E- B|E C+|C+ C|C
---
Bb3|F3 Eb|D F|F Bb|G# C|D Eb|Eb E*|F Bb|G# Eb|D E*|F
G3|A B|C4 E4*|F#4 G4|A B|C D|E G5|F# B|A D|C G6|E B|F#
D3|E F#|B A3|C#4 D4|E F#|G A|B D5|C# F#|E A|G D6|B F#|C# A|E
"""


def split_button(s: str, *, sep: str = "|"):
    """Split button with validation."""
    notes = s.split(sep)
    n = len(notes)
    if n > 2:
        raise ValueError(f"invalid button {s!r}, splitting on {sep!r} found >2 notes")
    elif n == 1:
        print(f"note: doubling detected single note {notes[0]!r}")
        notes.append(notes[0])

    return tuple(notes)


def read_layout(s: str, *, button_sep: str = "|"):
    bass_rows = []
    treb_rows = []
    bass = True
    for line in s.splitlines():
        if all(c == "-" for c in line.strip()):  # bellows
            bass = False
            continue

        notes = [split_button(button, sep=button_sep) for button in line.split()]
        if bass:
            bass_rows.append(notes)
        else:
            treb_rows.append(notes)

    # Allow for treble-only diagrams
    if bass:
        treb_rows, bass_rows = bass_rows, []

    return treb_rows, bass_rows


treb_rows, bass_rows = read_layout(elye_new)
nmax = max(len(row) for row in treb_rows)

# Size settings
figw = 9
drel = 0.32  # button padding relative to radius
r = 1 / (2 * nmax + (nmax + 1) * drel)  # radius, maximizing horiz space
d = drel * r  # space between
dx = 2 * r + d  # button center-to-center horiz distance
n_bellows = 4
dy_bellows = 0.03
w_bellows = 0.5
pad_bellows = 0.03

# Vertical offset to make angled/offset treble button spacing same as horiz
# (equilateral triangle arrangement)
d2 = np.sqrt((2 * r + d) ** 2 - (r + d / 2) ** 2) - 2 * r

fig, ax = plt.subplots(figsize=(figw, figw), constrained_layout=True)
# constrained layout seems to do a better job of eliminating unused margin space

if not DEBUG:
    ax.set_axis_off()

# Compute treble row starting positions??
# TODO: Probably want to be able to specify this in input
ns = [len(row) for row in treb_rows]
x0s = [0, 0.5, 1]  # just set for now (button-size-relative)

# Treble buttons
ys = d + r + np.arange(len(treb_rows)) * (2 * r + d2)
for x0, y, row in zip(x0s, ys, reversed(treb_rows)):
    xs = np.arange(len(row)) * dx + r + d + x0 * dx
    for x, s in zip(xs, row):
        plot_button((x, y), s, radius=r, ax=ax)

# Bellows
ys2 = ys[-1] + r + pad_bellows + np.arange(n_bellows) * dy_bellows
for y in ys2:
    ax.plot([0.5 - w_bellows / 2, 0.5 + w_bellows / 2], [y, y], "0.1", lw=1)

# Bass buttons
ys3 = ys2[-1] + pad_bellows + r + np.arange(len(bass_rows)) * dx
x0 = 0.5 - (len(bass_rows[-1]) * dx - d) / 2 + r
# TODO: also support specifying
for y, row in zip(ys3, reversed(bass_rows)):
    xs = x0 + np.arange(len(row)) * dx
    for x, s in zip(xs, row):
        plot_button((x, y), s, radius=r, ax=ax)

ymax = ys3[-1] + r + d

ax.axis("scaled")
ax.set(xlim=(0, 1), ylim=(0, ymax))

if not DEBUG:
    figw_ = fig.get_figwidth()
    assert figw_ == figw
    fig.set_size_inches((figw_, ymax * figw_ * 1.01))

# fig.tight_layout()
