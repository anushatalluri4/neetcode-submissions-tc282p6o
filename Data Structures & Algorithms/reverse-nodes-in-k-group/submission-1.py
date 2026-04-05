# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupstart = dummy
        while True:
            kth = self.getKth(groupstart,k)
            if not kth:
                break
            groupnext = kth.next
            prev, curr = kth.next, groupstart.next
            while curr != groupnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tmp = groupstart.next
            groupstart.next = kth
            groupstart = tmp
        return dummy.next

    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr