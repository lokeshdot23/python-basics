from pathlib import Path
path=Path('ecommerce')
print("using iterdir for getting a generator of paths and only get if its directory and not to include files ")
for p in (path.iterdir()):
    if p.is_dir():
        print(p)
print("using rglob for itereative search by pattern")
for p in path.rglob('*.py'):
    print(p)
print("normal use of path and itrdir without restrictions")
for p in path.iterdir():
    print(p)
#but this is not iterative and we wont be getting fils in sub directories so we use rglob or glob
#some common methods
print(path.is_dir())
print(path.is_file())
print(path.exists())
new_path=(path /'new_folder')
# new_path.mkdir(parents=True,exist_ok=True) # here ive created a folder now to delete ive commented this line
# new_path.rmdir() #here ive deleted the created folder

