import unittest
from nodefuncs import split_nodes_delimiter
from textnode import TextNode

text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_text = "text"
text_type_image = "image"

node = TextNode("This is text with a `code block` word", text_type_text)
node2 = TextNode("This is text with a **bold** word", text_type_text)
node3 = TextNode("This text is bold already", text_type_bold)
node4 = TextNode("This is text with an *italic* word", text_type_text)
node5 = TextNode("This text is **missing a delimiter", text_type_text)

class TestSplitNodes(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(split_nodes_delimiter([node], "`", text_type_code), [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)])
        self.assertEqual(split_nodes_delimiter([node2], "**", text_type_bold), [TextNode("This is text with a ", text_type_text), TextNode("bold", text_type_bold), TextNode(" word", text_type_text)])
        self.assertEqual(split_nodes_delimiter([node3], "**", text_type_bold), [node3])
        self.assertEqual(split_nodes_delimiter([node4], "*", text_type_italic), [TextNode("This is text with an ", text_type_text), TextNode("italic", text_type_italic), TextNode(" word", text_type_text)])
        self.assertEqual(split_nodes_delimiter([node2, node3], "**", text_type_bold), [TextNode("This is text with a ", text_type_text), TextNode("bold", text_type_bold), TextNode(" word", text_type_text), node3])
 
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node5], "**", text_type_bold)
