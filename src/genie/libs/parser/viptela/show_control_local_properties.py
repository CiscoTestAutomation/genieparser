from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from pprint import pprint
import re

# ===============================================
# Schema for 'show control local-properties'
# ===============================================

class ShowControlLocalPropertiesSchema(MetaParser):

    """ Schema for "show control local-properties" command """

    schema = {
        "personality": str,
        "sp_organization_name": str,
        "organization_name": str,
        "root_ca_chain_status": str,
        "certificate_status": str,
        "certificate_validity": str,
        "certificate_not_valid_before": str,
        "certificate_not_valid_after": str,
        Optional("enterprise_cert_status"): str,
        Optional("enterprise_cert_validity"): str,
        Optional("enterprise_cert_not_valid_before"): str,
        Optional("enterprise_cert_not_valid_after"): str,
        "dns_name": str,
        "site_id": str,
        "domain_id": str,
        "protocol": str,
        "tls_port": str,
        "system_ip": str,
        "chassis_num_unique_id": str,
        "serial_num": str,
        Optional("enterprise_serial_num"): str,
        "token": str,
        "keygen_interval": str,
        "retry_interval": str,
        "no_activity_exp_interval": str,
        "dns_cache_ttl": str,
        "port_hopped": str,
        "time_since_last_port_hop": str,
        Optional("pairwise_keying"): str,
        "embargo_check": str,
        "number_vbond_peers": str,
        "number_active_wan_interfaces": str,
        "connection_summary": {
            Any(): {
                "public_ipv4": str,
                "public_port": str,
                "private_ipv4": str,
                "private_ipv6": str,
                "private_port": str,
                "vsmart": str,
                "vmanage": str,
                "color": str,
                "state": str,
                "max_cntrl": str,
                "restrict": str,
                "control": str,
                "stun": str,
                "lr": str,
                "lb": str,
                "last_connection": str,
                "spi_time_remaining": str,
                "nat_type": str,
                "vm_con_prf": str,
            },
        },
    }


# ===============================================
# Parser for 'show control local-properties'
# ===============================================

class ShowControlLocalProperties(ShowControlLocalPropertiesSchema):

    """ Parser for "show control local-properties" """

    cli_command = "show control local-properties"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # personality                       vedge
        p1 = re.compile(
            r"^personality\s+(?P<personality>\S+)"
        )

        # sp_organization_name              SD_WAN_LAB _ 255639
        p2 = re.compile(
            r"^sp-organization-name\s+(?P<sp_organization_name>.*)"
        )

        # organization_name                 SD_WAN_LAB _ 255639
        p3 = re.compile(
            r"^organization-name\s+(?P<organization_name>.*)"
        )

        # root_ca_chain_status              Installed
        p4 = re.compile(
            r"^root-ca-chain-status\s+(?P<root_ca_chain_status>.*)"
        )

        # certificate_status                Installed
        # certificate_validity              Valid
        # certificate_not_valid_before      Jan 10 06:58:04 2020 GMT
        # certificate_not_valid_after       Aug 09 20:58:26 2099 GMT
        p5_1 = re.compile(
            r"^certificate-status\s+(?P<certificate_status>.*)"
        )

        p5_2 = re.compile(
            r"^certificate-validity\s+(?P<certificate_validity>.*)"
        )

        p5_3 = re.compile(
            r"^certificate-not-valid-before\s+(?P<certificate_not_valid_before>.*)"
        )

        p5_4 = re.compile(
            r"^certificate-not-valid-after\s+(?P<certificate_not_valid_after>.*)"
        )

        # enterprise_cert_status            Not_Applicable
        # enterprise_cert_validity          Not Applicable
        # enterprise_cert_not_valid_before  Not Applicable
        # enterprise_cert_not_valid_after   Not Applicable
        p6_1 = re.compile(
            r"^enterprise-cert-status\s+(?P<enterprise_cert_status>.*)"
        )

        p6_2 = re.compile(
            r"^enterprise-cert-validity\s+(?P<enterprise_cert_validity>.*)"
        )

        p6_3 = re.compile(
            r"^enterprise-cert-not-valid-before\s+(?P<enterprise_cert_not_valid_before>.*)"
        )

        p6_4 = re.compile(
            r"^enterprise-cert-not-valid-after\s+(?P<enterprise_cert_not_valid_after>.*)"
        )

        # dns_name                          vbond_950810.viptela.net
        p7 = re.compile(
            r"^dns-name\s+(?P<dns_name>.*)"
        )

        # site_id                           1101
        p8 = re.compile(
            r"^site-id\s+(?P<site_id>.*)"
        )

        # domain_id                         1
        p9 = re.compile(
            r"^domain-id\s+(?P<domain_id>.*)"
        )

        # protocol                          dtls
        p10 = re.compile(
            r"^protocol\s+(?P<protocol>.*)"
        )

        # tls_port                          0
        p11 = re.compile(
            r"^tls-port\s+(?P<tls_port>.*)"
        )

        # system_ip                         10.150.74.1
        p12 = re.compile(
            r"^system-ip\s+(?P<system_ip>.*)"
        )
        
        # chassis_num/unique_id             ISR1100_6G_FGL2402LJC8
        p13 = re.compile(
            r"^chassis-num\/unique-id\s+(?P<chassis_num_unique_id>.*)"
        )
        
        # serial_num                        01F60455
        p14 = re.compile(
            r"^serial-num\s+(?P<serial_num>.*)"
        )
        
        # enterprise_serial_num             No certificate installed
        p15 = re.compile(
            r"^enterprise-serial-num\s+(?P<enterprise_serial_num>.*)"
        )
        
        # token                             -NA-
        p16 = re.compile(
            r"^token\s+(?P<token>.*)"
        )
        
        # keygen_interval                   1:00:00:00
        p17 = re.compile(
            r"^keygen-interval\s+(?P<keygen_interval>.*)"
        )
        
        # retry_interval                    0:00:00:15
        p18 = re.compile(
            r"^retry-interval\s+(?P<retry_interval>.*)"
        )
        
        # no_activity_exp_interval          0:00:00:20
        p19 = re.compile(
            r"^no-activity-exp-interval\s+(?P<no_activity_exp_interval>.*)"
        )
        
        # dns_cache_ttl                     0:00:02:00
        p20 = re.compile(
            r"^dns-cache-ttl\s+(?P<dns_cache_ttl>.*)"
        )
        
        # port_hopped                       TRUE
        p21 = re.compile(
            r"^port-hopped\s+(?P<port_hopped>.*)"
        )
        
        # time_since_last_port_hop          8:00:54:07
        p22 = re.compile(
            r"^time-since-last-port-hop\s+(?P<time_since_last_port_hop>.*)"
        )
        
        # pairwise_keying                   Disabled
        p23 = re.compile(
            r"^pairwise-keying\s+(?P<pairwise_keying>.*)"
        )
        
        # embargo_check                     success
        p24 = re.compile(
            r"^embargo-check\s+(?P<embargo_check>.*)"
        )
        
        # number_vbond_peers                0
        p25 = re.compile(
            r"^number-vbond-peers\s+(?P<number_vbond_peers>.*)"
        )
        
        # number_active_wan_interfaces      2
        p26 = re.compile(
            r"^number-active-wan-interfaces\s+(?P<number_active_wan_interfaces>.*)"
        )

        # Match table output
        p27 = re.compile(
            r"(?P<interface>\S+)\s+(?P<public_ipv4>(?:\d{1,3}\.){3}\d{1,3})\s+" \
            "(?P<public_port>\S+)\s+(?P<private_ipv4>(?:\d{1,3}\.){3}\d{1,3})\s+" \
            "(?P<private_ipv6>\S+)\s+(?P<private_port>\S+)\s+(?P<vsmart>\d+)\/" \
            "(?P<vmanage>\d+)\s+(?P<color>\S+)\s+(?P<state>\S+)\s+(?P<max_cntrl>\d+)\s+" \
            "(?P<restrict>\w+)\/(?P<control>\w+)\/(?P<stun>\w+)\s+(?P<lr>\w+)\/(?P<lb>\w+)\s+" \
            "(?P<last_connection>\S+)\s+(?P<spi_time_remaining>\S+)\s+(?P<nat_type>[EAN])\s+" \
            "(?P<vm_con_prf>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                parsed_dict['personality'] = m.groupdict()['personality']
                continue

            m = p2.match(line)
            if m:
                parsed_dict['sp_organization_name'] = m.groupdict()['sp_organization_name']
                continue

            m = p3.match(line)
            if m:
                parsed_dict['organization_name'] = m.groupdict()['organization_name']
                continue

            m = p4.match(line)
            if m:
                parsed_dict['root_ca_chain_status'] = m.groupdict()['root_ca_chain_status']
                continue
            
            m = p5_1.match(line)
            if m:
                parsed_dict['certificate_status'] = m.groupdict()['certificate_status']
                continue

            m = p5_2.match(line)
            if m:
                parsed_dict['certificate_validity'] = m.groupdict()['certificate_validity']
                continue

            m = p5_3.match(line)
            if m:
                parsed_dict['certificate_not_valid_before'] = m.groupdict()['certificate_not_valid_before']
                continue

            m = p5_4.match(line)
            if m:
                parsed_dict['certificate_not_valid_after'] = m.groupdict()['certificate_not_valid_after']
                continue

            m = p6_1.match(line)
            if m:
                parsed_dict['enterprise_cert_status'] = m.groupdict()['enterprise_cert_status']
                continue

            m = p6_2.match(line)
            if m:
                parsed_dict['enterprise_cert_validity'] = m.groupdict()['enterprise_cert_validity']
                continue

            m = p6_3.match(line)
            if m:
                parsed_dict['enterprise_cert_not_valid_before'] = m.groupdict()['enterprise_cert_not_valid_before']
                continue

            m = p6_4.match(line)
            if m:
                parsed_dict['enterprise_cert_not_valid_after'] = m.groupdict()['enterprise_cert_not_valid_after']
                continue

            m = p7.match(line)
            if m:
                parsed_dict['dns_name'] = m.groupdict()['dns_name']
                continue

            m = p8.match(line)
            if m:
                parsed_dict['site_id'] = m.groupdict()['site_id']
                continue

            m = p9.match(line)
            if m:
                parsed_dict['domain_id'] = m.groupdict()['domain_id']
                continue

            m = p10.match(line)
            if m:
                parsed_dict['protocol'] = m.groupdict()['protocol']
                continue

            m = p11.match(line)
            if m:
                parsed_dict['tls_port'] = m.groupdict()['tls_port']
                continue

            m = p12.match(line)
            if m:
                parsed_dict['system_ip'] = m.groupdict()['system_ip']
                continue

            m = p13.match(line)
            if m:
                parsed_dict['chassis_num_unique_id'] = m.groupdict()['chassis_num_unique_id']
                continue

            m = p14.match(line)
            if m:
                parsed_dict['serial_num'] = m.groupdict()['serial_num']
                continue

            m = p15.match(line)
            if m:
                parsed_dict['enterprise_serial_num'] = m.groupdict()['enterprise_serial_num']
                continue

            m = p16.match(line)
            if m:
                parsed_dict['token'] = m.groupdict()['token']
                continue

            m = p17.match(line)
            if m:
                parsed_dict['keygen_interval'] = m.groupdict()['keygen_interval']
                continue

            m = p18.match(line)
            if m:
                parsed_dict['retry_interval'] = m.groupdict()['retry_interval']
                continue

            m = p19.match(line)
            if m:
                parsed_dict['no_activity_exp_interval'] = m.groupdict()['no_activity_exp_interval']
                continue

            m = p20.match(line)
            if m:
                parsed_dict['dns_cache_ttl'] = m.groupdict()['dns_cache_ttl']
                continue

            m = p21.match(line)
            if m:
                parsed_dict['port_hopped'] = m.groupdict()['port_hopped']
                continue

            m = p22.match(line)
            if m:
                parsed_dict['time_since_last_port_hop'] = m.groupdict()['time_since_last_port_hop']
                continue

            m = p23.match(line)
            if m:
                parsed_dict['pairwise_keying'] = m.groupdict()['pairwise_keying']
                continue

            m = p24.match(line)
            if m:
                parsed_dict['embargo_check'] = m.groupdict()['embargo_check']
                continue

            m = p25.match(line)
            if m:
                parsed_dict['number_vbond_peers'] = m.groupdict()['number_vbond_peers']
                continue

            m = p26.match(line)
            if m:
                parsed_dict['number_active_wan_interfaces'] = m.groupdict()['number_active_wan_interfaces']
                continue

            m = p27.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                parsed_dict.setdefault("connection_summary", {}).setdefault(interface, {})
                connection_dict = parsed_dict["connection_summary"][interface]
                connection_dict["public_ipv4"] = group["public_ipv4"]
                connection_dict["public_port"] = group["public_port"]
                connection_dict["private_ipv4"] = group["private_ipv4"]
                connection_dict["private_ipv6"] = group["private_ipv6"]
                connection_dict["private_port"] = group["private_port"]
                connection_dict["vsmart"] = group["vsmart"]
                connection_dict["vmanage"] = group["vmanage"]
                connection_dict["color"] = group["color"]
                connection_dict["state"] = group["state"]
                connection_dict["max_cntrl"] = group["max_cntrl"]
                connection_dict["restrict"] = group["restrict"]
                connection_dict["control"] = group["control"]
                connection_dict["stun"] = group["stun"]
                connection_dict["lr"] = group["lr"]
                connection_dict["lb"] = group["lb"]
                connection_dict["last_connection"] = group["last_connection"]
                connection_dict["spi_time_remaining"] = group["spi_time_remaining"]
                connection_dict["nat_type"] = group["nat_type"]
                connection_dict["vm_con_prf"] = group["vm_con_prf"]

                continue

        return parsed_dict
