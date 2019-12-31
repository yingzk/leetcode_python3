"""
1108. IP 地址无效化

给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。


示例 1：

输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：

输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
 

提示：

给出的 address 是一个有效的 IPv4 地址

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/defanging-an-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        """注：replace效率低"""
        new_addr = ''
        for c in address:
            if c != '.':
                new_addr += c
            else:
                new_addr += '[.]'
        return new_addr


if __name__ == '__main__':
    address = "1.1.1.1"
    result = Solution().defangIPaddr(address)
    print(result)
