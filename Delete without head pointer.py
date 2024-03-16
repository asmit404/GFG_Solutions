'''
Title     : Delete without head pointer
Author    : Asmit Singh
Solved On   : 16 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def deleteNode(self, del_node):
        del_node.data = del_node.next.data
        del_node.next = del_node.next.next

# Time Complexity: O(1)
# Space Complexity: O(1)