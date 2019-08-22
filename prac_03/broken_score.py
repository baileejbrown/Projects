"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    grade = grade_score(score)

    print(grade)


def grade_score(score):
    if 0 > score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


main()
