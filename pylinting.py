#! /bin/env python
#!python

import os, re, sys
import fnmatch
import argparse
import subprocess

def main(path_dir):
    exclude, modules, result = ([] for i in range(3))
    rate = old_rate = index = flag = 0

    # import pdb; pdb.set_trace()
    for root, dirnames, filenames in os.walk(path_dir):
        for filename in fnmatch.filter(filenames, '*.py'):
            module_file = os.path.join(root, filename)

            if fnmatch.fnmatch(module_file, '*tests/*'):
                # ignore test modules
                continue
            if fnmatch.fnmatch(filename, '__init__.py'):
                # ignore init files
                continue
            
            if fnmatch.fnmatch(filename, 'pylinting.py'):
                # ignore init files
                continue

            # address ignores
            for pattern in exclude:
                if fnmatch.fnmatch(module_file, pattern):
                    # pattern match!
                    break
            else:
                modules.append(module_file)

    if len(modules) == 0:
        print('-'*30)
        print('Did not lint any files, exited')
        print('-'*30)
        sys.exit(1)

    print('')
    print('Running Pylint on all modules')
    print('-'*29)
    
    index = -1
    for file in modules:
        index +=1
        # relative path to file being linted
        print('Linting %s' %file.split(os.getcwd().split('/')[-1] + '/')[-1])
        logfile = open('logfile.txt', 'w')

        # write the results to a file to parse later
        cmd = ('pylint {file}'.format(file=file))

        process = subprocess.call(cmd,
                                stdout=logfile,
                                stderr=logfile,
                                shell=True)

    
        with open('logfile.txt', 'r') as input:
            content = input.read()

            p1 = re.compile(r'^(\*){13} Module [\w\.]+$')
            
            p2 = re.compile(r'^Your code has been rated at '
                                '(?P<rating>[\-\w\.]+)\/10 \(previous run:'
                                ' (?P<prev_rating>[\-\w\.]+).+$')

            for line in content.splitlines():
                line = line.strip()

                # File does not ouput any ratings => result as failed
                m = p1.match(line)
                if m:
                    flag += 1
                    if flag > 1:
                        result.append('{:<25s}Rate:  {:>15s}'\
                            .format(modules[index-1].split('/')[-1],\
                            "No Rating, Error in file"))

                m = p2.match(line)
                if m:
                    result.append('{:<25s}Rate:  {:>14s}'\
                        .format(file.split('/')[-1], line[27:]))

                    # increment ratings
                    rate += float(m.groupdict()['rating'])
                    old_rate += float(m.groupdict()['prev_rating'])
                    flag = 0 # reset flag
            input.close()
        os.unlink('logfile.txt')
            
    print('')
    print('Summary of each file: ')
    print('-'*21)

    for element in result:
        print(element)

    # calculate the avg rates
    number_of_files = len(modules)
    final_rate = rate/number_of_files
    final_old_rate = old_rate/number_of_files


    print('-'*26)
    print("Average rate %.3f/10" %final_rate)
    print("Previous average rate %.3f/10" %final_old_rate)
    print('-'*26)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Provide path to lint')
    parser.add_argument('--path',
                        type = str,
                        default=os.getcwd())
    
    args = parser.parse_args()
    path_dir = args.path

    main(path_dir)