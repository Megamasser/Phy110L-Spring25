import numpy as np
import warnings


def build_square_setup(r=25):
    """
    x_Return an initial potential grid and a no_update mask for a grid
    of half-width r. The central square will always have a width
    which is 1/3 the total width of the box.

    Boundary of the central square will always be held at v = 1
    outer boundary of grid will always be at v = 0
    """
    y_grid, x_grid = np.mgrid[-r:r + 1, -r:r + 1]
    center_halfwidth = int(np.floor((r + 1) / 3))
    center_mask = build_center_square(center_halfwidth, x_grid, y_grid)
    edge_mask = (np.abs(x_grid) == r) | (np.abs(y_grid) == r)

    potentials = np.zeros(x_grid.shape)
    potentials[center_mask] = 1
    total_mask = edge_mask | center_mask
    return potentials, total_mask


def build_center_square(halfwidth, x_grid, y_grid):
    horizontal_walls = (np.abs(y_grid) == halfwidth) & (np.abs(x_grid)
                                                        <= halfwidth)
    vertical_walls = (np.abs(x_grid) == halfwidth) & (np.abs(y_grid)
                                                      <= halfwidth)
    return horizontal_walls | vertical_walls


def relax(potential, mask, tolerance=0.001):
    n_iterations = 1
    old_potential = potential
    new_potential = update_potential(potential, mask)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        while not has_converged(old_potential, new_potential, tolerance):
            old_potential = new_potential
            new_potential = update_potential(old_potential, mask)
            n_iterations += 1
    return new_potential, n_iterations


def update_potential(potentials, mask):
    """
    Update potentials with the average of their four surrounding
    values. Masked pixels are left unchanged
    """
    shift_down = np.roll(potentials, 1, axis=0)
    shift_up = np.roll(potentials, -1, axis=0)
    shift_left = np.roll(potentials, 1, axis=1)
    shift_right = np.roll(potentials, -1, axis=1)
    average = np.average([shift_down, shift_up, shift_left, shift_right],
                         axis=0)
    average[mask] = potentials[mask]
    return average


def has_converged(old_potential, new_potential, tolerance=0.001):
    fractional_deviation = (new_potential - old_potential) / old_potential
    if np.any(np.abs(fractional_deviation) > tolerance):
        return False
    return True