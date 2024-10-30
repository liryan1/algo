class Node:
    def __init__(self, data=0) -> None:
        self.val = data
        self.left = self.right = self.parent = None


def traverse(root: Node) -> None:
    """Edit: make first part of while loop functional
    The added reference reduces the number of changes
    """
    back = None
    curr = root
    # stop if back to root and coming from right
    while curr:
        next = curr
        if back == curr.parent:  # First time through
            print(curr.val)
            if curr.left:
                next = curr.left
            elif curr.right:
                next = curr.right
            else:
                next = curr.parent
        elif back == curr.left:  # coming from the left node
            if curr.right:
                next = curr.right
            else:
                next = curr.parent
        else:  # coming up from right node
            next = curr.parent
        back = curr
        curr = next
