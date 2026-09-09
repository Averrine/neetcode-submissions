# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # array of K * [Linked lists[lists]] = sorted in ascending order
        # Initial thought process:
            # access linked list[n], iterate through the list while storing in a new list
            # after storing all values in a. new independt list. = sort
        
        # base case
        stored = []
        if len(lists) == 0:
            return None

        # looping throuhg each list and storing values, then sortin glist
        for i in range(len(lists)):
            node = lists[i]
            while node is not None:
                stored.append(node.val)
                node = node.next
        stored.sort()

        # rebuilding merged linked list
        dummy = ListNode()
        current = dummy
        for val in stored:
            current.next = ListNode(val)
            current = current.next
        return dummy.next


