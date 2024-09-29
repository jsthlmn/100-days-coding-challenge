import math

def area_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

wall_height = int(input("Height of wall: "))
wall_width = int(input("Width of wall: "))
coverage = 5

area_calc(height=wall_height, width=wall_width, cover=coverage)