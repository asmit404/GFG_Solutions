"""
Title     : First and last occurrences of x
Author    : Asmit Singh
Solved On   : 22 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def find(self, arr, n, x):
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == x:
                first = mid
                while first > 0 and arr[first - 1] == x:
                    first -= 1

                last = mid
                while last < n - 1 and arr[last + 1] == x:
                    last += 1

                return first, last

            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return -1, -1

# Time Complexity: O(log n)
# Space Complexity: O(1)