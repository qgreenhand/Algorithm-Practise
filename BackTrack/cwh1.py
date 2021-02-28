res = []


def backtrack(havedone, n1, n2, n3, n4):
    """
    有2个1 2个2 2个3 2个4 要求两个n之间有n个数输出所有排列
    :param havedone:
    :param n1:
    :param n2:
    :param n3:
    :param n4:
    :return:
    """
    if len(havedone) == 8:
        res.append(havedone.copy())
        return
    if n1 == 2 or (len(havedone) >= 2 and n1 == 1 and havedone[-2] == 1):
        havedone.append(1)
        backtrack(havedone, n1 - 1, n2, n3, n4)
        havedone.pop()
    if n2 == 2 or (len(havedone) >= 3 and n2 == 1 and havedone[-3] == 2):
        havedone.append(2)
        backtrack(havedone, n1, n2 - 1, n3, n4)
        havedone.pop()
    if n3 == 2 or (len(havedone) >= 4 and n3 == 1 and havedone[-4] == 3):
        havedone.append(3)
        backtrack(havedone, n1, n2, n3 - 1, n4)
        havedone.pop()
    if n4 == 2 or (len(havedone) >= 5 and n4 == 1 and havedone[-5] == 4):
        havedone.append(4)
        backtrack(havedone, n1, n2, n3, n4 - 1)
        havedone.pop()


backtrack([], 2, 2, 2, 2)
print(res)
