import matplotlib.pyplot as pyplot

from randomwalks import RandomWalk


def walk_about():
    """Plot the walk, prompt for file save, and prompt to run again."""

    while True:
        # create a random walk
        random_walk = RandomWalk(num_points=100000)
        random_walk.fill_walk()

        # plot the walk
        pyplot.style.use("dark_background")
        fig, ax = pyplot.subplots(figsize=(15, 9), dpi=128)
        point_numbers = range(random_walk.num_points)
        ax.scatter(
            random_walk.x_values,
            random_walk.y_values,
            c=point_numbers,
            cmap=pyplot.cm.Greens,
            edgecolors="none",
            s=15,
        )

        # re-color first and last point
        ax.scatter(0, 0, color=(0.9, 0.6, 0, 0.75), edgecolors="none", s=75)
        ax.scatter(
            random_walk.x_values[-1],
            random_walk.y_values[-1],
            color=(0.9, 0.6, 0, 0.75),
            edgecolor="none",
            s=75,
        )

        ax.set_aspect("equal")

        # prompt for file save and re-run
        save_copy = input("Would you like to save a copy? (y/n): ")
        if save_copy == "y":
            pyplot.savefig("random_walk_100k.png", dpi="figure", bbox_inches="tight")

        pyplot.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == "n":
            break
