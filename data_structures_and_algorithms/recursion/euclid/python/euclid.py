#!/bin/python
import unittest

# Divide a rectangle into a set of squares with the largest size possible.
# The squares must fill the entire area and be a uniform size.
def euclid(width: int, height: int):
    ### Base Cases
    if width == height:
        return width
    elif width == 0:
        return height
    elif height == 0:
        return width


    ### Recursive Cases
    # The largest square is some multiple of the smaller side
    # Find out how many squares of that side fit into the rectangle and cut out that area
    # Then solve the remaining area recursively
    elif width > height:
        width -= height*(int(width/height))
        return euclid(width, height)
    else:
        height -= width*(int(height/width))
        return euclid(width, height)


# Unit Tests
class EuclidTest(unittest.TestCase):
    def test_square_50(self):
        self.assertEqual(euclid(50, 50), 50)

    def test_rect_100_50(self):
        self.assertEqual(euclid(100, 50), 50)

    def test_rect_150_50(self):
        self.assertEqual(euclid(150, 50), 50)

    def test_rect_50_150(self):
        self.assertEqual(euclid(50, 150), 50)

    def test_rect_250_150(self):
        self.assertEqual(euclid(250, 150), 50)

    def test_rect_10_100(self):
        self.assertEqual(euclid(10, 100), 10)

    def test_rect_100_10(self):
        self.assertEqual(euclid(100, 10), 10)

    # Expect (1, 1)
    def test_rect_3_5(self):
        self.assertEqual(euclid(3, 5), 1)

