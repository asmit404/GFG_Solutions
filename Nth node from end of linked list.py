'''
Title     : Nth node from end of linked list
Author    : Asmit Singh
Solved On   : 28 May 2023
Solved Using   : Python3
'''

def getNthFromLast(head, n):
    temp, var = head, 0
    while temp:
        var += 1
        temp = temp.next
    n, temp = var-n, head
    if n < 0 or n > var:
        return -1
    while n > 0:
        temp = temp.next
        n -= 1
    return temp.data
