# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        long = 0
        walker = head

        while walker:
            long += 1
            walker = walker.next

        ctr = 0
        w = head

        while ctr < long - n - 1:
            ctr += 1
            w = w.next
        if ctr > 0:
            w.next = w.next.next
        else:
            return None

        return head
        