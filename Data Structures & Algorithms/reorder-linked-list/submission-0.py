# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left , right = head, head.next
        while right and right.next:
            left=left.next
            right=right.next.next

        last = left.next
        prev = left.next= None
        while last:
            temp=last.next
            last.next=prev
            prev=last
            last=temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next=second
            second.next=temp1
            first, second = temp1, temp2