import matplotlib.pyplot as pyplot
from randomwalks import RandomWalk


def walk_about():
    # create a random walk
    random_walk = RandomWalk()
    random_walk.fill_walk()

    # plot the walk
    pyplot.style.use('dark_background')
    fig, ax = pyplot.subplots()
    ax.scatter(random_walk.x_values, random_walk.y_values, color=(0, 0.8, 0), s=15)
    ax.set_aspect('equal')
    pyplot.show()
