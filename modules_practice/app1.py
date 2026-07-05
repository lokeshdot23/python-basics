from time import ctime
import shutil
#for files 
from pathlib import Path
path=Path(r'ecommerce/__init__.py')
# print(path.name)
# print(path.exists())
# print(path.read_text())
# text=path.read_text()
# text= text+'\n'+"#Hello this is a sample text to write into a file using path from pathlib"
# path.write_text(text)
# print("after updating inside file")
# print(path.read_text())
#creation time lastupdate etc
# print(path.stat())#gets all the stats including last update date of creation last access time
print(ctime(path.stat().st_ctime))
#to copy all the dir and files to new folder
source=Path('ecommerce')
target=Path() /'new_folder'
shutil.copytree(source,target)
