''' 
show_platform.py
IOSXE parsers for the following show commands:
    * 'show platform integrity sign'
    * 'show platform sudi certificate sign'
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

log = logging.getLogger(__name__)


class ShowPlatformIntegritySchema(MetaParser):
    """Schema for show platform integrity sign"""

    schema = {
        'platform': str,
        'boot': {
            Any(): {
                'version': str,
                'hash': str,
            },
            'loader': {
                'version': str,
                'hash': str,
            },
        },
        'os_version': str,
        'os_hashes': {
            Any(): str,
        },
        Optional('signature_version'): int,
        Optional('signature'): str,
    }


class ShowPlatformIntegrity(ShowPlatformIntegritySchema):

    command ='show platform integrity sign'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.command)

        ret_dict = {}

        # Platform: C9300-24U
        p1 = re.compile(r'^Platform: +(?P<platform>\S+)$')

        # Boot 0 Version: F01144R16.216e68ad62019-02-13
        p2 = re.compile(r'^Boot +(?P<boot>\d+) +Version: +(?P<version>\S+)$')

        # Boot 0 Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
        p3 = re.compile(r'^Boot +(?P<boot>\d+) +Hash: +(?P<hash>\S+)$')

        # Boot Loader Version: System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE
        p4 = re.compile(r'^Boot +Loader +Version: +(?P<boot_loader_version>[\S ]+)$')

        # Boot Loader Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
        p5 = re.compile(r'^Boot +Loader +Hash: *(?P<hash>\S+)$')

        # 51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57
        p6 = re.compile(r'^(?P<hash>\S+)$')

        # OS Version: 2019-07-11_16.25_mzafar
        p7 = re.compile(r'^OS +Version: +(?P<os_version>\S+)$')

        # OS Hashes:
        p8 = re.compile(r'^OS +Hashes:$')

        # PCR0: BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E
        p9 = re.compile(r'^(?P<hash_key>\S+): +(?P<hash_val>\S+)$')

        # cat9k_iosxe.2019-07-11_16.25_mzafar.SSA.bin:
        p10 = re.compile(r'^(?P<os_hash>\S+):$')

        # Signature version: 1
        p11 = re.compile(r'^Signature version: +(?P<signature_version>\S+)$')

        # Signature:
        p12 = re.compile(r'^Signature:$')

        for line in output.splitlines():
            line = line.strip()

            # Platform: C9300-24U
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'platform': group['platform']})
                continue

            # Boot 0 Version: F01144R16.216e68ad62019-02-13
            m = p2.match(line)
            if m:
                group = m.groupdict()
                boot = int(group['boot'])
                version = group['version']
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot, {})
                boot_dict.update({'version': version})
                continue

            # Boot 0 Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                boot = int(group['boot'])
                hash_val = group['hash']
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot, {})
                boot_dict.update({'hash': hash_val})
                continue

            # Boot Loader Version: System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE
            m = p4.match(line)
            if m:
                group = m.groupdict()
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_version = group['boot_loader_version']
                boot_loader_dict.update({'version': boot_loader_version})
                continue

            # Boot Loader Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
            m = p5.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                hash_type = 'boot_loader'
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_hash = ret_dict.get('boot_loader_hash', '')
                boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                boot_loader_dict.update({'hash': boot_loader_hash})
                continue

            # 51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57
            m = p6.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                if hash_type == 'boot_loader':
                    boot_loader_hash = boot_loader_dict.get('boot_loader_hash', '')
                    boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                    boot_loader_dict.update({'hash': boot_loader_hash})
                elif hash_type == 'os_hash':
                    os_hash_val = os_hash_dict.get(os_hash, '')
                    os_hash_val = '{}{}'.format(os_hash_val, hash_val)
                    os_hash_dict.update({'os_hash': os_hash_val})
                elif hash_type == 'signature':
                    ret_dict.update({'signature': hash_val})
                continue

            # OS Version: 2019-07-11_16.25_mzafar
            m = p7.match(line)
            if m:
                group = m.groupdict()
                os_version = group['os_version']
                ret_dict.update({'os_version': os_version})
                continue

            # OS Hashes:
            m = p8.match(line)
            if m:
                hash_type = 'os_hashes'
                continue

            # Signature:
            m = p12.match(line)
            if m:
                hash_type = 'signature'
                continue

            # PCR0: BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E
            m = p9.match(line)
            if m:
                group = m.groupdict()
                hash_type = 'os_hashes'
                group = m.groupdict()
                os_hash = group['hash_key']
                hash_val = group['hash_val']
                os_hash_dict = ret_dict.setdefault('os_hashes', {})
                os_hash_dict.update({os_hash: hash_val})
                continue

            # cat9k_iosxe.2019-07-11_16.25_mzafar.SSA.bin:
            m = p10.match(line)
            if m:
                hash_type = 'os_hashes'
                group = m.groupdict()
                os_hash = group['os_hash']
                os_hash_dict = ret_dict.setdefault('os_hashes', {})
                os_hash_dict.update({os_hash: ''})
                continue

            # Signature version: 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'signature_version': int(group['signature_version'])})
                continue

        return ret_dict


class ShowPlatformSudiCertificateNonceSchema(MetaParser):
    """Schema for show platform sudi certificate sign nonce 123"""

    schema = {
        'certificates':{
            int: str,
        },
        Optional('signature'):str,
        Optional('signature_version'):int,
    }


class ShowPlatformSudiCertificateNonce(ShowPlatformSudiCertificateNonceSchema):
    """Parser for show platform  sudi  certificate sign nonce 123"""

    cli_command = ['show platform sudi certificate sign']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        certificate_num=0
        certficate=""
        sig_check =False
        ret_dict = {}

        # -----BEGIN CERTIFICATE-----
        p1 = re.compile(r'^\-+BEGIN CERTIFICATE\-+$')

        # -----END CERTIFICATE-----
        p2 = re.compile(r'^\-+END CERTIFICATE\-+$')

        # Signature version: 1
        p3 = re.compile(r'^Signature version:\s+(?P<signature>\d+)$')

        # Signature:
        p4 = re.compile(r'^Signature:$')

        # A59DA741EA66C2AFC006E1766B3B11493A79E67408388C40160C2729F88281E9
        p5 = re.compile(r'^(?P<signatur>[A-Z\d]+)$')

        # o4IBBDCCAQAwDgYDVR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgw
        p6 = re.compile(r'([a-zA-Z0-9/+=]+)')

        for line in output.splitlines():
            line=line.strip()

            # -----BEGIN CERTIFICATE-----
            m = p1.match(line)
            if m:
                begin_certf=True
                certificate_num = certificate_num + 1
                continue

            # -----END CERTIFICATE-----
            m = p2.match(line)
            if m:
                root_dict=ret_dict.setdefault('certificates',{})
                #certificate_list.append(certficate)
                root_dict[certificate_num] = certficate
                certficate = ''
                continue

            # Signature version: 1
            m = p3.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('signature_version',int(group['signature']))
                continue

            # Signature:
            m = p4.match(line)
            if m:
                sig_check=True
                continue

            # 7E873A87E287B685E823F7BC66CF13D43EC238D40DA7CBEA06F6926C04C8C5AFC21BA4C
            m = p5.match(line)
            if m and sig_check:
                group=m.groupdict()
                ret_dict.setdefault('signature', group['signatur'])
                continue

            # o4IBBDCCAQAwDgYDVR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgw
            m = p6.match(line)
            if m:
                certficate = certficate + m.group()
                continue

        return ret_dict

class ShowEnvironmentPowerSchema(MetaParser):
    """Schema for show environment power"""

    schema = {
        'power_supplies': {
            Any(): {
                'type': str,
                'status': str,
                Optional('voltage'): str
            }
        }
    }

class ShowEnvironmentPower(ShowEnvironmentPowerSchema):
    """Parser for show environment power"""

    cli_command = 'show environment power'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        
        # POWER SUPPLY-A      DC      OK      24V
        # POWER SUPPLY B      DC      OK      54V
        # POWER SUPPLY        DC      OK      24V
        p1 = re.compile(r'^(?P<name>(\w+\s\w+\-\w+(\s{2}))|((\w+\s){2}(\w+)(\s{2}))|(\w+\s\w+(\s{2})))\s+(?P<type>\S+)\s+(?P<status>\S+)\s{2,}(?P<voltage>\S+)$')

        # POWER SUPPLY-B      DC      OK
        # POWER SUPPLY B      DC      OK
        # POWER SUPPLY        DC      OK
        p2 = re.compile(r'^(?P<name>(\w+\s\w+\-\w+(\s{2}))|((\w+\s){2}(\w+)(\s{2}))|(\w+\s\w+(\s{2})))\s+(?P<type>\S+)\s+(?P<status>.+)$')

        for line in output.splitlines():
            line = line.strip()

            if 'Pwr Supply' in line:
                continue

            # POWER SUPPLY-A      DC      OK      24V
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['name'].strip()
                power_supply_dict = ret_dict.setdefault('power_supplies', {}).setdefault(name, {})
                power_supply_dict.update({
                    'type': group['type'],
                    'status': group['status'],
                    'voltage': group['voltage']
                })
                continue

            # POWER SUPPLY-B      DC      OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name = group['name'].strip()
                power_supply_dict = ret_dict.setdefault('power_supplies', {}).setdefault(name, {})
                power_supply_dict.update({
                    'type': group['type'],
                    'status': group['status'],
                })
                continue

        return ret_dict

class ShowEnvironmentTemperatureSchema(MetaParser):
    """Schema for show environment temperature"""

    schema = {
        'supervisor_temp_value': str,
        'supervisor_temp_state': str,
        'system_temperature_thresholds': {
            'minor_threshold': str,
            'major_threshold': str,
            'critical_threshold': str
        }
    }

class ShowEnvironmentTemperature(ShowEnvironmentTemperatureSchema):
    """Parser for show environment temperature"""

    cli_command = 'show environment temperature'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Supervisor Temperature Value: 48 C
        p1 = re.compile(r'^Supervisor +Temperature +Value: +(?P<supervisor_temp_value>.+)$')

        # Temperature State: GREEN
        p2 = re.compile(r'^Temperature +State: +(?P<supervisor_temp_state>\S+)$')

        # Minor Threshold    : 80 C (Yellow)
        p3 = re.compile(r'^Minor +Threshold +: +(?P<minor_threshold>.+)$')

        # Major Threshold    : 90 C (Red)
        p4 = re.compile(r'^Major +Threshold +: +(?P<major_threshold>.+)$')

        # Critical Threshold : 96 C
        p5 = re.compile(r'^Critical +Threshold +: +(?P<critical_threshold>.+)$')

        for line in output.splitlines():
            line = line.strip()

            # Supervisor Temperature Value: 48 C
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'supervisor_temp_value': group['supervisor_temp_value']})
                continue

            # Temperature State: GREEN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'supervisor_temp_state': group['supervisor_temp_state']})
                continue

            # Minor Threshold    : 80 C (Yellow)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('system_temperature_thresholds', {}).update({'minor_threshold': group['minor_threshold']})
                continue

            # Major Threshold    : 90 C (Red)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('system_temperature_thresholds', {}).update({'major_threshold': group['major_threshold']})
                continue

            # Critical Threshold : 96 C
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('system_temperature_thresholds', {}).update({'critical_threshold': group['critical_threshold']})
                continue

        return ret_dict

class ShowEnvironmentAlarmContactSchema(MetaParser):
    """Schema for show environment alarm-contact"""

    schema = {
        Any(): {
            'status': str,
            'description': str,
            'severity': str,
            'trigger': str,
        }
    }

class ShowEnvironmentAlarmContact(ShowEnvironmentAlarmContactSchema):
    """Parser for show environment alarm-contact"""

    cli_command = 'show environment alarm-contact'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # ALARM CONTACT 1
        p1 = re.compile(r'^ALARM +CONTACT +(?P<contact>\d+)$')

        # Status:      not asserted
        p2 = re.compile(r'^Status: +(?P<status>.+)$')

        # Description: external alarm contact 1
        p3 = re.compile(r'^Description: +(?P<description>.+)$')

        # Severity:    minor
        p4 = re.compile(r'^Severity: +(?P<severity>.+)$')

        # Trigger:     closed
        p5 = re.compile(r'^Trigger: +(?P<trigger>.+)$')

        for line in output.splitlines():
            line = line.strip()

            # ALARM CONTACT 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                contact = 'ALARM CONTACT ' + group['contact']
                alarm_contact_dict = ret_dict.setdefault(contact, {})
                continue

            # Status:      not asserted
            m = p2.match(line)
            if m:
                group = m.groupdict()
                alarm_contact_dict.update({'status': group['status']})
                continue

            # Description: external alarm contact 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                alarm_contact_dict.update({'description': group['description']})
                continue

            # Severity:    minor
            m = p4.match(line)
            if m:
                group = m.groupdict()
                alarm_contact_dict.update({'severity': group['severity']})
                continue

            # Trigger:     closed
            m = p5.match(line)
            if m:
                group = m.groupdict()
                alarm_contact_dict.update({'trigger': group['trigger']})
                continue

        return ret_dict

class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""

    schema = {
        Optional('alarms'): {
            Any(): {
                'status': str,
                'description': str,
                'severity': str,
                'trigger': str,
            }
        },
        Optional('temperatures'): {
            Optional('supervisor_temp_value'): str,
            Optional('supervisor_temp_state'): str,
            Optional('system_temperature_thresholds'): {
                'minor_threshold': str,
                'major_threshold': str,
                'critical_threshold': str
            }
        },
        Optional('power_supplies'): {
            Any(): {
                'type': str,
                'status': str,
                Optional('voltage'): str
            }
        },
        Optional('switch'): {
            Any(): {
                Optional('alarms'): {
                    Any(): {
                        'status': str,
                        'description': str,
                        'severity': str,
                        'trigger': str
                    }
                },
                Optional('system_temperature'): str,
                Optional('temperature_sensors'): {
                    Any(): {
                        'reading': {
                            'value': str,
                            'unit': str
                        },
                        'state': str,
                        'yellow_threshold': str,
                        'red_threshold': str
                    }
                },
                Optional('power_supply'): {
                    Any(): {
                        'pid': str,
                        Optional('serial'): str,
                        'status': str,
                        Optional('sys_pwr'): str,
                        Optional('watts'): str
                    }
                },
                Optional('sensors'): {
                    Any(): {
                        'status': str,
                        'reading': str
                    }
                }
            }
        }
    }

class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""

    cli_command = 'show environment all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        current_switch = None
        current_alarm = None
        current_sensor = None

        # Switch: 1
        p0 = re.compile(r'^Switch:\s+(?P<switch>\d+)$')

        # ALARM CONTACT 1
        p1 = re.compile(r'^ALARM +CONTACT +(?P<contact>\d+)$')

        # Status:      not asserted
        p2 = re.compile(r'^Status: +(?P<status>.+)$')

        # Description: external alarm contact 1
        p3 = re.compile(r'^Description: +(?P<description>.+)$')

        # Severity:    minor
        p4 = re.compile(r'^Severity: +(?P<severity>.+)$')

        # Trigger:     closed   
        p5 = re.compile(r'^Trigger: +(?P<trigger>.+)$')

        # Supervisor Temperature Value: 48 C
        p11 = re.compile(r'^Supervisor +Temperature +Value: +(?P<supervisor_temp_value>.+)$')

        # Temperature State: GREEN
        p12 = re.compile(r'^Temperature +State: +(?P<supervisor_temp_state>\S+)$')

        # Minor Threshold    : 80 C (Yellow)
        p13 = re.compile(r'^Minor +Threshold +: +(?P<minor_threshold>.+)$')

        # Major Threshold    : 90 C (Red)
        p14 = re.compile(r'^Major +Threshold +: +(?P<major_threshold>.+)$')

        # Critical Threshold : 96 C
        p15 = re.compile(r'^Critical +Threshold +: +(?P<critical_threshold>.+)$')

        # POWER SUPPLY-A      DC      OK      24V
        # POWER SUPPLY-A      DC      OK
        p16 = re.compile(r'^POWER +SUPPLY-(?P<id>[AB]) +(?P<type>\S+) +(?P<status>\S+)(\s+(?P<voltage>\S+))?$')

        # POWER SUPPLY        DC      OK
        p16b = re.compile(r'^POWER +SUPPLY\s+(?P<type>\S+)\s+(?P<status>\S+)$')

        # Switch 1: SYSTEM TEMPERATURE is OK
        p17 = re.compile(r'^Switch\s+\d+:\s+SYSTEM\s+TEMPERATURE\s+is\s+(?P<status>\w+)$')

        # Switch 1 - Inlet Temp Sensor 46 C
        p18 = re.compile(r'^Switch\s+\d+\s+-\s+(?P<sensor_name>[\w\-]+\s+Temp\s+Sensor)\s+(?P<value>\d+)\s+(?P<unit>\w+)$')

        # Yellow Threshold : 80 C
        p19 = re.compile(r'^Yellow\s+Threshold\s*:\s+(?P<threshold>.+)$')

        # Red Threshold    : 96 C
        p20 = re.compile(r'^Red\s+Threshold\s*:\s+(?P<threshold>.+)$')

        # POWER SUPPLY-1     Not Present
        p21 = re.compile(r'^(?P<ps>POWER\s+SUPPLY-\d+)\s+(?P<status>Not\s+Present)$')

        # POWER SUPPLY-2  PWR-RGD-AC-DC-250   DTH255202J5     OK               Good              250
        p22 = re.compile(
            r'^(?P<ps>POWER\s+SUPPLY-\d+)\s+(?P<pid>\S+)\s+(?P<serial>\S+)\s+(?P<status>\w+)'
            r'\s+(?P<sys_pwr>\w+)\s+(?P<watts>\d+)'
        )

        # PS-1 Vout     Not Present     0mV
        # PS-1 Hotspot  Not Present     0 C
        p23 = re.compile(r'^(?P<sensor_name>PS-\d+\s+\w+)\s+(?P<status>Not\s+Present|Good)\s+(?P<reading>.+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Skip header lines
            if line.startswith('---') or line.startswith('==='):
                continue
            if 'Pwr Supply' in line and 'Type' in line:
                continue
            if 'Sensor Name' in line and 'Status' in line:
                continue
            if 'System Temperature thresholds' in line:
                continue

            # Switch: 1
            m = p0.match(line)
            if m:
                current_switch = m.group("switch")
                continue

            # ALARM CONTACT 1
            m = p1.match(line)
            if m:
                contact = f"ALARM CONTACT {m.group('contact')}"
                current_alarm = contact
                if current_switch:
                    switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                    switch_dict.setdefault("alarms", {}).setdefault(current_alarm, {})
                else:
                    alarm_dict = ret_dict.setdefault('alarms', {}).setdefault(contact, {})
                continue

            #    Status:      not asserted
            m = p2.match(line)
            if m:
                if current_switch and current_alarm:
                    switch_dict = ret_dict["switch"][current_switch]
                    switch_dict["alarms"][current_alarm]["status"] = m.group("status")
                elif current_alarm:
                    ret_dict['alarms'][current_alarm].update({'status': m.group('status')})
                continue

            #    Description: external alarm contact 1
            m = p3.match(line)
            if m:
                if current_switch and current_alarm:
                    switch_dict = ret_dict["switch"][current_switch]
                    switch_dict["alarms"][current_alarm]["description"] = m.group("description")
                elif current_alarm:
                    ret_dict['alarms'][current_alarm].update({'description': m.group('description')})
                continue

            #    Severity:    minor
            m = p4.match(line)
            if m:
                if current_switch and current_alarm:
                    switch_dict = ret_dict["switch"][current_switch]
                    switch_dict["alarms"][current_alarm]["severity"] = m.group("severity")
                elif current_alarm:
                    ret_dict['alarms'][current_alarm].update({'severity': m.group('severity')})
                continue

            #    Trigger:     closed
            m = p5.match(line)
            if m:
                if current_switch and current_alarm:
                    switch_dict = ret_dict["switch"][current_switch]
                    switch_dict["alarms"][current_alarm]["trigger"] = m.group("trigger")
                elif current_alarm:
                    ret_dict['alarms'][current_alarm].update({'trigger': m.group('trigger')})
                continue

            # Supervisor Temperature Value: 48 C
            m = p11.match(line)
            if m:
                ret_dict.setdefault('temperatures', {}).update({'supervisor_temp_value': m.group('supervisor_temp_value')})
                continue

            # Temperature State: GREEN
            m = p12.match(line)
            if m:
                if current_switch and current_sensor:
                    switch_dict = ret_dict["switch"][current_switch]
                    switch_dict["temperature_sensors"][current_sensor]["state"] = m.group("supervisor_temp_state")
                else:
                    ret_dict.setdefault('temperatures', {}).update({'supervisor_temp_state': m.group('supervisor_temp_state')})
                continue

            # Minor Threshold    : 80 C (Yellow)
            m = p13.match(line)
            if m:
                ret_dict.setdefault('temperatures', {}).setdefault('system_temperature_thresholds', {}).update(
                    {'minor_threshold': m.group('minor_threshold')})
                continue

            # Major Threshold    : 90 C (Red)
            m = p14.match(line)
            if m:
                ret_dict.setdefault('temperatures', {}).setdefault('system_temperature_thresholds', {}).update(
                    {'major_threshold': m.group('major_threshold')})
                continue

            # Critical Threshold : 96 C 
            m = p15.match(line)
            if m:
                ret_dict.setdefault('temperatures', {}).setdefault('system_temperature_thresholds', {}).update(
                    {'critical_threshold': m.group('critical_threshold')})
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            m = p17.match(line)
            if m and current_switch:
                switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                switch_dict["system_temperature"] = m.group("status")
                continue

            # Switch 1 - Inlet Temp Sensor 46 C
            m = p18.match(line)
            if m and current_switch:
                sensor_name = m.group("sensor_name")
                current_sensor = sensor_name
                switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                sensor_dict = switch_dict.setdefault("temperature_sensors", {}).setdefault(sensor_name, {})
                sensor_dict["reading"] = {
                    "value": m.group("value"),
                    "unit": m.group("unit")
                }
                continue

            # Yellow Threshold : 80 C
            m = p19.match(line)
            if m and current_switch and current_sensor:
                switch_dict = ret_dict["switch"][current_switch]
                switch_dict["temperature_sensors"][current_sensor]["yellow_threshold"] = m.group("threshold")
                continue

            # Red Threshold    : 96 C
            m = p20.match(line)
            if m and current_switch and current_sensor:
                switch_dict = ret_dict["switch"][current_switch]
                switch_dict["temperature_sensors"][current_sensor]["red_threshold"] = m.group("threshold")
                continue

            # POWER SUPPLY-1     Not Present
            m = p21.match(line)
            if m and current_switch:
                ps = m.group("ps")
                switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                ps_dict = switch_dict.setdefault("power_supply", {}).setdefault(ps, {})
                ps_dict["pid"] = "Not Present"
                ps_dict["status"] = "Not Present"
                continue

            # POWER SUPPLY-2  PWR-RGD-AC-DC-250   DTH255202J5     OK               Good              250
            m = p22.match(line)
            if m and current_switch:
                ps = m.group("ps")
                switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                ps_dict = switch_dict.setdefault("power_supply", {}).setdefault(ps, {})
                ps_dict["pid"] = m.group("pid")
                ps_dict["serial"] = m.group("serial")
                ps_dict["status"] = m.group("status")
                ps_dict["sys_pwr"] = m.group("sys_pwr")
                ps_dict["watts"] = m.group("watts")
                continue

            # PS-1 Vout     Not Present     0mV
            m = p23.match(line)
            if m and current_switch:
                sensor_name = m.group("sensor_name").strip()
                switch_dict = ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                sensor_dict = switch_dict.setdefault("sensors", {}).setdefault(sensor_name, {})
                sensor_dict["status"] = m.group("status")
                sensor_dict["reading"] = m.group("reading")
                continue

            # POWER SUPPLY-A      DC      OK      24V
            # POWER SUPPLY-A      DC      OK
            m = p16.match(line)
            if m:
                ps_name = f"POWER SUPPLY-{m.group('id')}"
                ps_dict = ret_dict.setdefault('power_supplies', {}).setdefault(ps_name, {})
                ps_dict.update({
                    'type': m.group('type'),
                    'status': m.group('status')
                })
                if m.group('voltage'):
                    ps_dict['voltage'] = m.group('voltage')
                continue

            # POWER SUPPLY        DC      OK
            m = p16b.match(line)
            if m:
                ps_name = "POWER SUPPLY"
                ps_dict = ret_dict.setdefault('power_supplies', {}).setdefault(ps_name, {})
                ps_dict.update({
                    'type': m.group('type'),
                    'status': m.group('status')
                })
                continue

        return ret_dict

class ShowPlatformStatusSchema(MetaParser):
    """Schema for show platform status"""
    schema = {
        'hardware_locations': {
            Any(): {
                'status': str,
                Optional('issuer'): str,
                Optional('subject'): str
            }
        }
    }

class ShowPlatformStatus(ShowPlatformStatusSchema):
    """Parser for show platform status"""
    cli_command = 'show platform status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Main Board Authentication Status:
        p1 = re.compile(r'^(?P<hardware_location>.+) Status:$')

        # Status: Normal
        p2 = re.compile(r'^Status:\s+(?P<status>.+)$')

        # Issuer: /CN=High Assurance SUDI CA/O=Cisco
        p3 = re.compile(r'^Issuer:\s+(?P<issuer>.+)$')

        # Subject: /serialNumber=PID:IE-3100-3P1U2S SN:FDO2902JF4N/O=Cisco/OU=ACT-2 Lite SUDI/CN=IE-3100-3P1U2S
        p4 = re.compile(r'^Subject:\s+(?P<subject>.+)$')

        for line in output.splitlines():
            line = line.strip()

            # Main Board Authentication Status:
            # Linecard Authentication Status:
            m = p1.match(line)
            if m:
                hardware_location = str(m.group('hardware_location')).strip()
                inner_dict = ret_dict.setdefault('hardware_locations', {}).setdefault(hardware_location, {})
                continue

            # Status: Normal
            m = p2.match(line)
            if m:
                inner_dict['status'] = str(m.group('status')).strip()
                continue

            # Issuer: /CN=High Assurance SUDI CA/O=Cisco
            m = p3.match(line)
            if m:
                inner_dict['issuer'] = str(m.group('issuer')).strip()
                continue

            # Subject: /serialNumber=PID:IE-3100-3P1U2S SN:FDO2902JF4N/O=Cisco/OU=ACT-2 Lite SUDI/CN=IE-3100-3P1U2S
            m = p4.match(line)
            if m:
                inner_dict['subject'] = str(m.group('subject')).strip()
                continue

        return ret_dict
    
class ShowLocateSwitchSchema(MetaParser):
    """Schema for show locate switch"""

    schema = {
        'locate_switch_status': str,
        Optional('total_time'): int,
        Optional('time_left'): int,
    }

class ShowLocateSwitch(ShowLocateSwitchSchema):
    """Parser for show locate switch"""

    cli_command = 'show locate switch'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Locate Switch disabled!!
        p1 = re.compile(r'^Locate +[Ss]witch +(?P<status>disabled|enabled)!!$')

        # total time: 100 sec
        p2 = re.compile(r'^total +time: +(?P<total_time>\d+) +sec$')

        # time left:  96 sec
        p3 = re.compile(r'^time +left: +(?P<time_left>\d+) +sec$')

        for line in output.splitlines():
            line = line.strip()

            # Locate Switch disabled!!
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'locate_switch_status': group['status']})
                continue

            # total time: 100 sec
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'total_time': int(group['total_time'])})
                continue

            # time left:  96 sec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'time_left': int(group['time_left'])})
                continue

        return ret_dict