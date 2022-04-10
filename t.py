"""
Trying basic mel diagram
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

PI = np.pi


def plot_button(
    pos: tuple[float, float],
    notes: tuple[str, str],
    *,
    ax,
    radius: float = 0.02,
    rotation: float = -15,
):
    """
    Parameters
    ----------
    rotation
        Rotation of the push/pull separation line (degrees). Positive is anti-clockwise.
    """
    xc, yc = pos
    r = radius
    note_push, note_pull = notes

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
        color="gold",
        solid_capstyle="butt",
        zorder=0,
    )
    r2 = r / 2
    text_kwargs = dict(va="center", ha="center", fontfamily="sans-serif")
    ax.text(xc + r2 * np.cos(PI + rot), yc + r2 * np.sin(PI + rot), note_pull, **text_kwargs)
    ax.text(xc + r2 * np.cos(rot), yc + r2 * np.sin(rot), note_pull, **text_kwargs)


fig, ax = plt.subplots(figsize=(8, 7))

# ax.set_axis_off()

# TODO: look into PolyCollection instead individual patches for speed?

# Standard 21-key D/G
s2 = "F/Eb D/F# G/A B/C D/E F#/G B/A D/C G/E B/F#"
s1 = "G#/Bb A/C# D/E F#/G A/B D/C# F#/E A/G D/B F#/C# A/E"

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


ax.axis("scaled")
ax.set(xlim=(0, 1), ylim=(0, 1))

fig.tight_layout()
