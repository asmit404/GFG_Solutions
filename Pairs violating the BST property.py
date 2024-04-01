'''
Title     : Pairs violating the BST property
Author    : Asmit Singh
Solved On   : 1 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def pairsViolatingBST(self, n, root):
        pool = []
        res = 0

        def inorder(node):
            if not node: return
            inorder(node.left)
            pool.append(node.data)
            inorder(node.right)
        inorder(root)

        def mergesort(array, start, end):
            nonlocal res
            if end - start <= 1: return array[start:end]
            mid = (start + end) // 2
            lArr = mergesort(array, start, mid)
            rArr = mergesort(array, mid, end)
            l_idx, r_idx, arr = 0, 0, []
            while l_idx < len(lArr) and r_idx < len(rArr):
                if lArr[l_idx] <= rArr[r_idx]:
                    arr.append(lArr[l_idx])
                    l_idx += 1
                else:
                    res += len(lArr) - l_idx
                    arr.append(rArr[r_idx])
                    r_idx += 1
            if l_idx < len(lArr):
                arr.extend(lArr[l_idx:])
            if r_idx < len(rArr):
                arr.extend(rArr[r_idx:])
            return arr
        mergesort(pool, 0, len(pool))
        return res

# Time Complexity: O(n log n)
# Space Complexity: O(n)