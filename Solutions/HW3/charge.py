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

    def potential(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Calculate the potential at each point in the grid.
        """

        # calculate the distance from the charge to each point in the grid
        dx = x - self.x
        dy = y - self.y
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
                    x_extent: float,
                    y_extent: float,
                    charges: list[Charge],
                    step_size: float,
                    propogation_direction: str = "w",
                    method="rk2",
                    *args,
                    **kwargs):
    fig = plt.gcf()

    # check if we're plotting with or against the electric field.
    if propogation_direction == "a":
        prop_coeff = -1
    else:
        prop_coeff = 1

    if method == "rk2":
        step_fn = step_rk2
    elif method == "euler":
        step_fn = step_euler
    else:
        raise ValueError(
            "The only allowed integration methods are `rk2` and `euler`")

    current_point = starting_point

    fig = plt.gcf()
    while True:  # We will continue iterating until we hit one of our termination criteria
        new_point = step_fn(current_point, charges, step_size, prop_coeff)
        plt.plot([current_point[0], new_point[0]],
                 [current_point[1], new_point[1]],
                 zorder=0,
                 *args,
                 **kwargs)
        if should_terminate(new_point, charges, x_extent, y_extent, step_size,
                            prop_coeff):
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


def step_euler(starting_point: tuple[float, float],
               charges: list[Charge],
               step_size: float,
               propogation_coefficient: int,
               equipotential: bool = False):
    """
    Compute the next step based on the euler method.
    """
    dx, dy = 0, 0
    for charge in charges:
        ds = charge.e_field(*starting_point)
        dx += ds[0]
        dy += ds[1]
    # normalize to chosen step size
    return normalize_step(starting_point, dx, dy, step_size,
                          propogation_coefficient, equipotential)


def plot_equipotential(starting_point: tuple,
                       charges: list[Charge],
                       step_size: float,
                       method: str = "euler",
                       max_steps: int = 1000,
                       *args,
                       **kwargs):
    current_point = starting_point
    if method == "rk2":
        step_fn = step_rk2
    elif method == "euler":
        step_fn = step_euler
    else:
        raise ValueError(
            "The only allowed integration methods are `rk2` and `euler`")
    left_region = False
    tolerance = 0.2
    for i in range(max_steps):
        new_point = step_fn(current_point,
                            charges,
                            step_size,
                            1,
                            equipotential=True)
        plt.plot([current_point[0], new_point[0]],
                 [current_point[1], new_point[1]], *args, **kwargs)
        dist = np.sqrt((current_point[0] - new_point[0])**2 +
                       (current_point[1] - new_point[1])**2)

        if not left_region and dist > tolerance:
            left_region = True
        if left_region and dist < tolerance:
            break
        current_point = new_point


def step_rk2(starting_point: tuple[float, float],
             charges: list[Charge],
             step_size: float,
             propogation_coefficient: int,
             line_type="e_field",
             equipotential: bool = False):
    """
    Compute the next step using the second-order runge-kutta method.
    This function makes use of the euler step to compute the location
    of the intermediate point.
    """
    intermediate_point = step_euler(starting_point, charges, 0.5 * step_size,
                                    propogation_coefficient)
    dx, dy = 0, 0
    for charge in charges:
        ds = charge.e_field(*intermediate_point)
        dx += ds[0]
        dy += ds[1]

    return normalize_step(starting_point, dx, dy, step_size,
                          propogation_coefficient, equipotential)


def normalize_step(starting_point, dx, dy, step_size, propogation_coefficient,
                   equipotential):
    """
    Given a starting point and an unnormalized dx and dy, return the
    next point one step_size away.
    """
    ds_norm = step_size / np.sqrt(dx**2 + dy**2)
    dx = dx * ds_norm * propogation_coefficient
    dy = dy * ds_norm * propogation_coefficient

    if equipotential:
        # rotate 90
        dx, dy = -dy, dx

    return (starting_point[0] + dx, starting_point[1] + dy)


def should_terminate(current_point, charges, x_extent, y_extent, step_size,
                     prop_coeff):
    """
    There are two reasons the line plotting should terminate.
    1. We leave the bounds of the box provided by x_extent and y_extent
    2. We get close enough to one of the charges
    """
    x, y = current_point
    if x < x_extent[0] or x > x_extent[1] or y < y_extent[0] or y > y_extent[1]:
        return True
    for charge in charges:
        # If we're moving with the field line, terminate on a negative charge
        # If we're going against, terminate on a positive charge.
        if np.sign(charge.q) != np.sign(prop_coeff):
            distance = np.sqrt((x - charge.x)**2 + (y - charge.y)**2)
            if distance < 2 * step_size:
                return True
    return False