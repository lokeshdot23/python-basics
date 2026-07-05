#working with zip files
from zipfile import ZipFile
from pathlib import Path
#it creates a copy of zip folder in current folder for the specified directory
'''
#completed creating a zipfolder copy of a folder called ecommerce 
with ZipFile('new_zip','w') as zip:
    for path in Path('ecommerce').rglob('*.*'):
        zip.write(path)
'''
'''
#to extract and print list of dir in files
with ZipFile('new_zip') as zip:
    print(zip.namelist())
    zip.extractall('to_extract_dir') #extract all to this dir with name to_extract_dir
'''
#to view all paths inside our new folder or if you want what in each file use path.read_text

path_1=Path('to_extract_dir')

for p in path_1.rglob('*.*'):
    print(p)