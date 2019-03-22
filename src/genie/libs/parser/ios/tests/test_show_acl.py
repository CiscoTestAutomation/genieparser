#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.ios.show_acl import ShowAccessLists

from genie.libs.parser.iosxe.tests.test_show_acl import test_show_access_lists as test_show_access_lists_iosxe

class test_show_access_lists(test_show_access_lists_iosxe):

    golden_output_standard = {'execute.return_value': '''\
        Switch# show ip access-lists
        Standard IP access list 1
            permit 172.20.10.10
        Standard IP access list 10
            permit 12.12.12.12
        Standard IP access list 12
            deny   1.3.3.2
        Standard IP access list 32
            permit 172.20.20.20
        Standard IP access list 34
            permit 10.24.35.56
            permit 23.45.56.34
    '''}

    golden_parsed_output_standard = {
        "1": {
            "name": "1",
            "type": "ipv4-acl-type"
        },
        "10": {
            "name": "10",
            "type": "ipv4-acl-type"
        },
        "12": {
            "name": "12",
            "type": "ipv4-acl-type"
        },
        "32": {
            "name": "32",
            "type": "ipv4-acl-type"
        },
        "34": {
            "name": "34",
            "type": "ipv4-acl-type"
        }
    }

    golden_output_duplicate = {'execute.return_value': '''\
        Router# show access-lists 101
        Extended IP access list 101
            10 permit ip host 10.0.0.0 host 10.5.5.34
            20 permit icmp any any
            30 permit ip host 10.0.0.0 host 10.2.54.2
            40 permit ip host 10.0.0.0 host 10.3.32.3 log
        ip access-list extended 101
         100 permit icmp any any
        Extended IP access list 101
            10 permit ip host 10.3.3.3 host 10.5.5.34
            20 permit icmp any any
            30 permit ip host 10.34.2.2 host 10.2.54.2
            40 permit ip host 10.3.4.31 host 10.3.32.3 log
        Extended IP access lists 101
            10 permit ip host 10.3.3.3 host 10.5.5.34
            20 permit icmp any any
            30 permit ip host 10.34.2.2 host 10.2.54.2
            40 permit ip host 10.3.4.31 host 10.3.32.3 log
        ip access-lists extended 101
         20 permit udp host 10.1.1.1 host 10.2.2.2
        %Duplicate sequence number.
        Extended IP access lists 101
            10 permit ip host 10.3.3.3 host 10.5.5.34
            20 permit icmp any any
            30 permit ip host 10.34.2.2 host 10.2.54.2
            40 permit ip host 10.3.4.31 host 10.3.32.3 log
    '''}

    golden_parsed_output_duplicate = {
        "101": {
            "name": "101",
            "type": "ipv4-acl-type",
            "aces": {
                "10": {
                    "name": "10",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.0.0.0": {
                                        "source_network": "host 10.0.0.0"
                                    },
                                    "host 10.3.3.3": {
                                        "source_network": "host 10.3.3.3"
                                    }
                                },
                                "destination_network": {
                                    "host 10.5.5.34": {
                                        "destination_network": "host 10.5.5.34"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                },
                "20": {
                    "name": "20",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "icmp": {
                                "protocol": "icmp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                },
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                }
                            },
                            "udp": {
                                "protocol": "udp",
                                "source_network": {
                                    "host 10.1.1.1": {
                                        "source_network": "host 10.1.1.1"
                                    }
                                },
                                "destination_network": {
                                    "host 10.2.2.2": {
                                        "destination_network": "host 10.2.2.2"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "icmp": {
                                "established": False
                            },
                            "udp": {
                                "established": False
                            }
                        }
                    }
                },
                "30": {
                    "name": "30",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.0.0.0": {
                                        "source_network": "host 10.0.0.0"
                                    },
                                    "host 10.34.2.2": {
                                        "source_network": "host 10.34.2.2"
                                    }
                                },
                                "destination_network": {
                                    "host 10.2.54.2": {
                                        "destination_network": "host 10.2.54.2"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                },
                "40": {
                    "name": "40",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-syslog"
                    },
                    "matches": {
                        "l3": {
                            "ipv4": {
                                "protocol": "ipv4",
                                "source_network": {
                                    "host 10.0.0.0": {
                                        "source_network": "host 10.0.0.0"
                                    },
                                    "host 10.3.4.31": {
                                        "source_network": "host 10.3.4.31"
                                    }
                                },
                                "destination_network": {
                                    "host 10.3.32.3": {
                                        "destination_network": "host 10.3.32.3"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "ipv4": {
                                "established": False
                            }
                        }
                    }
                },
                "100": {
                    "name": "100",
                    "actions": {
                        "forwarding": "permit",
                        "logging": "log-none"
                    },
                    "matches": {
                        "l3": {
                            "icmp": {
                                "protocol": "icmp",
                                "source_network": {
                                    "any": {
                                        "source_network": "any"
                                    }
                                },
                                "destination_network": {
                                    "any": {
                                        "destination_network": "any"
                                    }
                                }
                            }
                        },
                        "l4": {
                            "icmp": {
                                "established": False
                            }
                        }
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessLists(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessLists(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_standard(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.golden_output_standard)
        obj = ShowAccessLists(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_standard)

    def test_golden_duplicate(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.golden_output_duplicate)
        obj = ShowAccessLists(device=self.dev1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_duplicate)


if __name__ == '__main__':
    unittest.main()

