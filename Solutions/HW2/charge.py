
import numpy as np
import matplotlib.pyplot as plt


class Charge:

    def __init__(self, x: int, y: int, q: int):
        """
        Our charges will be on grid points. We'll set all constants to 1,
        and make our charges integer as well.
        """
        self.x = x
        self.y = y
        self.q = q

    def potential(self, x_grid: np.ndarray, y_grid: np.ndarray) -> np.ndarray:
        """
        Calculate the potential at each point in the grid.
        """
        if x_grid.min() > self.x or x_grid.max() < self.x:
            raise ValueError("Charge x-coordinate outside of grid.")
        if y_grid.min() > self.y or y_grid.max() < self.y:
            raise ValueError("Charge y-coordinate outside of grid.")

        # calculate the distance from the charge to each point in the grid
        dx = x_grid - self.x
        dy = y_grid - self.y
        r = np.sqrt(dx**2 + dy**2)

        # calculate the potential at each point in the grid
        V = self.q / r
        return V

    def e_field(self, x, y):
        """
        Calculate the electric field at each point in the grid. This
        function will work with a single point or grid of points.
        """

        # calculate the distance from the charge to each point in the grid
        dx = x - self.x
        dy = y - self.y
        r = np.sqrt(dx**2 + dy**2)

        # calculate the electric field at each point in the grid
        Ex = self.q * dx / r**3
        Ey = self.q * dy / r**3

        return Ex, Ey


def plot_field_line(starting_point: tuple[float, float],
                    ending_point: tuple[float, float],
                    x_extent: float,
                    y_extent: float,
                    charges: list[Charge],
                    step_size: float,
                    propogation_direction: str = "w",
                    *args,
                    **kwargs):
    fig = plt.gcf()

    # check if we're plotting with or against the electric field.
    if propogation_direction == "a":
        prop_coeff = -1
    else:
        prop_coeff = 1

    current_point = starting_point

    while True:  # We will continue iterating until we hit one of our termination criteria
        dx, dy = 0, 0
        for charge in charges:
            ds = charge.e_field(*current_point)
            dx += ds[0]
            dy += ds[1]
        # normalize to chosen step size
        ds_norm = np.sqrt(step_size) / np.sqrt(dx**2 + dy**2)
        dx = dx * ds_norm * prop_coeff
        dy = dy * ds_norm * prop_coeff

        # compute the new point
        new_point = (current_point[0] + dx, current_point[1] + dy)
        plt.plot([current_point[0], new_point[0]],
                 [current_point[1], new_point[1]],
                 zorder=0,
                 *args,
                 **kwargs)
        if should_terminate(new_point, ending_point, charges, x_extent,
                            y_extent):
            break
        current_point = new_point

    # Now plot the charges
    for charge in charges:
        if charge.q > 0:
            c = "red"
        else:
            c = "blue"
        plt.scatter(charge.x, charge.y, c=c, zorder=1)

    return fig


def should_terminate(current_point, termination_point, charges, x_extent,
                     y_extent):
    """
    There are two reasons the line plotting should terminate.
    1. We leave the bounds of the box provided by x_extent and y_extent
    2. We get close to the termination point
    """
    x, y = current_point
    x_term, y_term = termination_point
    if x < x_extent[0] or x > x_extent[1] or y < y_extent[0] or y > y_extent[1]:
        return True
    distance = np.sqrt((x - x_term)**2 + (y - y_term)**2)
    if distance < 0.1:
        return True
    return False
