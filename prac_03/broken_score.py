"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = input_score()
    if 0 > score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def input_score():
    score = float(input("Enter score: "))
    return score


main()
