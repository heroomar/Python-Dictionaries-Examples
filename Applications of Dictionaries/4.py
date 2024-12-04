d = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
unique = {}
for k, v in d.items():
    unique[v] = k
d = {}
for k, v in unique.items():
    d[v] = k
print(d)