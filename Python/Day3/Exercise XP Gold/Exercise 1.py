import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def definition(self):
        """Print the geometrical definition of a circle."""
        print("A circle is a set of all points in a plane that are at a given distance from a fixed point, called the center.")

# Example usage:
circle = Circle(5)
print(f"Perimeter: {circle.perimeter():.2f}")
print(f"Area: {circle.area():.2f}")
circle.definition()
