nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4},'g':5,'f':9}

flat = {}
for k1, v1 in nested_dict.items():
    if type(v1) is not dict:
        flat[k1] = v1
    else:
        for k2, v2 in v1.items():
            flat[k2] = v2

print(flat)