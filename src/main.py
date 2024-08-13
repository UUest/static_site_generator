from copy_static import clean_public, copy_static
from generate_page import generate_page

clean_public()
copy_static()

fp = "content/index.md"
tp = "template.html"
dp = "public/index.html"
generate_page(fp, tp, dp)