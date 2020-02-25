# -*- coding: utf-8 -*-
"""
Chih-Yu Lee
"""

def classify_triangle(side_length1, side_length2, side_length3):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if (isinstance(side_length1, str) or isinstance(side_length2, str) or isinstance(side_length3, str)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if side_length1 <= 0 or side_length2 <= 0 or side_length3 <= 0:
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_length1+side_length2 < side_length3) or\
        (side_length1+side_length3 < side_length2) or\
        (side_length2+side_length3 < side_length1):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if side_length1 == side_length2 == side_length3:
        return 'Equilateral'
    if ((side_length1 ** 2) + (side_length2 ** 2)) == (side_length3 ** 2) or\
        ((side_length1 ** 2) + (side_length3 ** 2)) == (side_length2 ** 2) or\
        ((side_length2 ** 2) + (side_length3 ** 2)) == (side_length1 ** 2):
        return 'Right'
    elif (side_length1 != side_length2) and  (side_length2 != side_length3) and (side_length1 != side_length3):
        return 'Scalene'
    return 'Isoceles'
