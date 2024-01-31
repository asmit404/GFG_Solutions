"""
Title     : Insert and Search in a Trie
Author    : Asmit Singh
Solved On   : 31 Jan 2024
Solved Using   : Python3
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Solution:
    def insert(self, root, key):
        curr = root
        for c in key:
            index = ord(c) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, root, key):
        curr = root
        for c in key:
            index = ord(c) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

# Time Complexity: O(L)
# Space Complexity: O(L)