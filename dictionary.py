
#
# my_dictionary = {}
# print(type(my_dictionary))

#############################


my_dictionary = {
    'name': 'Anna',
    'last_name': 'Smith',
    'age': '30',
    'department': 'IT'
}
print(my_dictionary)
print(my_dictionary['department'])

#######################


my_dictionary = {
    'name': 'Anna',
    'last_name': 'Smith',
    'age': '30',
    'department': 'IT'
}
print(my_dictionary)
my_dictionary['last_name'] = 'Johns'
print(my_dictionary)
print(id(my_dictionary))


###############################################



my_dictionary = {
    'name': 'Anna',
    'last_name': 'Smith',
    'age': '30',
    'department': 'IT'
}
print(my_dictionary)
my_dictionary['salary'] = '5000'
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
print(my_dictionary.pop('salary', 'Not found'))  #delete key

####################################

#to create dictionaries

keys = ['name', 'salary', 'dept']
values = ['Alex', '5000', 'HR']
employee = dict(zip(keys, values))
print(employee)

#or

employee1 = dict(name='Alex', salary='5000', position='HR')