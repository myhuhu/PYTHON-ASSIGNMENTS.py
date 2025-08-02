import math

class Circle:
    def __init__(self, radius):
        """
        Initialize the Circle with a given radius.
        """
        self.radius = radius

    def getArea(self):
        """
        Calculate and return the area of the circle.
        Formula: Area = π * r^2
        """
        return math.pi * self.radius ** 2

    def getCircumference(self):
        """
        Calculate and return the circumference of the circle.
        Formula: Circumference = 2 * π * r
        """
        return 2 * math.pi * self.radius


# Example usage:
if __name__ == "__main__":
    # Create a Circle object with radius 5
    my_circle = Circle(5)

    # Get and print area and circumference
    print(f"Area: {my_circle.getArea():.2f}")
    print(f"Circumference: {my_circle.getCircumference():.2f}")
