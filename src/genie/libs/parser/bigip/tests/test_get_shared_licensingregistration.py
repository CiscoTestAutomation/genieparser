# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_shared_licensingregistration
from genie.libs.parser.bigip.get_shared_licensingregistration import (
    SharedLicensingRegistration,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/shared/licensing/registration'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "vendor": "F5 Networks, Inc.",
            "licensedDateTime": "2019-10-10T00:00:00-07:00",
            "licensedVersion": "14.1.2",
            "registrationKey": "IYMGF-MMRUK-NDXCX-CWRKR-AAMNTPS",
            "dossier": "1286c57cd91225fa98d12e1fa2e1a70d0a16bf8c38b5adcb8eda97059c044c59db05812bd369a8b4b5a58e2a2c80b6963bb58186de9e679b1325899eced722d5a0675bed8862d59b85f1732923517023c8435a1ab1890745cabc319cd3857c97f335714a5ec28bf2edbda975dc3531164bb995e194c6e7a1822fdf3d730c1bdb4ce7ae7ded071383",
            "authorization": "53b972604fb773445f7d25b447091e3db0633ca89b9674b16cdbd3cdfd3b4483d901cfc42299a8e2bb8c35724979e30bbc74b7d512fef2da266b024203ea9d4205328f85bc1b3817b46031ee10eb0c8f65633bae010f4eb9b04226be243a0146dae1083317e1c88530c7acc46314178174d81169c916e525e4b6f2a9e369f7d3dfa9ceb11e3ab273de9296ce7bff36c87091294e795b4dcd12febfbe60d83838fe7be870ef0c15b965d13aca5978b0c72619b901597f759c0a5f947693b87128dcfff179df3a7124c31bb0f34b2cf0556f3651cb5cb6aa7c226a676a3d7f74db4c4b35d630d79b83c055cf48fbba884dfc394e4e8d58760768315df097b18917",
            "usage": "Production",
            "platformId": "Z100",
            "authVers": "5b",
            "serviceCheckDateTime": "2019-09-25T00:00:00-07:00",
            "machineId": "a9a51b0b-afdd-445a-8ac7-b1ed2c90a1be",
            "exclusivePlatform": [
                "Z100",
                "Z100A",
                "Z100a_icm",
                "Z100AlibabaCloud",
                "Z100AzureCloud",
                "Z100GoogleCloud",
                "Z100H",
                "Z100K",
                "Z100x",
            ],
            "activeModules": [
                "BIG-IP, VE, LAB|GSMORBH-FRIQHYL|Rate Shaping|External Interface and Network HSM, VE|BIG-IP VE, Multicast Routing|Routing Bundle, VE|ASM, VE|SSL, VE|DNS VE Lab  (10K QPS)|Max Compression, VE|Advanced Protocols, VE|SSL Orchestrator, VE|Advanced Web Application Firewall, VE Lab|APM, Lab, VE|AFM, VE (LAB ONLY - NO ROUTING)|DNSSEC|VE, Carrier Grade NAT (AFM ONLY)|PSM, VE"
            ],
            "optionalModules": [
                "Anti-Bot Mobile, VE 25 Mbps",
                "App Mode (TMSH Only, No Root/Bash)",
                "FIPS 140-2 Level 1, BIG-IP VE-200M",
                "IP Intelligence, 1Yr, VE-200M/VE-25M",
                "IP Intelligence, 3Yr, VE-200M/VE-25M",
                "ONAP",
                "Threat Campaigns, 1Yr, VE-200M/VE-25M",
                "URL Filtering, VE-25M-1G, 500 Sessions, 1Yr",
                "URL Filtering, VE-25M-1G, 500 Sessions, 3Yr",
            ],
            "featureFlags": [
                {"featureName": "perf_SSL_Mbps", "featureValue": "1"},
                {"featureName": "gtm_rate_fallback", "featureValue": "10000"},
                {"featureName": "gtm_rate_limit", "featureValue": "10000"},
                {
                    "featureName": "ltm_dns_rate_fallback",
                    "featureValue": "10000",
                },
                {"featureName": "ltm_dns_rate_limit", "featureValue": "10000"},
                {"featureName": "apm_access_sessions", "featureValue": "40"},
                {"featureName": "apm_sessions", "featureValue": "10"},
                {
                    "featureName": "apm_urlf_limited_sessions",
                    "featureValue": "40",
                },
                {"featureName": "perf_VE_cores", "featureValue": "8"},
                {"featureName": "waf_gc", "featureValue": "enabled"},
                {"featureName": "mod_waf", "featureValue": "enabled"},
                {"featureName": "mod_datasafe", "featureValue": "enabled"},
                {
                    "featureName": "ltm_persist_cookie",
                    "featureValue": "enabled",
                },
                {"featureName": "ltm_persist", "featureValue": "enabled"},
                {"featureName": "ltm_lb_rr", "featureValue": "enabled"},
                {"featureName": "ltm_lb_ratio", "featureValue": "enabled"},
                {"featureName": "ltm_lb_priority", "featureValue": "enabled"},
                {
                    "featureName": "ltm_lb_pool_member_limit",
                    "featureValue": "UNLIMITED",
                },
                {
                    "featureName": "ltm_lb_least_conn",
                    "featureValue": "enabled",
                },
                {"featureName": "ltm_lb_l3_addr", "featureValue": "enabled"},
                {"featureName": "ltm_lb", "featureValue": "enabled"},
                {"featureName": "asm_apps", "featureValue": "unlimited"},
                {"featureName": "sslo_add", "featureValue": "enabled"},
                {"featureName": "mod_ssli", "featureValue": "enabled"},
                {"featureName": "ltm_ssl_fwdp", "featureValue": "enabled"},
                {"featureName": "pkcs11_nethsm", "featureValue": "enabled"},
                {
                    "featureName": "perf_VE_throughput_Mbps",
                    "featureValue": "10",
                },
                {
                    "featureName": "perf_remote_crypto_client",
                    "featureValue": "enabled",
                },
                {"featureName": "mod_ltm", "featureValue": "enabled"},
                {"featureName": "mod_ilx", "featureValue": "enabled"},
                {
                    "featureName": "ltm_network_virtualization",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "perf_SSL_total_TPS",
                    "featureValue": "UNLIMITED",
                },
                {
                    "featureName": "perf_SSL_per_core",
                    "featureValue": "enabled",
                },
                {"featureName": "perf_SSL_cmp", "featureValue": "enabled"},
                {
                    "featureName": "perf_http_compression_Mbps",
                    "featureValue": "UNLIMITED",
                },
                {"featureName": "nw_routing_rip", "featureValue": "enabled"},
                {"featureName": "nw_routing_ospf", "featureValue": "enabled"},
                {"featureName": "nw_routing_isis", "featureValue": "enabled"},
                {"featureName": "nw_routing_bgp", "featureValue": "enabled"},
                {"featureName": "nw_routing_bfd", "featureValue": "enabled"},
                {"featureName": "nw_routing_pim", "featureValue": "enabled"},
                {"featureName": "mod_dnsgtm", "featureValue": "enabled"},
                {"featureName": "ltm_dns_v13", "featureValue": "enabled"},
                {"featureName": "ltm_dns_lite", "featureValue": "enabled"},
                {
                    "featureName": "ltm_dns_licensed_objects",
                    "featureValue": "UNLIMITED",
                },
                {
                    "featureName": "gtm_licensed_objects",
                    "featureValue": "UNLIMITED",
                },
                {"featureName": "mod_cgnat", "featureValue": "enabled"},
                {"featureName": "ltm_monitor_udp", "featureValue": "enabled"},
                {
                    "featureName": "ltm_monitor_tcp_ho",
                    "featureValue": "enabled",
                },
                {"featureName": "ltm_monitor_tcp", "featureValue": "enabled"},
                {
                    "featureName": "ltm_monitor_radius",
                    "featureValue": "enabled",
                },
                {"featureName": "ltm_monitor_icmp", "featureValue": "enabled"},
                {
                    "featureName": "ltm_monitor_gateway_icmp",
                    "featureValue": "enabled",
                },
                {"featureName": "dslite", "featureValue": "enabled"},
                {"featureName": "cgnat", "featureValue": "enabled"},
                {"featureName": "mod_asm", "featureValue": "enabled"},
                {
                    "featureName": "ltm_proxy_content",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_ha_vlan_failsafe",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_conn_one_connect_pool",
                    "featureValue": "enabled",
                },
                {"featureName": "mod_apm", "featureValue": "enabled"},
                {
                    "featureName": "apm_web_applications",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "apm_remote_desktop",
                    "featureValue": "enabled",
                },
                {"featureName": "apm_pingaccess", "featureValue": "enabled"},
                {"featureName": "apm_na", "featureValue": "enabled"},
                {
                    "featureName": "apm_logon_page_fraud_protection",
                    "featureValue": "enabled",
                },
                {"featureName": "apm_ep_svk", "featureValue": "enabled"},
                {"featureName": "apm_ep_pws", "featureValue": "enabled"},
                {
                    "featureName": "apm_ep_machinecert",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "apm_ep_grouppolicy",
                    "featureValue": "enabled",
                },
                {"featureName": "apm_ep_fwcheck", "featureValue": "enabled"},
                {"featureName": "apm_ep_avcheck", "featureValue": "enabled"},
                {"featureName": "apm_ep", "featureValue": "enabled"},
                {"featureName": "apm_app_tunnel", "featureValue": "enabled"},
                {
                    "featureName": "apm_api_protection",
                    "featureValue": "enabled",
                },
                {"featureName": "apm_agc", "featureValue": "enabled"},
                {
                    "featureName": "api_protection_infra",
                    "featureValue": "enabled",
                },
                {"featureName": "mod_afw", "featureValue": "enabled"},
                {"featureName": "mod_afm", "featureValue": "enabled"},
                {"featureName": "ltm_monitor_rule", "featureValue": "enabled"},
                {
                    "featureName": "message_routing_sip",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "message_routing_diameter",
                    "featureValue": "enabled",
                },
                {"featureName": "ltm_proxy_gtp", "featureValue": "enabled"},
                {"featureName": "ltm_fix", "featureValue": "enabled"},
                {"featureName": "ltm_dbproxy", "featureValue": "enabled"},
                {"featureName": "ltm_dnssec", "featureValue": "enabled"},
                {
                    "featureName": "ltm_bandw_rate_tosque",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_bandw_rate_fairque",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_bandw_rate_classl7",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_bandw_rate_classl4",
                    "featureValue": "enabled",
                },
                {
                    "featureName": "ltm_bandw_rate_classes",
                    "featureValue": "enabled",
                },
                {"featureName": "certificate_auth", "featureValue": "v2"},
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:shared:licensing:registration:licensestate",
            "selfLink": "https://localhost/mgmt/tm/shared/licensing/registration",
        }


class test_get_shared_licensingregistration(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "activeModules": [
            "BIG-IP, VE, LAB|GSMORBH-FRIQHYL|Rate Shaping|External "
            "Interface and Network HSM, VE|BIG-IP VE, Multicast "
            "Routing|Routing Bundle, VE|ASM, VE|SSL, VE|DNS VE Lab  "
            "(10K QPS)|Max Compression, VE|Advanced Protocols, VE|SSL "
            "Orchestrator, VE|Advanced Web Application Firewall, VE "
            "Lab|APM, Lab, VE|AFM, VE (LAB ONLY - NO "
            "ROUTING)|DNSSEC|VE, Carrier Grade NAT (AFM ONLY)|PSM, VE"
        ],
        "authVers": "5b",
        "authorization": "53b972604fb773445f7d25b447091e3db0633ca89b9674b16cdbd3cdfd3b4483d901cfc42299a8e2bb8c35724979e30bbc74b7d512fef2da266b024203ea9d4205328f85bc1b3817b46031ee10eb0c8f65633bae010f4eb9b04226be243a0146dae1083317e1c88530c7acc46314178174d81169c916e525e4b6f2a9e369f7d3dfa9ceb11e3ab273de9296ce7bff36c87091294e795b4dcd12febfbe60d83838fe7be870ef0c15b965d13aca5978b0c72619b901597f759c0a5f947693b87128dcfff179df3a7124c31bb0f34b2cf0556f3651cb5cb6aa7c226a676a3d7f74db4c4b35d630d79b83c055cf48fbba884dfc394e4e8d58760768315df097b18917",
        "dossier": "1286c57cd91225fa98d12e1fa2e1a70d0a16bf8c38b5adcb8eda97059c044c59db05812bd369a8b4b5a58e2a2c80b6963bb58186de9e679b1325899eced722d5a0675bed8862d59b85f1732923517023c8435a1ab1890745cabc319cd3857c97f335714a5ec28bf2edbda975dc3531164bb995e194c6e7a1822fdf3d730c1bdb4ce7ae7ded071383",
        "exclusivePlatform": [
            "Z100",
            "Z100A",
            "Z100a_icm",
            "Z100AlibabaCloud",
            "Z100AzureCloud",
            "Z100GoogleCloud",
            "Z100H",
            "Z100K",
            "Z100x",
        ],
        "featureFlags": [
            {"featureName": "perf_SSL_Mbps", "featureValue": "1"},
            {"featureName": "gtm_rate_fallback", "featureValue": "10000"},
            {"featureName": "gtm_rate_limit", "featureValue": "10000"},
            {"featureName": "ltm_dns_rate_fallback", "featureValue": "10000"},
            {"featureName": "ltm_dns_rate_limit", "featureValue": "10000"},
            {"featureName": "apm_access_sessions", "featureValue": "40"},
            {"featureName": "apm_sessions", "featureValue": "10"},
            {"featureName": "apm_urlf_limited_sessions", "featureValue": "40"},
            {"featureName": "perf_VE_cores", "featureValue": "8"},
            {"featureName": "waf_gc", "featureValue": "enabled"},
            {"featureName": "mod_waf", "featureValue": "enabled"},
            {"featureName": "mod_datasafe", "featureValue": "enabled"},
            {"featureName": "ltm_persist_cookie", "featureValue": "enabled"},
            {"featureName": "ltm_persist", "featureValue": "enabled"},
            {"featureName": "ltm_lb_rr", "featureValue": "enabled"},
            {"featureName": "ltm_lb_ratio", "featureValue": "enabled"},
            {"featureName": "ltm_lb_priority", "featureValue": "enabled"},
            {
                "featureName": "ltm_lb_pool_member_limit",
                "featureValue": "UNLIMITED",
            },
            {"featureName": "ltm_lb_least_conn", "featureValue": "enabled"},
            {"featureName": "ltm_lb_l3_addr", "featureValue": "enabled"},
            {"featureName": "ltm_lb", "featureValue": "enabled"},
            {"featureName": "asm_apps", "featureValue": "unlimited"},
            {"featureName": "sslo_add", "featureValue": "enabled"},
            {"featureName": "mod_ssli", "featureValue": "enabled"},
            {"featureName": "ltm_ssl_fwdp", "featureValue": "enabled"},
            {"featureName": "pkcs11_nethsm", "featureValue": "enabled"},
            {"featureName": "perf_VE_throughput_Mbps", "featureValue": "10"},
            {
                "featureName": "perf_remote_crypto_client",
                "featureValue": "enabled",
            },
            {"featureName": "mod_ltm", "featureValue": "enabled"},
            {"featureName": "mod_ilx", "featureValue": "enabled"},
            {
                "featureName": "ltm_network_virtualization",
                "featureValue": "enabled",
            },
            {"featureName": "perf_SSL_total_TPS", "featureValue": "UNLIMITED"},
            {"featureName": "perf_SSL_per_core", "featureValue": "enabled"},
            {"featureName": "perf_SSL_cmp", "featureValue": "enabled"},
            {
                "featureName": "perf_http_compression_Mbps",
                "featureValue": "UNLIMITED",
            },
            {"featureName": "nw_routing_rip", "featureValue": "enabled"},
            {"featureName": "nw_routing_ospf", "featureValue": "enabled"},
            {"featureName": "nw_routing_isis", "featureValue": "enabled"},
            {"featureName": "nw_routing_bgp", "featureValue": "enabled"},
            {"featureName": "nw_routing_bfd", "featureValue": "enabled"},
            {"featureName": "nw_routing_pim", "featureValue": "enabled"},
            {"featureName": "mod_dnsgtm", "featureValue": "enabled"},
            {"featureName": "ltm_dns_v13", "featureValue": "enabled"},
            {"featureName": "ltm_dns_lite", "featureValue": "enabled"},
            {
                "featureName": "ltm_dns_licensed_objects",
                "featureValue": "UNLIMITED",
            },
            {
                "featureName": "gtm_licensed_objects",
                "featureValue": "UNLIMITED",
            },
            {"featureName": "mod_cgnat", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_udp", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_tcp_ho", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_tcp", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_radius", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_icmp", "featureValue": "enabled"},
            {
                "featureName": "ltm_monitor_gateway_icmp",
                "featureValue": "enabled",
            },
            {"featureName": "dslite", "featureValue": "enabled"},
            {"featureName": "cgnat", "featureValue": "enabled"},
            {"featureName": "mod_asm", "featureValue": "enabled"},
            {"featureName": "ltm_proxy_content", "featureValue": "enabled"},
            {"featureName": "ltm_ha_vlan_failsafe", "featureValue": "enabled"},
            {
                "featureName": "ltm_conn_one_connect_pool",
                "featureValue": "enabled",
            },
            {"featureName": "mod_apm", "featureValue": "enabled"},
            {"featureName": "apm_web_applications", "featureValue": "enabled"},
            {"featureName": "apm_remote_desktop", "featureValue": "enabled"},
            {"featureName": "apm_pingaccess", "featureValue": "enabled"},
            {"featureName": "apm_na", "featureValue": "enabled"},
            {
                "featureName": "apm_logon_page_fraud_protection",
                "featureValue": "enabled",
            },
            {"featureName": "apm_ep_svk", "featureValue": "enabled"},
            {"featureName": "apm_ep_pws", "featureValue": "enabled"},
            {"featureName": "apm_ep_machinecert", "featureValue": "enabled"},
            {"featureName": "apm_ep_grouppolicy", "featureValue": "enabled"},
            {"featureName": "apm_ep_fwcheck", "featureValue": "enabled"},
            {"featureName": "apm_ep_avcheck", "featureValue": "enabled"},
            {"featureName": "apm_ep", "featureValue": "enabled"},
            {"featureName": "apm_app_tunnel", "featureValue": "enabled"},
            {"featureName": "apm_api_protection", "featureValue": "enabled"},
            {"featureName": "apm_agc", "featureValue": "enabled"},
            {"featureName": "api_protection_infra", "featureValue": "enabled"},
            {"featureName": "mod_afw", "featureValue": "enabled"},
            {"featureName": "mod_afm", "featureValue": "enabled"},
            {"featureName": "ltm_monitor_rule", "featureValue": "enabled"},
            {"featureName": "message_routing_sip", "featureValue": "enabled"},
            {
                "featureName": "message_routing_diameter",
                "featureValue": "enabled",
            },
            {"featureName": "ltm_proxy_gtp", "featureValue": "enabled"},
            {"featureName": "ltm_fix", "featureValue": "enabled"},
            {"featureName": "ltm_dbproxy", "featureValue": "enabled"},
            {"featureName": "ltm_dnssec", "featureValue": "enabled"},
            {
                "featureName": "ltm_bandw_rate_tosque",
                "featureValue": "enabled",
            },
            {
                "featureName": "ltm_bandw_rate_fairque",
                "featureValue": "enabled",
            },
            {
                "featureName": "ltm_bandw_rate_classl7",
                "featureValue": "enabled",
            },
            {
                "featureName": "ltm_bandw_rate_classl4",
                "featureValue": "enabled",
            },
            {
                "featureName": "ltm_bandw_rate_classes",
                "featureValue": "enabled",
            },
            {"featureName": "certificate_auth", "featureValue": "v2"},
        ],
        "generation": 0,
        "kind": "tm:shared:licensing:registration:licensestate",
        "lastUpdateMicros": 0,
        "licensedDateTime": "2019-10-10T00:00:00-07:00",
        "licensedVersion": "14.1.2",
        "machineId": "a9a51b0b-afdd-445a-8ac7-b1ed2c90a1be",
        "optionalModules": [
            "Anti-Bot Mobile, VE 25 Mbps",
            "App Mode (TMSH Only, No Root/Bash)",
            "FIPS 140-2 Level 1, BIG-IP VE-200M",
            "IP Intelligence, 1Yr, VE-200M/VE-25M",
            "IP Intelligence, 3Yr, VE-200M/VE-25M",
            "ONAP",
            "Threat Campaigns, 1Yr, VE-200M/VE-25M",
            "URL Filtering, VE-25M-1G, 500 Sessions, 1Yr",
            "URL Filtering, VE-25M-1G, 500 Sessions, 3Yr",
        ],
        "platformId": "Z100",
        "registrationKey": "IYMGF-MMRUK-NDXCX-CWRKR-AAMNTPS",
        "selfLink": "https://localhost/mgmt/tm/shared/licensing/registration",
        "serviceCheckDateTime": "2019-09-25T00:00:00-07:00",
        "usage": "Production",
        "vendor": "F5 Networks, Inc.",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SharedLicensingRegistration(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SharedLicensingRegistration(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
