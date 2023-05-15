#https://leetcode.com/problems/valid-sudoku/

"""
Problem: Determine if numbers that are already on the sodoku board are valid such that they adhere to sodoku rules.
Three things to check
1) Row
2) Column
3) Square
Don't overthink the solution, we are not solving the board we are verifying that the elements currently on the board
are valid.
"""
import collections


def using_hashsets(board):
    """
    Detecting Duplicates, it makes sense to implement a hashset solution
    :param board: Given board with numbers ( nested list)
    :return: True if numbers present in board are valid


    """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key r_idx // 3 , c_idx // 3 ie, (2,2)

    for r_idx in range(9):
        for c_idx in range(9):
            sodoku_number = board[r_idx][c_idx]
            if sodoku_number == ".":
                continue
            if (sodoku_number in rows[r_idx] or
                sodoku_number in cols[c_idx] or
                sodoku_number in squares[(r_idx // 3, c_idx // 3)]):
                return  False
            rows[r_idx].add(sodoku_number)
            cols[c_idx].add(sodoku_number)
            squares[(r_idx//3, c_idx//3)].add(sodoku_number)
    return True

