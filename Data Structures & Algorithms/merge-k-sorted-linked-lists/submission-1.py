# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists)>1:
            mergedList = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.mergeLists(l1,l2))
            lists = mergedList
        return lists[0]
    def mergeLists(self,list1,list2):
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next