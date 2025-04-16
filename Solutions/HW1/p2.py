from charge import Charge
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Problem 2, dipole

    x_grid, y_grid = np.meshgrid(np.arange(-25, 26), np.arange(-25, 26))
    charges = [Charge(-7.5, 0, -1), Charge(7.5, 0, 1)]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)
    plt.figure(figsize=(10, 10))
    plt.imshow(potentials, cmap='viridis', extent=(-25, 25, -25, 25), aspect=1)
    plt.colorbar()
    levels = np.linspace(-0.5, 0.5, 10)
    plt.contour(potentials,
                levels=levels,
                colors='black',
                linestyles='dotted',
                extent=(-25, 25, -25, 25))

    plt.title("Potential of a dipole")
    plt.show()
    # Since we know the electric field goes like 1/r^3 for a dipole,
    # we expect the potential to go like 1/r^2.
