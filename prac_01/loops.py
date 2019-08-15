for i in range(1, 21, 2):
    print(i, end=' ')
print()
print()

print("a)")
for i in range(0, 101, 10):
    print(i, end=' ')
print()
print()

print("b)")
for i in range(0, 20):
    j = 20 - i
    print(j, end=' ')
print()
print()

print("c)")
number_of_stars = input("Number of stars?: ")

for i in range(0, int(number_of_stars)):
    print("*", end='')
print()
print()

print("d)")
for i in range(0, int(number_of_stars)):
    for j in range(0, i + 1):
        print("*", end='')
    print()




