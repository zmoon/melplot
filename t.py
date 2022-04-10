"""
Trying basic mel diagram
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")


def plot_button(pos: tuple[float, float], notes: tuple[str, str], *, ax, radius: float = 0.02):
    p = mpl.patches.Circle(pos, radius=radius, facecolor="none", edgecolor="blue")
    ax.add_patch(p)

    # theta0 = np.pi/2
    # rot = np.deg2rad(-30)
    # ax.plot(
    #     [pos[0] + r * np.cos(theta0 + rot), pos[0] + r * np.cos(theta0 - rot)],
    #     [pos[1] + r * np.sin(theta0 + rot), pos[1] + r * np.sin(-theta0 - rot)],
    #     "-", color="gold",
    # )
    ax.plot(
        [pos[0], pos[0]],
        [pos[1] + r, pos[1] - r],
        c="gold",
        solid_capstyle="butt",
        zorder=0,
    )
    ax.text(pos[0] - radius / 2, pos[1], notes[0], va="center", ha="center")
    ax.text(pos[0] + radius / 2, pos[1], notes[1], va="center", ha="center")


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
