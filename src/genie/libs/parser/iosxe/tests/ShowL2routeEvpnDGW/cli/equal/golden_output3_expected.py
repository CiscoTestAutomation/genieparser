# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                       1: {
                           "eth_tag": {
                               0: {
                                   "producer": {
                                       "BGP": {
                                           "mac_addr": {
                                               "0011.0011.0011": {
                                                   "host_ip": {
                                                       "192.168.11.254": {
                                                           "next_hops": [
                                                               "V:20011 3.3.3.2",
                                                               "V:20011 4.4.4.2"
                                                           ]
                                                       },
                                                       "2001:11::254": {
                                                           "next_hops": [
                                                               "V:20011 3.3.3.2"
                                                           ]
                                                       }
                                                   }
                                               },
                                               "aabb.0011.0031": {
                                                   "host_ip": {
                                                       "192.168.11.31": {
                                                           "next_hops": [
                                                               "V:20011 3.3.3.2"
                                                           ]
                                                       },
                                                       "FE80::A8BB:FF:FE11:31": {
                                                           "next_hops": [
                                                               "V:20011 3.3.3.2"
                                                           ]
                                                       }
                                                   }
                                               }
                                           }
                                       },
                                       "L2VPN": {
                                           "mac_addr": {
                                               "aabb.0011.0011": {
                                                   "host_ip": {
                                                       "192.168.11.11": {
                                                           "next_hops": [
                                                               "Et0/1:11"
                                                           ]
                                                       },
                                                       "FE80::A8BB:FF:FE11:11": {
                                                           "next_hops": [
                                                               "Et0/1:11"
                                                           ]
                                                       }
                                                   }
                                               }
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       2: {
                           "eth_tag": {
                               0: {
                                   "producer": {
                                       "BGP": {
                                           "mac_addr": {
                                               "0012.0012.0012": {
                                                   "host_ip": {
                                                       "192.168.12.254": {
                                                           "next_hops": [
                                                               "V:20012 3.3.3.2"
                                                           ]
                                                       },
                                                       "2001:12::254": {
                                                           "next_hops": [
                                                               "V:20012 3.3.3.2"
                                                           ]
                                                       }
                                                   }
                                               },
                                               "0012.0012.0013": {
                                                   "host_ip": {
                                                       "192.168.12.254": {
                                                           "next_hops": [
                                                               "V:20012 3.3.1.2"
                                                           ]
                                                       },
                                                       "2001:12::254": {
                                                           "next_hops": [
                                                               "V:20012 3.3.1.2"
                                                           ]
                                                       }
                                                   }
                                               },
                                               "aabb.0012.0022": {
                                                   "host_ip": {
                                                       "FE80:AAAA:BBBB:CCCC:A8BB:FFFF:FE12:2222": {
                                                           "next_hops": [
                                                               "V:20012 FE80:AAAA:BBBB:DDDD:A8BB:FFFF:FE12:2222",
                                                               "V:20012 FE80:AAAA:BBBB:DDDD:A8BB:FFFF:FE12:3333",
                                                               "V:20012 FE80:AAAA:BBBB:DDDD:A8BB:FFFF:FE12:4444"
                                                           ]
                                                       },
                                                       "FE80:AAAA:BBBB:CCCC:A8BB:FFFF:FE12:1111": {
                                                           "next_hops": [
                                                               "V:20012 FE80:AAAA:BBBB:EEEE:A8BB:FFFF:FE12:1111"
                                                           ]
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
