import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodefuncs import split_nodes_link, split_nodes_delimiter, split_nodes_image, extract_markdown_images, extract_markdown_links, text_to_text_nodes

text1 = "This is **text** with an *italic* word and a ```code block``` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text2 = "This is *italic* text with and **bold** word and an ![image](http://www.imgur.com/img.jpg) and no links. Maybe some more **bold** text over here."

class TextToTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(text_to_text_nodes(text1), [TextNode("This is ", "text", None), TextNode("text", "bold", None), TextNode(" with an ", "text", None), TextNode("italic", "italic", None), TextNode(" word and a ", "text", None), TextNode("code block", "code", None), TextNode(" and an ", "text", None), TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", "text", None), TextNode("link", "link", "https://boot.dev")])
        self.assertEqual(text_to_text_nodes(text2), [TextNode("This is ", "text"), TextNode("italic", "italic"), TextNode(" text with and ", "text"), TextNode("bold", "bold"), TextNode(" word and an ", "text"), TextNode("image", "image", "http://www.imgur.com/img.jpg"), TextNode(" and no links. Maybe some more ", "text"), TextNode("bold", "bold"), TextNode(" text over here.", "text")])