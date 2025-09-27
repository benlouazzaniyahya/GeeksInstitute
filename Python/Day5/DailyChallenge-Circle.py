
import math
import turtle
from typing import List

class Circle:
    def __init__(self, radius: float = None, diameter: float = None):
        if radius is not None:
            self.radius = float(radius)
        elif diameter is not None:
            self.radius = float(diameter) / 2.0
        else:
            raise ValueError("Circle requires either radius or diameter.")

        if self.radius < 0:
            raise ValueError("Radius cannot be negative.")

    @property
    def diameter(self) -> float:
        return self.radius * 2.0

    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def __repr__(self) -> str:
        # concise unambiguous representation
        return f"Circle(radius={self.radius:.3f})"

    def __str__(self) -> str:
        # user-friendly string with area rounded
        return (f"Circle(radius={self.radius}, diameter={self.diameter}, "
                f"area={self.area:.3f})")

    # Add two circles -> new Circle with summed radius
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    # Comparisons by radius. Return NotImplemented when other type doesn't match
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            # consider exact equality of radii; if you want tolerance use math.isclose
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented


# ---------- Turtle Drawing Utilities ----------
def draw_sorted_circles(circle_list: List[Circle], spacing: float = 20.0):
    """
    Draws the circles from circle_list (assumed sorted by radius ascending).
    Places them along the x-axis with spacing to avoid overlap.
    spacing: extra space (pixels) added between adjacent circles.
    """
    if not circle_list:
        print("No circles to draw.")
        return

    screen = turtle.Screen()
    screen.title("Sorted Circles")
    # Optionally set a larger canvas size if needed:
    # screen.setup(width=1200, height=600)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    # color palette to cycle through
    colors = ["red", "green", "blue", "orange", "purple", "brown", "cyan", "magenta"]

    # compute starting x so the group is roughly centered
    # We'll place circles left-to-right, stacking centers horizontally:
    total_width = 0.0
    radii = [c.radius for c in circle_list]
    for r in radii:
        total_width += (2 * r) + spacing
    total_width -= spacing  # last one doesn't need extra spacing

    start_x = -total_width / 2.0

    x = start_x
    for i, c in enumerate(circle_list):
        col = colors[i % len(colors)]
        t.penup()
        # move to center x, and move down by radius to start drawing circle from correct baseline
        center_x = x + c.radius
        t.goto(center_x, 0)          # center at y=0
        t.setheading(0)
        t.forward(0)  # no-op but keeps clarity
        t.right(90)
        t.forward(c.radius)          # move down to the starting point of turtle.circle
        t.left(90)

        t.pendown()
        t.color(col)
        # draw filled circle
        t.begin_fill()
        t.circle(c.radius)
        t.end_fill()
        t.penup()

        # draw a small label above the circle with radius value
        t.goto(center_x, c.radius + 10)
        t.write(f"r={c.radius}", align="center", font=("Arial", 10, "normal"))

        # move x forward by diameter + spacing for next circle
        x += (2 * c.radius) + spacing

        # return turtle to baseline orientation for next
        t.goto(center_x, 0)
        t.setheading(0)

    # Keep the window open until closed by the user
    turtle.done()


# ---------- Demo / Example Usage ----------
if __name__ == "__main__":
    # create a few circles in different ways
    c1 = Circle(radius=5)
    c2 = Circle(diameter=20)     # radius 10
    c3 = Circle(radius=2.5)
    c4 = Circle(diameter=15)     # radius 7.5
    c5 = Circle(radius=12)

    print("Individual circles:")
    for c in (c1, c2, c3, c4, c5):
        print(" ", c)

    # add two circles
    c_sum = c1 + c3
    print("\nSum of c1 and c3 ->", c_sum)

    # comparisons
    print("\nComparisons:")
    print(" c1 < c2 ?", c1 < c2)
    print(" c5 > c4 ?", c5 > c4)
    print(" c2 == Circle(diameter=20) ?", c2 == Circle(diameter=20))

    # sorting
    circles = [c1, c2, c3, c4, c5, c_sum]
    print("\nUnsorted radii:", [c.radius for c in circles])
    circles.sort()  # uses __lt__
    print("Sorted radii:  ", [c.radius for c in circles])

    # Draw sorted circles with turtle (will open a window)
    print("\nOpening turtle window to draw sorted circles...")
    draw_sorted_circles(circles, spacing=20.0)
