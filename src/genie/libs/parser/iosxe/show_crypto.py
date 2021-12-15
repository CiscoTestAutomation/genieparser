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

# =========================================================
#  Schema for 'show crypto pki certificates verbose <WORD>'
# =========================================================
class ShowCryptoPkiCertificateVerboseSchema(MetaParser):
    """Schema for show 
        * show crypto pki certificates verbose {trustpoint}
    """
    schema = {
        'certificates': {
            Any(): { 
                'status': str, 
                'serial': str, 
                'usage': str, 
                'issuer': {
                    Optional('common_name'): str, 
                    Optional('organization'): str, 
                    Optional('name'): str, 
                    Optional('organizational_unit'): str, 
                    Optional('country'): str, 
                    Optional('locale'): str, 
                    Optional('street'): str, 
                    Optional('hostname'): str,
                    Optional('email'): str,
                    Optional('ip_address'): str,
                    Optional('serial_number'): str
                }, 
                'subject': {
                    Optional('common_name'): str, 
                    Optional('organization'): str, 
                    Optional('name'): str, 
                    Optional('organizational_unit'): str, 
                    Optional('country'): str, 
                    Optional('locale'): str, 
                    Optional('street'): str, 
                    Optional('hostname'): str,
                    Optional('email'): str,
                    Optional('ip_address'): str,
                    Optional('serial_number'): str
                }, 
                'validity_date': {
                    'start_date': str, 
                    'end_date': str, 
                    Optional('renew_date'): str
                }, 
                'subject_key_info': {
                    'key_algorithm': str, 
                    'key_length': str
                }, 
                'signature_algorithm': str, 
                'fingerprint_md5': str, 
                'fingerprint_sha1': str, 
                Optional('cdp'): {
                    Any(): str
                }, 
                Optional('key_usage_hex'): str,
                'key_usage': {
                    Any(): str
                }, 
                Optional('subject_key_id'): str,
                Optional('subj_alt_name'): {
                    Optional('subj_alt_fqdn'): str,
                    Optional('subj_alt_ip_addr'): str,
                    Optional('subj_alt_other_names'): str
                },
                Optional('authority_key_id'): str, 
                Optional('ocsp_url'): str,
                Optional('ca_flag'):str,
                Optional('extended_key_unit'): {
                    Any(): str
                },
                Optional('cert_install_time'): str, 
                'trustpoints': str, 
                Optional('key_label'): str,
                Optional('storage'): str,
                Optional('key_store'): str
            }
        }
    }
# =========================================================
#  Parser for 'show crypto pki certificates verbose <WORD>'
# =========================================================   
class ShowCryptoPkiCertificateVerbose(ShowCryptoPkiCertificateVerboseSchema):
    """Parser for 
        * show crypto pki certificates verbose {trustpoint}
    """

    cli_command = ['show crypto pki certificates verbose {trustpoint}']

    def cli(self, trustpoint='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(trustpoint=trustpoint))

        # initial return dictionary
        ret_dict = {}
        # initial regexp pattern

        # CA Certificate
        # Certificate
        # Certificate (Rollover)
        # CA Certificate (Rollover)
        # Certificate (subordinate CA certificate)
        # Certificate (subordinate CA certificate, Rollover)
        # Certificate (RA mode CS certificate)
        # Certificate (RA mode CS certificate, Rollover)

        p1 = re.compile(r'^((?P<cer>Certificate)|(?P<cer_name>(CA|Router Self-Signed) +Certificate)|(?P<cer_rollover>(CA)? *Certificate +\(Rollover\))|(?P<cer_sub_ra>Certificate +\((subordinate|RA mode) +(CA|CS) +certificate\))|(?P<cer_sub_ra_rollover>Certificate +\((subordinate|RA mode) +(CA|CS) +certificate, +Rollover\)))$')
    
        # Status: Available
        p2 = re.compile(r'^Status:\s+(?P<status>\w+)$')

        # Certificate Serial Number (hex): 01
        p3 = re.compile(r'^Certificate +Serial +Number( +\(hex\))?: +(?P<serial>\w+)$')
        
        # Certificate Usage: Signature
        p4 = re.compile(r'^Certificate Usage: +(?P<usage>[\w\s]+)$')

        # Issuer:
        # Subject:
        # Validity Date:
        p5 = re.compile(r'^((?P<issuer>Issuer)|(?P<subject>Subject)|(?P<validity_date>Validity +Date)):$')

        # cn=ROOT
        p6 = re.compile(r'(?i)^cn *= *(?P<common_name>[\S\s]*)$')

        # ou=PKI
        p7 = re.compile(r'(?i)^o *= *(?P<organization>[\S\s]*)$')

        # Name: pki-reg7
        p8 = re.compile(r'(?i)^Name *: *(?P<name>[\S\s]*)$')

        # ou=EN
        p9 = re.compile(r'(?i)^ou *= *(?P<organizational_unit>[\S\s]*)$')

        # c=IN
        p10 = re.compile(r'(?i)^c *= *(?P<country>[\S\s]*)$')

        # l=Bangalore 
        p11 = re.compile(r'(?i)^l *= *(?P<locale>[\S\s]*)$')

        # st=Marthahalli
        p12 = re.compile(r'(?i)^st *= *(?P<street>[\S\s]*)$')
    
        # hostname=pnp-agent
        p13 = re.compile(r'(?i)^hostname *= *(?P<hostname>[\S\s]*)$')

        # e=ashpa@cisco.com
        p14 = re.compile(r'(?i)^e *= *(?P<email>[\S\s]*)$')

        # IP Address: 10.10.10.1
        p15 = re.compile(r'(?i)^IP Address: *(?P<ip_address>[\S\s]*)$')

        # Serial Number: 9AH31HA
        p16 = re.compile(r'(?i)^Serial Number: *(?P<serial_number>[\S\s]*)$')

        # start date: 21:58:50 IST Nov 10 2021
        # end   date: 21:58:50 IST Nov 10 2024
        # renew date: 21:58:50 IST Nov 10 2023
        p17 = re.compile(r'^((?P<start_date>start +date)|(?P<end_date>end +date)|(?P<renew_date>renew +date)): +(?P<value>.*)$')
    
        # Public Key Algorithm: rsaEncryption
        p18 = re.compile(r'^Public Key Algorithm: +(?P<key_type>\w+)$')

        # RSA Public Key: (2048 bit)
        p19 = re.compile(r'^(RSA|EC) Public Key: +\((?P<key_len>\d+) +bit\)$')

        # Signature Algorithm: SHA1 with RSA Encryption
        p20 = re.compile(r'^Signature Algorithm: +(?P<sign_algo>.*)$')

        # Fingerprint MD5: D9E4599D C573463B 07F2FBD6 620DB523 
        p21 = re.compile(r'^Fingerprint MD5: +(?P<fp_md5>.*)$')

        # Fingerprint SHA1: E8E0731C D31EA142 A23066D7 4178D696 2D9815E0
        p22 = re.compile(r'^Fingerprint SHA1: +(?P<fp_sha1>.*)$')
    
        # http://10.10.10.2/test.crl
        p23 = re.compile(r'^(?P<cdp_value>(http|ldap).*\.crl)$')

        # X509v3 Key Usage: A0000000
        p24 = re.compile(r'^(?P<key_usage>X509v3 Key Usage): *(?P<key_usage_hex>.*)$')

        # Digital Signature
        # Key Encipherment
        p25 = re.compile(r'^(?P<key_purpose>(Digital Signature|Non Repudiation|Key Encipherment|Data Encipherment|Key Agreement|Key Cert Sign|CRL Signature|Encipher Only|Decipher Only))$')

        # X509v3 Subject Key ID: 2F6A8670 6934D26E C27965E8 67C70441 BEF2EAFC 
        p26 = re.compile(r'^X509v3 Subject Key ID: +(?P<subject_key>[\S\s]*)$')

        # www.cisco.com
        p27 = re.compile(r'^(?P<subj_fqdn>(www|mail|ftp|store|support).*)$')

        # IP Address : 10.10.10.1
        p28 = re.compile(r'^IP Address : +(?P<subj_addr>.*)$')

        # OtherNames : ashpa@cisco.com
        p29 = re.compile(r'^OtherNames : +(?P<subj_other>.*)$')

        # X509v3 Authority Key ID: 31DEF8AC 8ED9E5F0 CDBC4749 61BED767 0CF75DB2
        p30 = re.compile(r'^X509v3 Authority Key ID: +(?P<authority_key>[\S\s]*)$')

        # OCSP URL: http://9.41.19.4/ocsp
        p31 = re.compile(r'^OCSP URL: +(?P<ocsp_url>.*)$')

        # CA: TRUE
        p32 = re.compile(r'^CA: +(?P<ca_flag>\w+)$')
        
        # Client Auth
        # Server Auth
        p33 = re.compile(r'^(?P<eku>((Server|Client) Auth|IPSEC (End System|Tunnel|User)|SSH (Server|Client)|Code Signing|Email Protection|OCSP Signing|Time Stamping|[\d\.]+))$')
        
        # Cert install time: 21:57:41 IST Nov 10 2021
        p34 = re.compile(r'^Cert install time: +(?P<install_time>.*)$')

        # Associated Trustpoints: client ROOT 
        p35 = re.compile(r'^Associated Trustpoints: +(?P<tp>.*)$')

        # Storage: nvram
        p36 = re.compile(r'^Storage: +(?P<storage>.*)$')

        # Key Label: client
        p37 = re.compile(r'^Key Label: +(?P<label>.*)$')

        # Key storage device: nvram:client.cer#
        p38 = re.compile(r'^Key storage device: +(?P<key_device>.*)$')
        
        ###Variables###
        cdp_incr_count = 0
        key_usage_count = 0
        eku_count = 0
        ###############


        for line in output.splitlines():
            line = line.strip()

            # CA Certificate
            # Certificate
            # Certificate (Rollover)
            # CA Certificate (Rollover)
            # Certificate (subordinate CA certificate)
            # Certificate (subordinate CA certificate, Rollover)
            # Certificate (RA mode CS certificate)
            # Certificate (RA mode CS certificate, Rollover)
            m = p1.match(line)
            if m:
                if m.groupdict()['cer']:
                    cer_type = 'certificate'
                elif m.groupdict()['cer_rollover']:
                    cer_type = m.groupdict()['cer_rollover'].lower().replace(" ", "_").replace("(", "").replace(")","")
                elif m.groupdict()['cer_sub_ra']:
                    cer_type = m.groupdict()['cer_sub_ra'].lower().replace("certificate ","").replace(" ", "_").replace("(", "").replace(")","")
                elif m.groupdict()['cer_sub_ra_rollover']:
                    cer_type = m.groupdict()['cer_sub_ra_rollover'].lower().replace("certificate ","").replace(" ", "_").replace("(", "").replace(")","").replace(",", "")
                else:
                    cer_type = m.groupdict()['cer_name'].lower().replace(" ", "_").replace("-", "_")
                cer_dict = ret_dict.setdefault('certificates', {}).setdefault(cer_type, {}) 
                continue

            # Status: Available
            m = p2.match(line)
            if m:
                cer_dict['status'] = m.groupdict()['status']
                continue
             
            # Certificate Serial Number (hex): 01
            m = p3.match(line)
            if m:
                cer_dict['serial'] = m.groupdict()['serial']
                continue

            # Certificate Usage: Signature
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

            # cn=ROOT
            m = p6.match(line)
            if m:
                sub_dict['common_name'] = m.groupdict()['common_name']
                continue
 
            # ou=PKI 
            m = p7.match(line)
            if m:
                sub_dict['organization'] = m.groupdict()['organization']
                continue
            
            # Name: pki-reg7
            m = p8.match(line)
            if m:
                sub_dict['name'] = m.groupdict()['name']
                continue

            # ou=EN
            m = p9.match(line)
            if m:
                sub_dict['organizational_unit'] = m.groupdict()['organizational_unit']
                continue
            
            # c=IN
            m = p10.match(line)
            if m:
                sub_dict['country'] = m.groupdict()['country']
                continue

            # l=Bangalore 
            m = p11.match(line)
            if m:
                sub_dict['locale'] = m.groupdict()['locale']
                continue


            # st=Marthahalli
            m = p12.match(line)
            if m:
                sub_dict['street'] = m.groupdict()['street']
                continue

            # hostname=pnp-agent   
            m = p13.match(line)
            if m:
                sub_dict['hostname'] = m.groupdict()['hostname']
                continue

            # e=ashpa@cisco.com   
            m = p14.match(line)
            if m:
                sub_dict['email'] = m.groupdict()['email']
                continue

            # IP address: 10.10.10.1
            m = p15.match(line)
            if m:
                sub_dict['ip_address'] = m.groupdict()['ip_address']
                continue

            # Serial Number: 9AH31HA
            m = p16.match(line)
            if m:
                sub_dict['serial_number'] = m.groupdict()['serial_number']
                continue

            # start date: 21:58:50 IST Nov 10 2021
            # end   date: 21:58:50 IST Nov 10 2024
            # renew date: 21:58:50 IST Nov 10 2023
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if group['start_date']:
                    sub_dict['start_date'] = group['value']
                if group['end_date']:
                    sub_dict['end_date'] = group['value']
                if group['renew_date']:
                    sub_dict['renew_date'] = group['value'] 


            # Public Key Algorithm: rsaEncryption
            m = p18.match(line)
            if m:
                sub_dict = cer_dict.setdefault('subject_key_info', {})
                sub_dict['key_algorithm'] = m.groupdict()['key_type']
                continue

            # RSA Public Key: (2048 bit)
            m = p19.match(line)
            if m:
                sub_dict['key_length'] = m.groupdict()['key_len']
                continue

            # Signature Algorithm: SHA1 with RSA Encryption
            m = p20.match(line)
            if m:
                cer_dict['signature_algorithm'] = m.groupdict()['sign_algo']
                continue

            # Fingerprint MD5: D9E4599D C573463B 07F2FBD6 620DB523
            m = p21.match(line)
            if m:
                cer_dict['fingerprint_md5'] = m.groupdict()['fp_md5']
                continue

            # Fingerprint SHA1: E8E0731C D31EA142 A23066D7 4178D696 2D9815E0
            m = p22.match(line)
            if m:
                cer_dict['fingerprint_sha1'] = m.groupdict()['fp_sha1']
                continue
            
            # http://10.10.10.2/test.crl
            m = p23.match(line)
            if m:
                sub_dict = cer_dict.setdefault('cdp', {})
                cdp_incr_count += 1
                sub_dict["cdp_url_{}".format(cdp_incr_count)] = m.groupdict()['cdp_value']
                continue

            # X509v3 Key Usage: A0000000
            m = p24.match(line)
            if m:
                cer_dict['key_usage_hex'] = m.groupdict()['key_usage_hex']
                sub_dict = cer_dict.setdefault('key_usage', {})
                continue

            # Digital Signature
            # Key Encipherment
            m = p25.match(line)
            if m:
                key_usage_count += 1
                sub_dict["key_usage_{}".format(key_usage_count)] = m.groupdict()['key_purpose']
                continue

            # X509v3 Subject Key ID: 2F6A8670 6934D26E C27965E8 67C70441 BEF2EAFC 
            m = p26.match(line)
            if m:
                cer_dict['subject_key_id'] = m.groupdict()['subject_key']
                continue
    
        
            # www.cisco.com
            m = p27.match(line)
            if m:
                sub_dict = cer_dict.setdefault('subj_alt_name', {})
                sub_dict["subj_alt_fqdn"] = m.groupdict()['subj_fqdn']
                continue

            # IP Address : 10.10.10.1
            m = p28.match(line)
            if m:
                sub_dict = cer_dict.setdefault('subj_alt_name', {})
                sub_dict["subj_alt_ip_addr"] = m.groupdict()['subj_addr']
                continue
            
            # OtherNames : ashpa@cisco.com
            m = p29.match(line)
            if m:
                sub_dict = cer_dict.setdefault('subj_alt_name', {})
                sub_dict["subj_alt_other_names"] = m.groupdict()['subj_other']
                continue

            # X509v3 Authority Key ID: 31DEF8AC 8ED9E5F0 CDBC4749 61BED767 0CF75DB2
            m = p30.match(line)
            if m:
                cer_dict['authority_key_id'] = m.groupdict()['authority_key']
                continue
            
            # OCSP URL: http://9.41.19.4/ocsp
            m = p31.match(line)
            if m:
                cer_dict['ocsp_url'] = m.groupdict()['ocsp_url']
                continue

            # CA: TRUE
            m = p32.match(line)
            if m:
                cer_dict['ca_flag'] = m.groupdict()['ca_flag']
                continue

            # Client Auth
            # Server Auth
            m = p33.match(line)
            if m:
                sub_dict = cer_dict.setdefault('extended_key_unit', {})
                eku_count += 1
                sub_dict["eku_{}".format(eku_count)] = m.groupdict()['eku']
                continue
            
            # Cert install time: 21:57:41 IST Nov 10 2021
            m = p34.match(line)
            if m:
                cer_dict['cert_install_time'] = m.groupdict()['install_time']
                continue

            # Associated Trustpoints: client ROOT 
            m = p35.match(line)
            if m:
                cdp_incr_count = 0
                key_usage_count = 0
                eku_count = 0
                cer_dict['trustpoints'] = m.groupdict()['tp']
                continue

            # Storage: nvram
            m = p36.match(line)
            if m:
                cer_dict['storage'] = m.groupdict()['storage']
                continue
   
            # Key Label: client
            m = p37.match(line)
            if m:
                cer_dict['key_label'] = m.groupdict()['label']
                continue

            # Key storage device: nvram:client.cer#
            m = p38.match(line)
            if m:
                cer_dict['key_store'] = m.groupdict()['key_device']
                continue
        
        return ret_dict 

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



class ShowCryptoSessionSchema(MetaParser):
    ''' Schema for show crypto session detail
        Schema for show crypto session'''
    schema = {
    "interface":{
        Any():
        {
            Optional("uptime"): str,
            Optional("user_name"): str,
            Optional("profile"): str,
            Optional("group"): str,
            Optional("assigned_address"):str,
            "session_status": str,
            "peer":{
                Any():
                {
                    "port":{
                        Any():
                        {
                        Optional("fvrf"): str,
                        Optional("ivrf"): str,
                        Optional("phase1_id"): str,
                        Optional("desc"): str,
                        "ike_sa":{
                            Any():
                            {
                                "local": str,
                                "local_port": str,
                                "remote": str,
                                "remote_port": str,
                                "sa_status": str,
                                "version":str,
                                Optional("capabilities"):str,
                                Optional("lifetime"): str,
                                Optional("conn_id"):str,
                                Optional("session_id"): str
                            },
                        },
                        "ipsec_flow": {
                            Any():
                                {
                                "active_sas": int,
                                "origin": str,
                                Optional("inbound_pkts_decrypted"): int,
                                Optional("inbound_pkts_drop"): int,
                                Optional("inbound_life_kb"): str,
                                Optional("inbound_life_secs"): str,
                                Optional("outbound_pkts_encrypted"): int,
                                Optional("outbound_pkts_drop"): int,
                                Optional("outbound_life_kb"): str,
                                Optional("outbound_life_secs"): str
                                },
                            }
                        },
                    }
                },
            }   
        },
    }
}
                                
class ShowCryptoSessionSuperParser(ShowCryptoSessionSchema):

    """Super Parser for 
        * 'show crypto session'
        * 'show crypto session detail'
    """
    
    cli_command = "show crypto session {detail}"

    def cli(self, output=None):

        #Interface: Tunnel13
        p1=re.compile(r'^Interface\:\s+(?P<interface_name>.+)$')

        #Uptime: 5d23h
        p2=re.compile(r'^Uptime\:\s+(?P<up_time>\S+)$')

        #Username: cisco
        p3=re.compile(r'^Username\:\s+(?P<user_name>.+)$')

        #Profile: prof
        p4=re.compile(r'^Profile\:\s+(?P<profile>.+)$')

        #Group: easy
        p5=re.compile(r'^Group\:\s+(?P<group>.+)$')

        #Assigned address: 10.3.3.4
        p6=re.compile(r'^Assigned\s+address\:\s+(?P<assigned_address>[\d\.]+)$')

        #Session status: UP-ACTIVE
        p7=re.compile(r'^Session\s+status\:\s+(?P<session_status>[\w-]+)')

        #Peer: 11.0.1.2 port 500
        #Peer: 11.0.1.2 port 500 fvrf: (none) ivrf: (none)
        p8=re.compile(r'^Peer\:\s+(?P<peer>[\d\.]+)\s+port\s+(?P<port>\d+)(\s+fvrf\:\s+\(*(?P<fvrf>none|[^(]\S+)\)*\s+ivrf\:\s+\(*(?P<ivrf>none|[^(]\S+)\)*)?')
        
        # Phase1_id: 11.0.1.2
        p9=re.compile(r'^\s*Phase1\_id\:\s+(?P<phase_id>\S+)$')

        # Desc: (none)
        p10=re.compile(r'^\s*Desc\:\s+\(?(?P<desc>none|.*)\)?$')

        # Session ID: 0  
        p11=re.compile(r'^\s*Session\s+ID\:\s+(?P<session_id>\d+)$')

        #IKEv1 SA: local 11.0.1.1/500 remote 11.0.1.2/500 Active 
        p12=re.compile(r'^\s*(?P<version>IKE(v\d)*)*\s+SA\:\s+local\s+(?P<local>[\d\.]+)\/(?P<local_port>\d+)\s+remote\s+(?P<remote>[\d\.]+)\/(?P<remote_port>\d+)\s+(?P<conn_status>\w+)$')

        #  Capabilities:(none) connid:1025 lifetime:03:04:13
        p13=re.compile(r'^\s*Capabilities\:\(*(?P<capabilities>\w+)+\)*\s+connid\:(?P<conn_id>\d+)\s+lifetime\:(?P<lifetime>[\d\:]+)$')

        # IPSEC FLOW: permit 47 host 11.0.1.1 host 11.0.1.2 
        p14=re.compile(r'^\s*IPSEC\s+FLOW\:\s+(?P<ipsec_flow>.+)$')

        #Active SAs: 2, origin: crypto map
        p15=re.compile(r'^\s*Active\s+SAs\:\s+(?P<active_sa>\d+)\,\s+origin\:\s+(?P<origin>[\w\s]+)$')

        #Inbound:  #pkts dec'ed 4172534851 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p16=re.compile(r'^\s*Inbound\:\s+\#pkts\s+dec\'ed\s+(?P<inbound_pkts_dec>\d+)\s+drop\s+(?P<inbound_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<inbound_life_kb>[\w\s]+)\/(?P<inbound_life_secs>\w+)$')

        #Outbound: #pkts enc'ed 4146702954 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p17=re.compile(r'^\s*Outbound\:\s+\#pkts\s+enc\'ed\s+(?P<outbound_pkts_enc>\d+)\s+drop\s+(?P<outbound_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<outbound_life_kb>[\w\s]+)\/(?P<outbound_life_secs>\w+)$')

        
        ret_dict = {}
        check_flag = 1
        peer_flag = 1
        sa_flag = 1
        flow_flag = 1
        ike_index = 1
        session_id = None
        
        for line in output.splitlines():
            line = line.strip()
            if check_flag==1:
                ret_dict['interface']={}
                crypto_session_dict=ret_dict['interface']
                check_flag=0
         
            #Interface: Tunnel0
            m1= p1.match(line)
            if m1:
                groups=m1.groupdict()
                crypto_session_dict[groups['interface_name']]={}
                interface_dict=crypto_session_dict[groups['interface_name']]
            
            #Uptime: 3d18h
            m2= p2.match(line)
            if m2:
                groups=m2.groupdict()
                interface_dict['uptime']=groups['up_time']

            #Username: cisco
            m3=p3.match(line)
            if m3:
                groups=m3.groupdict()
                interface_dict['user_name']=groups['user_name']
            
            #Profile: prof
            m4=p4.match(line)
            if m4:
                groups=m4.groupdict()
                interface_dict['profile']=groups['profile']
            
            #Group: easy
            m5=p5.match(line)
            if m5:
                groups=m5.groupdict()
                interface_dict['group']=groups['group']
            
            #Assigned address: 10.3.3.4
            m6=p6.match(line)
            if m6:
                groups=m6.groupdict()
                interface_dict['assigned_address']=groups['assigned_address']

            #Session status: UP-ACTIVE
            m7= p7.match(line)
            if m7:
                groups=m7.groupdict()
                interface_dict['session_status']=groups['session_status']

            #Peer: 10.1.1.2 port 500
            #Peer: 10.1.1.3 port 500 fvrf: (none) ivrf: (none)
            m8= p8.match(line)
            if m8:
                if peer_flag==1:
                    interface_dict['peer']={}
                    tunnel_dict= interface_dict['peer']
                    peer_flag=0

                groups=m8.groupdict()
                tunnel_dict[groups['peer']]={}
                peer_dict= tunnel_dict[groups['peer']]
                peer_dict['port']={}
                port_dict=peer_dict['port']
                port_dict[groups['port']]={}
                ike_dict= port_dict[groups['port']]
                if groups['fvrf']:
                    ike_dict['fvrf']=groups['fvrf']
                    ike_dict['ivrf']=groups['ivrf'] 

            #Phase1_id: 10.1.1.3
            m9= p9.match(line)
            if m9:
                groups=m9.groupdict()
                ike_dict['phase1_id']=groups['phase_id']

            #Desc: this is my peer at 10.1.1.3:500 Green
            m10= p10.match(line)
            if m10:
                groups=m10.groupdict()
                ike_dict['desc']=groups['desc']

            #Session ID: 0
            m11= p11.match(line)
            if m11:
                groups=m11.groupdict()
                session_id= groups['session_id']
            
            #IKE SA: local 10.1.1.4/500 remote 10.1.1.3/500 Active
            m12= p12.match(line)
            if m12:
                groups=m12.groupdict()
                if sa_flag==1:
                    ike_dict['ike_sa']={}
                    ike_version_dict= ike_dict['ike_sa']
                    sa_flag=0

                ike_version_dict[str(ike_index)]={}
                ike_params_dict=ike_version_dict[str(ike_index)]
                ike_index+= 1

                ike_params_dict['local'] =groups['local']
                ike_params_dict['local_port'] =groups['local_port']
                ike_params_dict['remote'] = groups['remote']
                ike_params_dict['remote_port']= groups['remote_port']
                ike_params_dict['sa_status']= groups['conn_status']
                ike_params_dict['version']= groups['version']
                if session_id is not None:
                    ike_params_dict['session_id']= session_id

            #Capabilities:D connid:1042 lifetime:05:50:03
            m13= p13.match(line)
            if m13:
                groups=m13.groupdict()
                ike_params_dict['conn_id'] = groups['conn_id']
                ike_params_dict['capabilities']= groups['capabilities']
                ike_params_dict['lifetime']= groups['lifetime']

            #IPSEC FLOW: permit 47 host 11.0.2.2 host 11.0.2.1     
            m14= p14.match(line)
            if m14:
                if flow_flag==1:
                    ike_dict['ipsec_flow']={}
                    ipsec_flow_dict= ike_dict['ipsec_flow']
                    flow_flag=0

                groups= m14.groupdict()
                ipsec_flow_dict[groups['ipsec_flow']]={}
                counter_dict=ipsec_flow_dict[groups['ipsec_flow']]

            # Active SAs: 2, origin: crypto map     
            m15= p15.match(line)
            if m15:
                groups=m15.groupdict()
                counter_dict['active_sas']= int(groups['active_sa'])
                counter_dict['origin']= groups['origin']

            #Inbound:  #pkts dec'ed 449282 drop 0 life (KB/Sec) KB Vol Rekey Disabled/3060
            m16= p16.match(line)
            if m16:
                groups=m16.groupdict()
                counter_dict['inbound_pkts_decrypted']=int(groups['inbound_pkts_dec'])
                counter_dict['inbound_pkts_drop']=int(groups['inbound_drop'])
                counter_dict['inbound_life_kb']=groups['inbound_life_kb']
                counter_dict['inbound_life_secs']=groups['inbound_life_secs']

            #Outbound: #pkts enc'ed 772730 drop 0 life (KB/Sec) KB Vol Rekey Disabled/3060
            m17= p17.match(line)
            if m17:
                groups=m17.groupdict()
                counter_dict['outbound_pkts_encrypted']=int(groups['outbound_pkts_enc'])
                counter_dict['outbound_pkts_drop']=int(groups['outbound_drop'])
                counter_dict['outbound_life_kb']=groups['outbound_life_kb']
                counter_dict['outbound_life_secs']=groups['outbound_life_secs']
        return ret_dict

class ShowCryptoSession(ShowCryptoSessionSuperParser,ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session'
    '''

    cli_command = "show crypto session"

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

class ShowCryptoSessionDetail(ShowCryptoSessionSuperParser,ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session detail'
    '''

    cli_command = "show crypto session detail"

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)
