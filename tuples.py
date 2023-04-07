

my_tuple = 1, 2, 3
print(my_tuple)
print(type(my_tuple))

###################################

my_tuple = [1, 'hello', 2.0, True, None, 1, 1]
print(my_tuple)

#####################

my_tuple = ('apple', 'banana', 'orange')
a, b, c = my_tuple
print(a)
print(b)
print(c)

##############

#tuple - нельзя заменять индексы, как мы это делали с листом/списком
#но мы можем изменить ее если поменяем tuple for list

changed_tuple = list(my_tuple)
changed_tuple[0] = 'avocado'
print(changed_tuple)      #и потом можем снова поменять на tuple

##################

print(f'Sum is: {sum(result)}')
print(f'Max is: {max(result)}')
print(f'Min is: {min(result)}')
print(f'Length of my tuple is: {sum(result)}')
print(f'Length of result is: {sum(result)}')


#################################

my_tuple = [1, 'name', None, 'name', 'name', 25]
result = tuple([item for item in my_tuple if isinstance(item, int)])
print(result)

#################

i = 0
while i < len(my_tuple):
    print(i, my_tuple)
    i += 1

###################

#nested list in tuple

fruits = ('apple', ['pineapple', 'mango'], 'watermelon')
fruits[1][0] = 'cherry'
print(fruits)
#несмотря на то что тюпл не изменяется, мы можем менять значение во вложенном листе

################

a = 5
b = 10
a, b = b, a
print(f'a= {a}')
print(f'b= {b}')

#########################

def func(*args):
    l = []
    print(len(args))
    for item in args:
        l.append(item*item)
    return l
print(func(2, 5, 6, 8, 10))