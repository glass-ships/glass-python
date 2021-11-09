### This script was written to input a directory of locally hosted git repositories, 
### and push to a GitLab mirror, creating if one does not exist

import os
from subprocess import call, STDOUT
from git import Repo

directory = '/data/git'
extension = '.git'

### Find all git repositories in a top-tree directory
repos = []
repos_gitlab = []
for dirpath, dirnames, files in os.walk(directory):
    for i in dirnames:
        if (extension and i.lower().endswith(extension)) and (os.path.isfile(os.path.join(dirpath, i, 'config'))):
            repos.append(os.path.join(dirpath, i))

# remove overly large boi from list
del repos[repos.index('/data/git/DMC/CDMS_DetectorMC.git')]

# create list of GitLab remotes
remotes = [i.replace('/data/git','supercdms') for i in repos]

### The Loop: push if gitlab mirror exists, create and push if not
for i in range(len(repos)):
    config_file = os.path.join(repos[i], 'config')
    with open(config_file, mode='r', encoding='iso-8859-15') as file:
        if 'gitlab' in file.read():
            try:
                repo = Repo(repos[i])
                remote = repo.remote(name='gitlab')
                remote.push()
                #print(repos[i],' success')
            except Exception as e:
                print('--------\n',repos[i],' failed: \n',e,'\n')
            
        else: 
            print(repos[i],' does not exist. creating and pushing')
            try:
                repo = Repo(repos[i])
                remote = repo.create_remote('gitlab', url='git@gitlab.com:{}'.format(remotes[i]))
                remote.push()
            except Exception as e:
                print('--------\n',repos[i],' failed: \n',e,'\n')