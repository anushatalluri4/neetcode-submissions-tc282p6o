# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen=0
        curr=head
        while curr:
            listLen += 1
            curr=curr.next
        removeIndex=listLen-n
        if removeIndex==0:
            return head.next
        curr=head
        for i in range(removeIndex):
            if (i+1) == removeIndex:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head
                
