"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/grading/problem

My solution:        Space Complexity: O(1)      Time Complexity: O(n)
"""


def grade_curve(grades):  # input is an array
    for i in range(len(grades)):

        if grades[i] > 37:
            if (grades[i] % 5) != 0:
                if 5 - (grades[i] % 5) < 3:
                    grades[i] += 5 - (grades[i] % 5)
    return grades


#  Test input and output
if __name__ == '__main__':
    my_grades = [73, 67, 38, 33]  # expected is 75, 67, 40, 33
    curved_grades = grade_curve(my_grades)
    print(curved_grades)
