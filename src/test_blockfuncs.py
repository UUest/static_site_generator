import unittest

from blockfuncs import markdown_to_blocks, block_to_block_type

md1 = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

md2 = """
## This is also a heading
         
# So is this
        
This is just a paragraph of some text
        
* a couple
* of
* bullets"""

block1 = "# This is a heading"
block2 = "#### This is also a heading"
block3 = "this is a paragraph"
block4 = "```this is some code```"
block5 = "> this is a quote"
block6 = """* this
* is
* an unordered
* list"""
block7 = """
1. This is an
2. ordered list
3. that is
4. formatted correctly"""
block8 = """
1. this is an ordered list
3. that is incorrect
2. and out of order"""

class TestBlockFuncs(unittest.TestCase):
    def test_eq(self):

        
        self.assertEqual(markdown_to_blocks(md1), ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])
        self.assertEqual(markdown_to_blocks(md2), ["## This is also a heading", "# So is this", "This is just a paragraph of some text", "* a couple\n* of\n* bullets"])
        self.assertEqual(block_to_block_type(block1), "heading")
        self.assertEqual(block_to_block_type(block2), "heading")
        self.assertEqual(block_to_block_type(block3), "paragraph")
        self.assertEqual(block_to_block_type(block4), "code")
        self.assertEqual(block_to_block_type(block5), "quote")
        self.assertEqual(block_to_block_type(block6), "unordered_list")
        self.assertEqual(block_to_block_type(block7), "ordered_list")
        with self.assertRaises(Exception):
            self.assertEqual(block_to_block_type(block8), "ordered_list")