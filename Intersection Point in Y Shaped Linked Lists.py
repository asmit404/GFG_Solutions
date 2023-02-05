'''
Title     : Intersection Point in Y Shaped Linked Lists
Domain    : Linked Lists, Data Structures
Author    : Asmit Singh
Solved On   : 05 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def intersetPoint(self,head1,head2):
        a = head1
        b = head2 
        no_intersection = 0
        while a!=b and no_intersection!=2:
            if a.next == None:
                no_intersection+=1
                a = head2
            if b.next == None:
                b = head1
            a = a.next
            b = b.next
        if no_intersection == 2:return -1
        return a.data
