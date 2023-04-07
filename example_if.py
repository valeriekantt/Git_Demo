

# a = int(input('Введите цифру: '))
# if a % 2 == 0:  #делиться нв 2 без остатка
#     if a % 10 == 0:
#         print(f"{a} делится на 2 и на 10")
#     else:
#         print(f"{a} делится на 2, но не делится на 10")
# else:
#     print(f"{a} не делится на 2")



a = int(input('Введите вашу отметку: '))
if a >= 90:
    print(5)
elif a >= 80:
    print(4)
elif a >= 70:
    print(3)
else:
    print(2)
