import unittest
import math


def find_side(width, height, number):
    total_area = width * height * number
    square = math.ceil(math.sqrt(total_area))
    # max_in_row = square // width
    # max_in_column = square // height
    # max_all = max_in_column * max_in_row
    # middle = (square + total_area + 1) / 2
    # if max_all >= number:
    #     return square
    # else:
    #     while True:
    #         new_square = middle
    #         max_in_row = new_square / width
    #         max_in_column = new_square / height
    #         max_all = max_in_column * max_in_row
    #         if max_all > number:
    #             middle = (square + new_square) / 2
    #         elif max_all < number:
    #             middle = (new_square + total_area + 1) / 2
    #         else:
    #             return math.ceil(new_square)
    for side in range(square, total_area + 1):
        max_in_row = side // width
        max_in_column = side // height
        max_all = max_in_column * max_in_row
        if number <= max_all:
            return side


#class Testing(unittest.TestCase):
    #def test_1(self):
        #self.assertEqual(find_side(3, 2, 10), 9)

    #def test_2(self):
        #self.assertEqual(find_side(1000000000, 999999999, 2), 1999999998)

    #def test_3(self):
        #self.assertEqual(find_side(1, 1, 4), 2)

if __name__ == "__main__":
    print(find_side(3, 2, 10))
