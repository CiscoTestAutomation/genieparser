''' show_version.py

Parser for the following show commands:
    * show version
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use

# =============================================
# Schema for 'show version'
# =============================================
class ShowVersionSchema(MetaParser):
    """Schema for
        * show version
    """

    schema = {
        'version': {
            'hostname': str,
            'uptime': str,
            'asa_version': str,
            'firepower_version': str,
            'asdm_version': str,
            'compiled_date': str,
            'compiled_by': str,
            'system_image': str,
            'boot_config_file': str,
            'platform': str,
            'mem_size': str,
            'processor_type': str,
            'asa_model': str,
            'bios_flash_firmware': str,
            Optional('disks'): {
                Any(): {
                    Optional('disk_size'): str,
                    Optional('type_of_disk'): str,
                }
            },
            Optional('interfaces'): {
                Any(): {
                    Optional('interface'): str,
                    Optional('mac_addr'): str,
                    Optional('intf_irq'): str,
                }
            },
            'license_mode': str,
            'license_state': str,
            'entitlement': str,
            'mem_allocation': str,
            Optional('licensed_features'): {
                Optional('max_vlans'): int,
                Optional('inside_hosts'): str,
                Optional('failover'): str,
                Optional('crypto_des'): str,
                Optional('crypto_3des_aes'): str,
                Optional('security_contexts'): int,
                Optional('carrier'): str,
                Optional('anyconnect_premium_peers'): int,
                Optional('anyconnect_essentials'): str,
                Optional('other_vpn_peers'): int,
                Optional('total_vpn_peers'): int,
                Optional('anyconnect_for_mobile'): str,
                Optional('anyconnect_for_cisco_vpn_phone'): str,
                Optional('advanced_endpoint_assessment'): str,
                Optional('shared_license'): str,
                Optional('total_tls_proxy_sessions'): int,
                Optional('botnet_traffic_filter'): str,
                Optional('cluster'): str,
            },
            'serial_number': str,
            'image_type': str,
            'key_version': str,
            'last_modified_by': str,
            'last_modified_date': str
        }
    }

# =============================================
# Parser for 'show version'
# =============================================
class ShowVersion(ShowVersionSchema):
    """Parser for
        * show version
    """

    cli_command = 'show version'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        version_dict = {}

        # Cisco Adaptive Security Appliance Software Version 9.8(4)10
        p0 = re.compile(r'^.+ Software Version (?P<asa_version>[\S]+)')

        # Firepower Extensible Operating System Version 2.2(2.121)
        p1 = re.compile(r'^.+System Version (?P<firepower_version>[\S]+)')

        # Device Manager Version 7.8(2)
        p2 = re.compile(r'^.+Manager Version (?P<asdm_version>[\S]+)')

        # Compiled on Tue 20-Aug-19 12:46 PDT by builders
        p3 = re.compile(
            r'^Compiled on (?P<compiled_date>\w{3} \S+ \d{1,2}:\d{1,2} \w{3}) by (?P<compiled_by>\w+)')

        # System image file is "boot:/asa984-10-smp-k8.bin"
        p4 = re.compile(r'^System image.+"(?P<system_image>\S+)"')

        # Config file at boot was "startup-config"
        p5 = re.compile(r'^Config file.+"(?P<boot_config_file>\S+)"')

        # ciscoasa up 1 day 12 hours
        p6 = re.compile(r'^(?P<hostname>\S+) up (?P<uptime>.+)')

        # Hardware:   ASAv, 2048 MB RAM, CPU Xeon E5 series 3491 MHz
        p7 = re.compile(r'^Hardware:\s+(?P<platform>\S+),'
                        r'\s+(?P<mem_size>[\w\s]+) RAM,'
                        r'\s+CPU (?P<processor_type>[\w\s]+)')

        # Model Id:   ASAv10
        p8 = re.compile(r'^Model Id:\s*(?P<asa_model>\S+)')

        # Internal ATA Compact Flash, 8192MB
        # Slot 1: ATA Compact Flash, 8192MB
        p9 = re.compile(r'^(?P<disks>\S+|Slot \d+):? '
                        r'(?P<type_of_disk>[\w\s]+), '
                        r'(?P<disk_size>\S+)')

        # BIOS Flash Firmware Hub @ 0x0, 0KB
        p10 = re.compile(r'^BIOS Flash Firmware (?P<bios_flash_firmware>.+)')

        # 0: Ext: Management0/0       : address is 5001.0003.0000, irq 11
        # 1: Ext: GigabitEthernet0/0  : address is 5001.0003.0001, irq 11
        # 2: Ext: GigabitEthernet0/1  : address is 5001.0003.0002, irq 10
        # 3: Ext: GigabitEthernet0/2  : address is 5001.0003.0003, irq 10
        # 4: Ext: GigabitEthernet0/3  : address is 5001.0003.0004, irq 11
        # 5: Ext: GigabitEthernet0/4  : address is 5001.0003.0005, irq 11
        # 6: Ext: GigabitEthernet0/5  : address is 5001.0003.0006, irq 10
        # 7: Ext: GigabitEthernet0/6  : address is 5001.0003.0007, irq 10
        p11 = re.compile(r'^\s*(?P<intf_number>\d+): '
                         r'Ext: (?P<interface>[\w\/\.\-]+)\s*: address is '
                         r'(?P<mac_addr>[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}), '
                         r'irq (?P<intf_irq>\d{1,2})')

        # License mode: Smart Licensing
        p12 = re.compile(r'^License mode: (?P<license_mode>.+)')

        # ASAv Platform License State: Unlicensed
        p13 = re.compile(r'^.+License State: (?P<license_state>.+)')

        # No active entitlement: no feature tier and no throughput level configured
        p14 = re.compile(r'^.+entitlement: (?P<entitlement>.+)')

        # *Memory resource allocation is more than the permitted limit.
        p15 = re.compile(r'^(?P<mem_allocation>\*Memory.+)')

        p16 = re.compile(r'^Maximum [Vv][Ll][Aa][Nn][Ss]\s*: (?P<max_vlans>\d+)')

        p17 = re.compile(r'^Inside [Hh]osts\s*: (?P<inside_hosts>\S+)')

        p18 = re.compile(r'^Failover\s*: (?P<failover>\S+)')

        p19 = re.compile(r'^Encryption-DES\s*: (?P<crypto_des>\S+)')

        p20 = re.compile(r'^Encryption-3DES-AES\s*: (?P<crypto_3des_aes>\S+)')

        p21 = re.compile(r'^Security Contexts\s*: (?P<security_contexts>\d+)')

        p22 = re.compile(r'^Carrier\s*: (?P<carrier>\S+)')

        p23 = re.compile(r'^Any[Cc]onnect Premium Peers\s*: (?P<anyconnect_premium_peers>\d+)')

        p24 = re.compile(r'^Any[Cc]onnect Essentials\s*: (?P<anyconnect_essentials>\S+)')

        p25 = re.compile(r'^Other VPN Peers\s*: (?P<other_vpn_peers>\d+)')

        p26 = re.compile(r'^Total VPN Peers\s*: (?P<total_vpn_peers>\d+)')

        p27 = re.compile(r'^Any[Cc]onnect for Mobile\s*: (?P<anyconnect_for_mobile>\S+)')

        p28 = re.compile(r'^Any[Cc]onnect for Cisco VPN Phone\s*: (?P<anyconnect_for_cisco_vpn_phone>\S+)')

        p29 = re.compile(r'^Advanced Endpoint Assessment\s*: (?P<advanced_endpoint_assessment>\S+)')

        p30 = re.compile(r'^Shared License\s*: (?P<shared_license>\S+)')

        p31 = re.compile(r'^Total TLS Proxy Sessions\s*: (?P<total_tls_proxy_sessions>\d+)')

        p32 = re.compile(r'^Botnet Traffic Filter\s*: (?P<botnet_traffic_filter>\S+)')

        p33 = re.compile(r'^Cluster\s*: (?P<cluster>\S+)')

        p34 = re.compile(r'^Serial.+: (?P<serial_number>\S+)')

        p35 = re.compile(r'^Image type\s*: (?P<image_type>\S+)')

        p36 = re.compile(r'^Key version\s*: (?P<key_version>\S+)')

        p37 = re.compile(r'^Configuration last.+by (?P<last_modified_by>\S+) at '
                         r'(?P<last_modified_date>[\d:\.]+.+)')

        for line in out.splitlines():
            line = line.strip()

            # Cisco Adaptive Security Appliance Software Version 9.8(4)10
            m = p0.match(line)
            if m:
                if 'version' not in version_dict:
                    version_dict['version'] = {}
                asa_version = m.groupdict()['asa_version']
                # 9.8(4)10
                version_dict['version']['asa_version'] = asa_version
                continue

            # Firepower Extensible Operating System Version 2.2(2.121)
            m = p1.match(line)
            if m:
                firepower_version = m.groupdict()['firepower_version']
                version_dict['version']['firepower_version'] = firepower_version
                continue

            # Device Manager Version 7.8(2)
            m = p2.match(line)
            if m:
                asdm_version = m.groupdict()['asdm_version']
                version_dict['version']['asdm_version'] = asdm_version
                continue

            # Compiled on Tue 20-Aug-19 12:46 PDT by builders
            m = p3.match(line)
            if m:
                compiled_date = m.groupdict()['compiled_date']
                compiled_by = m.groupdict()['compiled_by']
                version_dict['version']['compiled_date'] = compiled_date
                version_dict['version']['compiled_by'] = compiled_by
                continue

            # System image file is "boot:/asa984-10-smp-k8.bin"
            m = p4.match(line)
            if m:
                system_image = m.groupdict()['system_image']
                version_dict['version']['system_image'] = system_image
                continue

            # Config file at boot was "startup-config"
            m = p5.match(line)
            if m:
                boot_config_file = m.groupdict()['boot_config_file']
                version_dict['version']['boot_config_file'] = boot_config_file
                continue

            # ciscoasa up 1 day 12 hours
            m = p6.match(line)
            if m:
                hostname = m.groupdict()['hostname']
                uptime = m.groupdict()['uptime']
                version_dict['version']['hostname'] = hostname
                version_dict['version']['uptime'] = uptime
                continue

            # Hardware:   ASAv, 2048 MB RAM, CPU Xeon E5 series 3491 MHz
            m = p7.match(line)
            if m:
                platform = m.groupdict()['platform']
                mem_size = m.groupdict()['mem_size']
                processor_type = m.groupdict()['processor_type']
                version_dict['version']['platform'] = platform
                version_dict['version']['mem_size'] = mem_size
                version_dict['version']['processor_type'] = processor_type
                continue

            # Model Id:   ASAv10
            m = p8.match(line)
            if m:
                asa_model = m.groupdict()['asa_model']
                version_dict['version']['asa_model'] = asa_model
                continue

            # Internal ATA Compact Flash, 8192MB
            # Slot 1: ATA Compact Flash, 8192MB
            m = p9.match(line)
            if m:
                disks = m.groupdict()['disks']
                if 'disks' not in version_dict['version']:
                    version_dict['version']['disks'] = {}
                if disks not in version_dict['version']['disks']:
                    version_dict['version']['disks'][disks] = {}
                version_dict['version']['disks'][disks]['disk_size'] = \
                        m.groupdict()['disk_size']
                version_dict['version']['disks'][disks]['type_of_disk'] = \
                        m.groupdict()['type_of_disk']
                continue

            # BIOS Flash Firmware Hub @ 0x0, 0KB
            m = p10.match(line)
            if m:
                bios_flash_firmware = m.groupdict()['bios_flash_firmware']
                version_dict['version']['bios_flash_firmware'] = bios_flash_firmware


            # 0: Ext: Management0/0       : address is 5001.0003.0000, irq 11
            # 1: Ext: GigabitEthernet0/0  : address is 5001.0003.0001, irq 11
            # 2: Ext: GigabitEthernet0/1  : address is 5001.0003.0002, irq 10
            # 3: Ext: GigabitEthernet0/2  : address is 5001.0003.0003, irq 10
            # 4: Ext: GigabitEthernet0/3  : address is 5001.0003.0004, irq 11
            # 5: Ext: GigabitEthernet0/4  : address is 5001.0003.0005, irq 11
            # 6: Ext: GigabitEthernet0/5  : address is 5001.0003.0006, irq 10
            # 7: Ext: GigabitEthernet0/6  : address is 5001.0003.0007, irq 10
            m = p11.match(line)
            if m:
                intf_number = m.groupdict()['intf_number']
                if 'interfaces' not in version_dict['version']:
                    version_dict['version']['interfaces'] = {}
                if intf_number not in version_dict['version']['interfaces']:
                    version_dict['version']['interfaces'][intf_number] = {}
                version_dict['version']['interfaces'][intf_number]['interface'] = \
                        m.groupdict()['interface']
                version_dict['version']['interfaces'][intf_number]['mac_addr'] = \
                        m.groupdict()['mac_addr']
                version_dict['version']['interfaces'][intf_number]['intf_irq'] = \
                        m.groupdict()['intf_irq']
                continue
            
            # License mode: Smart Licensing
            m = p12.match(line)
            if m:
                license_mode = m.groupdict()['license_mode']
                version_dict['version']['license_mode'] = license_mode
                continue

            # ASAv Platform License State: Unlicensed
            m = p13.match(line)
            if m:
                license_state = m.groupdict()['license_state']
                version_dict['version']['license_state'] = license_state
                continue

            # No active entitlement: no feature tier and no throughput level configured
            m = p14.match(line)
            if m:
                entitlement = m.groupdict()['entitlement']
                version_dict['version']['entitlement'] = entitlement
                continue

            # *Memory resource allocation is more than the permitted limit.
            m = p15.match(line)
            if m:
                mem_allocation = m.groupdict()['mem_allocation']
                version_dict['version']['mem_allocation'] = mem_allocation
                continue

            m = p16.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['max_vlans'] = \
                        int(m.groupdict()['max_vlans'])
                continue

            m = p17.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['inside_hosts'] = \
                        m.groupdict()['inside_hosts']

            m = p18.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['failover'] = \
                        m.groupdict()['failover']
                continue

            m = p19.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['crypto_des'] = \
                        m.groupdict()['crypto_des']
                continue

            m = p20.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['crypto_3des_aes'] = \
                        m.groupdict()['crypto_3des_aes']
                continue

            m = p21.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['security_contexts'] = \
                        int(m.groupdict()['security_contexts'])
                continue

            m = p22.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['carrier'] = \
                        m.groupdict()['carrier']
                continue

            m = p23.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['anyconnect_premium_peers'] = \
                        int(m.groupdict()['anyconnect_premium_peers'])
                continue

            m = p24.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['anyconnect_essentials'] = \
                        m.groupdict()['anyconnect_essentials']
                continue

            m = p25.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['other_vpn_peers'] = \
                        int(m.groupdict()['other_vpn_peers'])
                continue

            m = p26.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['total_vpn_peers'] = \
                        int(m.groupdict()['total_vpn_peers'])
                continue

            m = p27.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['anyconnect_for_mobile'] = \
                        m.groupdict()['anyconnect_for_mobile']
                continue

            m = p28.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['anyconnect_for_cisco_vpn_phone'] = \
                        m.groupdict()['anyconnect_for_cisco_vpn_phone']
                continue

            m = p29.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['advanced_endpoint_assessment'] = \
                        m.groupdict()['advanced_endpoint_assessment']
                continue

            m = p30.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['shared_license'] = \
                        m.groupdict()['shared_license']
                continue

            m = p31.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['total_tls_proxy_sessions'] = \
                        int(m.groupdict()['total_tls_proxy_sessions'])
                continue

            m = p32.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['botnet_traffic_filter'] = \
                        m.groupdict()['botnet_traffic_filter']
                continue

            m = p33.match(line)
            if m:
                if 'licensed_features' not in version_dict['version']:
                    version_dict['version']['licensed_features'] = {}
                version_dict['version']['licensed_features']['cluster'] = \
                        m.groupdict()['cluster']
                continue

            m = p34.match(line)
            if m:
                serial_number = m.groupdict()['serial_number']
                version_dict['version']['serial_number'] = serial_number
                continue

            m = p35.match(line)
            if m:
                image_type = m.groupdict()['image_type']
                version_dict['version']['image_type'] = image_type
                continue

            m = p36.match(line)
            if m:
                key_version = m.groupdict()['key_version']
                version_dict['version']['key_version'] = key_version
                continue

            m = p37.match(line)
            if m:
                last_modified_by = m.groupdict()['last_modified_by']
                last_modified_date = m.groupdict()['last_modified_date']
                version_dict['version']['last_modified_by'] = last_modified_by
                version_dict['version']['last_modified_date'] = last_modified_date
                continue

        return version_dict
