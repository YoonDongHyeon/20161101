machine_part = [
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1]
]

machine_part_ma = [['A', 'B', 'C', 'D', 'E', 'F', 'G'], [1, 2, 3, 4, 5, 6, 7], machine_part]

weight = []

for i in range(1, 8):
    weight.append(2 ** i)

def col_op(ma, a, b):
    temp = ma[0][a]
    ma[0][a] = ma[0][b]
    ma[0][b] = temp

    for i in range(7):
        temp = ma[2][i][b]
        ma[2][i][a] = ma[2][i][b]
        ma[2][i][b] = temp
    return ma

def row_op(ma, a, b):
    temp = ma[1][a]
    ma[1][a] = ma[1][b]
    ma[1][b] = temp

    r = [0, 1, 2, 3, 4, 5, 6]

    temp = r[a]
    r[a] = r[b]
    r[b] = temp

    new_ma_cell = []

    for i in r:
        new_ma_cell.append(ma[2][i])

    new_ma = [ma[0], ma[1], new_ma_cell]

    return new_ma
def my_print(ma):
    for i in range(7):
        print('\t{}'.format(ma[0][i]),end=''),
    print(' ')
    for i in range(7):
        print(ma[1][i]),
        for j in range(7):
            print('\t{}'.format(ma[2][i][j]),end=''),
        print(' ')
    return True
def col_cal(ma):
    col_sum = []
    for i in range(7):
        col_sum.append(0)

    for i in range(7):
        for j in range(7):
            col_sum[i] = col_sum[i] + ma[2][j][i] * weight[j]

    return col_sum

def row_cal(ma):
    row_sum = []
    for i in range(7):
        row_sum.append(0)

    for i in range(7):
        for j in range(7):
            row_sum[i] = row_sum[i] + ma[2][i][j] *weight[j]

    return row_sum

def gt(ma):
    re = ma
    times = 0

    while True:
        times = times +1
        axis = times %2
        changed = 0
        if axis == 0:
            csum = col_cal(re)
            for i in range(7):
                for j in range(i+1,7):
                    if csum[i] > csum[j]:
                        temp = csum[i]
                        csum[i] = csum[j]
                        csum[j] = temp
                        re = col_op(re, i , j)
                        changed = changed +1
        elif axis == 1:
            rsum = row_cal(re)
            for i in range(7):
                for j in range(i+1,7):
                    if rsum[i] > rsum[j]:
                        temp = rsum[i]
                        rsum[i] = rsum[j]
                        rsum[j] = temp
                        re = row_op(re, i, j)
                        changed =changed +1
        else:
            print("Some Error")

        if changed >=1:
            continue
        else:
            return  re
celled = gt(machine_part_ma)
my_print(celled)