

l1 = [20, 15, 8, 7, 6]
l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
#ламбда быстрее выполняется и проще пишется -
# икс возведи в квадрат если икс - это число, в противном случае просто напищи икс
print(power)
from functools import reduce
result = reduce(lambda x, y: x*y, l1)
print(result)