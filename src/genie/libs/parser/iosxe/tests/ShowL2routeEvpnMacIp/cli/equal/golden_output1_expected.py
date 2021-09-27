# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                        1: {
                            "producer": {
                                "BGP": {
                                    "host_ip": {
                                        "192.168.11.254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr": {
                                                        "0011.0011.0011" : {
                                                            "next_hops": [
                                                                "V:20011 3.3.3.2",
                                                                "V:20011 4.4.4.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "2001:11::254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "0011.0011.0011" : {
                                                            "next_hops": [
                                                                "V:20011 3.3.3.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "192.168.11.31": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr": {
                                                        "aabb.0011.0031" : {
                                                            "next_hops": [
                                                                "V:20011 3.3.3.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "FE80::A8BB:FF:FE11:31": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "aabb.0011.0031" : {
                                                            "next_hops": [
                                                                "V:20011 3.3.3.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "L2VPN": {
                                    "host_ip": {
                                        "192.168.11.11": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr": {
                                                        "aabb.0011.0011": {
                                                            "next_hops": [
                                                                "Et0/1:11"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "FE80::A8BB:FF:FE11:11": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "aabb.0011.0011" : {
                                                            "next_hops": [
                                                                "Et0/1:11",
                                                                "V:20012 2.2.2.2",
                                                                "V:20011 4.4.4.2"
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
                            "producer": {
                                "BGP": {
                                    "host_ip": {
                                        "192.168.12.254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "0012.0012.0012" : {
                                                            "next_hops": [
                                                                "V:20012 3.3.3.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "2001:12::254": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "0012.0012.0012" : {
                                                            "next_hops": [
                                                                "V:20012 3.3.3.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "192.168.12.22": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "aabb.0012.0022" : {
                                                            "next_hops": [
                                                                "V:20012 2.2.2.2"
                                                            ]
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "FE80::A8BB:FF:FE12:22": {
                                            "eth_tag": {
                                                0 : {
                                                    "mac_addr" : {
                                                        "aabb.0012.0022" : {
                                                            "next_hops": [
                                                                "V:20012 2.2.2.2"
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