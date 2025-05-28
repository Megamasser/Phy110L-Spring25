import numpy as np
import matplotlib.pyplot as plt
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

    plt.figure(figsize=(8, 8))
    ax_start = plt.subplot(2, 2, 1)
    ax_end = plt.subplot(2, 2, 3)
    ax_cut = plt.subplot(1, 2, 2)

    potential, mask = build_square_setup(25)
    ax_start.imshow(potential)
    ax_start.set_title("Initial setup")
    potential, n_iterations = relax(potential, mask)
    print(f"51x51 grid converged after {n_iterations} steps")
    ax_end.imshow(potential)
    ax_end.set_title("After relaxation")
    cut = potential[:, 25]
    ax_cut.plot(cut)
    ax_cut.set_title("Cut along y axis")
    ax_cut.set_xlabel("y")
    ax_cut.set_ylabel("Potential")
    plt.show()