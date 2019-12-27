"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'


class Solution:
    def getListStr(self, l: ListNode):
        s = ''
        while True:
            s += str(l.val)
            if not l.next:
                return s[::-1]
            l = l.next

    def strToListNode(self, s, l=None) -> ListNode:
        if len(s) == 1:
            return ListNode(s)
        else:
            return ListNode(s[0], self.strToListNode(s[1:]))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = str(int(self.getListStr(l1)) + int(self.getListStr(l2)))[::-1]
        return self.strToListNode(result)


# a, b = l1, l2
# pre = ListNode(0)
# r = pre
# carry = 0
#
# while a or b:
#     x = a.val if a else 0
#     y = b.val if b else 0
#     s = x + y + carry
#     carry = s // 10
#     r.next = ListNode(s % 10)
#     r = r.next
#     if a:
#         a = a.next
#     if b:
#         b = b.next
# if carry > 0:
#     r.next = ListNode(carry)
#
# return pre.next
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        r = result
        carry = 0

        while l1 or l2:
            # 這裏l1和l2可能為0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10

            r.next = ListNode(s % 10)
            r = r.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            r.next = ListNode(carry)

        return result.next


if __name__ == '__main__':
    ll1 = ListNode(2, ListNode(4, ListNode(3)))
    ll2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution2().addTwoNumbers(ll1, ll2)
    print(result)
