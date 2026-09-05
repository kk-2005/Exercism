def is_valid_triangle(sides):
    """Checks if the sides can form a valid, non-degenerate triangle."""
    a, b, c = sorted(sides)
    return a > 0 and (a + b > c)

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or c == a

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return not isosceles(sides)
