# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# <first part (nullable)> <sublist to reverse (left <= right)> <remaining (nullable)>
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        prev = None
        current = head
        i = 0
        while current and i < left - 1:
            prev = current
            current = current.next
            i += 1
        
        last_node_first_part = prev # if prev is None, means there is no first part.
        last_node_sub_list = current
        
        i = 0
        later = None
        while current and i < right - left + 1:
            later = current
            current = current.next
            later.next = prev
            prev = later
            i += 1
            
        if last_node_first_part:
            last_node_first_part.next = prev
        else:
            head = prev
            
        last_node_sub_list.next = current
        
        return head
        
