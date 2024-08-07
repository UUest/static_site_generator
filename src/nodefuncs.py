from htmlnode import TextNode, LeafNode, HTMLNode, ParentNode
import re

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    else:
        raise Exception("Invalid text_type")
    
    
def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    def create_text_nodes(node: TextNode) -> list:
        if node.text_type != "text":
             return [node]
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched {delimiter} found in node text: {node.text}. Invalid Markdown syntax")
        return [
            TextNode(part, text_type if i % 2 else node.text_type)
            for i, part in enumerate(parts)
            ]
    return [new_node for node in old_nodes for new_node in create_text_nodes(node)]
    
    
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list) -> list:
    pass
    
def split_nodes_link(old_nodes: list) -> list:
    pass






