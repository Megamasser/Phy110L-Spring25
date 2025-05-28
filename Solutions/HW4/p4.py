
from p1 import relax
import matplotlib.pyplot as plt
import numpy as np

r = 50
y_grid, x_grid = np.mgrid[-r:r + 1, -r:r + 1]
potentials = np.zeros(x_grid.shape)

plate_y = int(0.2 * r)

positive_plate_mask = y_grid == plate_y
negative_plate_mask = y_grid == -plate_y

potentials[positive_plate_mask] = 1
potentials[negative_plate_mask] = -1

y_boundary_mask = np.abs(y_grid) == r

no_update_mask = y_boundary_mask | positive_plate_mask | negative_plate_mask
"""
The relaxation method is approximate. A pixel can only be set to zero if every
pixel around it is also zero. Take the case of a pixel directly adjacent
one of the plates. These plates are held at a constant potential, so the adjacent
pixel cannot ever be set to zero by definition.

We still get pretty close though.
"""

potential, n_iters = relax(potentials, no_update_mask)
plt.imshow(potential)
plt.colorbar()
plt.show()
