'''show_platform.py

IOSXE c9500 parsers for the following show commands:
   * show platform software object-manager {serviceprocessor} statistics
   * show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics
'''

# Python
import re
import logging
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSoftwareObjectmanagerSchema(MetaParser):

    ''' Schema for "show Platform software" '''

    schema = {
        Optional('statistics'):
                {Optional('object-update'):
                    {'pending-issue':int,
                     'pending-ack':int,
                    },
                Optional('batch-begin'):
                    {'pending-issue':int,
                     'pending-ack':int,
                    },
                Optional('batch-end'):
                    {'pending-issue':int,
                     'pending-ack':int,
                    },
                Optional('command'):
                    {'pending-ack':int,
                    },
                'total-objects':int,
                'stale-objects': int,
                'resolve-objects': int,
                'childless-delete-objects': int,
                'backplane-objects': int,
                'error-objects': int,
                'number-of-bundles': int,
                'paused-types': int,
                },
        }

# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSoftwareObjectmanager(ShowPlatformSoftwareObjectmanagerSchema):
    ''' Parser for 
      "show platform software object-manager {serviceprocessor} statistics"
      "show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics"
    '''

    cli_command = ['show platform software object-manager {serviceprocessor} statistics',
                   'show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics']

    def cli(self, switchvirtualstate="", serviceprocessor="", output=None):
        if output is None:
            if switchvirtualstate:
                cmd = self.cli_command[1].format(switchvirtualstate=switchvirtualstate,
                                             serviceprocessor=serviceprocessor)
            else:
                cmd = self.cli_command[0].format(serviceprocessor=serviceprocessor)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        #Forwarding Manager Asynchronous Object Manager Statistics
        p1 = re.compile(r'^Forwarding +Manager +Asynchronous +Object Manager*\s+(?P<statistics>(\S+))$')

        #Object update: Pending-issue: 0, Pending-acknowledgement: 0
        p2 = re.compile(r'^Object +update:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p3 = re.compile(r'Batch +begin:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p4 = re.compile(r'Batch +end:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Command:       Pending-acknowledgement: 0
        p5 = re.compile(r'Command:\s+Pending-acknowledgement:\s+(?P<pending_ack>\d+)')

        #Total-objects: 1231
        #Stale-objects: 0
        #Resolve-objects: 0
        #Childless-delete-objects: 0
        #Backplane-objects: 0
        #Error-objects: 0
        #Number of bundles: 0
        #Paused-types: 5
        p6 = re.compile(r'^(?P<key>[\S ]+): +(?P<value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Forwarding Manager Asynchronous Object Manager Statistics
            m = p1.match(line)
            if m:
                stats_dict = ret_dict.setdefault('statistics', {})
                continue

            #Object update: Pending-issue: 0, Pending-acknowledgement: 0
            m = p2.match(line)
            if m:
                object_update_dict = stats_dict.setdefault('object-update', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                object_update_dict['pending-issue']= pending_issue
                object_update_dict['pending-ack']= pending_ack
                continue

            #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
            m = p3.match(line)
            if m:
                batch_begin_dict = stats_dict.setdefault('batch-begin', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_begin_dict['pending-issue']= pending_issue
                batch_begin_dict['pending-ack']= pending_ack
                continue

            #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
            m = p4.match(line)
            if m:
                batch_end_dict = stats_dict.setdefault('batch-end', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_end_dict['pending-issue']= pending_issue
                batch_end_dict['pending-ack']= pending_ack
                continue

            #Command:       Pending-acknowledgement: 0
            m = p5.match(line)
            if m:
                command_dict = stats_dict.setdefault('command', {})
                pending_ack = int(m.groupdict()['pending_ack'])
                command_dict['pending-ack']= pending_ack
                continue

            #Total-objects: 1231
            #Stale-objects: 0
            #Resolve-objects: 0
            #Childless-delete-objects: 0
            #Backplane-objects: 0
            #Error-objects: 0
            #Number of bundles: 0
            #Paused-types: 5

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                scrubbed = groups['key'].replace(' ', '-')
                stats_dict.update({scrubbed.lower(): int(groups['value'])})
                continue

        return ret_dict
