# Tuples - Tuples are similar to list, but only difference is that we cannot modify it:(mutable = can be modified and immutable = can not be modified)

#Immutable

tuple_1 =('DBMS' ,'PYTHON' , 'OOPS' , 'AI, ML AND DL' , 'ADBMS')

print(tuple_1[0]) # showing the data of the zeroth index

tuple_2 = tuple_1

#tuple_2[0] = "Art" # Error : Tuple object does not support item assignment.

for index, items in enumerate(tuple_1 , start =1): # start = 1 putting the value of index 0 as 1 and so on
	print(f'{index} - {items}')

# Sets are values that are "unordered" and has no duplicates:

set_course = {'DBMS', "ADBMS" ,'PYTHON' , 'OOPS' , 'AI, ML AND DL' , 'ADBMS'} # set's inbuild functionality will delete the duplicate value "ADBMS

print(set_course)


# EMPTY LIST	

empty_list = []
empty_list = list()

#empty tuples

empty_tuples = ()
empty_tuples = tuple()

#empty set

empty_set = {} # This is not a empty set-- this is an empty dictionary
empty_set = set()