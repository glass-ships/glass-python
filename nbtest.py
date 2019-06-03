# notebook_runner.py
 
import nbformat
import os
import sys

from nbconvert.preprocessors import ExecutePreprocessor
    
def run_notebook(notebook_path):
    nb_name, _ = os.path.splitext(os.path.basename(notebook_path))
    dirname = os.path.dirname(notebook_path)
 
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
 
    proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    proc.allow_errors = True
 
    #proc.preprocess(nb, {'metadata': {'path': '/'}})
    #output_path = os.path.join(dirname, '{}_test.ipynb'.format(nb_name))
    #with open(output_path, mode='wt') as f:
    #    nbformat.write(nb, f)
 
    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)
 
    return nb, errors

# check if argument is file or directory
fp = os.path.abspath(sys.argv[1])
if os.path.isfile(fp):
    mode = 'single'
    notebook_path = fp
    print("notebook path: ",notebook_path)
elif os.path.isdir(fp):
    mode = 'multiple'
    notebook_path = []
    for file in os.listdir(fp):
        if file.endswith(".ipynb"):
            notebook_path.append(os.path.join(fp,file))
    #print('notebooks: ',*notebook_path, sep = '\n')
else:
    print("Could not find notebooks at \'",sys.argv[1],"\'")    

# test notebook; if directory, test all notebooks     
if mode == 'single':
    if __name__ == '__main__':
        nb, errors = run_notebook(notebook_path)
        print("notebook errors: ",errors)
elif mode == 'multiple': 
    for i in notebook_path:
        if __name__ == '__main__':
            nb, errors = run_notebook(i)
            print("notebook: ",i,"\n errors: ",errors)