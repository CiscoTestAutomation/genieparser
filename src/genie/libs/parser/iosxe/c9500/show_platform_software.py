''' show_platform_software.py
IOSXE parsers for the following show commands:
    * show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics
    * switchvirtualstate - active/standby
'''


# Python
import re
import xmltodict
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSchema(MetaParser):

    ''' Schema for "show Platform software" '''

    schema = {
        Optional('statistics'): 
                {Optional('Object_update'):
                    {Optional('pending_issue'):int,
                     Optional('pending_ack'):int,
                    },
                Optional('Batch_begin'):
                    {Optional('pending_issue'):int,
                     Optional('pending_ack'):int,
                    },
                Optional('Batch_end'):
                    {Optional('pending_issue'):int,
                     Optional('pending_ack'):int,
                    },
                Optional('Command'):
                    {Optional('pending_ack'):int,
                    },
                Optional('Total_objects'):int, 
                Optional('Stale_objects'): int,
                Optional('Resolve_objects'): int,
                Optional('Childless_delete_objects'): int,
                Optional('Backplane_objects'): int,
                Optional('Error-objects'): int,
                Optional('num_of_bundles'): int,
                Optional('paused_types'): int,
                },
        }

# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSoftware(ShowPlatformSchema):
    ''' Parser for
      "show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics"
    '''

    cli_command = ['show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics']

    def cli(self, switchvirtualstate="", serviceprocessor="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switchvirtualstate=switchvirtualstate,serviceprocessor=serviceprocessor)
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        #Forwarding Manager Asynchronous Object Manager Statistics
        p1 = re.compile(r'^Forwarding +Manager +Asynchronous +Object Manager*\s+(?P<statistics>(\S+))$')

        #Object update: Pending-issue: 0, Pending-acknowledgement: 0
        p2 = re.compile(r'^Object +update*:\s+Pending-issue*:+\s+(?P<pending_issue>(\d+)), +'
                         'Pending-acknowledgement*:\s+(?P<pending_ack>(\d+))$')

        #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p3 = re.compile(r'Batch +begin*:\s+Pending-issue*:+\s+(?P<pending_issue>(\d+)), +'
                         'Pending-acknowledgement*:\s+(?P<pending_ack>(\d+))$')

        #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p4 = re.compile(r'Batch +end*:\s+Pending-issue*:+\s+(?P<pending_issue>(\d+)), +'
                         'Pending-acknowledgement*:\s+(?P<pending_ack>(\d+))$')

        #Command:       Pending-acknowledgement: 0
        p5 = re.compile(r'Command*:\s+Pending-acknowledgement*:+\s+(?P<pending_ack>(\d+))')

        #Total-objects: 1231
        p6 = re.compile(r'Total-objects*:\s+(?P<tot_obj>(\d+))')

        #Stale-objects: 0
        p7 = re.compile(r'Stale-objects*:\s+(?P<stale_obj>(\d+))')

        #Resolve-objects: 0
        p8 = re.compile(r'Resolve-objects*:\s+(?P<resolve_obj>(\d+))')

        #Childless-delete-objects: 0
        p9 = re.compile(r'Childless-delete-objects*:\s+(?P<childless_delete_obj>(\d+))')

        #Backplane-objects: 0
        p10 = re.compile(r'Backplane-objects*:\s+(?P<backplane_obj>(\d+))')

        #Error-objects: 0
        p11 = re.compile(r'Error-objects*:\s+(?P<error_obj>(\d+))')

        #Number of bundles: 0
        p12 = re.compile(r'Number of bundles*:\s+(?P<num_of_bundles>(\d+))')

        #Paused-types: 5
        p13 = re.compile(r'Paused-types*:\s+(?P<paused_types>(\d+))')

        for line in out.splitlines():
            line = line.strip()

            #Forwarding Manager Asynchronous Object Manager Statistics
            m = p1.match(line)
            if m:
                statistics = m.groupdict()['statistics']
                stats_dict = ret_dict.setdefault('statistics', {})
                continue

            #Object update: Pending-issue: 0, Pending-acknowledgement: 0
            m = p2.match(line)
            if m:
                object_update_dict = stats_dict.setdefault('Object_update', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                object_update_dict['pending_issue']= pending_issue
                object_update_dict['pending_ack']= pending_ack
                continue

            #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
            m = p3.match(line)
            if m:
                batch_begin_dict = stats_dict.setdefault('Batch_begin', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_begin_dict['pending_issue']= pending_issue
                batch_begin_dict['pending_ack']= pending_ack
                continue

            #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
            m = p4.match(line)
            if m:
                batch_end_dict = stats_dict.setdefault('Batch_end', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_end_dict['pending_issue']= pending_issue
                batch_end_dict['pending_ack']= pending_ack
                continue

            #Command:       Pending-acknowledgement: 0
            m = p5.match(line)
            if m:
                command_dict = stats_dict.setdefault('Command', {})
                pending_ack = int(m.groupdict()['pending_ack'])
                command_dict['pending_ack']= pending_ack
                continue

            #Total-objects: 1231
            m = p6.match(line)
            if m:
                stats_dict['Total_objects'] = int(m.groupdict()['tot_obj'])
                continue

            #Stale-objects: 0
            m = p7.match(line)
            if m:
                stats_dict['Stale_objects'] = int(m.groupdict()['stale_obj'])
                continue

            #Resolve-objects: 0
            m = p8.match(line)
            if m:
                stats_dict['Resolve_objects'] = int(m.groupdict()['resolve_obj'])
                continue

            #Childless-delete-objects: 0
            m = p9.match(line)
            if m:
                stats_dict['Childless_delete_objects'] = int(m.groupdict()['childless_delete_obj'])
                continue

            #Backplane-objects: 0
            m = p10.match(line)
            if m:
                stats_dict['Backplane_objects'] = int(m.groupdict()['backplane_obj'])
                continue

            #Error-objects: 0
            m = p11.match(line)
            if m:
                stats_dict['Error-objects'] = int(m.groupdict()['error_obj'])
                continue

            #Number of bundles: 0
            m = p12.match(line)
            if m:
                stats_dict['num_of_bundles'] = int(m.groupdict()['num_of_bundles'])
                continue

            #Paused-types: 5
            m = p13.match(line)
            if m:
                stats_dict['paused_types'] = int(m.groupdict()['paused_types'])
                continue

        return ret_dict

