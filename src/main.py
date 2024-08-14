from copy_static import clean_public, copy_static
from generate_page import generate_page_recursively

clean_public()
copy_static()

fp = "content/"
tp = "template.html"
dp = "public/"
generate_page_recursively(fp, tp, dp)