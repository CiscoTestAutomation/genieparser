#! /bin/env python
#!python
#cython: language_level=3


import os
import fnmatch
from Cython.Build import cythonize

def generate_cython_modules(src_path, files, ignore_patterns = []):
    modules = []
    src = os.getcwd().split('/')[-1]

    for root, dirnames, filenames in os.walk(src_path):
        for filename in fnmatch.filter(filenames, '*.py'):
            module_file = os.path.join(root, filename)

            if module_file.endswith('__init__.py'):
                # ignore package declarations
                continue

            if fnmatch.fnmatch(module_file, '*tests/*'):
                # ignore test modules
                continue

            if fnmatch.fnmatch(filename, 'setup.py'):
                # ignore setup.py module
                continue

            if fnmatch.fnmatch(filename, 'compile.py'):
                # Don't cythonize this module
                continue

            # address ignores
            for pattern in ignore_patterns:
                if fnmatch.fnmatch(module_file, pattern):
                    # pattern match!
                    break
            else:
                modules.append(module_file)
                files.append(module_file[:-2] + 'c')
    
    for file in modules:
        cythonize(file, language_level = "3")


if __name__ == '__main__':
    # cythonize
    exclude = []
    files = []
    generate_cython_modules(os.getcwd(), files, exclude)

    print('Cythonized %d files' %len(files))

    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            print(file)
            
    print('Removed cythonized files')