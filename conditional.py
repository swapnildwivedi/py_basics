a = False

if a:
	print("Its true!!!")
else : 
	print ("its false -_-")



# ==========================================
# Python Comparison Operators
# ==========================================
# ==  (Equal to)
# !=  (Not equal to)
# >   (Greater than)
# <   (Less than)
# >=  (Greater than or equal to)
# <=  (Less than or equal to)


"""
=============================================================================================
PYTHON COMPARISON OPERATORS
=============================================================================================
Operator | Description                                       | Python Code | Result
---------+---------------------------------------------------+-------------+--------
==       | Equal to: Checks if left value equals right value | 5 == 5      | True
!=       | Not equal to: Checks if left value != right value | 5 != 3      | True
>        | Greater than: Checks if left value is larger      | 10 > 7      | True
<        | Less than: Checks if left value is smaller        | 4 < 9       | True
>=       | Greater than or equal to: Larger or equal          | 5 >= 5      | True
<=       | Less than or equal to: Smaller or equal           | 3 <= 8      | True
=============================================================================================
"""


"""

this is multi lined comment in python

"""
print("hey the everyone!!!")

if a or True:   # only one needs to be true
	print("this is or condition.")

if a and True:
	print("This is the and condition and all the conditions are true")
else :
	print("All the conditions are false or one of the condition is false")

# Create two distinct lists with identical values
a = [1, 2, 3]
b = [1, 2, 3]
c = a # a is pointing c at the same address because here in python variables are assigned to the memory address

print(id(a))
print(id(b))
print(id(c))  # id of a and c is same 
print(a == b)  # True  -> Values are equal
print(a is b)  # False -> Different objects in memory

print(a is c)  # True  -> 'c' points to the exact same memory address as 'a'   this is same as id(a) == id(c)