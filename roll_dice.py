import plotly.express as px

from die import Die


def roll(sides=6, rolls=100):
    """Roll the die and return a list of results"""
    die = Die(sides)
    results = [die.roll() for x in range(rolls)]
    return results


def result_frequency(sides=6, rolls=100):
    """Return a list of the frequency of occurrence for each value of the die"""
    # get roll results
    results = roll(sides, rolls)

    # create list of result frequencies
    frequencies = [results.count(value) for value in range(1, sides + 1)]
    return frequencies


def roll_histogram(frequencies, sides=6):
    """Create a histogram for a given number of rolls"""
    title = f"Results of Rolling One D{sides} {sum(frequencies):,} Times"
    labels = {"x": "Result", "y": "Frequency of Result"}
    fig = px.bar(x=range(1, sides + 1), y=frequencies, title=title, labels=labels)
    fig.show()
