from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            a, b, c = curr, curr.next, curr.next.next

            # Point prev -> b, b -> a, a -> c
            prev.next = b
            b.next = a
            a.next = c

            # we now have prev -> b -> a -> c, set prev = a, curr = c
            prev, curr = a, c

        return dummy.next
