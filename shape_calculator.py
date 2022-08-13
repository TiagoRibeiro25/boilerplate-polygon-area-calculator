class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width == 0 or self.height == 0:
            return ""
        elif self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, size):
        self.width = size
        self.height = size
