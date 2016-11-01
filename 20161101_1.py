def col_op(ma, a, b):
    temp = ma[0][a]
    ma[0][a] = ma[0][b]
    ma[0][b] = temp

    for i in range(7):
        temp = ma[2][i][a]
        ma[2][i][a] = ma[2][i][b]
        ma[2][i][b] = temp

    return ma
def row_op(ma, a, b):
    temp = ma[1][a]
    ma[1][a] = ma[1][b]
    ma[1][b] = temp

    r = [0, 1, 2 ,3 ,4 ,5, 6]

    temp = r[a]
    r[a] = r[b]
    r[b] = temp

    new_ma_cell = []

    for i in r:
        new_ma_cell.append(ma[2][i])