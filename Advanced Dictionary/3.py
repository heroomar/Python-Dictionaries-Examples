dict = {'a': 1, 'b': 2, 'c': 3}
reversed = {}
for k, v in {'a': 1, 'b': 2, 'c': 3}.items():
    reversed[v] = k
print(reversed)