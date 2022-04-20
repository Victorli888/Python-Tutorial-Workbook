"""
Practice Problems from the Slither into Python Tutorial Workbook
Question 1: Is the ** (power) operator left or right associative?
Question 2: Is the % operator left or right associative?
Question 3: Where in the precedence hierarchy do ** and % appear?
Question 4: How are the following expressions evaluated?
    4(a) 1 + 4 - 5 * 7 // 3
    4(b) 2 ** 3 * 4 + 8 // 3
    4(c) 4 % 3 ** 5 - 2 ** 2
Question 5: From the following list of integer expressions, which expression(s) have invalid syntax?
    5(a) ((4 * 6 - (4 // 2))
    5(b) 9 * - 11 + 6
    5(c) 6 - +4

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Question 1: ** operator is right (right to left) associative, meaning 2**3**2 = 512 not 81.
2**3**2 >> 2**9 >> 512 (CORRECT)
2**3**2 >> 9**2 >> 81  (WRONG)

Question 2: % is left associative (left to right)

Question 3: The power (**) operator appears at the top of the precedence hierarchy.
The modulo (%) operator appears at the same level as multiplication and division operators.

Question 4:
a) -6
b) 34
c) 0

Question 5:
a) Invalid >> there is an extra parenthesis
b) Valid
c) Valid  >> 6 ------- ++++++4 Works too (doesn't mean you should do it though)
"""

