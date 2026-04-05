# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0,head)
        left = prev
        curr = head
        while n>0:
            curr = curr.next
            n-=1
        while curr:
            left = left.next
            curr = curr.next
        left.next = left.next.next
        return prev.next

