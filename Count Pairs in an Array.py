'''
Title     : Count Pairs in an Array
Author    : Asmit Singh
Solved On   : 17 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def countPairs(self, arr, n):
        temp = [0] * n
        def merge(arr, temp, low, mid, high):
            left = i = low
            right = mid + 1
            count = 0

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp[i] = arr[left]
                    left += 1
                else:
                    count += (mid - left + 1)
                    temp[i] = arr[right]
                    right += 1
                i += 1

            while left <= mid:
                temp[i] = arr[left]
                i += 1
                left += 1

            while right <= high:
                temp[i] = arr[right]
                i += 1
                right += 1

            for i in range(low, high+1):
                arr[i] = temp[i]

            return count

        def merge_sort(arr, temp, left, right):
            count = 0
            if left < right:
                mid = (left + right) // 2
                count += merge_sort(arr, temp, left, mid)
                count += merge_sort(arr, temp, mid+1, right)
                count += merge(arr, temp, left, mid, right)
            return count

        for i in range(n):
            arr[i] *= i

        return merge_sort(arr, temp, 0, n-1)

# Time Complexity: O(n log n)
# Space Complexity: O(n)