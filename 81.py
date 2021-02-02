import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} can of paint.")


test_h = int(input("Height: "))
test_w = int(input("Width: "))
coverage = 5
paint_calc(height = test_h, width=test_w, cover=coverage)
