import nbformat
import os
import sys

from nbconvert.preprocessors import ExecutePreprocessor

if os.path.exists(sys.argv[1]):
    notebook_path = os.path.abspath(sys.argv[1])
else:
    print("Cannot find notebook \'",sys.argv[1],"\'")
    
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
 
if __name__ == '__main__':
    nb, errors = run_notebook(notebook_path)
    print("notebook errors: ",errors)
    