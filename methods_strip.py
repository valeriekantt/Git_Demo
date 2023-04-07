

# w = 'Барт Симпсон Гомерович'
# w1 = 'one% two% three% four% five%'


# w3 = '      hello       '
# print(w3)
# print(w3.strip())   #delete all spaces

# w3 = '%%%hello%%%'
# print(w3)
# print(w3.strip('%'))   #delete all %%

w3 = '%%%hello%%%'
print(w3)
print(w3.strip().strip('%'))   #delete all spaces and then all %