# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node | None, insertVal: int) -> Node:
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        # if we are on the larger part of the list, go until we get smaller
        curr = head
        while insertVal > curr.val:
            curr = curr.next

        # we're on the smaller part, find the insertion point
        while curr.val <= insertVal and curr.next.val >= insertVal:
            curr = curr.next

        # insert
        prev = curr
        prev.next = Node(insertVal)
        prev.next.next = curr.next

        return head
