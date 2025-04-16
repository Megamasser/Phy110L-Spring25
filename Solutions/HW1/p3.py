from charge import Charge
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Problem 2, dipole

    x_grid, y_grid = np.meshgrid(np.arange(-25, 26), np.arange(-25, 26))
    charges = [
        Charge(-7.5, 0, -1),
        Charge(7.5, 0, -1),
        Charge(0, -7.5, 1),
        Charge(0, 7.5, 1)
    ]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)
    plt.figure(figsize=(10, 10))
    plt.title("Potential of a quadrupole")
    plt.imshow(potentials, cmap='viridis', extent=(-25, 25, -25, 25), aspect=1)
    plt.colorbar()
    levels = np.linspace(-0.5, 0.5, 10)
    plt.contour(potentials,
                levels=levels,
                colors='black',
                linestyles='dotted',
                extent=(-25, 25, -25, 25))
    plt.figtext(
        0.5,
        0.01,
        "The potential of a quadrupole is shown. Note how the symmetry of the charges leads to a nice symmetry in the potential.",
        ha="center",
        wrap=True)
    plt.show()
