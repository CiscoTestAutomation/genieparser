#!/usr/bin/env python

import os
import re
import pathlib
import argparse

# Recursive function for putting the file together because we're cool like that
def build_file(parsed_dict, txt="", indent=-1):
    # This will be the end of the dict tree where it's a list
    if isinstance(parsed_dict, list):
        for item in parsed_dict:
            txt += ' ' * indent + '* ' + item + '\n'
        return txt
    # Recursively go through the keys in the dict
    for key in parsed_dict:
        # For the first level of the dict that holds the New/Fix labels
        if indent == -1:
            txt += '-' * 80 + '\n'
            txt += '{:^80}\n'.format(key)
            txt += '-' * 80 + '\n'
            txt = build_file(parsed_dict.get(key), txt, 0) + '\n\n'
        # Everything else that isn't New/Fix or a list of data
        else:
            txt += ' ' * indent + '* ' + key + '\n'
            txt = build_file(parsed_dict.get(key), txt, indent+4)
    
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

    # * IOSXE
    # * Junos
    p3 = re.compile(r'^ {0,3}\* +(?P<os>[\S ]+)$')

    #     * Added ShowLdpSessionIpaddressDetail
    #     * Fixed ShowLDPOverviewSchema
    p4 = re.compile(r'^ {4,7}\* +(?P<change>[\S ]+)$')

    #         * Made several keys optional
    #         * Show Ldp Session Ipaddress Detail
    p5 = re.compile(r'^ {8}\* +(?P<note>[\S ]+)$')

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
                    os_dict = parsed_dict.setdefault(group.get('key').title(), {})

                # * IOSXE
                # * Junos
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    change_dict = os_dict.setdefault(group.get('os').upper(), {})

                #     * Added ShowLdpSessionIpaddressDetail
                #     * Fixed ShowLDPOverviewSchema
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    notes_list = change_dict.setdefault(group.get('change'), [])

                #         * Made several keys optional
                #         * Show Ldp Session Ipaddress Detail
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    notes_list.append(group.get('note'))

    # And after a hard second's work it's time to write it all to a file
    with open(FINAL_PATH, 'w') as fil:
        fil.write(build_file(parsed_dict))