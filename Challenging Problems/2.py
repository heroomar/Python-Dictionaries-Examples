n = int(input("Enter a number: "))
cubes = {5}
for i in range(1, n+1):
    cubes[i] = i**3
print(cubes)