expected_output = {
   "vrf": {
      "**VRF_Name_01": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "local": {
                     "routes": 2,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 320
                  },
                  "connected": {
                     "routes": 0,
                     "backup": 2,
                     "deleted": 0,
                     "memory_bytes": 320
                  }
               },
               "total_route_source": {
                  "routes": 2,
                  "backup": 2,
                  "deleted": 0,
                  "memory_bytes": 640
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_02": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "static": {
                     "routes": 50,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 8000
                  },
                  "bgp": {
                     "111": {
                        "routes": 4,
                        "backup": 20,
                        "deleted": 0,
                        "memory_bytes": 3840
                     }
                  },
                  "connected": {
                     "routes": 2,
                     "backup": 1,
                     "deleted": 0,
                     "memory_bytes": 480
                  },
                  "local": {
                     "routes": 3,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 480
                  },
                  "ospf": {
                     "13": {
                        "routes": 554,
                        "backup": 46,
                        "deleted": 0,
                        "memory_bytes": 96000
                     }
                  },
                  "dagr": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 613,
                  "backup": 67,
                  "deleted": 0,
                  "memory_bytes": 108800
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_04": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 75,
                        "backup": 1,
                        "deleted": 0,
                        "memory_bytes": 12160
                     }
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "ospf": {
                     "13": {
                        "routes": 0,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 0
                     }
                  }
               },
               "total_route_source": {
                  "routes": 78,
                  "backup": 1,
                  "deleted": 0,
                  "memory_bytes": 12640
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_05": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 2,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 320
                  },
                  "bgp": {
                     "111": {
                        "routes": 74,
                        "backup": 1,
                        "deleted": 0,
                        "memory_bytes": 12000
                     }
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 2,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 320
                  },
                  "ospf": {
                     "13": {
                        "routes": 0,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 0
                     }
                  },
                  "dagr": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 79,
                  "backup": 1,
                  "deleted": 0,
                  "memory_bytes": 12800
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_06": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "dagr": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "bgp": {
                     "111": {
                        "routes": 49,
                        "backup": 1,
                        "deleted": 0,
                        "memory_bytes": 8000
                     }
                  }
               },
               "total_route_source": {
                  "routes": 51,
                  "backup": 1,
                  "deleted": 0,
                  "memory_bytes": 8320
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_07": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "dagr": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "bgp": {
                     "111": {
                        "routes": 15,
                        "backup": 1,
                        "deleted": 0,
                        "memory_bytes": 2560
                     }
                  }
               },
               "total_route_source": {
                  "routes": 17,
                  "backup": 1,
                  "deleted": 0,
                  "memory_bytes": 2880
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_08": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "ospf": {
                     "13": {
                        "routes": 0,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 0
                     }
                  },
                  "bgp": {
                     "111": {
                        "routes": 75,
                        "backup": 1,
                        "deleted": 0,
                        "memory_bytes": 12160
                     }
                  }
               },
               "total_route_source": {
                  "routes": 78,
                  "backup": 1,
                  "deleted": 0,
                  "memory_bytes": 12640
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_09": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 49,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 7840
                     }
                  }
               },
               "total_route_source": {
                  "routes": 52,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 8320
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_10": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 15,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 2400
                     }
                  }
               },
               "total_route_source": {
                  "routes": 18,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 2880
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_11": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 49,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 7840
                     }
                  }
               },
               "total_route_source": {
                  "routes": 52,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 8320
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_12": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 15,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 2400
                     }
                  }
               },
               "total_route_source": {
                  "routes": 18,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 2880
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_13": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 49,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 7840
                     }
                  }
               },
               "total_route_source": {
                  "routes": 52,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 8320
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_14": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 15,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 2400
                     }
                  }
               },
               "total_route_source": {
                  "routes": 18,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 2880
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_15": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 49,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 7840
                     }
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  }
               },
               "total_route_source": {
                  "routes": 52,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 8320
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      },
      "VRF_Name_16": {
         "address_family": {
            "IPv4 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "local": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "static": {
                     "routes": 1,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 160
                  },
                  "bgp": {
                     "111": {
                        "routes": 15,
                        "backup": 0,
                        "deleted": 0,
                        "memory_bytes": 2400
                     }
                  }
               },
               "total_route_source": {
                  "routes": 18,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 2880
               }
            },
            "IPv6 Unicast": {
               "route_source": {
                  "connected": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  },
                  "local": {
                     "routes": 0,
                     "backup": 0,
                     "deleted": 0,
                     "memory_bytes": 0
                  }
               },
               "total_route_source": {
                  "routes": 0,
                  "backup": 0,
                  "deleted": 0,
                  "memory_bytes": 0
               }
            }
         }
      }
   }
}
