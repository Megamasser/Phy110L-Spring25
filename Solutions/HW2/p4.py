
from charge import Charge, plot_field_line
import matplotlib.pyplot as plt
"""
There are a couple of ways to make this code look a little nice. One
would be to put the list of lines we want to plot in a text file,
then load them up.

But for the purposes of this assignment I'll just make a long list
"""

charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
y_extent = [-25, 25]
x_extent = [-25, 25]
plot_field_line((7.4, 0), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.5, 0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.5, -0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.45, 0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.45, -0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.55, 0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((7.55, -0.1), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plot_field_line((-7.55, 0.1), (7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                propogation_direction="a",
                color="black")
plot_field_line((-7.55, -0.1), (7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                propogation_direction="a",
                color="black")
plot_field_line((-7.55, 0.0), (7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                propogation_direction="a",
                color="black")
plot_field_line((7.55, 0.0), (-7.5, 0),
                x_extent,
                y_extent,
                charges,
                0.01,
                color="black")
plt.title("Some Electric Field Lines in a Dipole")
plt.xlim(x_extent)
plt.ylim(y_extent)
plt.show()
