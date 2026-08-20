# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [1, 2, 3, 4, 5, 6, 7]
        # [1, 7, 2, 6, 3, 5, 4]
        # append(left) left += 1, then append(right) right -= 1, repeat until linked list is None
        # pointer 0 --> pointer len() - 1, repeat

        # neetcode = seperate to 2 lists, reverse second list, then merge lists
        # slow and fast pointers
        # slow shifting by 1, fast shifting by 2

        # find middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        # reverses second portion of the list 
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs of lists
        first, second = head, prev 
        while second :
            tmp1, tmp2 = first.next, second.next
            # inserting first node of second list inbetween head and head.next
            first.next = second
            second.next = tmp1
            # shifting our pointer nodes
            first, second = tmp1 , tmp2





        
        