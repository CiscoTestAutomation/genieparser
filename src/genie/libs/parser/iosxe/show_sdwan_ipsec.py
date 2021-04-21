from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re
from collections import OrderedDict

# =================================================
# Schema for 'show sdwan ipsec inbound-connections'
# =================================================


class ShowSdwanIpsecInboundConnectionsSchema(MetaParser):
    """ Schema for "show sdwan ipsec inbound-connections" command """

    schema = {
        "source_ip": {
            Any(): {
                'destination_ip': {
                    Any(): {
                        "local_tloc_color": str,
                        "destination_port": int,
                        "local_tloc": str,
                        "remote_tloc_color": str,
                        "remote_tloc": str,
                        "source_port": int,
                        "encryption_algorithm": str,
                        "tc_spi": int,
                    },
                },
            },
        },
    }


# =================================================
# Schema for 'show sdwan ipsec outbound-connections'
# =================================================


class ShowSdwanIpsecOutboundConnectionsSchema(MetaParser):
    """ Schema for "show sdwan ipsec outbound-connections" command """

    schema = {
        "source_ip": {
            Any(): {
                'destination_ip': {
                    Any(): {
                        "destination_port": int,
                        "authentication": str,
                        "remote_tloc_color": str,
                        "key_hash": str,
                        "spi": int,
                        "source_port": int,
                        "remote_tloc": str,
                        "encryption_algorithm": str,
                        "tunnel_mtu": int,
                        "tc_spi": int,
                    },
                },
            },
        },
    }


# =================================================
# Schema for 'show sdwan ipsec local-sa <WORD>'
# =================================================
class ShowSdwanIpsecLocalsaSchema(MetaParser):
    """ Schema for "show sdwan ipsec local-sa <WORD>" command """

    schema = {
        "local_sa": {
            'inbound': {
                'spi': int,
                'source_ipv4': str,
                'source_port': int,
                'source_ipv6': str,
                'tloc_color': str,
                'key_hash': str,
            },
            'outbound': {
                'spi': int,
                'source_ipv4': str,
                'source_port': int,
                'source_ipv6': str,
                'tloc_color': str,
                'key_hash': str,
            },
        },
    }


# =================================================
# Parser for 'show sdwan ipsec inbound-connections'
# =================================================


class ShowSdwanIpsecInboundConnections(ShowSdwanIpsecInboundConnectionsSchema):
    """ Parser for "show sdwan ipsec inbound-connections" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec inbound-connections"

    def cli(self, output=''):
        if not output:
            output = self.device.execute(self.cli_command)
        
        parsed_dict = {}

        #10.106.2.2 12346   10.106.8.2 12406   10.111.0.6 biz-internet     10.111.0.9 biz-internet     AES-GCM-256           8
        p1 = re.compile(
            r"^(?P<source_ip>[\S]+) +(?P<source_port>[\d]+) +"
            r"(?P<destination_ip>[\S]+) +(?P<destination_port>[\d]+) +"
            r"(?P<remote_tloc>[\S]+) +(?P<remote_tloc_color>[\S]+) +"
            r"(?P<local_tloc>[\S]+) +(?P<local_tloc_color>[\S]+) +"
            r"(?P<encryption_algorithm>[\S]+) +(?P<tc_spi>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parameters_dict = {}
                source_ip = groups['source_ip']
                destination_ip = groups['destination_ip']
                parsed_dict.setdefault("source_ip",
                                       {}).setdefault(source_ip, {})
                destination_dict = parsed_dict["source_ip"][
                    source_ip].setdefault("destination_ip", {})
                parameters_dict.update({
                    'local_tloc_color':
                    groups['local_tloc_color'],
                    'destination_port':
                    int(groups['destination_port']),
                    'local_tloc':
                    groups['local_tloc'],
                    'remote_tloc_color':
                    groups['remote_tloc_color'],
                    'remote_tloc':
                    groups['remote_tloc'],
                    'source_port':
                    int(groups['source_port']),
                    'encryption_algorithm':
                    groups['encryption_algorithm'],
                    'tc_spi':
                    int(groups['tc_spi']),
                })
                ipsec_dict = destination_dict.setdefault(
                    destination_ip, parameters_dict)
                continue

        return parsed_dict


# =================================================
# Parser for 'show sdwan ipsec outbound-connections'
# =================================================


class ShowSdwanIpsecOutboundConnections(ShowSdwanIpsecOutboundConnectionsSchema
                                        ):
    """ Parser for "show sdwan ipsec outbound-connections" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec outbound-connections"

    def cli(self, output=''):
        if not output:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        #10.106.8.2                               12346   10.106.2.2                               12366   271     1438        10.111.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8
        p1 = re.compile(
            r"^(?P<source_ip>[\S]+) +(?P<source_port>[\d]+) +"
            r"(?P<destination_ip>[\S]+) +(?P<destination_port>[\d]+) +"
            r"(?P<spi>[\d]+) +(?P<tunnel_mtu>[\d]+) +"
            r"(?P<remote_tloc>[\S]+) +(?P<remote_tloc_color>[\S]+) +"
            r"(?P<authentication>[\S]+) +(?P<key_hash>[\S]+) +"
            r"(?P<encryption_algorithm>[\S]+) +(?P<tc_spi>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parameters_dict = {}
                source_ip = groups['source_ip']
                destination_ip = groups['destination_ip']
                parsed_dict.setdefault("source_ip",
                                       {}).setdefault(source_ip, {})
                destination_dict = parsed_dict["source_ip"][
                    source_ip].setdefault("destination_ip", {})
                parameters_dict.update({
                    'destination_port':
                    int(groups['destination_port']),
                    'authentication':
                    groups['authentication'],
                    'remote_tloc_color':
                    groups['remote_tloc_color'],
                    'key_hash':
                    groups['key_hash'],
                    'spi':
                    int(groups['spi']),
                    'source_port':
                    int(groups['source_port']),
                    'remote_tloc':
                    groups['remote_tloc'],
                    'encryption_algorithm':
                    groups['encryption_algorithm'],
                    'tunnel_mtu':
                    int(groups['tunnel_mtu']),
                    'tc_spi':
                    int(groups['tc_spi']),
                })
                ipsec_dict = destination_dict.setdefault(
                    destination_ip, parameters_dict)
                continue

        return parsed_dict


# =================================================
# Parser for 'show sdwan ipsec local-sa <WORD>'
# =================================================


class ShowSdwanIpsecLocalsa(ShowSdwanIpsecLocalsaSchema):
    """ Parser for "show sdwan ipsec local-sa <WORD>" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec local-sa {tloc_address}"

    def cli(self, tloc_address='', output=''):
        if not output:
            output = self.device.execute(self.cli_command.format(tloc_address=tloc_address))

        parsed_dict = {}

        #10.111.0.9        biz-internet     259     10.106.8.2        ::                                      12346   *****8d95
        #10.111.0.9        biz-internet     260     10.106.8.2        ::                                      12346   *****4447
        p1 = re.compile(
            r"^(?P<tloc_address>[\S]+) +(?P<tloc_color>[\S]+) +"
            r"(?P<spi>[\d]+) +(?P<source_ipv4>[\S]+) +"
            r"(?P<source_ipv6>[\S]+) +(?P<source_port>[\d]+) +(?P<key_hash>[\S]+)$"
        )

        count = 0
        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                if count != 2:
                    spi_dict = parsed_dict.setdefault(
                        "local_sa",
                        OrderedDict()).setdefault("inbound", OrderedDict())
                else:
                    spi_dict = parsed_dict.setdefault(
                        "local_sa",
                        OrderedDict()).setdefault("outbound", OrderedDict())
                keys = [
                    "spi", "source_ipv4", "source_port", "source_ipv6",
                    "tloc_color", "key_hash"
                ]
                for k in keys:
                    spi_dict[k] = int(groups[k]) if k in [
                        "spi", "source_port"
                    ] else groups[k]
        return parsed_dict