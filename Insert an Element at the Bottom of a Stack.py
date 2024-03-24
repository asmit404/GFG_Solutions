'''
Title     : Insert an Element at the Bottom of a Stack
Author    : Asmit Singh
Solved On   : 24 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def insertAtBottom(self, st, x):
        st.insert(0, x)
        return st

# Time Complexity: O(n)
# Space Complexity: O(1)