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