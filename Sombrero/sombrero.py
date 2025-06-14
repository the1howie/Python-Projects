import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def clean_data(start, end, num_pts):
    # remove 0 from data
    a = list(np.linspace(start, end, num_pts))
    if 0 in a:
        a.remove(0)
    return np.array(a)


def plot_sombrero():
    # set up data
    x_num_pts, y_num_pts = (1001, 1001)
    x = clean_data(-8, 8, x_num_pts)
    y = clean_data(-8, 8, y_num_pts)
    X, Y = np.meshgrid(x, y)

    # sombrero formula
    c = 5
    Z = c * np.sin(np.sqrt(X**2 + Y**2)) / np.sqrt(X**2 + Y**2)

    # set up figure
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    fig.set_size_inches(10, 10)
    fig.set_dpi(100)
    # fig.set_alpha(0.5)
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # plot surface
    surf = ax.plot_surface(X, Y, Z, cmap=cm.Greens, linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    for ytick in cbar.ax.get_yticklabels():
        ytick.set_color("white")
    plt.show()


if __name__ == "__main__":
    plot_sombrero()
