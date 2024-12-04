dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
for i in dict2:
    dict1[i] = dict2[i]
print(dict1)