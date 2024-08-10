import unittest

from htmlnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("this is a text node", "bold")
        node4 = TextNode("This is a text node", "italic")
        node5 = TextNode("This is a text node", "bold", "bootdev.com")
        node6 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertEqual(node, node6)
        
        
        
if __name__ == "__main__":
    unittest.main()