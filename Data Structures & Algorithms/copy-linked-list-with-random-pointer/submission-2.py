"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create copy nodes and store them in random pointer of original nodes
        # save original node random pointer in copy nodes next
        if head is None:
            return
        old = head
        while old:
            copy = Node(old.val)
            copy.next = old.random
            old.random = copy
            old = old.next
        newhead = head.random
        
        # Copy random pointers of old nodes to new nodes
        old = head
        while old:
            copy = old.random
            copy.random = copy.next.random if copy.next else None
            old = old.next
        
        # fix random pointers of old nodes and next pointers of new nodes
        old = head
        while old:
            copy = old.random
            old.random = copy.next
            copy.next = old.next.random if old.next else None
            old = old.next
        return newhead
        
        

            
