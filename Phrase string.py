
#给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？输出需要删除的字符个数。


import numpy as np


def maxlen(s1, s2):
    L1 = len(s1)
    L2 = len(s2)
    Maxlen = np.zeros((L1 + 1, L2 + 1))
    # for i in range(L1):
    #     Maxlen[i][0] = 0
    # for i in range(L2):
    #     Maxlen[0][i] = 0
    for i in range(L1):
        for j in range(L2):
            if s1[i] == s2[j]:
                Maxlen[i + 1][j + 1] = Maxlen[i][j] + 1
            else:
                Maxlen[i + 1][j + 1] = max(Maxlen[i][j + 1], Maxlen[i + 1][j])
            print('ij: ', s1[i], ',', s2[j], '\n', Maxlen)
    return Maxlen[L1][L2]


