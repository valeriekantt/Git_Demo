

my_list = [1, 'hello', 2.0, True, None, 1, 1]

sentence = "Python is awesome!"
print(sentence.split(' ', maxsplit=20))

print(my_list[0])
print(my_list[-1])

#########################


print('Before ', my_list)
my_list[0]=25   #меняет значение первого элемента
print('After ', my_list)


#######################


print(id(my_list))

my_list.append(sentence)  #добавляет элемент
print(my_list)

print(len(my_list))  #count the elements

my_list.insert(0, sentence)

print(my_list.count(1))  #считает сколько элементов 1  (тру идет как один)

###################

my_list1 = [1, 2, 3, 4, 5]
print(sum(my_list1))
print(max(my_list1))
print(min(my_list1))


###########################


my_list1 = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
print(my_list1[-1][1])   #сначала указываем список с конца, потом индекс цифры/элемента внутри списка


#####################

my_list.reverse()
print(my_list)

############################


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num*2)   #or num**2 - возводит в квадрат

############################
    
numbers = [1, 2, 3, 4, 5]
new_example = [i*i for i in numbers if i%2]       #умножь переменную на переменную для каждой перемнной в списке,
                                                  #если наша переменная является нечетной


#we can sort lists by SORT and SORTED (id the same and id is not the same)