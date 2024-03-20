# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.middle(head)
        left =head
        right = mid.next
        mid.next = None

        l = self.sortList(left)
        r = self.sortList(right)

        return self.merge(l, r)

    def middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l, r):
        dummy = ListNode()
        curr = dummy

        while l and r:
            if l.val<= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
            curr.next = l or r
        return dummy.next
