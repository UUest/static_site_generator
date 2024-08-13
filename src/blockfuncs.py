import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from nodefuncs import text_node_to_html_node, split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_images, extract_markdown_links, text_to_text_nodes, list_node_to_leaf_node

def markdown_to_blocks(markdown: str) -> list:
    return list(filter(lambda x: x != "", map(lambda string: string.strip("\n").strip(), re.split(r'^\s*$', markdown, flags=re.MULTILINE))))

def block_to_block_type(block: str) -> str:
    heading_pattern = re.compile(r'^#{1,6} .+', re.MULTILINE)
    code_pattern = re.compile(r'^```[\s\S]*?```', re.MULTILINE)
    quote_pattern = re.compile(r'^(> .*(\n|$))+', re.MULTILINE)
    unordered_list_pattern = re.compile(r'^(\* |- ).*(\n|$)', re.MULTILINE)
    ordered_list_pattern = re.compile(r'^\s*([0-9]+)\. .+', re.MULTILINE)
    
    if heading_pattern.match(block):
        return "heading"
    elif code_pattern.match(block):
        return "code"
    elif quote_pattern.match(block):
        return "quote"
    elif unordered_list_pattern.match(block):
        return "unordered_list"
    elif ordered_list_pattern.match(block):
        lines = block.split("\n")
        expected_num = 1
        for line in lines:
            match = ordered_list_pattern.match(line)
            if match:
                number_str = match.group(1)
                try:
                    number = int(number_str)
                except ValueError:
                    raise Exception("Invalid ordered list, check list numbering")
                if number != expected_num:
                    raise Exception("Invalid ordered list, check list numbering")
                expected_num += 1
        return "ordered_list"
    else:
        return "paragraph"
    
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
    
def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    htmlnodes = list(map(lambda node: HTMLNode(block_to_block_type(node), node), blocks))
    def text_to_children(text: str) -> list:
        return list(map(lambda textnode: text_node_to_html_node(textnode), text_to_text_nodes(text)))
    def node_to_parent_node(node: HTMLNode) -> ParentNode:
        if node.tag  == "heading":
            val_split = node.value.split()
            if val_split[0] == "#":
                new_tag = "h1"
            elif val_split[0] == "##":
                new_tag = "h2"
            elif val_split[0] == "###":
                new_tag = "h3"
            elif val_split[0] == "####":
                new_tag = "h4"
            elif val_split[0] == "#####":
                new_tag = "h5"
            elif val_split[0] == "######":
                new_tag = "h6"
            children = text_to_children(node.value.strip("#").strip())
        elif node.tag == "quote":
            new_tag = "blockquote"
            children = text_to_children(node.value.strip(">").strip())
        elif node.tag == "code":
            new_tag = "pre"
            children = text_to_children(node.value)
        elif node.tag == "unordered_list":
            new_tag = "ul"
            children = list_node_to_leaf_node(node.value)
        elif node.tag == "ordered_list":
            new_tag = "ol"
            children = list_node_to_leaf_node(node.value)
        elif node.tag == "paragraph":
            new_tag = "p"
            children = text_to_children(node.value)
        return ParentNode(new_tag, children)
    new_nodes = []
    for node in htmlnodes:
        new_nodes.append(node_to_parent_node(node))
    return ParentNode("div", new_nodes)
