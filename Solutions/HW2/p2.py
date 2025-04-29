import matplotlib.pyplot as plt
from charge import Charge
from p1 import gradient
import numpy as np

if __name__ == "__main__":
    xgrid, ygrid = np.meshgrid(np.arange(-25, 26), np.arange(-25, 26))
    charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
    potential = np.sum(c.potential(xgrid, ygrid) for c in charges)

    # Approximate the e-field with the gradient
    approx_e = gradient(potential)

    # Get the real e-field from coulomb's law
    real_ex = np.zeros_like(potential)
    real_ey = np.zeros_like(potential)

    for charge in charges:
        ex, ey = charge.e_field(xgrid, ygrid)
        real_ex += ex
        real_ey += ey

    grad_ex = -approx_e[1]
    grad_ey = -approx_e[0]

    # Compute fractional errors
    err_ex = (real_ex - grad_ex) / real_ex
    err_ey = (real_ey - grad_ey) / real_ey

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    im0 = axs[0].imshow(err_ex)
    axs[0].set_title("Error in Ex")
    im1 = axs[1].imshow(err_ey)
    axs[1].set_title("Error in Ey")
    fig.colorbar(im1, ax=axs[1])
    fig.colorbar(im0, ax=axs[0])
    plt.show()