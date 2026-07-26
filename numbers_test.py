num = 3

print(type(num)) #This type() function shows the datatype of the object  OUTPUT:: <class 'int'>

float_num = 3.14

print(type(float_num)) # now it is showing that the datatype is float OUTPUT:: <class 'float'>

# =====================================================================
# PYTHON ARITHMETIC OPERATORS (In Order of Evaluation Precedence)
# =====================================================================
#
#  1. Exponentiation / Power:
#     **  -> Raises a number to the power of another   (x ** y)   --->> that means x base to the power y
#
#  2. Multiplication, Division, Floor Division, Modulus:
#     *   -> Multiplies two values                     (x * y)
#     /   -> Divides and returns a float               (x / y)
#     //  -> Divides and returns the floor (integer)   (x // y)    (if x/y returns 1.5 then x//y returns 1)
#     %   -> Modulus (returns the remainder)          (x % y)
#
#  3. Addition & Subtraction:
#     +   -> Adds two values                           (x + y)
#     -   -> Subtracts one value from another          (x - y)
#
# =====================================================================


print(3/2) #output: 1.5

print(3//2) #output: 1

print(3*2+1) # this will do 3*2 first then it will add 1

print(3*(2+1)) #this will first solve the paranthesis and then multiply the result by 3

print(abs(-2)) # it will show the absolute value of the argument given to abs() method in short it will remove the
			   # negative sign

print(round(3.75))# it will round the value to the nearest integer value

# =====================================================================
# PYTHON COMPARISON (RELATIONAL) OPERATORS
# Returns True or False depending on whether the condition is met.
# =====================================================================
#
#  1. Equal to:
#     ==  -> Returns True if both values are equal          (x == y)
#
#  2. Not Equal to:
#     !=  -> Returns True if values are NOT equal          (x != y)
#
#  3. Greater than:
#     >   -> Returns True if x is greater than y            (x > y)
#
#  4. Less than:
#     <   -> Returns True if x is less than y               (x < y)
#
#  5. Greater than or Equal to:
#     >=  -> Returns True if x is greater than or equal y   (x >= y)
#
#  6. Less than or Equal to:
#     <=  -> Returns True if x is less than or equal y      (x <= y)
#
# =====================================================================

marks_a = 50
marks_b = 45

print(marks_a == marks_b) # returns boolean value -->> False
print(marks_a != marks_b) # returns boolean value -->> True
