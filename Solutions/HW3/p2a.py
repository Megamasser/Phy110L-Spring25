from charge import Charge, plot_field_line
import numpy as np
import matplotlib.pyplot as plt

charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
y_extent = [-25, 25]
x_extent = [-25, 25]
charge = Charge(0, 0, 1)
angles = np.linspace(0, 2 * np.pi, 9)

for angle in angles:
    start_x = 0.1 * np.cos(angle)
    start_y = 0.1 * np.sin(angle)
    plot_field_line((start_x, start_y),
                    x_extent=x_extent,
                    y_extent=y_extent,
                    charges=[charge],
                    step_size=0.1,
                    color="black")
plt.xlim(x_extent)
plt.ylim(y_extent)
plt.title("Field lines for single positive charge")
plt.show()