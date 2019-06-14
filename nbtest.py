# Checks that a jupyter notebook, or notebooks within a directory, run without error
# To use, call `$ python nbtest.py <NBPATH>` 
# where <NBPATH> is the path (abs or rel) to the notebook or directory of notebooks

import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path):
    nb_name, _ = os.path.splitext(os.path.basename(notebook_path))
    dirname = os.path.dirname(notebook_path)

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    proc.allow_errors = True

    proc.preprocess(nb, {'metadata': {'path': '/'}})
    output_path = os.path.join(dirname, '{}_test.ipynb'.format(nb_name))
    with open(output_path, mode='wt') as f:
        nbformat.write(nb, f)

    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)
    
    os.remove(output_path)

    return nb, errors

# check if argument is file or directory
fp = os.path.abspath(sys.argv[1])
if os.path.isfile(fp) and fp.endswith('.ipynb'):
    mode = 'single'
    notebook_path = fp
    print("notebook path: ",notebook_path)
elif os.path.isdir(fp):
    mode = 'multiple'
    notebook_path = []
    for file in os.listdir(fp):
        if file.endswith(".ipynb"):
            notebook_path.append(os.path.join(fp,file))
    if len(notebook_path) == 0:
        raise SystemExit("Could not find notebooks in directory: \'",sys.argv[1],"\'")
        #print('notebooks: ',*notebook_path, sep = '\n')
else:
    Raise ValueError("Invalid argument: ",sys.argv[1],"\n Please input a jupyter notebook or directory of notebooks.")

# test notebook; if directory, test all notebooks
if mode == 'single':
    if __name__ == '__main__':
        nb, errors = run_notebook(notebook_path)
        if errors:
            Raise ValueError("Notebook execution failed. Errors: {}".format(errors))
        elif not errors:
            print("Notebook execution successful.")

elif mode == 'multiple':
    for i in notebook_path:
        if __name__ == '__main__':
            nb, errors = run_notebook(i)
        if errors:
            Raise ValueError("Notebook execution failed. Errors: {}".format(errors))
        elif not errors:
            print("Notebook execution successful.")
