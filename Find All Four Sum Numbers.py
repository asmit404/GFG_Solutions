"""
Title     : Find All Four Sum Numbers
Author    : Asmit Singh
Solved On   : 26 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        n = len(arr)
        pool = []

        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    curr_sum = arr[i] + arr[j] + arr[left] + arr[right]

                    if curr_sum == k:
                        pool.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        left += 1

                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1
                        right -= 1

                    elif curr_sum < k:
                        left += 1
                    else:
                        right -= 1

        return pool

# Time Complexity: O(n^3)
# Space Complexity: O(n^2)