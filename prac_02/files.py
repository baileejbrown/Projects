name_file = open("name.txt", 'w')
name = input("Please enter your name: ")
print(name, file=name_file)
name_file.close()

name_file = open("name.txt", 'r')
print('Your name is {}'.format(name_file.read()))
name_file.close()

numbers_file = open('numbers.txt', 'w')
print('17', file=numbers_file)
print('42', file=numbers_file)
numbers_file.close()

numbers_file = open('numbers.txt', 'r')
number_1 = int(numbers_file.readline())
number_2 = int(numbers_file.readline())
print(number_1 + number_2)
numbers_file.close()

numbers_file = open('numbers.txt', 'r')
total = 0
for line in numbers_file:  # why does this pick the lines and not char
    number = int(line)
    total += number
print(total)
numbers_file.close()
