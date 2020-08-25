"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/grading/problem
- if the difference of the next multiple of 5 is less than 3 then round that grade up to 5
--- in other words 83 & 84 should round up to 85 and 88 & 89 should round up to 90
- if the value is less than 38 then no rounding should occur because it is a failing grade

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

test1 = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]  # Expected: [71, 72, 75, 75, 75, 76, 77, 80, 80, 80]

m = grade_curve(test1)
print(m)