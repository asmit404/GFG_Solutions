'''
Title     : Frequency Game
Author    : Asmit Singh
Solved On   : 31 May 2023
Solved Using   : Python3
'''

from collections import Counter
def LargButMinFreq(arr, n):
    a = Counter(arr)
    min_value = min(a.values())
    a = [key for key, value in a.items() if value == min_value]
    return max(a)
