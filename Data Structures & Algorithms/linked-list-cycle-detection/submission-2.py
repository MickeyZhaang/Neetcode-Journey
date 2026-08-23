# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set();

        walker = head

        while walker and walker.next != None:

            if walker in seen:
                return True
            seen.add(walker)
            walker = walker.next
        
        return False

