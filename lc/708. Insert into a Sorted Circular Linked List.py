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

        prev, curr = head, head.next
        while True:
            # most straightforward case, insert between prev and curr
            if prev.val <= insertVal <= curr.val:
                break

            # At the restarting point of the circular list, then either
            # the value is greater than both prev and curr OR
            # less than both prev and curr
            if prev.val > curr.val:
                if prev.val >= insertVal <= curr.val:
                    break
                if prev.val <= insertVal >= curr.val:
                    break

            prev, curr = curr, curr.next
            # this condition so that the while loop doesn't end right away
            if prev == head or curr == head:
                break

        # insert
        prev.next = Node(insertVal, curr)

        return head
