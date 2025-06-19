import os
import shutil

def clean_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy_static(src_path='static/', dest_path='docs/'):
    if not os.path.exists(src_path):
        print(f"Source path {src_path} does not exist")
        return

    src_dir = os.listdir(src_path)
    for item in src_dir:
        src_item_path = os.path.join(src_path, item)
        dest_item_path = os.path.join(dest_path, item)

        if os.path.isfile(src_item_path):
            shutil.copy2(src_item_path, dest_item_path)
            print(f'{src_item_path} copied to {dest_item_path}')
        elif os.path.isdir(src_item_path):
            os.makedirs(dest_item_path, exist_ok=True)
            copy_static(src_item_path + '/', dest_item_path + '/')
