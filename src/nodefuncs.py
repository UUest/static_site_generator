from htmlnode import TextNode, LeafNode, HTMLNode, ParentNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"





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
            TextNode(part, text_type if i % 2 == 1 else node.text_type)
            for i, part in enumerate(parts)
            ]
    return [new_node for node in old_nodes for new_node in create_text_nodes(node)]
    
    
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list) -> list:
    def create_image_nodes(node: TextNode) -> list:
        if node.text_type != "text":
            return [node]
        images = extract_markdown_images(node.text)
        nodes = []
        remaining_text = node.text
        for alt, url in images:
            before_image, _, remaining_text = remaining_text.partition(f"![{alt}]({url})")
            if before_image != "":
                nodes.append(TextNode(before_image, node.text_type))
            nodes.append(TextNode(alt, "image", url))
        if remaining_text != "":
            nodes.append(TextNode(remaining_text, node.text_type))
        return nodes
    return [new_node for node in old_nodes for new_node in create_image_nodes(node)]
        


def split_nodes_link(old_nodes: list) -> list:
    def create_link_nodes(node: TextNode) -> list:
        if node.text_type != "text":
            return [node]
        links = extract_markdown_links(node.text)
        nodes=[]
        remaining_text = node.text
        for alt, url in links:
            before_link, _, remaining_text = remaining_text.partition(f"[{alt}]({url})")
            if before_link != "":
                nodes.append(TextNode(before_link, node.text_type))
            nodes.append(TextNode(alt, "link", url))
        if remaining_text != "":
            nodes.append(TextNode(remaining_text, node.text_type))
        return nodes
    return [new_node for node in old_nodes for new_node in create_link_nodes(node)]


def text_to_text_nodes(text: str) -> list:
    node = TextNode(text, text_type_text)
    return split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node], "**", text_type_bold), "*", text_type_italic), "`", text_type_code)))