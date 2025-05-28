import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from laplace import build_square_setup, relax

if __name__ == "__main__":
    x_grid, y_grid = np.meshgrid(range(-25, 26), range(-25, 26))

    potential = np.zeros(x_grid.shape, dtype="float")
    # Let's make the square 17x17
    bounds = (-8, 8)
    mask_top = (y_grid == -8) & (x_grid < 9) & (x_grid > -9)
    mask_bottom = (y_grid == 8) & (x_grid < 9) & (x_grid > -9)
    mask_left = (x_grid == -8) & (y_grid < 9) & (y_grid > -9)
    mask_right = (x_grid == 8) & (y_grid < 9) & (y_grid > -9)
    square_mask = mask_top | mask_bottom | mask_left | mask_right

    outer_mask = (np.abs(x_grid) == x_grid.max()) | (np.abs(y_grid)
                                                     == y_grid.max())
    potential[square_mask] = 1
    full_mask = square_mask | outer_mask

    potential, mask = build_square_setup(25)
    potential, n_iterations = relax(potential, mask)
    print(f"51x51 grid converged after {n_iterations} steps")
    plt.imshow(potential)
    plt.show()

    potential, mask = build_square_setup(50)
    potential, n_iterations = relax(potential, mask)
    print(f"101x101 grid converged after {n_iterations} steps")
    plt.imshow(potential)
    plt.show()

    potential, mask = build_square_setup(100)
    potential, n_iterations = relax(potential, mask)
    print(f"201x201 grid converged afte0r {n_iterations} steps")
    plt.imshow(potential)
    plt.show()
    """
    The number of required iterations increases by about a factor of 2.5 when
    the grid size is doubled. Think of this in terms of the number of iterations
    for the potential from the center to "reach" the outer boundary. The distance
    doubles, so the number of iterations to get out there roughly doubles as well.

    For each iteration, there are a total of 7 operations. Four rolls, which
    are mostly just copying data around. One average (sum + division) and one
    update. However the complexity of each of these operations depends on the 
    of pixels in the grids. Roughly speaking, there are a total of 7 * n_pixels
    operations per iteration.
    """