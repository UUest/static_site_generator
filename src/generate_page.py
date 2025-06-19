from blockfuncs import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path).read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)

    # Replace template placeholders
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace("{{ BasePath }}", basepath)

    # Fix relative links and paths in the HTML content
    if basepath:
        # Only replace absolute paths that don't already have the basepath
        import re
        # Replace href="/" with href="/basepath/"
        template = template.replace('href="/"', f'href="{basepath}/"')
        # Replace other absolute hrefs that don't already start with basepath
        template = re.sub(r'href="(/(?!' + re.escape(basepath.lstrip('/')) + r')[^"]*)"',
                         f'href="{basepath}\\1"', template)
        # Replace absolute src paths that don't already start with basepath
        template = re.sub(r'src="(/(?!' + re.escape(basepath.lstrip('/')) + r')[^"]*)"',
                         f'src="{basepath}\\1"', template)

    open(dest_path, "w").write(template)

def generate_page_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    src_dir = os.listdir(dir_path_content)
    for dir in src_dir:
        src_path = f'{dir_path_content}/{dir}'
        if os.path.isfile(src_path):
            if dir.endswith('.md'):
                # Generate HTML from markdown
                dest_file = f'{dest_dir_path}/{dir[:-3]}.html'  # Replace .md with .html
                print(f"Generating page from {src_path} to {dest_file} using {template_path}")

                md_file = open(src_path).read()
                template = open(template_path).read()
                html_string = markdown_to_html_node(md_file).to_html()
                title = extract_title(md_file)

                # Replace template placeholders
                template = template.replace("{{ Title }}", title)
                template = template.replace("{{ Content }}", html_string)
                template = template.replace("{{ BasePath }}", basepath)

                # Fix relative links and paths in the HTML content
                if basepath:
                    import re
                    # Replace href="/" with href="/basepath/"
                    template = template.replace('href="/"', f'href="{basepath}/"')
                    # Replace other absolute hrefs that don't already start with basepath
                    template = re.sub(r'href="(/(?!' + re.escape(basepath.lstrip('/')) + r')[^"]*)"',
                                     f'href="{basepath}\\1"', template)
                    # Replace absolute src paths that don't already start with basepath
                    template = re.sub(r'src="(/(?!' + re.escape(basepath.lstrip('/')) + r')[^"]*)"',
                                     f'src="{basepath}\\1"', template)

                open(dest_file, "w").write(template)
        elif os.path.isdir(src_path):
            dest_subdir = f'{dest_dir_path}/{dir}'
            os.makedirs(dest_subdir, exist_ok=True)
            generate_page_recursively(f'{dir_path_content}/{dir}/', template_path, dest_subdir, basepath)
