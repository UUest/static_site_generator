from blockfuncs import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    # Extract filename without extension for URL replacements
    filename = os.path.basename(from_path)[:-3]  # Remove .md extension
    template = template.replace("href=\"/\"", f"href=\"{basepath}/{filename}.html\"")
    template = template.replace("src=\"", f"src=\"{basepath}/")
    open(dest_path, "w").write(template)

def generate_page_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    src_dir = os.listdir(dir_path_content)
    for dir in src_dir:
        if os.path.isfile(f'{dir_path_content}/{dir}') == True:
            print(f"Generating page from {dir_path_content}/{dir} to {dest_dir_path}/{dir[:-2]}html using {template_path}")
            md_file = open(f'{dir_path_content}/{dir}').read()
            template = open(template_path).read()
            html_string = markdown_to_html_node(md_file).to_html()
            title = extract_title(md_file)
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html_string)
            template = template.replace("href=\"/\"", f"href=\"{basepath}/{dir[:-2]}html\"")
            template = template.replace("src=\"", f"src=\"{basepath}/{dir[:-2]}")
            open(f'{dest_dir_path}/{dir[:-2]}html', "w").write(template)
        elif os.path.isdir(f'{dir_path_content}/{dir}'):
            os.makedirs(f'{dest_dir_path}/{dir}', exist_ok=True)
            generate_page_recursively(f'{dir_path_content}/{dir}/', template_path, f'{dest_dir_path}/{dir}', basepath)
