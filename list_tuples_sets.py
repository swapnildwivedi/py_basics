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

#Or you could do it as well: 
courses_2 = ['data science', 'artificial intelligence', 'data science']
courses.append(courses_2) 
print(courses) # output is ::  ['history', 'civics', 'maths', 'physics', 'Comp Sci', 'PSIR', ['DSA', 'Mechine Learning', 'Oops']]

