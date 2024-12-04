dict1={'a': 1, 'b': 2}

if dict.get(dict1, 'c'):
    print("Key Found: ",dict.get(dict1, 'c'))
else:
    print("key not found")