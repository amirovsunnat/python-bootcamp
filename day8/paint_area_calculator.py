import math


def paint_calculator(height, width, cover):
    area = height * width
    cans = area / cover
    return math.ceil(cans)


height = float(input("Enter the height of the wall: "))  # Height of wall (m)
width = float(input("Enter the width of the wall: "))  # Width of wall (m)
coverage = 5
cans_count = paint_calculator(height=height, width=width, cover=coverage)
print(f"You'll need {cans_count} cans of paint.")
