# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def isEmpty(self):
        return self.val == None

class Solution(ListNode):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        if current is None:
            return None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev