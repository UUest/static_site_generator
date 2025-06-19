from copy_static import clean_path, copy_static
from generate_page import generate_page_recursively
import sys
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = ""
clean_path("docs/")
copy_static()

fp = "content/"
tp = "template.html"
dp = "docs/"
generate_page_recursively(fp, tp, dp, basepath)
