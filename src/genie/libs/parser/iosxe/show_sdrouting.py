# Metaparser
import re

from genie import parsergen
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional



# ==============================================================
# Schema for 'show sd-routing control local-properties summary'
# ==============================================================

class ShowSdroutingControlLocalPropertiesSummarySchema(MetaParser):

    """ Schema for "show sd-routing control local-properties summary" command """

    schema = {
        "personality": str,
        Optional("sp_organization_name"): str,
        "organization_name": str,
        "root_ca_chain_status": str,
        "root_ca_crl_status": str,
        "certificate_status": str,
        "certificate_validity": str,
        "certificate_not_valid_before": str,
        "certificate_not_valid_after": str,
        Optional("enterprise_cert_status"): str,
        Optional("enterprise_cert_validity"): str,
        Optional("enterprise_cert_not_valid_before"): str,
        Optional("enterprise_cert_not_valid_after"): str,
        "dns_name": str,
        "site_id": int,
        "protocol": str,
        "tls_port": int,
        "system_ip": str,
        "chassis_num_unique_id": str,
        "serial_num": str,
        "subject_serial_num": str,
        Optional("enterprise_serial_num"): str,
        Optional("token"): str,
        "keygen_interval": str,
        "retry_interval": str,
        "no_activity_exp_interval": str,
        "dns_cache_ttl": str,
        "port_hopped": str,
        "time_since_last_port_hop": str,
        Optional("embargo_check"): str,
        "number_vbond_peers": int,
        "number_active_wan_interfaces": int,
    }


# =============================================================
# Parser for 'show sd-routing control local-properties summary'
# =============================================================

class ShowSdroutingControlLocalPropertiesSummary(ShowSdroutingControlLocalPropertiesSummarySchema):

    """ Parser for "show sd-routing control local-properties summary" """

    cli_command = "show sd-routing control local-properties summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # personality                       vedge
        p1 = re.compile(
            r"^personality\s+(?P<personality>\S+)$"
        )

        # sp_organization_name              SD_WAN_LAB _ 255639
        p2 = re.compile(
            r"^sp-organization-name\s+(?P<sp_organization_name>.*)$"
        )

        # organization_name                 SD_WAN_LAB _ 255639
        p3 = re.compile(
            r"^organization-name\s+(?P<organization_name>.*)$"
        )

        # root_ca_chain_status              Installed
        p4 = re.compile(
            r"^root-ca-chain-status\s+(?P<root_ca_chain_status>.*)$"
        )

        # root_ca_crl_status            Not-Installed
        p5 = re.compile(
            r"^root-ca-crl-status\s+(?P<root_ca_crl_status>.*)$"
        )

        # certificate_status                Installed
        p6 = re.compile(
            r"^certificate-status\s+(?P<certificate_status>.*)$"
        )

        # certificate_validity              Valid
        p7 = re.compile(
            r"^certificate-validity\s+(?P<certificate_validity>.*)$"
        )

        # certificate_not_valid_before      Jan 10 06:58:04 2020 GMT
        p8 = re.compile(
            r"^certificate-not-valid-before\s+(?P<certificate_not_valid_before>.*)$"
        )

        # certificate_not_valid_after       Aug 09 20:58:26 2099 GMT
        p9 = re.compile(
            r"^certificate-not-valid-after\s+(?P<certificate_not_valid_after>.*)$"
        )

        # enterprise_cert_status            Not_Applicable
        p10 = re.compile(
            r"^enterprise-cert-status\s+(?P<enterprise_cert_status>.*)$"
        )

        # enterprise_cert_validity          Not Applicable
        p11 = re.compile(
            r"^enterprise-cert-validity\s+(?P<enterprise_cert_validity>.*)$"
        )

        # enterprise_cert_not_valid_before  Not Applicable
        p12 = re.compile(
            r"^enterprise-cert-not-valid-before\s+(?P<enterprise_cert_not_valid_before>.*)$"
        )

        # enterprise_cert_not_valid_after   Not Applicable
        p13 = re.compile(
            r"^enterprise-cert-not-valid-after\s+(?P<enterprise_cert_not_valid_after>.*)$"
        )

        # dns_name                          vbond_950810.viptela.net
        p14 = re.compile(
            r"^dns-name\s+(?P<dns_name>.*)$"
        )

        # site_id                           1101
        p15 = re.compile(
            r"^site-id\s+(?P<site_id>\d+)$"
        )

        # protocol                          dtls
        p16 = re.compile(
            r"^protocol\s+(?P<protocol>.*)$"
        )

        # tls_port                          0
        p17 = re.compile(
            r"^tls-port\s+(?P<tls_port>\d+)$"
        )

        # system_ip                         10.150.74.1
        p18 = re.compile(
            r"^system-ip\s+(?P<system_ip>.*)$"
        )
        
        # chassis_num/unique_id             ISR1100_6G_FGL2402LJC8
        p19 = re.compile(
            r"^chassis-num\/unique-id\s+(?P<chassis_num_unique_id>.*)$"
        )
        
        # serial_num                        01F60455
        p20 = re.compile(
            r"^serial-num\s+(?P<serial_num>.*)$"
        )

        # subject-serial-num                        FDO2321A09H
        p21 = re.compile(
            r"^subject-serial-num\s+(?P<subject_serial_num>.*)$"
        )

        # enterprise_serial_num             No certificate installed
        p22 = re.compile(
            r"^enterprise-serial-num\s+(?P<enterprise_serial_num>.*)$"
        )
        
        # token                             -NA-
        p23 = re.compile(
            r"^token\s+(?P<token>.*)$"
        )
        
        # keygen_interval                   1:00:00:00
        p24 = re.compile(
            r"^keygen-interval\s+(?P<keygen_interval>.*)$"
        )
        
        # retry_interval                    0:00:00:15
        p25 = re.compile(
            r"^retry-interval\s+(?P<retry_interval>.*)$"
        )
        
        # no_activity_exp_interval          0:00:00:20
        p26 = re.compile(
            r"^no-activity-exp-interval\s+(?P<no_activity_exp_interval>.*)$"
        )
        
        # dns_cache_ttl                     0:00:02:00
        p27 = re.compile(
            r"^dns-cache-ttl\s+(?P<dns_cache_ttl>.*)$"
        )
        
        # port_hopped                       TRUE
        p28 = re.compile(
            r"^port-hopped\s+(?P<port_hopped>.*)$"
        )
        
        # time_since_last_port_hop          8:00:54:07
        p29 = re.compile(
            r"^time-since-last-port-hop\s+(?P<time_since_last_port_hop>.*)$"
        )        
        
        # embargo_check                     success
        p30 = re.compile(
            r"^embargo-check\s+(?P<embargo_check>.*)$"
        )
        
        # number_vbond_peers                0
        p31 = re.compile(
            r"^number-vbond-peers\s+(?P<number_vbond_peers>\d+)$"
        )
        
        # number_active_wan_interfaces      2
        p32 = re.compile(
            r"^number-active-wan-interfaces\s+(?P<number_active_wan_interfaces>\d+)$"
        )


        for line in out.splitlines():
            line = line.strip()

            # personality                       vedge
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                parsed_dict.update({
                    'personality': group['personality'],
                })
                continue

            # sp_organization_name              SD_WAN_LAB _ 255639
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                parsed_dict.update({
                    'sp_organization_name': group['sp_organization_name'],
                })
                continue

            # organization_name                 SD_WAN_LAB _ 255639
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                parsed_dict.update({
                    'organization_name': group['organization_name'],
                })
                continue

            # root_ca_chain_status              Installed
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                parsed_dict.update({
                    'root_ca_chain_status': group['root_ca_chain_status'],
                })
                continue

            # root_ca_crl_status            Not-Installed
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                parsed_dict.update({
                    'root_ca_crl_status': group['root_ca_crl_status'],
                })
                continue

            # certificate_status                Installed
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                parsed_dict.update({
                    'certificate_status': group['certificate_status'],
                })
                continue

            # certificate_validity              Valid
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                parsed_dict.update({
                    'certificate_validity': group['certificate_validity'],
                })
                continue

            # certificate_not_valid_before      Jan 10 06:58:04 2020 GMT
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                parsed_dict.update({
                    'certificate_not_valid_before': group['certificate_not_valid_before'],
                })
                continue

            # certificate_not_valid_after       Aug 09 20:58:26 2099 GMT
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                parsed_dict.update({
                    'certificate_not_valid_after': group['certificate_not_valid_after'],
                })
                continue

            # enterprise_cert_status            Not_Applicable
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                parsed_dict.update({
                    'enterprise_cert_status': group['enterprise_cert_status'],
                })
                continue

            # enterprise_cert_validity          Not Applicable
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                parsed_dict.update({
                    'enterprise_cert_validity': group['enterprise_cert_validity'],
                })
                continue

            # enterprise_cert_not_valid_before  Not Applicable
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                parsed_dict.update({
                    'enterprise_cert_not_valid_before': group['enterprise_cert_not_valid_before'],
                })
                continue

            # enterprise_cert_not_valid_after   Not Applicable 
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                parsed_dict.update({
                    'enterprise_cert_not_valid_after': group['enterprise_cert_not_valid_after'],
                })
                continue

            # dns_name                          vbond_950810.viptela.net
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                parsed_dict.update({
                    'dns_name': group['dns_name'],
                })
                continue

            # site_id                           1101
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                parsed_dict.update({
                    'site_id': int(group['site_id']),
                })
                continue

            # protocol                          dtls
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                parsed_dict.update({
                    'protocol': group['protocol'],
                })
                continue

            # tls_port                          0
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                parsed_dict.update({
                    'tls_port': int(group['tls_port']),
                })
                continue

            # system_ip                         10.150.74.1
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                parsed_dict.update({
                    'system_ip': group['system_ip'],
                })
                continue

            # chassis_num/unique_id             ISR1100_6G_FGL2402LJC8
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                parsed_dict.update({
                    'chassis_num_unique_id': group['chassis_num_unique_id'],
                })
                continue

            # serial_num                        01F60455
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                parsed_dict.update({
                    'serial_num': group['serial_num'],
                })
                continue

            # subject-serial-num                        FDO2321A09H
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                parsed_dict.update({
                    'subject_serial_num': group['subject_serial_num'],
                })
                continue

            # enterprise_serial_num             No certificate installed
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                parsed_dict.update({
                    'enterprise_serial_num': group['enterprise_serial_num'],
                })
                continue

            # token                             -NA-
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                parsed_dict.update({
                    'token': group['token'],
                })
                continue

            # keygen_interval                   1:00:00:00
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                parsed_dict.update({
                    'keygen_interval': group['keygen_interval'],
                })
                continue

            # retry_interval                    0:00:00:15
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                parsed_dict.update({
                    'retry_interval': group['retry_interval'],
                })
                continue

            # no_activity_exp_interval          0:00:00:20
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                parsed_dict.update({
                    'no_activity_exp_interval': group['no_activity_exp_interval'],
                })
                continue

            # dns_cache_ttl                     0:00:02:00
            m27 = p27.match(line)
            if m27:
                group = m27.groupdict()
                parsed_dict.update({
                    'dns_cache_ttl': group['dns_cache_ttl'],
                })
                continue

            # port_hopped                       TRUE
            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                parsed_dict.update({
                    'port_hopped': group['port_hopped'],
                })
                continue

            # time_since_last_port_hop          8:00:54:07
            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                parsed_dict.update({
                    'time_since_last_port_hop': group['time_since_last_port_hop'],
                })
                continue

            # embargo_check                     success
            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                parsed_dict.update({
                    'embargo_check': group['embargo_check'],
                })
                continue

            # number_vbond_peers                0
            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                parsed_dict.update({
                    'number_vbond_peers': int(group['number_vbond_peers']),
                })
                continue

            # number_active_wan_interfaces      2
            m32 = p32.match(line)
            if m32:
                group = m32.groupdict()
                parsed_dict.update({
                    'number_active_wan_interfaces': int(group['number_active_wan_interfaces']),
                })
                continue

        return parsed_dict


# ================================================================
# Schema for 'show sd-routing control local-properties wan detail'
# ================================================================
    
class ShowSdroutingControlLocalPropertiesWanDetailSchema(MetaParser):

    """ Schema for "show sd-routing control local-properties wan detail" command """

    schema = {    
        "wan_interfaces": {
            Any(): {
                "public_ipv4": str,
                "public_port": int,
                "private_ipv4": str,
                "private_ipv6": str,
                "private_port": int,
                "state": str,
                "vmanage": int,
                "control": str,
                "stun": str,
                "low_bandwidth_link": str,
                "last_connection": str,
                "spi_time_remaining": str,
                "nat_type": str,
                "vm_con": int,
                "region_id": int,
            },
        },
    }


# ================================================================
# Parser for 'show sd-routing control local-properties wan detail'
# ================================================================
    
class ShowSdroutingControlLocalPropertiesWanDetail(ShowSdroutingControlLocalPropertiesWanDetailSchema):

    """ Parser for "show sd-routing control local-properties wan detail" """

    cli_command = "show sd-routing control local-properties wan detail"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Interface TenGigabitEthernet0/1/0
        p1 = re.compile(
            r"^Interface\s+(?P<interface>\S+)$"
        )

        # Public  IPv4       : 75.75.1.2
        p2 = re.compile(
            r"^Public\s+IPv4\s+:\s+(?P<public_ipv4>.*)$"
        )

        # Public  Port       : 65086
        p3 = re.compile(
            r"^Public\s+Port\s+:\s+(?P<public_port>\d+)$"
        )

        # Private IPv4       : 75.75.1.2
        p4 = re.compile(
            r"^Private\s+IPv4\s+:\s+(?P<private_ipv4>.*)$"
        )

        # Private IPv6       : ::
        p5 = re.compile(
            r"^Private\s+IPv6\s+:\s+(?P<private_ipv6>.*)$"
        )

        # Private Port       : 65086
        p6 = re.compile(
            r"^Private\s+Port\s+:\s+(?P<private_port>\d+)$"
        )

        # State              : up
        p7 = re.compile(
            r"^State\s+:\s+(?P<state>.*)$"
        )

        # Number of vManages : 1
        p8 = re.compile(
            r"^Number\s+of\s+vManages\s+:\s+(?P<vmanage>.*)$"
        )

        # Control            : yes
        p9 = re.compile(
            r"^Control\s+:\s+(?P<control>.*)$"
        )

        # STUN               : no
        p10 = re.compile(
            r"^STUN\s+:\s+(?P<stun>.*)$"
        )

        # Low Bandwidth Link : no
        p11 = re.compile(
            r"^Low\s+Bandwidth\s+Link\s+:\s+(?P<low_bandwidth_link>.*)$"
        )

        # Last Connection    : 0:16:05:41
        p12 = re.compile(
            r"^Last\s+Connection\s+:\s+(?P<last_connection>.*)$"
        )

        # SPI Remaining Time : 0:00:00:00
        p13 = re.compile(
            r"^SPI\s+Remaining\s+Time\s+:\s+(?P<spi_time_remaining>.*)$"
        )

        # NAT Type           : N
        p14 = re.compile(
            r"^NAT\s+Type\s+:\s+(?P<nat_type>.*)$"
        )

        # vManage Connection : 5
        p15 = re.compile(
            r"^vManage\s+Connection\s+:\s+(?P<vm_con>\d+)$"
        )

        # Region IDs         : 0
        p16 = re.compile(
            r"^Region\s+IDs\s+:\s+(?P<region_id>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                interface = group['interface']

                parsed_dict.setdefault("wan_interfaces", {}).\
                            setdefault(interface, {})
                connection_dict = parsed_dict["wan_interfaces"][interface]
                continue


            # Public  IPv4       : 75.75.1.2
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                connection_dict.update({
                    'public_ipv4': group['public_ipv4'],
                })
                continue

            # Public  Port       : 65086
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                connection_dict.update({
                    'public_port': int(group['public_port']),
                })
                continue

            # Private IPv4       : 75.75.1.2
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                connection_dict.update({
                    'private_ipv4': group['private_ipv4'],
                })
                continue

            # Private IPv6       : ::
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                connection_dict.update({
                    'private_ipv6': group['private_ipv6'],
                })
                continue

            # Private Port       : 65086
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                connection_dict.update({
                    'private_port': int(group['private_port']),
                })
                continue

            # State              : up
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                connection_dict.update({
                    'state': group['state'],
                })
                continue


            # Number of vManages : 1
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                connection_dict.update({
                    'vmanage': int(group['vmanage']),
                })
                continue

            # Control            : yes
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                connection_dict.update({
                    'control': group['control'],
                })
                continue

            # STUN               : no
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                connection_dict.update({
                    'stun': group['stun'],
                })
                continue

            # Low Bandwidth Link : no
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                connection_dict.update({
                    'low_bandwidth_link': group['low_bandwidth_link'],
                })
                continue

            # Last Connection    : 0:16:05:41
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                connection_dict.update({
                    'last_connection': group['last_connection'],
                })
                continue

            # SPI Remaining Time : 0:00:00:00
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                connection_dict.update({
                    'spi_time_remaining': group['spi_time_remaining'],
                })
                continue
                        

            # NAT Type           : N
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                connection_dict.update({
                    'nat_type': group['nat_type'],
                })
                continue

            # vManage Connection : 5
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                connection_dict.update({
                    'vm_con': int(group['vm_con']),
                })
                continue

            # Region IDs         : 0
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                connection_dict.update({
                    'region_id': int(group['region_id']),
                })
                continue

        return parsed_dict


# ===================================================
# Schema for 'show control local-properties wan ipv4'
# ===================================================
    
class ShowSdroutingControlLocalPropertiesWanIpv4Schema(MetaParser):

    """ Schema for "show sd-routing control local-properties wan ipv4" command """

    schema = {    
        "wan_interfaces": {
            Any(): {
                "public_ipv4": str,
                "public_port": int,
                "private_ipv4": str,
                "private_port": int,
                "state": str,
            },
        },
    }


# ==============================================================
# Parser for 'show sd-routing control local-properties wan ipv4'
# ==============================================================

class ShowSdroutingControlLocalPropertiesWanIpv4(ShowSdroutingControlLocalPropertiesWanIpv4Schema):

    """ Parser for "show sd-routing control local-properties wan ipv4" """

    cli_command = "show sd-routing control local-properties wan ipv4"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # GigabitEthernet0/0/2           145.35.45.12     65052   145.35.45.12     65052    up
        p = re.compile(
            r"^(?P<interface>\S+)\s+(?P<public_ipv4>(?:\d{1,3}\.){3}\d{1,3})\s+" \
            r"(?P<public_port>\d+)\s+(?P<private_ipv4>(?:\d{1,3}\.){3}\d{1,3})\s+" \
            r"(?P<private_port>\d+)\s+(?P<state>\S+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/2           145.35.45.12     65052   145.35.45.12     65052    up
            m = p.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']

                parsed_dict.setdefault("wan_interfaces", {}).\
                            setdefault(interface, {})
                connection_dict = parsed_dict["wan_interfaces"][interface]
                connection_dict.update({'private_ipv4': group['private_ipv4']})
                connection_dict.update({'private_port': int(group['private_port'])})
                connection_dict.update({'public_ipv4': group['public_ipv4']})
                connection_dict.update({'public_port': int(group['public_port'])})
                connection_dict.update({'state': group['state']})
                continue

        return parsed_dict

# ===================================================
# Schema for 'show control local-properties wan ipv6'
# ===================================================
    
class ShowSdroutingControlLocalPropertiesWanIpv6Schema(MetaParser):

    """ Schema for "show sd-routing control local-properties wan ipv6" command """

    schema = {    
        "wan_interfaces": {
            Any(): {
                "public_port": int,
                "private_ipv6": str,
                "private_port": int,
                "state": str,
            },
        },
    }


# ==============================================================
# Parser for 'show sd-routing control local-properties wan ipv6'
# ==============================================================

class ShowSdroutingControlLocalPropertiesWanIpv6(ShowSdroutingControlLocalPropertiesWanIpv6Schema):

    """ Parser for "show sd-routing control local-properties wan ipv6" """

    cli_command = "show sd-routing control local-properties wan ipv6"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # TenGigabitEthernet0/1/0        65086   ::                                       65086    up
        p = re.compile(
            r"^(?P<interface>\S+)\s+(?P<public_port>\d+)\s+(?P<private_ipv6>\S+)\s+" \
            r"(?P<private_port>\d+)\s+(?P<state>\S+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # TenGigabitEthernet0/1/0        65086   ::                                       65086    up
            m = p.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                parsed_dict.setdefault("wan_interfaces", {}).\
                            setdefault(interface, {})
                connection_dict = parsed_dict["wan_interfaces"][interface]
                connection_dict.update({'public_port': int(group['public_port'])})
                connection_dict.update({'private_ipv6': group['private_ipv6']})
                connection_dict.update({'private_port': int(group['private_port'])})
                connection_dict.update({'state': group['state']})
                continue

        return parsed_dict
 
    
# ===================================================
# Schema for 'show control local-properties vbond'
# ===================================================
    
class ShowSdroutingControlLocalPropertiesVbondSchema(MetaParser):

    """ Schema for "show sd-routing control local-properties vbond" command """

    schema = {
        "vbond_index": {
            Any(): {
                "ip": str,
                "port": int,
            }
        }
    }


# ==============================================================
# Parser for 'show sd-routing control local-properties vbond'
# ==============================================================

class ShowSdroutingControlLocalPropertiesVbond(ShowSdroutingControlLocalPropertiesVbondSchema):

    """ Parser for "show sd-routing control local-properties vbond" """

    cli_command = "show sd-routing control local-properties vbond"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # 0        70.70.70.125                             12346
        p = re.compile(
            r"^(?P<index>\d+)\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s+(?P<port>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # 0        70.70.70.125                             12346
            m = p.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault("vbond_index", {}).\
                            setdefault(int(group['index']), {})
                connection_dict = parsed_dict["vbond_index"][int(group['index'])]
                connection_dict.update({'ip': group['ip']})
                connection_dict.update({'port': int(group['port'])})
                continue

        return parsed_dict

