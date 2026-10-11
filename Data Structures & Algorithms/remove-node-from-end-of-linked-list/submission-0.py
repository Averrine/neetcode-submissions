# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # given linked list: head node
        # remove index at n
        # return linked list

        current = head
        store = []

        while current:
            store.append(current.val)
            current = current.next
        print(len(store))

        dummy = ListNode(-1, head)
        current = dummy
        for i in range(len(store)- n):
            current = current.next
        current.next = current.next.next
        return dummy.next
