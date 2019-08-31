import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x1 = 1
y1 = 2
x2 = 8
y2 = 5
r1 = 10
r2 = 10
fig, ax = plt.subplots()

circle1 = plt.Circle((x1, y1), r1, fill=False, color='tab:blue')
circle2 = plt.Circle((x2, y2), r2, fill=False, color='tab:orange')
points, = ax.plot([], [], 'o')

def get_intersection(x1, x2, y1, y2, r1, r2):
    """ Return intersection point of two circles:
         Centers: (x1, y1), (x2, y2)
         Radii: r1, r2"""
    R = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    soln_x1 = 0.5*(x1 + x2) + ((r1**2 - r2**2)/(2*R**2))*(x2-x1) + \
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (y2 - y1)

    soln_x2 = 0.5*(x1 + x2) + ((r1**2 - r2**2)/(2*R**2))*(x2-x1) -\
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (y2 - y1)

    soln_y1 = 0.5*(y1 + y2) + ((r1**2 - r2**2)/(2*R**2))*(y2-y1) + \
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (x1 - x2)

    soln_y2 = 0.5*(y1 + y2) + ((r1**2 - r2**2)/(2*R**2))*(y2-y1) - \
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (x1 - x2)

    return (soln_x1, soln_y1), (soln_x2, soln_y2)


def get_y(x1, x2, y1, y2, r1, r2):
    """ Return intersection point of two circles:
     Centers: (x1, y1), (x2, y2)
     Radii: r1, r2"""

    R = np.sqrt((x2 - x1)**2 + (y2-y1)**2)
    result1 = 0.5*(y1 + y2) + ((r1**2 - r2**2)/(2*R**2))*(y2-y1) + \
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (x1 - x2)
    result2 = 0.5*(y1 + y2) + ((r1**2 - r2**2)/(2*R**2))*(y2-y1) - \
             0.5 * np.sqrt((2*(r1**2 + r2**2)/R**2) - ((r1**2 - r2**2)**2)/(R**4) - 1) * (x1 - x2)
    return result1, result2


def plot_intersections():
    results = get_intersection(x1, x2, y1, y2, r1, r2)
    for x, y in results:
        plt.scatter(x, y)

def init():
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    points.set_data([], [])
    return circle1, circle2, points

def animate(i):
    x1 = 5 + 3 * np.sin(np.radians(i))
    y1 = 5 + 3 * np.cos(np.radians(i))
    circle1.center = (x1, y1)

    x2 = 2 + 3 * np.sin(np.radians(i + 180))
    y2 = 2 + 3 * np.cos(np.radians(i + 180))
    circle2.center = (x2, y2)

    (ix1, iy1), (ix2, iy2) = get_intersection(x1, x2, y1, y2, r1, r2)
    points.set_data([ix1, ix2], [iy1, iy2])
    return circle1, circle2, points

def run_animation():
    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=360, interval=20, blit=True)


    plt.xlim([-20, 20])
    plt.ylim([-20, 20])
    plt.show()

def display():
    plt.show()


if __name__ == "__main__":

    # plot_intersections()
    # display()


    run_animation()
