# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverseList(node):
            dummy, walker = None, node
            while walker:
                temp = walker.next
                walker.next = dummy
                dummy = walker
                walker = temp
            
            return dummy
        
        w1 = head
        w2 = reverseList(slow.next)
        slow.next = None
        res = walker = head
        while w2:
            tmp1, tmp2 = w1.next, w2.next
            w1.next = w2
            w2.next = tmp1
            w1 = tmp1
            w2 = tmp2

        
        

            

