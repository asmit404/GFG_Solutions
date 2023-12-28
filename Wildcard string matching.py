"""
Title     : Wildcard string matching
Author    : Asmit Singh
Solved On   : 28 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def match(self, wild, pattern):
        if not wild:
            return not pattern
        if wild[0] == '*':
            if self.match(wild[1:], pattern) or (pattern and self.match(wild, pattern[1:])):
                return True
        elif wild[0] == '?':
            if pattern and self.match(wild[1:], pattern[1:]):
                return True
        elif pattern and wild[0] == pattern[0]:
            return self.match(wild[1:], pattern[1:])
        return False

# Did it without regex or fnmatch, you call this a hard problem?
# Time Complexity  : O(n * m)
# Space Complexity : O(n + m)