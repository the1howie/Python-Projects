import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, use


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
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # plot surface (cm.Greens or cm.viridis_r)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis_r, linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    for ytick in cbar.ax.get_yticklabels():
        ytick.set_color("white")

    return {"figure": fig, "axes": ax, "plot": surf}


def rotate_axes(ax, fig, step=1):
    # step is in degrees.
    # WARNING: If step==1, it takes a long time to run!!!
    # Source for the rotation loop:
    # https://matplotlib.org/stable/gallery/mplot3d/rotate_axes3d_sgskip.html

    # to ensure that the backend renderer doesn't change
    use("Qt5Agg")

    # data validation
    step = min(int(step) % 360, 360)

    # Rotate the axes and update
    for angle in range(0, 360 * 4 + 1, step):
        # Normalize the angle to the range [-180, 180] for display
        angle_norm = (angle + 180) % 360 - 180

        # Cycle through a full rotation of elevation, then azimuth, roll, and all
        elev = azim = roll = 0
        if angle <= 360:
            elev = angle_norm
        elif angle <= 360 * 2:
            azim = angle_norm
        elif angle <= 360 * 3:
            roll = angle_norm
        else:
            elev = azim = roll = angle_norm

        # Update the axis view and title
        ax.view_init(elev, azim, roll)
        plt.title(
            "Elevation: %d°, Azimuth: %d°, Roll: %d°" % (elev, azim, roll),
            color="white",
        )
        # plt.draw() # too slow, it re-draws the surface
        fig.canvas.draw()  # this method uses the existing figure
        plt.pause(0.001)


if __name__ == "__main__":
    sombrero = plot_sombrero()
    plt.show()
    # rotate_axes(sombrero["axes"], sombrero["figure"], 5)
