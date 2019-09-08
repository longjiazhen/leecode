import random

class Solution(object):
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # 并不允许这种写法
        # return tribonacci(self, n - 1) + tribonacci(self, n - 2) + tribonacci(self, n - 3)
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(3, n+1):
            ret = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = ret
        return ret

# def tribonacci(n):
#     if n < 0:
#         return
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


if __name__ == '__main__':
    n = random.randint(1, 20)
    obj = Solution()
    result = obj.tribonacci(n)
    # result = tribonacci(n)
    print("第" + str(n) + "个斐波那契数 = " + str(result))
