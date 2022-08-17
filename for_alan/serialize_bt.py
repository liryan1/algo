from PythonDS.BT import Node, Tree
from random import randrange


class serialize_tree:
    """ Implement encoding and decoding of a binary tree.
    """

    def serialize(self, root: 'Node', file_name: str = 'tree.txt') -> None:
        """ Encodes a tree to a file.
        """

    def deserialize(self, path_to_file: str) -> 'Node':
        """Decodes your encoded data to tree.
        """


def main():
    # Random test
    filename = "tree.txt"
    tree = Tree()
    for _ in range(10):
        x = randrange(1, 100)
        tree.insert(x)
    print("Original Tree\n", tree, sep="")
    print(f"Serializing Tree to {filename}")
    S = serialize_tree()
    S.serialize(tree.root, filename)
    print("Done")
    print("Deserializing Tree")
    new_tree = Tree(S.deserialize(filename))
    print("Done")
    print("New Tree\n", new_tree, sep="")


if __name__ == "__main__":
    main()
