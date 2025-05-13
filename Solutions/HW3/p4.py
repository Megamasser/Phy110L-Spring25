from charge import Charge, plot_field_line, plot_equipotential
import matplotlib.pyplot as plt
import json
import numpy as np
from functools import partial
"""
There are a couple of ways to make this code look a little nice. One
would be to put the list of lines we want to plot in a text file,
then load them up.

But for the purposes of this assignment I'll just make a long list
"""

charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
y_extent = [-25, 25]
x_extent = [-25, 25]
with open("lines.json", "r") as f:
    lines = json.load(f)

for line in lines:
    plot_field_line(**line,
                    x_extent=x_extent,
                    y_extent=y_extent,
                    charges=charges,
                    step_size=0.1,
                    method="rk2",
                    color="grey")


def get_potential_on_axis(x_point, charges):
    v = 0
    for charge in charges:
        v += charge.potential(x_point, 0)
    return v


potential_fn = partial(get_potential_on_axis, charges=charges)

levels = [0.5, 0.1, 0.05, -0.05, -0.1, -0.5]

xgrid = np.linspace(-7.49, 7.49, 200)
potentials = np.fromiter(map(potential_fn, xgrid), dtype="float")
for level in levels:
    i = np.argmax(potentials > level)
    starting_point = (xgrid[i], 0)
    plot_equipotential(starting_point,
                       charges,
                       0.01,
                       method="rk2",
                       max_steps=10000,
                       color="black")

plt.xlim([-25, 25])
plt.ylim([-25, 25])
plt.show()