import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodefuncs import split_nodes_link, split_nodes_delimiter, split_nodes_image, extract_markdown_images, extract_markdown_links

text_type_text = "text"


class TestSplitLinkImage(unittest.TestCase):
    def test_eq(self):
        pass