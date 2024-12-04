d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


filtered = {}

for k, v in d.items():
    if v >= 3:
       filtered[k]= v

print(filtered)