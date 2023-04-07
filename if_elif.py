import sys

#1
# x = 3
#
# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than five')
# else:
#     print('Less than five')


#2
#
# age = int(input('Please, enter your age:'))
# if age >= 18:
#     print('Welcome, take a drink!')
# else: print('Go to sleep!')

#3

# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')   #delenie, umnozhenie? kakoe deistvie?
# result = num1 / num2
# print(f'Result = {result}')

#4
# num1 = 0
# num2 = 0
try:
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
except ValueError:
    print('You entered not number')
    sys.exit()
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
operator = input('Operator: ')   #delenie, umnozhenie? kakoe deistvie?

if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
        print(f'Result = {result}')                 #блоком try мы ловим эту ошибку, обозначаем ее и код двигается дальше (не падает)
    except ZeroDivisionError:                       #название ошибки пишем как он ее назвал
        print('На ноль делить нельзя!')
else:
    result = num1 * num2
    print(f'Result = {result}')  #недоработанный код - только есть деление и умножение