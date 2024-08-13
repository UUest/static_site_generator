import re

def extract_title(markdown):
    if re.match(r'^[^\S\r\n]*#[^#\S\r\n]*([^#\s]+.*)', markdown):
        return re.match(r'^[^\S\r\n]*#[^#\S\r\n]*([^#\s]+.*)', markdown).group(0).strip('#').strip()
    else:
        raise Exception("No heading 1 found")    
