import math


class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x=0, y=0):
        '''Initiliaze position of a new point. The x and y coordinates can be specified.
         If they are not, the point default to origin.'''
        self.move(x, y)

    def move(self, x, y):
        'Move the point to a new location in two-dimensional space'
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back to the geometric origin'
        self.move(0, 0)

    def calculate_distance(self,  other_point):
        """Calculate the distance from the point to a second point passed as a parametr

        This function uses the Pythagorean Thereom to calculate the distance between the two points.
        The distance is a returned as a float."""

        return math.sqrt(
            (self.x - other_point)**2 +
            (self.y - other_point)**2
        )