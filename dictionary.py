# Dictionary

student = {'name': 'John', 'age':25,'course':['maths','comSci','hindi','english']}

student['phone'] = '19216842'


student.update({'name':'swapnil k dwivedi' , "age": 28})  # to update the values of existing data
print(student)

del student['course']

# del -- just deletes the value but "pop" --- method not only delete the value but also returns the deleted value:

age = student.pop('age') # value of poped key is stored in age:

print(age)

print(student)

#in order to see all the keys we can just do the below thing:
print(student.keys())

# to see all the values we can just:
print(student.values())

# when there is nothing in the dictionary it will give none on the other hand this will give 
print(student.get('name'))

for key,value in student.items():
	print(key,value)

# student.items() will return the key value pair:

print(student.items())  #dict_items([('name', 'swapnil k dwivedi'), ('phone', '19216842')])
