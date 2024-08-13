import os
import shutil

def clean_public():
    shutil.rmtree('./public')
    os.mkdir('./public')

def copy_static(path='./static/'):
    src_dir = os.listdir(path)
    for dir in src_dir:
        if os.path.isfile(f'{path}/{dir}') == True:
            shutil.copy(f'{path}{dir}', f'./public{path[8:]}{dir}')
            print(f'{path}{dir} copied to ./public{path[8:]}{dir}')
        elif os.path.isfile(f'{path}/{dir}') == False:
            os.mkdir(f'./public/{dir}')
            copy_static(f'{path}{dir}/')
            
         