# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        nums = []


        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        
        nums.sort()

        
        dummy = ListNode(0)
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next