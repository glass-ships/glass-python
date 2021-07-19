import os
from subprocess import call, STDOUT

# cd alias
def cd(a): os.chdir(a)

# Search recursively for files with extension
def file_search(directory='.', extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                print(os.path.join(dirpath, name))
            elif not extension:
                print(os.path.join(dirpath, name))
                
# Check if dir is a git repo
def check_repo():
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        print("Nope!")
    else:
        print("Yup!")

