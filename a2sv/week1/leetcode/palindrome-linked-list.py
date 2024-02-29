# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right = slow
        prev = None
        curr = head

        if fast:
            right = right.next

        while curr != slow:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode


        while right and prev:
            if right.val != prev.val:
                return False
            right = right.next
            prev = prev.next
        return True
