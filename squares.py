import matplotlib.pyplot as pyplot


def squared_nums_line():
    # plot of squared numbers based upon input values array
    input_values = [1, 2, 3, 4, 5, 6, 7, 8]
    squares = []
    for value in input_values:
        squares.append(value**2)

    pyplot.style.use("dark_background")
    fig, ax = pyplot.subplots()
    ax.plot(input_values, squares, linewidth=3)

    # set chart title and labels
    ax.set_title("Squares", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # set ticks
    ax.tick_params(labelsize=14)

    pyplot.show()


def squared_nums_points():
    # plot of one or more points

    x_values = range(1, 1001)
    y_values = [x**2 for x in x_values]

    pyplot.style.use("dark_background")
    fig, ax = pyplot.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Greens, s=10)

    # set chart title and labels
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # set ticks and range
    ax.tick_params(labelsize=14)
    ax.axis([0, x_values[-1] * 1.1, 0, y_values[-1] * 1.1])
    ax.ticklabel_format(style="plain")

    pyplot.savefig("squares_plot.png", bbox_inches="tight")
    pyplot.show()
