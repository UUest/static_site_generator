import os
import shutil

def clean_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy_static(path='./static/'):
    src_dir = os.listdir(path)
    for dir in src_dir:
        if os.path.isfile(f'{path}/{dir}') == True:
            shutil.copy(f'{path}{dir}', f'./docs/{path[8:]}{dir}')
            print(f'{path}{dir} copied to ./docs/{path[8:]}{dir}')
        elif os.path.isfile(f'{path}/{dir}') == False:
            os.mkdir(f'./docs/{dir}')
            copy_static(f'{path}{dir}/')
