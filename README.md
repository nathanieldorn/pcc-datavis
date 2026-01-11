# A Basic Data Visualization Project with Matplotlib and Plotly
Inspired by the data visualization projects in Python Crash Course, 3rd edition.

To create visuals, remove comments from the desired function calls in main.py. Only one may be run at a time.

## Squares
Create either a line or dot plot of the square of numbers. 
### Line Plot (squared_num_line)
The array, input_values, contains the integers, one through eight, to be squared and plotted. The function call will only display the result.
### Dot Plot (squared_num_points)
The array, x_values, represents the integers to be squared and is created using a list comprehension. It's counterpart list, y_values, uses list comprehension to calculate the square. The function call will both display and save a file of the result.

## Random Walks
Creates a scatter plot of a random walk from a starting cartesian position of (0, 0). The plot shades from white to green with both the start and end points highlighted in orange. Each step is randomly chosen within a defined range. When run, the user will be prompted to save the output or not, after which the result will be displayed via pyplot. 

A sample output:
![Random Walk Plot](https://github.com/nathanieldorn/pcc-datavis/blob/main/random_walk_100k.png)
