
#Set Methods

my_list = [1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 9]
print(set(my_list))  #delete duplicates


set1 = {1, 2, 3, 'one', 'ten', 20}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
set3 = {1, 2, 3}

print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))


################

fs = frozenset({1, 2, 3})
print(fs)
fs.remove(10)