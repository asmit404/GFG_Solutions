'''
Title     : Find anagrams in a linked list
Domain    : Linked List, Sliding-Window
Author    : Asmit Singh
Solved On   : 9 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def findAnagrams(self, head, s):
        a = [0]*26
        for e in s:
            a[ord(e)-ord('a')] += 1
        running = [0]*26
        start, end = head, head
        cnt = 0
        ans = []
        while start and end:
            idx = ord(end.data)-ord('a')
            running[idx] += 1
            cnt += 1
            if cnt > len(s):
                idx = ord(start.data)-ord('a')
                running[idx] -= 1
                cnt -= 1
                start.next, start = None, start.next
            if running == a:
                end.next, end = None, end.next
                ans.append(start)
                running = [0]*26
                cnt = 0
                start = end
            else:
                end = end.next
        return ans
