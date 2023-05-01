'''
Title     : Subtree In N-ary Tree
Author    : Asmit Singh
Solved On   : 1 May 2023
Solved Using   : Python3
'''

import collections
class Solution:
    def duplicateSubtreeNaryTree(self, root):
        def dfs(node, counter):
            if not node:
                return ''
            key = str(node.key) + ''.join(dfs(child, counter) for child in node.children)
            counter[key] += 1
            return key
        counter = collections.defaultdict(int)
        dfs(root, counter)
        return sum(count > 1 for count in counter.values())
