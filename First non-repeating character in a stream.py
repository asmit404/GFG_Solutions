'''
Title     : First non-repeating character in a stream
Author    : Asmit Singh
Solved On   : 17 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def FirstNonRepeating(self, A):
        pool = []
        mp = {}
        res = ''
        for ch in A:
            if ch not in mp:
                pool.append(ch)
                mp[ch] = 1
            else:
                if ch in pool:
                    pool.remove(ch)
            res += pool[0] if pool else '#'
        return res
