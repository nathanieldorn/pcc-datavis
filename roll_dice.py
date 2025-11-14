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
    results_first = roll(sides, rolls)
    results_second = roll(sides, rolls)
    results_sum = []
    for i in range(0, len(results_first)):
        results_sum.append(results_first[i] + results_second[i])

    # create list of result frequencies
    frequencies = [results_sum.count(value) for value in range(2, (sides + 1) * 2)]
    return frequencies


def roll_histogram(frequencies, sides=6):
    """Create a histogram for a given number of rolls"""
    title = f"Results of Rolling Two D{sides} {sum(frequencies):,} Times"
    labels = {"x": "Result", "y": "Frequency of Result"}
    fig = px.bar(x=range(2, (sides + 1) * 2), y=frequencies, title=title, labels=labels)
    fig.update_layout(xaxis_dtick=1)
    fig.write_html(f"dice_histogram_d{sides}")
    fig.show()
