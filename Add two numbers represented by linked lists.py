'''
Title     : Add two numbers represented by linked lists
Author    : Asmit Singh
Solved On   : 30 Apr 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, num1, num2):
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        curr = dummy = Node(0)
        carry = 0

        while num1 or num2 or carry:
            cnt = carry
            if num1:
                cnt += num1.data
                num1 = num1.next
            if num2:
                cnt += num2.data
                num2 = num2.next

            carry = cnt // 10
            curr.next = Node(cnt % 10)
            curr = curr.next

        res = self.reverse(dummy.next)
        while res and res.data == 0 and res.next:
            res = res.next
        return res

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Time Complexity: O(n)
# Space Complexity: O(n)