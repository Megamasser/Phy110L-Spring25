from charge import Charge, plot_field_line, plot_equipotential
import matplotlib.pyplot as plt
import json
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

plot_equipotential((2, 0),
                   charges,
                   step_size=0.01,
                   method="rk2",
                   max_steps=5000,
                   color="black")
plot_equipotential((-2, 0),
                   charges,
                   step_size=0.01,
                   method="rk2",
                   max_steps=5000,
                   color="black")
plot_equipotential((-4, 0),
                   charges,
                   step_size=0.01,
                   method="rk2",
                   max_steps=5000,
                   color="black")
plot_equipotential((4, 0),
                   charges,
                   step_size=0.01,
                   method="rk2",
                   max_steps=5000,
                   color="black")
plt.xlim(x_extent)
plt.ylim(y_extent)
plt.show()