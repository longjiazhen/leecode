"""
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
示例 1：
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
提示：
给出的 address 是一个有效的 IPv4 地址
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/defanging-an-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import re
import random

# 可以直接用replace
def invalid_ip1(str1):
	print("Before: " + str1)
	str2 = str1.replace(".", "[.]")
	print("After: " + str2)

# 也可以用re.sub
def invalid_ip2(str1):
	print("Before: " + str1)
	# str2 = str1.replace(".", "[.]")
	str2 = re.sub(r"\.", "[.]", str1)
	print("After: " + str2)

#str1 = "1.1.1.1"
str1 = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." \
      + str(random.randint(0,255)) + "." + str(random.randint(1,255))
invalid_ip1(str1)
invalid_ip2(str1)



"""
class Solution:
    def defangIPaddr(self, str):
        str2 = str.replace(".", "[.]")
        return str2
"""
