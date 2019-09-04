"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import random

class Solution:

    def randomList(self):
        list = []
        list_len = random.randint(2, 20)
        for i in range(list_len):
            list.append(random.randint(-100, 100))
        print("list = ", end = "")
        print(list)
        return list

    # 在list_len范围之内，找2个不相等的随机数，它们对应的值加起来就是target
    def randomTarget(self, list):
        i = random.sample(range(0, len(list)), 2)[0]
        j = random.sample(range(0, len(list)), 2)[1]
        print("list[" +str(i) + "] = " + str(list[i]) + " list[" + str(j) + "] = " + str(list[j]))
        target = list[i] + list[j]
        print("target = " + str(target))
        return target

    def twoSum(self, list, target):
        result = []
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                if list[i] + list[j] == target:
                    result.append(i)
                    result.append(j)
                    print(result)
                    return  result

if __name__ == '__main__':
    s = Solution()
    list = s.randomList()
    target = s.randomTarget(list)
    s.twoSum(list, target)
