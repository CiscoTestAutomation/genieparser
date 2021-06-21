expected_output = {
    'version': {
        'asa_version': '8.4(1)',
        'asdm_version': '6.4(1)',
        'bios_flash': 'AT49LW080 @ 0xfff00000, 1024KB',
        'system_image': 'disk0:/cdisk.bin',
        'boot_config_file': 'disk0:/tomm_backup.cfg',
        'compiled_by': 'builders',
        'compiled_date': 'Thu 20-Jan-12 04:05',
        'platform': 'ASA5520',
        'mem_size': '512 MB',
        'processor_type': 'Pentium 4 Celeron 2000 MHz',
        'disks': {
            'Internal': {
                'type_of_disk': 'ATA Compact Flash',
                'disk_size': '64MB'
            },
            'Slot 1': {
                'disk_size': '128MB',
                'type_of_disk': 'ATA Compact Flash'
            }
        },
        'encryption_hardware': {
            'encryption_device': 'Cisco ASA-55x0 on-board accelerator (revision 0x0)',
            'boot_microcode': 'CN1000-MC-BOOT-2.00',
            'ssl_ike_microcode': 'CNLite-MC-SSLm-PLUS-2.03',
            'ipsec_microcode': 'CNlite-MC-IPSECm-MAIN-2.06',
        },
        'hostname': 'asa3',
        'uptime': '3 days 3 hours',
        'interfaces': {
            '0': {
                'interface': 'GigabitEthernet0/0',
                'intf_irq': 9,
                'mac_addr': '0013.c480.82ce'
            },
            '1': {
                'interface': 'GigabitEthernet0/1',
                'intf_irq': 9,
                'mac_addr': '0013.c480.82cf'
            },
            '2': {
                'interface': 'GigabitEthernet0/2',
                'intf_irq': 9,
                'mac_addr': '0013.c480.82d0'
            },
            '3': {
                'interface': 'GigabitEthernet0/3',
                'intf_irq': 9,
                'mac_addr': '0013.c480.82d1'
            },
            '4': {
                'interface': 'Management0/0',
                'intf_irq': 11,
                'mac_addr': '0013.c480.82cd'
            },
            '5': {
                'interface': 'Not used',
                'intf_irq': 11
            },
            '6': {
                'interface': 'Not used',
                'intf_irq': 5
            },
        },
        'licensed_features': {
            'max_physical_interfaces': 'Unlimited',
            'max_vlans': 150,
            'inside_hosts': 'Unlimited',
            'failover': 'Active/Active',
            'crypto_des': 'Enabled',
            'crypto_3des_aes': 'Enabled',
            'security_contexts': 10,
            'gtp_gprs': 'Enabled',
            'anyconnect_essentials': 'Disabled',
            'anyconnect_premium_peers': 2,
            'other_vpn_peers': 750,
            'total_vpn_peers': 750,
            'shared_license': 'Enabled',
            'shared_anyconnect_premium_peers': 12000,
            'anyconnect_for_mobile': 'Disabled',
            'anyconnect_for_cisco_vpn_phone': 'Disabled',
            'advanced_endpoint_assessment': 'Disabled',
            'uc_phone_proxy_sessions': 12,
            'total_uc_proxy_sessions': 12,
            'botnet_traffic_filter': 'Enabled',
            'intercompany_media_engine': 'Disabled'
        },
        'serial_number': 'JMX0938K0C0',
        'last_modified_by': 'docs',
        'last_modified_date': '15:23:22.339 EDT Fri Oct 30 2012',
    }
}
