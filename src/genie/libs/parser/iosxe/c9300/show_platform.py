
# Python
import re
import logging
from collections import OrderedDict
import xml.etree.ElementTree as ET
from genie.libs.parser.utils.common import Common
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowPlatformIntegritySchema(MetaParser):
    schema = {
        'platform': str,
        'boot': {
            Any(): {
                'version': str,
                'hash': str,
            }
        },
        'boot_loader_version': str,
        'boot_loader_hash': str,
        'os_version': str,
        'os_hashes': {
            Any(): str,
        }
    }

class ShowPlatformIntegrity(ShowPlatformIntegritySchema):
    cli_command = 'show platform integrity'
    xml_command = 'show platform integrity | xml'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        # Platform: C9300-24U
        p1 = re.compile(r'^Platform: +(?P<platform>\S+)$')
        # Boot 0 Version: F01144R16.216e68ad62019-02-13
        p2 = re.compile(r'^Boot +(?P<boot>\d+) +Version: +(?P<version>\S+)$')
        # Boot 0 Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
        p3 = re.compile(r'^Boot +(?P<boot>\d+) +Hash: +(?P<hash>\S+)$')
        # Boot Loader Version: System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE
        p4 = re.compile(r'^Boot +Loader +Version: +(?P<boot_loader_version>[\S ]+)$')
        # Boot Loader Hash: 
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

        for line in out.splitlines():
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
                boot_loader_version = group['boot_loader_version']
                ret_dict.update({'boot_loader_version': boot_loader_version})
                continue
            
            # Boot Loader Hash: 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                hash_type = 'boot_loader'
                boot_loader_hash = ret_dict.get('boot_loader_hash', '')
                boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                ret_dict.update({'boot_loader_hash': boot_loader_hash})
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
            
            # PCR0: BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E
            p9 = re.compile(r'^(?P<hash_key>\S+): +(?P<hash_val>\S+)$')
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
            
            # 51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57
            m = p6.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                if hash_type == 'boot_loader':
                    boot_loader_hash = ret_dict.get('boot_loader_hash', '')
                    boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                    ret_dict.update({'boot_loader_hash': boot_loader_hash})
                elif hash_type == 'os_hash':
                    os_hash_val = os_hash_dict.get(os_hash, '')
                    os_hash_val = '{}{}'.format(os_hash_val, hash_val)
                    os_hash_dict.update({'os_hash': os_hash_val})
                continue
        return ret_dict
    
    def xml(self, output=None):
        if not output:
            out = self.device.execute(self.xml_command)
        else:
            out = output
        out = out.replace("]]>]]>", "")
        root = ET.fromstring(out)
        boot_integrity_oper_data = Common.retrieve_xml_child(root=root, key='boot-integrity-oper-data')
        boot_integrity = Common.retrieve_xml_child(root=boot_integrity_oper_data, key='boot-integrity')
        ret_dict = {}
        boot_index = 0
        name = None
        for child in boot_integrity:
            if child.tag.endswith('platform'):
                ret_dict.update({'platform': child.text})
            elif child.tag.endswith('os-version'):
                ret_dict.update({'os_version': child.text})
            elif child.tag.endswith('boot-ver'):
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot_index, {})
                boot_dict.update({'version': child.text})
                boot_index+=1
            elif child.tag.endswith('boot-hash'):
                boot_dict.update({'hash': child.text})
            elif child.tag.endswith('boot-loader-hash'):
                ret_dict.update({'boot_loader_hash': child.text})
            elif child.tag.endswith('boot-loader-ver'):
                ret_dict.update({'boot_loader_version': child.text})
            elif child.tag.endswith('package-signature'):
                for sub_child in child:
                    os_hashes = ret_dict.setdefault('os_hashes', {})
                    if sub_child.tag.endswith('name'):
                        name = sub_child.text
                    elif name and sub_child.tag.endswith('hash'):
                        os_hashes.update({name: sub_child.text})
                        name = None
            elif child.tag.endswith('pcr-register'):
                for sub_child in child:
                    os_hashes = ret_dict.setdefault('os_hashes', {})
                    if sub_child.tag.endswith('index'):
                        name = 'PCR{}'.format(sub_child.text)
                    elif name and sub_child.tag.endswith('pcr-content'):
                        os_hashes.update({name: sub_child.text})
                        name = None
        
        return ret_dict
