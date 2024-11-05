class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def findNodes(
        self,
        node: TreeNode | None,
        targetNodes: set[TreeNode],
        ancestor: list[TreeNode | None],
    ) -> int:
        """
        DFS, save the ancestor if nodesFound == len(targetNodes)
        """
        if not node:
            return 0
        left = self.findNodes(node.left, targetNodes, ancestor)
        right = self.findNodes(node.right, targetNodes, ancestor)

        nodesFound = left + right + int(node in targetNodes)
        # We found all nodes in targetNodes and no answer was recorded
        if nodesFound == len(targetNodes) and ancestor[0] is None:
            ancestor[0] = node
        return nodesFound

    def lowestCommonAncestorOneAndTwo(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        ancestor: list[TreeNode | None] = [None]
        self.findNodes(root, set([p, q]), ancestor)
        return ancestor[0]

    def lowestCommonAncestorFour(
        self, root: TreeNode, nodes: list[TreeNode]
    ) -> TreeNode | None:
        ancestor: list[TreeNode | None] = [None]
        self.findNodes(root, set(nodes), ancestor)
        return ancestor[0]


class SolutionThree:
    def lowestCommonAncestorThree(
        self, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        pTrack, qTrack = p, q
        while pTrack != qTrack:
            pTrack = pTrack.parent if pTrack else q
            qTrack = qTrack.parent if qTrack else p
        return pTrack
