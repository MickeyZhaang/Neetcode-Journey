# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        walker = head  
        ctr = 0
        while walker.next and ctr < n - 1:
            walker = walker.next
            ctr += 1

        if walker.next and walker.next.next:
            walker.next = walker.next.next
        
        return head if ctr != 0 else None

