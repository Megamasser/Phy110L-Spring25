from charge import Charge
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Problem 2, dipole

    x_grid, y_grid = np.meshgrid(np.arange(-25, 26), np.arange(-25, 26))
    charges = [Charge(-7.5, 0, -1), Charge(7.5, 0, 1)]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)
    e_field = np.gradient(potentials)
    # Note, numpy index ordering is (y,x), so to get angles that are consistent
    # with usual conventions, we need to do the opposite of what may be natural
    angles = np.degrees(np.arctan2(-e_field[0], -e_field[1]))
    plt.imshow(
        angles,
        extent=(-25, 25, -25, 25),
        cmap='twilight',
    )
    plt.colorbar(label="Angle (degrees)")
    plt.title("Electric field direction for a dipole")
    plt.show()
    """
    There are a few issues with using Coulomb's law directly to calculate the electric field. The most notable is that
    we then have to track components of the electric field during computation, which adds complexity. There is a very
    simple relationship between potential and electric field, and the potential is pretty cheap to calcualte.

    The main issue with the potential -> electric field method if we care about the E field is we have to do a second 
    calculation to get there, which leads to the possibility of numerical errors.
    """
