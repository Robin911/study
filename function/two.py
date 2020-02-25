# 编写一个函数，接受一个参数n，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐。
# 倒三角
def showtail(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' ' * i, tail[i + 1:])


showtail(12)

# 正三角
def showtail(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    width = len(tail)
    for i in range(1, n):
        print("{:>{}}".format(" ".join([str(j) for j in range(i, 0, -1)]), width))
    print(tail)


showtail(12)
