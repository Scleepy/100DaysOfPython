import math

def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil((height * width) / cover)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(test_h, test_w, coverage)
