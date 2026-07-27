#swapping of two variables using temp variable:

a = 50
b = 60

temp = a
a = b 
b = temp

print(f"these are the numbers after swapping a = {a} and b = {b}")


#swapping the numbers without using temp variable:

x = 10
y = 20

print(f'Values of x={x} and y={y} before swapping:')
x = x + y # x = 30 and y = 20
y = x - y # y = 10 and x = 30
x = x - y # y = 10 and x = 20

print(f'Values of x={x} and y={y} after swapping without using temp variable:')

#program to test whether a number is even or odd by using a input() method to take number from user:
num = int(input('Enter a number: '))

if num % 2 == 0:
	print(f"{num} is an even number")
else :
	print(f"{num} is an odd number")

# checking the sign of a number positive /negative/zero:

test_sign = int(input('enter any number here to check if its positive or negative: '))

if test_sign > 0 :
	print('Sign is positive')
elif test_sign == 0 :
	print('Oops! this seems like a trick question but the number is ZERO here.')
else:
	print('Number is negative')


	import numpy as np

print(np.sign(15))   # Output: 1
print(np.sign(-42))  # Output: -1
print(np.sign(0))    # Output: 0




