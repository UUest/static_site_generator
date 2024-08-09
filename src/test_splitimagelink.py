import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodefuncs import split_nodes_link, split_nodes_delimiter, split_nodes_image, extract_markdown_images, extract_markdown_links

text_type_text = "text"
text_type_link = "link"
text_type_image = "image"
text_type_bold = "bold"

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
)
node2 = TextNode(
    "This is text with an image ![woah there](https://www.img.com/show.jpg)",
    text_type_text
)
node3 = TextNode(
    "![image text](http://www.img.com/pic.png) this is an image at the start and an image at the end ![image ender](http://www.img.com/pic2.jpg)",
    text_type_text
)
node4 = TextNode(
    "This text is **bold** with no images",
    text_type_bold
)
node5 = TextNode(
    "This text contains a [link](https://www.boot.dev) and another [link2](https://www.google.com) and even a third [link3](https://www.chatgpt.com) with some extra text after",
    text_type_text
)

class TestSplitLinkImage(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(split_nodes_link([node]), [TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")])
        self.assertEqual(split_nodes_image([node2]), [TextNode("This is text with an image ", text_type_text), TextNode("woah there", text_type_image, "https://www.img.com/show.jpg")])
        self.assertEqual(split_nodes_image([node3]), [TextNode("image text", text_type_image, "http://www.img.com/pic.png"), TextNode(" this is an image at the start and an image at the end ", text_type_text), TextNode("image ender", text_type_image, "http://www.img.com/pic2.jpg")])
        self.assertEqual(split_nodes_link([node4]), [TextNode("This text is **bold** with no images", text_type_bold)])
        self.assertEqual(split_nodes_link([node5]), [TextNode("This text contains a ", text_type_text), TextNode("link", text_type_link, "https://www.boot.dev"), TextNode(" and another ", text_type_text), TextNode("link2", text_type_link, "https://www.google.com"), TextNode(" and even a third ", text_type_text), TextNode("link3", text_type_link, "https://www.chatgpt.com"), TextNode(" with some extra text after", text_type_text)])
