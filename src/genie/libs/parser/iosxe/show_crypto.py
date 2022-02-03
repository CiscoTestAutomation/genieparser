"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto pki certificates <WORD>
   * show crypto entropy status
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

# =====================================
# Schema for:
#  * 'show crypto entropy status' 
# =====================================
class ShowCryptoEntropyStatusSchema(MetaParser):
    """Schema for show crypto entropy status."""

    schema = {
        "entropy_collection": str,
        "entropy_collection_recent": str,
        "Entropy_target": str,
        "entropy_actual_collection" : str,
        "entropies" : {
            int : {
                "source": str,
                "type": str,
                "status": str,
                "requests": str,
                "entropy_bits": str,
            }
        }
    }
# =====================================
# Parser for:
#  * 'show crypto entropy status'
# =====================================
class ShowCryptoEntropyStatus(ShowCryptoEntropyStatusSchema):
    """Parser for show crypto entropy status"""

    cli_command = 'show crypto entropy status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
		## Entropy source       Type Status  Entropy Bits
		#1 ACT-2                 HW  Working  384
		#2 randfill              SW  Working  128(*)
        #3 getrandombytes        SW  Working  160(*)
        p1 = re.compile(r"^(?P<count>\d+)\s+(?P<source>\S+)\s+(?P<type>\S+)\s+(?P<status>\S+)(\s+|\s+(?P<requests>\d+)\s+)(?P<entropy_bits>(\S+|\d+\/\d+\s+\(\*\)))$")
							
	    #Fresh entropy collected once every 60 minutes
        p2 = re.compile(r'^Fresh +entropy +collected +once +every +(?P<total>[\d\s\w]+)$')
											   
		#Entropy most recently collected 22 minutes ago
        p3 = re.compile(r'^Entropy +most +recently +collected +(?P<count>[\d\s\w]+)$')
		
		#Entropy target = 256 bits; entropy actually collected = 384 bits
        p4 = re.compile(r'^Entropy +target\s+=\s+(?P<count1>[\d\s\w]+);\s+entropy +actually +collected\s+=\s+(?P<count2>[\d\s\w]+)$')

        chassis_obj = {}
        
        for line in output.splitlines():
            line = line.strip()
                    
            m=p1.match(line)
            if m:
                group = m.groupdict()
                entry_dict = chassis_obj.setdefault("entropies", {})
                count = int(group["count"])
                entry_dict.update(
                    { int(count) : {
                        "source" : group["source"],
                        "type" : group["type"],
                        "status" : group["status"],
                        "requests" : str(group["requests"]),
                        "entropy_bits" : group["entropy_bits"],
                                }
                            }
                        )
                continue 

            m = p2.match(line)
            if m:
                group = m.groupdict()
                chassis_obj['entropy_collection'] = group['total']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                chassis_obj['entropy_collection_recent'] = group['count']
                continue
                    
            m = p4.match(line)
            if m:
                group = m.groupdict()
                chassis_obj['Entropy_target'] = group['count1']
                chassis_obj['entropy_actual_collection'] = group['count2']
                
        return chassis_obj

# =================================================
#  Schema for 'show crypto pki server'
# =================================================
class ShowCryptoPkiServerSchema(MetaParser):
    """Schema for show crypto pki server"""
    schema = {
        'server':{
            Any():
                {
                    'status': str, 
                    'state': str, 
                    'issuer': str,
                    'fingerprint': str,
                    Optional('subca_fingerprint'): str,
                    Optional('ra_fingerprint'): str,
                    Optional('ca_type'): str,
                    Optional('grant_mode'): str,
                    Optional('last_serial_num'): str,
                    'ca_expiry_timer': str,
                    Optional('crl_next_update_timer'): str,
                    Optional('primary_storage'): str,
                    Optional('database_level'): str,
                    Optional('auto_rollover_timer'): str
                },
            },
        }

# =========================================================
#  Parser for 'show crypto pki server'
# =========================================================   
class ShowCryptoPkiServer(ShowCryptoPkiServerSchema):
    """Parser for 
        * show crypto pki server
    """

    cli_command = 'show crypto pki server'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # Certificate Server root:
        p1 = re.compile(r'^Certificate +Server +(?P<server_name>\S+):$')
    
        # Status: enabled
        p2 = re.compile(r'^Status:\s+(?P<ca_status>\w+)$')

        # State: enabled
        p3 = re.compile(r'^State:\s+(?P<ca_state>\w+)$')
        
        # Issuer name: CN=root
        p4 = re.compile(r'^Issuer\s+name:\s+(?P<cert_issuer>[\S\s]+)$')

        # CA cert fingerprint: CF2C23D1 560F25DB 22E9D10F E595A6D6
        p5 = re.compile(r'^CA\s+cert\s+fingerprint:\s+(?P<ca_fingerprint>[\S\s]+)$')

        # Granting mode is: auto
        p6 = re.compile(r'^Granting\s+mode\s+is:\s+(?P<mode>\w+)$')

        # Last certificate issued serial number (hex): 1
        p7 = re.compile(r'Last\s+certificate\s+issued\s+serial\s+number\s+\(hex\):\s+(?P<serial>\S+)$')

        # CA certificate expiration timer: 12:58:34 UTC Jan 4 2025
        p8 = re.compile(r'^CA\s+certificate\s+expiration\s+timer:\s+(?P<ca_expiry>[\S\s]+)$')

        # CRL NextUpdate timer: 18:58:35 UTC Jan 5 2022
        p9 = re.compile(r'^CRL\s+NextUpdate\s+timer:\s+(?P<crl_update>[\S\s]+)$')

        # Current primary storage dir: nvram:
        p10 = re.compile(r'^Current\s+primary\s+storage\s+dir:\s+(?P<storage>\S+)$')

        # Database Level: Complete - all issued certs written as <serialnum>.cer 
        p11 = re.compile(r'^Database Level:\s+(?P<level>\w+)$')

        # Autorollover timer: 12:58:34 UTC Jan 3 2025
        p12 = re.compile(r'^Autorollover\s+timer:\s+(?P<rollover_timer>[\S\s]+)$')

        # Upper CA cert fingerprint: 8EF4710D 2C01F563 2ADBFC3C 716442CC
        p13 = re.compile(r'^Upper\s+CA\s+cert\s+fingerprint:\s+(?P<subca_fp>[\S\s]+)$')

        # RA cert fingerprint: 885DA102 58DDDE50 3ECBA461 C0E71AEB
        p14 = re.compile(r'^RA\s+cert\s+fingerprint:\s+(?P<ra_fp>[\S\s]+)$')

        # Server configured in RA mode
        p15 = re.compile(r'^Server\s+configured\s+in\s+(?P<type>[\S\s]+)\s+mode$')

        for line in output.splitlines():
            line = line.strip()
            # Certificate Server root:
            m = p1.match(line)
            if m:
                ca_name = m.groupdict()['server_name']
                ser_dict = ret_dict.setdefault('server', {}).setdefault(ca_name, {}) 
                continue

            # Status: enabled
            m = p2.match(line)
            if m:
                ser_dict['status'] = m.groupdict()['ca_status']
                continue
             
            # State: enabled
            m = p3.match(line)
            if m:
                ser_dict['state'] = m.groupdict()['ca_state']
                continue

            # Issuer name: CN=root
            m = p4.match(line)
            if m:
                ser_dict['issuer'] = m.groupdict()['cert_issuer']
                continue
     
            # CA cert fingerprint: CF2C23D1 560F25DB 22E9D10F E595A6D6
            m = p5.match(line)
            if m:
                ser_dict['fingerprint'] = m.groupdict()['ca_fingerprint']
                continue

            # Granting mode is: auto
            m = p6.match(line)
            if m:
                ser_dict['grant_mode'] = m.groupdict()['mode']
                continue
 
            # Last certificate issued serial number (hex): 1
            m = p7.match(line)
            if m:
                ser_dict['last_serial_num'] = m.groupdict()['serial']
                continue
            
            # CA certificate expiration timer: 12:58:34 UTC Jan 4 2025
            m = p8.match(line)
            if m:
                ser_dict['ca_expiry_timer'] = m.groupdict()['ca_expiry']
                continue

            # CRL NextUpdate timer: 18:58:35 UTC Jan 5 2022
            m = p9.match(line)
            if m:
                ser_dict['crl_next_update_timer'] = m.groupdict()['crl_update']
                continue
            
            # Current primary storage dir: nvram:
            m = p10.match(line)
            if m:
                ser_dict['primary_storage'] = m.groupdict()['storage']
                continue

            # Database Level: Complete - all issued certs written as <serialnum>.cer 
            m = p11.match(line)
            if m:
                ser_dict['database_level'] = m.groupdict()['level']
                continue


            # Autorollover timer: 12:58:34 UTC Jan 3 2025
            m = p12.match(line)
            if m:
                ser_dict['auto_rollover_timer'] = m.groupdict()['rollover_timer']
                continue
            
            # Upper CA cert fingerprint: 8EF4710D 2C01F563 2ADBFC3C 716442CC
            m = p13.match(line)
            if m:
                ser_dict['subca_fingerprint'] = m.groupdict()['subca_fp']
                continue

            # RA cert fingerprint: 885DA102 58DDDE50 3ECBA461 C0E71AEB
            m = p14.match(line)
            if m:
                ser_dict['ra_fingerprint'] = m.groupdict()['ra_fp']
                continue

            # Server configured in RA mode
            m = p15.match(line)
            if m:
                ser_dict['ca_type'] = m.groupdict()['type']
                continue

        return ret_dict 

# =================================================
#  Schema for 'show crypto pki timer detail'
# =================================================
class ShowCryptoPkiTimerDetailSchema(MetaParser):
    """  Schema for show crypto pki timer detail """
    schema = {
        'timer':{
            'session_cleanup': str,
            'session_cleanup_iso': str, 
            Optional('renew_timer'): str, 
            Optional('renew_timer_iso'): str,
            Optional('shadow_timer'): str, 
            Optional('shadow_timer_iso'): str,
            Optional('poll_timer'): str, 
            Optional('poll_timer_iso'): str,
            Optional('expiry_alert_id'): str,
            Optional('expiry_alert_id_iso'): str,
            Optional('expiry_alert_ca'): str,
            Optional('expiry_alert_ca_iso'): str,
            Optional('crl_expire'): str,
            Optional('crl_expire_iso'): str,
            Optional('crl_update'): str,
            Optional('crl_update_iso'): str,
            Optional('crl_dwnld_retry'): str,
            Optional('crl_dwnld_retry_iso'): str,
            Optional('trustpool_timer'): str,
            Optional('trustpool_timer_iso'): str,
            Optional('est_connect_retry'): str,
            Optional('est_connect_retry_iso'): str,
            Optional('cs_crl_update'): str,
            Optional('cs_crl_update_iso'): str,
            Optional('cs_shadow_gen'): str,
            Optional('cs_shadow_gen_iso'): str,
            Optional('cs_cert_expiry'): str,
            Optional('cs_cert_expiry_iso'): str,
            Optional('enroll_req_expiry'): str,
            Optional('enroll_req_expiry_iso'): str
            },
        }

# =========================================================
#  Parser for 'show crypto pki timer <>'
# =========================================================   
class ShowCryptoPkiTimerDetail(ShowCryptoPkiTimerDetailSchema):
    """Parser for 
        * show crypto pki timer detail
    """

    cli_command = 'show crypto pki timer detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        #  |        8:02.030  (2022-01-16T03:09:36Z) SESSION CLEANUP
        p1 = re.compile(r'^\s*\|?\s*(?P<sess_cleanup>\S+)\s+\((?P<sess_cleanup_iso>\S+)\)\s+SESSION\s+CLEANUP$')
    
        # |291d23:59:52.231  (2022-11-04T03:01:26Z) RENEW client
        p2 = re.compile(r'^\s*\|?\s*(?P<renew>\S+)\s+\((?P<renew_iso>\S+)\)\s+RENEW\s+\S+$')

        #  |985d11:54:30.614  (2024-09-26T20:48:17Z) SHADOW client
        p3 = re.compile(r'^\s*\|?\s*(?P<shadow>\S+)\s+\((?P<shadow_iso>\S+)\)\s+SHADOW\s+\S+$')
        
        # |          57.782  (2022-01-16T05:02:44Z) POLL client
        p4 = re.compile(r'^\s*\|?\s*(?P<poll>\S+)\s+\((?P<poll_iso>\S+)\)\s+POLL\s+\S+$')

        # |304d23:54:53.213  (2022-11-17T03:01:26Z) ID(client)
        p5 = re.compile(r'^\s*\|?\s*(?P<expiry_id>\S+)\s+\((?P<expiry_id_iso>\S+)\)\s+ID\(\S+\)$')

        # |1034d 5:41:45.106  (2024-11-15T08:48:18Z) CS(root)
        p6 = re.compile(r'^\s*\|?\s*(?P<expiry_ca>\S+)\s+\((?P<expiry_ca_iso>\S+)\)\s+CS\(\S+\)$')

        #  |     5:58:01.690  (2022-01-16T19:51:22Z) CRL EXPIRE c=US,o=Let's Encrypt,cn=R3
        p7 = re.compile(r'^\s*\|?\s*(?P<crl_exp>\S+)\s+\((?P<crl_exp_iso>\S+)\)\s+CRL\s+EXPIRE\s+\S+$')

        #|     5:58:01.690  (2022-01-16T19:51:22Z) CRL UPDATE *c=US,o=Let's Encrypt,cn=R3
        p8 = re.compile(r'^\s*\|?\s*(?P<crl_up>\S+)\s+\((?P<crl_up_iso>\S+)\)\s+CRL\s+UPDATE\s+\S+$')

        #|       29:47.358  (2022-01-16T03:36:20Z) CRL auto-download retry timer
        p9 = re.compile(r'^\s*\|?\s*(?P<crl_dnld>\S+)\s+\((?P<crl_dnld_iso>\S+)\)\s+CRL\s+auto-download\s+retry\s+timer$')

        # |2655d22:49:09.717  (2029-04-25T01:55:42Z) TRUSTPOOL
        p10 = re.compile(r'^\s*\|?\s*(?P<trustpool>\S+)\s+\((?P<trustpool_iso>\S+)\)\s+TRUSTPOOL$')

        #| 6.908 (2020-05-02T04:10:40Z) CONNECT RETRY estclient
        p11 = re.compile(r'^\s*\|?\s*(?P<est_retry>\S+)\s+\((?P<est_retry_iso>\S+)\)\s+CONNECT\s+RETRY\s+\S+$')

        # |     5:40:16.483  (2022-01-16T08:46:49Z) CS CRL UPDATE
        p12 = re.compile(r'^\s*\|?\s*(?P<cs_crl>\S+)\s+\((?P<cs_crl_iso>\S+)\)\s+CS\s+CRL\s+UPDATE$')

        # |1094d 5:21:45.573  (2025-01-14T08:28:18Z) CS SHADOW CERT GENERATION
        p13 = re.compile(r'^\s*\|?\s*(?P<cs_shadow>\S+)\s+\((?P<cs_shadow_iso>\S+)\)\s+CS\s+SHADOW\s+CERT\s+GENERATION$')

        # |1094d 5:41:45.332  (2025-01-14T08:48:18Z) CS CERT EXPIRE
        p14 = re.compile(r'^\s*\|?\s*(?P<cs_expiry>\S+)\s+\((?P<cs_expiry_iso>\S+)\)\s+CS\s+CERT\s+EXPIRE$')

        # |  6d23:59:57.701  (2025-01-14T08:48:18Z) ER EXPIRE 1
        p15 = re.compile(r'^\s*\|?\s*(?P<er_expiry>\S+)\s+\((?P<er_expiry_iso>\S+)\)\s+ER\s+EXPIRE\s+\d+$')

        for line in output.splitlines():
            line = line.strip()
            #  |        8:02.030  (2022-01-16T03:09:36Z) SESSION CLEANUP
            m = p1.match(line)
            if m:
                ser_dict = ret_dict.setdefault('timer', {})
                ser_dict['session_cleanup'] = m.groupdict()['sess_cleanup']
                ser_dict['session_cleanup_iso'] = m.groupdict()['sess_cleanup_iso']
                continue

            # |291d23:59:52.231  (2022-11-04T03:01:26Z) RENEW client
            m = p2.match(line)
            if m:
                ser_dict['renew_timer'] = m.groupdict()['renew']
                ser_dict['renew_timer_iso'] = m.groupdict()['renew_iso']
                continue
             
            #  |985d11:54:30.614  (2024-09-26T20:48:17Z) SHADOW client
            m = p3.match(line)
            if m:
                ser_dict['shadow_timer'] = m.groupdict()['shadow']
                ser_dict['shadow_timer_iso'] = m.groupdict()['shadow_iso']
                continue

            # |          57.782  (2022-01-16T05:02:44Z) POLL client
            m = p4.match(line)
            if m:
                ser_dict['poll_timer'] = m.groupdict()['poll']
                ser_dict['poll_timer_iso'] = m.groupdict()['poll_iso']
                continue
     
            # |304d23:54:53.213  (2022-11-17T03:01:26Z) ID(client)
            m = p5.match(line)
            if m:
                ser_dict['expiry_alert_id'] = m.groupdict()['expiry_id']
                ser_dict['expiry_alert_id_iso'] = m.groupdict()['expiry_id_iso']
                continue

            # |1034d 5:41:45.106  (2024-11-15T08:48:18Z) CS(root)
            m = p6.match(line)
            if m:
                ser_dict['expiry_alert_ca'] = m.groupdict()['expiry_ca']
                ser_dict['expiry_alert_ca_iso'] = m.groupdict()['expiry_ca_iso']
                continue
 
            #  |     5:58:01.690  (2022-01-16T19:51:22Z) CRL EXPIRE c=US,o=Let's Encrypt,cn=R3
            m = p7.match(line)
            if m:
                ser_dict['crl_expire'] = m.groupdict()['crl_exp']
                ser_dict['crl_expire_iso'] = m.groupdict()['crl_exp_iso']
                continue
            
            #|     5:58:01.690  (2022-01-16T19:51:22Z) CRL UPDATE *c=US,o=Let's Encrypt,cn=R3
            m = p8.match(line)
            if m:
                ser_dict['crl_update'] = m.groupdict()['crl_up']
                ser_dict['crl_update_iso'] = m.groupdict()['crl_up_iso']
                continue

            #|       29:47.358  (2022-01-16T03:36:20Z) CRL auto-download retry timer
            m = p9.match(line)
            if m:
                ser_dict['crl_dwnld_retry'] = m.groupdict()['crl_dnld']
                ser_dict['crl_dwnld_retry_iso'] = m.groupdict()['crl_dnld_iso']
                continue
            
            # |2655d22:49:09.717  (2029-04-25T01:55:42Z) TRUSTPOOL
            m = p10.match(line)
            if m:
                ser_dict['trustpool_timer'] = m.groupdict()['trustpool']
                ser_dict['trustpool_timer_iso'] = m.groupdict()['trustpool_iso']
                continue

            #| 6.908 (2020-05-02T04:10:40Z) CONNECT RETRY estclient
            m = p11.match(line)
            if m:
                ser_dict['est_connect_retry'] = m.groupdict()['est_retry']
                ser_dict['est_connect_retry_iso'] = m.groupdict()['est_retry_iso']
                continue


            # |     5:40:16.483  (2022-01-16T08:46:49Z) CS CRL UPDATE
            m = p12.match(line)
            if m:
                ser_dict['cs_crl_update'] = m.groupdict()['cs_crl']
                ser_dict['cs_crl_update_iso'] = m.groupdict()['cs_crl_iso']
                continue
            
            # |1094d 5:21:45.573  (2025-01-14T08:28:18Z) CS SHADOW CERT GENERATION
            m = p13.match(line)
            if m:
                ser_dict['cs_shadow_gen'] = m.groupdict()['cs_shadow']
                ser_dict['cs_shadow_gen_iso'] = m.groupdict()['cs_shadow_iso']
                continue

            # |1094d 5:41:45.332  (2025-01-14T08:48:18Z) CS CERT EXPIRE
            m = p14.match(line)
            if m:
                ser_dict['cs_cert_expiry'] = m.groupdict()['cs_expiry']
                ser_dict['cs_cert_expiry_iso'] = m.groupdict()['cs_expiry_iso']
                continue

            # Server configured in RA mode
            m = p15.match(line)
            if m:
                ser_dict['enroll_req_expiry'] = m.groupdict()['er_expiry']
                ser_dict['enroll_req_expiry_iso'] = m.groupdict()['er_expiry_iso']
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto pki server <> requests'
# =================================================
class ShowCryptoPkiServerRequestsSchema(MetaParser):
    """  Schema for show crypto pki server <> requests """
    schema = {
                'request': {
                    Any(): {
                        Any(): {
                            Optional('state'): str,
                            Optional('fingerprint'): str,
                            Optional('subject_name'): str
                        },
                    },
                },
            }          
            
        
    

# =========================================================
#  Parser for 'show crypto pki server <> requests'
# =========================================================   
class ShowCryptoPkiServerRequests(ShowCryptoPkiServerRequestsSchema):
    """Parser for 
        * show crypto pki server {server} requests
    """

    cli_command = ['show crypto pki server {server} requests']

    def cli(self, server='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(server=server))

        # initial return dictionary
        ret_dict = {}

        # Subordinate CA certificate requests:
        # RA certificate requests:
        # Router certificates requests:
        p1 = re.compile(r'^(?P<request_type>[\S\s]*) (certificate|certificates) requests:$')
    
        # 1      granted    744566E755B84AEE18A86DF715D8EE33 hostname=pki-reg2.cisco.com,cn=R1 C=pki
        # 2      pending    744866E755B84AEE18A86DF715D8EE33 hostname=pki-reg2.cisco.com,cn=R1 C=pki
        # 3      authorized 744866E755B84AEE18A86DF715D8EE35 hostname=pki-reg2.cisco.com,cn=R1 C=pki
        p2 = re.compile(r'^(?P<serial>\d+)\s+(?P<status>\S+)\s+(?P<fp>\S+)\s+(?P<subject>[\S\s]+)$')

        for line in output.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            
            if m:
                request_type = m.groupdict()['request_type'].lower().replace(" ", "_")
                cert_dict = ret_dict.setdefault('request', {}).setdefault(request_type, {})
                continue
            

            m = p2.match(line)
            if m:
                serial_num = m.groupdict()['serial']
                sub_dict = cert_dict.setdefault(serial_num, {})
                sub_dict['state'] = m.groupdict()['status']
                sub_dict['fingerprint'] = m.groupdict()['fp']
                sub_dict['subject_name'] = m.groupdict()['subject']
                continue

        if ret_dict['request']['ra'] == {}:
            del ret_dict['request']['ra']

        if ret_dict['request']['router'] == {}:
            del ret_dict['request']['router']

        if ret_dict['request']['subordinate_ca'] == {}:
            del ret_dict['request']['subordinate_ca']
        
        return ret_dict
    
# ==============================
# Schema for
#   'show crypto session remote {remote_ip}'
#   'show crypto session remote {remote_ip} detail'
# ==============================
class ShowCryptoSessionRemoteSchema(MetaParser):
    """
    Schema for
        * 'show crypto session remote {remote_ip}'
        * 'show crypto session remote {remote_ip} detail'
    """
    
    schema = {
        'interfaces': {
                Any():{
                    Optional('profile'): str,
                    Optional('uptime'): str,
                    'session_status': str,
                    'peer_ip': str,
                    Optional('peer_port'): int,
                    Optional('fvrf'): str,
                    Optional('ivrf'): str,
                    Optional('phase_id'): str,
                    Optional('session_id'):int,
                    Any():{
                        Optional('local_ip'):str,
                        Optional('local_port'):int,
                        Optional('remote_ip'):str,
                        Optional('remote_port'):int,
                        Optional('capabilities'):str,
                        Optional('connid'):int,
                        Optional('lifetime'):str
                    },
                    Optional('ipsec_flow'):{
                        Any():{
                            Optional('flow'):str,
                            Optional('active_sa'):int,
                            Optional('origin'):str,
                            Optional('inbound'):{
                                Optional('decrypted'):int,
                                Optional('dropped'):int,
                                Optional('life_in_kb'):int,
                                Optional('life_in_sec'):int
                            },
                            Optional('outbound'):{
                                Optional('encrypted'):int,
                                Optional('dropped'):int,
                                Optional('life_in_kb'):int,
                                Optional('life_in_sec'):int
                            },
                        },
                    },
                },
            },
        }
    

class ShowCryptoSessionRemoteSuper(ShowCryptoSessionRemoteSchema):
    """
    Parser for
        * 'show crypto session remote {remote_ip}'
        * 'show crypto session remote {remote_ip} detail'
    """
    
    # Defines a function to run the cli_command
    def cli(self, remote_ip=None, output=None):
        # initial return dictionary
        ret_dict = {}

        # Interface: Virtual-Access1325
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')
    
        # Profile: IKEV2_PROFILE
        p2 = re.compile(r'^Profile:\s+(?P<profile>\S+)$')

        # Uptime: 13:17:14
        p3 = re.compile(r'^Uptime:\s+(?P<up>\S+)$')
        
        # Session status: UP-ACTIVE 
        p4 = re.compile(r'^Session status:\s+(?P<session_stats>\S+)$')

        # Peer: 17.27.1.11 port 38452 fvrf: (none) ivrf: 10
        p5 = re.compile(r'^Peer:\s+(?P<peer>\S+)\s+port\s+(?P<port>\d+)(\s+fvrf:\s+\(?(?P<f_vrf>(\w+|\d+))\)?\s+ivrf:\s+\(?(?P<i_vrf>(\w+|\d+))\)?)?$')

        # Phase1_id: scale
        p6 = re.compile(r'^Phase1_id:\s+(?P<phase_name>\S+)$')

        # Session ID: 22062
        p7 = re.compile(r'^Session\s+ID:\s+(?P<session_num>\S+)$')

        # IKEv2 SA: local 1.1.1.1/4500 remote 17.27.1.11/38452 Active
        p8 = re.compile(r'^(?P<version>\w+)\s+SA:\s+local\s+(?P<localip>\S+)\/(?P<localport>\d+)\s+remote\s+(?P<remoteip>\S+)\/(?P<remoteport>\d+)\s+\S+$')

        # Capabilities:DN connid:323 lifetime:10:43:07
        p9 = re.compile(r'^Capabilities:(?P<caps>\S+)\s+connid:(?P<conn>\d+)\s+lifetime:(?P<life>\S+)$')

        # IPSEC FLOW: permit ip 0.0.0.0/0.0.0.0 host 7.1.2.88 
        p10 = re.compile(r'^IPSEC\s+FLOW:\s+(?P<TS>[\S\s]+)$')

        # Active SAs: 2, origin: crypto map
        p11 = re.compile(r'^Active\s+SAs:\s+(?P<sa_count>\d+)\,\s+origin:\s+(?P<origin_type>[\S\s]+)$')

        # Inbound:  #pkts dec'ed 47668 drop 0 life (KB/Sec) 4607746/1687
        p12 = re.compile(r'^Inbound:\s+#pkts\s+dec\'ed\s+(?P<decrypt_count>\d+)\s+drop\s+(?P<in_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<in_life_kb>\d+)\/(?P<in_life_sec>\d+)$')

        # Outbound: #pkts enc'ed 47672 drop 0 life (KB/Sec) 4607812/1874
        p13 = re.compile(r'^Outbound:\s+#pkts\s+enc\'ed\s+(?P<encrypt_count>\d+)\s+drop\s+(?P<out_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<out_life_kb>\d+)\/(?P<out_life_sec>\d+)$')

        
        count = 0

        for line in output.splitlines():
            line = line.strip()
            # Interface: Virtual-Access1325
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                ser_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                continue

            # Profile: IKEV2_PROFILE
            m = p2.match(line)
            if m:
                ser_dict['profile'] = m.groupdict()['profile']
                continue
             
            # Uptime: 13:17:14
            m = p3.match(line)
            if m:
                ser_dict['uptime'] = m.groupdict()['up']
                continue

            # Session status: UP-ACTIVE 
            m = p4.match(line)
            if m:
                ser_dict['session_status'] = m.groupdict()['session_stats']
                continue
     
            # Peer: 17.27.1.11 port 38452 fvrf: (none) ivrf: 10
            m = p5.match(line)
            if m:
                ser_dict['peer_ip'] = m.groupdict()['peer']
                ser_dict['peer_port'] = int(m.groupdict()['port'])
                if m.groupdict()['f_vrf'] is not None:
                    ser_dict['fvrf'] = m.groupdict()['f_vrf']
                if m.groupdict()['i_vrf'] is not None:
                    ser_dict['ivrf'] = m.groupdict()['i_vrf']
                continue

            # Phase1_id: scale
            m = p6.match(line)
            if m:
                ser_dict['phase_id'] = m.groupdict()['phase_name']
                continue
 
            # Session ID: 22062
            m = p7.match(line)
            if m:
                ser_dict['session_id'] = int(m.groupdict()['session_num'])
                continue
            
            # IKEv2 SA: local 1.1.1.1/4500 remote 17.27.1.11/38452 Active
            m = p8.match(line)
            if m:
                count = 0
                ike_version = m.groupdict()['version']
                ikev2_dict = ser_dict.setdefault(ike_version, {})
                ikev2_dict['local_ip'] = m.groupdict()['localip']
                ikev2_dict['local_port'] = int(m.groupdict()['localport'])
                ikev2_dict['remote_ip'] = m.groupdict()['remoteip']
                ikev2_dict['remote_port'] = int(m.groupdict()['remoteport'])
                continue

            # Capabilities:DN connid:323 lifetime:10:43:07
            m = p9.match(line)
            if m:
                ikev2_dict['capabilities'] = m.groupdict()['caps']
                ikev2_dict['connid'] = int(m.groupdict()['conn'])
                ikev2_dict['lifetime'] = m.groupdict()['life']
                continue
            
            # IPSEC FLOW: permit ip 0.0.0.0/0.0.0.0 host 7.1.2.88 
            m = p10.match(line)
            if m:
                count += 1
                ipsec_dict = ser_dict.setdefault('ipsec_flow', {}).setdefault(count, {})
                ipsec_dict['flow'] = m.groupdict()['TS']
                continue

            # Active SAs: 2, origin: crypto map
            m = p11.match(line)
            if m:
                ipsec_dict['active_sa'] = int(m.groupdict()['sa_count'])
                ipsec_dict['origin'] = m.groupdict()['origin_type']
                continue


            # Inbound:  #pkts dec'ed 47668 drop 0 life (KB/Sec) 4607746/1687
            m = p12.match(line)
            if m:
                inbound_dict = ipsec_dict.setdefault('inbound', {})
                inbound_dict['decrypted'] = int(m.groupdict()['decrypt_count'])
                inbound_dict['dropped'] = int(m.groupdict()['in_drop'])
                inbound_dict['life_in_kb'] = int(m.groupdict()['in_life_kb'])
                inbound_dict['life_in_sec'] = int(m.groupdict()['in_life_sec'])
                continue
            
            # Outbound: #pkts enc'ed 47672 drop 0 life (KB/Sec) 4607812/1874
            m = p13.match(line)
            if m:
                outbound_dict = ipsec_dict.setdefault('outbound', {})
                outbound_dict['encrypted'] = int(m.groupdict()['encrypt_count'])
                outbound_dict['dropped'] = int(m.groupdict()['out_drop'])
                outbound_dict['life_in_kb'] = int(m.groupdict()['out_life_kb'])
                outbound_dict['life_in_sec'] = int(m.groupdict()['out_life_sec'])
                continue

        return ret_dict

class ShowCryptoSessionRemote(ShowCryptoSessionRemoteSuper,ShowCryptoSessionRemoteSchema):
    '''Parser for:
        * 'show crypto session remote {remote_ip}'
    '''

    cli_command = ['show crypto session remote {remote_ip}']

    def cli(self, remote_ip='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(remote_ip=remote_ip))
        else:
            out = output
        return super().cli(output=out)

class ShowCryptoSessionRemoteDetail(ShowCryptoSessionRemoteSuper,ShowCryptoSessionRemoteSchema):
    '''Parser for:
        * 'show crypto session remote {remote_ip} detail'
    '''

    cli_command = ['show crypto session remote {remote_ip} detail']

    def cli(self, remote_ip='', output=None):
        if output is None:
           out = self.device.execute(self.cli_command[0].format(remote_ip=remote_ip))
        else:
            out = output
        return super().cli(output=out)


# ==============================
# Schema for
#   'show crypto ikev2 stats'
# ==============================
class ShowCryptoIkev2StatsExtSchema(MetaParser):
    """
    Schema for
        * 'show crypto ikev2 stats ext-service'
    """
    
    schema = {
        'ikev2_stats': {
                'aaa_operation':{
                    'receive_pskey': {
                        'passed': int,
                        'failed': int
                    },
                    'eap_auth': {
                        'passed': int,
                        'failed': int
                    },
                    'start_acc': {
                        'passed': int,
                        'failed': int
                    },
                    'stop_acc': {
                        'passed': int,
                        'failed': int
                    },
                    'authorization': {
                        'passed': int,
                        'failed': int
                    }
                },
                'ipsec_operation': {
                    'ipsec_policy_verify': {
                        'passed': int,
                        'failed': int
                    },
                    'sa_creation': {
                        'passed': int,
                        'failed': int
                    },
                    'sa_deletion':{
                        'passed': int,
                        'failed': int
                    }
                },
                'crypto_engine_operation': {
                    'dh_key_generated': {
                        'passed': int,
                        'failed': int
                    },
                    'secret_generated': {
                        'passed': int,
                        'failed': int
                    },
                    'signature_sign': {
                        'passed': int,
                        'failed': int
                    },
                    'signature_verify': {
                        'passed': int,
                        'failed': int
                    }
                },
                'pki_operation': {
                    'verify_cert': {
                        'passed': int,
                        'failed': int
                    },
                    'cert_using_http': {
                        'passed': int,
                        'failed': int
                    },
                    'peer_cert_using_http': {
                        'passed': int,
                        'failed': int
                    },
                    'get_issuers': {
                        'passed': int,
                        'failed': int
                    },
                    'get_cert_from_issuers': {
                        'passed': int,
                        'failed': int
                    },
                    'get_dn_from_cert': {
                        'passed': int,
                        'failed': int
                    }
                },
                'gkm_operation': {
                    'get_policy': {
                        'passed': int,
                        'failed': int
                    },
                    'set_policy': {
                        'passed': int,
                        'failed': int
                    }
                },
                'ppk_sks_operation': {
                    'ppk_get_cap': {
                        'passed': int,
                        'failed': int
                    },
                    'ppk_get_key': {
                        'passed': int,
                        'failed': int
                    }
                },
                'ike_preroute': {
                    'idb_verification': {
                        'passed': int,
                        'failed': int
                    }
                },
            },        
        }
    
# =========================================================
#  Parser for 'show crypto ikev2 stats ext-service'
# =========================================================   
class ShowCryptoIkev2StatsExt(ShowCryptoIkev2StatsExtSchema):
    """
    Parser for
        * 'show crypto ikev2 stats ext-service'
    """
    
    # Defines a function to run the cli_command
    cli_command = 'show crypto ikev2 stats ext-service'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # RECEIVING PSKEY                                   0          0
        p1 = re.compile(r'^RECEIVING PSKEY\s+(?P<rec_ps_pass>\d+)\s+(?P<rec_ps_fail>\d+)$')
    
        # AUTHENTICATION USING EAP                      23986          0
        p2 = re.compile(r'^AUTHENTICATION\s+USING\s+EAP\s+(?P<eap_auth_pass>\d+)\s+(?P<eap_auth_fail>\d+)$')

        # START ACCOUNTING                               3990          0
        p3 = re.compile(r'^START\s+ACCOUNTING\s+(?P<start_acc_pass>\d+)\s+(?P<start_acc_fail>\d+)$')
        
        # STOP ACCOUNTING                                3186          0
        p4 = re.compile(r'^STOP ACCOUNTING\s+(?P<stop_acc_pass>\d+)\s+(?P<stop_acc_fail>\d+)$')

        # AUTHORIZATION                                     0          0
        p5 = re.compile(r'^AUTHORIZATION\s+(?P<auth_pass>\d+)\s+(?P<auth_fail>\d+)$')

        # IPSEC POLICY VERIFICATION                      8895          0
        p6 = re.compile(r'^IPSEC POLICY VERIFICATION\s+(?P<policy_ver_pass>\d+)\s+(?P<policy_ver_fail>\d+)$')

        # SA CREATION                                    8895          0
        p7 = re.compile(r'^SA CREATION\s+(?P<sa_creation_pass>\d+)\s+(?P<sa_creation_fail>\d+)$')

        # SA DELETION                                   16182          0
        p8 = re.compile(r'^SA DELETION\s+(?P<sa_del_pass>\d+)\s+(?P<sa_del_fail>\d+)$')

        # DH PUBKEY GENERATED                           11432          0
        p9 = re.compile(r'^DH\s+PUBKEY\s+GENERATED\s+(?P<pubkey_gen_pass>\d+)\s+(?P<pubkey_gen_fail>\d+)$')

        # DH SHARED SECKEY GENERATED                    11432          0
        p10 = re.compile(r'^DH\s+SHARED\s+SECKEY\s+GENERATED\s+(?P<secret_gen_pass>\d+)\s+(?P<secret_gen_fail>\d+)$')

        # SIGNATURE SIGN                                 4000          0
        p11 = re.compile(r'^SIGNATURE\s+SIGN\s+(?P<sign_pass>\d+)\s+(?P<sign_fail>\d+)$')

        # SIGNATURE VERIFY                                  0          0
        p12 = re.compile(r'^SIGNATURE VERIFY\s+(?P<sign_ver_pass>\d+)\s+(?P<sign_ver_fail>\d+)$')

        # VERIFY CERTIFICATE                                0          0
        p13 = re.compile(r'^VERIFY CERTIFICATE\s+(?P<ver_cert_pass>\d+)\s+(?P<ver_cert_fail>\d+)$')

        # FETCHING CERTIFICATE USING HTTP                   0          0
        p14 = re.compile(r'^FETCHING\s+CERTIFICATE\s+USING\s+HTTP\s+(?P<cert_http_pass>\d+)\s+(?P<cert_http_fail>\d+)$')

        # FETCHING PEER CERTIFICATE USING HTTP              0          0
        p15 = re.compile(r'^FETCHING\s+PEER\s+CERTIFICATE\s+USING\s+HTTP\s+(?P<peer_cert_http_pass>\d+)\s+(?P<peer_cert_http_fail>\d+)$')

        # GET ISSUERS                                   13054          0
        p16 = re.compile(r'^GET\s+ISSUERS\s+(?P<get_issuers_pass>\d+)\s+(?P<get_issuers_fail>\d+)$') 

        # GET CERTIFICATES FROM ISSUERS                  6518          0
        p17 = re.compile(r'^GET\s+CERTIFICATES\s+FROM\s+ISSUERS\s+(?P<get_cert_pass>\d+)\s+(?P<get_cert_fail>\d+)$')

        # GET DN FROM CERT                                  0          0
        p18 = re.compile(r'^GET\s+DN\s+FROM\s+CERT\s+(?P<get_dn_pass>\d+)\s+(?P<get_dn_fail>\d+)$')        

        # GET_POLICY                                        0          0
        p19 = re.compile(r'^GET_POLICY\s+(?P<get_policy_pass>\d+)\s+(?P<get_policy_fail>\d+)$')

        # SET_POLICY                                        0          0
        p20 = re.compile(r'^SET_POLICY\s+(?P<set_policy_pass>\d+)\s+(?P<set_policy_fail>\d+)$')

        # PPK GET CAP                                       0          0
        p21 = re.compile(r'^PPK\s+GET\s+CAP\s+(?P<ppk_get_cap_pass>\d+)\s+(?P<ppk_get_cap_fail>\d+)$')

        # PPK GET KEY                                       0          0
        p22 = re.compile(r'^PPK\s+GET\s+KEY\s+(?P<ppk_get_key_pass>\d+)\s+(?P<ppk_get_key_fail>\d+)$')

        # IKE PREROUTE IDB VERIFICATION                     0          0
        p23 = re.compile(r'^IKE\s+PREROUTE\s+IDB\s+VERIFICATION\s+(?P<idb_ver_pass>\d+)\s+(?P<idb_ver_fail>\d+)$')

        # initial return dictionary
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # RECEIVING PSKEY                                   0          0
            m = p1.match(line)
            if m:
                ser_dict = ret_dict.setdefault('ikev2_stats', {})
                aaa_dict = ser_dict.setdefault('aaa_operation', {})
                aaa_dict.update ( { 'receive_pskey' : {
                        'passed': int(m.groupdict()['rec_ps_pass']),
                        'failed': int(m.groupdict()['rec_ps_fail'])
                    }
                })
                continue

            # AUTHENTICATION USING EAP                      23986          0
            m = p2.match(line)
            if m:
                aaa_dict.update ( { 'eap_auth' : {
                        'passed': int(m.groupdict()['eap_auth_pass']),
                        'failed': int(m.groupdict()['eap_auth_fail'])
                    }
                })
                continue
             
            # START ACCOUNTING                               3990          0
            m = p3.match(line)
            if m:
                aaa_dict.update ( { 'start_acc' : {
                        'passed': int(m.groupdict()['start_acc_pass']),
                        'failed': int(m.groupdict()['start_acc_fail'])
                    }
                })
                continue

            # STOP ACCOUNTING                                3186          0
            m = p4.match(line)
            if m:
                aaa_dict.update ( { 'stop_acc' : {
                        'passed': int(m.groupdict()['stop_acc_pass']),
                        'failed': int(m.groupdict()['stop_acc_fail'])
                    }
                })
                continue
     
            # AUTHORIZATION                                     0          0
            m = p5.match(line)
            if m:
                aaa_dict.update ( { 'authorization' : {
                        'passed': int(m.groupdict()['auth_pass']),
                        'failed': int(m.groupdict()['auth_fail'])
                    }
                })
                continue

            # IPSEC POLICY VERIFICATION                      8895          0
            m = p6.match(line)
            if m:
                ipsec_dict = ser_dict.setdefault('ipsec_operation', {})
                ipsec_dict.update ( { 'ipsec_policy_verify' : {
                        'passed': int(m.groupdict()['policy_ver_pass']),
                        'failed': int(m.groupdict()['policy_ver_fail'])
                    }
                })
                continue
 
            # SA CREATION                                    8895          0
            m = p7.match(line)
            if m:
                ipsec_dict.update ( { 'sa_creation' : {
                        'passed': int(m.groupdict()['sa_creation_pass']),
                        'failed': int(m.groupdict()['sa_creation_fail'])
                    }
                })
                continue
            
            # SA DELETION                                   16182          0
            m = p8.match(line)
            if m:
                ipsec_dict.update ( { 'sa_deletion' : {
                        'passed': int(m.groupdict()['sa_del_pass']),
                        'failed': int(m.groupdict()['sa_del_fail'])
                    }
                })
                continue

            # DH PUBKEY GENERATED                           11432          0
            m = p9.match(line)
            if m:
                crypto_dict = ser_dict.setdefault('crypto_engine_operation', {})
                crypto_dict.update ( { 'dh_key_generated' : {
                        'passed': int(m.groupdict()['pubkey_gen_pass']),
                        'failed': int(m.groupdict()['pubkey_gen_fail'])
                    }
                })
                continue
                        
            # DH SHARED SECKEY GENERATED                    11432          0
            m = p10.match(line)
            if m:
                crypto_dict.update ( { 'secret_generated' : {
                        'passed': int(m.groupdict()['secret_gen_pass']),
                        'failed': int(m.groupdict()['secret_gen_fail'])
                    }
                })
                continue

            # SIGNATURE SIGN                                 4000          0
            m = p11.match(line)
            if m:
                crypto_dict.update ( { 'signature_sign' : {
                        'passed': int(m.groupdict()['sign_pass']),
                        'failed': int(m.groupdict()['sign_fail'])
                    }
                })
                continue
            
            # SIGNATURE VERIFY                                  0          0
            m = p12.match(line)
            if m:
                crypto_dict.update ( { 'signature_verify' : {
                        'passed': int(m.groupdict()['sign_ver_pass']),
                        'failed': int(m.groupdict()['sign_ver_fail'])
                    }
                })
                continue
            
            # VERIFY CERTIFICATE                                0          0
            m = p13.match(line)
            if m:
                pki_dict = ser_dict.setdefault('pki_operation', {})
                pki_dict.update ( { 'verify_cert' : {
                        'passed': int(m.groupdict()['ver_cert_pass']),
                        'failed': int(m.groupdict()['ver_cert_fail'])
                    }
                })
                continue
            
            # FETCHING CERTIFICATE USING HTTP                   0          0
            m = p14.match(line)
            if m:
                pki_dict.update ( { 'cert_using_http' : {
                        'passed': int(m.groupdict()['cert_http_pass']),
                        'failed': int(m.groupdict()['cert_http_fail'])
                    }
                })
                continue

            # FETCHING PEER CERTIFICATE USING HTTP              0          0
            m = p15.match(line)
            if m:
                pki_dict.update ( { 'peer_cert_using_http' : {
                        'passed': int(m.groupdict()['peer_cert_http_pass']),
                        'failed': int(m.groupdict()['peer_cert_http_fail'])
                    }
                })
                continue

            # GET ISSUERS                                   13054          0
            m = p16.match(line)
            if m:
                pki_dict.update ( { 'get_issuers' : {
                        'passed': int(m.groupdict()['get_issuers_pass']),
                        'failed': int(m.groupdict()['get_issuers_fail'])
                    }
                })
                continue            

            # GET CERTIFICATES FROM ISSUERS                  6518          0
            m = p17.match(line)
            if m:
                pki_dict.update ( { 'get_cert_from_issuers' : {
                        'passed': int(m.groupdict()['get_cert_pass']),
                        'failed': int(m.groupdict()['get_cert_fail'])
                    }
                })
                continue            

            # GET DN FROM CERT                                  0          0
            m = p18.match(line)
            if m:
                pki_dict.update ( { 'get_dn_from_cert' : {
                        'passed': int(m.groupdict()['get_dn_pass']),
                        'failed': int(m.groupdict()['get_dn_fail'])
                    }
                })
                continue   
            
            # GET_POLICY                                        0          0
            m = p19.match(line)
            if m:    
                gkm_dict = ser_dict.setdefault('gkm_operation', {})
                gkm_dict.update ( { 'get_policy' : {
                        'passed': int(m.groupdict()['get_policy_pass']),
                        'failed': int(m.groupdict()['get_policy_fail'])
                    }
                })
                continue 

            # SET_POLICY                                        0          0
            m = p20.match(line)
            if m:    
                gkm_dict.update ( { 'set_policy' : {
                        'passed': int(m.groupdict()['set_policy_pass']),
                        'failed': int(m.groupdict()['set_policy_fail'])
                    }
                })            
                continue

            # PPK GET CAP                                       0          0
            m = p21.match(line)
            if m:   
                ppk_dict = ser_dict.setdefault('ppk_sks_operation', {})
                ppk_dict.update ( { 'ppk_get_cap' : {
                        'passed': int(m.groupdict()['ppk_get_cap_pass']),
                        'failed': int(m.groupdict()['ppk_get_cap_fail'])
                    }
                })      
                continue

            # PPK GET KEY                                       0          0
            m = p22.match(line)
            if m:   
                ppk_dict.update ( { 'ppk_get_key' : {
                        'passed': int(m.groupdict()['ppk_get_key_pass']),
                        'failed': int(m.groupdict()['ppk_get_key_fail'])
                    }
                })      
                continue

            # IKE PREROUTE IDB VERIFICATION                     0          0
            m = p23.match(line)
            if m:   
                ike_dict = ser_dict.setdefault('ike_preroute', {})
                ike_dict.update ( { 'idb_verification' : {
                        'passed': int(m.groupdict()['idb_ver_pass']),
                        'failed': int(m.groupdict()['idb_ver_fail'])
                    }
                }) 
                continue
            
        return ret_dict
