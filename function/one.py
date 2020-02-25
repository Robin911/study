# 一、编写一个函数，能够接受至少2个参数，返回最小值和最大值。
# 1
def sums(x, y, *args):
    print(min(x, y, *args))
    print(max(x, y, *args))


sums(1, 5, -5, 0, 123)

# 2
import random
def double_values(*nums):
    print(nums)
    return max(nums), min(nums)

print(*double_values(*[random.randint(10, 20) for _ in range(10)]))