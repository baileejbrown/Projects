import random

NUMBERS_PER_QUICKPICK = 6
RANGE_OF_QUICKPICK = 45

number_of_quickpicks = int(input('How many QuickPicks? '))

for i in range(0, number_of_quickpicks):

    quickpick = []
    for k in range(0, NUMBERS_PER_QUICKPICK - 1):
        number = random.randint(1, 45)

        while number in quickpick:
            number = random.randint(1, RANGE_OF_QUICKPICK)
        quickpick.append(number)

    quickpick.sort()

    for i in range(0, NUMBERS_PER_QUICKPICK - 1):
        print('{:3}'.format(quickpick[i]), end='')

    print("\n")
