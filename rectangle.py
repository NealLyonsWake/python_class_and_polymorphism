class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
        self.length = length

    def __str__(self):
        return f"Square of length: {self.length}"


rectangleOne = Rectangle(10,2)
squareOne = Square(5)
# print(squareOne.get_area())

print(squareOne)


# true or false each are a version of the other?
# print(
#     f'A rectangle is a rectangle: {isinstance(rectangleOne, Rectangle)}'
# )
# print(
#     f'A rectangle is a square: {isinstance(rectangleOne, Square)}'
# )
# print(
#     f'A square is a rectangle: {isinstance(squareOne, Rectangle)}'
# )
# print(
#     f'A square is a square: {isinstance(squareOne, Square)}'
# )







# class Cup():

#     def __init__ (self, colour, material):
#         self.colour = colour
#         self.material = material

# class WhiteCeramicCup(Cup):
    
#     def __init__(self):
#         super().__init__("white", "ceramic")