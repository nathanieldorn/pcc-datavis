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
    """Creaet a histogram for a given number of rolls"""
    fig = px.bar(x=range(1, sides + 1), y=frequencies)
    fig.show()
