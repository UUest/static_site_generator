import re

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