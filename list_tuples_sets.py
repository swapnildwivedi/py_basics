courses = ['history' , 'maths' , 'physics' , 'Comp Sci']

print(courses[0]) #value of the list since the first value is at index 0
print(len(courses)) # len() method to find the length of the list/string

#slicing the list in python:

print(courses[0:3]) # Here we are slicing the list from index 0 to 2 (3 is not included)

print(courses)

courses.append('PSIR') # PSIR is added to the courses

print(courses) # ['history', 'maths', 'physics', 'Comp Sci', 'PSIR']

courses.insert(1 , 'civics')  # The insert() method in Python is used to insert an element at a specified position in a list.
                  # Unlike the append() method, which adds an element to the end of the list,
                  # insert() allows you to add an element at any position.

print(courses) # ['history', 'civics', 'maths', 'physics', 'Comp Sci', 'PSIR']

# You could also append a list inside a list in python

courses.append(['DSA' , 'Mechine Learning' , 'Oops']) #You can just directly put a list inside a append method in python

# Or you could do it as well: 
courses_2 = ['data science', 'artificial intelligence', 'data science']
courses.append(courses_2) 
print(courses) # output is ::  ['history', 'civics', 'maths', 'physics', 'Comp Sci', 'PSIR', ['DSA', 'Mechine Learning', 'Oops'], ['data science', 'artificial intelligence', 'data science']]

courses.remove('maths') # remove() method takes the element of the list as an argument and remove that perticular element from the list

courses_2.pop() # pop() method does not take any argument and it removes the last element from the list
courses.pop()
print(courses)


# there is a sort() method to sort the list in the alphabetical order and reverse() method to reverse a list 


nums = [1,5,4,9,3]

nums.sort()

print(nums)
#to sort the list in decending order
nums.sort(reverse = True)

print(nums)
#nums.sort() (In-Place Sorting)
#Yeh function original list ke andar hi changes kar deta hai. Yeh koi nayi list bana kar return nahi karta, bas aapki maujooda list ko order me set kar deta hai. Iska return type Python me None rakha gaya hai taaki aapko pata chale ki list modify ho chuki hai.



#sorted(nums) (Returns New List)
#Agar aap chahte ho ki aapko ek nayi sorted list mile aur original list jaisi hai waise hi rahe, toh aapko Built-in sorted() function use karna chahiye:
#List, Tuple, String, Dictionary sab par chalta hai

#------------------->

#Python ki philosophy hai ki jo functions original object ko directly change (mutate) karte hain, unka return value mostly None hota hai (jaise .append(), .extend(), .reverse()).

print(min(nums)) # returns the minimum value of the list
print(max(nums)) # returns the maximum value of the list
print(sum(nums)) # returns the sum of all the values of the list

print(courses.index('PSIR')) # It returns the index value of the perticular value of the list that you pass into the function

# Now we'll see how to loop through the items of the list in python


for items in courses:
	print(items) #all the items are coming here one by one.

# if we want value as well as index of that perticular value then we'll use enumerate() method and pass the list inside it as an argument

for index , items in enumerate(courses):   # We can also do enumerate(courses , start = 1) with this insted if giving the value of index = 0 it will give 1 (It dosent mean that loop will start from index 1)
	print(f'item = {items} is at the {index} index')

# Tuples - Tuples are similar to list, but only difference is that we cannot modify it:(mutable = can be modified and immutable = can not be modified)
