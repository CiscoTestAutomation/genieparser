# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_packet_testersecurity
from genie.libs.parser.bigip.get_net_packet_testersecurity import (
    NetPackettesterSecurity,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/packet-tester/security'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:packet-tester:security:securitystats",
            "selfLink": "https://localhost/mgmt/tm/net/packet-tester/security?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/packet-tester/security/0": {
                    "nestedStats": {
                        "entries": {
                            "ack": {"description": "0"},
                            "acl_device_action": {"description": "0"},
                            "acl_device_dest_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_device_dst_geo": {"description": "unset"},
                            "acl_device_irule_name": {"description": "unset"},
                            "acl_device_is_default_rule": {"description": "0"},
                            "acl_device_is_staged": {"description": "0"},
                            "acl_device_log_config": {"description": "0"},
                            "acl_device_policy_name": {"description": "unset"},
                            "acl_device_policy_type": {"description": "unset"},
                            "acl_device_rule_name": {"description": "unset"},
                            "acl_device_src_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_device_src_geo": {"description": "unset"},
                            "acl_device_subs_group_name": {
                                "description": "unset"
                            },
                            "acl_device_subs_name": {"description": "unset"},
                            "acl_device_vs_forward": {"description": "unset"},
                            "acl_listener_action": {"description": "0"},
                            "acl_listener_dest_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_listener_dst_geo": {"description": "unset"},
                            "acl_listener_irule_name": {
                                "description": "unset"
                            },
                            "acl_listener_is_default_rule": {
                                "description": "0"
                            },
                            "acl_listener_is_staged": {"description": "0"},
                            "acl_listener_log_config": {"description": "0"},
                            "acl_listener_name": {"description": "unset"},
                            "acl_listener_policy_name": {
                                "description": "unset"
                            },
                            "acl_listener_policy_type": {
                                "description": "unset"
                            },
                            "acl_listener_rule_name": {"description": "unset"},
                            "acl_listener_src_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_listener_src_geo": {"description": "unset"},
                            "acl_listener_subs_group_name": {
                                "description": "unset"
                            },
                            "acl_listener_subs_name": {"description": "unset"},
                            "acl_rtdom_action": {"description": "0"},
                            "acl_rtdom_dest_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_rtdom_dst_geo": {"description": "unset"},
                            "acl_rtdom_irule_name": {"description": "unset"},
                            "acl_rtdom_is_default_rule": {"description": "0"},
                            "acl_rtdom_is_staged": {"description": "0"},
                            "acl_rtdom_log_config": {"description": "0"},
                            "acl_rtdom_name": {"description": "unset"},
                            "acl_rtdom_policy_name": {"description": "unset"},
                            "acl_rtdom_policy_type": {"description": "unset"},
                            "acl_rtdom_rule_name": {"description": "unset"},
                            "acl_rtdom_src_fqdn_name": {
                                "description": "unset"
                            },
                            "acl_rtdom_src_geo": {"description": "unset"},
                            "acl_rtdom_subs_group_name": {
                                "description": "unset"
                            },
                            "acl_rtdom_subs_name": {"description": "unset"},
                            "acl_rtdom_vs_forward": {"description": "unset"},
                            "check_staged": {"description": "0"},
                            "dest_ip": {"description": "::"},
                            "dest_port": {"description": "0"},
                            "dos_device_action": {"description": "0"},
                            "dos_device_attack_detected": {"description": "0"},
                            "dos_device_attack_drop_flag": {
                                "description": "0"
                            },
                            "dos_device_attack_vector": {
                                "description": "unset"
                            },
                            "dos_device_log_config": {"description": "0"},
                            "dos_device_wl": {"description": "0"},
                            "dos_listener_action": {"description": "0"},
                            "dos_listener_attack_detected": {
                                "description": "0"
                            },
                            "dos_listener_attack_drop_flag": {
                                "description": "0"
                            },
                            "dos_listener_attack_vector": {
                                "description": "unset"
                            },
                            "dos_listener_dos_profile_name": {
                                "description": "unset"
                            },
                            "dos_listener_log_config": {"description": "0"},
                            "dos_listener_name": {"description": "unset"},
                            "dos_listener_wl": {"description": "0"},
                            "fin": {"description": "0"},
                            "global_default_action": {"description": "0"},
                            "ipi_device_action": {"description": "0"},
                            "ipi_device_dst_category": {
                                "description": "unset"
                            },
                            "ipi_device_dst_hit_type": {"description": "0"},
                            "ipi_device_irule_name": {"description": "unset"},
                            "ipi_device_is_drop_dst": {"description": "0"},
                            "ipi_device_is_drop_src": {"description": "0"},
                            "ipi_device_is_shun": {"description": "0"},
                            "ipi_device_is_wl_dst": {"description": "0"},
                            "ipi_device_is_wl_src": {"description": "0"},
                            "ipi_device_log_config": {"description": "0"},
                            "ipi_device_policy_name": {"description": "unset"},
                            "ipi_device_src_category": {
                                "description": "unset"
                            },
                            "ipi_device_src_hit_type": {"description": "0"},
                            "ipi_listener_action": {"description": "0"},
                            "ipi_listener_dst_category": {
                                "description": "unset"
                            },
                            "ipi_listener_dst_hit_type": {"description": "0"},
                            "ipi_listener_irule_name": {
                                "description": "unset"
                            },
                            "ipi_listener_is_drop_dst": {"description": "0"},
                            "ipi_listener_is_drop_src": {"description": "0"},
                            "ipi_listener_is_shun": {"description": "0"},
                            "ipi_listener_is_wl_dst": {"description": "0"},
                            "ipi_listener_is_wl_src": {"description": "0"},
                            "ipi_listener_log_config": {"description": "0"},
                            "ipi_listener_name": {"description": "unset"},
                            "ipi_listener_policy_name": {
                                "description": "unset"
                            },
                            "ipi_listener_src_category": {
                                "description": "unset"
                            },
                            "ipi_listener_src_hit_type": {"description": "0"},
                            "ipi_rtdom_action": {"description": "0"},
                            "ipi_rtdom_dst_category": {"description": "unset"},
                            "ipi_rtdom_dst_hit_type": {"description": "0"},
                            "ipi_rtdom_irule_name": {"description": "unset"},
                            "ipi_rtdom_is_drop_dst": {"description": "0"},
                            "ipi_rtdom_is_drop_src": {"description": "0"},
                            "ipi_rtdom_is_shun": {"description": "0"},
                            "ipi_rtdom_is_wl_dst": {"description": "0"},
                            "ipi_rtdom_is_wl_src": {"description": "0"},
                            "ipi_rtdom_log_config": {"description": "0"},
                            "ipi_rtdom_name": {"description": "unset"},
                            "ipi_rtdom_policy_name": {"description": "unset"},
                            "ipi_rtdom_src_category": {"description": "unset"},
                            "ipi_rtdom_src_hit_type": {"description": "0"},
                            "nat_dst_object_name": {"description": "unset"},
                            "nat_dst_success": {"description": "1"},
                            "nat_dst_translated_address": {
                                "description": "::"
                            },
                            "nat_dst_translated_port": {"description": "0"},
                            "nat_dst_type": {"description": "0"},
                            "nat_policy_name": {"description": "unset"},
                            "nat_rule_name": {"description": "unset"},
                            "nat_src_object_name": {"description": "unset"},
                            "nat_src_success": {"description": "1"},
                            "nat_src_translated_address": {
                                "description": "::"
                            },
                            "nat_src_translated_port": {"description": "0"},
                            "nat_src_type": {"description": "0"},
                            "packet_test_listener_name": {
                                "description": "unset"
                            },
                            "packet_test_rtdom_name": {"description": "unset"},
                            "pat_src_mode": {"description": "unset"},
                            "pt_protocol": {"description": "0"},
                            "push": {"description": "0"},
                            "rst": {"description": "0"},
                            "source_ip": {"description": "::"},
                            "source_port": {"description": "0"},
                            "src_vlan": {"description": "unset"},
                            "syn": {"description": "0"},
                            "trigger_irule": {"description": "0"},
                            "trigger_log": {"description": "0"},
                            "ttl": {"description": "255"},
                            "urg": {"description": "0"},
                        }
                    }
                }
            },
        }


class test_get_net_packet_testersecurity(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/packet-tester/security/0": {
                "nestedStats": {
                    "entries": {
                        "ack": {"description": "0"},
                        "acl_device_action": {"description": "0"},
                        "acl_device_dest_fqdn_name": {"description": "unset"},
                        "acl_device_dst_geo": {"description": "unset"},
                        "acl_device_irule_name": {"description": "unset"},
                        "acl_device_is_default_rule": {"description": "0"},
                        "acl_device_is_staged": {"description": "0"},
                        "acl_device_log_config": {"description": "0"},
                        "acl_device_policy_name": {"description": "unset"},
                        "acl_device_policy_type": {"description": "unset"},
                        "acl_device_rule_name": {"description": "unset"},
                        "acl_device_src_fqdn_name": {"description": "unset"},
                        "acl_device_src_geo": {"description": "unset"},
                        "acl_device_subs_group_name": {"description": "unset"},
                        "acl_device_subs_name": {"description": "unset"},
                        "acl_device_vs_forward": {"description": "unset"},
                        "acl_listener_action": {"description": "0"},
                        "acl_listener_dest_fqdn_name": {
                            "description": "unset"
                        },
                        "acl_listener_dst_geo": {"description": "unset"},
                        "acl_listener_irule_name": {"description": "unset"},
                        "acl_listener_is_default_rule": {"description": "0"},
                        "acl_listener_is_staged": {"description": "0"},
                        "acl_listener_log_config": {"description": "0"},
                        "acl_listener_name": {"description": "unset"},
                        "acl_listener_policy_name": {"description": "unset"},
                        "acl_listener_policy_type": {"description": "unset"},
                        "acl_listener_rule_name": {"description": "unset"},
                        "acl_listener_src_fqdn_name": {"description": "unset"},
                        "acl_listener_src_geo": {"description": "unset"},
                        "acl_listener_subs_group_name": {
                            "description": "unset"
                        },
                        "acl_listener_subs_name": {"description": "unset"},
                        "acl_rtdom_action": {"description": "0"},
                        "acl_rtdom_dest_fqdn_name": {"description": "unset"},
                        "acl_rtdom_dst_geo": {"description": "unset"},
                        "acl_rtdom_irule_name": {"description": "unset"},
                        "acl_rtdom_is_default_rule": {"description": "0"},
                        "acl_rtdom_is_staged": {"description": "0"},
                        "acl_rtdom_log_config": {"description": "0"},
                        "acl_rtdom_name": {"description": "unset"},
                        "acl_rtdom_policy_name": {"description": "unset"},
                        "acl_rtdom_policy_type": {"description": "unset"},
                        "acl_rtdom_rule_name": {"description": "unset"},
                        "acl_rtdom_src_fqdn_name": {"description": "unset"},
                        "acl_rtdom_src_geo": {"description": "unset"},
                        "acl_rtdom_subs_group_name": {"description": "unset"},
                        "acl_rtdom_subs_name": {"description": "unset"},
                        "acl_rtdom_vs_forward": {"description": "unset"},
                        "check_staged": {"description": "0"},
                        "dest_ip": {"description": "::"},
                        "dest_port": {"description": "0"},
                        "dos_device_action": {"description": "0"},
                        "dos_device_attack_detected": {"description": "0"},
                        "dos_device_attack_drop_flag": {"description": "0"},
                        "dos_device_attack_vector": {"description": "unset"},
                        "dos_device_log_config": {"description": "0"},
                        "dos_device_wl": {"description": "0"},
                        "dos_listener_action": {"description": "0"},
                        "dos_listener_attack_detected": {"description": "0"},
                        "dos_listener_attack_drop_flag": {"description": "0"},
                        "dos_listener_attack_vector": {"description": "unset"},
                        "dos_listener_dos_profile_name": {
                            "description": "unset"
                        },
                        "dos_listener_log_config": {"description": "0"},
                        "dos_listener_name": {"description": "unset"},
                        "dos_listener_wl": {"description": "0"},
                        "fin": {"description": "0"},
                        "global_default_action": {"description": "0"},
                        "ipi_device_action": {"description": "0"},
                        "ipi_device_dst_category": {"description": "unset"},
                        "ipi_device_dst_hit_type": {"description": "0"},
                        "ipi_device_irule_name": {"description": "unset"},
                        "ipi_device_is_drop_dst": {"description": "0"},
                        "ipi_device_is_drop_src": {"description": "0"},
                        "ipi_device_is_shun": {"description": "0"},
                        "ipi_device_is_wl_dst": {"description": "0"},
                        "ipi_device_is_wl_src": {"description": "0"},
                        "ipi_device_log_config": {"description": "0"},
                        "ipi_device_policy_name": {"description": "unset"},
                        "ipi_device_src_category": {"description": "unset"},
                        "ipi_device_src_hit_type": {"description": "0"},
                        "ipi_listener_action": {"description": "0"},
                        "ipi_listener_dst_category": {"description": "unset"},
                        "ipi_listener_dst_hit_type": {"description": "0"},
                        "ipi_listener_irule_name": {"description": "unset"},
                        "ipi_listener_is_drop_dst": {"description": "0"},
                        "ipi_listener_is_drop_src": {"description": "0"},
                        "ipi_listener_is_shun": {"description": "0"},
                        "ipi_listener_is_wl_dst": {"description": "0"},
                        "ipi_listener_is_wl_src": {"description": "0"},
                        "ipi_listener_log_config": {"description": "0"},
                        "ipi_listener_name": {"description": "unset"},
                        "ipi_listener_policy_name": {"description": "unset"},
                        "ipi_listener_src_category": {"description": "unset"},
                        "ipi_listener_src_hit_type": {"description": "0"},
                        "ipi_rtdom_action": {"description": "0"},
                        "ipi_rtdom_dst_category": {"description": "unset"},
                        "ipi_rtdom_dst_hit_type": {"description": "0"},
                        "ipi_rtdom_irule_name": {"description": "unset"},
                        "ipi_rtdom_is_drop_dst": {"description": "0"},
                        "ipi_rtdom_is_drop_src": {"description": "0"},
                        "ipi_rtdom_is_shun": {"description": "0"},
                        "ipi_rtdom_is_wl_dst": {"description": "0"},
                        "ipi_rtdom_is_wl_src": {"description": "0"},
                        "ipi_rtdom_log_config": {"description": "0"},
                        "ipi_rtdom_name": {"description": "unset"},
                        "ipi_rtdom_policy_name": {"description": "unset"},
                        "ipi_rtdom_src_category": {"description": "unset"},
                        "ipi_rtdom_src_hit_type": {"description": "0"},
                        "nat_dst_object_name": {"description": "unset"},
                        "nat_dst_success": {"description": "1"},
                        "nat_dst_translated_address": {"description": "::"},
                        "nat_dst_translated_port": {"description": "0"},
                        "nat_dst_type": {"description": "0"},
                        "nat_policy_name": {"description": "unset"},
                        "nat_rule_name": {"description": "unset"},
                        "nat_src_object_name": {"description": "unset"},
                        "nat_src_success": {"description": "1"},
                        "nat_src_translated_address": {"description": "::"},
                        "nat_src_translated_port": {"description": "0"},
                        "nat_src_type": {"description": "0"},
                        "packet_test_listener_name": {"description": "unset"},
                        "packet_test_rtdom_name": {"description": "unset"},
                        "pat_src_mode": {"description": "unset"},
                        "pt_protocol": {"description": "0"},
                        "push": {"description": "0"},
                        "rst": {"description": "0"},
                        "source_ip": {"description": "::"},
                        "source_port": {"description": "0"},
                        "src_vlan": {"description": "unset"},
                        "syn": {"description": "0"},
                        "trigger_irule": {"description": "0"},
                        "trigger_log": {"description": "0"},
                        "ttl": {"description": "255"},
                        "urg": {"description": "0"},
                    }
                }
            }
        },
        "kind": "tm:net:packet-tester:security:securitystats",
        "selfLink": "https://localhost/mgmt/tm/net/packet-tester/security?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetPackettesterSecurity(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetPackettesterSecurity(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
