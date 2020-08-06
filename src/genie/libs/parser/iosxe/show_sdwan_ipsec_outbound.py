from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any,Optional
import re

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
                        "destination_port": str,
                        "authentication": str,
                        "remote_tloc_color": str,
                        "key_hash": str,
                        "spi": str,
                        "source_port": str,
                        "remote_tloc": str,
                        "encryption_algorithm": str,
                        "tunnel_mtu": str,
                        "tc_spi": str,
                    },
                },
            },
        },
    }


# =================================================
# Parser for 'show sdwan ipsec outbound-connections'
# =================================================

class ShowSdwanIpsecOutboundConnections(ShowSdwanIpsecOutboundConnectionsSchema):

    """ Parser for "show sdwan ipsec outbound-connections" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec outbound-connections"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        #77.27.8.2                               12346   77.27.2.2                               12366   271     1438        78.78.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8            
        p1=re.compile(r"^(?P<source_ip>[\S]+) +(?P<source_port>[\d]+) +"
                      r"(?P<destination_ip>[\S]+) +(?P<destination_port>[\d]+) +"
                      r"(?P<spi>[\d]+) +(?P<tunnel_mtu>[\d]+) +"
                      r"(?P<remote_tloc>[\S]+) +(?P<remote_tloc_color>[\S]+) +"
                      r"(?P<authentication>[\S]+) +(?P<key_hash>[\S]+) +"
                      r"(?P<encryption_algorithm>[\S]+) +(?P<tc_spi>[\d]+)$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                source_ip = groups['source_ip']
                destination_ip = groups['destination_ip']
                parsed_dict.setdefault("source_ip", {}).setdefault(source_ip, {})
                destination_dict = parsed_dict["source_ip"][source_ip].setdefault("destination_ip", {})
                groups.pop('source_ip')
                groups.pop('destination_ip')
                ipsec_dict = destination_dict.setdefault(destination_ip, groups)
                continue

        return parsed_dict