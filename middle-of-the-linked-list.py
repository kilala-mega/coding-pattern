# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1 2 3 4 5 7 9

1   s   5 f

3 4 5 6 7 8
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        
        while fast != None:
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                return slow
            fast = fast.next.next
            
        return slow
            
            
        
