from charge import Charge, plot_field_line
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
                                step_size=0.5,
                                method="euler",
                                color="grey")
                plot_field_line(**line,
                                x_extent=x_extent,
                                y_extent=y_extent,
                                charges=charges,
                                step_size=0.5,
                                method="rk2",
                                color="black")

plt.title("Comparing Euler (grey) to RK2 (black) with h = 0.5")
plt.xlim(x_extent)
plt.ylim(y_extent)
plt.show()

for line in lines:
                plot_field_line(**line,
                                x_extent=x_extent,
                                y_extent=y_extent,
                                charges=charges,
                                step_size=0.1,
                                method="euler",
                                color="grey")
                plot_field_line(**line,
                                x_extent=x_extent,
                                y_extent=y_extent,
                                charges=charges,
                                step_size=0.1,
                                method="rk2",
                                color="black")

plt.title("Comparing Euler (grey) to RK2 (black) with h = 0.1")
plt.xlim(x_extent)
plt.ylim(y_extent)
plt.show()