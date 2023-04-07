# #1
# num = 0
# while num <= 10:
#     print(num)
#     num = num + 1 #or num += 1

#2
# message = "Hello"
# i = 1 #начальное значение
# while i < 6:
#     print(i, message)
#     i += 1

#3
# message = "Hello"
# i = 1 #начальное значение
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

#3
# message = "Hello"
# i = 0  # начальное значение
# while i < 6:
#     i += 1
#     if i == 3:
#         continue  #skip 3
#     print(i, message)


#4
#
# i = 0
# x = 0
# while i < 5:
#     print(i)
#     x += i
#     i += 1
#     print(f"x={x}, i = {i}")

    #while - we need conditions, for we dont need conditions


text = int(input('Введите число: '))
count = 0
while text != 'stop':
    num = int(text) #число переводит в строку потому что инпут всегда строка
    count += num #прибавляем
    text = input('Для продолжения введите число, если не хотите, то введите stop ')
print(f"Сумма чисел равна {count}")