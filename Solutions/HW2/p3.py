
from charge import Charge, plot_field_line
import matplotlib.pyplot as plt

if __name__ == "__main__":
    charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
    # A) From positive-> negative
    start = (7.4, 0)
    end = (charges[1].x, charges[1].y)
    figure = plot_field_line(start,
                             end, [-25, 25], [-25, 25],
                             charges,
                             step_size=0.1,
                             color="black")
    plt.title("From positive charge to negative charge")
    plt.show()

    # B) From negative->positive (Against the field!)
    start = (-7.4, 0)
    end = (charges[0].x, charges[0].y)
    figure = plot_field_line(start,
                             end, [-25, 25], [-25, 25],
                             charges,
                             step_size=0.1,
                             color="black",
                             propogation_direction="a")
    plt.title("From negative charge to positive charge")
    plt.show()

    # C) Launch straight up from positive charge
    start = (7.5, 0.1)
    end = (charges[1].x, charges[1].y)
    figure = plot_field_line(start,
                             end, [-25, 25], [-25, 25],
                             charges,
                             step_size=0.01,
                             color="black")
    plt.title("Launched directly up from positive charge")
    plt.show()

    # D) In real life, the trajectory of the charge will depend on its current speed, its mass, and its total charge. The field line tells us things about the acceleration of a charge located at a given point, but an actual charge will behave differently.
