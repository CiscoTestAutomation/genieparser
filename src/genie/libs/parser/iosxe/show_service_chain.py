"""show_service_chain.py
   IOSXE parsers for the following show commands:
     * show platform software sdwan service-chain database summary
     * show platform software sdwan service-chain stats detail
     * show platform hardware qfp active feature sdwan datapath statistics
     * show endpoint-tracker
     * show track dynamic
"""
#python
import re
import logging
logger = logging.getLogger(__name__)

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,Or,And,Default,Use

# ========================================================================
# Schema for 'show platform software sdwan service-chain database summary'
# ========================================================================
class ShowSdwanServiceChainDatabaseSummarySchema(MetaParser):
    """Schema for 'show platform software sdwan service-chain database summary'
    """
    schema = {
        'service_chain': {
            Any(): {
                'vrf': int,
                'srv_count': int,
                'label': int,
                'status': str
            }
        }
    }

# =======================================================================
#  Parser for show platform software sdwan service-chain database summary
# =======================================================================
class ShowSdwanServiceChainDatabaseSummary(ShowSdwanServiceChainDatabaseSummarySchema):
    """Parser for 'show platform software sdwan service-chain database summary'
    """

    cli_command = "show platform software sdwan service-chain database summary"

    def cli(self, output=None):

        # Get output by executing cmd on device
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # SC1   101    4      1014      Up
        p1 = re.compile(r'^(?P<sc>\S+)\s+(?P<vrf>\d+)\s+(?P<srv_count>\d+)\s+(?P<label>\d+)\s+(?P<status>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # SC1   101    4      1014      Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                srv_dict = ret_dict.setdefault('service_chain', {})
                sc_dict = srv_dict.setdefault(group['sc'], {})
                sc_dict.update({
                    'vrf': int(group['vrf']),
                    'srv_count': int(group['srv_count']),
                    'label': int(group['label']),
                    'status': group['status']
                })
                continue

        return ret_dict

# ========================================================================
# Schema for 'show platform software sdwan service-chain stats detail'
# ========================================================================
class ShowSdwanServiceChainStatsDetailSchema(MetaParser):
    """Schema for 'show platform software sdwan service-chain stats detail'
    """
    schema = {
        'service_chain': {
            str: {
                'vrf': int,
                'label': int,
                'status': str,
                'service': {
                    str: {
                        'sent': int,
                        'rcvd': int,
                        int: {
                            str: {
                                str: {
                                    'sent': int,
                                    'rcvd': int
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =======================================================================
#  Parser for show platform software sdwan service-chain stats detail
# =======================================================================
class ShowSdwanServiceChainStatsDetail(ShowSdwanServiceChainStatsDetailSchema):
    """Parser for 'show platform software sdwan service-chain stats detail'
    """

    cli_command = "show platform software sdwan service-chain stats detail"

    def cli(self, output=None):

        # Get output by executing cmd on device
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # Summary: SC1, VRF: 101, Label: 1014, Status: Up
        p1 = re.compile(r'^Summary:\s+(?P<sc>\S+)\,\s+VRF:\s+(?P<vrf>\d+)\,\s+Label:\s+(?P<label>\d+)\,\s+Status:\s+(?P<status>\w+)$')

        # Service: FW Sent: 3151958519 Rcvd: 3126458239
        p2 = re.compile(r'^Service:\s+(?P<service>\S+)\s+Sent:\s+(?P<t_send>\d+)\s+Rcvd:\s+(?P<t_rcvd>\d+)$')

        # HA Pair 1: IPv4
        # HA Pair 1: IPv6
        # HA Pair 2: Tunnel IPv6
        # HA Pair 3: Tunnel IPv4
        p3 = re.compile(r'^HA\s+Pair\s+(?P<ha_num>\d+):\s+(?P<type>[\S\s]+)$')

        # Active Sent: 1101144045 Rcvd: 1101143388
        p4 = re.compile(r'^(?P<ha_mode>(Active|Backup))\s+Sent:\s+(?P<ha_send>\d+)\s+Rcvd:\s+(?P<ha_rcvd>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # SC1   101    4      1014      Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                chain_dict = ret_dict.setdefault('service_chain', {})
                sc_dict = chain_dict.setdefault(group['sc'], {})
                sc_dict.update({
                    'vrf': int(group['vrf']),
                    'label': int(group['label']),
                    'status': group['status']
                })
                continue
            
            # Service: FW Sent: 3151958519 Rcvd: 3126458239
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ser_dict = sc_dict.setdefault('service', {})
                srv_dict = ser_dict.setdefault(group['service'], {})
                srv_dict.update({
                    'sent': int(group['t_send']),
                    'rcvd': int(group['t_rcvd'])
                })
                continue

            # HA Pair 1: IPv4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_type = m.groupdict()['type'].lower()
                if group['type'] == "Tunnel IPv4":
                    intf_type = "tunnelv4"
                if group['type'] == "Tunnel IPv6":
                    intf_type = "tunnelv6"
                ha_dict = srv_dict.setdefault(int(group['ha_num']), {}).setdefault(intf_type, {})
                continue

            # Active Sent: 1101144045 Rcvd: 1101143388
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ha_mode = group['ha_mode'].lower()
                type_dict = ha_dict.setdefault(ha_mode, {})
                type_dict.update({
                    'sent': int(group['ha_send']),
                    'rcvd': int(group['ha_rcvd'])
                })
                continue
            
        return ret_dict

# =============================================================================================
# Schema for 'show platform hardware qfp active feature sdwan datapath statistics'
# =============================================================================================
class ShowSdwanQfpActiveDatapathStatsSchema(MetaParser):
    """Schema for 'show platform hardware qfp active feature sdwan datapath statistics'
    """
    schema = {
        'statistics': {
            Any(): int
        }
    }

# ===============================================================================
#  Parser for show platform hardware qfp active feature sdwan datapath statistics
# ===============================================================================
class ShowSdwanQfpActiveDatapathStats(ShowSdwanQfpActiveDatapathStatsSchema):
    """Parser for 'show platform hardware qfp active feature sdwan datapath statistics'
    """

    cli_command = "show platform hardware qfp active feature sdwan datapath statistics | include {filter}"

    def cli(self, filter=None, output=None):

        # Get output by executing cmd on device
        if output is None:
            output = self.device.execute(self.cli_command.format(filter=filter))
    
        # initial return dictionary
        ret_dict = {}

        # ipv4-acl-in-sc-strict-drop   57
        p1 = re.compile(r'^(?P<type>\S+)\s+(?P<drop>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # ipv4-acl-in-sc-strict-drop   57
            m = p1.match(line)
            if m:
                group = m.groupdict()
                drop_dict = ret_dict.setdefault('statistics', {})
                drop_dict.update({group['type']: int(group['drop'])})
                continue
    
        return ret_dict

# ====================================
# Schema for 'show endpoint-tracker'
# ====================================
class ShowEndpointTrackerSchema(MetaParser):
    """Schema for 'show endpoint-tracker'
    """
    schema = {
        'tracker': {
            Any(): {
                'status': str,
                'interface': str,
                'af': str,
                'rtt': str,
                'probe_id': int,
                'next_hop': str
            }
        }
    }

# ====================================
#  Parser for show endpoint-tracker
# ====================================
class ShowEndpointTracker(ShowEndpointTrackerSchema):
    """Parser for 'show endpoint-tracker'
    """

    cli_command = "show endpoint-tracker"

    def cli(self, output=None):

        # Get output by executing cmd on device
        if output is None:
            output = self.device.execute(self.cli_command)
    
        # initial return dictionary
        ret_dict = {}

        # 201:101:22:t3                    t3                     Up              IPv4             1               1          192.168.46.1
        p1 = re.compile(r'^(?P<intf>\S+)\s+(?P<ep>\S+)\s+(?P<state>\S+)\s+(?P<addr>\S+)\s+(?P<rt>\S+)\s+(?P<probe>\d+)\s+(?P<hop>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #201:101:22:t3                    t3                     Up              IPv4             1               1          192.168.46.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                end_dict = ret_dict.setdefault('tracker', {}).setdefault(group['ep'], {})
                end_dict.update({
                    'status': group['state'].lower(),
                    'interface': group['intf'],
                    'af': group['addr'].lower(),
                    'rtt': group['rt'],
                    'probe_id': int(group['probe']),
                    'next_hop': group['hop']
                })
                continue
    
        return ret_dict

# ====================================
# Schema for 'show track dynamic'
# ====================================
class ShowTrackDynamicSchema(MetaParser):
    """Schema for 'show track dynamic'
    """
    schema = {
        'track': {
            Any(): {
                'state': str,
                'num_change': int,
                'last_change': str,
                'route_map': str
            }
        }
    }

# ====================================
#  Parser for show track dynamic
# ====================================
class ShowTrackDynamic(ShowTrackDynamicSchema):
    """Parser for 'show track dynamic'
    """

    cli_command = "show track dynamic"

    def cli(self, output=None):

        # Get output by executing cmd on device
        if output is None:
            output = self.device.execute(self.cli_command)
    
        # initial return dictionary
        ret_dict = {}

        # Track 20
        p1 = re.compile(r'^Track\s+(?P<id>\d+)$')

        # State is Up
        p2 = re.compile(r'^State\s+is\s+(?P<status>\S+)$')

        # 2 changes, last change 16:33:53
        p3 = re.compile(r'^(?P<num>\d+)\s+changes\,\s+last\s+change\s+(?P<time>\S+)$')

        # Route Map 0
        p4 = re.compile(r'^Route\s+Map\s+(?P<map>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Track 20
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tr_dict = ret_dict.setdefault('track', {}).setdefault(int(group['id']), {})
                continue

            # State is Up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tr_dict.update({
                    'state': group['status'].lower()
                })
                continue

            # 2 changes, last change 16:33:53
            m = p3.match(line)
            if m:
                group = m.groupdict()
                tr_dict.update({
                    'num_change': int(group['num']),
                    'last_change': group['time']
                })
                continue

            # Route Map 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                tr_dict.update({
                    'route_map': group['map']
                })
                continue
    
        return ret_dict
