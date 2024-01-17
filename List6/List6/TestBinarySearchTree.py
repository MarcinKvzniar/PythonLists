import unittest
from BinarySearchTree import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        # Creating a sample BST for testing
        self.root = Node(10, "ten")
        self.root[5] = 'five'
        self.root[15] = 'fifteen'
        self.root[3] = 'three'
        self.root[7] = 'seven'
        self.root[12] = 'twelve'
        self.root[18] = 'eighteen'

    def test_getitem(self):
        # Test __getitem__ method

        # Test value retrieval
        self.assertEqual(self.root[10], "ten")
        self.assertEqual(self.root[3], "three")
        self.assertEqual(self.root[18], "eighteen")

        # Test KeyError
        with self.assertRaises(KeyError):
            self.value = self.root[8]

    def test_setitem(self):
        # Test __setitem__ method

        # Test value update
        self.root[5] = "ten_ten"
        self.assertEqual(self.root[5], "ten_ten")

        self.root[15] = "fifteen_fifteen"
        self.assertEqual(self.root[15], "fifteen_fifteen")

        # Test new node insertion
        self.root[8] = "eight"
        self.assertEqual(self.root[8], "eight")

    def test_delitem(self):
        # Test __delitem__ method
        del self.root[5]
        with self.assertRaises(KeyError):
            self.value = self.root[5]

        del self.root[15]
        with self.assertRaises(KeyError):
            self.value = self.root[15]

        # Test KeyError for non-existent key
        with self.assertRaises(KeyError):
            del self.root[100]

    def test_node_sort(self):
        # Test node_sort method
        nodes_sorted = self.root.node_sort()
        expected_result = [
            (3, "three"),
            (5, "five"),
            (7, "seven"),
            (10, "ten"),
            (12, "twelve"),
            (15, "fifteen"),
            (18, "eighteen")]
        self.assertEqual(nodes_sorted, expected_result)

        # Test node_sort method for empty BST
        empty_bst = Node(None, None)
        empty_nodes_sorted = empty_bst.node_sort()
        self.assertEqual(empty_nodes_sorted, [])

    def test_node_rsort(self):
        # Test node_rsort method
        nodes_sorted = self.root.node_rsort()
        expected_result = [
            (18, "eighteen"),
            (15, "fifteen"),
            (12, "twelve"),
            (10, "ten"),
            (7, "seven"),
            (5, "five"),
            (3, "three")]
        self.assertEqual(nodes_sorted, expected_result)

        # Test node_rsort method for empty BST
        empty_bst = Node(None, None)
        empty_nodes_sorted = empty_bst.node_rsort()
        self.assertEqual(empty_nodes_sorted, [])


if __name__ == '__main__':
    unittest.main()


