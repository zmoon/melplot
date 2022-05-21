"""
Trying basic mel diagram
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

PI = np.pi
DEBUG = True


tran = str.maketrans("#b=0123456789", "♯♭♮₀₁₂₃₄₅₆₇₈₉")


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
    ax.text(xc + r2 * np.cos(PI + rot), yc + r2 * np.sin(PI + rot), note_push, **text_kwargs)
    ax.text(xc + r2 * np.cos(rot), yc + r2 * np.sin(rot), note_pull, **text_kwargs)


fig, ax = plt.subplots(figsize=(8.5, 8.5))

if not DEBUG:
    ax.set_axis_off()

# TODO: look into PolyCollection instead individual patches for speed?

# Standard 21-key D/G
s4 = "D+/A+ D/A G+/D+ G/D"
s3 = "B+/E- B/E C+/C+ C/C"
s2 = "F5/Eb5 D4/F#4 G4/A B/C D/E G5/F# B/A D/C G6/E B/F#"
s1 = "G#4/Bb4 A3/C#4 D4/E F#/G A/B D5/C# F#/E A/G D6/B F#/C# A/E"

# Row 1
r = 0.04  # radius
d = 0.01  # space between
dx = 2 * r + d  # center to center
xs = np.arange(11) * dx + r + d
for x, s in zip(xs, s1.split()):
    plot_button((x, 0.2), s.split("/"), radius=r, ax=ax)

# Row 2
xs = np.arange(10) * dx + r + d + dx / 2
for x, s in zip(xs, s2.split()):
    plot_button((x, 0.29), s.split("/"), radius=r, ax=ax)

# "Bellows"
ys = [0.37, 0.4, 0.43, 0.46]
for y in ys:
    ax.plot([0.3, 0.7], [y, y], "0.1", lw=1)

xs = np.arange(4) * dx + r + d + 3.5 * dx
for x, s in zip(xs, s3.split()):
    plot_button((x, 0.53), s.split("/"), radius=r, ax=ax)

for x, s in zip(xs, s4.split()):
    plot_button((x, 0.62), s.split("/"), radius=r, ax=ax)


ax.axis("scaled")
ax.set(xlim=(0, 1), ylim=(0, 1))

fig.tight_layout()
