from collections import deque


class Node:
    def __init__(self, data: int = 0) -> None:
        self.val = data
        self.left = self.right = None

    def print_PO(self) -> str:
        '''Pre order print'''
        if self is None:
            return ""
        return " " + str(self.val) + Node.look(self.left) + Node.look(self.right)

    def display(self) -> str:
        ''' Prints a visual of the tree to console. Code is from:
            https://stackoverflow.com/questions/34012886
        '''
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self) -> str:
        """ https://stackoverflow.com/questions/34012886
        Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Tree:
    def __init__(self, data=None) -> None:
        ''' If data is Node instance, set root to data.
            If data is not iterable, set root to None.
            Else, construct the tree by inserting every element in data.
        '''
        if hasattr(data, 'val') and hasattr(data, 'left') and hasattr(data, 'right'):
            self.root = data
            return
        try:
            iter(data)
        except TypeError:
            self.root = None
        else:
            self.root = None
            for d in data:
                self.insert(d)
        return

    def layers(self):
        ''' Debug function to look through the tree per level with BFS '''
        if not self.root:
            return ""
        out = ""
        curr_lev = 0
        q = deque()
        q.appendleft((self.root, 0))
        while q:
            curr, lev = q.pop()
            if lev > curr_lev:
                curr_lev += 1
                out += "\n"
            out += f"\t{curr.val}"
            if curr.left:
                q.appendleft((curr.left, lev+1))
            if curr.right:
                q.appendleft((curr.right, lev+1))
        return out

    def insert(self, i: int) -> None:
        ''' Insert element into BST. '''
        def _insert(node, i):
            if node.val > i:
                if not node.left:
                    node.left = Node(i)
                else:
                    _insert(node.left, i)
            elif node.val < i:
                if not node.right:
                    node.right = Node(i)
                else:
                    _insert(node.right, i)
            else:  # node value is the same as i
                print("Value already exists")

        if not self.root:
            self.root = Node(i)
        else:
            _insert(self.root, i)

    def delete(self, i: int) -> None:
        '''Delete the value and maintain valid BST.
        1. If not self.left or not self.right, then we just remove the non-empty node,
        then move the value up.
        2. Else, find value of the maximum on the left node 
        '''
        def _deleteNode(node: Node, i: int) -> Node:
            if not node:
                return None
            if node.val > i:
                node.left = _deleteNode(node.left, i)
            elif node.val < i:
                node.right = _deleteNode(node.right, i)
            else:  # found the node to delete
                if not node.left or node.right:
                    return node.right or node.left
                # darn it, both nodes exist
                temp = node.left
                while temp.right:
                    temp = temp.right
                node.val = temp.val
                node.left = _deleteNode(node.left, node.val)
            return node

        self.root = _deleteNode(self.root, i)

    def __repr__(self) -> str:
        return self.root.display() if self.root else ""
