'''
for itr in range(0,10):
	print(itr)

'''
'''
#loop range(5) ki bjh se 0-4 tak chalega 5 include nahi hoga:
for i in range(5):
	print(i)
'''
'''
# loop 1-5 chalega 6 include nahi hoga isme :

for i in range(1,6):
	print(i)
'''

'''
#List par loop chalane ke liye:

computer = ['keyboard' , 'mouse' , 'monitor' , 'cpu' , 'printer' , 'lightpen']

for comp in computer:
	print(comp)

'''

# break : jab aapko loop beech me hi poora band karna ho:
# continue : jab aapko current cycle ko skip krke agli cycle par jaana ho:

num_list = [1,2,3,4,5,6,7,8,9]

for num in num_list:
	#print(num)

	if num == 3:
		print(f"We have reached {num} we are skipping it:")
		continue

	if num == 7:
		print(f"We have reached {num} now we are breaking it:")
		break
	print(num)


# While_loop in python:

'''
		Difference in for loop and while loop:

			for loop fixed number of iterations ke liye chalta hai.

			where as while loop jab tak chalta hai jab tak condition true hai(aapko bhi nahi pata hota kitne baar chalega)
			bas condition jab tak true rahegi while loop chalta rahega
'''

iterator = 6

while iterator >= 2:
	print(f"We are inside the while loop {iterator}")
	iterator-=1

