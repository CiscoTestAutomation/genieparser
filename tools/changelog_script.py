#!/usr/bin/env python

# Written by Thomas Ryan

import re
import pathlib
import argparse

# Linked list class to store our information
class LList():
    def __init__(self, key, prev=None):
        self.prev = prev.set_next(self) if prev else None
        self.next = None
        self.key = key

    def set_next(self, obj):
        if isinstance(self.next, list):
            self.next.append(obj)
            return self
        if self.next:
            self.next = [self.next]
            self.next.append(obj)
            return self
        self.next = obj
        return self

# Function for building our file
def build_file(llist, txt="", indent=-4):
    if isinstance(llist, LList):
        if not llist.prev:
            txt += '-' * 80 + '\n'
            txt += '{:^80}\n'.format(llist.key)
            txt += '-' * 80 + '\n'
        else:
            if indent == 0:
                txt += ' ' * indent + '\n* ' + llist.key.upper() + '\n'
            else:
                txt += ' ' * indent + '* ' + llist.key + '\n'

    if isinstance(llist.next, list):
        for sub_llist in llist.next:
            txt = build_file(sub_llist, txt, indent+4)
    else:
        if llist.next:
            txt = build_file(llist.next, txt, indent+4)

    return txt

# Main function
if __name__ == "__main__":
    # Argparse for all your argument parsing needs
    parser = argparse.ArgumentParser()

    # If no path is supplied then default the ./changelog/undistributed folder
    # of wherever this script is
    # Honestly, not good to rely on this. Better to supply your own path
    # (Protip: This would make for a good bash script component)
    parser.add_argument(
        "path",
        help="Changelog path",
        type=pathlib.Path,
        default=f"{pathlib.Path(__file__).parent.absolute()}/changelog/undistributed/",
        nargs="?"
    )

    parser.add_argument(
        "--output", "-o",
        help="Output file",
        default=f"{pathlib.Path(__file__).parent.absolute()}/undistributed.rst"
    )

    args = parser.parse_args()
    
    # Get a couple very important variables for later
    CHANGELOG_PATH = args.path
    FINAL_PATH = args.output
    RST_FILES = list(CHANGELOG_PATH.glob('*.rst'))

    parsed_dict = dict()

    # Regex! Glorious Regex! Groups, matching, and quantifiers!

    # --------------------------------------------------------------------------------
    p1 = re.compile(r'^ *-+$')

    #                                 New
    #                                 Fix
    p2 = re.compile(r'^ *(?P<key>[^\*\-\s]+)$')

    p3 = re.compile(r'^(?P<spaces>\s*)\* *(?P<data>.+):?$')

    # Some variables for our use
    last_space = 0
    key_dict = dict()
    key = None

    # Open each file (skip the template file if it exists) and parse through each one
    # Goal here is to make a dictionary structure 
    for rst_file in RST_FILES:
        if rst_file.name == 'template.rst':
            continue
        with open(rst_file) as fil:
            for line in fil:

                # --------------------------------------------------------------------------------
                m = p1.match(line)
                if m:
                    pass

                #                                 New
                #                                 Fix
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    key = group['key'].title()
                    key_dict.setdefault(key, LList(key))
                    index_list = list()

                m = p3.match(line)
                if m:
                    space_count = len(m.groupdict()['spaces'])
                    data = m.groupdict()['data'].replace(':','').title()

                    if space_count not in index_list:
                        index_list.append(space_count)
                        index_list.sort()

                    if space_count == 0:
                        last_space = space_count
                        if isinstance(key_dict[key].next, list):
                            if data in [llist.key for llist in key_dict[key].next]:
                                for llist in key_dict[key].next:
                                    if llist.key == data:
                                        last_llist = llist
                                        break
                            else:
                                last_llist = LList(data, key_dict[key])
                        else:
                            if key_dict[key].next and key_dict[key].next.key == data:
                                last_llist = key_dict[key].next
                            else:
                                last_llist = LList(data, key_dict[key])
                        continue

                    elif space_count == last_space:
                        last_llist = LList(data, last_llist.prev)
                        continue

                    elif space_count > last_space:
                        last_space = space_count
                        last_llist = LList(data, last_llist)
                        continue
                    
                    elif space_count < last_space:
                        go_back = index_list.index(last_space) - index_list.index(space_count)
                        for i in range(abs(go_back)+1):
                            last_llist = last_llist.prev
                        last_llist = LList(data, last_llist)
                        last_space = space_count
                        continue

    # And after a hard second's work it's time to write it all to a file
    with open(FINAL_PATH, 'w') as fil:
        txt = ""
        for llist in key_dict.values():
            txt += build_file(llist) + '\n\n'
        fil.write(txt)