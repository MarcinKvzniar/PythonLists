from IPython import display
import graphviz


class Node:
    """
    This class represents a node in the Binary Search Tree (BST).

    Attributes:
    - key: The key of the node.
    - value: The value associated with the key.
    - left: Reference to the left child node.
    - right: Reference to the right child node.

    Methods:
    - __init__: Initialize a new node with a key and value.
    - __setitem__: Set the value associated with the specified key.
    - __delitem__: Remove the node with the specified key from the BST.
    - __getitem__: Retrieve the value associated with the specified key.
    - node_sort: Traverse the BST in in-order and return nodes in a list.
    - node_rsort: Traverse the BST in reversed in-order and return nodes in a list.
    - tree2digraph: Convert the BST into a graphviz Digraph for visualization.
    """
    def __init__(self, key, value):
        """
        Initialize a new node in the Binary Search Tree (BST).
        *Code implemented from a jupyter notebook provided by the lecturer.
        Key: a unique identifier within the tree that determines the
             position of the node relative to other nodes. In a BST, the key
             of each node is greater than all keys in its left subtree and
             less than all keys in its right subtree.
        Value: data or information associated with the key in a particular
             node. The value can be anything, such as a string or integer.

        Parameters:
        - key: The key of the node.
        - value: The value associated with the key.
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def node_sort(self):
        """
        Traverse the BST in in-order and return nodes in a list.
        If the BST is empty, an empty list will be returned.
        *Code implemented from a jupyter notebook provided by the lecturer
        and adjusted to fit the BST implementation.

        Returns:
        - A list of nodes in in-order.
        """
        nodes_sorted = []

        if self.key is None and self.value is None:
            return nodes_sorted

        if self.left:
            nodes_sorted += self.left.node_sort()

        nodes_sorted.append((self.key, self.value))

        if self.right:
            nodes_sorted += self.right.node_sort()

        return nodes_sorted

    def tree2digraph(self, g=None):
        """
        Convert the BST into a graphviz Digraph for visualization.
        *Code implemented from a jupyter notebook provided by the lecturer.

        Parameters:
        - g: The graphviz Digraph object.

        Returns:
        - The graphviz Digraph object.
        """
        if g is None:
            g = graphviz.Digraph()
            g.engine = 'dot'

        if self is not None:
            g.node(str(self.key))

            if self.left is not None:
                g.edge(str(self.key), str(self.left.key), 'L')
                self.left.tree2digraph(g)
            if self.right is not None:
                g.edge(str(self.key), str(self.right.key), 'R')
                self.right.tree2digraph(g)

        return g

    def __getitem__(self, key):
        """
        Get the value associated with the specified key.
        Method done with help from this source:
        "https://stackoverflow.com/questions/12460580/
        getitem-or-square-brackets-for-recursive-data-structure"

        Parameters:
        - key: The key of the node.

        Returns:
        - The value associated with the key.

        Raises:
        - KeyError: If the specified key does not exist.
        """
        if key == self.key:
            return self.value
        elif key < self.key and self.left is not None:
            return self.left[key]
        elif key > self.key and self.right is not None:
            return self.right[key]
        else:
            raise KeyError("The specified key does not exist.")

    def __setitem__(self, key, value):
        """
        Set the value associated with the specified key.
        If the key does not exist, a new node will be inserted into the BST.
        Therefore, this method can be used to both update and insert nodes.

        Parameters:
        - key: The key of the node.
        - value: The value associated with the key.
        """
        if key == self.key:
            self.value = value
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left[key] = value
        if key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right[key] = value

    def __delitem__(self, key):
        """
        Remove the node with the specified key from the BST.
        *Code adapted and adjusted from a jupyter notebook's
        'remove' method provided by the lecturer.

        Parameters:
        - key: The key of the node to be removed.

        Returns:
        - The root of the removed BST if the key exists.

        Raises:
        - KeyError: If the specified key does not exist.
        """
        if self is None:
            return None

        if key == self.key:
            if self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                successor_parent = self
                successor = self.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left
                if successor_parent is not self:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

            successor.left = self.left
            successor.right = self.right

            return successor

        elif key < self.key and self.left is not None:
            self.left = self.left.__delitem__(key)
        elif key > self.key and self.right is not None:
            self.right = self.right.__delitem__(key)
        else:
            raise KeyError(f"Key not found: {key}")

        return self

    def node_rsort(self):
        """
        Traverse the BST in reverse in-order and return nodes in a list.

        Returns:
        - A list of nodes in reverse in-order.
        """
        nodes_rev_sorted = []

        if self.key is None and self.value is None:
            return nodes_rev_sorted

        if self.right:
            nodes_rev_sorted += self.right.node_rsort()

        nodes_rev_sorted.append((self.key, self.value))

        if self.left:
            nodes_rev_sorted += self.left.node_rsort()

        return nodes_rev_sorted


if __name__ == "__main__":

    root = Node(5, 'five')
    root[20] = 'twenty'
    root[10] = 'ten'
    root[2] = 'two'
    root[50] = 'fifty'
    root[4] = 'four'
    root[7] = 'seven'

    print("Initial tree: ")
    display.display(root.tree2digraph())

    print("Example of __getitem__ method: ")
    print(root[2])

    print("\nExample of __setitem__ method: ")
    root[2] = 'abcd'
    print(root[2])

    print("\nExample of __delitem__ method: ")
    try:
        print(root[2])
        del root[2]
        print(root[2])
    except KeyError as e:
        print(e)

    empty_bst = Node(None, None)

    print("\nExample of node_sort method: ")
    print(Node.node_sort(root))
    print(empty_bst.node_sort())

    print("\nExample of node_rsort method: ")
    print(Node.node_rsort(root))
    print(empty_bst.node_rsort())
