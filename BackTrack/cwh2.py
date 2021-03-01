def do(N):
    """
    有n个球可以刷成黑色或者红色，但是不能连着三个同一颜色的球。求有几种排列方式。
    :param N:
    :return:
    """
    # last[0]代表末尾有一个重复球的可能排列数量 lastp[1]代表末尾有两个个重复球的可能排列数量
    last = [0, 0]
    for i in range(1, N + 1):
        if i == 1:
            last[0] = 2
            last[1] = 0
        else:
            n0 = last[1] + last[0]
            n1 = last[0]
            last[0] = n0
            last[1] = n1
    return sum(last)


print(do(2))