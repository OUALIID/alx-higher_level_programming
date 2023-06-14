#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtr = [row[:] for row in matrix]
    for i in range(len(mtr)):
        for j in range(len(mtr[i])):
            mtr[i][j] = mtr[i][j] ** 2
    return mtr
