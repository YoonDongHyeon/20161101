import random
import copy
DIGITMAX = 3


def get_number(n,digit):
    howmany = 0
    k=n
    while (n > 0):
        n = n // 10
        howmany += 1


    x=None
    for i in range (howmany -digit+1):
        x = k // (10 ** (howmany - (i + 1)))
        k = k%(10**(howmany-(i+1)))

    return x

    # f = n //10**(howmany -1)
    # s = (n-f*100)//10
    # t = n % 10
    #
    # if digit ==1:
    #     return t
    # elif digit ==2:
    #     return s
    # elif digit == 3:
    #     return f
    # else:
    #     return -1

# get_number(123456789,7)
print(get_number(123456789,2))
# rn = random.randint(0,999)

# while get_number(rn, 1) == get_number(rn, 2) or get_number(rn, 1) == get_number(rn, 3) or get_number(rn, 2) == get_number(rn, 3):
#     rn = random.randint(0, 999)

# while True:
#     ans = None
#     try:
#         ans = int(input('Input:'))
#     except:
#         continue
#
#     if ans > 999 or ans < 0:
#         continue
#
#     strike = 0
#     ball = 0
#
#     for i in range(DIGITMAX):
#         for j in range(DIGITMAX):
#             if i==j and get_number(rn, i+1) == get_number(ans, j+1):
#                 strike += 1
#             if i!=j and get_number(rn, i+1) == get_number(ans, j+1):
#                 ball += 1
#
#     print (strike, ball)
#     if strike == DIGITMAX:
#         break