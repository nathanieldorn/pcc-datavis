from randomwalk_plot import walk_about
from roll_dice import result_frequency, roll_histogram
from squares import squared_nums_line, squared_nums_points


def main():
    """Remove comment to run a function. Only one at a time may be run."""

    # graphs a line of squared numbers
    # squared_nums_lines()

    # graphs points of squared numbers
    # squared_nums_points()

    # graphs a random walk function
    # walk_about()

    # roll a die and get the frequency of results as a histogram
    roll_histogram(result_frequency(rolls=10000))


if __name__ == "__main__":
    main()
