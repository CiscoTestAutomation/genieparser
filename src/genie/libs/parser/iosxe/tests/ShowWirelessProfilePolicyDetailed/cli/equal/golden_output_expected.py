expected_output = {
    "policy_profile_name": "lizzard_Fabric_F_90c67354",
    "description": "lizzard_Fabric_F_90c67354",
    "status": "ENABLED",
    "vlan": "1",
    "multicast_vlan": "0",
    "wireless_mgmt_interface_vlan": "10",
    "multicast_filter": "DISABLED",
    "qbss_load": "ENABLED",
    "passive_client": "DISABLED",
    "et_analytics": "DISABLED",
    "staticip_mobility": "DISABLED",
    "wlan_switching_policy": {
        "flex_central_switching": "DISABLED",
        "flex_central_authentication": "ENABLED",
        "flex_central_dhcp": "DISABLED",
        "flex_nat_pat": "DISABLED",
        "flex_central_assoc": "ENABLED"
    },
    "wlan_flex_policy": {
        "vlan_based_central_switching": "DISABLED"
    },
    "wlan_acl": {
        "ipv4_acl": "Not Configured",
        "ipv6_acl": "Not Configured",
        "l2_acl": "Not Configured",
        "preauth_urlfilter_list": "Not Configured",
        "postauth_urlfilter_list": "Not Configured"
    },
    "wlan_timeout": {
        "session_timeout": 36000,
        "idle_timeout": 7200,
        "idle_threshold": 0,
        "guest_timeout": "DISABLED"
    },
    "wlan_local_profiling": {
        "subscriber_policy_name": "Not Configured",
        "radius_profiling": "ENABLED",
        "http_tlv_caching": "DISABLED",
        "dhcp_tlv_caching": "DISABLED"
    },
    "cts_policy": {
        "inline_tagging": "DISABLED",
        "sgacl_enforcement": "DISABLED",
        "default_sgt": 0
    },
    "wlan_mobility": {
        "anchor": "DISABLED"
    },
    "avc_visibility": "Enabled",
    "ipv4_flow_monitors": [
        "ingress",
        "egress"
    ],
    "ipv6_flow_monitors": [
        "ingress",
        "egress"
    ],
    "nbar_protocol_discovery": "Disabled",
    "reanchoring": "Disabled",
    "classmap_for_reanchoring": {
        "classmap_name": "Not Configured"
    },
    "qos_per_ssid": {
        "ingress_service_name": "platinum-up",
        "egress_service_name": "platinum"
    },
    "qos_per_client": {
        "ingress_service_name": "Not Configured",
        "egress_service_name": "Not Configured"
    },
    "umbrella_information": {
        "cisco_umbrella_parameter_map": "Not Configured",
        "dhcp_dns_option": "ENABLED",
        "mode": "ignore"
    },
    "autoqos_mode": "None",
    "call_snooping": "Disabled",
    "tunnel_profile": {
        "profile_name": "Not Configured"
    },
    "fabric_profile": {
        "profile_name": "lizzard_Fabric_F_90c67354"
    },
    "accounting_list": {
        "accounting_list": "dnac-client-radius-group"
    },
    "dhcp": {
        "required": "ENABLED",
        "server_address": "0.0.0.0",
        "opt82": {
            "dhcpopt82enable": "DISABLED",
            "dhcpopt82ascii": "DISABLED",
            "dhcpopt82rid": "DISABLED",
            "apmac": "DISABLED",
            "ssid": "DISABLED",
            "ap_ethmac": "DISABLED",
            "apname": "DISABLED",
            "policy_tag": "DISABLED",
            "ap_location": "DISABLED",
            "vlan_id": "DISABLED"
        }
    },
    "exclusionlist_params": {
        "exclusionlist": "ENABLED",
        "exclusiontimeout": 60
    },
    "aaa_policy_params": {
        "aaa_override": "ENABLED",
        "aaa_nac": "ENABLED",
        "aaa_policy_name": "default-aaa-policy"
    },
    "wgb_policy_params": {
        "broadcast_tagging": "DISABLED"
    },
    "hotspot_2.0_server-name": "Not Configured",
    "mobility_anchor_list": {},
    "mdns_gateway": {
        "mdns_service_policy_name": "default-mdns-service-policy"
    },
    "policy_proxy_settings": {
        "arp_proxy_state": "DISABLED",
        "ipv6_proxy_state": "None"
    },
    "airtime_fairness_profile": {
        "2.4ghz_atf_policy": "default-atf-policy",
        "5ghz_atf_policy": "default-atf-policy"
    }
}