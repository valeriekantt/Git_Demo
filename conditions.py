
#
# x, y = 45, 50
# s = x if x > y else y
# print(s)

#OR we can write like this

# x, y = 45, 50
# if x > y:
#     print(x)
# else:
#     print(y)

value = 6
match value:       #команда - смотри, даю значение 2 - оно мечется в первом кейсе, а во втором, в третье? то напиши 2 если мечается
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case 4:
        print(4)
    case 5:
        print(5)
    case _:
        print('Такой цифры нет')