import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props1 = {"href": "https://www.google.com", "target": "_blank"}
        props2 = {"href": "https:/www.google.com", "target": "_blank"}
        props3 = {}
        prop_to_html_result = ' href="https://www.google.com" target="_blank"'
        repr_result = "HTMLNode(tag=p, value=This is a paragraph, children=None, props={'href': 'https://www.google.com', 'target': '_blank'})"
        node = HTMLNode("p", "This is a paragraph", None, props1)
        node2 = HTMLNode("p", "This is a paragraph", None, props1)
        children1 = [node2]
        node3 = HTMLNode("p", "This is also a paragraph", None, props1) 
        node4 = HTMLNode("p", None, children1, props1)
        node5 = HTMLNode("p", "This is a paragraph", None, props2)
        node6 = HTMLNode("p", None, children1, props1)
        node7 = HTMLNode("P", "This is a paragraph", None, None)
        node8 = HTMLNode("p", "This is a paragraph", None, props3)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node, node5)
        self.assertEqual(node4, node6)
        self.assertNotEqual(node7, node8)
        self.assertEqual(node.props_to_html(), prop_to_html_result)
        self.assertEqual(node.__repr__(), repr_result)

if __name__ == "__main__":
    unittest.main()
        