'''
Title     : Modify Linked List-1
Author    : Asmit Singh
Solved On   : 27 May 2023
Solved Using   : Python3
'''

class Solution:
    def modify_the_list(self, head):
        arr = []
        temp = head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        x, y = 0, len(arr)-1
        while x < y:
            arr[y], arr[x] = arr[x], arr[y]-arr[x]
            x += 1
            y -= 1
        index, temp = 0, head
        while temp:
            temp.data = arr[index]
            index += 1
            temp = temp.next
        return head
