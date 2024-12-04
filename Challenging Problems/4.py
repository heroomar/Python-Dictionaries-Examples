d = {'a': 10, 'b': 15, 'c': 8, 'd': 7}

even = {}
odd = {}

for k, v in d.items():
    if v % 2 == 0:
        even[k] = v

for k, v in d.items():
    if v % 2 != 0:
        odd[k] = v

print("Even values:", even)

print("Odd values:", odd)