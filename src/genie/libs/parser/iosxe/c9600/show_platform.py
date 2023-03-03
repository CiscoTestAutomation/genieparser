'''show_platform.py

IOSXE c9500 parsers for the following show commands:
   * show platform software object-manager {serviceprocessor} statistics
   * show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics
   * show platform software fed active ifm mappings
   * show platform hardware fed active fwd-asic resource tcam utilization
   * show platform software fed active acl info summary
   * show platform software fed active acl info summary | include {acl_name}
   * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
   * show platform software fed active fnf record-count asic {asic_num}
   * show platform software fed {switch} active fnf record-count asic {asic_num}
   * show platform software fed switch standby acl usage | include {acl_name}
   * show platform software fed switch standby acl usage
   * show platform hardware fed switch standby fwd-asic resource tcam utilization
   * show platform software bp crimson statistics
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

from genie.libs.parser.iosxe.c9500.show_platform import \
    ShowPlatformHardwareChassisPowerSupplyDetailAll as ShowPlatformHardwareChassisPowerSupplyDetailAll_c9500, \
    ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll as ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll_c9500, \
    ShowPlatformFedTcamPbrNat as ShowPlatformFedTcamPbrNat_c9500

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
                        Optional('IFG_ID'): str,
                        'Port': str,
                        'SubPort': str,
                        'Mac': str,
                        Optional('First_Serdes'): str,
                        Optional('Last_Serdes'): str,
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
        #p1 = re.compile(
        #    r'^(?P<interface>\S+)\s+(?P<ifId>\S+)\s+(?P<inst>\d+)\s+(?P<asic>\d+)\s+(?P<core>\d+)\s+(?P<ifgId>\d+)\s+(?P<port>\d+)\s+(?P<sbPort>\d+)\s+(?P<mac>\d+)\s+(?P<first_serdes>\d+)\s+(?P<last_serdes>\d+)\s+(?P<cntx>\d+)\s+(?P<lpn>\d+)\s+(?P<gpn>\d+)\s+(?P<type>\w+)\s+(?P<act>\w+)$')
        
        #Interface IF_ID Inst Asic Core Port SubPort Mac Cntx LPN GPN Type Active
        #FortyGigabitEthernet1/0/1 0x75 0 0 0 0 0 0 0 1 101 NIF N

        p1 = re.compile(
            r'^(?P<interface>\S+)\s+(?P<ifId>\S+)\s+(?P<inst>\d+)\s+(?P<asic>\d+)\s+(?P<core>\d+)\s+(?P<ifgId>\d+)?\s+(?P<port>\d+)\s+(?P<sbPort>\d+)\s+(?P<mac>\d+)\s+(?P<first_serdes>\d+)?\s+(?P<last_serdes>\d+)?\s+(?P<cntx>\d+)\s+(?P<lpn>\d+)\s+(?P<gpn>\d+)\s+(?P<type>\w+)\s+(?P<act>\w+)$')
            
        for line in output.splitlines():
            line = line.strip()
            # HundredGigE1/0/21       0x4d6    0   0    0      0    0      0     1   0            1            0    1    1    NIF    Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intfId = group['interface']
                final_dict = ret_dict.setdefault('interface', {}).setdefault(intfId, {})
                final_dict['IF_ID'] = group['ifId']
                final_dict['Inst'] = group['inst']
                final_dict['Asic'] = group['asic']
                final_dict['Core'] = group['core']
                if group['ifgId'] is not None:
                    final_dict['IFG_ID'] = group['ifgId']
                final_dict['Port'] = group['port']
                final_dict['SubPort'] = group['sbPort']
                final_dict['Mac'] = group['mac']
                if group['first_serdes'] is not None:
                    final_dict['First_Serdes'] = group['first_serdes']
                if group['last_serdes'] is not None:
                    final_dict['Last_Serdes'] = group['last_serdes']
                final_dict['Cntx'] = group['cntx']
                final_dict['LPN'] = group['lpn']
                final_dict['GPN'] = group['gpn']
                final_dict['Type'] = group['type']
                final_dict['Active'] = group['act']	
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
        


class ShowPlatformHardwareChassisPowerSupplyDetailAll(ShowPlatformHardwareChassisPowerSupplyDetailAll_c9500):
    """ Parser for show platform hardware chassis power-supply detail all"""
    pass
    
    
class ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll(ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll_c9500):
    """ Parser for show platform hardware chassis power-supply detail switch {mode} all"""
    pass

class ShowPlatformFedTcamPbrNat(ShowPlatformFedTcamPbrNat_c9500):
    """ Parser for show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}"""
    pass    

# ============================================================
#  Schema for 'show platform software fed active fnf record-count asic <asic num>'
# ============================================================
class ShowPlatformFedActiveFnfRecordCountAsicNumSchema(MetaParser):
    """Schema for show platform software fed active fnf record-count asic <asic num>
            show platform software fed switch active fnf record-count asic <asic num>"""

    schema = {
        "current_flow_count": int,
        "total_flows_learned": int,
        "hash_searched_flow_count": int,
        "overflow_searched_flow_count": int,
        "hash_unsearched_flow_count": int,
        "overflow_unsearched_flow_count": int,
        "total_flow_searched": int,
        "total_search_failures": int,
        "total_avc_cpu_copy_disable": int,
        "total_eta_cpu_copy_disable": int,
        "total_cpu_copy_disable": int,
        "total_avc_feature_flows": int,
        "total_eta_feature_flows": int,
        "total_eta_and_avc_feature_flows": int,
        "total_num_eta_flows_agedout": int,
        Optional("reflexive_claimed_flow"): int,
        Optional("reflexive_claimed_flow_deleted"): int,
        Optional("reflexive_stale_flow_aged_out"): int,
        Optional("reflexive_flow_deleted"): int,
        "total_flows_deleted": int,
        "total_delete_failures": int,
        "total_flow_aged_out": int,
        "total_stale_flow_deleted": int,
        "total_stale_flow_del_aborted": int,
        "total_packets_aged_out": int,
        "total_bytes_aged_out": int
        }

# ============================================================================
#  Parser for
#  * 'show platform software fed active fnf record-count asic <asic num>'
#  * 'show platform software fed switch active fnf record-count asic <asic num>'
# ============================================================================
class ShowPlatformFedActiveFnfRecordCountAsicNum(ShowPlatformFedActiveFnfRecordCountAsicNumSchema):
    """
    Parser for
    * 'show platform software fed active fnf record-count asic {asic_num}'
    * 'show platform software fed switch {state} fnf record-count asic {asic_num}'
    """

    cli_command = ['show platform software fed active fnf record-count asic {asic_num}',
                   'show platform software fed switch {state} fnf record-count asic {asic_num}']

    def cli(self, asic_num="", state=None, output=None):
        if output is None:
            if state:
                cmd = self.cli_command[1].format(state=state, asic_num=asic_num)
            else:
                cmd = self.cli_command[0].format(asic_num=asic_num)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<pattern>[\S ]+)= +(?P<value>\d+)$')

        # Current flow count               = 0
        # Total flows learned              = 0
        # Hash searched flow count         = 0
        # Overflow searched flow count     = 0
        # Hash unsearched flow count       = 0
        # Overflow unsearched flow count   = 0
        # Total flow Searched              = 0
        # Total search failures            = 0
        # Total AVC cpu copy disable       = 0
        # Total ETA cpu copy disable       = 0
        # Total cpu copy disable           = 0
        # Total AVC feature flows          = 0
        # Total ETA feature flows          = 0
        # Total ETA and AVC feature flows  = 0
        # Total num_eta_flows_agedout      = 0
        # Reflexive claimed flow           = 0
        # Reflexive flow deleted           = 0
        # Reflexive stale flow aged out    = 0
        # Total flows deleted              = 0
        # Total delete failures            = 0
        # Total flow aged out              = 0
        # Total stale flow deleted         = 0
        # Total stale flow del aborted     = 0
        # Total packets aged out           = 0
        # Total bytes aged out             = 0

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_')
                ret_dict.update({scrubbed.lower(): int(group['value'])})
                continue
        return ret_dict 

# ============================================================
#  Schema for 'show platform software fed switch active ifm mappings'
# ============================================================
class ShowPlatformFedSwitchActiveIfmMappingSchema(MetaParser):
    """Schema for show platform software fed switch active ifm mappings"""

    schema = {'interface':
                  {Any():
                       {'IF_ID': str,
                        'Inst': int,
                        'Asic': int,
                        'Core': int,
                        'Port': int,
                        'SubPort': int,
                        'Mac': int,
                        'Cntx': int,
                        'LPN': int,
                        'GPN': int,
                        'Type': str,
                        'Active': str,
                        }
                   },
              }

# ============================================================
#  Parser for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformFedSwitchActiveIfmMapping(ShowPlatformFedSwitchActiveIfmMappingSchema):
    """ Parser for show platform software fed switch active ifm mappings"""

    cli_command = 'show platform software fed {switch} {state} ifm mappings'

    def cli(self, switch="switch", state="active", output=None):

        if output is None:
            cmd = self.cli_command.format(switch=switch, state=state)
            # Execute command to get output from device
            output = self.device.execute(cmd)

        # initialize variables
        ret_dict = {}

        # HundredGigE1/0/21       0x4d6    0   0    0      0    0      0     1  0            1            0    1    1    NIF    Y
        p1 = re.compile(
            r'^(?P<interface>\S+)\s+(?P<ifId>\S+)\s+(?P<inst>\d+)\s+(?P<asic>\d+)\s+(?P<core>\d+)\s+(?P<ifgId>\d+)?\s+(?P<port>\d+)\s+(?P<sbPort>\d+)\s+(?P<mac>\d+)\s+(?P<first_serdes>\d+)?\s+(?P<last_serdes>\d+)?\s+(?P<cntx>\d+)\s+(?P<lpn>\d+)\s+(?P<gpn>\d+)\s+(?P<type>\w+)\s+(?P<act>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE1/0/21       0x4d6    0   0    0      0    0      0     1   0            1            0    1    1    NIF    Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intfId = group['interface']
                ifId = group['ifId']
                instance = int(group['inst'])
                asic = int(group['asic'])
                core = int(group['core'])
                port = int(group['port'])
                subPort = int(group['sbPort'])
                mac = int(group['mac'])
                cntx = int(group['cntx'])
                lpn = int(group['lpn'])
                gpn = int(group['gpn'])
                type = group['type']
                active = group['act']
                final_dict = ret_dict.setdefault('interface', {}).setdefault(intfId, {})
                final_dict['IF_ID'] = ifId
                final_dict['Inst'] = instance
                final_dict['Asic'] = asic
                final_dict['Core'] = core
                final_dict['Port'] = port
                final_dict['SubPort'] = subPort
                final_dict['Mac'] = mac
                final_dict['Cntx'] = cntx
                final_dict['LPN'] = lpn
                final_dict['GPN'] = gpn
                final_dict['Type'] = type
                final_dict['Active'] = active
                continue
        return ret_dict

# =========================================================
#  Schema for
#  * 'show platform software fed switch standby acl usage'
#  * 'show platform software fed switch standby acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchStandbyAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch standby acl usage
    """
    schema = {
        Optional('acl_usage'): {
            Optional('ace_software'): {
                 Optional('vmr_max'): int,
                 Optional('used'): int,
             },
            'acl_name': {
                Any(): {
                    'direction': {
                        Any(): {
                            'feature_type': str,
                            'acl_type': str,
                            'entries_used': int,
                        },
                    },
                },
            },
        }
    }

# =========================================================
#  Parser for
#  * 'show platform software fed switch standby acl usage'
#  * 'show platform software fed switch standby acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchStandbyAclUsage(ShowPlatformSoftwareFedSwitchStandbyAclUsageSchema):
    """
    Parser for :
        * show platform software fed switch standby acl usage
        * show platform software fed switch standby acl usage | include {acl_name}
    """

    cli_command = ['show platform software fed switch standby acl usage',
                   'show platform software fed switch standby acl usage | include {acl_name}']

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # #####  ACE Software VMR max:196608 used:253
        p1 = re.compile(r'^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$')

        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(r'^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault('acl_usage', {})

            # #####  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault('acl_usage', {})
                ace_software = acl_usage.setdefault('ace_software', {})

                vmr_max = group['vmr_max']
                ace_software['vmr_max'] = int(vmr_max)

                used = group['used']
                ace_software['used'] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault('acl_name', {}).setdefault(
                    Common.convert_intf_name(group['name']), {})
                direction = acl_name.setdefault('direction', {}).setdefault(
                    Common.convert_intf_name(group['direction']), {})

                direction['feature_type'] = group['feature_type']
                direction['acl_type'] = group['acl_type']
                direction['entries_used'] = int(group['entries_used'])
                continue
        return ret_dict

# =========================================================
#  Schema for
#  * 'show platform hardware fed switch standby fwd-asic resource tcam utilization'
# =========================================================
class ShowPlatformTcamUtilizationswitchStandbySchema(MetaParser):
    """Schema for show platform hardware fed switch standby fwd-asic resource tcam utilization """
    schema = {
        'asic': {
            Any(): {
                'table': {
                    Any(): {
                        'subtype': {
                            Any(): {
                                'direction': {
                                    Any(): {
                                        'max': str,
                                        'used': str,
                                        'used_percent': str,
                                        'v4': str,
                                        'v6': str,
                                        'mpls': str,
                                        'other': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =========================================================
#  Parser for
#  * 'show platform hardware fed sw standby fwd-asic resource tcam utilization'
# =========================================================
class ShowPlatformSwitchStandbyTcamUtilization(ShowPlatformTcamUtilizationswitchStandbySchema):
    """Parser for show platform hardware fed sw standby fwd-asic resource tcam utilization """

    cli_command = 'show platform hardware fed switch standby fwd-asic resource tcam utilization'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # CAM Utilization for ASIC  [0]
        p1 = re.compile(r'CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        #CTS Cell Matrix/VPN
        #Label                  EM           O       16384        0    0.00%        0        0        0        0
        #CTS Cell Matrix/VPN
        #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
        # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
        p2 = re.compile(r'(?P<table>.*(\S+)) +(?P<subtype>\S+) +(?P<direction>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            # CAM Utilization for ASIC  [0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #CTS Cell Matrix/VPN
            #Label                  EM           O       16384        0    0.00%        0        0        0        0
            #CTS Cell Matrix/VPN
            #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
            # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
            m = p2.match(line)
            if m:
                group = m.groupdict()
                table_ = group.pop('table')
                if table_ == 'Label':
                    table_ = 'CTS Cell Matrix/VPN Label'
                subtype_ = group.pop('subtype')
                dir_ = group.pop('direction')
                dir_dict = asic_dict.setdefault('table', {}). \
                            setdefault(table_, {}). \
                            setdefault('subtype', {}). \
                            setdefault(subtype_, {}). \
                            setdefault('direction', {}). \
                            setdefault(dir_, {})
                dir_dict.update({k: v for k, v in group.items()})
                continue

        return ret_dict

# ============================================================================
#  Parser for
#  * 'show platform software bp crimson statistics'
# ============================================================================
class ShowPlatformSoftwareBpCrimsonStatisticsSchema(MetaParser):
    """
    Schema for show platform software bp crimson statistics
    """
    schema = {
        'bp_crimson_statistics':{
            Any():str,
        },
        'bp_svl_crimson_statistics':{
            Any():str,
        },
        'bp_remote_db_statistics':{
            'get_requests':{
                Any():str,
        },
            'set_requests':{
                Any():str,
        },
            'in_progress_requests':{
                Any():str,
        },
            'dbal_response_time':{
            'max_(ms)': int,
        },
            'record_free_failures':{
                Any():str,
            },
        },
    }
class ShowPlatformSoftwareBpCrimsonStatistics(ShowPlatformSoftwareBpCrimsonStatisticsSchema):
    """ Parser for show platform software bp crimson statistics"""

    cli_command = 'show platform software bp crimson statistics'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # BP Crimson Statistics
        p1 = re.compile(r'^(?P<bp_crimson_statistics>BP Crimson Statistics)$')

        # Initialized            : Yes
        p2 = re.compile(r'^(?P<description>[\w\'\s]+)\:\s+(?P<value>\w+)$')

        # BP SVL Crimson Statistics
        p3 = re.compile(r'^(?P<bp_svl_crimson_statistics>BP SVL Crimson Statistics)$')

        # BP Remote DB Statistics
        p4 = re.compile(r'^(?P<bp_remote_db_statistics>BP Remote DB Statistics)$')

        # GET Requests
        p5 = re.compile(r'^(?P<get_requests>GET Requests\:)$')

        # SET Requests
        p6 = re.compile(r'^(?P<set_requests>SET Requests\:)$')

        # In Progress Requests
        p7 = re.compile(r'^(?P<in_progress_requests>In Progress Requests\:)$')

        # DBAL Response Time
        p8 = re.compile(r'^(?P<dbal_response_time>DBAL Response Time\:)$')

        #MAX (ms)         : 115
        p9 = re.compile(r'MAX .ms.\s+\:\s+(?P<MAX>\d+)')

        # Record Free Failures
        p10 = re.compile('^(?P<record_free_failures>Record Free Failures\:)$')

        for line in output.splitlines():
            line=line.strip()
            # BP Crimson Statistics
            m=p1.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_crimson_statistics',{})
                continue

            # Initialized            : Yes
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict[group['description']] = group['value']
                continue

            # BP SVL Crimson Statistics
            m=p3.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_svl_crimson_statistics',{})
                continue

            # BP Remote DB Statistics
            m=p4.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_remote_db_statistics',{})
                continue

            # GET Requests 
            m=p5.match(line)
            if m:
                root_dict = root_dict.setdefault('get_requests',{})
                continue

            # SET Requests  
            m=p6.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_remote_db_statistics',{})
                root_dict = root_dict.setdefault('set_requests',{})
                continue

            # In Progress Requests
            m=p7.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_remote_db_statistics',{})
                root_dict = root_dict.setdefault('in_progress_requests',{})
                continue

            # DBAL Response Time
            m=p8.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_remote_db_statistics',{})
                root_dict = root_dict.setdefault('dbal_response_time',{})
                continue

            # MAX (ms)          
            m=p9.match(line)
            if m:
                group=m.groupdict()
                root_dict['max_(ms)']=int(group['MAX'])

            # Record Free Failures
            m=p10.match(line)
            if m:
                root_dict = ret_dict.setdefault('bp_remote_db_statistics',{})
                root_dict = root_dict.setdefault('record_free_failures',{})
                continue

        return ret_dict

# ======================================================================================
# Schema for 'show platform software memory switch <switch number> alloc callsite brief'
# ======================================================================================
class ShowPlatformSoftwareMemorySwitchCallsiteSchema(MetaParser):
    """ Schema for show platform software memory fed switch <switch_num> alloc callsite brief """
    schema = {
        'tracekey': {
            Any(): {
                'callsite': {
                    Any(): {
                        'thread': int,
                        'diff_byte': int,
                        'diff_call': int
                    }
                }
            }
        }
    }

# ======================================================================================
# Parser for 'show platform software memory switch <switch number> alloc callsite brief'
# ======================================================================================
class ShowPlatformSoftwareMemorySwitchAllocCallsite(ShowPlatformSoftwareMemorySwitchCallsiteSchema):
    """ Parser for show platform software memory fed switch <switch_num> alloc callsite brief """

    cli_command = ['show platform software memory fed switch {switch_num} alloc callsite brief', 'show platform software memory fed {switch_type} alloc callsite brief']

    def cli(self, switch_num="", switch_type="", output=None):
        if output is None:
            if switch_num is not None:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            elif switch_type is not None:
                cmd = self.cli_command[1].format(switch_type=switch_type)
            else:
                raise TypeError('Must pass either switch_num or switch_type')
            output = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        
        # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
        p1 = re.compile(r'^The +current +tracekey +is\s*: +(?P<tracekey>[#\w\d+]*)$')

        # callsite      thread    diff_byte               diff_call
        # ----------------------------------------------------------
        # 1617611779    31884     57424                   2
        p2 = re.compile(r'^(?P<callsite>(\d\w+))\s+(?P<thread>(\d+))\s+(?P<diffbyte>(\d+))\s+(?P<diffcall>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tracekey = group['tracekey']
                callsite_dict = parsed_dict.setdefault('tracekey', {}).setdefault(tracekey, {})
                continue

            # callsite      thread    diff_byte               diff_call
            # ----------------------------------------------------------
            # 1617611779    31884     57424                   2

            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = group['callsite']
                one_callsite_dict = callsite_dict.setdefault('callsite', {}).setdefault(callsite, {})
                one_callsite_dict['thread'] = int(group['thread'])
                one_callsite_dict['diff_byte'] = int(group['diffbyte'])
                one_callsite_dict['diff_call'] = int(group['diffcall'])
                continue
        return parsed_dict

#====================================================================================
# Schema for 'show platform software memory switch <switch_num> alloc backtrace'
#====================================================================================
class ShowPlatformSoftwareMemorySwitchBacktraceSchema(MetaParser):
    """ Schema for show platform software memory switch <switch_num> alloc backtrace,
    show platform software memory <active/standby> alloc backtrace """
    schema = {
        'backtrace': {
            Any(): {
                'callsite': {
                    Any(): {
                        'allocs': int,
                        'frees': int,
                        'call_diff': int,
                        'thread_id': int
                        }
                    }
                }
            }
        }

#====================================================================================
# Parser for 'show platform software memory switch <switch_num> alloc backtrace'
#====================================================================================
class ShowPlatformSoftwareMemorySwitchAllocBacktrace(ShowPlatformSoftwareMemorySwitchBacktraceSchema):
    """ Parser for show platform software memory fed switch <switch_num> alloc backtrace, show platform software memory fed <active/standby> alloc backtrace """

    cli_command = ['show platform software memory fed switch {switch_num} alloc backtrace', 'show platform software memory fed {switch_type} alloc backtrace']
    def cli(self, switch_num="", switch_type="", output=None):
        if output is None:
            if switch_num is not None:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            elif switch_type is not None:
                cmd = self.cli_command[1].format(switch_type=switch_type)
            else:
                raise TypeError('Must pass either switch_num or switch_type')
            output = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        
        # backtrace: 1#2315ece11e07bc883d89421df58e37b6
        p1 = re.compile(r'^backtrace: +(?P<backtrace>[#\w\d+]*)')

        #   callsite: 2150603778, thread_id: 31884
        p2 = re.compile(r'^callsite: +(?P<callsite>\d\w+), +thread_id: +(?P<thread_id>\d+)$')

        #   allocs: 1, frees: 0, call_diff: 1
        p3 = re.compile(r'^allocs: +(?P<allocs>(\d+)), +frees: +(?P<frees>(\d+)), +call_diff: +(?P<call_diff>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            # backtrace: 1#2315ece11e07bc883d89421df58e37b6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                backtrace = str(group['backtrace'])
                backtrace_dict = parsed_dict.setdefault('backtrace', {}).setdefault(backtrace, {})
                continue

            #   callsite: 2150603778, thread_id: 31884
            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = str(group['callsite'])
                backtraces_dict = backtrace_dict.setdefault('callsite', {}).setdefault(callsite, {})
                backtraces_dict['thread_id'] = int(group['thread_id'])
                continue

            #   allocs: 1, frees: 0, call_diff: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                backtraces_dict['allocs'] = int(group['allocs'])
                backtraces_dict['frees'] = int(group['frees'])
                backtraces_dict['call_diff'] = int(group['call_diff'])
                continue

        return parsed_dict

# ======================================================================================
# Schema for 'show platform hardware fed switch <> qos dscp-cos counters <interface>'
# ======================================================================================
class ShowPlatformHardwareFedSwitchQosDscpcosCountersSchema(MetaParser):
    """ Schema for show platform hardware fed switch <> qos dscp-cos counters <interface> """
    schema = {
        "@heading": str,
        "traffictype": {
            Any(): {            
                "frames": int,
                "bytes": int
                }
            }
    }
    
# ======================================================================================
# Parser for 'show platform hardware fed switch <> qos dscp-cos counters <interface>'
# ======================================================================================
class ShowPlatformHardwareFedSwitchQosDscpcosCounters(ShowPlatformHardwareFedSwitchQosDscpcosCountersSchema):
    """ Parser for show platform hardware fed switch <> qos dscp-cos counters <interface> """

    cli_command = ['show platform hardware fed switch {switch_num} qos dscp-cos counters interface {interface}','show platform hardware fed switch {switch_type} qos dscp-cos counters interface {interface}']
    def cli(self, interface, switch_num="", switch_type="", output=None):
        if output is None:
            if switch_num is not None:
                cmd = self.cli_command[0].format(switch_num=switch_num,interface=interface)
            elif switch_type is not None:
                cmd = self.cli_command[1].format(switch_type=switch_type,interface=interface)
            else:
                raise TypeError('Must pass either switch_num or switch_type')
            output = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        
        #               Frames        Bytes
        p1 = re.compile(r'^(?P<heading>\AFrames[\s]+ +Bytes)$')

        # Ingress DSCP0 0             0
        p2 = re.compile(r'^(?P<traffictype>[\w\s]*) +(?P<frames>\d+) +(?P<bytes>\d+)$')

        for lines in output.splitlines():
            line = lines.strip()

            #               Frames        Bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['@heading'] = group['heading']
                continue                

            # Ingress DSCP0 0             0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                traffictype = group['traffictype']
                type_dict = parsed_dict.setdefault('traffictype', {}).setdefault(traffictype, {})
                type_dict['frames'] = int(group['frames'])
                type_dict['bytes'] = int(group['bytes'])
                continue

        return parsed_dict

# =========================================================
#  Schema for
#  * 'show platform software fed switch active acl usage'
#  * 'show platform software fed switch active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchActivEAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch standby acl usage
    """
    schema = {
        Optional('acl_usage'): {
            Optional('ace_software'): {
                 Optional('vmr_max'): int,
                 Optional('used'): int,
             },
            'acl_name': {
                Any(): {
                    'direction': {
                        Any(): {
                            'feature_type': str,
                            'acl_type': str,
                            'entries_used': int,
                        },
                    },
                },
            },
        }
    }

# =========================================================
#  Parser for
#  * 'show platform software fed switch active acl usage'
#  * 'show platform software fed switch active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedSwitchActivEAclUsage(ShowPlatformSoftwareFedSwitchActivEAclUsageSchema):
    """
    Parser for :
        * show platform software fed switch active acl usage
        * show platform software fed switch active acl usage | include {acl_name}
    """

    cli_command = ['show platform software fed switch active acl usage',
                   'show platform software fed switch active acl usage | include {acl_name}']

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # #####  ACE Software VMR max:196608 used:253
        p1 = re.compile(r'^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$')

        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(r'^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault('acl_usage', {})

            # #####  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault('acl_usage', {})
                ace_software = acl_usage.setdefault('ace_software', {})

                vmr_max = group['vmr_max']
                ace_software['vmr_max'] = int(vmr_max)

                used = group['used']
                ace_software['used'] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault('acl_name', {}).setdefault(
                    Common.convert_intf_name(group['name']), {})
                direction = acl_name.setdefault('direction', {}).setdefault(
                    Common.convert_intf_name(group['direction']), {})

                direction['feature_type'] = group['feature_type']
                direction['acl_type'] = group['acl_type']
                direction['entries_used'] = int(group['entries_used'])
                continue
        return ret_dict

# =========================================================
#  Schema for
#  * 'show platform hardware fed {switch} active fwd-asic resource tcam utilization'
# =========================================================
class ShowPlatformTcamUtilizationswitchActiveSchema(MetaParser):
    """Schema for show platform hardware fed {switch} active fwd-asic resource tcam utilization """
    schema = {
        'asic': {
            Any(): {
                'table': {
                    Any(): {
                        'subtype': {
                            Any(): {
                                'dir': {
                                    Any(): {
                                        'max': str,
                                        'used': str,
                                        'used_percent': str,
                                        'v4': str,
                                        'v6': str,
                                        'mpls': str,
                                        'other': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =========================================================
#  Parser for
#  * 'show platform hardware fed {switch} active fwd-asic resource tcam utilization'
# =========================================================
class ShowPlatformSwitchActiveTcamUtilization(ShowPlatformTcamUtilizationswitchActiveSchema):
    """Parser for show platform hardware fed {switch} active fwd-asic resource tcam utilization """

    cli_command = 'show platform hardware fed {switch} active fwd-asic resource tcam utilization'

    def cli(self, switch='switch', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch))

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # CAM Utilization for ASIC  [0]
        p1 = re.compile(r'CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        #CTS Cell Matrix/VPN
        #Label                  EM           O       16384        0    0.00%        0        0        0        0
        #CTS Cell Matrix/VPN
        #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
        # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
        p2 = re.compile(r'(?P<table>.*(\S+)) +(?P<subtype>\S+) +(?P<dir>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            # CAM Utilization for ASIC  [0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #CTS Cell Matrix/VPN
            #Label                  EM           O       16384        0    0.00%        0        0        0        0
            #CTS Cell Matrix/VPN
            #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
            # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
            m = p2.match(line)
            if m:
                group = m.groupdict()
                table_ = group.pop('table')
                if table_ == 'Label':
                    table_ = 'CTS Cell Matrix/VPN Label'
                subtype_ = group.pop('subtype')
                dir_ = group.pop('dir')
                dir_dict = asic_dict.setdefault('table', {}). \
                            setdefault(table_, {}). \
                            setdefault('subtype', {}). \
                            setdefault(subtype_, {}). \
                            setdefault('dir', {}). \
                            setdefault(dir_, {})
                dir_dict.update({k: v for k, v in group.items()})
                continue

        return ret_dict        

