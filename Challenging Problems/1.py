dict1 = {'a': 5, 'b': 10,'c': 17}
dict2 = {'a': 3, 'b': 7}
result = {}
for k in dict1:
    print(k)
    if k in dict2.keys():
        result[k] = dict1[k] + dict2[k]

print(result)