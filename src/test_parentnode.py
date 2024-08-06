import unittest

from htmlnode import LeafNode, ParentNode

to_html_test = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
parent_to_html_test = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
no_child_to_html_test = "<p></p>"
class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        node4 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        node2 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"), node])
        node3 = ParentNode("p", [])
        self.assertEqual(node, node4)
        self.assertEqual(node.to_html(), to_html_test)
        self.assertEqual(node2.to_html(), parent_to_html_test)
        with self.assertRaises(ValueError):
            node3.to_html() 
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()