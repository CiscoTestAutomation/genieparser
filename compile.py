#! /bin/env python
#!python
#cython: language_level=3


import os
import fnmatch

from distutils.core import Extension
from Cython.Build import cythonize

def generate_cython_modules(src_path, ignore_patterns = []):
    modules = []
    src = os.getcwd().split('/')[-1]
    # import pdb;pdb.set_trace()

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

            # address ignores
            for pattern in ignore_patterns:
                if fnmatch.fnmatch(module_file, pattern):
                    # pattern match!
                    break
            else:
                module_name = module_file.split('.')[0].split('/')

                if 'ats' in module_name:
                    index = module_name.index('ats')
                else:
                    index = module_name.index(src) + 1

                module_name = '.'.join(module_name[index:])

                modules.append(Extension(module_name, [module_file,]))

    return modules


if __name__ == '__main__':
    # cythonize
    exclude = []
    cisco_cythonized_mods = cythonize(generate_cython_modules(os.getcwd(), exclude))
