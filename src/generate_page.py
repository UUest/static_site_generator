from blockfuncs import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    open(dest_path, "w").write(template)
    
    