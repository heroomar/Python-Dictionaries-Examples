d = {'a': 10, 'b': 15, 'c': 7}
max = 0
key=None
for i in d:
    if d[i] > max:
        max = d[i]
        key=i
print("Key with max value:", key)