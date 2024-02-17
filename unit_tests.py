from skeleton import VectorCore

vcore = VectorCore()

# Test Case 1: Adding two vectors of the same length
v1 = [1, 2, 3]
v2 = [4, 5, 6]
expected_output = [5, 7, 9]
assert vcore.addv_(v1, v2) == expected_output
print("Test Case 1: Adding two vectors of same length - Passed")

v1 = [1, 2, 3]
scalar = 5
expected_output = [6, 7, 8]
assert vcore.addv_(v1, scalar) == expected_output

print("Test Case 2: Adding a vector and a scalar - Passed")

v1 = []
v2 = []
expected_output = []
assert vcore.addv_(v1, v2) == expected_output

print("Test Case 3: Adding two empty vectors - Passed")

v1 = [1, 2, 3]
v2 = [4, 5, 6]
expected_output = [-3, -3, -3]
assert vcore.subv_(v1, v2) == expected_output
print("Test Case 4: Subtracting two vectors of the same length - Passed")


v1 = [1, 2, 3]
scalar = 5
expected_output = [-4, -3, -2]
assert vcore.subv_(v1, scalar) == expected_output
print("Test Case 5: Subtracting a vector and a scalar - Passed")

v1 = []
v2 = []
expected_output = []
assert vcore.subv_(v1, v2) == expected_output
print("Test Case 6: Subtracting two empty vectors - Passed")


# Test Case 7: Multiplying two vectors of the same length
v1 = [1, 2, 3]
v2 = [4, 5, 6]
expected_output = [4, 10, 18]
assert vcore.mulv_(v1, v2) == expected_output
print("Test case 7: Multiplying two vectors of the same length - Passed")

# Test Case 8: Multiplying a vector and a scalar
v1 = [1, 2, 3]
scalar = 5
expected_output = [5, 10, 15]
assert vcore.mulv_(v1, scalar) == expected_output
print("Test case 8: Multiplying a vector and a scalar - Passed")

# Test Case 9: Multiplying two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.mulv_(v1, v2) == expected_output
print("Test case 9: Multiplying two empty vectors - Passed")

# Test Case 10: Dividing two vectors of the same length
v1 = [6, 12, 18]
v2 = [2, 3, 6]
expected_output = [3, 4, 3]
assert vcore.divv_(v1, v2) == expected_output
print("Test case 10: Dividing two vectors of the same length - Passed")

# Test Case 11: Dividing a vector by a scalar
v1 = [10, 20, 30]
scalar = 5
expected_output = [2, 4, 6]
assert vcore.divv_(v1, scalar) == expected_output
print("Test case 11: Dividing a vector by a scalar - Passed")

# Test Case 12: Dividing two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.divv_(v1, v2) == expected_output
print("Test case 12: Dividing two empty vectors - Passed")

# Test Case 13: Testing equality between two vectors of the same length
v1 = [1, 2, 3]
v2 = [1, 2, 4]
expected_output = [True, True, False]
assert vcore.EQ(v1, v2) == expected_output
print("Test case 13: Testing equality between two vectors of the same length - Passed")

# Test Case 14: Testing equality between a vector and a scalar
v1 = [1, 2, 3]
scalar = 3
expected_output = [False, False, True]
assert vcore.EQ(v1, scalar) == expected_output
print("Test case 14: Testing equality between a vector and a scalar - Passed")

# Test Case 15: Testing equality between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.EQ(v1, v2) == expected_output
print("Test case 15: Testing equality between two empty vectors - Passed")

v1 = [1, 2, 3]
v2 = [4, 2, 6]
expected_output = [True, False, True]
assert vcore.NE(v1, v2) == expected_output
print("Test case 16: Testing inequality between two vectors of the same length - Passed")

# Test Case 17: Testing inequality between a vector and a scalar
v1 = [1, 2, 3]
scalar = 3
expected_output = [True, True, False]
assert vcore.NE(v1, scalar) == expected_output
print("Test case 17: Testing inequality between a vector and a scalar - Passed")

# Test Case 18: Testing inequality between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.NE(v1, v2) == expected_output
print("Test case 18: Testing inequality between two empty vectors - Passed")

# Test Case 19: Testing greater than comparison between two vectors of the same length
v1 = [1, 10, 15, 19]
v2 = [3, 10, 12, 1]
expected_output = [False, False, True, True]
assert vcore.GT(v1, v2) == expected_output
print("Test case 19: Testing greater than comparison between two vectors of the same length - Passed")

# Test Case 20: Testing greater than comparison between a vector and a scalar
v1 = [5, 10, 15]
scalar = 10
expected_output = [False, False, True]
assert vcore.GT(v1, scalar) == expected_output
print("Test case 20: Testing greater than comparison between a vector and a scalar - Passed")

# Test Case 21: Testing greater than comparison between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.GT(v1, v2) == expected_output
print("Test case 21: Testing greater than comparison between two empty vectors - Passed")

# Test Case 22: Testing greater than or equal comparison between two vectors of the same length
v1 = [5, 10, 15]
v2 = [3, 12, 15]
expected_output = [True, False, True]
assert vcore.GE(v1, v2) == expected_output
print("Test case 22: Testing greater than or equal comparison between two vectors of the same length - Passed")

# Test Case 23: Testing greater than or equal comparison between a vector and a scalar
v1 = [5, 10, 15]
scalar = 10
expected_output = [False, True, True]
assert vcore.GE(v1, scalar) == expected_output
print("Test case 23: Testing greater than or equal comparison between a vector and a scalar - Passed")

# Test Case 24: Testing greater than or equal comparison between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.GE(v1, v2) == expected_output
print("Test case 24: Testing greater than or equal comparison between two empty vectors - Passed")


# Test Case 25: Testing less than comparison between two vectors of the same length
v1 = [3, 8, 12, 1]
v2 = [5, 8, 15, 0]
expected_output = [True, False, True, False]
assert vcore.LT(v1, v2) == expected_output
print("Test case 25: Testing less than comparison between two vectors of the same length - Passed")

# Test Case 26: Testing less than comparison between a vector and a scalar
v1 = [5, 10, 15]
scalar = 10
expected_output = [True, False, False]
assert vcore.LT(v1, scalar) == expected_output
print("Test case 26: Testing less than comparison between a vector and a scalar - Passed")

# Test Case 27: Testing less than comparison between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.LT(v1, v2) == expected_output
print("Test case 27: Testing less than comparison between two empty vectors - Passed")

# Test Case 28: Testing less than or equal comparison between two vectors of the same length
v1 = [3, 8, 15, 1]
v2 = [5, 8, 15, 0]
expected_output = [True, True, True, False]
assert vcore.LE(v1, v2) == expected_output
print("Test case 28: Testing less than or equal comparison between two vectors of the same length - Passed")

# Test Case 29: Testing less than or equal comparison between a vector and a scalar
v1 = [5, 10, 15]
scalar = 10
expected_output = [True, True, False]
assert vcore.LE(v1, scalar) == expected_output
print("Test case 29: Testing less than or equal comparison between a vector and a scalar - Passed")

# Test Case 30: Testing less than or equal comparison between two empty vectors
v1 = []
v2 = []
expected_output = []
assert vcore.LE(v1, v2) == expected_output
print("Test case 30: Testing less than or equal comparison between two empty vectors - Passed")

# Test Case 31: Unpacking lower halves of v2 and v3 into v1
v1 = [0, 0, 0, 0]  # Initialized with zeroes
v2 = [1, 2, 3, 4]   # v2 lower half [1, 2]
v3 = [5, 6, 7, 8]   # v3 lower half [5, 6]
expected_output = [1, 5, 2, 6]  # Expected result after unpacking lower halves of v2 and v3 into v1
vcore.UNPACKLO(v1, v2, v3)
assert v1 == expected_output
print("Test case 31: Unpacking lower halves of v2 and v3 into v1 - Passed")

# Test Case 32: Unpacking upper halves of v2 and v3 into v1 with interleaving
v1 = [0, 0, 0, 0]  # Initialized with zeroes
v2 = [1, 2, 3, 4]   # v2 upper half [3, 4]
v3 = [5, 6, 7, 8]   # v3 upper half [7, 8]
expected_output = [3, 7, 4, 8]  # Expected result after interleaving upper halves of v2 and v3 into v1
vcore.UNPACKHI(v1, v2, v3)
assert v1 == expected_output
print("Test case 32: Unpacking upper halves of v2 and v3 into v1 with interleaving - Passed")

# Test Case 33: Packing even elements of v2 and v3 into v1 (PACKLO)
v1 = [0, 0, 0, 0]  # Initialized with zeroes
v2 = [1, 2, 3, 4]   # v2 even elements [1, 3]
v3 = [5, 6, 7, 8]   # v3 even elements [5, 7]
expected_output = [1, 3, 5, 7]  # Expected result after packing even elements of v2 and v3 into v1 (PACKLO)
vcore.PACKLO(v1, v2, v3)
assert v1 == expected_output
print("Test case 33: Packing even elements of v2 and v3 into v1 (PACKLO) - Passed")

# Test Case 34: Packing odd elements of v2 and v3 into v1 (PACKHI)
v1 = [0, 0, 0, 0]  # Initialized with zeroes
v2 = [1, 2, 3, 4]   # v2 odd elements [2, 4]
v3 = [5, 6, 7, 8]   # v3 odd elements [6, 8]
expected_output = [2, 4, 6, 8]  # Expected result after packing odd elements of v2 and v3 into v1 (PACKHI)
vcore.PACKHI(v1, v2, v3)
assert v1 == expected_output
print("Test case 34: Packing odd elements of v2 and v3 into v1 (PACKHI) - Passed")

'''
Write test cases for LV, SV, etc.

Write test cases for scalars
'''

print()