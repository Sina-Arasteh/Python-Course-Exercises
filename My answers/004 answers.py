def sum_up_diagonals(list):
    a = sum([list[i][i] for i in range(len(list))])
    b = sum([list[i][-i-1] for i in range(len(list))])
    return a + b

