expected_output = {
  "interfaces": {
    "TenGigabitEthernet1/0/1": {
      "mac": "0000.0000.0000",
      "directions": {
        "input": {
          "protocols": {
            "mac": {
              "policy": {
                "policy_name": "pacl1",
                "policy_handle": "0x8c0000ad",
                "policy_intf_handle": "0xee0000b5",
                "id": 60,
                "protocol": "MAC",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 4,
                "acls": {
                  "1": {
                    "acl_handle": "0x500000f0",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 5,
                    "aces": {
                      "1": { "ace_handle": "0xb4000185" },
                      "2": { "ace_handle": "0x87000186" },
                      "3": { "ace_handle": "0x70000187" },
                      "4": { "ace_handle": "0x61000188" },
                      "5": { "ace_handle": "0xfd000189" }
                    }
                  }
                }
              }
            },
            "ipv6": {
              "policy": {
                "policy_name": "pacl5",
                "policy_handle": "0xab0000b1",
                "policy_intf_handle": "0xe50000b9",
                "id": 64,
                "protocol": "IPV6",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 8,
                "acls": {
                  "1": {
                    "acl_handle": "0xa80000f4",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 7,
                    "aces": {
                      "1": { "ace_handle": "0x1e000199" },
                      "2": { "ace_handle": "0xaa00019a" },
                      "3": { "ace_handle": "0xcd00019b" },
                      "4": { "ace_handle": "0xfb00019c" },
                      "5": { "ace_handle": "0xae00019d" },
                      "6": { "ace_handle": "0xa200019e" },
                      "7": { "ace_handle": "0x6e00019f" }
                    }
                  }
                }
              }
            },
            "ipv4": {
              "policy": {
                "policy_name": "pacl3",
                "policy_handle": "0xdb0000af",
                "policy_intf_handle": "0xf40000b7",
                "id": 62,
                "protocol": "IPV4",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 4,
                "acls": {
                  "1": {
                    "acl_handle": "0x800000f2",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 5,
                    "aces": {
                      "1": { "ace_handle": "0xe900018f" },
                      "2": { "ace_handle": "0xec000190" },
                      "3": { "ace_handle": "0x74000191" },
                      "4": { "ace_handle": "0x06000192" },
                      "5": { "ace_handle": "0xee000193" }
                    }
                  }
                }
              }
            }
          }
        },
        "output": {
          "protocols": {
            "ipv6": {
              "policy": {
                "policy_name": "pacl6",
                "policy_handle": "0x4f0000b2",
                "policy_intf_handle": "0xcd0000ba",
                "id": 65,
                "protocol": "IPV6",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 8,
                "acls": {
                  "1": {
                    "acl_handle": "0x800000f5",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 7,
                    "aces": {
                      "1": { "ace_handle": "0x6e0001a0" },
                      "2": { "ace_handle": "0x620001a1" },
                      "3": { "ace_handle": "0xe90001a2" },
                      "4": { "ace_handle": "0x850001a3" },
                      "5": { "ace_handle": "0x2f0001a4" },
                      "6": { "ace_handle": "0x890001a5" },
                      "7": { "ace_handle": "0xf40001a6" }
                    }
                  }
                }
              }
            },
            "mac": {
              "policy": {
                "policy_name": "pacl2",
                "policy_handle": "0x640000ae",
                "policy_intf_handle": "0x220000b6",
                "id": 61,
                "protocol": "MAC",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 4,
                "acls": {
                  "1": {
                    "acl_handle": "0x590000f1",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 5,
                    "aces": {
                      "1": { "ace_handle": "0xe300018a" },
                      "2": { "ace_handle": "0xf700018b" },
                      "3": { "ace_handle": "0xe800018c" },
                      "4": { "ace_handle": "0xc300018d" },
                      "5": { "ace_handle": "0x4200018e" }
                    }
                  }
                }
              }
            },
            "ipv4": {
              "policy": {
                "policy_name": "pacl4",
                "policy_handle": "0xd60000b0",
                "policy_intf_handle": "0x910000b8",
                "id": 63,
                "protocol": "IPV4",
                "feature": "AAL_FEATURE_PACL",
                "number_of_acls": 1,
                "number_of_vmrs": 4,
                "acls": {
                  "1": {
                    "acl_handle": "0xe60000f3",
                    "acl_flags": "0x00000001",
                    "number_of_aces": 5,
                    "aces": {
                      "1": { "ace_handle": "0xd7000194" },
                      "2": { "ace_handle": "0xd5000195" },
                      "3": { "ace_handle": "0x13000196" },
                      "4": { "ace_handle": "0x6f000197" },
                      "5": { "ace_handle": "0xce000198" }
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
}
