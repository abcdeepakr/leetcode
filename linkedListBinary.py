# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head.val
        ans = ""
        ans += str(curr)
        while head.next !=None:
            ans += str(head.next.val)
            head = head.next
        return int(ans,2)