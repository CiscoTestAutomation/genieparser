"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto pki certificates <WORD>
   * show crypto entropy status
   * show crypto ipsec sa count
   * show crypto ikev2 sa detail
   * show crypto ikev2 sa local {} detail
   * show crypto ikev2 sa local {}
   * show crypto session
   * show crypto session detail
   * show crypto session local {} detail
   * show crypto session local {}
   * show crypto ikev2 stats timeout
   * show crypto ikev2 stats reconnect
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

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

class ShowCryptoSessionLocalDetail(ShowCryptoSessionSuperParser, ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session local {} detail'
    '''

    cli_command = "show crypto session local {ip_address} detail"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

class ShowCryptoSessionLocal(ShowCryptoSessionSuperParser, ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session local {}'
    '''

    cli_command = "show crypto session local {ip_address}"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# =================================================
#  Schema for 'show crypto ipsec sa count'
# =================================================
class ShowCryptoIpsecSaCountSchema(MetaParser):
    """Schema for show crypto ipsec sa count"""
    schema = {
        "active":int,
        "rekeying":int,
        "ipsec_sa_total":int,
        "unused":int,
        "invalid":int,
    }


# =================================================
#  Parser for 'show crypto ipsec sa count'
# =================================================
class ShowCryptoIpsecSaCount(ShowCryptoIpsecSaCountSchema):

    """Parser for show crypto ipsec sa count"""

    cli_command = 'show crypto ipsec sa count'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return_dict = {}
        # IPsec SA total: 8, active: 8, rekeying: 0, unused: 0, invalid: 0
        r1 = "^IPsec SA total: +(?P<ipsec_sa_total>[\d]+), +active: +(?P<active>[\d]+), +rekeying: +(?P<rekeying>[\d]+), +unused: +(?P<unused>[\d]+), +invalid: +(?P<invalid>[\d]+)$"
        p1 = re.compile(r1)
        for line in output.splitlines():
            # IPsec SA total: 8, active: 8, rekeying: 0, unused: 0, invalid: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                return_dict.update({k: int(v) for k, v in group.items()})
        return return_dict


# =================================================
#  Schema for 'show crypto ikev2 sa detail'
# =================================================
class ShowCryptoIkev2SaDetailSchema(MetaParser):
    """Schema for show crypto ikev2 sa detail"""
    schema = {
            "tunnel_id":{
                Any():{
                    "local": str,
                    "remote": str,
                    "fvrf": str,
                    "ivrf": str,
                    "status": str,
                    "encryption": str,
                    "keysize": int,
                    "prf": str,
                    "hash": str,
                    "dh_grp": int,
                    "auth_sign": str,
                    "auth_verify": str,
                    "life_time": int,
                    "active_time": int,
                    "ce_id": int,
                    "session_id": int,
                    "local_spi": str,
                    "remote_spi": str,
                    Optional("status_description"): str,
                    Optional("local_id"): str,
                    Optional("remote_id"): str,
                    Optional("local_reg_msg_id"): int,
                    Optional("remote_req_msg_id"): int,
                    Optional("local_next_msg_id"): int,
                    Optional("remote_next_msg_id"): int,
                    Optional("local_req_queued"): int,
                    Optional("remote_req_queued"): int,
                    Optional("local_window"): int,
                    Optional("remote_window"): int,
                    Optional("dpd_configured_time"): int,
                    Optional("retry"): int,
                    Optional("fragmentation"): str,
                    Optional("dynamic_route_update"): str,
                    Optional("extended_authentication"): str,
                    Optional("nat_t"): str,
                    Optional("cisco_trust_security_sgt"): str,
                    Optional("initiator_of_sa"): str,
                    Optional("pushed_ip"): str,
                    Optional("remote_subnets"): list
                }
            }
        }

# =================================================
#  Parser for 'show crypto ikev2 sa detail'
# =================================================
class ShowCryptoIkev2SaDetail(ShowCryptoIkev2SaDetailSchema):

    """Parser for show crypto ikev2 sa detail"""

    cli_command = 'show crypto ikev2 sa detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        # 973       92.1.121.1/500        22.1.1.2/500          none/121             READY
        r1 = "^(?P<tunnel_id>[\d]+) +(?P<local>[0-9\.\S]+) +(?P<remote>[0-9\.\S]+) +(?P<fvrf>[\w]+)\/(?P<ivrf>[\d\w]+) +(?P<status>[\w]+)$"
        p1 = re.compile(r1)

        # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: PSK, Auth verify: PSK
        r2 = "^Encr: +(?P<encryption>[\d\w\-]+), keysize: +(?P<keysize>[\d]+), PRF: +(?P<prf>[\w]+), +Hash: +(?P<hash>[\w]+), +DH Grp:+(?P<dh_grp>[\w\d]+), +Auth sign: +(?P<auth_sign>[\w]+), +Auth verify: +(?P<auth_verify>[\w]+)$"
        p2 = re.compile(r2)

        # Life/Active Time: 86400/12689 sec
        r3 = "^Life+\S+Active Time: +(?P<life_time>[\d]+)\/(?P<active_time>[\d]+) +sec$"
        p3 = re.compile(r3)

        # CE id: 76468, Session-id: 17155
        r4 = "^CE id:+ (?P<ce_id>[\d]+), +Session-id: +(?P<session_id>[\d]+)$"
        p4 = re.compile(r4)

        # Status Description: Negotiation done
        r5 = "^Status Description:+ (?P<status_description>[\w\d\s]+)$"
        p5 = re.compile(r5)

        # Local spi: 000D3669857A0F82       Remote spi: E0419B1DB02DE6AE
        r6 = "^Local spi: +(?P<local_spi>[\w\d]+) +Remote spi: +(?P<remote_spi>[\w\d]+)$"
        p6 = re.compile(r6)

        # Local id: user2621@cisco.com
        r7 = "^Local id: +(?P<local_id>[\w\d\S]+)$"
        p7 = re.compile(r7)

        # Remote id: 22.1.1.2
        r8 = "^Remote id: +(?P<remote_id>[\d\.]+)$"
        p8 = re.compile(r8)

        # Local req msg id:  214            Remote req msg id:  6
        r9 = "^Local req msg id:  +(?P<local_reg_msg_id>[\d]+) +Remote req msg id:  +(?P<remote_req_msg_id>[\d]+)$"
        p9 = re.compile(r9)

        # Local next msg id: 214            Remote next msg id: 6
        r10 = "^Local next msg id: +(?P<local_next_msg_id>[\d]+) +Remote next msg id: +(?P<remote_next_msg_id>[\d]+)$"
        p10 = re.compile(r10)

        # Local req queued:  214            Remote req queued:  6
        r11 = "^Local req queued:  +(?P<local_req_queued>[\d]+) +Remote req queued:  +(?P<remote_req_queued>[\d]+)$"
        p11 = re.compile(r11)

        # Local window:      5              Remote window:      5
        r12 = "^Local window: +(?P<local_window>[\d]+) +Remote window: +(?P<remote_window>[\d]+)$"
        p12 = re.compile(r12)

        # DPD configured for 60 seconds, retry 3
        r13 = "^DPD configured for +(?P<dpd_configured_time>[\d]+) +seconds, retry +(?P<retry>[\d]+)$"
        p13 = re.compile(r13)

        # Fragmentation not  configured.
        r14 = "^Fragmentation +(?P<fragmentation>[\d\s\S]+)$"
        p14 = re.compile(r14)

        # Dynamic Route Update: enabled
        r15 = "^Dynamic Route Update: +(?P<dynamic_route_update>[\d\s\S]+)$"
        p15 = re.compile(r15)

        # Extended Authentication not configured.
        r16 = "^Extended Authentication +(?P<extended_authentication>[\d\s\S]+)$"
        p16 = re.compile(r16)

        # NAT-T is not detected
        r17 = "^NAT-T is +(?P<nat_t>[\d\s\S]+)$"
        p17 = re.compile(r17)

        # Cisco Trust Security SGT is disabled
        r18 = "^Cisco Trust Security SGT is +(?P<cisco_trust_security_sgt>[\d\s\S]+)$"
        p18 = re.compile(r18)

        # Initiator of SA : Yes
        r19 = "^Initiator of SA :+(?P<initiator_of_sa>[\d\s\S]+)$"
        p19 = re.compile(r19)

        # Pushed IP address: 8.1.9.4
        r20 = "^Pushed IP address: +(?P<pushed_ip>[0-9\.]+)$"
        p20 = re.compile(r20)

        # 10.0.0.0 255.0.0.0
        r21 = "^(?P<remote_subnets>[0-9\.\s]+)$"
        p21 = re.compile(r21)

        ret_dict={}
        for line in output.splitlines():
            line=line.strip()
            # 973       92.1.121.1/500        22.1.1.2/500          none/121             READY
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group['status'] = group['status'].lower()
                tunnel_id = int(group.pop('tunnel_id'))
                master_dict = ret_dict.setdefault('tunnel_id', {}).setdefault(tunnel_id, {})
                master_dict.update(group)
                remote_subnets_dict = master_dict.setdefault('remote_subnets', [])
                continue
            # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: PSK, Auth verify: PSK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: v.lower() for k, v in group.items()}
                group['dh_grp'] = int(group['dh_grp'])
                group['keysize'] = int(group['keysize'])
                master_dict.update(group)
                continue
            # Life/Active Time: 86400/12689 sec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group['life_time'] = int(group['life_time'])
                group['active_time'] = int(group['active_time'])
                master_dict.update(group)
                continue
            # CE id: 76468, Session-id: 17155
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group['session_id'] = int(group['session_id'])
                group['ce_id'] = int(group['ce_id'])
                master_dict.update(group)
                continue
            # Status Description: Negotiation done
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group['status_description'] = group['status_description'].lower()
                master_dict.update(group)
                continue
            # Local spi: 000D3669857A0F82       Remote spi: E0419B1DB02DE6AE
            m = p6.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Local id: user2621@cisco.com
            m = p7.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Remote id: 22.1.1.2
            m = p8.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Local req msg id:  214            Remote req msg id:  6
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group['remote_req_msg_id'] = int(group['remote_req_msg_id'])
                group['local_reg_msg_id'] = int(group['local_reg_msg_id'])
                master_dict.update(group)
                continue
            # Local next msg id: 214            Remote next msg id: 6
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group['remote_next_msg_id'] = int(group['remote_next_msg_id'])
                group['local_next_msg_id'] = int(group['local_next_msg_id'])
                master_dict.update(group)
                continue
            # Local req queued:  214            Remote req queued:  6
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group['remote_req_queued'] = int(group['remote_req_queued'])
                group['local_req_queued'] = int(group['local_req_queued'])
                master_dict.update(group)
                continue
            # Local window:      5              Remote window:      5
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group['remote_window'] = int(group['remote_window'])
                group['local_window'] = int(group['local_window'])
                master_dict.update(group)
                continue
            # DPD configured for 60 seconds, retry 3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group['retry'] = int(group['retry'])
                group['dpd_configured_time'] = int(group['dpd_configured_time'])
                master_dict.update(group)
                continue
            # Fragmentation not  configured.
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group['fragmentation'] = group['fragmentation'].replace('.','')
                master_dict.update(group)
                continue
            # Dynamic Route Update: enabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Extended Authentication not configured.
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group['extended_authentication'] = group['extended_authentication'].replace('.','')
                master_dict.update(group)
                continue
            # NAT-T is not detected
            m = p17.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Cisco Trust Security SGT is disabled
            m = p18.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # Initiator of SA : Yes
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group['initiator_of_sa']=group['initiator_of_sa'].strip().lower()
                master_dict.update(group)
                continue
            # Pushed IP address: 8.1.9.4
            m = p20.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue
            # 10.0.0.0 255.0.0.0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                remote_subnets_dict.append(group['remote_subnets'])
        return ret_dict


class ShowCryptoIkev2SaLocalDetail(ShowCryptoIkev2SaDetail, ShowCryptoIkev2SaDetailSchema):
    '''Parser for:
        * 'show crypto ikev2 sa local {} detail'
    '''

    cli_command = "show crypto ikev2 sa local {ip_address} detail"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


class ShowCryptoIkev2SaLocal(ShowCryptoIkev2SaDetail, ShowCryptoIkev2SaDetailSchema):
    '''Parser for:
        * 'show crypto ikev2 sa local {}'
    '''

    cli_command = "show crypto ikev2 sa local {ip_address}"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

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




# ======================================
#  Schema for 'show crypto ikev2 stats timeout'
# ======================================
class ShowCryptoIkev2StatsTimeoutSchema(MetaParser):

    """Schema for show crypto ikev2 stats timeout"""

    schema = {
         'ext_service_timer': int,
         'auth_timer': int,
         'packet_max_retrans_timer': int,
         'dpd_max_retrans_timer': int,
        }

# ======================================
#  Parser for 'show crypto ikev2 stats timeout'
# ======================================
class ShowCryptoIkev2StatsTimeout(ShowCryptoIkev2StatsTimeoutSchema):

    """Parser for show crypto ikev2 stats timeout"""

    cli_command = ['show crypto ikev2 stats timeout']

    def cli(self,output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        
        #EXT SERVICE TIMER    0
        p1 = re.compile(r'^EXT\s+SERVICE\s+TIMER\s+(?P<ext_service_timer>\d+)$')


        #AUTH TIMER     0
        p2 = re.compile(r'^AUTH\s+TIMER\s+(?P<auth_timer>\d+)$')


        #PACKET MAXIMUM RETRANS TIMER     7736
        p3 = re.compile(r'^PACKET\s+MAXIMUM\s+RETRANS\s+TIMER\s+(?P<packet_max_retrans_timer>\d+)$')


        #DPD MAX RETRANS TIMER         0
        p4 = re.compile(r'^DPD\s+MAX\s+RETRANS\s+TIMER\s+(?P<dpd_max_retrans_timer>\d+)$')        

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ext_service_timer'] = int(group['ext_service_timer'])
                continue


            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['auth_timer'] = int(group['auth_timer'])
                continue


            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['packet_max_retrans_timer'] = int(group['packet_max_retrans_timer'])                
                continue
            
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['dpd_max_retrans_timer'] = int(group['dpd_max_retrans_timer'])                
                continue
                

        return ret_dict




# ====================================================
#  Schema for 'show crypto ikev2 stats reconnect'
# ====================================================
class ShowCryptoIkev2StatsReconnectSchema(MetaParser):
    """Schema for:
        show crypto ikev2 stats reconnect"""

    schema = {

                 'incoming_reconnect': int,
                 'success_reconnect': int,
                 'failed_reconnect': int,
                 'active_session_count': int,
                 'inactive_session_count': int,

    }

# =================================================
#  Parser for 'show crypto ikev2 stats reconnect'
# =================================================	

class ShowCryptoIkev2StatsReconnect(ShowCryptoIkev2StatsReconnectSchema):
    """Parser for show crypto ikev2 stats reconnect"""

    cli_command = 'show crypto ikev2 stats reconnect'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        inventory_dict = {}
        
        #Total incoming reconnect connection: 10        
        p1 = re.compile(r'^Total\s+incoming\s+reconnect\s+connection:\s+(?P<incoming_reconnect>\d+)$')


        #Success reconnect connection: 10
        p2 = re.compile(r'^Success\s+reconnect\s+connection:\s+(?P<success_reconnect>\d+)$') 


        #Failed reconnect connection: 0        
        p3 = re.compile(r'^Failed\s+reconnect\s+connection:\s+(?P<failed_reconnect>\d+)$')


        #Reconnect capable active session count: 4        
        p4 = re.compile(r'^Reconnect\s+capable\s+active\s+session\s+count:\s(?P<active_session_count>\d+)$')  


        #Reconnect capable inactive session count: 6
        p5 = re.compile(r'^Reconnect\s+capable\s+inactive\s+session\s+count:\s(?P<inactive_session_count>\d+)$')  
        

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)
            if result:
                group = result.groupdict()
                inventory_dict['incoming_reconnect'] = int(group['incoming_reconnect'])
                continue

            
            result = p2.match(line)
            if result:
                group = result.groupdict()
                inventory_dict['success_reconnect'] = int(group['success_reconnect'])
                continue
            
                
            result = p3.match(line)                                             
            if result:
                group = result.groupdict()
                inventory_dict['failed_reconnect'] = int(group['failed_reconnect'])
                continue    
                
                
            result = p4.match(line)                                            
            if result:
                group = result.groupdict()
                inventory_dict['active_session_count'] = int(group['active_session_count'])
                continue                   
             
  
            result = p5.match(line)     
            if result:
                group = result.groupdict()
                inventory_dict['inactive_session_count'] = int(group['inactive_session_count'])
                continue                   
   
                
                

        return inventory_dict        

# ==============================
# Schema for
#   'show crypto isakmp sa'
# ==============================
class ShowCryptoIsakmpSaSchema(MetaParser):
    """
    Schema for
        * 'show crypto isakmp sa'
    """
    
    schema = {
        'isakmp_stats': {
            Or('IPv4', 'IPv6'):{
                int:{
                    'destination': str,
                    'source': str,
                    'session_state': str,
                    'conn_id': int,
                    'status': str,
                    Optional('current_status'): str,
                },
            },
        },
    } 

class ShowCryptoIsakmpSa(ShowCryptoIsakmpSaSchema):
    
    # Defines a function to run the cli_command
    cli_command = 'show crypto isakmp sa'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        # initial return dictionary
        ret_dict = {}

        # IPv4 Crypto ISAKMP SA
        # IPv6 Crypto ISAKMP SA
        p1 = re.compile(r'^(?P<version>\S+) Crypto ISAKMP SA$')
    
        # 9.45.9.7        9.45.9.8        QM_IDLE           1064 ACTIVE
        # 9.45.9.8        9.45.9.7        MM_NO_STATE       1063 ACTIVE (deleted)
        # 2001::1         3001::1         QM_IDLE           1064 ACTIVE
        p2 = re.compile(r'^(?P<dst>\S+)\s+(?P<src>\S+)\s+(?P<state>\S+)\s+'
                        r'(?P<id>\d+)\s+(?P<stats>\S+)(\s+\((?P<stats_now>\S+)\))?$')

        count = 0
        for line in output.splitlines():
            line = line.strip()
            # IPv4 Crypto ISAKMP SA
            # IPv6 Crypto ISAKMP SA
            m = p1.match(line)
            if m:
                ser_dict = ret_dict.setdefault('isakmp_stats', {})
                if m.groupdict()['version'] == "IPv4":
                    sub_dict = ser_dict.setdefault('IPv4', {})
                
                if m.groupdict()['version'] == "IPv6":
                    count = 0
                    sub_dict = ser_dict.setdefault('IPv6', {})
                continue

            # 9.45.9.7        9.45.9.8        QM_IDLE           1064 ACTIVE
            # 9.45.9.8        9.45.9.7        MM_NO_STATE       1063 ACTIVE (deleted)
            # 2001::1         3001::1         QM_IDLE           1064 ACTIVE
            m = p2.match(line)
            if m:
                count += 1
                isakmp_dict = sub_dict.setdefault(count, {})
                isakmp_dict['destination'] = m.groupdict()['dst']
                isakmp_dict['source'] = m.groupdict()['src']
                isakmp_dict['session_state'] = m.groupdict()['state']
                isakmp_dict['conn_id'] = int(m.groupdict()['id'])
                isakmp_dict['status'] = m.groupdict()['stats']
                if  m.groupdict()['stats_now'] is not None:
                    isakmp_dict['current_status'] = m.groupdict()['stats_now']
                continue

        if ret_dict['isakmp_stats']['IPv4'] == {}:
            del ret_dict['isakmp_stats']['IPv4']

        if ret_dict['isakmp_stats']['IPv6'] == {}:
            del ret_dict['isakmp_stats']['IPv6']     

        return ret_dict

# ==============================
# Schema for
#   'show crypto isakmp sa detail'
# ==============================
class ShowCryptoIsakmpSaDetailSchema(MetaParser):
    """
    Schema for
        * 'show crypto isakmp sa detail'
    """
    
    schema = {
        'isakmp_stats': {
            Or('IPv4', 'IPv6'):{
                int:{
                    'c_id': int,
                    'local_ip': str,
                    'remote_ip': str,
                    Optional('ivrf'): str,
                    Optional('status'): str,
                    Optional('encr_algo'): str,
                    Optional('hash_algo'): str,
                    Optional('auth_type'): str,
                    Optional('dh_group'): int,
                    Optional('lifetime'): str,
                    Optional('capabilities'): str,
                    Optional('engine_id'): str,
                    Optional('conn_id'): int,
                },
            },
        },
    } 

class ShowCryptoIsakmpSaDetail(ShowCryptoIsakmpSaDetailSchema):
    
    # Defines a function to run the cli_command
    cli_command = 'show crypto isakmp sa detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # IPv4 Crypto ISAKMP SA
        # IPv6 Crypto ISAKMP SA
        p1 = re.compile(r'^(?P<version>\S+) Crypto ISAKMP SA$')
    
        # 29609 100.0.10.2      100.13.220.2           ACTIVE aes  sha    psk  16 00:01:47 D
        # 29610 100.0.10.2      100.13.220.2     RED      ACTIVE aes  sha    psk  16 00:01:47 D
        # 29611 100.0.10::2      100.13.220::2     RED      ACTIVE aes  sha    psk  16 00:01:47 D
        p2 = re.compile(r'^(?P<conn_id>\d+)\s+(?P<local>\S+)\s+(?P<remote>\S+)\s+(?P<vrf>\S+)?\s+'
                        r'(?P<stats>\w+)\s+(?P<encr>\S+)\s+(?P<hash>\S+)\s+(?P<auth>\S+)\s+'
                        r'(?P<dh>\d+)\s+(?P<life>\S+)\s+(?P<cap>\S+)$')
 
        # Engine-id:Conn-id =  SW:12609
        # Engine-id:Conn-id =  ????
        p3 = re.compile(r'^Engine-id:Conn-id\s+=\s+(?P<engine>\S+):(?P<id>\d+)$')

        count = 0
        for line in output.splitlines():
            line = line.strip()
            # IPv4 Crypto ISAKMP SA
            # IPv6 Crypto ISAKMP SA
            m = p1.match(line)
            if m:
                ser_dict = ret_dict.setdefault('isakmp_stats', {})
                if m.groupdict()['version'] == "IPv4":
                    sub_dict = ser_dict.setdefault('IPv4', {})
                
                if m.groupdict()['version'] == "IPv6":
                    count = 0
                    sub_dict = ser_dict.setdefault('IPv6', {})
                continue

            # 29609 100.0.10.2      100.13.220.2           ACTIVE aes  sha    psk  16 00:01:47 D
            # 29610 100.0.10.2      100.13.220.2     RED      ACTIVE aes  sha    psk  16 00:01:47 D
            # 29611 100.0.10::2      100.13.220::2     RED      ACTIVE aes  sha    psk  16 00:01:47 D
            m = p2.match(line)
            if m:
                count += 1
                isakmp_dict = sub_dict.setdefault(count, {})
                isakmp_dict['c_id'] = int(m.groupdict()['conn_id'])
                isakmp_dict['local_ip'] = m.groupdict()['local']
                isakmp_dict['remote_ip'] = m.groupdict()['remote']
                if m.groupdict()['vrf'] is not None:
                     isakmp_dict['ivrf'] = m.groupdict()['vrf']
                isakmp_dict['status'] = m.groupdict()['stats']
                isakmp_dict['encr_algo'] = m.groupdict()['encr']
                isakmp_dict['hash_algo'] = m.groupdict()['hash']
                isakmp_dict['auth_type'] = m.groupdict()['auth']
                isakmp_dict['dh_group'] = int(m.groupdict()['dh'])
                isakmp_dict['lifetime'] = m.groupdict()['life']
                isakmp_dict['capabilities'] = m.groupdict()['cap']
                continue
            # Engine-id:Conn-id =  SW:12609
            # Engine-id:Conn-id =  ????
            m = p3.match(line)
            if m:
                if  m.groupdict()['engine'] is not None:
                    isakmp_dict['engine_id'] = m.groupdict()['engine']
                
                if  m.groupdict()['id'] is not None:
                    isakmp_dict['conn_id'] = int(m.groupdict()['id'])
                continue

        if ret_dict['isakmp_stats']['IPv4'] == {}:
            del ret_dict['isakmp_stats']['IPv4']

        if ret_dict['isakmp_stats']['IPv6'] == {}:
            del ret_dict['isakmp_stats']['IPv6']     

        return ret_dict

# ====================================================
#  Schema for 'show crypto mib ipsec flowmib endpoint'
# ====================================================
class ShowCryptoMibIpsecFlowmibEndpointSchema(MetaParser):
    """Schema for show crypto mib ipsec flowmib endpoint"""
    schema = {
        Any(): {
            Any(): {
                Any(): {
                    'index': str,
                    'local_type': str,
                    'local_address': str,
                    'protocol': int,
                    'local_port': int,
                    'remote_type': str,
                    'remote_address': str,
                    'remote_port': int
                    },
                },
            'total_vrf': int,
        }
    }

# ====================================================
#  Parser for 'show crypto mib ipsec flowmib endpoint'
# ====================================================  
class ShowCryptoMibIpsecFlowmibEndpoint(ShowCryptoMibIpsecFlowmibEndpointSchema):
    """Parser for 
        * show crypto mib ipsec flowmib endpoint
    """

    cli_command = 'show crypto mib ipsec flowmib endpoint'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        end_points_dict = {}

        # vrf CC-INTERNET
        p1 = re.compile(r'^vrf\s+(?P<vrf_name>[\S\s]+)$')

        # Index:                       17
        p2 = re.compile(r'^Index:\s+(?P<index>\d+)$')

        # Local type:                  Single IP address
        p3 = re.compile(r'^Local\s+type:\s+(?P<local_type>[\S\s]+)$')

        # Local address:               1.1.0.100
        p4 = re.compile(r'^Local\s+address:\s+(?P<local_address>[\S\s]+)$')

        # Protocol:                    47
        p5 = re.compile(r'^Protocol:\s+(?P<protocol>\d+)$')

        # Local port:                  0
        p6 = re.compile(r'^Local\s+port:\s+(?P<local_port>\d+)$')
 
        # Remote type:                 Single IP address
        p7 = re.compile(r'^Remote\s+type:\s+(?P<remote_type>[\S\s]+)$')

        # Remote address:              1.1.0.101
        p8 = re.compile(r'^Remote\s+address:\s+(?P<remote_address>[\S\s]+)$')

        # Remote port:                 0
        p9 = re.compile(r'^Remote\s+port:\s+(?P<remote_port>\d+)$')
 
        vrf_count = 0
        result_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # vrf CC-INTERNET
            m = p1.match(line)
            if m:
                vrf_count += 1
                if 'total_vrf' not in end_points_dict:
                    result_dict = end_points_dict.setdefault('ipsec_flowmib_endpoints', {})
                result_dict['total_vrf'] = vrf_count
                vrf_name = m.groupdict()['vrf_name']
                vrf_name_dict = result_dict.setdefault(vrf_name, {})
                index_count = 0
                continue

            # Index:                       17
            m = p2.match(line)
            if m:
                index_count += 1
                index_count_dict = vrf_name_dict.setdefault(str(index_count), {})
                index_count_dict['index'] = m.groupdict()['index']
                continue

            # Local type:                  Single IP address
            m = p3.match(line)
            if m:
                index_count_dict['local_type'] = m.groupdict()['local_type']
                continue

            # Local address:               1.1.0.100
            m = p4.match(line)
            if m:
                index_count_dict['local_address'] = m.groupdict()['local_address']
                continue

            # Protocol:                    47
            m = p5.match(line)
            if m:
                index_count_dict['protocol'] = int(m.groupdict()['protocol'])
                continue

            # Local port:                  0
            m = p6.match(line)
            if m:
                index_count_dict['local_port'] = int(m.groupdict()['local_port'])
                continue

            # Remote type:                 Single IP address
            m = p7.match(line)
            if m:
                index_count_dict['remote_type'] = m.groupdict()['remote_type']
                continue

            # Remote address:              1.1.0.101
            m = p8.match(line)
            if m:
                index_count_dict['remote_address'] = m.groupdict()['remote_address']
                continue
 
            # Remote port:                 0
            m = p9.match(line)
            if m:
                index_count_dict['remote_port'] = int(m.groupdict()['remote_port'])
                continue

        return end_points_dict

# ====================================================
#  Schema for 'show crypto mib ipsec flowmib tunnel'
# ====================================================
class ShowCryptoMibIpsecFlowmibTunnelSchema(MetaParser):
    """Schema for show crypto mib ipsec flowmib tunnel"""
    schema = {
        Any(): {
            Any(): {
                Any(): {
                    'index': str,
                    'local_address': str,
                    'remote_address': str,
                    'ipsec_keying': str,
                    'encap_mode': int,
                    'lifetime_kb': int,
                    'lifetime_sec': int,
                    'active_time': str,
                    'lifetime_threshold_kb': int,
                    'lifetime_threshold_sec': int,
                    'no_of_refresh': int,
                    'expired_sa': int,
                    'current_sa': int,
                    'in_sa_dh_group': str,
                    'in_sa_encrypt_algorithm': str,
                    'in_sa_ah_auth_algorithm': str,
                    'in_sa_esp_auth_algorithm': str,
                    'in_sa_uncompress_algorithm': str,
                    'out_sa_dh_group': str,
                    'out_sa_encrypt_algorithm': str,
                    'out_sa_ah_auth_algorithm': str,
                    'out_sa_esp_auth_algorithm': str,
                    'out_sa_uncompress_algorithm': str,
                    'in_octets': int,
                    'decompressed_octets': int,
                    'in_packets': int,
                    'in_drops': int,
                    'in_replay_drops': int,
                    'in_authentications': int,
                    'in_auth_failures': int,
                    'in_decrypts': int,
                    'in_decrypt_failures': int,
                    'out_octets': int,
                    'out_uncompressed_octets': int,
                    'out_packets': int,
                    'out_drops': int,
                    'out_authentications': int,
                    'out_auth_failures': int,
                    'out_encryptions': int,
                    'out_encryption_failures': int,
                    'compressed_octets': int,
                    'decompressed_octets_1': int,
                    'out_uncompressed_octets_1': int,
                    },
                },
            'total_vrf': int,
        }
    }
# ====================================================
#  Parser for 'show crypto mib ipsec flowmib tunnel'
# ====================================================
class ShowCryptoMibIpsecFlowmibTunnel(ShowCryptoMibIpsecFlowmibTunnelSchema):
    """Parser for
        * show crypto mib ipsec flowmib tunnel
    """

    cli_command = 'show crypto mib ipsec flowmib tunnel'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        flowmib_tunnel_dict = {}

        # vrf CC-INTERNET
        p1 = re.compile(r'^vrf\s+(?P<vrf_name>[\S\s]+)$')
        
        # Index:                       17
        p2 = re.compile(r'^Index:\s+(?P<index>\d+)$')

        # Local address:               1.1.0.100
        p3 = re.compile(r'^Local\s+address:\s+(?P<local_address>[\S\s]+)$')

        # Remote address:              1.1.0.101
        p4 = re.compile(r'^Remote\s+address:\s+(?P<remote_address>[\S\s]+)$')

        # IPSEC keying:                IKE
        p5 = re.compile(r'^IPSEC\s+keying:\s+(?P<ipsec_keying>[\S\s]+)$')

        # Encapsulation mode:          2
        p6 = re.compile(r'^Encapsulation\s+mode:\s+(?P<encap_mode>\d+)$')

        # Lifetime (KB):               4608000
        p7 = re.compile(r'^Lifetime\s+\(KB\):\s+(?P<lifetime_kb>\d+)$')

        # Lifetime (Sec):              3600
        p8 = re.compile(r'^Lifetime\s+\(Sec\):\s+(?P<lifetime_sec>\d+)$')
 
        # Active time:                 00:05:50
        p9 = re.compile(r'^Active\s+time:\s+(?P<active_time>[\S\s]+)$')

        # Lifetime threshold (KB):     64
        p10 = re.compile(r'^Lifetime\s+threshold\s+\(KB\):\s+(?P<lifetime_threshold_kb>\d+)$')

        # Lifetime threshold (Sec):    10
        p11 = re.compile(r'^Lifetime\s+threshold\s+\(Sec\):\s+(?P<lifetime_threshold_sec>\d+)$')

        # Total number of refreshes:   0
        p12 = re.compile(r'^Total\s+number\s+of\s+refreshes:\s+(?P<no_of_refresh>\d+)$')

        # Expired SA instances:        0
        p13 = re.compile(r'^Expired\s+SA\s+instances:\s+(?P<expired_sa>\d+)$')

        # Current SA instances:        2
        p14 = re.compile(r'^Current\s+SA\s+instances:\s+(?P<current_sa>\d+)$')

        # In SA DH group:              None
        p15 = re.compile(r'^In\s+SA\s+DH\s+group:\s+(?P<in_sa_dh_group>[\S\s]+)$')

        # In sa encrypt algorithm:     aes
        p16 = re.compile(r'^In\s+sa\s+encrypt\s+algorithm:\s+(?P<in_sa_encrypt_algorithm>[\S\s]+)$')

        # In SA AH auth algorithm:     None
        p17 = re.compile(r'^In\s+SA\s+AH\s+auth\s+algorithm:\s+(?P<in_sa_ah_auth_algorithm>[\S\s]+)$')

        # In SA ESP auth algo:         None
        p18 = re.compile(r'^In\s+SA\s+ESP\s+auth\s+algo:\s+(?P<in_sa_esp_auth_algorithm>[\S\s]+)$')

        # In SA uncompress algorithm:  None
        p19 = re.compile(r'^In\s+SA\s+uncompress\s+algorithm:\s+(?P<in_sa_uncompress_algorithm>[\S\s]+)$')

        # Out SA DH group:             None
        p20 = re.compile(r'^Out\s+SA\s+DH\s+group:\s+(?P<out_sa_dh_group>[\S\s]+)$')

        # Out SA encryption algorithm: aes
        p21 = re.compile(r'^Out\s+SA\s+encryption\s+algorithm:\s+(?P<out_sa_encrypt_algorithm>[\S\s]+)$')

        # Out SA auth algorithm:       None
        p22 = re.compile(r'^Out\s+SA\s+auth\s+algorithm:\s+(?P<out_sa_ah_auth_algorithm>[\S\s]+)$')

        # Out SA ESP auth algorithm:   None
        p23 = re.compile(r'^Out\s+SA\s+ESP\s+auth\s+algorithm:\s+(?P<out_sa_esp_auth_algorithm>[\S\s]+)$')

        # Out SA uncompress algorithm: None
        p24 = re.compile(r'^Out\s+SA\s+uncompress\s+algorithm:\s+(?P<out_sa_uncompress_algorithm>[\S\s]+)$')

        # In octets:                   386160
        p25 = re.compile(r'^In\s+octets:\s+(?P<in_octets>\d+)$')

        # Decompressed octets:         386160
        p26 = re.compile(r'^Decompressed\s+octets:\s+(?P<decompressed_octets>\d+)$')

        # In packets:                  3210
        p27 = re.compile(r'^In\s+packets:\s+(?P<in_packets>\d+)$')
 
        # In drops:                    0
        p28 = re.compile(r'^In\s+drops:\s+(?P<in_drops>\d+)$')
 
        # In replay drops:             0
        p29 = re.compile(r'^In\s+replay\s+drops:\s+(?P<in_replay_drops>\d+)$')
 
        # In authentications:          3210
        p30 = re.compile(r'^In\s+authentications:\s+(?P<in_authentications>\d+)$')
 
        # In authentication failures:  0
        p31 = re.compile(r'^In\s+authentication\s+failures:\s+(?P<in_auth_failures>\d+)$')

        # In decrypts:                 3210
        p32 = re.compile(r'^In\s+decrypts:\s+(?P<in_decrypts>\d+)$')
 
        # In decrypt failures:         0
        p33 = re.compile(r'^In\s+decrypt\s+failures:\s+(?P<in_decrypt_failures>\d+)$')
 
        # Out octets:                  194700
        p34 = re.compile(r'^Out\s+octets:\s+(?P<out_octets>\d+)$')

        # Out uncompressed octets:     194700
        p35 = re.compile(r'^Out\s+uncompressed\s+octets:\s+(?P<out_uncompressed_octets>\d+)$')

        # Out packets:                 3222
        p36 = re.compile(r'^Out\s+packets:\s+(?P<out_packets>\d+)$')
 
        # Out drops:                   0
        p37 = re.compile(r'^Out\s+drops:\s+(?P<out_drops>\d+)$')
 
        # Out authentications:         3222
        p38 = re.compile(r'^Out\s+authentications:\s+(?P<out_authentications>\d+)$')
 
        # Out authentication failures: 0
        p39 = re.compile(r'^Out\s+authentication\s+failures:\s+(?P<out_auth_failures>\d+)$')
 
        # Out encryptions:             3222
        p40 = re.compile(r'^Out\s+encryptions:\s+(?P<out_encryptions>\d+)$')
 
        # Out encryption failures:     0
        p41 = re.compile(r'^Out\s+encryption\s+failures:\s+(?P<out_encryption_failures>\d+)$')
 
        # Compressed octets:           0
        p42 = re.compile(r'^Compressed\s+octets:\s+(?P<compressed_octets>\d+)$')

        # Decompressed octets:         0
        p43 = re.compile(r'^Decompressed\s+octets:\s+(?P<decompressed_octets_1>\d+)$')

        # Out uncompressed octets:     0
        p44 = re.compile(r'^Out\s+uncompressed\s+octets:\s+(?P<out_uncompressed_octets_1>\d+)$')

        vrf_count = 0
        result_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # vrf CC-INTERNET
            m = p1.match(line)
            if m:
                vrf_count += 1
                if 'total_vrf' not in flowmib_tunnel_dict:
                    result_dict = flowmib_tunnel_dict.setdefault('ipsec_flowmib_tunnel', {})
                result_dict['total_vrf'] = vrf_count
                vrf_name = m.groupdict()['vrf_name']
                vrf_name_dict = result_dict.setdefault(vrf_name, {})
                index_count = 0
                continue

            # Index:                       17
            m = p2.match(line)
            if m:
                index_count += 1
                index_count_dict = vrf_name_dict.setdefault(str(index_count), {})
                index_count_dict['index'] = m.groupdict()['index']
                # There are duplicate entries in the output of this show command
                # CSCwa72431 is used to track IPSec Mib issues
                # Until the issue is fixed, we will check with flags below
                # and handle duplicate entries
                decompressed_octets_seen = False
                out_uncompressed_octets_seen = False
                continue

            # Local address:               1.1.0.100
            m = p3.match(line)
            if m:
                index_count_dict['local_address'] = m.groupdict()['local_address']
                continue

            # Remote address:              1.1.0.101
            m = p4.match(line)
            if m:
                index_count_dict['remote_address'] = m.groupdict()['remote_address']
                continue
            
            # IPSEC keying:                IKE
            m = p5.match(line)
            if m:
                index_count_dict['ipsec_keying'] = m.groupdict()['ipsec_keying']
                continue

            # Encapsulation mode:          2
            m = p6.match(line)
            if m:
                index_count_dict['encap_mode'] = int(m.groupdict()['encap_mode'])
                continue

            # Lifetime (KB):               4608000
            m = p7.match(line)
            if m:
                index_count_dict['lifetime_kb'] = int(m.groupdict()['lifetime_kb'])
                continue

            # Lifetime (Sec):              3600
            m = p8.match(line)
            if m:
                index_count_dict['lifetime_sec'] = int(m.groupdict()['lifetime_sec'])
                continue

            # Active time:                 00:05:50
            m = p9.match(line)
            if m:
                index_count_dict['active_time'] = m.groupdict()['active_time']
                continue

            # Lifetime threshold (KB):     64
            m = p10.match(line)
            if m:
                index_count_dict['lifetime_threshold_kb'] = int(m.groupdict()['lifetime_threshold_kb'])
                continue

            # Lifetime threshold (Sec):    10
            m = p11.match(line)
            if m:
                index_count_dict['lifetime_threshold_sec'] = int(m.groupdict()['lifetime_threshold_sec'])
                continue

            # Total number of refreshes:   0
            m = p12.match(line)
            if m:
                index_count_dict['no_of_refresh'] = int(m.groupdict()['no_of_refresh'])
                continue

            # Expired SA instances:        0
            m = p13.match(line)
            if m:
                index_count_dict['expired_sa'] = int(m.groupdict()['expired_sa'])
                continue

            # Current SA instances:        2
            m = p14.match(line)
            if m:
                index_count_dict['current_sa'] = int(m.groupdict()['current_sa'])
                continue

            # In SA DH group:              None
            m = p15.match(line)
            if m:
                index_count_dict['in_sa_dh_group'] = m.groupdict()['in_sa_dh_group']
                continue

            # In sa encrypt algorithm:     aes
            m = p16.match(line)
            if m:
                index_count_dict['in_sa_encrypt_algorithm'] = m.groupdict()['in_sa_encrypt_algorithm']
                continue

            # In SA AH auth algorithm:     None
            m = p17.match(line)
            if m:
                index_count_dict['in_sa_ah_auth_algorithm'] = m.groupdict()['in_sa_ah_auth_algorithm']
                continue

            # In SA ESP auth algo:         None
            m = p18.match(line)
            if m:
                index_count_dict['in_sa_esp_auth_algorithm'] = m.groupdict()['in_sa_esp_auth_algorithm']
                continue

            # In SA uncompress algorithm:  None
            m = p19.match(line)
            if m:
                index_count_dict['in_sa_uncompress_algorithm'] = m.groupdict()['in_sa_uncompress_algorithm']
                continue

            # Out SA DH group:             None
            m = p20.match(line)
            if m:
                index_count_dict['out_sa_dh_group'] = m.groupdict()['out_sa_dh_group']
                continue

            # Out SA encryption algorithm: aes
            m = p21.match(line)
            if m:
                index_count_dict['out_sa_encrypt_algorithm'] = m.groupdict()['out_sa_encrypt_algorithm']
                continue

            # Out SA auth algorithm:       None
            m = p22.match(line)
            if m:
                index_count_dict['out_sa_ah_auth_algorithm'] = m.groupdict()['out_sa_ah_auth_algorithm']
                continue

            # Out SA ESP auth algorithm:   None
            m = p23.match(line)
            if m:
                index_count_dict['out_sa_esp_auth_algorithm'] = m.groupdict()['out_sa_esp_auth_algorithm']
                continue

            # Out SA uncompress algorithm: None
            m = p24.match(line)
            if m:
                index_count_dict['out_sa_uncompress_algorithm'] = m.groupdict()['out_sa_uncompress_algorithm']
                continue

            # In octets:                   386160
            m = p25.match(line)
            if m:
                index_count_dict['in_octets'] = int(m.groupdict()['in_octets'])
                continue

            # Decompressed octets:         386160
            if not decompressed_octets_seen:
                m = p26.match(line)
                if m:
                    index_count_dict['decompressed_octets'] = int(m.groupdict()['decompressed_octets'])
                    decompressed_octets_seen = True
                    continue

            # In packets:                  3210
            m = p27.match(line)
            if m:
                index_count_dict['in_packets'] = int(m.groupdict()['in_packets'])
                continue

            # In drops:                    0
            m = p28.match(line)
            if m:
                index_count_dict['in_drops'] = int(m.groupdict()['in_drops'])
                continue

            # In replay drops:             0
            m = p29.match(line)
            if m:
                index_count_dict['in_replay_drops'] = int(m.groupdict()['in_replay_drops'])
                continue

            # In authentications:          3210
            m = p30.match(line)
            if m:
                index_count_dict['in_authentications'] = int(m.groupdict()['in_authentications'])
                continue

            # In authentication failures:  0
            m = p31.match(line)
            if m:
                index_count_dict['in_auth_failures'] = int(m.groupdict()['in_auth_failures'])
                continue

            # In decrypts:                 3210
            m = p32.match(line)
            if m:
                index_count_dict['in_decrypts'] = int(m.groupdict()['in_decrypts'])
                continue

            # In decrypt failures:         0
            m = p33.match(line)
            if m:
                index_count_dict['in_decrypt_failures'] = int(m.groupdict()['in_decrypt_failures'])
                continue

            # Out octets:                  194700
            m = p34.match(line)
            if m:
                index_count_dict['out_octets'] = int(m.groupdict()['out_octets'])
                continue

            # Out uncompressed octets:     194700
            if not out_uncompressed_octets_seen:
                m = p35.match(line)
                if m:
                    index_count_dict['out_uncompressed_octets'] = int(m.groupdict()['out_uncompressed_octets'])
                    out_uncompressed_octets_seen = True
                    continue

            # Out packets:                 3222
            m = p36.match(line)
            if m:
                index_count_dict['out_packets'] = int(m.groupdict()['out_packets'])
                continue

            # Out drops:                   0
            m = p37.match(line)
            if m:
                index_count_dict['out_drops'] = int(m.groupdict()['out_drops'])
                continue

            # Out authentications:         3222
            m = p38.match(line)
            if m:
                index_count_dict['out_authentications'] = int(m.groupdict()['out_authentications'])
                continue

            # Out authentication failures: 0
            m = p39.match(line)
            if m:
                index_count_dict['out_auth_failures'] = int(m.groupdict()['out_auth_failures'])
                continue

            # Out encryptions:             3222
            m = p40.match(line)
            if m:
                index_count_dict['out_encryptions'] = int(m.groupdict()['out_encryptions'])
                continue

            # Out encryption failures:     0
            m = p41.match(line)
            if m:
                index_count_dict['out_encryption_failures'] = int(m.groupdict()['out_encryption_failures'])
                continue

            # Compressed octets:           0
            m = p42.match(line)
            if m:
                index_count_dict['compressed_octets'] = int(m.groupdict()['compressed_octets'])
                continue

            # Decompressed octets:         0
            if decompressed_octets_seen:
                m = p43.match(line)
                if m:
                    index_count_dict['decompressed_octets_1'] = int(m.groupdict()['decompressed_octets_1'])
                    continue

            # Out uncompressed octets:     0
            if out_uncompressed_octets_seen:
                m = p44.match(line)
                if m:
                    index_count_dict['out_uncompressed_octets_1'] = int(m.groupdict()['out_uncompressed_octets_1'])
                    continue

        return flowmib_tunnel_dict

# ==============================
# Schema for
#   'show crypto ikev2 session'
#   'show crypto ikev2 session detailed'
# ==============================
class ShowCryptoIkev2SessionSchema(MetaParser):
    """
    Schema for
        * 'show crypto ikev2 session'
        * 'show crypto ikev2 session detailed'
    """
    
    schema = {
        'ikev2_session': {
            Or('IPv4', 'IPv6'):{
                int:{
                    'session_id': int,
                    'status': str,
                    'ike_count': int,
                    'child_count': int,
                    'tunnel_id': int,
                    'local_ip': str,
                    'local_port': int,
                    'remote_ip': str,
                    'remote_port': int,
                    'fvrf': str,
                    'ivrf': str,
                    'session_status': str,
                    Optional('encryption'): str,
                    Optional('key_length'): int,
                    Optional('prf'): str,
                    Optional('hash_algo'): str,
                    Optional('dh_group'): int,
                    Optional('auth_sign'): str,
                    Optional('auth_verify'): str,
                    Optional('lifetime'): int,
                    Optional('activetime'): int,
                    Optional('ce_id'): int,
                    Optional('id'): int,
                    Optional('mib_id'): int,
                    Optional('local_spi'): str,
                    Optional('remote_spi'): str,
                    Optional('local_id'): str,
                    Optional('remote_id'): str,
                    Optional('remote_eap_id'): str,
                    Optional('local_mesg_id'): int,
                    Optional('remote_mesg_id'): int,
                    Optional('local_next_id'): int,
                    Optional('remote_next_id'): int,
                    Optional('local_queued'): int,
                    Optional('remote_queued'): int,
                    Optional('local_window'): int,
                    Optional('remote_window'): int,
                    Optional('dpd_time'): int,
                    Optional('dpd_retry'): int,
                    Optional('fragmentation'): str,
                    Optional('dynamic_route'): str,
                    Optional('nat_detected'): str,
                    Optional('cts_sgt'): str,
                    Optional('initiator_of_sa'): str,
                    Optional('child_sa'):{
                        int:{
                            'local_selectors': list,
                            'remote_selectors': list,
                            Optional('esp_spi_in'): str,
                            Optional('esp_spi_out'): str,
                            Optional('ah_spi_in'): str,
                            Optional('ah_spi_out'): str,
                            Optional('cpi_in'): str,
                            Optional('cpi_out'): str,
                            Optional('child_encr'): str,
                            Optional('keysize'): int,
                            Optional('esp_hmac'): str,
                            Optional('ah_hmac'): str,
                            Optional('compression'): str,
                            Optional('mode'): str,
                        },
                    },
                },
            },
        },
    }

class ShowCryptoIkev2Session(ShowCryptoIkev2SessionSchema):   
    # Defines a function to run the cli_command
    cli_command = ['show crypto ikev2 session',
                'show crypto ikev2 session detailed']

    def cli(self, detail=False, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[int(detail)]) 

        # initial return dictionary
        ret_dict = {}
 
        # IPv4 Crypto IKEv2 Session
        # IPv6 Crypto IKEv2 Session
        p1 = re.compile(r'^(?P<version>\S+) Crypto IKEv2 Session$')
   
        # Session-id:3, Status:UP-ACTIVE, IKE count:1, CHILD count:1
        p2 = re.compile(r'^Session-id:(?P<s_id>\d+),\s+Status:(?P<stats>\S+),\s+'
                        r'IKE count:(?P<ike>\d+),\s+CHILD count:(?P<child>\d+)$')
       
        # 1         1.1.1.1/500           1.1.1.2/500           none/none            READY
        # 2         1.1.1.1/4500          17.27.1.12/45711      none/10              READY
        p3 = re.compile(r'^(?P<t_id>\d+)\s+(?P<loc_ip>\S+)\/(?P<loc_port>\d+)\s+'
                        r'(?P<rem_ip>\S+)\/(?P<rem_port>\d+)\s+'
                        r'(?P<f_vrf>\S+)\/(?P<i_vrf>\S+)\s+(?P<sess_stats>\S+)$')
 
        # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: RSA, Auth verify: AnyConnect-EAP
        # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:14, Auth sign: PSK, Auth verify: PSK
        p4 = re.compile(r'^Encr:\s+(?P<encr>\S+),\s+keysize:\s+(?P<key_len>\d+),\s+'
                        r'PRF:\s+(?P<random>\S+),\s+Hash:\s+(?P<hash>\S+),\s+DH Grp:(?P<dh>\d+),\s+'
                        r'Auth sign:\s+(?P<auth>\S+),\s+Auth verify:\s+(?P<auth_ver>\S+)$')
 
        # Life/Active Time: 86400/38157 sec
        p5 = re.compile(r'^Life\/Active\s+Time:\s+(?P<life>\d+)\/(?P<active>\d+)\s+sec$')
 
        # CE id: 1008, Session-id: 3
        # CE id: 0, Session-id: 1, MIB-id: 1
        p6 = re.compile(r'^CE\s+id:\s+(?P<c_id>\d+),\s+Session-id:\s+(?P<se_id>\d+)(,\s+MIB-id:\s+(?P<m_id>\d+))?$')
 
        # Local spi: 12A1648D1789A9F9       Remote spi: 0408D9A1AFA334B4
        p7 = re.compile(r'^Local spi:\s+(?P<l_spi>\S+)\s+Remote spi:\s+(?P<r_spi>\S+)$')
 
        # Local id: 1.1.1.1
        p8 = re.compile(r'^Local id:\s+(?P<l_id>\S+)$')
 
        # Remote id: 1.1.1.2
        # Remote id: Scale
        p9 = re.compile(r'^Remote id:\s+(?P<r_id>\S+)$')
 
        # Remote EAP id: docker9_69
        p10 = re.compile(r'^Remote EAP id:\s+(?P<r_eap_id>\S+)$')
 
        # Local req msg id:  2              Remote req msg id:  0
        p11 = re.compile(r'^Local req msg id:\s+(?P<l_req_id>\d+)\s+'
                         r'Remote req msg id:\s+(?P<r_req_id>\d+)$')
 
        # Local next msg id: 2              Remote next msg id: 0
        p12 = re.compile(r'^Local next msg id:\s+(?P<l_next_id>\d+)\s+'
                         r'Remote next msg id:\s+(?P<r_next_id>\d+)$')
 
        # Local req queued:  2              Remote req queued:  0
        p13 = re.compile(r'^Local req queued:\s+(?P<l_queued>\d+)\s+'
                         r'Remote req queued:\s+(?P<r_queued>\d+)$')
 
        # Local window:      5              Remote window:      5
        p14 = re.compile(r'^Local window:\s+(?P<l_window>\d+)\s+'
                         r'Remote window:\s+(?P<r_window>\d+)$')
 
        # DPD configured for 45 seconds, retry 2
        p15 = re.compile(r'^DPD\s+configured\s+for\s+(?P<dpd_in>\d+)\s+seconds,\s+retry\s+(?P<retry>\d+)$')
 
        # Fragmentation not  configured.
        p16 = re.compile(r'^Fragmentation\s+not\s+configured\.$')
 
        # IETF Std Fragmentation  configured.
        p17 = re.compile(r'^IETF\s+Std\s+Fragmentation\s+configured\.$')
 
        # Dynamic Route Update: enabled
        p18 = re.compile(r'^Dynamic\s+Route\s+Update:\s+(?P<dyn_route>\S+)$')
 
        # NAT-T is not detected
        p19 = re.compile(r'^NAT-T\s+is\s+not\s+detected$')
 
        # NAT-T is detected  outside
        # NAT-T is detected  inside
        p20 = re.compile(r'^NAT-T\s+is\s+detected\s+(?P<nat>\w+)$')
 
        # Cisco Trust Security SGT is enabled
        # Cisco Trust Security SGT is disabled
        p21 = re.compile(r'^Cisco\s+Trust\s+Security\s+SGT\s+is\s+(?P<sgt>\w+)$')
 
        # Initiator of SA : Yes
        p22 = re.compile(r'^Initiator\s+of\s+SA\s+:\s+(?P<initiator>\w+)$')
 
        # Child sa: local selector  10.10.10.0/0 - 10.10.10.255/65535
        # local selector  10.10.10.0/0 - 10.10.10.255/65535
        p23 = re.compile(r'^((?P<child_sa>[\S\s]+):\s+)?local\s+selector\s+(?P<child_l>[\S\s]+)$')

        # remote selector 20.20.20.0/0 - 20.20.20.255/65535
        p24 = re.compile(r'^remote\s+selector\s+(?P<child_r>[\S\s]+)$')

        # ESP spi in/out: 0x232CB82D/0x30767B6E
        p25 = re.compile(r'^ESP\s+spi\s+in\/out:\s+(?P<esp_i>\S+)\/(?P<esp_o>\S+)$')

        # AH spi in/out: 0x0/0x0
        p26 = re.compile(r'^AH\s+spi\s+in\/out:\s+(?P<ah_i>\S+)\/(?P<ah_o>\S+)$')

        # CPI in/out: 0x0/0x0
        p27 = re.compile(r'^CPI\s+in\/out:\s+(?P<cpi_i>\S+)\/(?P<cpi_o>\S+)$')

        # Encr: AES-CBC, keysize: 256, esp_hmac: SHA256
        p28 = re.compile(r'^Encr:\s+(?P<encr_algo>\S+),\s+keysize:\s+(?P<key_s>\d+),\s+'
                         r'esp_hmac:\s+(?P<hmac>\S+)$')

        # ah_hmac: None, comp: IPCOMP_NONE, mode tunnel
        p29 = re.compile(r'^ah_hmac:\s+(?P<ahhmac>[\S\s]*),\s+comp:\s+(?P<comp>\S+),\s+'
                         r'mode\s+(?P<tunnel_type>\S+)$')

        child_count = count = 0
        for line in output.splitlines():
            line = line.strip()
            # IPv4 Crypto IKEv2 Session
            # IPv6 Crypto IKEv2 Session
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ser_dict = ret_dict.setdefault('ikev2_session', {})
                if group['version'] == "IPv4":
                    sub_dict = ser_dict.setdefault('IPv4', {})
               
                if group['version'] == "IPv6":
                    count = 0
                    sub_dict = ser_dict.setdefault('IPv6', {})
                continue
 
            # Session-id:3, Status:UP-ACTIVE, IKE count:1, CHILD count:1
            m = p2.match(line)
            if m:
                count += 1
                child_count = 0 
                ikev2_dict = sub_dict.setdefault(count, {})
                group = m.groupdict()
                ikev2_dict['session_id'] = int(group['s_id'])
                ikev2_dict['status'] = group['stats']
                ikev2_dict['ike_count'] = int(group['ike'])
                ikev2_dict['child_count'] = int(group['child'])
                continue
            # 1         1.1.1.1/500           1.1.1.2/500           none/none            READY
            # 2         1.1.1.1/4500          17.27.1.12/45711      none/10              READY
            m = p3.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['tunnel_id'] = int(group['t_id'])
                ikev2_dict['local_ip'] = group['loc_ip']
                ikev2_dict['local_port'] = int(group['loc_port'])
                ikev2_dict['remote_ip'] = group['rem_ip']
                ikev2_dict['remote_port'] = int(group['rem_port'])
                ikev2_dict['fvrf'] = group['f_vrf']
                ikev2_dict['ivrf'] = group['i_vrf']
                ikev2_dict['session_status'] = group['sess_stats']
                continue

            # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: RSA, Auth verify: AnyConnect-EAP
            # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:14, Auth sign: PSK, Auth verify: PSK
            m = p4.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['encryption'] = group['encr']
                ikev2_dict['key_length'] = int(group['key_len'])
                ikev2_dict['prf'] = group['random']
                ikev2_dict['hash_algo'] = group['hash']
                ikev2_dict['dh_group'] = int(group['dh'])
                ikev2_dict['auth_sign'] = group['auth']
                ikev2_dict['auth_verify'] = group['auth_ver']
                continue

            # Life/Active Time: 86400/38157 sec
            m = p5.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['lifetime'] = int(group['life'])
                ikev2_dict['activetime'] = int(group['active'])
                continue

            # CE id: 1008, Session-id: 3
            # CE id: 0, Session-id: 1, MIB-id: 1
            m = p6.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['ce_id'] = int(group['c_id'])
                ikev2_dict['id'] = int(group['se_id'])
                if group['m_id'] is not None:
                    ikev2_dict['mib_id'] = int(group['m_id'])
                continue

            # Local spi: 12A1648D1789A9F9       Remote spi: 0408D9A1AFA334B4
            m = p7.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_spi'] = group['l_spi']
                ikev2_dict['remote_spi'] = group['r_spi']
                continue
            # Local id: 1.1.1.1
            m = p8.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_id'] = group['l_id']
                continue
            
            # Remote id: 1.1.1.2
            # Remote id: Scale
            m = p9.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['remote_id'] = group['r_id']
                continue
            
            # Remote EAP id: docker9_69
            m = p10.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['remote_eap_id'] = group['r_eap_id']
                continue
            
            # Local req msg id:  2              Remote req msg id:  0
            m = p11.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_mesg_id'] = int(group['l_req_id'])
                ikev2_dict['remote_mesg_id'] = int(group['r_req_id'])
                continue
            
            # Local next msg id: 2              Remote next msg id: 0
            m = p12.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_next_id'] = int(group['l_next_id'])
                ikev2_dict['remote_next_id'] = int(group['r_next_id'])
                continue

            # Local req queued:  2              Remote req queued:  0
            m = p13.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_queued'] = int(group['l_queued'])
                ikev2_dict['remote_queued'] = int(group['r_queued'])
                continue

            # Local window:      5              Remote window:      5
            m = p14.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['local_window'] = int(group['l_window'])
                ikev2_dict['remote_window'] = int(group['r_window'])
                continue

            # DPD configured for 45 seconds, retry 2
            m = p15.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['dpd_time'] = int(group['dpd_in'])
                ikev2_dict['dpd_retry'] = int(group['retry'])
                continue

            # Fragmentation not  configured.
            m = p16.match(line)
            if m:    
                ikev2_dict['fragmentation'] = "no"
                continue

            # IETF Std Fragmentation  configured.
            m = p17.match(line)
            if m:    
                ikev2_dict['fragmentation'] = "yes"
                continue
            
            # Dynamic Route Update: enabled
            m = p18.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['dynamic_route'] = group['dyn_route']
                continue

            # NAT-T is not detected
            m = p19.match(line)
            if m:    
                ikev2_dict['nat_detected'] = "no"
                continue

            # NAT-T is detected  outside
            # NAT-T is detected  inside
            m = p20.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['nat_t'] = group['nat']
                continue
            
            # Cisco Trust Security SGT is enabled
            # Cisco Trust Security SGT is disabled
            m = p21.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['cts_sgt'] = group['sgt']
                continue

            # Initiator of SA : Yes
            m = p22.match(line)
            if m:    
                group = m.groupdict()
                ikev2_dict['initiator_of_sa'] = group['initiator']
                continue
            
            # Child sa: local selector  10.10.10.0/0 - 10.10.10.255/65535
            # local selector  10.10.10.0/0 - 10.10.10.255/65535
            m = p23.match(line)
            if m:    
                group = m.groupdict()
                if group['child_sa'] == "Child sa":
                    child_dict = ikev2_dict.setdefault('child_sa', {})
                    child_count += 1 
                    child_entry_dict = child_dict.setdefault(child_count, {})
                    child_entry_dict.update({'local_selectors':  []})
                    child_entry_dict.update({'remote_selectors':  []})

                child_entry_dict['local_selectors'].append(group['child_l'])
                continue
            
            # remote selector 20.20.20.0/0 - 20.20.20.255/65535
            m = p24.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['remote_selectors'].append(group['child_r'])
                continue

            # ESP spi in/out: 0x232CB82D/0x30767B6E
            m = p25.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['esp_spi_in'] = group['esp_i']
                child_entry_dict['esp_spi_out'] = group['esp_o']
                continue

            # AH spi in/out: 0x0/0x0
            m = p26.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['ah_spi_in'] = group['ah_i']
                child_entry_dict['ah_spi_out'] = group['ah_o']
                continue

            # CPI in/out: 0x0/0x0
            m = p27.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['cpi_in'] = group['cpi_i']
                child_entry_dict['cpi_out'] = group['cpi_o']

            # Encr: AES-CBC, keysize: 256, esp_hmac: SHA256
            m = p28.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['child_encr'] = group['encr_algo']
                child_entry_dict['keysize'] = int(group['key_s'])
                child_entry_dict['esp_hmac'] = group['hmac']
                
            # ah_hmac: None, comp: IPCOMP_NONE, mode tunnel
            m = p29.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['ah_hmac'] = group['ahhmac']
                child_entry_dict['compression'] = group['comp']
                child_entry_dict['mode'] = group['tunnel_type']

        if ret_dict['ikev2_session']['IPv4'] == {}:
            del ret_dict['ikev2_session']['IPv4']
 
        if ret_dict['ikev2_session']['IPv6'] == {}:
            del ret_dict['ikev2_session']['IPv6']    
 
        return ret_dict

