from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        # set direction and distance list
        # 15-4
        self.direction = [1, -1]
        self.distance = list(range(0, 9))

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go in the direction
            x_step = self._get_step()
            y_step = self._get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # 15-5
    def _get_step(self):
        """Counts a step for axis"""
        direction = choice(self.direction)
        distance = choice(self.distance)
        step = direction * distance

        return step
