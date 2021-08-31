"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto pki certificates <WORD>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# Genie Libs
from genie.libs.parser.utils.common import Common

# =================================================
#  Schema for 'show crypto pki certificates <WORD>'
# =================================================
class ShowCryptoPkiCertificatesSchema(MetaParser):
    """Schema for show crypto pki certificates <WORD>"""
    schema = {
        'trustpoints':
            {Any():
                {'associated_trustpoints':
                    {Any():
                        {'status': str,
                        'serial_number_in_hex': str,
                        'usage': str,
                        Optional('storage'): str,
                        'issuer':
                            {
                            Optional('cn'): str,
                            Optional('o'): str},
                        'subject':
                            {Optional('name'): str,
                            Optional('serial_number'): str,
                            Optional('pid'): str,
                            Optional('cn'): str,
                            Optional('o'): str,
                            },
                        Optional('crl_distribution_points'): str,
                        'validity_date':
                            {'start_date':str,
                            'end_date': str,
                            },
                        },
                    },
                },
            },
        }

# =================================================
#  Parser for 'show crypto pki certificates <WORD>'
# =================================================
class ShowCryptoPkiCertificates(ShowCryptoPkiCertificatesSchema):
    """Parser for show crypto pki certificates <WORD>"""

    cli_command = ['show crypto pki certificates {trustpoint_name}','show crypto pki certificates']

    def cli(self, trustpoint_name='',output=None):
        if output is None:
            if trustpoint_name:
                cmd = self.cli_command[0].format(trustpoint_name=trustpoint_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Certificate
        # CA Certificate
        p1 = re.compile(r'^((?P<cer>Certificate)|(?P<cer_name>(CA|Router Self-Signed) +Certificate))$')

        # Status: Available
        p2 = re.compile(r'^Status: +(?P<status>\w+)$')

        # Certificate Serial Number (hex): 793B572700000003750B
        # Certificate Serial Number: 0x15
        p3 = re.compile(r'^Certificate +Serial +Number( +\(hex\))?: +(?P<serial_number_in_hex>\w+)$')

        # Certificate Usage: General Purpose
        p4 = re.compile(r'^Certificate Usage: +(?P<usage>[\w\s]+)$')

        # Issuer:
        # Subject:
        # Validity Date:
        p5 = re.compile(r'^((?P<issuer>Issuer)|(?P<subject>Subject)|(?P<validity_date>Validity +Date)):$')

        # cn=Cisco Manufacturing CA SHA2
        # CN = tpca-root
        p6 = re.compile(r'(?i)^cn *= *(?P<cn>[\S\s]+)$')

        # o=Cisco
        # O = Company
        p7 = re.compile(r'(?i)^o *= *(?P<o>[\w\s]+)$')

        # Name: WS-C3850-24P-0057D21BC800
        p8 = re.compile(r'^Name: +(?P<name>.*)$')

        # Serial Number: PID:WS-C3850-24P SN:FCW1947C0GF
        p9 = re.compile(r'^Serial +Number: *'
                          'PID: *(?P<pid>[\w\-]+) +'
                          'SN: *(?P<serial_number>[\w\-]+)$')

        # CRL Distribution Points: 
        #     http://www.cisco.com/security/pki/crl/cmca2.crl
        p10 = re.compile(r'(?P<crl_distribution_points>^http:[\w\/\:\.]+)$')

        # start date: 00:34:52 UTC Nov 20 2015
        # end   date: 00:44:52 UTC Nov 20 2025
        p11 = re.compile(r'^((?P<start_date>start +date)|(?P<end_date>end +date)): +(?P<value>.*)$')

        # Associated Trustpoints: CISCO_IDEVID_SUDI
        # Associated Trustpoints: CISCO_IDEVID_SUDI Trustpool
        p12 = re.compile(r'^Associated +Trustpoints: +(?P<trustpoints>[\w\-]+)( +Trustpool)?$')

        # Storage: nvram:IOS-Self-Sig#1.cer
        p13 = re.compile(r'^Storage: +(?P<storage>(\S+))$')

        for line in out.splitlines():
            line = line.strip()
            
            # Certificate
            # CA Certificate
            m = p1.match(line)
            if m:
                if m.groupdict()['cer']:
                    cer_type = 'certificate'
                else:
                    cer_type = m.groupdict()['cer_name'].lower().replace(" ", "_").replace("-", "_")
                cer_dict = ret_dict.setdefault(cer_type, {})
                continue

            # Status: Available
            m = p2.match(line)
            if m:
                cer_dict['status'] = m.groupdict()['status']
                continue

            # Certificate Serial Number (hex): 793B572700000003750B
            # Certificate Serial Number: 0x15
            m = p3.match(line)
            if m:
                cer_dict['serial_number_in_hex'] = m.groupdict()['serial_number_in_hex']
                continue

            # Certificate Usage: General Purpose
            m = p4.match(line)
            if m:
                cer_dict['usage'] = m.groupdict()['usage']
                continue

            # Issuer:
            # Subject:
            # Validity Date:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group.get('issuer', {}):
                    sub_dict = cer_dict.setdefault('issuer', {})
                if group.get('subject', {}):
                    sub_dict = cer_dict.setdefault('subject', {})
                if group.get('validity_date', {}):
                    sub_dict = cer_dict.setdefault('validity_date', {})
                continue

            # cn=Cisco Manufacturing CA SHA2
            # CN = tpca-root
            m = p6.match(line)
            if m:
                sub_dict['cn'] = m.groupdict()['cn']
                continue
            
            # o=Cisco
            # O = Company
            m = p7.match(line)
            if m:
                sub_dict['o'] = m.groupdict()['o']
                continue

            # Name: WS-C3850-24P-0057D21BC800
            m = p8.match(line)
            if m:
                sub_dict['name'] = m.groupdict()['name']
                continue

            # Serial Number: PID:WS-C3850-24P SN:FCW1947C0GF
            m = p9.match(line)
            if m:
                sub_dict.update({k:v for k,v in m.groupdict().items()})
                continue
            
            # CRL Distribution Points: 
            #     http://www.cisco.com/security/pki/crl/cmca2.crl
            m = p10.match(line)
            if m:
                cer_dict['crl_distribution_points'] = m.groupdict()['crl_distribution_points']
                continue

            # start date: 00:34:52 UTC Nov 20 2015
            # end   date: 00:44:52 UTC Nov 20 2025
            m = p11.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault('start_date', group['value']) if \
                    group.get('start_date', {}) else None
                sub_dict.setdefault('end_date', group['value']) if \
                    group.get('end_date', {}) else None
                continue

            # Storage: nvram:IOS-Self-Sig#1.cer
            m = p13.match(line)
            if m:
                cer_dict['storage'] = m.groupdict()['storage']
                continue

            # Associated Trustpoints: CISCO_IDEVID_SUDI
            # Associated Trustpoints: CISCO_IDEVID_SUDI Trustpool
            m = p12.match(line)
            if m:
                trustpoints = m.groupdict()['trustpoints'] 
                continue
        try:
            return {'trustpoints': {trustpoints: {'associated_trustpoints': ret_dict}}}
        except Exception:
            return {}

# =================================================
#  Schema for 'show crypto pki trustpoints'
# =================================================
class ShowCryptoPkiTrustpointsStatusSchema(MetaParser):
    """Schema for show crypto pki trustpoints <WORD>"""
    schema = {
        'Trustpoints':{
            Any(): {
                Any():{
                    Any(): {
                        'subject': {
                            Optional('common_name'): str,
                            Optional('organisation_unit'): str,
                            Optional('organisation'): str,
                            Optional('location'): str,
                            Optional('state'): str,
                            Optional('country'): str,
                            Optional('md5'): str,
                            Optional('sha1'): str,
                        }
                    }
                },
                Optional('last_enroll'): str,
                'state': {
                    'keys_generated': str,
                    'issuing_ca_authenticated': str,
                    'certificate_requests': str
                }
            },
        }
    }

# =================================================
#  Parser for 'show crypto pki trustpoints <WORD> status'
# =================================================
class ShowCryptoPkiTrustpointsStatus(ShowCryptoPkiTrustpointsStatusSchema):
    """Parser for show crypto pki trustpoints <WORD>"""

    cli_command = ['show crypto pki trustpoints {trustpoint_name} status','show crypto pki trustpoints status']

    def cli(self, trustpoint_name='',output=None):
        if output is None:
            if trustpoint_name:
                cmd = self.cli_command[0].format(trustpoint_name=trustpoint_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        # Trustpoint PROXY-SIGNING-CA:
        # Trustpoint PROXY-SIGNING-ROOT-CA:
        # Trustpoint TP-self-signed-1922326537:
        # Trustpoint SLA-TrustPoint:
        p1 = re.compile(r'^Trustpoint +(?P<tp_name>[\s\S]+):$')
        # Issuing CA certificate configured:
        # Router General Purpose certificate configured:
        p2 = re.compile(r'^(?P<cert>[\s\S]+) +certificate +(?P<cert_status>[\s\S]+):$')
        # Subject Name:
        p3 = re.compile(r'^Subject Name:$')
        # Last enrollment status: Granted
        p4 = re.compile(r'^Last +enrollment +status: (?P<last_enroll_status>[\s\S]+)$')
        # State:
        p5 = re.compile(r'^State:$')
        # cn=singlevman.viptela
        # ou=ET
        # o=SDWAN
        # l=BLR
        p6 = re.compile(r'^(?P<common_name>[\s\S]+)=+(?P<cn_value>\S+),(?P<org_unit>[\s\S]+)=+(?P<org_unit_value>\S+),(?P<org>[\s\S]+)=+(?P<org_value>\S+),(?P<loc>[\s\S]+)=+(?P<loc_value>\S+),(?P<state>[\s\S]+)=+(?P<state_value>\S+),(?P<country>[\s\S]+)=+(?P<country_value>\S+)$')
        #cn=C8K-130c17d6-a587-4834-bfce-c12b7bba3c33
        p6_1 = re.compile(r'^(?P<common_name>[\s\S]+)=+(?P<cn_value>\S+)$')
        # cn=OCSP-CA,dc=pki,dc=pki-dt,dc=com
        p6_2 = re.compile(r'^(?P<common_name>[\s\S]+)=+(?P<cn_value>\S+),(?P<domain_component>[\s\S]+)=+(?P<dc_value>\S+),(?P<domain_pki>[\s\S]+)=+(?P<pki_value>\S+),(?P<domain_suffix>[\s\S]+)=+(?P<suffix_value>\S+)$')
        # Fingerprint MD5: 71C6E810 3E6D3664 4BF9F450 05C41AEC
        p7 = re.compile(r'^Fingerprint +(?P<fp_type>[\s\S]+)\: (?P<fp_value>[\s\S]+)$')
        # Keys generated ............. Yes (General Purpose, non-exportable)
        p8 = re.compile(r'^(?P<key_type>[\s\S]+) +\.{1,} +(?P<key_state>[\s\S]+) \(([\s\S]+)\)$')
        # Issuing CA authenticated ....... Yes
        p9 = re.compile(r'^(?P<key_type>[\s\S]+) +\.{1,} +(?P<key_state>[\s\S]+)$')
        # Certificate request(s) ..... Yes
        p10 = re.compile(r'^(?P<key_type>[\s\S]+)(s) +\.{1,} +(?P<key_state>[\s\S]+)$')
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            # Trustpoint PROXY-SIGNING-CA:
            # Trustpoint PROXY-SIGNING-ROOT-CA:
            # Trustpoint TP-self-signed-1922326537:
            # Trustpoint SLA-TrustPoint:  
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tp_type = groups['tp_name'].replace(':', '') 
                tp_dict = ret_dict.setdefault('Trustpoints',{}).setdefault(tp_type,{})
                last_dict_ptr = tp_dict
                continue
            # Issuing CA certificate configured:
            # Router General Purpose certificate configured:
            m = p2.match(line)
            if m:
                cert_grp = m.groupdict()
                cert_type = cert_grp['cert'].replace(':', '')
                cert_type_state = cert_grp['cert_status'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                cert_status_dict = tp_dict.setdefault("certificate_configured",{})
                cert_type_dict = cert_status_dict.setdefault(cert_type,{})
                last_dict_ptr = cert_type_dict
                continue
            # Subject Name:
            m = p3.match(line)
            if m:
                subject_dict = cert_type_dict.setdefault('subject',{})
                last_dict_ptr = subject_dict
                continue
            # Last enrollment status: Granted
            m = p4.match(line)
            if m:
                last_enroll = m.groupdict()
                last_enroll_stat = last_enroll['last_enroll_status'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                tp_dict.update({"last_enroll": last_enroll_stat})
                continue
            # State:
            m = p5.match(line)
            if m:
                state_dict = tp_dict.setdefault('state',{})
                last_dict_ptr = state_dict
                continue
            # cn=singlevman.viptela
            # ou=ET
            # o=SDWAN
            # l=BLR
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                key = groups['common_name'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['cn_value']
                last_dict_ptr.update({'common_name':value})
                key = groups['org_unit'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['org_unit_value']
                last_dict_ptr.update({'organisation_unit':value})
                key = groups['org'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['org_value']
                last_dict_ptr.update({'organisation':value})
                key = groups['loc'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['loc_value']
                last_dict_ptr.update({'location':value})
                key = groups['state'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['state_value']
                last_dict_ptr.update({'state':value})
                key = groups['country'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['country_value']
                last_dict_ptr.update({'country':value})
                continue
            #cn=C8K-130c17d6-a587-4834-bfce-c12b7bba3c33
            m = p6_1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['common_name'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['cn_value']
                last_dict_ptr.update({'common_name':value})
                continue
            # cn=OCSP-CA,dc=pki,dc=pki-dt,dc=com
            m = p6_2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['common_name'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                value = groups['cn_value']
                last_dict_ptr.update({'common_name':value})
                continue
            # Fingerprint MD5: 71C6E810 3E6D3664 4BF9F450 05C41AEC
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                fp_type = groups['fp_type'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                fp_value = groups['fp_value']
                last_dict_ptr.update({fp_type:fp_value})
                continue
            # Keys generated ............. Yes (General Purpose, non-exportable)
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                key_type = groups['key_type'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                key_state = groups['key_state'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                state_dict.update({key_type:key_state})
                continue
            # Issuing CA authenticated ....... Yes
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                key_type = groups['key_type'].replace('-', '_').replace(' ', '_').replace(':', '').lower().replace('(',"").replace(')',"")
                key_state = groups['key_state'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                state_dict.update({key_type:key_state})
                continue
            # Certificate request(s) ..... Yes
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                key_type = groups['key_type'].replace('-', '_').replace(' ', '_').replace(':', '').lower().replace('(',"").replace(')',"")
                key_state = groups['key_state'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                state_dict.update({key_type:key_state})
                continue

        return ret_dict
