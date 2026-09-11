# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        done = 0
        # DEBUG
        debug_ctr = 0
        n = len(lists)
        res = walker = ListNode()

        while done < n:
            # DEBUG
            if debug_ctr > 10:
                return
            place, minim = -1, float("inf")
            for i, node in enumerate(lists):
                if not node:
                    continue
                if node.val < minim:
                    place = i
                    minim = node.val
            if not lists[place]:
                done += 1
            else:
                walker.next = lists[place]
                walker = walker.next
                lists[place] = lists[place].next
            # DEBUG
            debug_ctr += 1
        return res.next
            
        

