

number = int(input('Введите число: '))
if number < 10:
    print('Однозначное число')
elif 10 <= number <= 99:
    print('Двузначное число')
elif 100 <= number <= 999:
    print('Трехзначное число')
else:
    print('Мы это еще не проходили')