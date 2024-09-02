"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto gdoi ipsec sa
   * show crypto gdoi feature and sub commands
   * show crypto gdoi gm
   * show crypto gdoi ks coop version 
   * show crypto gdoi ks
   * show crypto gdoi rekey sa
   * show crypto gdoi rekey sa detail
   * show crypto gdoi ks detail
   * show crypto gdoi ks coop detail
   * show crypto gdoi ks identifier
   * show crypto gdoi ks identifier detail
   * show crypto gdoi ks coop identifier detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

# Genie Libs
from genie.libs.parser.utils.common import Common


# =================================================
#  Schema for 'show crypto gdoi ks coop version '
# =================================================
class ShowCryptoGdoiKsCoopVersionSchema(MetaParser):
    """Schema for show crypto gdoi ks coop version"""
    schema = {
        "coop_ver": str,
        "ks_pol_ver": str,
        "gm_ver": str,
        "sid_ver": str
    }   

# ==============================
# Parser for
#   'show crypto gdoi ks coop version'
# ==============================

class ShowCryptoGdoiKsCoopVersion(ShowCryptoGdoiKsCoopVersionSchema):
    """
    Parser for
        * 'show crypto gdoi ks coop version'
    """

    cli_command = ['show crypto gdoi ks coop version']

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable    
        coop_dict = {}

        # Cooperative key server infra Version : 2.0.0 
        p1 = re.compile(r'Cooperative key server infra Version\s+:\s+(?P<coop_ver>\S+)$')

        # Client : KS_POLICY_CLIENT        Version : 2.0.0 
        p2 = re.compile(r'Client\s+:\s+KS_POLICY_CLIENT\s+Version\s+:\s+(?P<ks_pol_ver>\S+)$')

        # Client : GROUP_MEMBER_CLIENT     Version : 2.0.1 
        p3 = re.compile(r'Client\s+:\s+GROUP_MEMBER_CLIENT\s+Version\s+:\s+(?P<gm_ver>\S+)$')

        # Client : SID_CLIENT              Version : 1.0.1 
        p4 = re.compile(r'Client\s+:\s+SID_CLIENT\s+Version\s+:\s+(?P<sid_ver>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Cooperative key server infra Version : 2.0.0 
            m = p1.match(line)
            if m:
                coop_dict['coop_ver'] = m.groupdict()['coop_ver']
                continue

            # Client : KS_POLICY_CLIENT        Version : 2.0.0 
            m = p2.match(line)
            if m:
                coop_dict['ks_pol_ver'] = m.groupdict()['ks_pol_ver']
                continue

            # Client : GROUP_MEMBER_CLIENT     Version : 2.0.1 
            m = p3.match(line)
            if m:
                coop_dict['gm_ver'] = m.groupdict()['gm_ver']
                continue

            # Client : SID_CLIENT              Version : 1.0.1 
            m = p4.match(line)
            if m:
                coop_dict['sid_ver'] = m.groupdict()['sid_ver']
                continue

        return coop_dict  


# =================================================
#  Schema for 'show crypto gdoi'
# =================================================
class ShowCryptoGdoiSchema(MetaParser):
    """Schema for show crypto gdoi"""
    schema =  {
                "group_name":{
                    Any():{
                        "group_information":{
                            "crypto_path":str,
                            "group_identity":str,
                            "group_member":{
                                Any():{
                                    "active_tek_num":int,
                                    "allowable_rekey_cipher":str,
                                    "attempted_registration_count":int,
                                    "dp_error_monitoring":str,
                                    Optional("fail_close_revert"):str,
                                    "fvrf":str,
                                    "ipsec_init_reg_executed":int,
                                    "ipsec_init_reg_postponed":int,
                                    "ivrf":str,
                                    "last_rekey_seq_num":int,
                                    "last_rekey_server":str,
                                    "local_addr":str,
                                    "local_addr_port":str,
                                    Optional("pfs_rekey_received"):int,
                                    "re_register_time_sec":int,
                                    "registration":str,
                                    "rekey_acks_sent":int,
                                    "remote_addr":str,
                                    "remote_addr_port":int,
                                    "sa_track":str,
                                    "server_ip":str,
                                    "succeeded_registration_count":int,
                                    "uncicast_rekey_received":int,
                                    "version":str,
                                    "vrf":str
                                    }
                                },
                            "group_member_information":{
                                "acl_download_from_ks":{
                                    Any():{
                                        "acl_list":list
                                        }
                                    },
                                "acl_received_from_ks":str,
                                "rekeys_cumulative":{
                                    "after_latest_register":int,
                                    "rekey_acks_sents":int,
                                    "total_received":int
                                    }
                                },
                            "group_server_list":str,
                            "group_type":str,
                            "ipsec_sa_direction":str,
                            "kek_policy":{
                                "encrypt_algorithm":str,
                                "key_size":int,
                                "lifetime":int,
                                "rekey_transport_type":str,
                                "sig_hash_algorithm":str,
                                "sig_key_length":int
                            },
                            "key_management_path":str,
                            "kgs_policy":{
                                "reg_gm":{
                                    "local_addr":str
                                    }
                                },
                            "p2p_policy":{
                                "reg_gm":{
                                    "local_addr":str
                                    }
                                },
                            "rekeys_received":int,
                            "tek_policy":{
                                "interfaces":{
                                    Any():{
                                        "ipsec_sa":{
                                            "spi":{
                                                Any():{
                                                    "alg_key_size_bytes":int,
                                                    "sig_key_size_bytes":int,
                                                    Optional("anti_replay_count"):int,
                                                    "encaps":str,
                                                    "sa_remaining_key_lifetime":int,
                                                    "tag_method":str,
                                                    "transform":str
                                                    },
                                                Any():{
                                                    "alg_key_size_bytes":int,
                                                    "sig_key_size_bytes":int,
                                                    Optional("anti_replay_count"):int,
                                                    "encaps":str,
                                                    "sa_remaining_key_lifetime":int,
                                                    "tag_method":str,
                                                    "transform":str
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi'
# =================================================
class ShowCryptoGdoi(ShowCryptoGdoiSchema):
    """Parser for show crypto gdoi"""

    cli_command = ['show crypto gdoi']


    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Group Name               : getvpn1
        p1 = re.compile(r"^Group Name +: +(?P<group_name>\w+)$")

        # Group Identity           : 1223
        p2 = re.compile(r"^Group Identity +: +(?P<group_identity>\w+)$")

        # Group Type               : GDOI (ISAKMP)
        # Group Type               : G-IKEv2 (IKEv2)
        p3 = re.compile(r"^Group Type +: +(?P<group_type>[\w\d\S\-\s]+)$")

        # Crypto Path              : ipv4
        p4 = re.compile(r"^Crypto Path +: +(?P<crypto_path>\w+)$")

        # Key Management Path      : ipv4
        p5 = re.compile(r"^Key Management Path +: +(?P<key_management_path>\w+)$")

        # Rekeys received          : 25
        p6 = re.compile(r"^Rekeys received +: +(?P<rekeys_received>\w+)$")

        # IPSec SA Direction       : Both
        p7 = re.compile(r"^IPSec SA Direction +: +(?P<ipsec_sa_direction>\w+)$")

        # Group Server list       : 1.1.1.1
        p8 = re.compile(r"^Group Server list +: +(?P<group_server_list>[\d\.]+)$")

        # Group Member Information For Group getvpn1:
        p9 = re.compile(r"^Group Member.* +(?P<group>\w+):$")

        # ACL Received From KS     : gdoi_group_getvpn1_temp_acl
        p10 = re.compile(r"^ACL Received.* +(?P<acl_received_from_ks>\w+)$")

        # Group member             : 3.3.1.1         vrf: None
        p11 = re.compile(r"^Group member.* +: +(?P<group_member>[\d\.]+) +vrf: +(?P<vrf>[\w]+)$")

        # Local addr/port       : 3.3.1.1/848
        p12 = re.compile(r"^Local addr\/port +: +(?P<local_addr>[\d\.]+)\/(?P<local_addr_port>[\d]+)$")

        # Remote addr/port      : 1.1.1.1/848
        p13 = re.compile(r"^Remote addr\/port +: +(?P<remote_addr>[\d\.]+)\/(?P<remote_addr_port>[\d]+)$")

        # fvrf/ivrf             : None/None
        p14 = re.compile(r"^fvrf\/ivrf +: +(?P<fvrf>\w+)\/(?P<ivrf>\w+)$")

        # Version               : 1.0.26
        p15 = re.compile(r"^Version +: +(?P<version>[\d\.]+)$")

        # Registration status   : Registered
        p16 = re.compile(r"^Registration.* +(?P<registration>\w+)$")

        # Registered with       : 1.1.1.1
        p17 = re.compile(r"^Registered.* +(?P<server_ip>[\d\.]+)$")

        # Re-registers in       : 449 sec
        p18 = re.compile(r"^Re.* +(?P<re_register_time_sec>[\d]+) +sec$")

        # Succeeded registration: 1
        p19 = re.compile(r"^Succeeded.* +(?P<succeeded_registration_count>\d+)$")

        # Attempted registration: 1
        p20 = re.compile(r"^Attempted.* +(?P<attempted_registration_count>\d+)$")

        # Last rekey from       : UNKNOWN
        # Last rekey from       : 1.1.1.1
        p21 = re.compile(r"^Last rekey from.* +(?P<last_rekey_server>[\w\d\.]+)$")

        # Last rekey seq num    : 0
        p22 = re.compile(r"^Last rekey seq.* +(?P<last_rekey_seq_num>\d+)$")

        # Rekey ACKs sent       : 25
        p23 = re.compile(r"^Rekey ACKs sent.* +(?P<rekey_acks_sent>\d+)$")

        # Rekey Rcvd(hh:mm:ss)  : 00:01:30
        p24 = re.compile(r"^Rekey Rcvd.* +(?P<rekey_received_time>[\d\:]+)$")

        # PFS Rekey received    : 0
        p25 = re.compile(r"^PFS.* +(?P<pfs_rekey_received>\d+)$")

        # DP Error Monitoring   : OFF
        p26 = re.compile(r"^DP.* +(?P<dp_error_monitoring>\w+)$")

        # IPSEC init reg executed    : 0
        p27 = re.compile(r"^IPSEC init reg executed.* +(?P<ipsec_init_reg_executed>\d+)$")

        # IPSEC init reg postponed   : 0
        p28 = re.compile(r"^IPSEC init reg postponed.* +(?P<ipsec_init_reg_postponed>\d+)$")

        # Active TEK Number     : 2
        p29 = re.compile(r"^Active.* +(?P<active_tek_num>\d+)$")

        # SA Track (OID/status) : disabled
        p30 = re.compile(r"^SA.* +(?P<sa_track>[disabled|enabled]+)$")

        # Fail-Close Revert : Disabled
        p31 = re.compile(r"^Fail.* +(?P<fail_close_revert>[Disabled|Enabled]+)$")

        # allowable rekey cipher: any
        p32 = re.compile(r"^allowable.* +(?P<allowable_rekey_cipher>\w+)$")

        # allowable rekey hash  : any
        p33 = re.compile(r"^allowable rekey hash.* +(?P<allowable_rekey_hash>\w+)$")

        # allowable transformtag: any ESP
        p34 = re.compile(r"^allowable transformtag: +(?P<allowable_transformtag>[\w\s]+)$")

        # Total received        : 25
        p35 = re.compile(r"^Total received.* +(?P<total_received>\d+)$")

        # After latest register : 25
        p36 = re.compile(r"^After latest register.* +(?P<after_latest_register>\d+)$")

        # Rekey Acks sents      : 25
        p37 = re.compile(r"^Rekey Acks sents.* +(?P<rekey_acks_sents>\d+)$")

        # ACL Downloaded From KS 1.1.1.1:
        p38 = re.compile(r"^ACL Downloaded From KS.* +(?P<ks_server>[\d\.]+):$")

        # access-list   deny ip host 11.23.33.33 host 24.54.55.55
        # access-list   deny ip host 41.23.32.37 host 44.58.59.55
        # access-list   deny esp any any
        # access-list   deny udp any any port = 3784
        # access-list   deny udp any any port = 3785
        # access-list   deny udp any port = 3785 any
        # access-list   deny tcp any any port = 179
        # access-list   deny tcp any port = 179 any
        # access-list   deny tcp any any port = 22
        # access-list   deny tcp any port = 22 any
        # access-list   deny ospf any any
        # access-list   deny pim any 224.0.0.0 0.0.0.255
        # access-list   deny udp any any port = 123
        # access-list   deny udp any any port = 514
        # access-list   deny udp any port = 500 any port = 500
        # access-list   deny udp any port = 848 any
        # access-list   deny udp any any port = 848
        # access-list   deny ip any 10.90.0.0 0.0.255.255
        # access-list   deny ip 10.90.0.0 0.0.255.255 any
        # access-list   permit ip 25.25.0.0 0.0.255.255 15.15.0.0 0.0.255.255
        # access-list   permit ip 15.15.0.0 0.0.255.255 25.25.0.0 0.0.255.255
        # access-list   permit ip 16.16.0.0 0.0.255.255 26.26.0.0 0.0.255.255
        p39 = re.compile(r"^access-list.*$")

        # Rekey Transport Type     : Unicast
        p40 = re.compile(r"^Rekey Transport Type.*: (?P<rekey_transport_type>\w+)$")

        # Lifetime (secs)          : 1109
        p41 = re.compile(r"^Lifetime.*: (?P<lifetime>\d+)$")

        # Encrypt Algorithm        : AES
        p42 = re.compile(r"^Encrypt Algorithm.*: (?P<encrypt_algorithm>\w+)$")

        # Key Size                 : 256
        p43 = re.compile(r"^Key Size.*: (?P<key_size>\d+)$")

        # Sig Hash Algorithm       : HMAC_AUTH_SHA
        p44 = re.compile(r"^Sig Hash Algorithm.*: (?P<sig_hash_algorithm>\w+)$")

        # Sig Key Length (bits)    : 4400
        p45 = re.compile(r"^Sig Key Length.*: (?P<sig_key_length>\w+)$")

        # GigabitEthernet0/0/1:
        p46 = re.compile(r"^(?P<interface>[\S]+):$")

        # spi: 0x5A69F51E(1516893470)
        p47 = re.compile(r"^spi.* +(?P<spi>[\w\S]+)$")

        # transform: esp-256-aes esp-sha256-hmac
        p48 = re.compile(r"^transform.*: +(?P<transform>[\w\S\s]+)$")

        # sa timing:remaining key lifetime (sec): (510)
        p49 = re.compile(r"^sa timing.*\(+(?P<sa_remaining_key_lifetime>\d+)+\)$")

        # Anti-Replay(Counter Based) : 64
        p50 = re.compile(r"^Anti-Replay.*: +(?P<anti_replay_count>\d+)$")

        # tag method : disabled
        p51 = re.compile(r"^tag method.*: +(?P<tag_method>[disabled|enabled]+)$")

        # alg key size: 32 (bytes)
        p52 = re.compile(r"^alg key.*: +(?P<alg_key_size_bytes>[\d]+) +\(bytes\)$")

        # sig key size: 32 (bytes)
        p53 = re.compile(r"^sig key.*: +(?P<sig_key_size_bytes>[\d]+) +\(bytes\)$")

        # encaps: ENCAPS_TUNNEL
        p54 = re.compile(r"^encaps.*: +(?P<encaps>[\w\S]+)$")

        # KGS POLICY:
        p55 = re.compile(r"^KGS POLICY:$")

        # P2P POLICY:
        p56 = re.compile(r"^P2P POLICY:$")

        # REG_GM: local_addr 3.3.1.1
        p57 = re.compile(r"^REG_GM.* +(?P<local_addr>[\d\.]+)$")

        # Unicast rekey received: 25
        p58 = re.compile(r"^Unicast rekey .* +(?P<uncicast_rekey_received>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line=line.strip()
            
            # Group Name               : getvpn1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group_name', {}).setdefault(group['group_name'],{}).setdefault("group_information",{})
                continue
            
            # Group Identity           : 1223
            m = p2.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Group Type               : GDOI (ISAKMP)
            m = p3.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Crypto Path              : ipv4
            m = p4.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Key Management Path      : ipv4
            m = p5.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Rekeys received          : 25
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # IPSec SA Direction       : Both
            m = p7.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Group Server list       : 1.1.1.1
            m = p8.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Group Member Information For Group getvpn1:
            m = p9.match(line)
            if m:
                mem_info_dict = group_dict.setdefault("group_member_information",{})
                continue
            
            # ACL Received From KS     : gdoi_group_getvpn1_temp_acl
            m = p10.match(line)
            if m:
                mem_info_dict.update(m.groupdict())
                continue
            
            # Group member             : 3.3.1.1         vrf: None
            m = p11.match(line)
            if m:
                group = m.groupdict()
                mem_dict = group_dict.setdefault("group_member",{}).setdefault(group['group_member'], {})
                mem_dict.update({'vrf' :group['vrf']})
                continue
            
            # Local addr/port       : 3.3.1.1/848
            m = p12.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Remote addr/port      : 1.1.1.1/848
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group['remote_addr_port'] = int(group['remote_addr_port'])
                mem_dict.update(group)
                continue
            
            # fvrf/ivrf             : None/None
            m = p14.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Version               : 1.0.26
            m = p15.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Registration status   : Registered
            m = p16.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Registered with       : 1.1.1.1
            m = p17.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Re-registers in       : 449 sec
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Succeeded registration: 1
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Attempted registration: 1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue

            # Last rekey from       : 1.1.1.1
            m = p21.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Last rekey seq num    : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Rekey ACKs sent       : 25
            m = p23.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Unicast rekey received: 25
            m = p58.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Rekey Rcvd(hh:mm:ss)  : 00:01:30
            m = p24.match(line)
            if m:
                mem_dict.update(group)
                continue
            
            # PFS Rekey received    : 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # DP Error Monitoring   : OFF
            m = p26.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # IPSEC init reg executed    : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # IPSEC init reg postponed   : 0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Active TEK Number     : 2
            m = p29.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue

            # SA Track (OID/status) : disabled
            m = p30.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Fail-Close Revert : Disabled
            m = p31.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # allowable rekey cipher: any
            m = p32.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
             # allowable rekey hash  : any
            m = p33.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # allowable transformtag: any ESP
            m = p34.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Total received        : 25
            m = p35.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict=mem_info_dict.setdefault("rekeys_cumulative", {})
                cum_dict.update(group)
                continue
            
            # After latest register : 25
            m = p36.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict.update(group)
                continue
            
            # Rekey Acks sents      : 25
            m = p37.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict.update(group)
                continue
            
            # ACL Downloaded From KS 1.1.1.1:
            m = p38.match(line)
            if m:
                group = m.groupdict()
                acl_list = mem_info_dict.setdefault("acl_download_from_ks",{}).setdefault(group['ks_server'],{}).setdefault('acl_list',[])
                continue
            
            # access-list   permit ip 25.25.0.0 0.0.255.255 15.15.0.0 0.0.255.255
            # access-list   permit ip 15.15.0.0 0.0.255.255 25.25.0.0 0.0.255.255
            # access-list   permit ip 16.16.0.0 0.0.255.255 26.26.0.0 0.0.255.255
            m = p39.match(line)
            if m:
                acl_list.append(line)
                continue
            

            # Rekey Transport Type     : Unicast
            m = p40.match(line)
            if m:
                kek_policy_dict = group_dict.setdefault("kek_policy",{})
                kek_policy_dict.update(m.groupdict())
                continue
            

            # Lifetime (secs)          : 1109
            m = p41.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # Encrypt Algorithm        : AES
            m = p42.match(line)
            if m:
                kek_policy_dict.update(m.groupdict())
                continue
            
            # Key Size                 : 256
            m = p43.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # Sig Hash Algorithm       : HMAC_AUTH_SHA
            m = p44.match(line)
            if m:
                kek_policy_dict.update(m.groupdict())
                continue
            
            # Sig Key Length (bits)    : 4400
            m = p45.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # GigabitEthernet0/0/1:
            m = p46.match(line)
            if m:
                group = m.groupdict()
                tek_policy_dict = group_dict.setdefault("tek_policy",{}).setdefault('interfaces',{}).setdefault(group['interface'],{})
                continue
            
            # spi: 0x5A69F51E(1516893470)
            m = p47.match(line)
            if m:
                group = m.groupdict()
                spi_dict = tek_policy_dict.setdefault('ipsec_sa', {}).setdefault('spi', {}).setdefault(group['spi'], {})
                continue
            

            # transform: esp-256-aes esp-sha256-hmac
            m = p48.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # sa timing:remaining key lifetime (sec): (510)
            m = p49.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # Anti-Replay(Counter Based) : 64
            m = p50.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            

            # tag method : disabled
            m = p51.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # alg key size: 32 (bytes)
            m = p52.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # sig key size: 32 (bytes)
            m = p53.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # encaps: ENCAPS_TUNNEL
            m = p54.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # KGS POLICY:
            m = p55.match(line)
            if m:
                kgs_policy_dict = group_dict.setdefault('kgs_policy', {}).setdefault('reg_gm', {})
                continue
            
            # P2P POLICY:
            m = p56.match(line)
            if m:
                p2p_policy_dict = group_dict.setdefault('p2p_policy', {}).setdefault('reg_gm', {})
                continue
            
            # REG_GM: local_addr 3.3.1.1
            m = p57.match(line)
            if m:
                if 'p2p_policy' not in group_dict:kgs_policy_dict.update(m.groupdict())
                else:p2p_policy_dict.update(m.groupdict())
                continue
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi detail'
# =================================================
class ShowCryptoGdoiDetail(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gdoi detail'
    '''
    cli_command = "show crypto gdoi detail"

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Parser for 'show crypto gdoi group {group_name}'
# =================================================
class ShowCryptoGdoiGroup(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gdoi group {group_name}'
    '''
    cli_command = "show crypto gdoi group {group_name}"

    def cli(self, group_name = '', output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Parser for 'show crypto gkm'
# =================================================
class ShowCryptoGkm(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gkm'
    '''
    cli_command = "show crypto gkm"

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Schema for 'show crypto gdoi ks policy'
# =================================================

class ShowCryptoGdoiKsPolicySchema(MetaParser):
    """Schema for show crypto gdoi ks policy"""
    schema =  {
                "key_server_policy":{
                    "group":{
                        Any():{
                            "handle":str,
                            "server":{
                                Any():{
                                    "handle":str,
                                    "kek_policy":{
                                        "spi":{
                                            Any():{
                                                "acknowledgement":str,
                                                "crypto_iv_length":int,
                                                "encrypt_alg":str,
                                                "key_size":int,
                                                "management_alg":str,
                                                "orig_life_secs":int,
                                                "remaining_life_secs":int,
                                                "sig_hash_algorithm":str,
                                                "sig_key_length":int,
                                                "sig_key_name":str,
                                                "sig_size":int,
                                                "time_to_rekey_sec":str
                                                }
                                            },
                                        "transport_type":str
                                        },
                                    "seq_num":int,
                                    "tek_policy":{
                                        "encaps":str,
                                        "spi":{
                                            Any():{
                                                "access_list":str,
                                                "alg_key_size":int,
                                                "antireplay_window_size":int,
                                                "elapsed_time_sec":int,
                                                "orig_life_secs":int,
                                                "override_life_sec":int,
                                                "remaining_life_secs":int,
                                                "sig_key_size":int,
                                                "tek_life_sec":int,
                                                Optional("time_to_rekey_sec"):str,
                                                "transform":str
                                                },
                                            }
                                        },
                                    "teks_num":int
                                    }
                                }
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi ks policy'
# =================================================
class ShowCryptoGdoiKsPolicy(ShowCryptoGdoiKsPolicySchema):
    """Parser for show crypto ikev2 policy"""

    cli_command = ['show crypto gdoi ks policy']

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # For group getvpn1 (handle: 0x40000002) server 1.1.1.1 (handle: 0x40000002):
        p1 = re.compile(r"^For group +(?P<group_name>\w+) +\(handle: +(?P<group_handle>[\w]+)\) +server +(?P<server_ip>[\d\.]+) +\(handle: +(?P<server_handle>\w+)\):$")

        # # of teks : 2  Seq num : 0
        p2 = re.compile(r"^# of teks : +(?P<teks_num>\d+) + Seq num : +(?P<seq_num>\d+)$")

        # KEK POLICY (transport type : Unicast)
        p3 = re.compile(r"^KEK POLICY +\(transport type : +(?P<transport_type>\w+)\)$")

        # spi : 0xEEB0E9A2BBD4C71AF1034F6B24EB8022
        p4 = re.compile(r"^spi : +(?P<spi>\w+)$")

        # management alg     : disabled      encrypt alg           : AES
        p5 = re.compile(r"^management alg.*: +(?P<management_alg>[\disbaled|enabled]+) +encrypt alg.*: +(?P<encrypt_alg>\w+)$")

        # crypto iv length   : 16            key size              : 32
        p6 = re.compile(r"^crypto iv length.*: +(?P<crypto_iv_length>\d+) +key size.*: +(?P<key_size>\d+)$")

        # orig life(sec)     : 1200          remaining life(sec)   : 787
        p7 = re.compile(r"^orig life.*: +(?P<orig_life_secs>\d+) +remaining.*: +(?P<remaining_life_secs>\d+)$")

        # time to rekey (sec): 552
        p8 = re.compile(r"^time to rekey.* +(?P<time_to_rekey_sec>[\d\S]+)$")

        # sig hash algorithm : enabled       sig key length        : 550
        p9 = re.compile(r"^sig hash algorithm.* +(?P<sig_hash_algorithm>[enabled|disabled]+) +sig key length.* +(?P<sig_key_length>\d+)$")

        # sig size           : 512
        p10 = re.compile(r"^sig size.*: +(?P<sig_size>\d+)$")

        # sig key name       : REKEYRSA
        p11 = re.compile(r"^sig key name.*: +(?P<sig_key_name>\w+)$")

        # acknowledgement    : Cisco
        p12 = re.compile(r"^acknowledgement.*: +(?P<acknowledgement>\w+)$")

        # TEK POLICY (encaps : ENCAPS_TUNNEL)
        p13 = re.compile(r"^TEK POLICY +\(encaps : +(?P<encaps>\w+)\)$")

        # spi                : 0xEE021924
        p14 = re.compile(r"^spi.*: +(?P<spi>\w+)$")

        # access-list        : acl1
        p15 = re.compile(r"^access-list.*: +(?P<access_list>\w+)$")

        # transform          : esp-256-aes esp-sha256-hmac
        p16 = re.compile(r"^transform.*: +(?P<transform>[\w\s\S]+)$")

        #  alg key size       : 32            sig key size          : 32
        p17 = re.compile(r"^alg key size.*: +(?P<alg_key_size>\d+) +sig key size.* +(?P<sig_key_size>\d+)$")

        # tek life(sec)      : 600           elapsed time(sec)     : 412
        p18 = re.compile(r"^tek life.*: +(?P<tek_life_sec>\d+) +elapsed time.* +(?P<elapsed_time_sec>\d+)$")

        # override life(sec) : 0             antireplay window size: 64
        p19 = re.compile(r"^override life.*: +(?P<override_life_sec>\d+) +antireplay window size.*: +(?P<antireplay_window_size>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # For group getvpn1 (handle: 0x40000002) server 1.1.1.1 (handle: 0x40000002):
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('key_server_policy', {}).setdefault('group', {}).setdefault(group['group_name'], {})
                group_dict.update({'handle':group['group_handle']})
                server_dict = group_dict.setdefault('server',{}).setdefault(group['server_ip'], {})
                server_dict.update({'handle':group['server_handle']})
                continue
            
            # # of teks : 2  Seq num : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                server_dict.update(group)
                continue

            # KEK POLICY (transport type : Unicast)
            m = p3.match(line)
            if m:
                kek_policy_dict = server_dict.setdefault('kek_policy', {})
                kek_policy_dict.update(m.groupdict())
                continue

            # spi : 0xEEB0E9A2BBD4C71AF1034F6B24EB8022
            m = p4.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict = kek_policy_dict.setdefault('spi',{}).setdefault(group['spi'], {})
                continue

            # management alg     : disabled      encrypt alg           : AES
            m = p5.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # crypto iv length   : 16            key size              : 32
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_spi_dict.update(group)
                continue
            
            # sig hash algorithm : enabled       sig key length        : 550
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group['sig_key_length'] = int(group['sig_key_length']) 
                kek_spi_dict.update(group)
                continue
            
            # sig size           : 512
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_spi_dict.update(group)
                continue
            
            # sig key name       : REKEYRSA
            m = p11.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # acknowledgement    : Cisco
            m = p12.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # TEK POLICY (encaps : ENCAPS_TUNNEL)
            m = p13.match(line)
            if m:
                tek_policy_dict = server_dict.setdefault('tek_policy', {})
                tek_policy_dict.update(m.groupdict())
                continue
            
            # spi                : 0xEE021924
            m = p14.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict = tek_policy_dict.setdefault('spi',{}).setdefault(group['spi'], {})
                continue
            
            # access-list        : acl1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict.update(group)
                continue
            
            # transform          : esp-256-aes esp-sha256-hmac
            m = p16.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict.update(group)
                continue
            
            # alg key size       : 32            sig key size          : 32
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # tek life(sec)      : 600           elapsed time(sec)     : 412
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # override life(sec) : 0             antireplay window size: 64
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # orig life(sec)     : 1200          remaining life(sec)   : 787
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                if 'tek_policy' not in server_dict: kek_spi_dict.update(group)
                else: tek_spi_dict.update(group)
                continue
            
            # time to rekey (sec): 552
            # time to rekey (sec): 62
            # time to rekey (sec): n/a
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if 'tek_policy' not in server_dict: kek_spi_dict.update(group)
                else: tek_spi_dict.update(group)
                continue
        return master_dict

# =================================================
#  Schema for 'show crypto gdoi gm dataplan counter'
# =================================================
class ShowCryptoGdoiGmDataplanCounterSchema(MetaParser):
    """Schema for show crypto gdoi gm dataplan counter"""
    schema =  {
                "data_plane_statistics":{
                    "group":{
                        Any():{
                            "pkts_decrypt":int,
                            "pkts_encrypt":int,
                            "pkts_invalid_prot":int,
                            "pkts_no_sa":int,
                            "pkts_not_tagged":int,
                            "pkts_not_untagged":int,
                            "pkts_tagged":int,
                            "pkts_untagged":int,
                            "pkts_verify_fail":int
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi gm dataplan counter'
# =================================================
class ShowCryptoGdoiGmDataplanCounter(ShowCryptoGdoiGmDataplanCounterSchema):
    """Parser for show crypto gdoi gm dataplan counter"""

    cli_command = ['show crypto gdoi gm dataplan counter']

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Data-plane statistics for group getvpn1:
        p1 = re.compile(r"^Data-plane statistics for group +(?P<group_name>[\w\S]+):$")

        # #pkts encrypt            : 21592009    #pkts decrypt            : 0
        p2 = re.compile(r"^#pkts encrypt.*: +(?P<pkts_encrypt>\d+) +#pkts decrypt.*: +(?P<pkts_decrypt>\d+)$")

        # #pkts tagged (send)      : 0        #pkts untagged (rcv)     : 0
        p3 = re.compile(r"^#pkts tagged.*: +(?P<pkts_tagged>\d+) +#pkts untagged.*: +(?P<pkts_untagged>\d+)$")

        # #pkts no sa (send)       : 0        #pkts invalid sa (rcv)   : 0
        p4 = re.compile(r"^#pkts no sa.*: +(?P<pkts_no_sa>\d+) +#pkts invalid sa.*: +(?P<pkts_untagged>\d+)$")

        # #pkts encaps fail (send) : 0        #pkts decap fail (rcv)   : 0
        p5 = re.compile(r"^#pkts encaps fail.*: +(?P<pkts_tagged>\d+) +#pkts decap fail.*: +(?P<pkts_untagged>\d+)$")

        # #pkts invalid prot (rcv) : 0        #pkts verify fail (rcv)  : 0
        p6 = re.compile(r"^#pkts invalid prot.*: +(?P<pkts_invalid_prot>\d+) +#pkts verify fail.*: +(?P<pkts_verify_fail>\d+)$")

        # #pkts not tagged (send)  : 0        #pkts not untagged (rcv) : 0
        p7 = re.compile(r"^#pkts not tagged.*: +(?P<pkts_not_tagged>\d+) +#pkts not untagged.*: +(?P<pkts_not_untagged>\d+)$")

        # #pkts internal err (send): 0        #pkts internal err (rcv) : 0
        p8 = re.compile(r"^#pkts internal err.*: +(?P<pkts_encrypt>\d+) +#pkts internal err.*: +(?P<pkts_decrypt>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Data-plane statistics for group getvpn1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('data_plane_statistics', {}).setdefault('group', {}).setdefault(group['group_name'], {})
                continue
            
            # #pkts encrypt            : 21592009    #pkts decrypt            : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # #pkts tagged (send)      : 0        #pkts untagged (rcv)     : 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts no sa (send)       : 0        #pkts invalid sa (rcv)   : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # #pkts encaps fail (send) : 0        #pkts decap fail (rcv)   : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts invalid prot (rcv) : 0        #pkts verify fail (rcv)  : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts not tagged (send)  : 0        #pkts not untagged (rcv) : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts internal err (send): 0        #pkts internal err (rcv) : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

        return master_dict

# ==============================
# Schema for
#   'show crypto gdoi feature dp-recovery'
# ==============================
class ShowCryptoGdoiFeatureSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi feature dp-recovery'
    """

    schema = {
        'group': {
            Any():{
                'key_server':{
                    Any():{
                        'key_server_id': str,
                        'key_version': str,
                        'key_feature_supported': str
                    },
                },
                'group_member':{
                    Any():{
                        'group_member_id': str,
                        'group_member_version': str,
                        'group_feature_supported': str
                    },                   
                },
            },
        },
    }


# =================================================
#  Parser for 'show crypto gdoi feature'
# =================================================

class ShowCryptoGdoiFeature(ShowCryptoGdoiFeatureSchema):
    
    """Parser for 'show crypto gdoi feature' """
    
    cli_command = 'show crypto gdoi feature'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Group Name: getvpn1
        p1 = re.compile(r'^Group Name:\s(?P<group>[\S]+)$')

        #     Key Server ID       Version   Feature Supported
        p2 = re.compile(r'Key Server ID \s+Version\s+Feature\sSupported')

        #         15.15.15.1          1.0.26         Yes
        p3 = re.compile(r'(?P<key_server_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<key_version>[\d\.]+)\s+(?P<key_feature_supported>[\w]+)$')

        #    Group Member ID     Version   Feature Supported
        p4 = re.compile(r'Group Member ID\s+Version\s+Feature\sSupported')

        #         25.25.25.1          1.0.25         Yes
        p5 = re.compile(r'(?P<group_member_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<group_member_version>[\d\.]+)\s+(?P<group_feature_supported>[\w]+)$')

        master_dict = {}
        server_flag = False
        member_flag = False
        for line in output.splitlines():

            line = line.strip()
            
            # Group Name: getvpn1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                continue
                
            #     Key Server ID       Version   Feature Supported
            m = p2.match(line)
            if m:
                group = m.groupdict()
                server_dict = group_dict.setdefault('key_server', {})
                server_flag = True
                continue

            #         1.1.1.1          1.0.27         Yes
            if server_flag:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ser_count_dict = server_dict.setdefault(len(server_dict)+1, {})
                    ser_count_dict.update({'key_server_id': group['key_server_id']})
                    ser_count_dict.update({'key_version': group['key_version']})
                    ser_count_dict.update({'key_feature_supported': group['key_feature_supported']})                    
                    continue

            #    Group Member ID     Version   Feature Supported
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member_dict = group_dict.setdefault('group_member', {})
                server_flag = False
                member_flag = True
                continue

            #        3.3.1.1          1.0.26         Yes
            if member_flag:
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    count_dict = group_member_dict.setdefault(len(group_member_dict)+1, {})
                    count_dict.update({'group_member_id' : group['group_member_id']})
                    count_dict.update({'group_member_version': group['group_member_version']})
                    count_dict.update({'group_feature_supported': group['group_feature_supported']})
                    continue
                       
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi feature dp-recovery'
# =================================================
class ShowCryptoGdoiFeatureDpRecovery(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature dp-recovery'
    '''

    cli_command = "show crypto gdoi feature dp-recovery"

# =================================================
#  Parser for 'show crypto gdoi feature ckm'
# =================================================
class ShowCryptoGdoiFeatureCkm(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature ckm'
    '''

    cli_command = "show crypto gdoi feature ckm"

# =================================================
#  Parser for 'show crypto gdoi feature suite-b'
# =================================================
class ShowCryptoGdoiFeatureSuiteB(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature suite-b'
    '''

    cli_command = "show crypto gdoi feature suite-b"

# =================================================
#  Parser for 'show crypto gdoi feature policy-replace'
# =================================================
class ShowCryptoGdoiFeaturePolicyReplace(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature policy-replace'
    '''

    cli_command = "show crypto gdoi feature policy-replace"

# =================================================
#  Parser for 'show crypto gdoi feature gm-removal'
# =================================================
class ShowCryptoGdoiFeatureGmRemoval(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gm-removal'
    '''

    cli_command = "show crypto gdoi feature gm-removal"

# =================================================
#  Parser for 'show crypto gdoi feature gdoi-mib'
# =================================================
class ShowCryptoGdoiFeatureGdoiMib(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gdoi-mib'
    '''

    cli_command = "show crypto gdoi feature gdoi-mib"

# =================================================
#  Parser for 'show crypto gdoi feature gdoi-interop-ack'
# =================================================
class ShowCryptoGdoiFeatureGdoiInteropAck(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gdoi-interop-ack'
    '''

    cli_command = "show crypto gdoi feature gdoi-interop-ack"

# =================================================
#  Parser for 'show crypto gdoi feature ip-d3p'
# =================================================
class ShowCryptoGdoiFeatureIpD3p(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature ip-d3p'
    '''

    cli_command = "show crypto gdoi feature ip-d3p"

# =================================================
#  Parser for 'show crypto gdoi feature long-sa-lifetime'
# =================================================
class ShowCryptoGdoiFeatureLongSaLifetime(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature long-sa-lifetime'
    '''

    cli_command = "show crypto gdoi feature long-sa-lifetime"

# =================================================
#  Parser for 'show crypto gdoi feature pfs'
# =================================================
class ShowCryptoGdoiFeaturePfs(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature pfs'
    '''

    cli_command = "show crypto gdoi feature pfs"

    

# =================================================
# Schema for
#  Schema for 'show crypto gdoi gm'
# =================================================
class ShowCryptoGdoiGmSchema(MetaParser):
    """schema for show crypto gdoi gm"""

    schema = {
        'group_member': {
            Any(): {
                'direction': str, 
                'acl_recieved': str,
                'group_member_ip': str,
                'vrf': str,
                'local_ip': str,
                'local_port': int,
                'remote_ip': str,
                'remote_port': int,
                'fvrf': str,
                'ivrf': str,
                'version': str,
                'registration_status': str,
                'registered_ip': str,
                Optional('registered_time'): str,
                Optional('registration_succeded'): int,
                Optional('registration_attempt'): int,
                Optional('rekey_ip'): str,
                Optional('rekey_seq_num'): int,
                Optional('unicast_rekeys_recieved'): int,
                Optional('ack_unicast_key'): int,
                Optional('rekey_recieved_time'): str,
                Optional('pfs_rekey_recieved'): int,
                Optional('dp_error_monitoring'): str,
                Optional('ipsec_init_reg_executed'): int,
                Optional('ipsec_init_reg_postponed'): int,
                Optional('active_tek_number'): int,
                Optional('sa_track_status'): str,
                Optional('fail_close_revert'): str
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi gm'
# ===================================================
class ShowCryptoGdoiGm(ShowCryptoGdoiGmSchema):

    """Parser for show crypto gdoi gm"""

    cli_command = 'show crypto gdoi gm'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Group Member Information For Group getvpn1: 
        p1 = re.compile(r'^Group +Member +Information +For +Group +(?P<group_member>[\d\w]+)')
        #    IPSec SA Direction       : Both
        p2 = re.compile(r'^IPSec +SA +Direction +: +(?P<direction>[\w]+)$')
        #    ACL Received From KS     : gdoi_group_getvpn1_temp_acl
        p3 = re.compile(r'^ACL Received From KS     : (?P<acl_recieved>[\w\d_-]+)')
        #    Group member             : 3.3.1.1         vrf: None
        p4 = re.compile(r'^Group +member +: +(?P<group_member_ip>[\d.]+) +vrf: +(?P<vrf>[\w\d]+)')        
        #       Local addr/port       : 3.3.1.1/848
        p5 = re.compile(r'^Local addr.port +: +(?P<local_ip>[\d.]+).(?P<local_port>[\d]+)')
        #       Remote addr/port      : 1.1.1.1/848
        p6 = re.compile(r'^Remote +addr.port +: +(?P<remote_ip>[\d.]+).(?P<remote_port>[\d]+)')
        #       fvrf/ivrf             : None/None
        p7 = re.compile(r'^fvrf.ivrf +: +(?P<fvrf>[\d\w]+).(?P<ivrf>[\d\w]+)')
        #       Version               : 1.0.26
        p8 = re.compile(r'^Version +: +(?P<version>[\d.]+)')
        #       Registration status   : Registered
        p9 = re.compile(r'^Registration +status +: +(?P<registration_status>[\w]+)')
        #       Registered with       : 1.1.1.1
        p10 = re.compile(r'^Registered +with +: +(?P<registered_ip>[\d.]+)')
        #       Re-registers in       : 518 sec
        p11 = re.compile(r'^Re\-registers +in +: +(?P<registered_time>[\d\w ]+)')
        #       Succeeded registration: 1
        p12 = re.compile(r'^Succeeded +registration: +(?P<registration_succeded>[\d]+)')
        #       Attempted registration: 1
        p13 = re.compile(r'^Attempted +registration: +(?P<registration_attempt>[\d]+)')
        #       Last rekey from       : 1.1.1.1
        p14 = re.compile(r'^Last +rekey +from +: +(?P<rekey_ip>[\d.]+)')
        #       Last rekey seq num    : 1
        p15 = re.compile(r'^Last +rekey +seq +num +: +(?P<rekey_seq_num>[\d]+)')
        #       Unicast rekey received: 26
        p16 = re.compile(r'^Unicast +rekey +received: +(?P<unicast_rekeys_recieved>[\d]+)')
        #       Rekey ACKs sent       : 26
        p17 = re.compile(r'^Rekey +ACKs +sent +: +(?P<ack_unicast_key>[\d]+)')
        #       Rekey Rcvd(hh:mm:ss)  : 00:00:19
        p18 = re.compile(r'^Rekey +Rcvd.hh:mm:ss. +: +(?P<rekey_recieved_time>[\d:]+)')
        #       PFS Rekey received    : 0
        p19 = re.compile(r'^PFS +Rekey +received +: +(?P<pfs_rekey_recieved>[\d]+)')
        #       DP Error Monitoring   : OFF
        p20 = re.compile(r'^DP +Error +Monitoring +: +(?P<dp_error_monitoring>[\w]+)')
        #       IPSEC init reg executed    : 0
        p21 = re.compile(r'^IPSEC +init +reg +executed +: +(?P<ipsec_init_reg_executed>[\d]+)')
        #       IPSEC init reg postponed   : 0
        p22 = re.compile(r'^IPSEC +init +reg +postponed +: +(?P<ipsec_init_reg_postponed>[\d]+)')
        #       Active TEK Number     : 2
        p23 = re.compile(r'^Active +TEK +Number +: +(?P<active_tek_number>[\d]+)')
        #       SA Track (OID/status) : disabled
        p24 = re.compile(r'^SA +Track +.OID.status. +: +(?P<sa_track_status>[\w]+)')
        #       Fail-Close Revert : Disabled
        p25 = re.compile(r'^Fail.Close +Revert +: +(?P<fail_close_revert>[\w]+)')

        # initial return dictionary
        ret_dict = {}
  
        for line in out.splitlines():
            line=line.strip()
            #Group Member Information For Group getvpn1:
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                group_member = ret_dict.setdefault('group_member', {}).setdefault(group['group_member'], {})           
                continue

            #    IPSec SA Direction       : Both            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'direction': group['direction']})
                continue

            #    ACL Received From KS     : gdoi_group_getvpn1_temp_acl            
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'acl_recieved': group['acl_recieved']})
                continue

            #    Group member             : 3.3.1.1         vrf: None
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'group_member_ip': group['group_member_ip']})
                group_member.update({'vrf': group['vrf']})
                continue                

            #Local addr/port       : 3.3.1.1/848
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'local_ip': group['local_ip']})
                group_member.update({'local_port': int(group['local_port'])})
                continue            

            #       Remote addr/port      : 1.1.1.1/848
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'remote_ip': group['remote_ip']})
                group_member.update({'remote_port': int(group['remote_port'])})
                continue
                
            #       fvrf/ivrf             : None/None
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'fvrf': group['fvrf']})
                group_member.update({'ivrf': group['ivrf']})
                continue
                
            #       Version               : 1.0.26
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'version': group['version']})
                continue

            #       Registration status   : Registered
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_status': group['registration_status']})
                continue

            #       Registered with       : 1.1.1.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registered_ip': group['registered_ip']})
                continue

            #Re-registers in       : 518 sec
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registered_time': group['registered_time']})
                continue

            #       Succeeded registration: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_succeded': int(group['registration_succeded'])})
                continue

            #       Attempted registration: 1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_attempt': int(group['registration_attempt'])})
                continue

            #       Last rekey from       : 1.1.1.1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_ip': group['rekey_ip']})
                continue

            #       Last rekey seq num    : 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_seq_num': int(group['rekey_seq_num'])})
                continue

            #       Unicast rekey received: 26
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'unicast_rekeys_recieved': int(group['unicast_rekeys_recieved'])})
                continue

            #       Rekey ACKs sent       : 26
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ack_unicast_key': int(group['ack_unicast_key'])})
                continue

            #       Rekey Rcvd(hh:mm:ss)  : 00:00:19
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_recieved_time': group['rekey_recieved_time']})
                continue

            #       PFS Rekey received    : 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'pfs_rekey_recieved': int(group['pfs_rekey_recieved'])})
                continue

            #       DP Error Monitoring   : OFF
            m = p20.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'dp_error_monitoring': group['dp_error_monitoring']})
                continue

            #       IPSEC init reg executed    : 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ipsec_init_reg_executed': int(group['ipsec_init_reg_executed'])})
                continue

            #       IPSEC init reg postponed   : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ipsec_init_reg_postponed': int(group['ipsec_init_reg_postponed'])})
                continue

            #       Active TEK Number     : 2
            m = p23.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'active_tek_number': int(group['active_tek_number'])})
                continue

            #       SA Track (OID/status) : disabled
            m = p24.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'sa_track_status': group['sa_track_status']})
                continue

            #       Fail-Close Revert : Disabled
            m = p25.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'fail_close_revert': group['fail_close_revert']})
                continue        
        return ret_dict




# =================================================
#  Schema for 'show crypto gdoi ks'
# =================================================
class ShowCryptoGdoiKsSchema(MetaParser):
    """schema for show crypto gdoi ks"""
    schema = {
        'crypto_gdoi_ks': {
            'total_group_members': int,
            'crypto_gdoi_ks_group': {
                'key_server_group_name': str,
                'group_name': str,
                'reauth_status': str,
                'group_identity': int,
                'group_type': str,
                'group_members': int,
                'rekey_ack_config': str,
                'direction': str,
                'd3p_window_status': str,
                'sr_factor': int,
                'ckm_status': str,
                'acl_configured': {
                    'acl_name': str
                },
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks'
# ===================================================
class ShowCryptoGdoiKs(ShowCryptoGdoiKsSchema):
    """Parser for show crypto gdoi ks"""
    cli_command = 'show crypto gdoi ks'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        #Total group members registered to this box: 2
        p1 = re.compile(r'^Total +group +members +registered +to +this +box: +(?P<total_group_members>[\d]+)$')
        #Key Server Information For Group getvpn1:
        p2 = re.compile(r'^Key +Server +Information +For +Group +(?P<key_server_group_name>[\w\d]+):$')
        #    Group Name               : getvpn1
        p3 = re.compile(r'Group +Name +: +(?P<group_name>[\w\d]+)$')
        #    Re-auth on new CRL       : Disabled
        p4 = re.compile(r'^Re.auth +on +new +CRL +: +(?P<reauth_status>[\w]+)$')
        #    Group Identity           : 1223
        p5 = re.compile(r'^Group +Identity +: +(?P<group_identity>[\d]+)$')
        #    Group Type               : GDOI (ISAKMP)
        p6 = re.compile(r'^Group +Type +: +(?P<group_type>[\w \(\)]+)$')
        #    Group Members            : 2
        p7 = re.compile(r'^Group +Members +: +(?P<group_members>[\d]+)$')
        #    Rekey Acknowledgement Cfg: Cisco
        p8 = re.compile(r'^Rekey +Acknowledgement +Cfg: +(?P<rekey_ack_config>[\w]+)$')
        #    IPSec SA Direction       : Both
        p9 = re.compile(r'^IPSec +SA +Direction +: +(?P<direction>[\w]+)$')
        #    IP D3P Window            : Disabled
        p10 = re.compile(r'IP +D3P +Window +: +(?P<d3p_window_status>[\w]+)$')
        #    Split Resiliency Factor  : 0
        p11 = re.compile(r'^Split +Resiliency +Factor +: +(?P<sr_factor>[\d]+)$')
        #    CKM status               : Disabled
        p12 = re.compile(r'^CKM +status +: +(?P<ckm_status>[\w]+)$')
        #    ACL Configured:
        #        access-list acl1
        p13 = re.compile(r'^access.list +(?P<acl_name>[\w\d]+)$')

        ret_dict = {}
  
        for line in output.splitlines():
            line = line.strip()
            #Total group members registered to this box: 2
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                crypto_gdoi_ks = ret_dict.setdefault('crypto_gdoi_ks', {})
                crypto_gdoi_ks.update({'total_group_members': int(group['total_group_members'])})
                continue

            #Key Server Information For Group getvpn1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group = crypto_gdoi_ks.setdefault('crypto_gdoi_ks_group', {})
                crypto_gdoi_ks_group.update({'key_server_group_name': group['key_server_group_name']})
                continue

            #    Group Name               : getvpn1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_name': group['group_name']})
                continue

            #    Re-auth on new CRL       : Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'reauth_status': group['reauth_status']})
                continue

            #    Group Identity           : 1223
            m = p5.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_identity': int(group['group_identity'])})
                continue
                
            #    Group Type               : GDOI (ISAKMP)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_type': group['group_type']})
                continue
                
            #    Group Members            : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_members': int(group['group_members'])})
                continue

            #    Rekey Acknowledgement Cfg: Cisco
            m = p8.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'rekey_ack_config': group['rekey_ack_config']})
                continue

            #    IPSec SA Direction       : Both
            m = p9.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'direction': group['direction']})
                continue

            #    IP D3P Window            : Disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'d3p_window_status': group['d3p_window_status']})
                continue

            #    Split Resiliency Factor  : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'sr_factor': int(group['sr_factor'])})
                continue

            #    CKM status               : Disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'ckm_status': group['ckm_status']})
                continue

            #    ACL Configured:
            #        access-list acl1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                acl_configured = crypto_gdoi_ks_group.setdefault('acl_configured', {})
                acl_configured.update({'acl_name': group['acl_name']})
                continue
        
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi rekey sa'
# =================================================
class ShowCryptoGdoiRekeySaSchema(MetaParser):
    """schema for show crypto gdoi rekey sa"""
    
    schema = {
        'getvpn_rekey': {
            Any(): {
                'dst_ip': str,
                'src_ip': str,
                'connection_id': int,
                'rekey_status': str
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi rekey sa'
# ===================================================
class ShowCryptoGdoiRekeySa(ShowCryptoGdoiRekeySaSchema):
    """Parser for show crypto gdoi rekey sa"""
    
    cli_command = 'show crypto gdoi rekey sa'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # dst             src             conn-id         status
        p0 = re.compile(r'dst +src +conn.id +status')

        # 3.3.1.1         1.1.1.1         1712            ACTIVE
        p1 = re.compile(r'(?P<dst_ip>[\d.]+) +(?P<src_ip>[\d.]+) +(?P<connection_id>[\d]+) +(?P<rekey_status>[\w]+)')
        
        ret_dict = {}
  
        for line in output.splitlines():
            line=line.strip()
            
            m = p0.match(line)
            if m:
                group = m.groupdict()
                getvpn_rekey = ret_dict.setdefault('getvpn_rekey', {})
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()                
                count_dict = getvpn_rekey.setdefault(len(getvpn_rekey)+1, {})
                count_dict.update({'dst_ip': group['dst_ip']})
                count_dict.update({'src_ip': group['src_ip']})
                count_dict.update({'connection_id': int(group['connection_id'])})
                count_dict.update({'rekey_status': group['rekey_status']})                
                continue
        
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi rekey sa detail'
# =================================================
class ShowCryptoGdoiRekeySaDetailSchema(MetaParser):
    """schema for show crypto gdoi rekey sa detail"""
    schema = {
        'kek_sa_db_stats': {
            'num_active': int,
            'num_malloc': int,
            'num_free': int,
            'kek_policy': {
                'transport_type': str,
                'local_addr': str,
                'local_port': int,
                'remote_details': {
                    'remote_addr': str,
                    'remote_port': int,
                    'spi': str,
                    'mgmt_alg_status': str,
                    'encrypt_alg': str,
                    'crypto_iv_length': int,
                    'key_size': int,
                    'orig_life': int,
                    'sig_hash_alg_status': str,
                    'sig_key_length': int,
                    'sig_size': int,
                    'ack': str,
                    'connection_type': str,
                    'connection_id': int,
                    'seq_num': int,
                    'prev_seq_num': int,
                    'handle': int,
                    'interface_type': str,
                    'group_name': str
                },
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi rekey sa detail'
# ===================================================
class ShowCryptoGdoiRekeySaDetail(ShowCryptoGdoiRekeySaDetailSchema):

    """Parser for show crypto gdoi rekey sa detail"""

    cli_command = 'show crypto gdoi rekey sa detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # num_active = 1
        p1 = re.compile(r'num_active += +(?P<num_active>[\d]+)')
        
        # num_malloc = 107
        p2 = re.compile(r'num_malloc += +(?P<num_malloc>[\d]+)')
        
        # num_free = 105
        p3 = re.compile(r'num_free += +(?P<num_free>[\d]+)')
        
        #  KEK POLICY (transport type : Unicast)
        p4 = re.compile(r'KEK +POLICY +.transport +type +: +(?P<transport_type>[\w]+).')
        
        #   Local addr/port : 26.26.26.1/848
        p5 = re.compile(r'Local +addr.port +: +(?P<local_addr>[\d.]+).(?P<local_port>[\d]+)')
        
        #   Remote addr/port : 15.15.15.1/848
        p6 = re.compile(r'Remote +addr.port +: +(?P<remote_addr>[\d.]+).(?P<remote_port>[\d]+)')
        
        #    spi : 0x5C78568A11D464C47E9268A1D9A8787D
        p7 = re.compile(r'spi +: +(?P<spi>[\w\d]+)')
        
        #    management alg     : disabled    encrypt alg       : AES       
        p8 = re.compile(r'management +alg +: +(?P<mgmt_alg_status>[\w]+) +encrypt +alg +: +(?P<encrypt_alg>[\w]+)')
        
        #    crypto iv length   : 16          key size          : 32      
        p9 = re.compile(r'crypto +iv +length +: +(?P<crypto_iv_length>[\d]+)  +key +size +: +(?P<key_size>[\d]+)')
        
        #    orig life(sec)     : 0         
        p10 = re.compile(r'orig +life.sec. +: +(?P<orig_life>[\d]+)')
        
        #    sig hash algorithm : enabled     sig key length    : 294     
        p11 = re.compile(r'sig +hash +algorithm +: +(?P<sig_hash_alg_status>[\w]+) +sig +key +length +: +(?P<sig_key_length>[\d]+)')
        
        #    sig size           : 256
        p12 = re.compile(r'sig +size +: +(?P<sig_size>[\d]+)')
        
        #    acknowledgement    : Cisco
        p13 = re.compile(r'acknowledgement +: +(?P<ack>[\w]+)')
        
        #    conn_id (IKEv1)    : 1138
        p14 = re.compile(r'conn_id +.(?P<connection_type>[\w\d]+). +: +(?P<connection_id>[\d]+)')
        
        #    seq num            : 0           prev seq num      : 0       
        p15 = re.compile(r'seq +num +: +(?P<seq_num>[\d]+) +prev +seq +num +: +(?P<prev_seq_num>[\d]+)')
        
        #    handle             : 40000072  
        p16 = re.compile(r'handle +: +(?P<handle>[\d]+)')
        
        #    Interface          : GigabitEthernet
        p17 = re.compile(r'Interface +: +(?P<interface_type>[\w]+)')
        
        #    Group Name         : GV-GROUP1
        p18 = re.compile(r'Group +Name +: +(?P<group_name>[\d\w._-]+)')

        ret_dict = {}
  
        for line in output.splitlines():
            line=line.strip()
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats = ret_dict.setdefault('kek_sa_db_stats', {})
                kek_sa_db_stats.update({'num_active': int(group['num_active'])})
                continue

            m = p2.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats.update({'num_malloc': int(group['num_malloc'])})
                continue

            m = p3.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats.update({'num_free': int(group['num_free'])})
                continue

            m = p4.match(line) 
            if m:
                group = m.groupdict()
                kek_policy = kek_sa_db_stats.setdefault('kek_policy', {})
                kek_policy.update({'transport_type': group['transport_type']})
                continue

            m = p5.match(line) 
            if m:
                group = m.groupdict()
                kek_policy.update({'local_addr': group['local_addr']})
                kek_policy.update({'local_port': int(group['local_port'])})
                continue

            m = p6.match(line) 
            if m:
                group = m.groupdict()
                remote_details = kek_policy.setdefault('remote_details', {})
                remote_details.update({'remote_addr': group['remote_addr']})
                remote_details.update({'remote_port': int(group['remote_port'])})
                continue

            m = p7.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'spi': group['spi']})
                continue

            m = p8.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'mgmt_alg_status': group['mgmt_alg_status']})
                remote_details.update({'encrypt_alg': group['encrypt_alg']})
                continue

            m = p9.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'crypto_iv_length': int(group['crypto_iv_length'])})
                remote_details.update({'key_size': int(group['key_size'])})
                continue

            m = p10.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'orig_life': int(group['orig_life'])})
                continue

            m = p11.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'sig_hash_alg_status': group['sig_hash_alg_status']})
                remote_details.update({'sig_key_length': int(group['sig_key_length'])})
                continue

            m = p12.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'sig_size': int(group['sig_size'])})
                continue

            m = p13.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'ack': group['ack']})
                continue

            m = p14.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'connection_type': group['connection_type']})
                remote_details.update({'connection_id': int(group['connection_id'])})
                continue

            m = p15.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'seq_num': int(group['seq_num'])})
                remote_details.update({'prev_seq_num': int(group['prev_seq_num'])})
                continue

            m = p16.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'handle': int(group['handle'])})
                continue

            m = p17.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'interface_type': group['interface_type']})
                continue

            m = p18.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'group_name': group['group_name']})
                continue
            
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm identifier'
# =================================================
class ShowCryptoGdoiGmIdentifierSchema(MetaParser):
    """Schema for show crypto gdoi gm identifier"""
    schema = {
        'group':{
            Any(): {
                Any(): {
                    'vrf_name': str,
                    'transform_mode': str,
                    'no_of_sid': int,
                    'current_sid': str
                    },
                },
            },
        }

# =================================================
#  Parser for 'show crypto gdoi gm identifier'
# =================================================
class ShowCryptoGdoiGmIdentifier(ShowCryptoGdoiGmIdentifierSchema):
    """Parser for show crypto gdoi gm identifier"""

    cli_command = ['show crypto gdoi gm identifier']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GM Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^GM Sender ID \(SID\) Information for Group\s*(?P<group_name>\S+):$')

        # Group Member: 44.44.44.1       vrf: None
        p2 = re.compile(r'^Group Member:\s*(?P<group_member>[\S]+)\s*vrf:\s*(?P<vrf_name>[\S]+)$')

        # Transform Mode                  : Non-Counter (Non-Suite-B)
        p3 = re.compile(r'^Transform Mode\s*:\s*(?P<transform_mode>[\w\s\(\)-]+)$')

        # of SIDs Last Requested        : 0
        p4 = re.compile(r'^# of SIDs Last Requested\s*:\s*(?P<no_of_sid>[\d]+)$')

        # CURRENT SIDs: None
        p5 = re.compile(r'^CURRENT SIDs:\s*(?P<current_sid>[\S]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # GM Sender ID (SID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                group_name = groups['group_name']
                group_name_dict = ret_dict.setdefault('group',{}).setdefault(group_name,{})
                continue

            # Group Member: 44.44.44.1       vrf: None
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict = group_name_dict.setdefault(groups['group_member'],{})
                group_member_dict.update({'vrf_name': groups['vrf_name']})
                continue
        

            # Transform Mode                  : Non-Counter (Non-Suite-B)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue

            # of SIDs Last Requested        : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_member_dict.update(group)
                continue

            # CURRENT SIDs: None
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue        
       
        return ret_dict 

# =========================================
#  Schema for 'show crypto gdoi ks detail'
# =========================================
class ShowCryptoGdoiKsDetailSchema(MetaParser):
    """schema for show crypto gdoi ks detail"""

    schema = {
        'group_members_registered': int,
        Any(): {
            'group_name': str,
            're_auth_on_new_crl': str,
            'group_identity': int,
            'group_type': str,
            'group_members': int,
            'rekey_acknowledgement_cfg': str,
            'ipsec_sa_direction': str,
            'ip_d3p_window': str,
            'split_resiliency_factor': int,
            'ckm_status': str,
            'acl_configured': {
                'access_list': str,
            },
            'redundancy': {
                'redundancy_mode': str,
                'local_address': str,
                'local_priority': int,
                'local_ks_status': str,
                'local_ks_role': str,
                'local_ks_version': str,
                'local_coop_version': str
            }
        }     
    }

# ===================================================
#  Parser for 'show crypto gdoi ks detail'
# ===================================================
class ShowCryptoGdoiKsDetail(ShowCryptoGdoiKsDetailSchema):

    """Parser for 'show crypto gdoi ks detail"""

    cli_command = 'show crypto gdoi ks detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Total group members registered to this box: 12
        p1 = re.compile(r'^Total\s+group\s+members\s+registered\s+to\s+this\s+box:+\s(?P<group_members_registered>\d+)$')
        # Key Server Information For Group bw6000:
        p2 = re.compile(r'^Key\s+Server\s+Information\s+For\s+Group\s+(?P<key_server_group>\S+):$')
        # Group Name               : bw6000
        p3 = re.compile(r'^Group\s+Name\s+:\s+(?P<group_name>\S+)$')
        # Re-auth on new CRL       : Disabled
        p4 = re.compile(r'^Re-auth\s+on\s+new\s+CRL\s+:\s+(?P<re_auth_on_new_crl>\w+)$')
        # Group Identity           : 6000
        p5 = re.compile(r'^Group\s+Identity\s+:\s+(?P<group_identity>\d+)$')
        # Group Type               : GDOI (ISAKMP)
        p6 = re.compile(r'^Group\s+Type\s+:\s+GDOI\s+\((?P<group_type>\S+)\)$')
        # Group Members            : 2
        p7 = re.compile(r'^Group\s+Members\s+:\s+(?P<group_members>\d+)$')
        # Rekey Acknowledgement Cfg: Cisco
        p8 = re.compile(r'^Rekey\s+Acknowledgement\s+Cfg:\s+(?P<rekey_acknowledgement_cfg>\w+)$')
        # IPSec SA Direction       : Both
        p9 = re.compile(r'^IPSec\s+SA\s+Direction\s+:\s+(?P<ipsec_sa_direction>\w+)$')
        # IP D3P Window            : Disabled
        p10 = re.compile(r'^IP\s+D3P\s+Window\s+:\s+(?P<ip_d3p_window>\w+)$')
        # Split Resiliency Factor  : 0
        p11 = re.compile(r'^Split\s+Resiliency\s+Factor\s+:\s+(?P<split_resiliency_factor>\d+)$')
        # CKM status               : Disabled
        p12 = re.compile(r'^CKM\s+status\s+:\s+(?P<ckm_status>\w+)$')
        # ACL Configured: 
        # access-list bw600-crypto-policy
        p13 = re.compile(r'^access-list\s+(?P<access_list>\S+)$')
        # Redundancy               : Configured
        p14 = re.compile(r'^Redundancy\s+:\s+(?P<redundancy_mode>\w+)$')
        # Local Address        : 15.15.15.1
        p15 =  re.compile(r'^Local\s+Address\s+:\s+(?P<local_address>\S+)$')
        # Local Priority       : 245
        p16 = re.compile(r'^Local\s+Priority\s+:\s+(?P<local_priority>\d+)$')
        # Local KS Status      : Alive
        p17 = re.compile(r'^Local\s+KS\s+Status\s+:\s+(?P<local_ks_status>\w+)$')
        # Local KS Role        : Primary
        p18 = re.compile(r'^Local\s+KS\s+Role\s+:\s+(?P<local_ks_role>\w+)$')
        # Local KS Version     : 1.0.27
        p19 = re.compile(r'^Local\s+KS\s+Version\s+:\s+(?P<local_ks_version>\S+)$')
        # Local COOP Version   : 1.0.8 
        p20 = re.compile(r'^Local\s+COOP\s+Version\s+:\s+(?P<local_coop_version>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Total group members registered to this box: 12
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'group_members_registered': int(group['group_members_registered'])})
                continue

            # Key Server Information For Group bw6000:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_name = group['key_server_group']
                server_dict = ret_dict.setdefault(group_name, {})
                continue

            # Group Name               : bw6000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_name': group['group_name']})
                continue

            # Re-auth on new CRL       : Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'re_auth_on_new_crl': group['re_auth_on_new_crl']})
                continue
             
            # Group Identity           : 6000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_identity': int(group['group_identity'])})
                continue

            # Group Type               : GDOI (ISAKMP)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_type': group['group_type']})
                continue

            # Group Members            : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_members': int(group['group_members'])})
                continue

            # Rekey Acknowledgement Cfg: Cisco
            m = p8.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'rekey_acknowledgement_cfg': group['rekey_acknowledgement_cfg']})
                continue

            # IPSec SA Direction       : Both
            m = p9.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ipsec_sa_direction': group['ipsec_sa_direction']})
                continue

            # IP D3P Window            : Disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ip_d3p_window': group['ip_d3p_window']})
                continue

            # Split Resiliency Factor  : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'split_resiliency_factor': int(group['split_resiliency_factor'])})
                continue

            # CKM status               : Disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ckm_status': group['ckm_status']})
                continue

            # access-list bw600-crypto-policy
            m = p13.match(line)
            if m:
                group = m.groupdict()
                access_list_dict = server_dict.setdefault('acl_configured', {})
                access_list_dict.update({'access_list': group['access_list']})
                continue

            # Redundancy               : Configured
            m = p14.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict = server_dict.setdefault('redundancy', {})
                redundancy_dict.update({'redundancy_mode': group['redundancy_mode']})
                continue

            # Local Address        : 15.15.15.1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_address': group['local_address']})
                continue

            # Local Priority       : 245
            m = p16.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_priority': int(group['local_priority'])})
                continue

            # Local KS Status      : Alive
            m = p17.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_status': group['local_ks_status']})
                continue

            # Local KS Role        : Primary
            m = p18.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_role': group['local_ks_role']})
                continue

            # Local KS Version     : 1.0.27
            m = p19.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_version': group['local_ks_version']})
                continue

            # Local COOP Version   : 1.0.8
            m = p20.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_coop_version': group['local_coop_version']})
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm pubkey'
# =================================================
class ShowCryptoGdoiGmPubkeySchema(MetaParser):
    """Schema for show crypto gdoi gm pubkey"""
    schema = {
        'gdoi_group': {
            Any(): {
                Optional(Any()): {
                    Optional('ks_ipaddress'): str,
                    Optional('conn_id'): int,
                    Optional('my_cookie'): str,
                    Optional('his_cookie'): str,
                    Optional('key_data'): {
                        Optional('key_data_info'): list
                        }
                    }
                }
            }
        }


# =================================================
#  Parser for 'show crypto gdoi gm pubkey'
# =================================================
class ShowCryptoGdoiGmPubkey(ShowCryptoGdoiGmPubkeySchema):
    """Parser for show crypto gdoi gm pubkey"""

    cli_command = ['show crypto gdoi gm pubkey']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GDOI Group: bw6000
        p1 = re.compile(r'^GDOI\s*Group:\s*(?P<group_name>\S+)$')

        # KS IP Address: 15.15.15.1
        p2 = re.compile(r'^KS\s*IP\s*Address:\s*(?P<ks_ipaddress>\S+)$')

        # conn-id: 44334    my-cookie:C5AC6039    his-cookie:A440633E
        p3 = re.compile(r'^conn-id:\s*(?P<conn_id>\d+)\s*my-cookie:\s*(?P<my_cookie>\S+)\s*his-cookie:\s*(?P<his_cookie>\S+)$')

        # Key Data:
        p4 = re.compile(r'^(?P<key_data_info>[0-9A-Z\s]+)$')


        for line in output.splitlines():
            line = line.strip()

            # GDOI Group: bw6000
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('gdoi_group', {}).setdefault(group_name, {})
                count = 0
                continue

            # KS IP Address: 15.15.15.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ks_dict = group_name_dict.setdefault(count, {})
                ks_dict['ks_ipaddress'] = group['ks_ipaddress']
                count +=1
                continue


            # conn-id: 44334    my-cookie:C5AC6039    his-cookie:A440633E
            m = p3.match(line)
            if m:
                ks_dict['conn_id'] = int(m.groupdict()['conn_id'])
                ks_dict['my_cookie'] = m.groupdict()['my_cookie']
                ks_dict['his_cookie'] = m.groupdict()['his_cookie']
                continue

            # Key Data:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_data_dict = ks_dict.setdefault('key_data', {})
                key_data_dict_full = key_data_dict.setdefault('key_data_info', [])
                key_data_dict_full.append(group['key_data_info'])
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm rekey detail'
# =================================================
class ShowCryptoGdoiGmRekeyDetailSchema(MetaParser):
    """Schema for show crypto gdoi gm rekey detail"""
    schema = {
        'gdoi_group':{
            Any(): {
                    'rekeys_cumulative': int,
                    'rekeys_registration': int,
                    'rekey_acks_sent': int,
                    'rekey_sa_information': {
                        Any(): {
                            'dst': str,
                            'src': str,
                            'conn_id': str,
                            'my_cookie': str,
                            'his_cookie': str                            
                        }
                    }
                }
            }
        }

# =================================================
#  Parser for 'show crypto gdoi gm rekey detail'
# =================================================
class ShowCryptoGdoiGmRekeyDetail(ShowCryptoGdoiGmRekeyDetailSchema):
    """Parser for show crypto gdoi gm rekey detail"""

    cli_command = ['show crypto gdoi gm rekey detail']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # Group bw6000 (Unicast)
        p1 = re.compile(r'^Group\s*(?P<group_name>\S+)\s*\(Unicast\)$')

        # Number of Rekeys received (cumulative)       : 0
        p2 = re.compile(r'^Number\s*of\s*Rekeys\s*received\s*\(cumulative\)\s*:\s*(?P<rekeys_cumulative>\d+)$')

        # Number of Rekeys received after registration : 0
        p3 = re.compile(r'^Number\s*of\s*Rekeys\s*received\s*after\s*registration\s*:\s*(?P<rekeys_registration>\d+)$')

        # Number of Rekey Acks sent                    : 0
        p4 = re.compile(r'^Number\s*of\s*Rekey\s*Acks\s*sent\s*:\s*(?P<rekey_acks_sent>\d+)$')
        
        # New     : 41.41.41.1      15.15.15.1       44327   14C40DC1   88AD3ACA
        p5 = re.compile(r'^(?P<state>(New|Current|Previous))\s*:\s*(?P<dst>[\S]+)\s*(?P<src>[\S]+)\s*(?P<conn_id>[\S]+)\s*(?P<my_cookie>[\S]+)\s*(?P<his_cookie>[\S]+)$')
        

        for line in output.splitlines():
            line = line.strip()

            # Group bw6000 (Unicast)
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('gdoi_group', {}).setdefault(group_name, {})
                continue

            # Number of Rekeys received (cumulative)       : 0
            m = p2.match(line)
            if m:
                group_name_dict['rekeys_cumulative'] = int(m.groupdict()['rekeys_cumulative'])
                continue
        
            # Number of Rekeys received after registration : 0
            m = p3.match(line)
            if m:
                group_name_dict['rekeys_registration'] = int(m.groupdict()['rekeys_registration'])                       
                continue
        
            # Number of Rekey Acks sent                    : 0
            m = p4.match(line)
            if m:
                group_name_dict['rekey_acks_sent'] = int(m.groupdict()['rekey_acks_sent'])  
                continue

            # Rekey (KEK) SA information :
            m = p5.match(line)
            if m:
                state = m.groupdict()['state']             
                rekey_data_dict = group_name_dict.setdefault('rekey_sa_information', {}).setdefault(state, {})
                rekey_data_dict['dst'] = m.groupdict()['dst']
                rekey_data_dict['src'] = m.groupdict()['src']
                rekey_data_dict['conn_id'] = m.groupdict()['conn_id']
                rekey_data_dict['my_cookie'] = m.groupdict()['my_cookie']
                rekey_data_dict['his_cookie'] = m.groupdict()['his_cookie']                                              
                continue

        
        return ret_dict        

# =================================================
#  Schema for 'show crypto gdoi ks coop detail'
# =================================================
class ShowCryptoGdoiKsCoopDetailSchema(MetaParser):
    """schema for show crypto gdoi ks coop detail"""
    schema = {
        'crypto_gdoi_group_name': {
            Any(): {
                'group_handle': int,
                'local_key_server_handle': int,
                Optional('redundancy_state'): str,
                Optional('local_address'): str,
                Optional('local_priority'): int,
                Optional('local_ks_role'): str,
                Optional('local_ks_status'): str,
                Optional('local_ks_version'): str,
                Optional('local_coop_version'): str,
                Optional('primary_timers'): {
                    Optional('primary_refresh_policy_time'): int,
                    Optional('remaining_time'): int,
                    Optional('per_user_timer_remaining_time'): int,
                    Optional('antireplay_sequence_number'): int,
                },
                Optional('secondary_timers'): {
                    Optional('sec_primary_periodic_time'): int,
                    Optional('remaining_time'): int,
                    Optional('retries'): int,
                    Optional('invalid_ann_pst_recvd'): int,
                    Optional('new_gm_temp_blk_enforced'): str,
                    Optional('per_user_timer_remaining_time'): int,
                    Optional('antireplay_sequence_number'): int,
                },
                Optional(Any()): {
                    Optional('server_handle'): int,
                    Optional('peer_address'): str,
                    Optional('peer_version'): str,
                    Optional('peer_coop_version'): str,
                    Optional('coop_protocol'): str,
                    Optional('peer_priority'): int,
                    Optional('peer_ks_role'): str,
                    Optional('peer_ks_status'): str,
                    Optional('antireplay_sequence_number'): int,
                    Optional('ike_status'): str,
                    Optional('counters'): {
                        Optional('ann_msgs_sent'): int,
                        Optional('ann_msgs_sent_with_reply_request'): int,
                        Optional('ann_msgs_recv'): int,
                        Optional('ann_msgs_recv_with_reply_request'): int,
                        Optional('packet_sent_drops'): int,
                        Optional('packet_recv_drops'): int,
                        Optional('total_bytes_sent'): int,
                        Optional('total_bytes_recv'): int
                    }
                }
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks coop detail'
# ===================================================
class ShowCryptoGdoiKsCoopDetail(ShowCryptoGdoiKsCoopDetailSchema):
    """Parser for show crypto gdoi ks coop detail"""
    cli_command = 'show crypto gdoi ks coop detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Crypto Gdoi Group Name :g1
        p1 = re.compile(r'^Crypto\s+Gdoi\s+Group\s+Name +:(?P<crypto_gdoi_group_name>\S+)$')
        # Group handle: 1073741826, Local Key Server handle: 1073741826
        p2 = re.compile(r'^Group\s+handle:\s+(?P<group_handle>\d+),\s+Local\s+Key\s+Server\s+handle:\s+(?P<local_key_server_handle>\d+)$')
        # *NO* redundancy configured for this group
        p3 = re.compile(r'\*(?P<redundancy_state>NO)\*\s+redundancy\s+configured\s+for\s+this\s+group')
        # Local Address: 10.78.106.116
        p4 = re.compile(r'^Local\s+Address:\s+(?P<local_address>\S+)$')
        # Local Priority: 100
        p5 = re.compile(r'^Local\s+Priority:\s+(?P<local_priority>\d+)$')
        # Local KS Role: Primary , Local KS Status: Alive
        p6 = re.compile(r'^Local\s+KS\s+Role:\s+(?P<local_ks_role>\w+)\s+,\s+Local\s+KS\s+Status:\s+(?P<local_ks_status>\w+)$')
        # Local KS version: 1.0.27
        p7 = re.compile(r'^Local\s+KS\s+version:\s+(?P<local_ks_version>\S+)$')
        # Local COOP version: 1.0.8
        p8 = re.compile(r'^Local\s+COOP\s+version:\s+(?P<local_coop_version>\S+)$')
        # Primary Refresh Policy Time: 20
        p9 = re.compile(r'^Primary\s+Refresh\s+Policy\s+Time:\s+(?P<primary_refresh_policy_time>\d+)$')
        # Remaining Time: 14
        p10 = re.compile(r'^Remaining\s+Time:\s+(?P<remaining_time>\d+)$')
        # Per-user timer remaining time: 0
        p11 = re.compile(r'^Per-user\s+timer\s+remaining\s+time:\s+(?P<per_user_timer_remaining_time>\d+)$')
        # Antireplay Sequence Number: 79
        p12 = re.compile(r'^Antireplay\s+Sequence\s+Number:\s+(?P<antireplay_sequence_number>\d+)$')
        # Session 1:
        p13 = re.compile(r'^Session\s+(?P<session_id>\d+):$')
        # Server handle: 1073741827
        p14 = re.compile(r'^Server\s+handle:\s+(?P<server_handle>\d+)$')
        # Peer Address: 10.78.106.117
        p15 = re.compile(r'^Peer\s+Address:\s+(?P<peer_address>\S+)$')
        # Peer Version: 1.0.27
        p16 = re.compile(r'^Peer\s+Version:\s+(?P<peer_version>\S+)$')
        # Peer COOP version: 1.0.8
        p17 = re.compile(r'^Peer\s+COOP\s+version:\s+(?P<peer_coop_version>\S+)$')
        # COOP Protocol: base
        p18 = re.compile(r'^COOP\s+Protocol:\s+(?P<coop_protocol>\S+)$')
        # Peer Priority: 90
        p19 = re.compile(r'^Peer\s+Priority:\s+(?P<peer_priority>\d+)$')
        # Peer KS Role: Secondary , Peer KS Status: Alive
        p20 = re.compile(r'^Peer\s+KS\s+Role:\s+(?P<peer_ks_role>\w+)\s+,\s+Peer\s+KS\s+Status:\s+(?P<peer_ks_status>\w+)$')
        # IKE status: Established
        p21 = re.compile(r'^IKE\s+status:\s+(?P<ike_status>\w+)$')
        # Ann msgs sent: 122
        p22 = re.compile(r'^Ann\s+msgs\s+sent:\s+(?P<ann_msgs_sent>\d+)$')
        # Ann msgs sent with reply request: 1
        p23 = re.compile(r'^Ann\s+msgs\s+sent\s+with\s+reply\s+request:\s+(?P<ann_msgs_sent_with_reply_request>\d+)$')
        # Ann msgs recv: 4
        p24 =  re.compile(r'^Ann\s+msgs\s+recv:\s+(?P<ann_msgs_recv>\d+)$')
        # Ann msgs recv with reply request: 1
        p25 = re.compile(r'^Ann\s+msgs\s+recv\s+with\s+reply\s+request:\s+(?P<ann_msgs_recv_with_reply_request>\d+)$')
        # Packet sent drops: 1
        p26 = re.compile(r'^Packet\s+sent\s+drops:\s+(?P<packet_sent_drops>\d+)$')
        # Packet Recv drops: 0
        p27 = re.compile(r'^Packet\s+Recv\s+drops:\s+(?P<packet_recv_drops>\d)$')
        # Total bytes sent: 104495
        p28 = re.compile(r'^Total\s+bytes\s+sent:\s+(?P<total_bytes_sent>\d+)$')
        # Total bytes recv: 2130
        p29 = re.compile(r'^Total\s+bytes\s+recv:\s+(?P<total_bytes_recv>\d+)$')
        # Sec Primary Periodic Time: 30
        p30 = re.compile(r'^Sec Primary.*: +(?P<sec_primary_periodic_time>\d+)$')
        # Remaining Time: 11, Retries: 0
        p31 = re.compile(r'^Remaining Time: +(?P<remaining_time>\d+), +Retries: +(?P<retries>\d+)$')
        # Invalid ANN PST recvd: 0
        p32 = re.compile(r'^Invalid.*: +(?P<invalid_ann_pst_recvd>\d+)$')
        # New GM Temporary Blocking Enforced?: No
        p33 = re.compile(r'^New.*?: +(?P<new_gm_temp_blk_enforced>\w+)$')

        ret_dict = {}
        reply_num = 0
        for line in output.splitlines():
            line = line.strip()
            # Crypto Gdoi Group Name :g1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group_id = group['crypto_gdoi_group_name']
                crypto_gdoi_group = ret_dict.setdefault('crypto_gdoi_group_name', {}).setdefault(crypto_gdoi_group_id, {})
                reply_num = 0
                continue

            # Group handle: 1073741826, Local Key Server handle: 1073741826
            m = p2.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'group_handle': int(group['group_handle'])})
                crypto_gdoi_group.update({'local_key_server_handle': int(group['local_key_server_handle'])})
                continue

            # *NO* redundancy configured for this group
            m = p3.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'redundancy_state': group['redundancy_state']})
                continue

            # Local Address: 10.78.106.116
            m = p4.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_address': group['local_address']})
                continue

            # Local Priority: 100
            m = p5.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_priority': int(group['local_priority'])})
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p6.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_ks_role': group['local_ks_role']})
                crypto_gdoi_group.update({'local_ks_status': group['local_ks_status']})
                continue

            # Local KS version: 1.0.27
            m = p7.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_ks_version': group['local_ks_version']})
                continue

            # Local COOP version: 1.0.8
            m = p8.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_coop_version': group['local_coop_version']})
                continue

            # Primary Refresh Policy Time: 20
            m = p9.match(line)
            if m:
                group = m.groupdict()
                primary_timer_dict = crypto_gdoi_group.setdefault('primary_timers', {})
                primary_timer_dict.update({'primary_refresh_policy_time': int(group['primary_refresh_policy_time'])})
                continue

            # Sec Primary Periodic Time: 30
            m = p30.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict = crypto_gdoi_group.setdefault('secondary_timers', {})
                secondary_timer_dict.update({'sec_primary_periodic_time': int(group['sec_primary_periodic_time'])})
                continue

            # Remaining Time: 11, Retries: 0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                secondary_timer_dict.update(group)
                continue

            # Invalid ANN PST recvd: 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict.update({'invalid_ann_pst_recvd': int(group['invalid_ann_pst_recvd'])})
                continue

            # New GM Temporary Blocking Enforced?: No
            m = p33.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict.update(group)
                continue

            # Remaining Time: 14
            m = p10.match(line)
            if m:
                group = m.groupdict()
                primary_timer_dict.update({'remaining_time': int(group['remaining_time'])})
                continue

            # Per-user timer remaining time: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if 'primary_timers' in crypto_gdoi_group:
                    primary_timer_dict.update({'per_user_timer_remaining_time': int(group['per_user_timer_remaining_time'])})
                elif 'secondary_timers' in crypto_gdoi_group:
                    secondary_timer_dict.update({'per_user_timer_remaining_time': int(group['per_user_timer_remaining_time'])})
                continue

            # Antireplay Sequence Number: 124
            m = p12.match(line)
            if (reply_num == 0):
                if m:
                    group = m.groupdict()
                    if 'primary_timers' in crypto_gdoi_group:
                        primary_timer_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    elif 'secondary_timers' in crypto_gdoi_group:
                        secondary_timer_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    reply_num += 1
                    continue

            # Session 1:
            m = p13.match(line)
            if m:
                group = m.groupdict()
                session_id = group['session_id']
                session_dict = ret_dict.setdefault('crypto_gdoi_group_name', {}).setdefault(crypto_gdoi_group_id,\
                        {}).setdefault(session_id, {})
                continue

            # Server handle: 1073741827
            m = p14.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'server_handle': int(group['server_handle'])})
                continue

            # Peer Address: 10.78.106.117
            m = p15.match(line)
            if m:
                group =m.groupdict()
                session_dict.update({'peer_address': group['peer_address']})
                continue

            # Peer Version: 1.0.27
            m = p16.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_version': group['peer_version']})
                continue

            # Peer COOP version: 1.0.8
            m = p17.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_coop_version': group['peer_coop_version']})
                continue

            # COOP Protocol: base
            m = p18.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'coop_protocol': group['coop_protocol']})
                continue

            # Peer Priority: 90
            m = p19.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_priority': int(group['peer_priority'])})
                continue

            # Peer KS Role: Secondary , Peer KS Status: Alive
            m = p20.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_ks_role': group['peer_ks_role']})
                session_dict.update({'peer_ks_status': group['peer_ks_status']})
                continue

            # Antireplay Sequence Number: 5
            m = p12.match(line)
            if (reply_num == 1):
                if m:
                    group = m.groupdict()
                    session_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    continue

            # IKE status: Established
            m = p21.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'ike_status': group['ike_status']})
                continue

            # Ann msgs sent: 122
            m = p22.match(line)
            if m:
                group = m.groupdict()
                counter_dict = session_dict.setdefault('counters', {})
                counter_dict.update({'ann_msgs_sent': int(group['ann_msgs_sent'])})
                continue

            # Ann msgs sent with reply request: 1
            m = p23.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_sent_with_reply_request': int(group['ann_msgs_sent_with_reply_request'])})
                continue

            # Ann msgs recv: 4
            m = p24.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_recv': int(group['ann_msgs_recv'])})
                continue

            #Ann msgs recv with reply request: 1
            m = p25.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_recv_with_reply_request': int(group['ann_msgs_recv_with_reply_request'])})
                continue

            # Packet sent drops: 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'packet_sent_drops': int(group['packet_sent_drops'])})
                continue

            # Packet Recv drops: 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'packet_recv_drops': int(group['packet_recv_drops'])})
                continue

            # Total bytes sent: 104495
            m = p28.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'total_bytes_sent': int(group['total_bytes_sent'])})
                continue

            # Total bytes recv: 2130
            m = p29.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'total_bytes_recv': int(group['total_bytes_recv'])})

        return ret_dict

# ======================================================================================
#  Schema for 'show crypto gdoi ks identifier' and 'show crypto gdoi ks identifier detail'
# ======================================================================================
class ShowCryptoGdoiKsIdentifierSchema(MetaParser):
    """schema for:
        show crypto gdoi ks identifier
        show crypto gdoi ks identifier detail
    """

    schema = {
        'ks_sender_info': {
            Any(): {
                'transform_mode': str,
                're_initializing': str,
                'sid_length': int,
                'current_kssid_in_use': str,
                'last_gmsid_used': str,
                Optional('kssid_assigned'): str,
                Optional('kssid_used'): str,
                Optional('kssid_used_old'): str,
                Optional('available_kssid'): str,
                Optional('remining_sid'): str
            }
        }
    }

# ======================================================================================
#  Parser for 'show crypto gdoi ks identifier' and 'show crypto gdoi ks identifier detail'
# ======================================================================================
class ShowCryptoGdoiKsIdentifierSuperParser(ShowCryptoGdoiKsIdentifierSchema):
    ''' Parser for:
        show crypto gdoi ks identifier
        show crypto gdoi ks identifier detail
    '''

    def cli(self, output = None):

        res_dict = {}

        # KS Sender ID (KSSID) Information for Group bw6000:
        p1 = re.compile(r'^KS\s+Sender\s+ID\s+\(KSSID\)\s+Information\s+for\s+Group\s+(?P<ks_sender_id>\S+):$')
        # Transform Mode           : Non-Counter (Non-Suite-B)
        p2 = re.compile(r'^Transform\s+Mode\s+:\s+(?P<transform_mode>\S+)\s+\(\S+\)$')
        # Re-initializing          : No
        p3 = re.compile(r'^Re-initializing\s+:\s+(?P<re_initializing>\w+)$')
        # SID Length (Group Size)  : 24 bits (MEDIUM)
        p4 = re.compile(r'^SID\s+Length\s+\(Group\s+Size\)\s+:\s+(?P<sid_length>\d+)\s+bits\s+\(\S+\)$')
        # Current KSSID In-Use     : none
        p5 = re.compile(r'^Current KSSID\s+In-Use\s+:\s+(?P<current_kssid_in_use>\S+)$')
        # Last GMSID Used          : none
        p6 = re.compile(r'^Last\s+GMSID\s+Used\s+:\s+(?P<last_gmsid_used>\S+)$')
        # KSSID(s) Assigned        : none
        p7 = re.compile(r'^KSSID\(s\)\s+Assigned\s+:\s+(?P<kssid_assigned>\S+)$')
        # KSSID(s) Used            : none
        p8 = re.compile(r'^KSSID\(s\)\s+Used\s+:\s+(?P<kssid_used>\S+)$')
        # KSSID(s) Used (Old)      : none
        p9 = re.compile(r'^KSSID\(s\)\s+Used\s+\(Old\)\s+:\s+(?P<kssid_used_old>\S+)$')
        # Available KSSID(s)       : none
        p10 = re.compile(r'^Available\s+KSSID\(s\)\s+:\s+(?P<available_kssid>\S+)$')
        # REMAINING SIDs: none
        p11 = re.compile(r'^REMAINING\s+SIDs:\s+(?P<remining_sid>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # KS Sender ID (KSSID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ks_sender_id = group['ks_sender_id']
                ks_dict = res_dict.setdefault('ks_sender_info', {}).setdefault(ks_sender_id, {})
                continue

            # Transform Mode           : Non-Counter (Non-Suite-B)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'transform_mode': group['transform_mode']})
                continue

            # Re-initializing          : No
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'re_initializing': group['re_initializing']})
                continue

            # SID Length (Group Size)  : 24 bits (MEDIUM)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'sid_length': int(group['sid_length'])})
                continue

            # Current KSSID In-Use     : none
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'current_kssid_in_use': group['current_kssid_in_use']})
                continue

            # Last GMSID Used          : none
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'last_gmsid_used': group['last_gmsid_used']})
                continue

            # KSSID(s) Assigned        : none
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_assigned': group['kssid_assigned']})
                continue

            # KSSID(s) Used            : none
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_used': group['kssid_used']})
                continue

            # KSSID(s) Used (Old)      : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_used_old': group['kssid_used_old']})
                continue

            # Available KSSID(s)       : none
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'available_kssid': group['available_kssid']})
                continue

            # REMAINING SIDs: none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'remining_sid': group['remining_sid']})
                continue

        return res_dict


class ShowCryptoGdoiKsIdentifier(ShowCryptoGdoiKsIdentifierSuperParser):
    ''' Parser for:
        show crypto gdoi ks identifier
    '''
    cli_command = 'show crypto gdoi ks identifier'

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowCryptoGdoiKsIdentifierDetail(ShowCryptoGdoiKsIdentifierSuperParser):
    ''' Parser for:
        show crypto gdoi ks identifier detail
    '''
    cli_command = 'show crypto gdoi ks identifier detail'

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# ===================================================
#  Schema for 'show crypto gdoi gm identifier detail'
# ===================================================

class ShowCryptoGdoiGmIdentifierDetailSchema(MetaParser):
    """Schema for show crypto gdoi gm identifier detail"""

    schema = {
        'group': {
            Any(): {
                Any(): {
                    'vrf_name': str,
                    'transform_mode': str,
                    'transform_name': str,
                    'no_of_sid': int,
                    'current_sid': str,
                    'next_sid_request': {
                        'tek_lifetime_sec': int,
                        'sid_length': int,
                        'sid_group_size': str
                    }
                }   
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi gm identifier detail'
# ===================================================

class ShowCryptoGdoiGmIdentifierDetail(ShowCryptoGdoiGmIdentifierDetailSchema):
    """Parser for show crypto gdoi gm identifier detail"""

    cli_command = ['show crypto gdoi gm identifier detail'] 

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GM Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^GM Sender ID \(SID\) Information for Group\s*(?P<group_name>\S+):$')

        # Group Member: 44.44.44.1       vrf: None
        p2 = re.compile(r'^Group Member:\s*(?P<group_member>[\S]+)\s*vrf:\s*(?P<vrf_name>[\S]+)$')

        # Transform Mode                  : Non-Counter (Non-Suite-B)
        p3 = re.compile(r'^Transform Mode\s*:\s*(?P<transform_mode>[\w-]*)\s*\((?P<transform_name>[\w-]*)\)$')

        # of SIDs Last Requested        : 0
        p4 = re.compile(r'^# of SIDs Last Requested\s*:\s*(?P<no_of_sid>[\d]+)$')

        # CURRENT SIDs: None
        p5 = re.compile(r'^CURRENT SIDs:\s*(?P<current_sid>[\S]+)$')

        # TEK Lifetime                  : 4873 sec
        p6 = re.compile(r'^TEK Lifetime\s*:\s*(?P<tek_lifetime>[\w]+)\s*sec$')

        # SID Length (Group Size)       : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\)\s*:\s*(?P<sid_length>[\d]+)\s*bits\s*\((?P<group_size>[\w]+)\)$')        

        for line in output.splitlines():
            line = line.strip()

            # GM Sender ID (SID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('group',{}).setdefault(group_name,{})
                continue

            # Group Member: 44.44.44.1       vrf: None
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict = group_name_dict.setdefault(groups['group_member'],{})
                group_member_dict.update({'vrf_name': groups['vrf_name']})
                continue
        

            # Transform Mode                  : Non-Counter (Non-Suite-B)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue

            # of SIDs Last Requested        : 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                groups = {k: int(v) for k, v in groups.items()}
                group_member_dict.update(groups)
                continue

            # CURRENT SIDs: None
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue        
        
            # TEK Lifetime                  : 4873 sec
            m = p6.match(line)
            if m:
                next_sid_request_dict = group_member_dict.setdefault('next_sid_request', {})
                next_sid_request_dict['tek_lifetime_sec'] = int(m.groupdict()['tek_lifetime'])
                continue                
 
            # SID Length (Group Size)       : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                next_sid_request_dict['sid_length'] = int(m.groupdict()['sid_length'])
                next_sid_request_dict['sid_group_size'] = m.groupdict()['group_size']
                continue                
     
        return ret_dict


# ==============================
# Schema for
#   'show crypto gdoi ks coop identifier detail'
# ==============================

class ShowCryptoGdoiKsCoopIdentifierDetailSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks coop identifier detail'
    """
    schema = {
        'group': {
            Any():{
                Or('local', 'peer'): {
                    'ks_role': str,
                    'ks_status': str,
                    'address': str,
                    'next_sid_client_operation': str,
                    're_initializing': str,
                    'kssid_overlap': str,
                    'sid_length_cfg': str,
                    'sid_length_used': str,
                    'current_kssid_inuse': str,
                    'kssids_assigned': str,
                    'kssids_used': str,
                    'old_kssids_used': str
                }
            }
        }
    }

# ========================================================
#  Parser for 'show crypto gdoi ks coop identifier detail'
# ========================================================

class ShowCryptoGdoiKsCoopIdentifierDetail(ShowCryptoGdoiKsCoopIdentifierDetailSchema):
    
    """Parser for 'show crypto gdoi ks coop identifier detail'"""
    
    cli_command = 'show crypto gdoi ks coop identifier detail'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # COOP-KS Sender ID (SID) Information for Group g1:
        p1 = re.compile(r'^COOP-KS Sender ID \(SID\) Information for Group (?P<group>[\w\d\-]+):$')

        # Local KS Role: Primary , Local KS Status: Alive
        p2 = re.compile(r'^Local KS Role:\s+(?P<ks_role>[\w]+)\s+\,\s+Local KS Status:\s+(?P<ks_status>[\w]+)$')

        # Local Address : 10.78.106.116
        p3 = re.compile(r'^Local Address\s+:\s+(?P<address>\d+\.\d+\.\d+\.\d+)$')

        # Next SID Client Operation : NOTIFY
        p4 = re.compile(r'^Next SID Client Operation\s+:\s+(?P<next_sid_client_operation>[A-Z]+)$')

        # Re-initializing : No
        p5 = re.compile(r'^Re-initializing\s+:\s+(?P<re_initializing>[\w]+)$')

        # KSSID Overlap : No
        p6 = re.compile(r'^KSSID Overlap\s+:\s+(?P<kssid_overlap>[\w]+)$')

        # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\) Cfg\s+:\s+(?P<sid_length_cfg>[\s\w\(\)]+)$')

        # SID Length (Group Size) Used : 24 bits (MEDIUM)
        p8 = re.compile(r'^SID Length \(Group Size\) Used\s+:\s+(?P<sid_length_used>[\s\w\(\)]+)$')

        # Current KSSID In-Use : none
        p9 = re.compile(r'^Current KSSID In-Use\s+:\s+(?P<current_kssid_inuse>[a-z]+)$')

        # KSSID(s) Assigned : none
        p10 = re.compile('^KSSID\(s\) Assigned\s+:\s+(?P<kssids_assigned>[a-z]+)$')

        # KSSID(s) Used : none
        p11 = re.compile('^KSSID\(s\) Used\s+:\s+(?P<kssids_used>[a-z]+)$')

        # Old KSSID(s) Used : none
        p12 = re.compile('^Old KSSID\(s\) Used\s+:\s+(?P<old_kssids_used>[a-z]+)$')

        # Peer KS Role: Secondary , Peer KS Status: Alive
        p13 = re.compile('^Peer KS Role:\s+(?P<ks_role>[\w]+)\s\, Peer KS Status:\s+(?P<ks_status>[\w]+)$')

        # Peer Address : 10.78.106.117
        p14 = re.compile('^Peer Address\s+:\s+(?P<address>\d+\.\d+\.\d+\.\d+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            # GCOOP-KS Sender ID (SID) Information for Group g1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                local_dict = group_dict.setdefault('local', {})
                target_dict = local_dict
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p2.match(line)
            if m:
                group = m.groupdict()                    
                target_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Local Address : 10.78.106.116
            m = p3.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'address': group['address']})
                continue

            # Next SID Client Operation : NOTIFY
            m = p4.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'next_sid_client_operation': group['next_sid_client_operation']})
                continue

            # Re-initializing : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'re_initializing': group['re_initializing']})
                continue

            # KSSID Overlap : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'kssid_overlap': group['kssid_overlap']})
                continue

            # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'sid_length_cfg': group['sid_length_cfg']})
                continue

            # SID Length (Group Size) Used : 24 bits (MEDIUM)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'sid_length_used': group['sid_length_used']})
                continue

            # Current KSSID In-Use : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'current_kssid_inuse': group['current_kssid_inuse']})
                continue
            # KSSID(s) Assigned : none
            m = p10.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'kssids_assigned': group['kssids_assigned']})
                continue

            # KSSID(s) Used : none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'kssids_used': group['kssids_used']})
                continue

            # Old KSSID(s) Used : none
            m = p12.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'old_kssids_used': group['old_kssids_used']})
                continue

            # Peer KS Role: Secondary , Peer KS Status: Alive
            m = p13.match(line)
            if m:
                group = m.groupdict(line)
                target_dict = group_dict.setdefault('peer', {})
                target_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Peer Address : 10.78.106.117
            m = p14.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'address': group['address']})
                continue
 
        return master_dict

# ==================================
# Schema for
#   'show crypto gdoi feature set'
# ==================================
class ShowCryptoGdoiFeatureSetSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi feature'
    """

    schema = {
        'group': {
            Any():{
                'key_server':{
                    Any():{
                        'key_server_id': str,
                        'key_version': str,
                        'key_feature_supported': str
                    },
                },
                'group_member':{
                    Any():{
                        'group_member_id': str,
                        'group_member_version': str,
                        'group_feature_supported': str
                    },                   
                },
            },
        },
    }


# =================================================
#  Parser for 'show crypto gdoi feature set'
# =================================================

class ShowCryptoGdoiFeatureSet(ShowCryptoGdoiFeatureSetSchema):
    
    """Parser for 'show crypto gdoi feature' """
    
    cli_command = 'show crypto gdoi feature'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Group Name: bw6000
        p1 = re.compile(r'^Group Name:\s(?P<group>[\S]+)$')

        #     Key Server ID       Version   Feature Supported
        p2 = re.compile(r'Key Server ID \s+Version\s+Feature\sSupported')

        #         15.15.15.1          1.0.27         Yes
        p3 = re.compile(r'(?P<key_server_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<key_version>[\d\.]+)\s+(?P<key_feature_supported>[\w]+)$')

        #    Group Member ID     Version   Feature Supported
        p4 = re.compile(r'Group Member ID\s+Version\s+Feature\sSupported')

        #         25.25.25.1          1.0.25         Yes
        p5 = re.compile(r'(?P<group_member_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<group_member_version>[\d\.]+)\s+(?P<group_feature_supported>[\w]+)$')

        master_dict = {}
        server_flag = False
        member_flag = False
        for line in output.splitlines():

            line = line.strip()
            
            # Group Name: bw6000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                continue
                
            #     Key Server ID       Version   Feature Supported
            m = p2.match(line)
            if m:
                group = m.groupdict()
                server_dict = group_dict.setdefault('key_server', {})
                server_flag = True
                continue

            #         1.1.1.1          1.0.27         Yes
            if server_flag:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ser_count_dict = server_dict.setdefault(len(server_dict)+1, {})
                    ser_count_dict.update({'key_server_id': group['key_server_id']})
                    ser_count_dict.update({'key_version': group['key_version']})
                    ser_count_dict.update({'key_feature_supported': group['key_feature_supported']})                    
                    continue

            #    Group Member ID     Version   Feature Supported
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member_dict = group_dict.setdefault('group_member', {})
                server_flag = False
                member_flag = True
                continue

            #        3.3.1.1          1.0.26         Yes
            if member_flag:
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    count_dict = group_member_dict.setdefault(len(group_member_dict)+1, {})
                    count_dict.update({'group_member_id' : group['group_member_id']})
                    count_dict.update({'group_member_version': group['group_member_version']})
                    count_dict.update({'group_feature_supported': group['group_feature_supported']})
                    continue
                       
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi feature crl-check'
# =================================================
class ShowCryptoGdoiFeatureCrlCheck(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature crl-check'
    '''

    cli_command = "show crypto gdoi feature crl-check"

# =================================================
#  Parser for 'show crypto gdoi feature cts-sgt'
# =================================================
class ShowCryptoGdoiFeatureCtsSgt(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature cts-sgt'
    '''

    cli_command = "show crypto gdoi feature cts-sgt"

# =================================================
#  Parser for 'show crypto gdoi feature gikev2'
# =================================================
class ShowCryptoGdoiFeatureGikev2(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature gikev2'
    '''

    cli_command = "show crypto gdoi feature gikev2"

# ========================================
# Schema for
#   'show crypto gdoi ks coop identifier'
# ========================================

class ShowCryptoGdoiKsCoopIdentifierSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks coop identifier'
    """
    schema = {
        'group': {
            Any():{
                'local': {
                    'ks_role': str,
                    'ks_status': str,
                    'address': str,
                    'next_sid_client_operation': str,
                    're_initializing': str,
                    'kssid_overlap': str,
                    'sid_length_cfg': str,
                    'sid_length_used': str,
                    'current_kssid_inuse': str,
                    'kssids_assigned': str,
                    'kssids_used': str,
                    'old_kssids_used': str
                }
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks coop identifier'
# ===================================================

class ShowCryptoGdoiKsCoopIdentifier(ShowCryptoGdoiKsCoopIdentifierSchema):
    
    """Parser for show crypto gdoi ks coop identifier """
    
    cli_command = 'show crypto gdoi ks coop identifier'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # COOP-KS Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^COOP-KS Sender ID \(SID\) Information for Group (?P<group>[\w\d\-]+):$')

        # Local KS Role: Primary   , Local KS Status: Alive
        p2 = re.compile(r'^Local KS Role: (?P<ks_role>[\w]+)\s*\, Local KS Status: (?P<ks_status>[\w]+)$')

        # Local Address                : 15.15.15.1
        p3 = re.compile(r'^Local Address\s*: (?P<address>\d+\.\d+\.\d+\.\d+)$')

        # Next SID Client Operation    : NOTIFY
        p4 = re.compile(r'^Next SID Client Operation\s*: (?P<next_sid_client_operation>[A-Z]+)$')

        # Re-initializing              : No
        p5 = re.compile(r'^Re-initializing\s*: (?P<re_initializing>[\w]+)$')

        # KSSID Overlap                : No
        p6 = re.compile(r'^KSSID Overlap\s*: (?P<kssid_overlap>[\w]+)$')

        # SID Length (Group Size) Cfg  : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\) Cfg\s*: (?P<sid_length_cfg>[\s\w\(\)]+)$')

        # SID Length (Group Size) Used : 24 bits (MEDIUM)
        p8 = re.compile(r'^SID Length \(Group Size\) Used\s*: (?P<sid_length_used>[\s\w\(\)]+)$')

        # Current KSSID In-Use         : none
        p9 = re.compile(r'^Current KSSID In-Use\s*: (?P<current_kssid_inuse>[a-z]+)$')

        # KSSID(s) Assigned            : none
        p10 = re.compile(r'^KSSID\(s\) Assigned\s*: (?P<kssids_assigned>[a-z]+)$')

        # KSSID(s) Used                : none
        p11 = re.compile(r'^KSSID\(s\) Used\s*: (?P<kssids_used>[a-z]+)$')

        # Old KSSID(s) Used            : none
        p12 = re.compile(r'^Old KSSID\(s\) Used\s*: (?P<old_kssids_used>[a-z]+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            # GCOOP-KS Sender ID (SID) Information for Group g1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                local_dict = group_dict.setdefault('local', {})
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p2.match(line)
            if m:
                group = m.groupdict()                    
                local_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Local Address : 10.78.106.116
            m = p3.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'address': group['address']})
                continue

            # Next SID Client Operation : NOTIFY
            m = p4.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'next_sid_client_operation': group['next_sid_client_operation']})
                continue

            # Re-initializing : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'re_initializing': group['re_initializing']})
                continue

            # KSSID Overlap : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'kssid_overlap': group['kssid_overlap']})
                continue

            # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'sid_length_cfg': group['sid_length_cfg']})
                continue

            # SID Length (Group Size) Used : 24 bits (MEDIUM)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'sid_length_used': group['sid_length_used']})
                continue

            # Current KSSID In-Use : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'current_kssid_inuse': group['current_kssid_inuse']})
                continue
                
            # KSSID(s) Assigned : none
            m = p10.match(line)
            if m:
                group = m.groupdict(line)
                local_dict.update({'kssids_assigned': group['kssids_assigned']})
                continue

            # KSSID(s) Used : none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'kssids_used': group['kssids_used']})
                continue

            # Old KSSID(s) Used : none
            m = p12.match(line)
            if m:
                group = m.groupdict(line)
                local_dict.update({'old_kssids_used': group['old_kssids_used']})
                continue
    
        return master_dict

# =================================================
#  Schema for 'show crypto gdio ipsec sa'
# =================================================
class ShowCryptogdoiIpsecSaSchema(MetaParser):
    """Schema for 'show crypto gdoi ipsec sa' """

    schema = {
        'sa_created_for_group': {
            Any():{
                'interface': {
                    Any():{
                        'protocol':{
                            Any():{
                                Any():{
                                    'local_ident': str,
                                    'local_port': int,
                                    'remote_ident': str,
                                    'remote_port': int,
                                    'direction': str,
                                    'replay':{
                                        'method': str,
                                        'window': int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =================================================
#  Parser for 'show crypto gdio ipsec sa'
# =================================================

class ShowCryptogdoiIpsecSa(ShowCryptogdoiIpsecSaSchema):

    """Parser for 'show crypto gdoi ipsec sa' """

    cli_command = 'show crypto gdoi ipsec sa'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #SA created for group getvpn1:
        p1 = re.compile(r'^SA +created +for +group (?P<sa_created_for_group>[\w\d]+):$')
        #   GigabitEthernat0/0/1:
        p2 = re.compile(r'(?P<interface>[\w\d\/]+):$')
        #protocol = ip
        p3 = re.compile(r'^protocol\s= (?P<protocol>\w{2,})$')
        #local ident  = 11.23.33.33, port = 0
        p4 = re.compile(r'^local.* +(?P<local_ident>[ANY|0-9\.\/]+), +port = (?P<port>[\d]+)$')
        #remote ident = 24.54.55.55, port = 0
        p5 = re.compile(r'^remote.* +(?P<remote_ident>[ANY|0-9\.\/]+), +port = (?P<remote_port>[\d]+)$')
        #direction: Both, replay(method/window): Counter/64
        p6 = re.compile(r'^direction: (?P<direction>[\w]+), +replay.*: +(?P<method>[\w]+)\/(?P<window>[\d]+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()

            # SA created for group getvpn1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('sa_created_for_group', {}).setdefault(group['sa_created_for_group'], {})
                continue

            # GigabitEthernat0/0/1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inter_dict = group_dict.setdefault('interface', {}).setdefault(group['interface'], {})
                protocol_dict = inter_dict.setdefault('protocol', {})
                continue

            # protocol = ip
            m = p3.match(line)
            if m:
                group = m.groupdict()
                session_dict = protocol_dict.setdefault(group['protocol'], {})
                ident_dict = session_dict.setdefault(len(session_dict)+1, {})
                continue

            # local ident  = 11.23.33.33, port = 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'local_ident': group['local_ident'], 'local_port': int(group['port'])})
                continue

            # remote ident = 24.54.55.55, port = 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'remote_ident': group['remote_ident'], 'remote_port': int(group['remote_port'])})
                continue

            # direction: Both, replay(method/window): Counter/64
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'direction': group['direction']})
                replay_dict = ident_dict.setdefault('replay',{})
                replay_dict.update({'method': group['method'], 'window': int(group['window'])})
                continue

        return master_dict

# ========================================
# Schema for
#   'show crypto gdoi ks acl'
# ========================================
class ShowCryptoGdoiKsAclSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks acl'
    """
    schema = {
        "group_name": {
            Any(): {
                Optional("configured_acl"): list,
                Optional("configured_acl_locally"): list
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks acl'
# ===================================================
class ShowCryptoGdoiKsAcl(ShowCryptoGdoiKsAclSchema):
    """Parser for show crypto gdoi ks Acl """
    
    cli_command = 'show crypto gdoi ks acl'

    def cli(self, output = None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Group Name: bw6000
        p1 = re.compile(r"^Group Name: +(?P<group_name>[\d\S]+)$")

        # Configured ACL:
        p2 = re.compile(r"^Configured ACL:$")

        # Group Name               : getvpn1
        p3 = re.compile(r"^access-list .*$")

        # ACL Configured Locally:
        p4 = re.compile(r"^ACL Configured Locally:.*$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Group Name: bw6000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group_name', {}).setdefault(group['group_name'], {})
                continue

            # Configured ACL:
            m = p2.match(line)
            if m:
                acl_list = group_dict.setdefault('configured_acl', [])
                continue
            
            # Group Name               : getvpn1
            m = p4.match(line)
            if m:
                acl_list = group_dict.setdefault('configured_acl_locally', [])
                continue
            
            # ACL Configured Locally:
            m = p3.match(line)
            if m:
                acl_list.append(line)
                continue
    
        return master_dict

# ===================================================
#  Parser for 'show crypto gdoi gm acl local'
# ===================================================
class ShowCryptoGdoiGmAclLocal(ShowCryptoGdoiKsAcl):
    ''' Parser for:
        show crypto gdoi gm acl local
    '''
    cli_command = 'show crypto gdoi gm acl local'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# ========================================
# Schema for
#   'show crypto gdoi ks members'
# ========================================
class ShowCryptoGdoiKsMembersSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks members'
    """
    schema = {
        "groups": {
            Any(): {
                "group_members": {
                    Any(): {
                        "gm_state": str,
                        "gm_version": str,
                        "group_id": int,
                        "group_name": str,
                        Optional("group_type"): str,
                        Optional("key_server_id"): str,
                        Optional("rcvd_seq_num"): {
                            Optional("seq1"): int,
                            Optional("seq2"): int,
                            Optional("seq3"): int,
                            Optional("seq4"): int,
                        },
                        "rekey_acks_missed": int,
                        "rekey_acks_rcvd": int,
                        "rekeys_retries": int,
                        "rekeys_sent": int,
                        Optional("sent_seq_num"): {
                            Optional("seq1"): int,
                            Optional("seq2"): int,
                            Optional("seq3"): int,
                            Optional("seq4"): int,
                        }
                    },
                },
                "last_rekey_duration": int,
                "rekeys_sent": int,
                "retransmits_num": int,
            },
        },
    }

# ===================================================
#  Parser for 'show crypto gdoi ks members'
# ===================================================
class ShowCryptoGdoiKsMembers(ShowCryptoGdoiKsMembersSchema):
    """Parser for show crypto gdoi ks members"""
    
    cli_command = 'show crypto gdoi ks members'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Number of rekeys sent for group bw-suiteB-v6 : 0
        p2 = re.compile(r"^Number of rekeys sent for group +(?P<group_name>[\w\d\-]+).*: +(?P<rekeys_sent>\d+)$")

        # Number of retransmits during the last rekey for group bw-suiteB-v6 : 0
        p3 = re.compile(r"^Number of retransmits.* +(?P<group_name>[\w\d\-]+).*: +(?P<retransmits_num>\d+)$")

        # Duration of the last rekey for group bw-suiteB-v6 : 1 msec
        p4 = re.compile(r"^Duration.* +(?P<group_name>[\w\d\-]+).*: +(?P<last_rekey_duration>\d+) +msec$")

        # Group Member ID    : 44.44.44.1  GM Version: 1.0.25
        p5 = re.compile(r"^Group Member ID.*: +(?P<group_member_id>[\d\.]+).* +GM Version: +(?P<gm_version>[\d\.]+)$")

        # Group ID          : 2002
        p6 = re.compile(r"^Group ID.*: +(?P<group_id>[\d\.]+)$")

        # Group Name        : bw-suiteB-v6
        p7 = re.compile(r"^Group Name.*: +(?P<group_name>[\d\S]+)$")

        # Group Type        : GDOI (ISAKMP)
        p8 = re.compile(r"^Group Type.*: +(?P<group_type>[\s\S]+)$")

        # GM State          : Registered
        p9 = re.compile(r"^GM State.*: +(?P<gm_state>[\w]+)$")

        # Key Server ID     : 16.16.16.1
        p10 = re.compile(r"^Key Server ID.*: +(?P<key_server_id>[\d\.]+)$")

        # Rekeys sent       : 0
        p11 = re.compile(r"^Rekeys sent.*: +(?P<rekeys_sent>\d+)$")

        # Rekeys retries    : 0
        p12 = re.compile(r"^Rekeys retries.*: +(?P<rekeys_retries>\d+)$")

        # Rekey Acks Rcvd   : 0
        p13 = re.compile(r"^Rekey Acks Rcvd.*: +(?P<rekey_acks_rcvd>\d+)$")

        # Rekey Acks missed : 0
        p14 = re.compile(r"^Rekey Acks missed.*: +(?P<rekey_acks_missed>\d+)$")

        # Sent seq num : 0     0     0     0
        p15 = re.compile(r"^Sent seq num.*: +(?P<seq1>\d+) +(?P<seq2>\d+) +(?P<seq3>\d+) +(?P<seq4>\d+)$")

        # Rcvd seq num : 0     0     0     0
        p16 = re.compile(r"^Rcvd seq num.*: +(?P<seq1>\d+) +(?P<seq2>\d+) +(?P<seq3>\d+) +(?P<seq4>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Number of rekeys sent for group bw-suiteB-v6 : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault("groups", {}).setdefault(group['group_name'], {})
                group_dict.update({'rekeys_sent': int(group['rekeys_sent'])})
                continue
            
            # Number of retransmits during the last rekey for group bw-suiteB-v6 : 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group_dict.update({'retransmits_num': int(group['retransmits_num'])})
                continue
            
            # Duration of the last rekey for group bw-suiteB-v6 : 1 msec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_dict.update({'last_rekey_duration': int(group['last_rekey_duration'])})
                continue
            
            # Group Member ID    : 44.44.44.1  GM Version: 1.0.25
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group_id_dict = group_dict.setdefault("group_members", {}).setdefault(group['group_member_id'], {})
                group_id_dict.update({"gm_version": group['gm_version']})
                continue

            # Group ID          : 2002
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Group Name        : bw-suiteB-v6
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Group Type        : GDOI (ISAKMP)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # GM State          : Registered
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Key Server ID     : 16.16.16.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Rekeys sent       : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekeys retries    : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekey Acks Rcvd   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekey Acks missed : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue
            
            # Sent seq num : 0     0     0     0    
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                sent_seq_dict = group_id_dict.setdefault("sent_seq_num", {})
                sent_seq_dict.update(group)
                continue

            # Rcvd seq num : 0     0     0     0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                rcvd_seq_dict = group_id_dict.setdefault("rcvd_seq_num", {})
                rcvd_seq_dict.update(group)
                continue
            
        return master_dict

# ===================================================
#  Parser for 'show crypto gdoi ks members ip {member_ip}'
# ===================================================
class ShowCryptoGdoiKsMembersIp(ShowCryptoGdoiKsMembers):
    ''' Parser for:
        show crypto gdoi ks members {member_ip}
    '''
    cli_command = 'show crypto gdoi ks members {member_ip}'

    def cli(self, member_ip='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# ========================================
# Schema for
#   'show crypto gdoi ks members summary'
# ========================================
class ShowCryptoGdoiKsMembersSummarySchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks members summary'
    """
    schema = {
        "group_member_information": {
            "groups": {
                Any(): {
                    "key_server_ids": {
                        Any(): {
                            Optional("gmdb_state"): str,
                            Optional("group_members"): int,
                            Optional("members"): {
                                Optional(Any()): {
                                    Optional("rekey_ack_missed"): int,
                                    Optional("rekey_sent"): int,
                                    Optional("version"): str,
                                }
                            },
                        },
                    },
                    "group_id": int,
                    "group_members": int,
                },
            },
        },
    }

# ========================================
#   Parser for 'show crypto gdoi ks members summary'
# ========================================
class ShowCryptoGdoiKsMembersSummary(ShowCryptoGdoiKsMembersSummarySchema):
    """Parser for show crypto gdoi ks members summary"""
    
    cli_command = 'show crypto gdoi ks members summary'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Group Member Information :
        p1 = re.compile(r"^Group Member Information.*$")

        # Group Name: bw6000_eft, ID: 1122, Group Members: 2
        p2 = re.compile(r"^Group Name: +(?P<group_name>[\S]+), +ID: +(?P<group_id>\d+), +Group Members: +(?P<group_members>\d+)$")

        # Key Server ID: 16.16.16.1, GMDB state: REDUNDANT, Group Members: 1
        p3 = re.compile(r"^Key Server ID: +(?P<key_server_id>[\d\.]+), +GMDB state: +(?P<gmdb_state>\w+), +Group Members: +(?P<group_members>\d+)$")

        # 42.42.42.1   1.0.25         0               0
        p4 = re.compile(r"^(?P<member_id>[\d\.]+) +(?P<version>[\d\.]+) +(?P<rekey_sent>\d+) +(?P<rekey_ack_missed>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Group Member Information :
            m = p1.match(line)
            if m:
                group_mem_dict = master_dict.setdefault("group_member_information", {}).setdefault("groups", {})
                continue
            
            # Group Name: bw6000_eft, ID: 1122, Group Members: 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_dict = group_mem_dict.setdefault(group['group_name'], {})
                group_dict.update({'group_id':int(group['group_id'])})
                group_dict.update({'group_members':int(group['group_members'])})
                continue
            
            # Key Server ID: 16.16.16.1, GMDB state: REDUNDANT, Group Members: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                key_server_id = group_dict.setdefault("key_server_ids", {}).setdefault(group['key_server_id'], {})
                key_server_id.update({'gmdb_state':group['gmdb_state']})
                key_server_id.update({'group_members':int(group['group_members'])})
                continue

            # 42.42.42.1   1.0.25         0               0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                memeber_dict = key_server_id.setdefault("members", {}).setdefault(group['member_id'], {})
                memeber_dict.update({'version':group['version']})
                memeber_dict.update({'rekey_sent':int(group['rekey_sent'])})
                memeber_dict.update({'rekey_ack_missed':int(group['rekey_ack_missed'])})
                continue
        return master_dict


