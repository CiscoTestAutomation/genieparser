expected_output = {
  "RM-NAM-IBGP-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_local_pref": 700,
          "set_community": "1:1"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-PBR_APPS_TO_MPLS": {
    "statements": {
      "5": {
        "actions": { "set_next_hop_self": False, "route_disposition": "deny" },
        "conditions":{
          "match_access_list": "PBR-EXCLUSION-SITE-SUBNET"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      },
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_next_hop": ["172.16.154.94", "172.16.154.102"]
        },
        "conditions":{
          "match_access_list": "ACL-APPLICATION-SAP-DC"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      },
      "20": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_next_hop": ["172.16.154.94", "172.16.154.102"]
        },
        "conditions":{
          "match_access_list": "ACL-APPLICATION-SAP_PLM-DC"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      },
      "30": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_next_hop": ["172.16.154.94", "172.16.154.102"]
        },
        "conditions":{
          "match_access_list": "ACL-APPLICATION-ABACUS_EUREKA-DC"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      },
      "40": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_next_hop": ["172.16.154.94", "172.16.154.102"]
        },
        "conditions":{
          "match_access_list": "ACL-APPLICATION-INTERSPEC-DC"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-LATAM-IBGP-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_local_pref": 700,
          "set_community": "1:110"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-BGP-SPOKES-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit"
        },
        "conditions": {
          "match_community_list": "CL-HUB-ORIGINATE"
        },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-FILTER-REDISTRIBUTED-DMVPN-ROUTES-IN": {
    "statements": {
      "10": {
        "actions": { "set_next_hop_self": False, "route_disposition": "deny" },
        "conditions": { "match_tag_list": "65534" },
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      },
      "20": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-EU-IBGP-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_local_pref": 900,
          "set_community": "1:5"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-APAC-IBGP-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_local_pref": 700,
          "set_community": "1:19"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  },
  "RM-AMET-IBGP-OUT": {
    "statements": {
      "10": {
        "actions": {
          "set_next_hop_self": False,
          "route_disposition": "permit",
          "set_local_pref": 900,
          "set_community": "1:27"
        },
        "conditions": {},
        "policy_routing_matches": { "packets": 0, "bytes": 0 }
      }
    }
  }
}
