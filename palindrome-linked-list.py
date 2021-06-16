# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1 2 3
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        walker, runner = head, head.next
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        
        def reverse(node):
            former, latter = None, node
            temp = None
            while latter:
                temp = latter
                latter = latter.next
                temp.next = former
                former = temp
            return temp
        
        end=reverse(walker)
        copy_end=end

        while head is not None and end is not None:
            if head.val != end.val:
                return False
            head = head.next
            end = end.next

        reverse(copy_end)

        return True



