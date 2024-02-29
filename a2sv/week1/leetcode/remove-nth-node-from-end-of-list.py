# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = head
    
        while n >0 and fast:
            fast = fast.next
            n -=1
        curr = dummy
        while fast:
            fast = fast.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
      

