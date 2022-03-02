'''show_platform.py

IOSXE c9500 parsers for the following show commands:
   * show platform software object-manager {serviceprocessor} statistics
   * show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics
   * show platform software fed active ifm mappings
   * show platform hardware fed active fwd-asic resource tcam utilization
   * show platform software fed active acl info summary
   * show platform software fed active acl info summary | include {acl_name}
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

# ============================================================
#  Schema for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformFedActiveIfmMappingSchema(MetaParser):
    """Schema for show platform software fed active ifm mappings"""

    schema = {'interface':
                  {Any():
                       {'IF_ID': str,
                        'Inst': str,
                        'Asic': str,
                        'Core': str,
                        'IFG_ID': str,
                        'Port': str,
                        'SubPort': str,
                        'Mac': str,
                        'First_Serdes': str,
                        'Last_Serdes': str,
                        'Cntx': str,
                        'LPN': str,
                        'GPN': str,
                        'Type': str,
                        'Active': str,
                        }
                   },
              }

# ============================================================
#  Parser for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformFedActiveIfmMapping(ShowPlatformFedActiveIfmMappingSchema):
    """ Parser for show platform software fed active ifm mappings"""

    cli_command = "show platform software fed active ifm mappings"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initialize variables
        ret_dict = {}

        # HundredGigE1/0/21       0x4d6    0   0    0      0    0      0     1  0            1            0    1    1    NIF    Y
        p1 = re.compile(
            r'^(?P<interface>\S+)\s+(?P<ifId>\S+)\s+(?P<inst>\d+)\s+(?P<asic>\d+)\s+(?P<core>\d+)\s+(?P<ifgId>\d+)\s+(?P<port>\d+)\s+(?P<sbPort>\d+)\s+(?P<mac>\d+)\s+(?P<first_serdes>\d+)\s+(?P<last_serdes>\d+)\s+(?P<cntx>\d+)\s+(?P<lpn>\d+)\s+(?P<gpn>\d+)\s+(?P<type>\w+)\s+(?P<act>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE1/0/21       0x4d6    0   0    0      0    0      0     1   0            1            0    1    1    NIF    Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intfId = group['interface']
                ifId = group['ifId']
                instance = group['inst']
                asic = group['asic']
                core = group['core']
                ifgId = group['ifgId']
                port = group['port']
                subPort = group['sbPort']
                mac = group['mac']
                first_serdes = group['first_serdes']
                last_serdes = group['last_serdes']
                cntx = group['cntx']
                lpn = group['lpn']
                gpn = group['gpn']
                type = group['type']
                active = group['act']

                final_dict = ret_dict.setdefault('interface', {}).setdefault(intfId, {})

                final_dict['IF_ID'] = ifId
                final_dict['Inst'] = instance
                final_dict['Asic'] = asic
                final_dict['Core'] = core
                final_dict['IFG_ID'] = ifgId
                final_dict['Port'] = port
                final_dict['SubPort'] = subPort
                final_dict['Mac'] = mac
                final_dict['First_Serdes'] = first_serdes
                final_dict['Last_Serdes'] = last_serdes
                final_dict['Cntx'] = cntx
                final_dict['LPN'] = lpn
                final_dict['GPN'] = gpn
                final_dict['Type'] = type
                final_dict['Active'] = active
                continue

        return ret_dict

# ==================================================================================
#  Schema for 'show platform hardware fed active fwd-asic resource tcam utilization'
# ==================================================================================
class ShowPlatformFedActiveTcamUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic resource tcam utilization"""
    schema = {
        'Slice0': {
            'egress_wide_direction': str,
            'used0': int,
            'free0': int,
            'ingress_wide_direction': str,
            'inw_used0': int,
            'inw_free0': int
        },
        'Slice1': {
            'egress_wide_direction': str,
            'used1': int,
            'free1': int,
            'ingress_wide_direction': str,
            'inw_used1': int,
            'inw_free1': int
        },
        'Slice2': {
            'egress_wide_direction': str,
            'used2': int,
            'free2': int,
            'ingress_wide_direction': str,
            'inw_used2': int,
            'inw_free2': int
        },
        'Slice3': {
            'egress_wide_direction': str,
            'used3': int,
            'free3': int,
            'ingress_wide_direction': str,
            'inw_used3': int,
            'inw_free3': int
        },
        'Slice4': {
            'egress_wide_direction': str,
            'used4': int,
            'free4': int,
            'ingress_wide_direction': str,
            'inw_used4': int,
            'inw_free4': int
        },
        'Slice5': {
            'egress_wide_direction': str,
            'used5': int,
            'free5': int,
            'ingress_wide_direction': str,
            'inw_used5': int,
            'inw_free5': int
        },
    }

# ==================================================================================
#  Parser for 'show platform hardware fed active fwd-asic resource tcam utilization'
# ==================================================================================
class ShowPlatformFedActiveTcamUtilization(ShowPlatformFedActiveTcamUtilizationSchema):
    """ Parser for show platform hardware fed active fwd-asic resource tcam utilization"""

    cli_command = "show platform hardware fed active fwd-asic resource tcam utilization"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        slice_dict = {}

        # Slice0       Slice1       Slice2       Slice3       Slice4       Slice5
        p1 = re.compile(r'^(?P<slice_id0>(\w+))\s+(?P<slice_id1>(\w+))\s+(?P<slice_id2>(\w+))\s+(?P<slice_id3>(\w+))\s+(?P<slice_id4>(\w+))\s+(?P<slice_id5>(\w+))$')

        # Egress Wide TCAM entries
        p2 = re.compile(r'^Egress +(?P<egress_wide_direction>([a-zA-Z]+)) +TCAM +entries\s+(?P<used0>(\d+))\s+(?P<free0>(\d+))\s+(?P<used1>(\d+))\s+(?P<free1>(\d+))\s+(?P<used2>(\d+))\s+(?P<free2>(\d+))\s+(?P<used3>(\d+))\s+(?P<free3>(\d+))\s+(?P<used4>(\d+))\s+(?P<free4>(\d+))\s+(?P<used5>(\d+))\s+(?P<free5>(\d+)).*$')
        # Ingress Wide TCAM entries
        p3 = re.compile(r'^Ingress +(?P<ingress_wide_direction>([a-zA-Z]+)) +TCAM +entries\s+(?P<inw_used0>(\d+))\s+(?P<inw_free0>(\d+))\s+(?P<inw_used1>(\d+))\s+(?P<inw_free1>(\d+))\s+(?P<inw_used2>(\d+))\s+(?P<inw_free2>(\d+))\s+(?P<inw_used3>(\d+))\s+(?P<inw_free3>(\d+))\s+(?P<inw_used4>(\d+))\s+(?P<inw_free4>(\d+))\s+(?P<inw_used5>(\d+))\s+(?P<inw_free5>(\d+)).*$')

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                slice_id0 = group['slice_id0']
                if slice_id0 not in slice_dict:
                    slice_dict[slice_id0] = {}
                slice_id1 = group['slice_id1']
                if slice_id1 not in slice_dict:
                    slice_dict[slice_id1] = {}
                slice_id2 = group['slice_id2']
                if slice_id2 not in slice_dict:
                    slice_dict[slice_id2] = {}
                slice_id3 = group['slice_id3']
                if slice_id3 not in slice_dict:
                    slice_dict[slice_id3] = {}
                slice_id4 = group['slice_id4']
                if slice_id4 not in slice_dict:
                    slice_dict[slice_id4] = {}
                slice_id5 = group['slice_id5']
                if slice_id5 not in slice_dict:
                    slice_dict[slice_id5] = {}
                continue
            m = p2.match(line)

            if m:
                group = m.groupdict()
                direction = group["egress_wide_direction"]
                if direction not in slice_dict:
                    slice_dict[slice_id0]["egress_wide_direction"] = direction
                    slice_dict[slice_id1]["egress_wide_direction"] = direction
                    slice_dict[slice_id2]["egress_wide_direction"] = direction
                    slice_dict[slice_id3]["egress_wide_direction"] = direction
                    slice_dict[slice_id4]["egress_wide_direction"] = direction
                    slice_dict[slice_id5]["egress_wide_direction"] = direction
                for x in range(6):
                    slice_id = 'Slice' + str(x).strip()
                    used = 'used' + str(x)
                    free = 'free' + str(x)
                    slice_dict[slice_id][used] = int(group[used])
                    slice_dict[slice_id][free] = int(group[free])

            m = p3.match(line)
            if m:
                group = m.groupdict()
                direction = group["ingress_wide_direction"]
                if direction not in slice_dict:
                    slice_dict[slice_id0]["ingress_wide_direction"] = direction
                    slice_dict[slice_id1]["ingress_wide_direction"] = direction
                    slice_dict[slice_id2]["ingress_wide_direction"] = direction
                    slice_dict[slice_id3]["ingress_wide_direction"] = direction
                    slice_dict[slice_id4]["ingress_wide_direction"] = direction
                    slice_dict[slice_id5]["ingress_wide_direction"] = direction
                for x in range(6):
                    slice_id = 'Slice' + str(x).strip()
                    inw_used = 'inw_used' + str(x)
                    inw_free = 'inw_free' + str(x)
                    slice_dict[slice_id][inw_used] = int(group[inw_used])
                    slice_dict[slice_id][inw_free] = int(group[inw_free])

        return slice_dict

# ============================================================================
#  Schema for
#  * 'show platform software fed active acl info summary'
#  * 'show platform software fed active acl info summary | include {acl_name}'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclInfoSummarySchema(MetaParser):
    """Schema for 'show platform software fed active acl info summary
    """
    schema = {
        'acl_name': {
            Any(): {
                'cg_id': int,
                'protocol': str,
                'no_of_aces': int,
                'direction_ingress': str,
                'direction_egress': str
            },
        },
    }

# ============================================================================
#  Parser for
#  * 'show platform software fed active acl info summary'
#  * 'show platform software fed active acl info summary | include {acl_name}'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclInfoSummary(ShowPlatformSoftwareFedActiveAclInfoSummarySchema):
    """
    Parser for
    * 'show platform software fed active acl info summary'
    * 'show platform software fed active acl info summary | include {acl_name}'
    """

    cli_command = ['show platform software fed active acl info summary',
                   'show platform software fed active acl info summary | include {acl_name}']

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                output = self.device.execute(self.cli_command[1].format(acl_name=acl_name))
            else:
                output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        #CG id    ACL name                                    No of ACEs  Protocol  Ingress    Egress
        p1 = re.compile(r'^(?P<cg_id>\S+)\s+(?P<acl_name>\S+)\s+(?P<no_of_aces>\S+)\s+(?P<protocol>\S+)\s+(?P<direction_ingress>\w+)\s+(?P<direction_egress>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # CG id    ACL name                                    No of ACEs  Protocol  Ingress    Egress
            m = p1.match(line)
            if m:
                group = m.groupdict()

                # convert str to int
                key_list = ["cg_id", "no_of_aces"]
                for key in key_list:
                    group[key] = int(group[key])

                # pull a key from dict to use as new_key
                new_key = 'acl_name'
                info_dict = {group[new_key]: {}}
                # update then pop new_key from the dict
                info_dict[group[new_key]].update(group)
                info_dict[group[new_key]].pop(new_key)

                if not ret_dict.get(new_key):
                    # initialize the dict with new_key
                    ret_dict[new_key] = {}

                ret_dict[new_key].update(info_dict)
                continue

        return ret_dict