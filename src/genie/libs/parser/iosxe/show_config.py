''' show_config.py
IOSXE parsers for the following show command
    * show archive config differences
    * show archive config differences <fileA> <fileB>
    * show archive config differences <fileA>
    * show archive config incremental-diffs <fileA>
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Optional, \
                                                Any

# ====================================================
# Parser for 'show archive config differences'
# ====================================================

class ShowArchiveConfigDifferencesSchema(MetaParser):
    """
    Schema for show archive config differences
    """
    
    schema = {'contextual_config_diffs': {
        'index': { Any():{
                'before': list,
                'after': list
                }
            }
        }
    }

class ShowArchiveConfigDifferences(ShowArchiveConfigDifferencesSchema):
    """ Parser for show archive config differences"""

    cli_command = ['show archive config differences', 
                'show archive config differences {fileA} {fileB}',
                'show archive config differences {fileA}'
            ]

    def cli(self, fileA='', fileB='',output=None):
        if output is None:
            # execute command to get output
            if fileA and fileB:
                cmd = self.cli_command[1].format(fileA=fileA, fileB=fileB)
            elif fileA:
                cmd = self.cli_command[2].format(fileA=fileA)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial varaiables
        ret_dict = {}
        contextual_found = False
        index = 0
        # !Contextual Config Diffs:
        p1 = re.compile(r'^\s*!Contextual +Config +Diffs:$')
        # +hostname Router1
        p2 = re.compile(r'^\s*\+')
        # -hostname Router2
        p3 = re.compile(r'^\s*\-')
        for line in out.splitlines():
            line = line.strip()

            if not contextual_found:
                #!Contextual Config Diffs
                m = p1.match(line)
                if m:
                    contextual_found = True
                    contextual_config_diffs = ret_dict.setdefault('contextual_config_diffs',{}).\
                                                setdefault('index',{})
                    #index_dict = contextual_config_diffs.setdefault(index, {"before": [],"after": []})
                    continue
            else:
                m = p2.match(line)
                if m:
                    index_dict['after'].append(line)
                    continue
                m = p3.match(line)
                if m:
                    index+=1
                    index_dict = contextual_config_diffs.setdefault(index, {"before": [],"after": []})
                    index_dict['before'].append(line)
                    continue
                    
        return ret_dict

