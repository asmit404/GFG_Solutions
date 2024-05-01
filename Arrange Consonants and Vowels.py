'''
Title     : Arrange Consonants and Vowels
Author    : Asmit Singh
Solved On   : 1 May 2024
Solved Using   : Python3
'''

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def arrangeCV(self, head):
        if not head or not head.next: 
            return head

        def is_vowel(char):
            vowels = "aeiou"
            return char in vowels

        vHead = cHead = vTail = cTail = None
        curr = head
        while curr:
            if is_vowel(curr.data):
                if not vHead:
                    vHead = curr
                    vTail = curr
                else:
                    vTail.next = curr
                    vTail = curr
            else:
                if not cHead:
                    cHead = curr
                    cTail = curr
                else:
                    cTail.next = curr
                    cTail = curr
            curr = curr.next

        if vHead:
            head = vHead
            vTail.next = cHead
        else:
            head = cHead

        if cTail:
            cTail.next = None

        return head

# Time Complexity: O(n)
# Space Complexity: O(1)