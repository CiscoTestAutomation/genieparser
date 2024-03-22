expected_output = {
  'sla_class': {
    'raghav_test_Bulk_Data': {
      'loss': 21,
      'latency': 300,
      'jitter': 100
    },
    'raghav_test_Default': {
      'loss': 18,
      'latency': 300,
      'jitter': 100,
      'fallback_best_tunnel': {
        'criteria': [
          'loss',
          'latency',
          'jitter'
        ],
        'loss_variance': 10,
        'latency_variance': 100,
        'jitter_variance': 200
      }
    }
  },
  'data_policy': {
    '_vpn_list_Site7_Data_Policy': {
      'direction': 'from-service',
      'vpn_list': {
        'vpn_11': {
          'sequence': {
            1: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'dscp': [
                  24
                ]
              },
              'action': {
                'accept': {
                  'count': 'DP_DSCP_24_Match_-2032887342',
                  'set': {
                    'local_tloc_list': {
                      'color': [
                        'public-internet',
                        'gold'
                      ],
                      'encap': 'ipsec',
                      'restrict': True
                    }
                  }
                }
              }
            },
            11: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'app_list': 'App_List'
              },
              'action': {
                'accept': {
                  'count': 'DP_APP_LIST_MATCH_-2032887342',
                  'set': {
                    'local_tloc_list': {
                      'color': [
                        'public-internet',
                        'gold'
                      ],
                      'encap': 'ipsec',
                      'restrict': True
                    }
                  }
                }
              }
            },
            21: {
              'match': {
                'source_data_prefix_list': 'site8_vpn11_ipv4'
              },
              'action': {
                'accept': {
                  'count': 'nat_vrf_11_-2032887342',
                  'nat': {
                    'pool': '11'
                  }
                }
              }
            },
            31: {
              'match': {
                'source_ip': '0.0.0.0/0'
              },
              'action': {
                'accept': {
                  'loss_protection': {
                    'forward_error_correction': 'always'
                  }
                }
              }
            }
          },
          'default_action': 'accept'
        },
        'vpn_23': {
          'sequence': {
            1: {
              'match': {
                'source_data_prefix_list': 'site1_vpn10_ipv4',
                'destination_data_prefix_list': 'site6_service_ipv4_red',
                'app_list': 'WEB_TOOLS_APP',
                'dns_app_list': 'Microsoft_Apps',
                'source_port': 1024,
                'destination_port': 8080,
                'protocol': [
                  '23',
                  '56',
                  '80'
                ],
                'dscp': [
                  14
                ],
                'tcp': 'syn',
                'plp': 'high',
                'traffic_to': 'core',
                'destination_region': 'primary-region',
                'packet_length': '1-4096',
                'dns': 'request'
              },
              'action': {
                'accept': {
                  'count': 'test_-1743798427',
                  'nat': {
                    'pool': '23'
                  },
                  'cflowd': True,
                  'set': {
                    'local_tloc_list': {
                      'color': [
                        'blue',
                        'bronze'
                      ],
                      'encap': 'ipsec'
                    },
                    'next_hop': '10.0.0.1',
                    'next_hop_loose': True,
                    'policer': 'site6_policer',
                    'dscp': [
                      45
                    ],
                    'forwarding_class': 'Net-Mgmt',
                    'vpn': 10,
                    'vip_tloc_pref_list': {
                      '0': {
                        'tloc': {
                          'label': 1002,
                          'ip': '8.8.8.1',
                          'color': 'public-internet',
                          'encap': 'ipsec'
                        }
                      },
                      '1': {
                        'tloc': {
                          'label': 1007,
                          'ip': '8.8.8.3',
                          'color': 'public-internet',
                          'encap': 'ipsec'
                        }
                      }
                    },
                    'tloc_list': [
                      'HUB2'
                    ]
                  }
                }
              }
            },
            11: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'app_list': 'APP_BULK_DATA',
                'dns_app_list': 'Microsoft_Apps'
              },
              'action': {
                'accept': {
                  'nat': {
                    'use_vpn': 0,
                    'fallback': True
                  },
                  'log': True,
                  'tcp_optimization': True,
                  'loss_protection': {
                    'forward_error_correction': 'adaptive'
                  },
                  'redirect_dns': 'umbrella',
                  'set': {
                    'next_hop': '10.0.0.1',
                    'service': {
                      'name': 'FW',
                      'vpn': 23,
                      'tloc': {
                        'ip': '10.101.7.2',
                        'color': [
                          'public-internet'
                        ],
                        'encap': 'ipsec'
                      }
                    }
                  }
                }
              }
            },
            21: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'destination_ip': '0.0.0.0/0',
                'dscp': [
                  15
                ],
                'destination_region': 'secondary-region'
              },
              'action': {
                'accept': {
                  'loss_protection': {
                    'forward_error_correction': 'always'
                  },
                  'set': {
                    'vip_tloc_pref_list': {
                      '0': {
                        'tloc': {
                          'ip': '8.8.8.1',
                          'color': 'public-internet',
                          'encap': 'ipsec'
                        }
                      },
                      '1': {
                        'tloc': {
                          'ip': '8.8.8.3',
                          'color': 'public-internet',
                          'encap': 'ipsec'
                        }
                      }
                    },
                    'service': {
                      'name': 'IDP',
                      'vpn': 11,
                      'tloc_list': [
                        'HUB2'
                      ]
                    }
                  }
                }
              }
            },
            31: {
              'match': {
                'source_ip': '10.10.2.0/24',
                'traffic_to': 'service',
                'destination_region': 'other-region'
              },
              'action': {
                'accept': {
                  'loss_protection': {
                    'packet_duplication': True
                  },
                  'set': {
                    'service': {
                      'name': 'appqoe',
                      'vpn': 11,
                      'tloc': {
                        'ip': '10.102.7.2',
                        'color': [
                          '3g'
                        ],
                        'encap': 'ipsec'
                      }
                    }
                  }
                }
              }
            },
            41: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'dns_app_list': 'Telnet',
                'source_port': 1024,
                'traffic_to': 'access',
                'destination_region': 'other-region'
              },
              'action': {
                'accept': {
                  'redirect_dns': 'host'
                }
              }
            }
          },
          'default_action': 'accept'
        }
      }
    }
  },
  'cflowd_template': {
    'cflowd_test': {
      'flow_active_timeout': 600,
      'flow_inactive_timeout': 60,
      'template_refresh': 600,
      'flow_sampling_interval': 1,
      'protocol': [
        'ipv4'
      ],
      'customized_ipv4_record_fields': {
        'collect_tos': True,
        'collect_dscp_output': False
      },
      'collector': {
        'vpn': {
          '10': {
            'address': '10.0.0.1',
            'port': 1024,
            'transport': 'transport_udp',
            'source_interface': 'GigabitEthernet0/0/0'
          }
        }
      }
    }
  },
  'app_route_policy': {
    '_vpn_23_Site7_AAR_Policy': {
      'vpn_list': {
        'vpn_10': {
          'sequence': {
            1: {
              'match': {
                'source_data_prefix_list': 'site1_vpn10_ipv4',
                'destination_ip': '10.99.99.0/24',
                'app_list': 'raghav-ops-admin-mgmt',
                'dns_app_list': 'Google_Apps',
                'source_port': 1024,
                'destination_port': 5676,
                'protocol': [
                  '34',
                  '56',
                  '87'
                ],
                'dscp': [
                  11,
                  12,
                  13,
                  14
                ],
                'plp': 'low',
                'traffic_to': 'access',
                'destination_region': 'primary-region',
                'dns': 'request'
              },
              'action': {
                'count': 'testing-counter_-2070586118',
                'log': True,
                'backup_sla_preferred_color': 'bronze',
                'sla_class': {
                  'types': [
                    'raghav-test-Bulk-Data'
                  ],
                  'preferred_color': [
                    'biz-internet',
                    'custom1'
                  ]
                }
              }
            },
            11: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'app_list': 'Google_Apps',
                'dscp': [
                  11,
                  12,
                  13
                ]
              },
              'action': {
                'sla_class': {
                  'types': [
                    'raghav-test-Bulk-Data',
                    'strict'
                  ],
                  'preferred_color': [
                    'biz-internet',
                    'custom1'
                  ]
                }
              }
            },
            21: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'cloud_saas_app_list': 'gotomeeting_apps'
              },
              'action': {
                'cloud_saas': 'allow-local'
              }
            },
            31: {
              'match': {
                'source_ip': '0.0.0.0/0',
                'app_list': 'Google_Apps'
              },
              'action': {
                'sla_class': {
                  'types': [
                    'raghav-test-Default',
                    'fallback-to-best-path'
                  ],
                  'preferred_color': [
                    'blue',
                    'gold',
                    'custom1'
                  ]
                }
              }
            }
          }
        }
      }
    }
  },
  'policer': {
    'site6_policer': {
      'rate': 3000000,
      'burst': 150000,
      'exceed': 'drop'
    }
  },
  'lists': {
    'vpn_list': {
      'vpn_10': {
        'vpn': 10
      },
      'vpn_11': {
        'vpn': 11
      },
      'vpn_23': {
        'vpn': 23
      }
    },
    'app_list': {
      'APP_BULK_DATA': {
        'app': [
          'cisco-jabber-im',
          'ftp',
          'ftp-data',
          'ftp_data',
          'jabber',
          'netblt',
          'rsync'
        ]
      },
      'App_List': {
        'app_family': [
          'app-fam-2',
          'application-service',
          'application_service',
          'audio-video',
          'audio_video',
          'behavioral',
          'database',
          'encrypted',
          'erp',
          'file-transfer',
          'file_server',
          'file_transfer',
          'game',
          'instant-messaging',
          'mail',
          'microsoft-office',
          'microsoft_office',
          'middleware',
          'network-management',
          'network-service',
          'network_management',
          'network_service',
          'peer-to-peer',
          'peer_to_peer',
          'printer',
          'security-service',
          'security_service',
          'terminal',
          'thin-client',
          'thin_client',
          'tunneling',
          'web',
          'webmail'
        ]
      },
      'Google_Apps': {
        'app': [
          'android-updates',
          'blogger',
          'chrome_update',
          'gcs',
          'gmail',
          'gmail_basic',
          'gmail_chat',
          'gmail_drive',
          'gmail_mobile',
          'google',
          'google-docs',
          'google-downloads',
          'google-earth',
          'google-photos',
          'google-play',
          'google-plus',
          'google-services',
          'google-services-audio',
          'google-services-media',
          'google-services-video',
          'google_accounts',
          'google_ads',
          'google_analytics',
          'google_appengine',
          'google_cache',
          'google_calendar',
          'google_classroom',
          'google_code',
          'google_desktop',
          'google_docs',
          'google_earth',
          'google_gen',
          'google_groups',
          'google_localguides',
          'google_maps',
          'google_photos',
          'google_picasa',
          'google_play',
          'google_play_music',
          'google_plus',
          'google_safebrowsing',
          'google_skymap',
          'google_spaces',
          'google_sprayscape',
          'google_tags',
          'google_toolbar',
          'google_translate',
          'google_trusted_store',
          'google_weblight',
          'googlebot',
          'gstatic',
          'gtalk',
          'gtalk-chat',
          'gtalk-ft',
          'gtalk-video',
          'gtalk-voip',
          'hangouts',
          'hangouts-audio',
          'hangouts-chat',
          'hangouts-file-transfer',
          'hangouts-media',
          'hangouts-video',
          'picasa',
          'youtube',
          'youtube_hd',
          'ytimg'
        ]
      },
      'Microsoft_Apps': {
        'app': [
          'bing',
          'excel_online',
          'groove',
          'hockeyapp',
          'live_groups',
          'live_hotmail',
          'live_mesh',
          'live_storage',
          'livemail_mobile',
          'lync',
          'lync_online',
          'microsoft',
          'ms-lync',
          'ms-lync-audio',
          'ms-lync-control',
          'ms-lync-video',
          'ms-office-365',
          'ms-office-web-apps',
          'ms-services',
          'ms-update',
          'ms_communicator',
          'ms_onenote',
          'ms_planner',
          'ms_sway',
          'ms_translator',
          'office365',
          'office_docs',
          'onedrive',
          'outlook',
          'outlook-web-service',
          'owa',
          'powerpoint_online',
          'share-point',
          'sharepoint',
          'sharepoint_admin',
          'sharepoint_blog',
          'sharepoint_calendar',
          'sharepoint_document',
          'sharepoint_online',
          'skydrive',
          'skydrive_login',
          'skype',
          'windows-azure',
          'windows_azure',
          'windows_marketplace',
          'windows_update',
          'windowslive',
          'windowslivespace',
          'windowsmedia',
          'word_online',
          'xbox',
          'xbox_music',
          'xbox_video',
          'xboxlive',
          'xboxlive_marketplace',
          'yammer'
        ]
      },
      'Telnet': {
        'app': [
          'telnet',
          'tnvip'
        ]
      },
      'WEB_TOOLS_APP': {
        'app': [
          'http',
          'https',
          'ssh',
          'sshell'
        ]
      },
      'gotomeeting_apps': {
        'app': [
          'citrix',
          'citrix_online',
          'citrix_pvs',
          'gotomeeting',
          'ica',
          'jedi'
        ]
      },
      'raghav_ops_admin_mgmt': {
        'app': [
          '914c/g',
          'acap',
          'active-directory',
          'agentx',
          'alpes',
          'aminet',
          'aruba-papi',
          'asip-webadmin',
          'asipregistry',
          'at-echo',
          'at-nbp',
          'at-zis',
          'auditd',
          'auth',
          'auth-service',
          'bacnet',
          'bacnet_vlc',
          'bb',
          'cdc',
          'chargen',
          'chshell',
          'cisco-controller',
          'cisco-cta',
          'cisco-fna',
          'cisco-nac',
          'cisco-rtmt',
          'cisco-sd-avc',
          'cisco-stealthwatch',
          'cisco-sys',
          'cisco-tna',
          'cisco_sdavc',
          'cmip-agent',
          'cmip-man',
          'codaauth2',
          'compressnet',
          'cpq-wbem',
          'crs',
          'cryptoadmin',
          'csnet-ns',
          'ctf',
          'cvc_hostd',
          'cycleserv',
          'cycleserv2',
          'daytime',
          'dcp',
          'decauth',
          'decvms-sysmgt',
          'dhcp',
          'dhcp-failover',
          'dhcp-failover2',
          'dhcp6',
          'dhcpv6',
          'dhcpv6-client',
          'dhcpv6-server',
          'dn6-nlm-aud',
          'dns',
          'dnsix',
          'echo',
          'elcsd',
          'entrust-aaas',
          'entrust-aams',
          'entrust-ash',
          'entrust-kmsh',
          'entrust-sps',
          'exec',
          'fcp',
          'finger',
          'fln-spx',
          'gkrellm',
          'go-login',
          'gss-http',
          'ha-cluster',
          'hassle',
          'hdap',
          'hello-port',
          'hmmp-ind',
          'hmmp-op',
          'hostname',
          'hp-alarm-mgr',
          'hp-collector',
          'hp-managed-node',
          'http-mgmt',
          'icmp',
          'icmp6',
          'ident',
          'igmp',
          'ipcserver',
          'ipfix',
          'ipv6-icmp',
          'ipx_in_ip',
          'iso-tsap',
          'kerberos',
          'kerberos-adm',
          'keyserver',
          'klogin',
          'kpasswd',
          'krb5',
          'kshell',
          'lanserver',
          'ldap',
          'ldaps',
          'llmnr',
          'locus-con',
          'locus-map',
          'login',
          'mac-srvr-admin',
          'masqdialer',
          'mdns',
          'micromuse-lm',
          'monitor',
          'mptn',
          'mrm',
          'ms-netlogon',
          'ms-win-dns',
          'msft-gc',
          'msft-gc-ssl',
          'name',
          'nas',
          'nbns',
          'ncp',
          'ndsauth',
          'nest-protocol',
          'netbios-dgm',
          'netbios-ns',
          'netbios-ssn',
          'netflow',
          'netrjs-1',
          'netrjs-2',
          'netrjs-3',
          'netrjs-4',
          'netviewdm1',
          'netviewdm2',
          'netviewdm3',
          'netware-ip',
          'new-rwho',
          'nextstep',
          'nicname',
          'nlogin',
          'nmap',
          'novadigm',
          'npmp-gui',
          'npmp-local',
          'npmp-trap',
          'nqs',
          'nsiiops',
          'nsrmp',
          'ntp',
          'nxedit',
          'opalis-robot',
          'osu-nms',
          'passgo',
          'passgo-tivoli',
          'password-chg',
          'photuris',
          'ping',
          'pkix-3-ca-ra',
          'pkix-timestamp',
          'ptp-event',
          'purenoise',
          'pwdgen',
          'qbikgdp',
          'quotad',
          'radius',
          'rescap',
          'rje',
          'rlogin',
          'rlp',
          'rmonitor',
          'rmt',
          'rrp',
          'rsh',
          'rsh-spx',
          'rsvp',
          'rsvp-encap-1',
          'rsvp-encap-2',
          'rtelnet',
          'sco-dtmgr',
          'sco-inetmgr',
          'sco-sysmgr',
          'sco-websrvrmg3',
          'sco-websrvrmgr',
          'sdnskmp',
          'secure-ldap',
          'secure-telnet',
          'server-ipx',
          'sgmp',
          'sgmp-traps',
          'shell',
          'shrinkwrap',
          'smsp',
          'snare',
          'snmp',
          'sntp-heartbeat',
          'src',
          'srmp',
          'ssh',
          'sshell',
          'statsrv',
          'stuns',
          'sun-dr',
          'supdup',
          'synoptics-trap',
          'synotics-broker',
          'synotics-relay',
          'syslog',
          'systat',
          'tacacs',
          'tacacs_plus',
          'telnet',
          'telnets',
          'time',
          'timed',
          'tnvip',
          'traceroute-linux',
          'ulp',
          'urm',
          'utime',
          'uucp',
          'uucp-rlogin',
          'websense',
          'whoami',
          'whois',
          'whois++',
          'wins',
          'x-bone-ctl',
          'xdmcp',
          'xns',
          'xns-auth',
          'xns-ch',
          'xns-time'
        ]
      }
    },
    'data_prefix_list': {
      'site1_vpn10_ipv4': {
        'ip_prefix': '10.10.1.0/24'
      },
      'site6_service_ipv4_red': {
        'ip_prefix': '10.10.6.32/27'
      },
      'site8_vpn11_ipv4': {
        'ip_prefix': '10.11.8.0/24'
      }
    },
    'tloc_list': {
      'HUB2': {
        'tloc': {
          '8.8.8.1': {
            'color': 'public-internet',
            'encap': 'ipsec'
          },
          '8.8.8.3': {
            'color': 'public-internet',
            'encap': 'ipsec'
          }
        }
      }
    },
    'preferred_color_group': {
      'color_list': {
        'primary_preference': {
          'color_preference': 'biz-internet',
          'path_preference': 'direct-path'
        },
        'secondary_preference': {
          'color_preference': 'bronze',
          'path_preference': 'multi-hop-path'
        },
        'tertiary_preference': {
          'color_preference': 'custom1'
        }
      }
    }
  }
}
