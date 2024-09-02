"""show_lisp_dynamic.py

    * show lisp all instance-id <instance_id> dynamic-eid detail
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
    * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
    * show lisp instance-id {instance_id} dynamic-eid summary
    * show lisp eid-table vrf {vrf} dynamic-eid summary
    * show lisp eid-table vlan {vlan} dynamic-eid summary
    * show lisp eid-table {eid_table} dynamic-eid summary
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
    * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
    * show lisp instance-id {instance_id} dynamic-eid
    * show lisp eid-table {eid_table} dynamic-eid
    * show lisp eid-table vrf {vrf} dynamic-eid
    * show lisp eid-table vlan {vlan} dynamic-eid
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
    * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
    * show lisp instance-id {instance_id} dynamic-eid detail
    * show lisp eid-table {eid-table} dynamic-eid detail
    * show lisp eid-table vrf {vrf} dynamic-eid detail
    * show lisp eid-table vlan {vlan} dynamic-eid detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_lisp_super import *

# =======================================================================
# Schema for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# =======================================================================
class ShowLispDynamicEidDetailSchema(MetaParser):

    ''' Schema for "show lisp all instance-id <instance_id> dynamic-eid detail" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {Optional('service'):
                    {Any():
                        {'etr':
                            {'local_eids':
                                {Any():
                                    {'dynamic_eids':
                                        {Any():
                                            {'dynamic_eid_name': str,
                                            'id': str,
                                            'rlocs': str,
                                            Optional('registering_more_specific'): bool,
                                            Optional('loopback_address'): str,
                                            Optional('priority'): int,
                                            Optional('weight'): int,
                                            Optional('record_ttl'): int,
                                            Optional('site_based_multicast_map_notify_group'): str,
                                            Optional('proxy_reply'): bool,
                                            Optional('registration_interval'): int,
                                            Optional('global_map_server'): bool,
                                            Optional('num_of_roaming_dynamic_eid'): int,
                                            Optional('mapping_servers'):
                                                {Any():
                                                    {Optional('proxy_reply'): bool,
                                                    },
                                                },
                                            Optional('last_dynamic_eid'):
                                                {Any():
                                                    {'last_dynamic_eid_discovery_elaps_time': str,
                                                    'eids':
                                                        {Any():
                                                            {'interface': str,
                                                            'uptime': str,
                                                            'last_activity': str,
                                                            'discovered_by': str,
                                                            },
                                                        },
                                                    },
                                                },
                                            Optional('eid_address'):
                                                {Optional('address_type'): str,
                                                Optional('virtual_network_id'): str,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =======================================================================
# Parser for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# =======================================================================
class ShowLispDynamicEidDetail(ShowLispDynamicEidDetailSchema):

    ''' Parser for "show lisp all instance-id <instance_id> dynamic-eid detail"'''

    cli_command = 'show lisp all instance-id {instance_id} dynamic-eid detail'

    def cli(self, instance_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(instance_id=instance_id))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<lisp_router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP Dynamic EID Information for VRF "red"
        p2 = re.compile(r'LISP +Dynamic +EID +Information +for +VRF'
                         ' +"(?P<vrf>(\S+))"$')

        # Dynamic-EID name: 192
        p3 = re.compile(r'Dynamic-EID +name: +(?P<eid_id>(\S+))$')

        # Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
        p4 = re.compile(r'Database-mapping +EID-prefix: +(?P<dyn_eid>(\S+)),'
                         ' +locator-set +(?P<locator_set_name>(\S+))$')

        # Registering more-specific dynamic-EIDs
        p5 = re.compile(r'Registering +more-specific +dynamic-EIDs$')

        # Map-Server(s): none configured, use global Map-Server
        p6 = re.compile(r'Map-Server\(s\)\: none configured, use global Map-Server$')

        # Map-Server(s): 10.64.4.4  (proxy-replying)
        # Map-Server(s): 10.144.6.6
        # Map-Server(s): 10:144:6:6::
        p6_1 = re.compile(r'Map-Server\(s\)\: +(?P<ms>([\d\.\:a-fA-F]+))'
                          r'(?: +\((?P<pr>(proxy-replying))\))?$')

        # Site-based multicast Map-Notify group: none configured
        # Site-based multicast Map-Notify group: 225.1.1.2
        # Site-based multicast Map-Notify group: 225:1:1:2::
        p7 = re.compile(r'Site-based +multicast +Map-Notify +group\:'
                        r' +(?P<map_notify>([a-zA-Z0-9\s]+)|([a-fA-F\d\:]+))$')

        # Number of roaming dynamic-EIDs discovered: 1
        p8 = re.compile(r'Number +of +roaming +dynamic-EIDs +discovered:'
                         ' +(?P<roam>(\d+))$')

        # Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
        p9 = re.compile(r'Last +dynamic-EID +discovered: +(?P<last>(\S+)),'
                         ' +(?P<time>(\S+)) +ago$')

        # 192.168.0.1, GigabitEthernet5, uptime: 01:17:25
        # 192:168:0:1::, GigabitEthernet5, uptime: 01:17:25
        p10 = re.compile(r'(?P<eid>([0-9\.]+)|([a-fA-F\d\:]+)), +(?P<interface>(\S+)),'
                         r' +uptime: +(?P<uptime>(\S+))$')

        #   last activity: 00:00:23, discovered by: Packet Reception
        p11 = re.compile(r'last +activity: +(?P<last>(\S+)), +discovered +by:'
                          ' +(?P<discovered_by>([a-zA-Z\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['lisp_router_id'])
                lisp_dict = parsed_dict.setdefault(
                    'lisp_router_instances', {}).setdefault(lisp_router_id, {})
                if group['instance_id']:
                    instance_id = group['instance_id']
                continue

            # LISP Dynamic EID Information for VRF "red"
            m = p2.match(line)
            if m:
                eid_vrf = m.groupdict()['vrf']
                continue

            # Dynamic-EID name: 192
            m = p3.match(line)
            if m:
                dynamic_eid_name = m.groupdict()['eid_id']
                continue

            # Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
            m = p4.match(line)
            if m:
                default_af = 'ipv4'
                group = m.groupdict()
                dyn_eid = group['dyn_eid']
                if ':' in dyn_eid:
                    default_af = 'ipv6'
                dynamic_eids_dict = lisp_dict.setdefault('service', {}).\
                                    setdefault(default_af, {}).\
                                    setdefault('etr', {}).\
                                    setdefault('local_eids', {}).\
                                    setdefault(instance_id, {}).\
                                    setdefault('dynamic_eids', {}).\
                                    setdefault(dyn_eid, {})

                # Set values
                dynamic_eids_dict['dynamic_eid_name'] =  dynamic_eid_name
                dynamic_eids_dict['id'] =  dyn_eid
                dynamic_eids_dict['rlocs'] = group['locator_set_name']
                if 'eid_address' not in dynamic_eids_dict:
                    dynamic_eids_dict['eid_address'] = {}
                try:
                    dynamic_eids_dict['eid_address']['virtual_network_id'] = eid_vrf
                except:
                    pass
                continue

            # Registering more-specific dynamic-EIDs
            m = p5.match(line)
            if m:
                dynamic_eids_dict['registering_more_specific'] = True
                continue

            # Map-Server(s): none configured, use global Map-Server
            m = p6.match(line)
            if m:
                dynamic_eids_dict['global_map_server'] = True
                continue

            # Map-Server(s): 10.64.4.4  (proxy-replying)
            # Map-Server(s): 10.144.6.6
            # Map-Server(s): 10:144:6:6::
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                mapserver = group['ms']
                ms_dict = dynamic_eids_dict.setdefault('mapping_servers', {}).\
                          setdefault(mapserver, {})
                if group['pr']:
                    ms_dict['proxy_reply'] = True
                continue

            # Site-based multicast Map-Notify group: none configured
            # Site-based multicast Map-Notify group: 225.1.1.2
            # Site-based multicast Map-Notify group: 225:1:1:2::
            m = p7.match(line)
            if m:
                dynamic_eids_dict['site_based_multicast_map_notify_group'] = \
                    m.groupdict()['map_notify']
                continue

            # Number of roaming dynamic-EIDs discovered: 1
            m = p8.match(line)
            if m:
                dynamic_eids_dict['num_of_roaming_dynamic_eid'] = int(m.groupdict()['roam'])

            # Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
            m = p9.match(line)
            if m:
                group = m.groupdict()
                last_eid = group['last']
                time = group['time']
                # Create dict
                last_dyn_dict = dynamic_eids_dict.\
                                    setdefault('last_dynamic_eid', {}).\
                                    setdefault(last_eid, {})
                last_dyn_dict['last_dynamic_eid_discovery_elaps_time'] = time
                continue

            # 192.168.0.1, GigabitEthernet5, uptime: 01:17:25
            # 192:168:0:1::, GigabitEthernet5, uptime: 01:17:25
            m = p10.match(line)
            if m:
                group = m.groupdict()
                eid = group['eid']
                interface = group['interface']
                uptime = group['uptime']
                last_eids_dict = last_dyn_dict.setdefault('eids', {}).\
                                    setdefault(eid, {})
                last_eids_dict['interface'] = interface
                last_eids_dict['uptime'] = uptime
                continue

            # last activity: 00:00:23, discovered by: Packet Reception
            m = p11.match(line)
            if m:
                group = m.groupdict()
                last_activity = group['last']
                discovered_by = group['discovered_by'].lower()
                last_eids_dict['last_activity'] = last_activity
                last_eids_dict['discovered_by'] = discovered_by
                continue

        return parsed_dict


class ShowLispDynamicEidSummarySchema(MetaParser):

    ''' Schema for
            * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
            * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
            * show lisp instance-id {instance_id} dynamic-eid summary
            * show lisp eid-table vrf {vrf} dynamic-eid summary
            * show lisp eid-table vlan {vlan} dynamic-eid summary
            * show lisp eid-table {eid_table} dynamic-eid summary
    '''

    schema = {
        "lisp_id": {
            int: {
                "instance_id": {
                    int: {
                        Optional("eid_table"): str,
                        Optional("dynamic_eids"): {
                            str: {
                                "eids": {
                                    str: {
                                        "interface": str,
                                        "uptime": str,
                                        "last_packet": str,
                                        "pending_ping_count": int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLispDynamicEidSummary(ShowLispDynamicEidSummarySchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
        * show lisp instance-id {instance_id} dynamic-eid summary
        * show lisp eid-table vrf {vrf} dynamic-eid summary
        * show lisp eid-table vlan {vlan} dynamic-eid summary
        * show lisp eid-table {eid_table} dynamic-eid summary
    """

    cli_command = [
       'show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary',
       'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary',
       'show lisp instance-id {instance_id} dynamic-eid summary',
       'show lisp eid-table vrf {vrf} dynamic-eid summary',
       'show lisp eid-table vlan {vlan} dynamic-eid summary',
       'show lisp eid-table {eid_table} dynamic-eid summary',
       ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None, eid_table=None):

        # init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                out = self.device.execute(self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                out = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif vrf:
                out = self.device.execute(self.cli_command[3].format(vrf=vrf))
            elif vlan:
                out = self.device.execute(self.cli_command[4].format(vlan=vlan))
            elif eid_table:
                out = self.device.execute(self.cli_command[5].format(eid_table=eid_table))
            else:
                return ret_dict
        else:
            out = output


        # LISP Dynamic EID Summary for router 0, IID 4100, EID-table VRF "red"
        # LISP Dynamic EID Summary for router 0, IID 101
        p1 = re.compile(r'^LISP +Dynamic +EID +Summary +for +router\s+(?P<lisp_id>\d+),\s+IID\s+'
                        r'(?P<instance_id>\d+)(, EID-table VRF\s+)?(?P<eid_table>.+)?$')

        # 192_168_1_0          192.168.1.1             Vl101         1d22h     never     0
        p2 = re.compile(r'^(?P<dynamic_eid_name>\S+)\s+(?P<eid>\S+)\s+(?P<interface>\S+)'
                        r'\s+(?P<uptime>\S+)\s+(?P<last_packet>\S+)\s+(?P<pending_ping_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # LISP Dynamic EID Summary for router 0, IID 4100, EID-table VRF "red"
            # LISP Dynamic EID Summary for router 0, IID 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {}) \
                        .setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                if group['eid_table']:
                    eid_table = group['eid_table'].replace('"','')
                    lisp_id_dict.update({'eid_table': eid_table})
                continue

            # 192_168_1_0          192.168.1.1             Vl101         1d22h     never     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dynamic_eid_dict = \
                    lisp_id_dict.setdefault('dynamic_eids', {})\
                                .setdefault(group['dynamic_eid_name'], {})
                each_eid_dict = \
                    dynamic_eid_dict.setdefault('eids', {})\
                                    .setdefault(group['eid'], {})

                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])

                each_eid_dict.update({
                    'interface': interface,
                    'uptime': group['uptime'],
                    'last_packet': group['last_packet'],
                    'pending_ping_count': int(group['pending_ping_count'])
                })
                continue

        return ret_dict


class ShowLispDynamicEid(ShowLispDynamicEidSuperParser, ShowLispDynamicEidSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
        * show lisp instance-id {instance_id} dynamic-eid
        * show lisp eid-table {eid_table} dynamic-eid
        * show lisp eid-table vrf {vrf} dynamic-eid
        * show lisp eid-table vlan {vlan} dynamic-eid
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} dynamic-eid',
        'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid',
        'show lisp instance-id {instance_id} dynamic-eid',
        'show lisp eid-table {eid_table} dynamic-eid',
        'show lisp eid-table vrf {vrf} dynamic-eid',
        'show lisp eid-table vlan {vlan} dynamic-eid',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None,
            eid_table=None):

        #init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            elif vrf:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))
            elif vlan:
                output = self.device.execute(self.cli_command[5].format(vlan=vlan))
            else:
                return ret_dict
        else:
            output = output

        return super().cli(output=output)


class ShowLispDynamicEidAllDetail(ShowLispDynamicEidSuperParser, ShowLispDynamicEidSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
        * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
        * show lisp instance-id {instance_id} dynamic-eid detail
        * show lisp eid-table {eid-table} dynamic-eid detail
        * show lisp eid-table vrf {vrf} dynamic-eid detail
        * show lisp eid-table vlan {vlan} dynamic-eid detail
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail',
        'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid detail',
        'show lisp instance-id {instance_id} dynamic-eid detail',
        'show lisp eid-table {eid_table} dynamic-eid detail',
        'show lisp eid-table vrf {vrf} dynamic-eid detail',
        'show lisp eid-table vlan {vlan} dynamic-eid detail',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None,
            eid_table=None):

        # init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            elif vrf:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))
            elif vlan:
                output = self.device.execute(self.cli_command[5].format(vlan=vlan))
            else:
                return ret_dict
        else:
            output = output

        return super().cli(output=output)


