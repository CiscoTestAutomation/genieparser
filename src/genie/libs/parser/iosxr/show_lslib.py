''' show_lslib.py

Parser for the following commands:
    * show lslib server producer <prod> instance-id <id>
    * show lslib server topology protocol ospfv3 nlri-type link detail
    * show lslib server topology-db protocol ospf nlri-type link detail
    * show lslib cache ospf <process_id> links attributes
'''

import re

import genie.metaparser.util.exceptions
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowLslibServerProducerInfoSchema(MetaParser):
    """
    Schema for parsing 'show lslib server producer <prod> instance-id <id>'
    """
    schema = {
            "producer": {
                Any(): {
                    "name": str,
                    "instance_identifier": int,
                    "local_identifier": int,
                    "connected_at": str,
                    "up_time": str,
                    "sod_received_at": str,
                    "eod_received_at": str,
                    "eod_pending": str,
                    "eod_timer_running": str,
                    "checkpointed": str,
                    "statistics": {
                        "markers": {
                            "sod": int,
                            "eod": int,
                            },
                        "nlri": {
                            Any(): {
                                "type": str,
                                "initial_data": {
                                    "update": int,
                                    "delete": int,
                                    "error": int,
                                    },
                                "cumulative": {
                                    "update": int,
                                    "delete": int,
                                    "error": int,
                                    }
                                }
                            }
                        }
                    }
                }
            }

class ShowLslibServerProducerInfo(ShowLslibServerProducerInfoSchema):
    """
    Parser for 'show lslib server producer <producer> instance-id <id>'
    'show lslib server producer detail'
    """

    cli_command = ['show lslib server producer {producer} instance-id {inst_id}',
                   'show lslib server producer detail']

    def cli(self, producer='', inst_id='', output=None):
        if output is None:
            if producer and id:
                out = self.device.execute(self.cli_command[0].format(producer=producer, inst_id=inst_id))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        ret_dict = {}
        producer_name = None
        nlri_section = False
        nlri_names = []
        stats_section = False

        # Producer: ospfv3
        p1 = re.compile(r'^Producer:\s*(?P<producer>\S+)$')
        # Instance Identifier: 10
        p2 = re.compile(r'^Instance Identifier:\s*(?P<instance>\d+)$')
        # Local Identifier: 1
        p3 = re.compile(r'^Local Identifier:\s*(?P<local>\d+)$')
        # Connected at: Aug 14 06:26:52
        p4 = re.compile(r'^Connected at:\s*(?P<connected>.+)$')
        # Up Time: 01:13:17
        p5 = re.compile(r'^Up Time:\s*(?P<uptime>\S+)$')
        # SOD received at: Aug 14 06:26:52.336
        p6 = re.compile(r'^SOD received at:\s*(?P<sod>.+)$')
        # EOD received at: Aug 14 06:26:52.336
        p7 = re.compile(r'^EOD received at:\s*(?P<eod>.+)$')
        # EOD Pending: No
        p8 = re.compile(r'^EOD Pending:\s*(?P<eod_pending>\S+)$')
        # EOD Timer running: No
        p9 = re.compile(r'^EOD Timer running:\s*(?P<eod_timer>\S+)$')
        # Checkpointed: Yes
        p10 = re.compile(r'^Checkpointed:\s*(?P<checkpointed>\S+)$')
        # Statistics:
        p11 = re.compile(r'^Statistics:$')
        # Markers
        p12 = re.compile(r'^Markers\s*$')
        # SOD       1
        p13 = re.compile(r'^SOD\s+(?P<sod>\d+)$')
        # EOD       1
        p14 = re.compile(r'^EOD\s+(?P<eod>\d+)$')
        #               InitialData          Cumulative
        p15 = re.compile(r'^InitialData\s+Cumulative\s*$')
        # NLRI      Update     Delete     Error          Update     Delete     Error
        p16 = re.compile(
                r'^NLRI\s+Update\s+Delete\s+Error\s+Update\s+Delete\s+Error\s*$')
        # Node      9          0          0              9          0          0
        # Link      32         0          0              32         0          0
        # Prefix    45         0          0              45         0          0
        p17 = re.compile(r'^(?P<nlri>[\w\s]+)\s+(?P<init_update>\d+)\s+(?P<init_delete>\d+)\s+(?P<init_error>\d+)\s+(?P<cum_update>\d+)\s+(?P<cum_delete>\d+)\s+(?P<cum_error>\d+)\s*$')

        for line in out.splitlines():
            line = line.strip()

            # Producer: ospfv3
            m = p1.match(line)
            if m:
                producer_name = m.group('producer')
                prod_dict = ret_dict.setdefault('producer', {}).setdefault(producer_name, {})
                prod_dict['name'] = producer_name
                continue

            # Instance Identifier: 10
            m = p2.match(line)
            if m and producer_name:
                prod_dict['instance_identifier'] = int(m.group('instance'))
                continue

            # Local Identifier: 1
            m = p3.match(line)
            if m and producer_name:
                prod_dict['local_identifier'] = int(m.group('local'))
                continue

            # Connected at: Aug 14 06:26:52
            m = p4.match(line)
            if m and producer_name:
                prod_dict['connected_at'] = m.group('connected')
                continue

            # Up Time: 01:13:17
            m = p5.match(line)
            if m and producer_name:
                prod_dict['up_time'] = m.group('uptime')
                continue

            # SOD received at: Aug 14 06:26:52.336
            m = p6.match(line)
            if m and producer_name:
                prod_dict['sod_received_at'] = m.group('sod')
                continue

            # EOD received at: Aug 14 06:26:52.336
            m = p7.match(line)
            if m and producer_name:
                prod_dict['eod_received_at'] = m.group('eod')
                continue

            # EOD Pending: No
            m = p8.match(line)
            if m and producer_name:
                prod_dict['eod_pending'] = m.group('eod_pending')
                continue

            # EOD Timer running: No
            m = p9.match(line)
            if m and producer_name:
                prod_dict['eod_timer_running'] = m.group('eod_timer')
                continue

            # Checkpointed: Yes
            m = p10.match(line)
            if m and producer_name:
                prod_dict['checkpointed'] = m.group('checkpointed')
                continue

            # Statistics:
            m = p11.match(line)
            if m and producer_name:
                stats_section = True
                stats_dict = prod_dict.setdefault('statistics', {})
                continue

            # Markers
            m = p12.match(line)
            if m and stats_section:
                markers_dict = stats_dict.setdefault('markers', {})
                continue

            # SOD       1
            m = p13.match(line)
            if m and stats_section:
                markers_dict['sod'] = int(m.group('sod'))
                continue

            # EOD       1
            m = p14.match(line)
            if m and stats_section:
                markers_dict['eod'] = int(m.group('eod'))
                continue

            # InitialData          Cumulative
            m = p15.match(line)
            if m and stats_section:
                nlri_section = True
                continue

            # NLRI      Update     Delete     Error          Update     Delete     Error
            m = p16.match(line)
            if m and stats_section:
                continue

            # Node      9          0          0              9          0          0
            # Link      32         0          0              32         0          0
            # Prefix    45         0          0              45         0          0
            m = p17.match(line)
            if m and nlri_section:
                nlri = m.group('nlri').strip()
                nlri_dict = stats_dict.setdefault('nlri', {}).setdefault(nlri, {})
                nlri_dict['type'] = nlri
                # InitialData
                init_data_dict = nlri_dict.setdefault('initial_data', {})
                if nlri != 'Unknown':
                    init_data_dict['update'] = int(m.group('init_update'))
                    init_data_dict['delete'] = int(m.group('init_delete'))
                init_data_dict['error'] = int(m.group('init_error'))
                # Cumulative
                cumu_data_dict = nlri_dict.setdefault('cumulative', {})
                if nlri != 'Unknown':
                    cumu_data_dict['update'] = int(m.group('cum_update'))
                    cumu_data_dict['delete'] = int(m.group('cum_delete'))
                cumu_data_dict['error'] = int(m.group('cum_error'))
                continue

        return ret_dict

class ShowLslibServerTopologyOspfv3NodeNlriSchema(MetaParser):
    """
    Schema for 'show lslib server topology-db protocol ospfv3 instance-id <id> nlri-type node detail'
    """
    schema = {
        "nlri": {
            Any(): {
                "nlri_str": str,
                "nlri_length_bytes": int,
                "attribute_length_bytes": int,
                "producers": {
                    Any(): {
                        "inst_id": int,
                        "producer": str,
                    },
                },
                "nlri_type": str,
                "protocol": str,
                "identifier": str,
                "local_node_descriptor": {
                    "as_number": int,
                    "bgp_identifier": str,
                    "area_id": str,
                    "router_id_ipv4": str
                },
                Optional("attributes"): {
                    "node_flag_bits": str,
                    "node_flags": str,
                },
            },
        }
    }


class ShowLslibServerTopologyOspfv3NodeNlri(ShowLslibServerTopologyOspfv3NodeNlriSchema):
    """
    Parser for 'show lslib server topology-db protocol ospfv3 instance-id <id> nlri-type node detail'
    """
    cli_command = ['show lslib server topology-db protocol ospfv3 instance-id {inst_id} nlri-type node detail']

    def cli(self, inst_id='0', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(inst_id=inst_id))
        else:
            out = output

        ret_dict = {}
        producers_dict = {}
        nlri_dict = None
        local_node = False

        # [V][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]]/376
        p1 = re.compile(r'^\[V\](?P<nlri>.+)$')

        # NLRI Length: 47 bytes
        p2 = re.compile(r'^NLRI Length:\s*(?P<length>\d+) bytes$')

        # Attribute Length: 5 bytes
        p3 = re.compile(r'^Attribute Length:\s*(?P<length>\d+) bytes$')

        # 10, ospfv3
        p4 = re.compile(r'^\s*(?P<idx>\d+),\s*(?P<name>\S+)$')

        # NLRI Type: Node
        p5 = re.compile(r'^NLRI Type:\s*(?P<type>.+)$')

        # Protocol: OSPFv3
        p6 = re.compile(r'^Protocol:\s*(?P<proto>.+)$')

        # Identifier: 0xa
        p7 = re.compile(r'^Identifier:\s*(?P<id>.+)$')

        # Local Node Descriptor:
        p8 = re.compile(r'^Local Node Descriptor:$')

        # AS Number: 0
        p9 = re.compile(r'^\s*AS Number:\s*(?P<asnum>\d+)$')

        # BGP Identifier: 0.0.0.0
        p10 = re.compile(r'^\s*BGP Identifier:\s*(?P<bgp>\S+)$')

        # Area ID: 0.0.0.0
        p11 = re.compile(r'^\s*Area ID:\s*(?P<area>\S+)$')

        # Router ID IPv4: 192.168.0.3
        p12 = re.compile(r'^\s*Router ID IPv4:\s*(?P<rid>\S+)$')

        # Attributes: Node flag bits: 10[A]
        # Attributes: Node flag bits: 30[EA]
        p13 = re.compile(r'^\s*Attributes: Node flag bits:\s*(?P<node_flag_bits>\d+)\[(?P<node_flag>.+?)\]$')

        for line in out.splitlines():
            line = line.strip()

            # [V][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]]/376
            m = p1.match(line)
            if m:
                nlri = line
                nlri_dict = ret_dict.setdefault('nlri', {}).setdefault(nlri, {})
                nlri_dict["nlri_str"] = nlri
                continue

            # NLRI Length: 47 bytes
            m = p2.match(line)
            if m:
                nlri_dict["nlri_length_bytes"] = int(m.group("length"))
                continue

            # Attribute Length: 5 bytes
            m = p3.match(line)
            if m:
                nlri_dict["attribute_length_bytes"] = int(m.group("length"))
                continue

            # 10, ospfv3
            m = p4.match(line)
            if m:
                producers_dict[int(m.group("idx"))] = {
                    "inst_id": int(m.group("idx")),
                    "producer": m.group("name").lower()
                }
                nlri_dict["producers"] = producers_dict
                continue

            # NLRI Type: Node
            m = p5.match(line)
            if m:
                nlri_dict["nlri_type"] = m.group("type").lower()
                continue

            # Protocol: OSPFv3
            m = p6.match(line)
            if m:
                nlri_dict["protocol"] = m.group("proto").lower()
                continue

            # Identifier: 0xa
            m = p7.match(line)
            if m:
                nlri_dict["identifier"] = m.group("id").lower()
                continue

            # Local Node Descriptor:
            m = p8.match(line)
            if m:
                local_node = True
                continue

            # AS Number: 0
            m = p9.match(line)
            if m and local_node:
                nlri_dict.setdefault("local_node_descriptor", {})
                nlri_dict["local_node_descriptor"]["as_number"] = int(m.group("asnum"))
                continue

            # BGP Identifier: 0.0.0.0
            m = p10.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["bgp_identifier"] = m.group("bgp")
                continue

            # Area ID: 0.0.0.0
            m = p11.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["area_id"] = m.group("area")
                continue

            # Router ID IPv4: 192.168.0.3
            m = p12.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["router_id_ipv4"] = m.group("rid")
                continue

            # Attributes: Node flag bits: 10[A]
            # Attributes: Node flag bits: 30[EA]
            m = p13.match(line)
            if m:
                attr_dict = nlri_dict.setdefault("attributes", {})
                attr_dict["node_flag_bits"] = m.group("node_flag_bits")
                attr_dict["node_flags"] = m.group("node_flag")
                continue

        return ret_dict

class ShowLslibServerTopologyOspfv3LinkNlriSchema(MetaParser):
    """
    Schema for 'show lslib server topology protocol ospfv3 instance-id <id> nlri-type link detail'
    """
    schema = {
            "nlri": {
                Any(): {
                    "nlri_str": str,
                    "nlri_length_bytes": int,
                    "attribute_length_bytes": int,
                    "producers": {
                        Any(): {
                            "inst_id": int,
                            "producer": str,
                        },
                    },
                    "nlri_type": str,
                    "protocol": str,
                    "identifier": str,
                    "local_node_descriptor": {
                        "as_number": int,
                        "bgp_identifier": str,
                        "area_id": str,
                        "router_id_ipv4": str
                        },
                    "remote_node_descriptor": {
                        "as_number": int,
                        "bgp_identifier": str,
                        "area_id": str,
                        "router_id_ipv4": str
                        },
                    "link_descriptor": {
                        "link_id": str
                        },
                    Optional("attributes"): {
                        "metric": int,
                        Optional("opaque_link_attr"): str
                        },
                    },
                },
            }


class ShowLslibServerTopologyOspfv3LinkNlri(ShowLslibServerTopologyOspfv3LinkNlriSchema):
    """
    Parser for 'show lslib server topology-db protocol ospfv3 instance-id <id> nlri-type link detail'
    """

    cli_command = ['show lslib server topology-db protocol ospfv3 instance-id {inst_id} nlri-type link detail']

    def cli(self, inst_id='0', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(inst_id=inst_id))
        else:
            out = output

        ret_dict = {}
        producers_dict = {}
        local_node = {}
        remote_node = {}
        link_desc = {}
        attributes = {}

        # [E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][R[c0][b0.0.0.0][a0.0.0.0][r192.168.0.4]][L[l64.35]]/760
        p1 = re.compile(r'^\[E\](?P<nlri>.+)$')

        # NLRI Length: 95 bytes
        p2 = re.compile(r'^NLRI Length:\s*(?P<length>\d+) bytes$')

        # Attribute Length: 7 bytes
        p3 = re.compile(r'^Attribute Length:\s*(?P<length>\d+) bytes$')

        # 10, ospfv3
        p4 = re.compile(r'^\s*(?P<idx>\d+),\s*(?P<name>\S+)$')

        # NLRI Type: Link
        p5 = re.compile(r'^NLRI Type:\s*(?P<type>.+)$')

        # Protocol: OSPFv3
        p6 = re.compile(r'^Protocol:\s*(?P<proto>.+)$')

        # Identifier: 0xa
        p7 = re.compile(r'^Identifier:\s*(?P<id>.+)$')

        # Local Node Descriptor:
        p8 = re.compile(r'^Local Node Descriptor:$')

        # Remote Node Descriptor:
        p9 = re.compile(r'^Remote Node Descriptor:$')

        # AS Number: 0
        p10 = re.compile(r'^\s*AS Number:\s*(?P<asnum>\d+)$')

        # BGP Identifier: 0.0.0.0
        p11 = re.compile(r'^\s*BGP Identifier:\s*(?P<bgp>\S+)$')

        # Area ID: 0.0.0.0
        p12 = re.compile(r'^\s*Area ID:\s*(?P<area>\S+)$')

        # Router ID IPv4: 192.168.0.3
        p13 = re.compile(r'^\s*Router ID IPv4:\s*(?P<rid>\S+)$')

        # Link Descriptor:
        p14 = re.compile(r'^Link Descriptor:$')

        # Link ID: 64.35
        p15 = re.compile(r'^\s*Link ID:\s*(?P<linkid>.+)$')

        # Attributes: metric: 10
        p16 = re.compile(r'^\s*Attributes: metric: (?P<metric>\d+)(?:, Opaque-link-attr: (?P<opaque>[\dA-Fa-fx\.]+))?$')

        # .00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d.43.5f.30.5f.30
        # .5f.30.20.20.20
        p17 = re.compile(r'^\s*\.(?P<opaque>.+)$')

        last_opaque = ""

        for line in out.splitlines():
            line = line.strip()

            # [E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][R[c0][b0.0.0.0][a0.0.0.0][r192.168.0.4]][L[l64.35]]/760
            m = p1.match(line)
            if m:
                nlri = '[E]' + m.group('nlri')
                nlri_dict = ret_dict.setdefault('nlri', {}).setdefault(nlri, {})
                nlri_dict["nlri_str"] = nlri
                continue

            # NLRI Length: 95 bytes
            m = p2.match(line)
            if m:
                nlri_dict["nlri_length_bytes"] = int(m.group("length"))
                continue

            # Attribute Length: 7 bytes
            m = p3.match(line)
            if m:
                nlri_dict["attribute_length_bytes"] = int(m.group("length"))
                continue

            # 10, ospfv3
            m = p4.match(line)
            if m:
                producers_dict[int(m.group("idx"))] = {
                    "inst_id": int(m.group("idx")),
                    "producer": m.group("name").lower()
                }
                nlri_dict["producers"] = producers_dict
                continue

            # NLRI Type: Link
            m = p5.match(line)
            if m:
                nlri_dict["nlri_type"] = m.group("type").lower()
                continue

            # Protocol: OSPFv3
            m = p6.match(line)
            if m:
                nlri_dict["protocol"] = m.group("proto").lower()
                continue

            # Identifier: 0xa
            m = p7.match(line)
            if m:
                nlri_dict["identifier"] = m.group("id")
                continue

            # Local Node Descriptor:
            m = p8.match(line)
            if m:
                local_node = True
                remote_node = False
                link = False

            # Remote Node Descriptor:
            m = p9.match(line)
            if m:
                remote_node = True
                local_node = False
                link = False

            # AS Number: 0
            m = p10.match(line)
            if m:
                if local_node:
                    if "local_node_descriptor" not in nlri_dict:
                        nlri_dict["local_node_descriptor"] = {}
                    nlri_dict["local_node_descriptor"]["as_number"] = int(m.group("asnum"))
                elif remote_node:
                    if "remote_node_descriptor" not in nlri_dict:
                        nlri_dict["remote_node_descriptor"] = {}
                    nlri_dict["remote_node_descriptor"]["as_number"] = int(m.group("asnum"))
                continue

            # BGP Identifier: 0.0.0.0
            m = p11.match(line)
            if m:
                if local_node:
                    nlri_dict["local_node_descriptor"]["bgp_identifier"] = m.group("bgp")
                elif remote_node:
                    nlri_dict["remote_node_descriptor"]["bgp_identifier"] = m.group("bgp")
                continue

            # Area ID: 0.0.0.0
            m = p12.match(line)
            if m:
                if local_node:
                    nlri_dict["local_node_descriptor"]["area_id"] = m.group("area")
                elif remote_node:
                    nlri_dict["remote_node_descriptor"]["area_id"] = m.group("area")
                continue

            # Router ID IPv4: 192.168.0.3
            m = p13.match(line)
            if m:
                if local_node:
                    nlri_dict["local_node_descriptor"]["router_id_ipv4"] = m.group("rid")
                elif remote_node:
                    nlri_dict["remote_node_descriptor"]["router_id_ipv4"] = m.group("rid")
                continue

            # Link Descriptor:
            m = p14.match(line)
            if m:
                local_node = False
                remote_node = False
                link = True
                continue

            # Link ID: 64.35
            m = p15.match(line)
            if m:
                if link:
                    if "link_descriptor" not in nlri_dict:
                        nlri_dict["link_descriptor"] = {}
                    nlri_dict["link_descriptor"]["link_id"] = m.group("linkid")
                continue

            # Attributes: metric: 1, Opaque-link-attr: 80.02.00.18.00
            m = p16.match(line)
            if m:
                attr_dict = nlri_dict.setdefault("attributes", {})
                attr_dict["metric"] = int(m.group("metric"))
                if m.group("opaque"):
                    # If opaque is present, store it
                    last_opaque = m.group("opaque").replace('.', '').replace(' ', '')
                    attr_dict["opaque_link_attr"] = last_opaque
                continue

            # .00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d.43.5f.30.5f.30
            # .5f.30.20.20.20
            m = p17.match(line)
            if m and last_opaque:
                # Remove dots and spaces, append to previous
                last_opaque += m.group("opaque").replace('.', '').replace(' ', '')
                attr_dict["opaque_link_attr"] = last_opaque
                continue

        return ret_dict

class ShowLslibServerTopologyOspfv3PrefixNlriSchema(MetaParser):
    """
    Schema for 'show lslib server topology-db protocol ospfv3 instance-id <id> nlri-type ipv6-prefix detail'
    """
    schema = {
        "nlri": {
            Any(): {
                "nlri_str": str,
                "nlri_length_bytes": int,
                "attribute_length_bytes": int,
                "producers": {
                    Any(): {
                        "inst_id": int,
                        "producer": str,
                    },
                },
                "nlri_type": str,
                "protocol": str,
                "identifier": str,
                "local_node_descriptor": {
                    "as_number": int,
                    "bgp_identifier": str,
                    "area_id": str,
                    "router_id_ipv4": str
                },
                "prefix_descriptor": {
                    "ospf_route_type": str,
                    "prefix": str
                },
                Optional("attributes"): {
                    "metric": int,
                },
            },
        }
    }

class ShowLslibServerTopologyOspfv3PrefixNlri(ShowLslibServerTopologyOspfv3PrefixNlriSchema):
    """
    Parser for 'show lslib server topology-db protocol ospfv3 instance-id <id> nlri-type ipv6-prefix detail'
    """
    cli_command = ['show lslib server topology-db protocol ospfv3 instance-id {inst_id} nlri-type ipv6-prefix detail']

    def cli(self, inst_id='0', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(inst_id=inst_id))
        else:
            out = output

        ret_dict = {}
        producers_dict = {}
        nlri_dict = None
        local_node = False
        prefix_desc = False

        # [T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][P[o0x01][p34:34:1::/64]]/520
        p1 = re.compile(r'^\[T\](?P<nlri>.+)$')
        # NLRI Length: 65 bytes
        p2 = re.compile(r'^NLRI Length:\s*(?P<length>\d+) bytes$')
        # Attribute Length: 8 bytes
        p3 = re.compile(r'^Attribute Length:\s*(?P<length>\d+) bytes$')
        # 10, ospfv3
        p4 = re.compile(r'^\s*(?P<idx>\d+),\s*(?P<name>\S+)$')
        # NLRI Type: Prefix
        p5 = re.compile(r'^NLRI Type:\s*(?P<type>.+)$')
        # Protocol: OSPFv3
        p6 = re.compile(r'^Protocol:\s*(?P<proto>.+)$')
        # Identifier: 0xa
        p7 = re.compile(r'^Identifier:\s*(?P<id>.+)$')
        # Local Node Descriptor:
        p8 = re.compile(r'^Local Node Descriptor:$')
        # AS Number: 0
        p9 = re.compile(r'^\s*AS Number:\s*(?P<asnum>\d+)$')
        # BGP Identifier: 0.0.0.0
        p10 = re.compile(r'^\s*BGP Identifier:\s*(?P<bgp>\S+)$')
        # Area ID: 0.0.0.0
        p11 = re.compile(r'^\s*Area ID:\s*(?P<area>\S+)$')
        # Router ID IPv4: 192.168.0.3
        p12 = re.compile(r'^\s*Router ID IPv4:\s*(?P<rid>\S+)$')
        # Prefix Descriptor:
        p13 = re.compile(r'^Prefix Descriptor:$')
        # OSPF Route Type: 0x01
        p14 = re.compile(r'^\s*OSPF Route Type:\s*(?P<rtype>0x[0-9A-Fa-f]+)$')
        # Prefix: 34:34:1::/64
        p15 = re.compile(r'^\s*Prefix:\s*(?P<prefix>.+)$')
        # Attributes: Metric: 10
        p16 = re.compile(r'^\s*Attributes: Metric: (?P<metric>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # [T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][P[o0x01][p34:34:1::/64]]/520
            m = p1.match(line)
            if m:
                nlri = '[T]' + m.group('nlri')
                nlri_dict = ret_dict.setdefault('nlri', {}).setdefault(nlri, {})
                nlri_dict["nlri_str"] = nlri
                continue

            # NLRI Length: 65 bytes
            m = p2.match(line)
            if m:
                nlri_dict["nlri_length_bytes"] = int(m.group("length"))
                continue

            # Attribute Length: 8 bytes
            m = p3.match(line)
            if m:
                nlri_dict["attribute_length_bytes"] = int(m.group("length"))
                continue

            # 10, ospfv3
            m = p4.match(line)
            if m:
                producers_dict[int(m.group("idx"))] = {
                    "inst_id": int(m.group("idx")),
                    "producer": m.group("name").lower()
                }
                nlri_dict["producers"] = producers_dict
                continue

            # NLRI Type: Prefix
            m = p5.match(line)
            if m:
                nlri_dict["nlri_type"] = m.group("type").lower()
                continue

            # Protocol: OSPFv3
            m = p6.match(line)
            if m:
                nlri_dict["protocol"] = m.group("proto").lower()
                continue

            # Identifier: 0xa
            m = p7.match(line)
            if m:
                nlri_dict["identifier"] = m.group("id")
                continue

            # Local Node Descriptor:
            m = p8.match(line)
            if m:
                local_node = True
                prefix_desc = False
                continue

            # AS Number: 0
            m = p9.match(line)
            if m and local_node:
                nlri_dict.setdefault("local_node_descriptor", {})
                nlri_dict["local_node_descriptor"]["as_number"] = int(m.group("asnum"))
                continue

            # BGP Identifier: 0.0.0.0
            m = p10.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["bgp_identifier"] = m.group("bgp")
                continue

            # Area ID: 0.0.0.0
            m = p11.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["area_id"] = m.group("area")
                continue

            # Router ID IPv4: 192.168.0.3
            m = p12.match(line)
            if m and local_node:
                nlri_dict["local_node_descriptor"]["router_id_ipv4"] = m.group("rid")
                continue

            # Prefix Descriptor:
            m = p13.match(line)
            if m:
                prefix_desc = True
                local_node = False
                continue

            # OSPF Route Type: 0x01
            m = p14.match(line)
            if m and prefix_desc:
                nlri_dict.setdefault("prefix_descriptor", {})
                nlri_dict["prefix_descriptor"]["ospf_route_type"] = m.group("rtype")
                continue

            # Prefix: 34:34:1::/64
            m = p15.match(line)
            if m and prefix_desc:
                nlri_dict.setdefault("prefix_descriptor", {})
                nlri_dict["prefix_descriptor"]["prefix"] = m.group("prefix")
                continue

            # Attributes: Metric: 10
            m = p16.match(line)
            if m:
                attr_dict = nlri_dict.setdefault("attributes", {})
                attr_dict["metric"] = int(m.group("metric"))
                continue

        return ret_dict

# =============================================================
# Schema for 'show lslib cache ospf <process_id> links attributes'
# =============================================================
class ShowLslibCacheOspfLinksAttributesSchema(MetaParser):
    """
    Schema for show lslib cache ospf <process_id> links attributes
    """
    schema = {
        'links': {
            Any(): {
                'local_link_id': int,
                'remote_link_id': int,
                'metric': int,
                'opaque_link_attr': str,
            }
        }
    }

class ShowLslibCacheOspfLinksAttributes(ShowLslibCacheOspfLinksAttributesSchema):
    """
    Parser for show lslib cache ospf <process_id> links attributes
    """
    cli_command = 'show lslib cache ospf {process_id} links attributes'

    def cli(self, process_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(process_id=process_id))
        else:
            out = output

        ret_dict = {}

        # [E][O][I0x0][N[c65535.65535][b255.255.255.255][a0.0.0.0][r1.1.1.1]][R[c65535.65535][b255.255.255.255][a0.0.0.0][r1.1.1.2]][L[i99.1.2.1][n99.1.2.2]]
        p1 = re.compile(r'^\[E\](?P<nlri>.+)$')
        # Attributes: Link ID: Local:109 Remote:16, metric: 1, Opaque-link-attr:
        p2 = re.compile(r'^Attributes: Link ID: Local:(\d+) Remote:(\d+), metric: (\d+), Opaque-link-attr: *$')
        # Attributes: Link ID: Local:15 Remote:44, Opaque-link-attr:
        p3 = re.compile(r'^Attributes: Link ID: Local:(\d+) Remote:(\d+), Opaque-link-attr:\s*$')
        # 80.02.00.18.00.00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d
        # .43.5f.30.5f.30.5f.32.20.20.20
        p4 = re.compile(r'^(?:\s*\.?)([0-9A-Fa-f]{2}(?:\.[0-9A-Fa-f]{2})+)')

        ret_dict = {'links': {}}

        for line in out.splitlines():
            line = line.strip()

            # [E][O][I0x0][N[c65535.65535][b255.255.255.255][a0.0.0.0][r1.1.1.1]][R[c65535.65535][b255.255.255.255][a0.0.0.0][r1.1.1.2]][L[i99.1.2.1][n99.1.2.2]]
            m = p1.match(line)
            if m:
                cur_link = '[E]' + m.group('nlri')
                ret_dict['links'][cur_link] = {}
                continue

            # Attributes: Link ID: Local:109 Remote:16, metric: 1, Opaque-link-attr:
            m = p2.match(line)
            if m and cur_link is not None:
                ret_dict['links'][cur_link]['local_link_id'] = int(m.group(1))
                ret_dict['links'][cur_link]['remote_link_id'] = int(m.group(2))
                ret_dict['links'][cur_link]['metric'] = int(m.group(3))
                ret_dict['links'][cur_link]['opaque_link_attr'] = ''
                continue

            # Attributes: Link ID: Local:15 Remote:44, Opaque-link-attr:
            m = p3.match(line)
            if m and cur_link is not None:
                ret_dict['links'][cur_link]['local_link_id'] = int(m.group(1))
                ret_dict['links'][cur_link]['remote_link_id'] = int(m.group(2))
                ret_dict['links'][cur_link]['metric'] = 0  # Default metric when not specified
                ret_dict['links'][cur_link]['opaque_link_attr'] = ''
                continue

            # 80.02.00.18.00.00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d
            # .43.5f.30.5f.30.5f.32.20.20.20
            m = p4.match(line)
            if m and cur_link is not None:
                hex_str = m.group(1).replace('.', '')
                ret_dict['links'][cur_link]['opaque_link_attr'] += hex_str
                continue

        return ret_dict

# =============================================================
# Schema for 'show lslib server topology-db protocol ospf nlri-type link detail'
# =============================================================
class ShowLslibServerTopologyDbOspfNlriTypeLinkDetailSchema(MetaParser):
    """
    Schema for show lslib server topology-db protocol ospf instance-id <id> nlri-type link detail
    """
    schema = {
        'links': {
            Any(): {
                'nlri_length': int,
                'attribute_length': int,
                'producers': {
                    Any(): {
                        'inst_id': int,
                        'producer': str,
                    },
                },
                'nlri_type': str,
                'protocol': str,
                'identifier': str,
                'local_node_descriptor': {
                    'as_number': int,
                    'bgp_identifier': str,
                    'area_id': str,
                    'router_id_ipv4': str,
                },
                'remote_node_descriptor': {
                    'as_number': int,
                    'bgp_identifier': str,
                    'area_id': str,
                    'router_id_ipv4': str,
                },
                'link_descriptor': {
                    'local_interface_address_ipv4': str,
                    'neighbor_interface_address_ipv4': str,
                },
                Optional('attributes'): {
                    'local_link_id': int,
                    'remote_link_id': int,
                    'metric': int,
                    Optional('opaque_link_attr'): str,
                }
            }
        }
    }

class ShowLslibServerTopologyDbOspfNlriTypeLinkDetail(ShowLslibServerTopologyDbOspfNlriTypeLinkDetailSchema):
    """
    Parser for show lslib server topology-db protocol ospf nlri-type link detail
    """
    cli_command = ['show lslib server topology-db protocol ospf instance-id {inst_id} nlri-type link detail']

    def cli(self, inst_id='0', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(inst_id=inst_id))
        else:
            out = output

        ret_dict = {}
        producers_dict = {}
        nlri_dict = None
        in_local_node = False
        in_remote_node = False
        in_link_desc = False

        # [E][O][I0x0][N[c0][b0.0.0.0][a0.0.0.0][r1.1.1.1]][R[c0][b0.0.0.0][a0.0.0.0][r1.1.1.2]][L[l64.35]]/792
        p1 = re.compile(r'^\[E\](?P<nlri>.+)$')
        # NLRI Length: 99 bytes
        p2 = re.compile(r'^NLRI Length: (\d+) bytes$')
        # Attribute Length: 51 bytes
        p3 = re.compile(r'^Attribute Length: (\d+) bytes$')
        # 0, ospf
        p4 = re.compile(r'^(\d+),\s*(\w+)$')
        # NLRI Type: Link
        p5 = re.compile(r'^NLRI Type: (.+)$')
        # Protocol: OSPF
        p6 = re.compile(r'^Protocol: (.+)$')
        # Identifier: 0x0
        p7 = re.compile(r'^Identifier: (.+)$')
        # Local Node Descriptor:
        p8 = re.compile(r'^Local Node Descriptor:$')
        # Remote Node Descriptor:
        p9 = re.compile(r'^Remote Node Descriptor:$')
        # Link Descriptor:
        p10 = re.compile(r'^Link Descriptor:')
        # AS Number: 0
        p11 = re.compile(r'^AS Number: (\d+)$')
        # BGP Identifier: 0.0.0.0
        p12 = re.compile(r'^BGP Identifier: ([\d\.]+)$')
        # Area ID: 0.0.0.0
        p13 = re.compile(r'^Area ID: ([\d\.]+)$')
        # Router ID IPv4: 1.1.1.1
        p14 = re.compile(r'^Router ID IPv4: ([\d\.]+)$')
        # Local Interface Address IPv4: 99.1.2.1
        p15 = re.compile(r'^Local Interface Address IPv4: ([\d\.]+)$')
        # Neighbor Interface Address IPv4: 99.1.2.2
        p16 = re.compile(r'^Neighbor Interface Address IPv4: ([\d\.]+)$')
        # Attributes: Link ID: Local:109 Remote:16, metric: 1, Opaque-link-attr:
        p17 = re.compile(r'^Attributes: Link ID: Local:(\d+) Remote:(\d+), metric: (\d+), Opaque-link-attr: *$')
        # 80.02.00.18.00.00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d
        # .43.5f.30.5f.30.5f.32.20.20.20
        p18 = re.compile(r'^(?:\s*\.?)([0-9A-Fa-f]{2}(?:\.[0-9A-Fa-f]{2})+)')

        for line in out.splitlines():
            line = line.strip()

            # [E][O][I0x0][N[c0][b0.0.0.0][a0.0.0.0][r1.1.1.1]][R[c0][b0.0.0.0][a0.0.0.0][r1.1.1.2]][L[i99.1.2.1][n99.1.2.2]]/792
            m = p1.match(line)
            if m:
                nlri = '[E]' + m.group(1)
                nlri_dict = ret_dict.setdefault('links', {}).setdefault(nlri, {})
                continue

            # NLRI Length: 99 bytes
            m = p2.match(line)
            if m and nlri_dict is not None:
                nlri_dict['nlri_length'] = int(m.group(1))
                continue

            # Attribute Length: 51 bytes
            m = p3.match(line)
            if m and nlri_dict is not None:
                nlri_dict['attribute_length'] = int(m.group(1))
                continue

            # 0, ospf
            m = p4.match(line)
            if m and nlri_dict is not None:
                producers_dict[int(m.group(1))] = {
                    'inst_id': int(m.group(1)),
                    'producer': m.group(2).lower()
                }
                nlri_dict['producers'] = producers_dict
                continue

            # NLRI Type: Link
            m = p5.match(line)
            if m and nlri_dict is not None:
                nlri_dict['nlri_type'] = m.group(1).lower()
                continue

            # Protocol: OSPF
            m = p6.match(line)
            if m and nlri_dict is not None:
                nlri_dict['protocol'] = m.group(1).lower()
                continue

            # Identifier: 0x0
            m = p7.match(line)
            if m and nlri_dict is not None:
                nlri_dict['identifier'] = m.group(1)
                continue

            # Local Node Descriptor:
            m = p8.match(line)
            if m and nlri_dict is not None:
                in_local_node = True
                in_remote_node = False
                in_link_desc = False
                nlri_dict['local_node_descriptor'] = {}
                continue

            # Remote Node Descriptor:
            m = p9.match(line)
            if m and nlri_dict is not None:
                in_local_node = False
                in_remote_node = True
                in_link_desc = False
                nlri_dict['remote_node_descriptor'] = {}
                continue

            # Link Descriptor:
            m = p10.match(line)
            if m and nlri_dict is not None:
                in_local_node = False
                in_remote_node = False
                in_link_desc = True
                nlri_dict['link_descriptor'] = {}
                continue

            # AS Number: 0
            m = p11.match(line)
            if m and nlri_dict is not None:
                if in_local_node:
                    nlri_dict['local_node_descriptor']['as_number'] = int(m.group(1))
                elif in_remote_node:
                    nlri_dict['remote_node_descriptor']['as_number'] = int(m.group(1))
                continue

            # BGP Identifier: 0.0.0.0
            m = p12.match(line)
            if m and nlri_dict is not None:
                if in_local_node:
                    nlri_dict['local_node_descriptor']['bgp_identifier'] = m.group(1)
                elif in_remote_node:
                    nlri_dict['remote_node_descriptor']['bgp_identifier'] = m.group(1)
                continue

            # Area ID: 0.0.0.0
            m = p13.match(line)
            if m and nlri_dict is not None:
                if in_local_node:
                    nlri_dict['local_node_descriptor']['area_id'] = m.group(1)
                elif in_remote_node:
                    nlri_dict['remote_node_descriptor']['area_id'] = m.group(1)
                continue

            # Router ID IPv4: 1.1.1.1
            m = p14.match(line)
            if m and nlri_dict is not None:
                if in_local_node:
                    nlri_dict['local_node_descriptor']['router_id_ipv4'] = m.group(1)
                elif in_remote_node:
                    nlri_dict['remote_node_descriptor']['router_id_ipv4'] = m.group(1)
                continue

            # Local Interface Address IPv4: 99.1.2.1
            m = p15.match(line)
            if m and nlri_dict is not None and in_link_desc:
                nlri_dict['link_descriptor']['local_interface_address_ipv4'] = m.group(1)
                continue

            # Neighbor Interface Address IPv4: 99.1.2.2
            m = p16.match(line)
            if m and nlri_dict is not None and in_link_desc:
                nlri_dict['link_descriptor']['neighbor_interface_address_ipv4'] = m.group(1)
                continue

            # Attributes: Link ID: Local:109 Remote:16, metric: 1, Opaque-link-attr:
            m = p17.match(line)
            if m and nlri_dict is not None:
                nlri_dict['attributes'] = {
                    'local_link_id': int(m.group(1)),
                    'remote_link_id': int(m.group(2)),
                    'metric': int(m.group(3)),
                    'opaque_link_attr': ''
                }
                continue

            # 80.02.00.18.00.00.00.09.76.31.2e.30.30.2d.4f.4c.54.2d
            # .43.5f.30.5f.30.5f.30.20.20.20
            m = p18.match(line)
            if m and nlri_dict is not None:
                if 'attributes' in nlri_dict:
                    nlri_dict['attributes']['opaque_link_attr'] += m.group(1).replace('.', '')
                continue

        return ret_dict
