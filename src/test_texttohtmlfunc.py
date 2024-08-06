import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_eq(self):
        boldnode = TextNode("This is bold", "bold")
        textnode = TextNode("this is text", "text")
        italicnode = TextNode("This is italic", "italic")
        codenode = TextNode("This is code", "code")
        linknode = TextNode("This is a link", "link", "https://www.google.com")
        imagenode = TextNode("This is an image", "image", "https://www.google.com/photo.png")
        self.assertEqual(text_node_to_html_node(boldnode), LeafNode("b", "This is bold"))
        self.assertEqual(text_node_to_html_node(boldnode).to_html(), "<b>This is bold</b>")
        self.assertEqual(text_node_to_html_node(textnode).to_html(), "this is text")
        self.assertEqual(text_node_to_html_node(italicnode).to_html(), "<i>This is italic</i>")
        self.assertEqual(text_node_to_html_node(codenode).to_html(), "<code>This is code</code>")
        self.assertEqual(text_node_to_html_node(linknode).to_html(), '<a href="https://www.google.com">This is a link</a>')
        self.assertEqual(text_node_to_html_node(imagenode).to_html(), '<img src="https://www.google.com/photo.png" alt="This is an image"></img>')