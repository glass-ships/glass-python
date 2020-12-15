import os
from subprocess import call, STDOUT

# cd alias
def cd(a): os.chdir(a)

# recursive file search
def file_search(directory='.', extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                print(os.path.join(dirpath, name))
            elif not extension:
                print(os.path.join(dirpath, name))
                
# git checker
def check_repo():
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        print("Nope!")
    else:
        print("Yup!")

