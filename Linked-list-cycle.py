# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
head
fast,slow point to head
when fast.next = None, there is no cycle, 
move fast twice speed as slow pointer
when fast and slow meet again, this means there is a cycle.
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        if head == None:
            return False
        while fast.next != None:
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                return False
            else:
                fast = fast.next.next
            if fast == slow:
                return True
        return False
        
