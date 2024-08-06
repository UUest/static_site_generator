import unittest
from htmlnode import LeafNode

tag1 = "p"
tag2 = "a"
tag3 = "b"
value1 = "This is a paragraph of text."
value2 = ""
value3 = "Click me!"
props1 = {}
props2 = {"href": "https://www.google.com"}
to_html_test = "<p>This is a paragraph of text.</p>"
to_html_with_props_test = '<a href="https://www.google.com">Click me!</a>'


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag1, value1)
        node2 = LeafNode(tag1, value1)
        node3 = LeafNode(tag2, value3, props2)
        node5 = LeafNode(tag1, value1, props1)
        self.assertEqual(node, node2)
        self.assertEqual(node, node5)
        self.assertNotEqual(node, node3)
        self.assertEqual(node.to_html(), to_html_test)
        self.assertEqual(node3.to_html(), to_html_with_props_test)
        with self.assertRaises(ValueError):
            node4 = LeafNode(tag1, value2)
        
        
if __name__ == "__main__":
    unittest.main()
        