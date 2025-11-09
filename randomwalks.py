from random import choice


class RandomWalk:
    """Creates random walks for data visualization"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # starting position of all walks
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Determine all points in a walk"""

        while len(self.x_values) < self.num_points:
            # Choose direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
