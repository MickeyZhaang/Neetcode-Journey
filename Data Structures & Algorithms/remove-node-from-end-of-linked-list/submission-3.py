# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        left, right = head, head

        ctr = 0
        while ctr < n:
            ctr+=1
            right = right.next
        
        while right and right.next:
            right = right.next
            left = left.next
        
        if left == head:
            head = head.next
        else:
            left.next = left.next.next

        return head