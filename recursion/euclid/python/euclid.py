#!/bin/python

# Divide a rectangle into a set of squares with the largest size possible.
# The squares must fill the entire area and be a uniform size.
def euclid(width: int, height: int):
    ### Base Cases
    if width == 0:
        return (height, height)
    elif height == 0:
        return (width, width)
    elif width == height:
        return (width, height)


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

# Expect (50, 50)
print(euclid(50, 50))
print(euclid(100, 50))
print(euclid(150, 50))
print(euclid(50, 150))
print(euclid(250, 150))

# Expect (10, 10)
print(euclid(10, 100))
print(euclid(100, 10))

# Expect (1, 1)
print(euclid(3, 5))

