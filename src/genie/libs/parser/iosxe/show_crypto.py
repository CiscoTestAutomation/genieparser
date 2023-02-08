"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto pki certificates <WORD>
   * show crypto entropy status
   * show crypto ipsec sa count
   * show crypto ikev2 sa detail
   * show crypto ikev2 sa local {} detail
   * show crypto ikev2 sa local {}
   * show crypto ikev2 sa remote {} detail
   * show crypto ikev2 sa remote {}
   * show crypto session
   * show crypto session detail
   * show crypto session local {} detail
   * show crypto session local {}
   * show crypto ikev2 stats timeout
   * show crypto ikev2 stats reconnect
   * show crypto ipsec sa detail
   * show crypto ipsec sa
   * show crypto ipsec sa peer {} detail
   * show crypto ipsec sa peer {}
   * show crypto gdoi ipsec sa
   * show crypto gkm gm replay
   * show crypto gdoi feature and sub commands
   * show crypto gdoi gm
   * show crypto gdoi ks coop version 
   * show crypto gdoi ks
   * show crypto gdoi rekey sa
   * show crypto gdoi rekey sa detail
   * show tunnel protection statistics
   * show crypto gdoi ks detail
   * show crypto gdoi ks coop detail
   * show crypto gdoi ks identifier
   * show crypto gdoi ks identifier detail
   * show crypto gdoi ks coop identifier detail
   * show crypto ikev2 psh
   * show crypto ikev2 performance
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
            Optional("peer"):{
                Any():
                {
                    "port":{
                        Any():
                        {
                        Optional("fvrf"): str,
                        Optional("ivrf"): str,
                        Optional("phase1_id"): str,
                        Optional("desc"): str,
                        Optional("ike_sa"):{
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
                        Optional("ipsec_flow"): {
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
        p8=re.compile(r'^Peer\:\s+(?P<peer>[\d\.\:]+)\s+port\s+(?P<port>\d+)(\s+fvrf\:\s+\(*(?P<fvrf>none|[^(]\S+)\)*\s+ivrf\:\s+\(*(?P<ivrf>none|[^(]\S+)\)*)?')
        
        # Phase1_id: 11.0.1.2
        p9=re.compile(r'^\s*Phase1\_id\:\s+(?P<phase_id>\S+)$')

        # Desc: (none)
        p10=re.compile(r'^\s*Desc\:\s+\(?(?P<desc>none|.*)\)?$')

        # Session ID: 0  
        p11=re.compile(r'^\s*Session\s+ID\:\s+(?P<session_id>\d+)$')

        #IKEv1 SA: local 11.0.1.1/500 remote 11.0.1.2/500 Active
        p12=re.compile(r'^\s*(?P<version>IKE(v\d)*)*\s+SA\:\s+local\s+(?P<local>[\d\.\:]+)\/(?P<local_port>\d+)')

        #  Capabilities:(none) connid:1025 lifetime:03:04:13
        p13=re.compile(r'^\s*Capabilities\:\(*(?P<capabilities>\w+)+\)*\s+connid\:(?P<conn_id>\d+)\s+lifetime\:(?P<lifetime>[\d\:]+)$')

        # IPSEC FLOW: permit 47 host 11.0.1.1 host 11.0.1.2 
        p14=re.compile(r'^\s*IPSEC\s+FLOW\:\s+(?P<ipsec_flow>.+)$')

        #Active SAs: 2, origin: crypto map
        p15=re.compile(r'^\s*Active\s+SAs\:\s+(?P<active_sa>\d+)\,\s+origin\:\s+(?P<origin>[\w\s]+)$')

        #Inbound:  #pkts dec'ed 4172534851 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p16=re.compile(r'^\s*Inbound\:\s+\#pkts\s+dec\'ed\s+(?P<inbound_pkts_dec>\d+)\s+drop\s+(?P<inbound_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<inbound_life_kb>[\w\s]+)\/(?P<inbound_life_secs>[\d a-z\/\,]+)$')

        #Outbound: #pkts enc'ed 4146702954 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p17=re.compile(r'^\s*Outbound\:\s+\#pkts\s+enc\'ed\s+(?P<outbound_pkts_enc>\d+)\s+drop\s+(?P<outbound_drop>\d+)\s+life\s+\(KB\/Sec\)\s+(?P<outbound_life_kb>[\w\s]+)\/(?P<outbound_life_secs>[\d a-z\/\,]+)$')

        #remote 2001:101:0:1::2/500 Active
        p18=re.compile(r'.*remote\s+(?P<remote>[\d\.\:]+)\/(?P<remote_port>\d+)\s+(?P<conn_status>\w+)')
        
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
            
            #IKE SA: local 10.1.1.4/500
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
                ike_params_dict['version']= groups['version']
                if session_id is not None:
                    ike_params_dict['session_id']= session_id

            #remote 2001:101:0:1::2/500 Active
            m18= p18.match(line)
            if m18:
                groups=m18.groupdict()
                ike_params_dict['remote'] = groups['remote']
                ike_params_dict['remote_port']= groups['remote_port']
                ike_params_dict['sa_status']= groups['conn_status']

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

class ShowCryptoSessionInterfaceDetail(ShowCryptoSessionSuperParser,ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session interface {interface} detail'
    '''

    cli_command = "show crypto session interface {interface} detail"

    def cli(self, interface = '', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
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
                    Optional("qr"): str,
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
                    Optional("remote_subnets"): list,
                    Optional("quantum_resistance"): str
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

        # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: PSK, Auth verify: PSK, QR
        r2 = "^Encr: +(?P<encryption>[\d\w\-]+), keysize: +(?P<keysize>[\d]+), PRF: +(?P<prf>[\w]+), +Hash: +(?P<hash>[\w]+), +DH Grp:+(?P<dh_grp>[\w\d]+), +Auth sign: +(?P<auth_sign>[\w]+), +Auth verify: +(?P<auth_verify>[\w]+)(,\s+(?P<qr>[\w]+))?$"
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
        r9 = "^Local req msg id: +(?P<local_reg_msg_id>[\d]+) +Remote req msg id: +(?P<remote_req_msg_id>[\d]+)$"
        p9 = re.compile(r9)

        # Local next msg id: 214            Remote next msg id: 6
        r10 = "^Local next msg id: +(?P<local_next_msg_id>[\d]+) +Remote next msg id: +(?P<remote_next_msg_id>[\d]+)$"
        p10 = re.compile(r10)

        # Local req queued:  214            Remote req queued:  6
        r11 = "^Local req queued: +(?P<local_req_queued>[\d]+) +Remote req queued: +(?P<remote_req_queued>[\d]+)$"
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

        # Quantum Resistance Enabled
        r22 = "^Quantum Resistance +(?P<quantum_resistance>[\d\s\S]+)$"
        p22 = re.compile(r22)

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
            # Encr: AES-CBC, keysize: 256, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: PSK, Auth verify: PSK, QR
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: v.lower() for k, v in group.items() if v is not None}
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
            # Quantum Resistance Enabled
            m = p22.match(line)
            if m:
                group = m.groupdict()
                master_dict.update(group)
                continue                
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


class ShowCryptoIkev2SaRemoteDetail(ShowCryptoIkev2SaDetail, ShowCryptoIkev2SaDetailSchema):
    '''Parser for:
        * 'show crypto ikev2 sa remote {} detail'
    '''

    cli_command = "show crypto ikev2 sa remote {ip_address} detail"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(ip_address=ip_address))
        return super().cli(output=output)


class ShowCryptoIkev2SaRemote(ShowCryptoIkev2SaDetail, ShowCryptoIkev2SaDetailSchema):
    '''Parser for:
        * 'show crypto ikev2 sa remote {}'
    '''

    cli_command = "show crypto ikev2 sa remote {ip_address}"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(ip_address=ip_address))
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
                'aaa_operation': {
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
                    'sa_deletion': {
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
                Optional('gkm_operation'): {
                    'get_policy': {
                        'passed': int,
                        'failed': int
                    },
                    'set_policy': {
                        'passed': int,
                        'failed': int
                    }
                },
                Optional('ppk_sks_operation'): {
                    'ppk_get_cap': {
                        'passed': int,
                        'failed': int
                    },
                    'ppk_get_key': {
                        'passed': int,
                        'failed': int
                    },
                },
                Optional('ike_preroute'): {
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
                            Optional('traffic_selectors'): list,
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
 
        # Child sa:
        p23 = re.compile(r'^(?P<child_sa>[\S\s]+):$')

        # local selector       ->      remote selector
        p23_1 = re.compile(r'^local\s+selector\s+->\s+remote\s+selector$')

        # Child sa: local selector  10.10.10.0/0 - 10.10.10.255/65535
        # local selector  10.10.10.0/0 - 10.10.10.255/65535
        p23_2 = re.compile(r'^((?P<child_sa>[\S\s]+):\s+)?local\s+selector\s+(?P<child_l>[\S\s]+)$')

        # remote selector 20.20.20.0/0 - 20.20.20.255/65535
        p23_3 = re.compile(r'^remote\s+selector\s+(?P<child_r>[\S\s]+)$')

        # 89.89.89.0/0 - 89.89.89.255/65535    ->    99.99.99.0/0 - 99.99.99.255/65535
        # 8001::/0 - 8001::FFFF:FFFF:FFFF:FFFF/65535    ->    9001::/0 - 9001::FFFF:FFFF:FFFF:FFFF/65535
        p24 = re.compile(r'^(?P<traffic_selector>\S+\s+-\s+\S+\s+->\s+\S+\s+-\s+\S+)$')

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
            
            # Child sa:
            m1 = p23.match(line)
            if m1:
                group = m1.groupdict()
                if group['child_sa'] == "Child sa":
                    child_dict = ikev2_dict.setdefault('child_sa', {})
                    child_count += 1 
                    child_entry_dict = child_dict.setdefault(child_count, {})
                    child_entry_dict.update({'local_selectors':  []})
                    child_entry_dict.update({'remote_selectors':  []})
                continue

            # Child sa: local selector  10.10.10.0/0 - 10.10.10.255/65535
            # local selector  10.10.10.0/0 - 10.10.10.255/65535
            m2 = p23_2.match(line)
            if m2:
                group = m2.groupdict()
                if group['child_sa'] == "Child sa":
                    child_dict = ikev2_dict.setdefault('child_sa', {})
                    child_count += 1 
                    child_entry_dict = child_dict.setdefault(child_count, {})
                    child_entry_dict.update({'local_selectors':  []})
                    child_entry_dict.update({'remote_selectors':  []})
                if 'selector' not in group['child_l']:
                    child_entry_dict['local_selectors'].append(group['child_l'])
                    continue
                else:
                    child_entry_dict.update({'traffic_selectors':  []})
                continue

            # remote selector 20.20.20.0/0 - 20.20.20.255/65535
            m = p23_3.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['remote_selectors'].append(group['child_r'])
                continue

            # 89.89.89.0/0 - 89.89.89.255/65535    ->    99.99.99.0/0 - 99.99.99.255/65535
            # 8001::/0 - 8001::FFFF:FFFF:FFFF:FFFF/65535    ->    9001::/0 - 9001::FFFF:FFFF:FFFF:FFFF/65535
            m = p24.match(line)
            if m:    
                group = m.groupdict()
                child_entry_dict['traffic_selectors'].append(group['traffic_selector'])
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

# =================================================
#  Schema for 'show crypto ipsec sa detail'
# =================================================
class ShowCryptoIpsecSaDetailSchema(MetaParser):
    """Schema for show crypto ipsec sa Schema"""
    schema = {
        'interface': {
                Any(): {
                    'crypto_map_tag': str,
                    'local_addr': str,
                    'ident': {
                        Any(): {
                            'protected_vrf': str,
                            'local_ident': {
                                'addr': str,
                                'mask': str,
                                'port': str,
                                'prot': str
                                },
                            'remote_ident': {
                                'addr': str,
                                'mask': str,
                                'port': str,
                                'prot': str
                                },
                            'peer_ip': str,
                            'port': int,
                            'action': str,
                            'acl': str,
                            Optional('pkts_compr_failed'): int,
                            Optional('pkts_compressed'): int,
                            Optional('pkts_decaps'): int,
                            Optional('pkts_decompress_failed'): int,
                            Optional('pkts_decompressed'): int,
                            Optional('pkts_decrypt'): int,
                            Optional('pkts_not_compressed'): int,
                            Optional('pkts_not_decompressed'): int,
                            Optional('pkts_verify'): int,
                            Optional('pkts_internal_err_recv'): int,
                            Optional('pkts_internal_err_send'): int,
                            Optional('pkts_invalid_identity_recv'): int,
                            Optional('pkts_invalid_prot_recv'): int,
                            Optional('pkts_invalid_sa_rcv'): int,
                            Optional('pkts_no_sa_send'): int,                      
                            Optional('pkts_not_tagged_send'): int,
                            Optional('pkts_not_untagged_rcv'): int,
                            Optional('pkts_replay_failed_rcv'): int,
                            Optional('pkts_replay_rollover_rcv'): int,
                            Optional('pkts_replay_rollover_send'): int,
                            Optional('pkts_tagged_send'): int,
                            Optional('pkts_untagged_rcv'): int,
                            Optional('pkts_verify_failed'): int,
                            Optional('recv_errors'): int,
                            Optional('send_errors'): int,
                            'path_mtu': int,
                            'ip_mtu':int,
                            'pfs': str,
                            'plaintext_mtu': int,
                            'remote_crypto_endpt': str,
                            'current_outbound_spi': str,
                            'dh_group': str,
                            'ip_mtu_idb': str,
                            'local_crypto_endpt': str,
                            Or('inbound_ah_sas',
                               'inbound_esp_sas',
                               'inbound_pcp_sas',
                               'outbound_ah_sas',
                               'outbound_esp_sas',
                               'outbound_pcp_sas'): {
                                    Optional('spi'): {
                                        Any(): {
                                            Optional('conn_id'): int,
                                            Optional('crypto_map'): str,
                                            Optional('flow_id'): str,
                                            Optional('flow_id_val'): int,
                                            Optional('transform'): str,
                                            Optional('kilobyte_volume_rekey'): str,
                                            Optional('in_use_settings'): str,
                                            Optional('iv_size'): str,
                                            Optional('remaining_key_lifetime'): str,
                                            Optional('replay_detection_support'): str,
                                            Optional('sibling_flags'): str,
                                            Optional('status'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }

# ===================================================
#  Parser for 'show crypto ipsec sa detail'
# ===================================================
class ShowCryptoIpsecSaDetail(ShowCryptoIpsecSaDetailSchema):

    """Parser for show crypto ipsec sa detail"""

    cli_command = 'show crypto ipsec sa detail'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # interface: GigabitEthernet3
        p1 = re.compile(r'^interface:+ (?P<interface>[\w\d]+)$')

        # Crypto map tag: vpn-crypto-map, local addr 1.1.1.2
        p2 = re.compile(r'^Crypto map tag: (?P<crypto_map_tag>[\w\d\-]+), +local addr +(?P<local_addr>[\d\.]+)$')

        # protected vrf: (none)
        p3 = re.compile(r'^protected vrf: (?P<protected_vrf>\S+)$')

        # local ident (addr/mask/prot/port): (20.20.20.0/255.255.255.0/0/0)
        p4 = re.compile(r'^local.*: +\((?P<addr>[0-9\.]+)\/(?P<mask>[0-9\.]+)\/(?P<prot>[\d]+)\/(?P<port>[\d]+)\)$')

        # remote ident (addr/mask/prot/port): (10.10.10.0/255.255.255.0/0/0)
        p5 = re.compile(r'^remote.*: +\((?P<addr>[0-9\.]+)\/(?P<mask>[0-9\.]+)\/(?P<prot>[\d]+)\/(?P<port>[\d]+)\)$')

        # current_peer 1.1.1.1 port 500
        p6 = re.compile(r'^current_peer +(?P<peer_ip>[0-9\.]+) +port +(?P<port>[0-9]+)$')

        # PERMIT, flags={origin_is_acl,}
        p7 = re.compile(r'^(?P<action>\w+), +flags=\{(?P<acl>[\w\_\-\,]+)\}$')

        # #pkts encaps: 4, #pkts encrypt: 4, #pkts digest: 4
        p8 = re.compile(r'^#pkts encaps: +(?P<pkts_decaps>\d+).*: +(?P<pkts_decrypt>\d+).*: +(?P<pkts_verify>\d+)$')

        # #pkts decaps: 4, #pkts decrypt: 4, #pkts verify: 4
        p9 = re.compile(r'^#pkts decaps: +(?P<pkts_decaps>\d+).*: +(?P<pkts_decrypt>\d+).*: +(?P<pkts_verify>\d+)$')

        # #pkts compressed: 0, #pkts decompressed: 0
        p10 = re.compile(r'^#pkts compressed: +(?P<pkts_compressed>\d+).*: +(?P<pkts_decompressed>\d+)$')

        # #pkts not compressed: 0, #pkts compr. failed: 0
        p11 = re.compile(r'^#pkts not compressed: +(?P<pkts_not_compressed>\d+).*: +(?P<pkts_compr_failed>\d+)$')

        # #pkts not decompressed: 0, #pkts decompress failed: 0
        p12 = re.compile(r'^#pkts not decompressed: +(?P<pkts_not_decompressed>\d+).*: +(?P<pkts_decompress_failed>\d+)$')

        # #send errors 0, #recv errors 0 
        p13 = re.compile(r'^#send errors +(?P<send_errors>\d+).* +(?P<recv_errors>\d+)$')

        # #pkts no sa (send) 0, #pkts invalid sa (rcv) 0 
        p14 = re.compile(r'^#pkts no sa.* +(?P<pkts_no_sa_send>\d+).* +(?P<pkts_invalid_sa_rcv>\d+)$')

        # #pkts invalid prot (recv) 0, #pkts verify failed: 0
        p15 = re.compile(r'^#pkts invalid prot.* +(?P<pkts_invalid_prot_recv>\d+).* +(?P<pkts_verify_failed>\d+)$')

        # #pkts invalid identity (recv) 0, #pkts invalid len (rcv) 0 
        p16 = re.compile(r'^#pkts invalid identity.* +(?P<pkts_invalid_identity_recv>\d+).* +(?P<pkts_verify_failed>\d+)$')

        # #pkts replay rollover (send): 0, #pkts replay rollover (rcv) 0 
        p17 = re.compile(r'^#pkts replay rollover.* +(?P<pkts_replay_rollover_send>\d+).* +(?P<pkts_replay_rollover_rcv>\d+)$')

        # ##pkts replay failed (rcv): 0 
        p18 = re.compile(r'^##pkts replay failed.* +(?P<pkts_replay_failed_rcv>\d+)$')

        # #pkts tagged (send): 0, #pkts untagged (rcv): 0 
        p19 = re.compile(r'^#pkts tagged.* +(?P<pkts_tagged_send>\d+).*: +(?P<pkts_untagged_rcv>\d+)$')

        # #pkts not tagged (send): 0, #pkts not untagged (rcv): 0 
        p20 = re.compile(r'^#pkts not tagged.* +(?P<pkts_not_tagged_send>\d+).*: +(?P<pkts_not_untagged_rcv>\d+)$')

        # #pkts internal err (send): 0, #pkts internal err (recv) 0 
        p21 = re.compile(r'^#pkts internal err.* +(?P<pkts_internal_err_send>\d+).* +(?P<pkts_internal_err_recv>\d+)$')

        # local crypto endpt.: 1.1.1.2, remote crypto endpt.: 1.1.1.1 
        p22 = re.compile(r'^local crypto endpt.: +(?P<local_crypto_endpt>[\d\.]+).* +(?P<remote_crypto_endpt>[\d\.]+)$')

        # plaintext mtu 1438, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet3 
        p23 = re.compile(r'^plaintext mtu +(?P<plaintext_mtu>\d+),.* +(?P<path_mtu>\d+), ip mtu +(?P<ip_mtu>\d+),.*idb +(?P<ip_mtu_idb>\S+)$')

        # current outbound spi: 0x397C36EE(964441838) 
        p24 = re.compile(r'^current outbound spi: +(?P<current_outbound_spi>\S+)$')

        # PFS (Y/N): N, DH group: none 
        p25 = re.compile(r'^PFS.*: +(?P<pfs>[Y|N]+).*: +(?P<dh_group>\w+)$')

        # inbound esp sas: 
        p26 = re.compile(r'^inbound esp sas:$')

        # spi: 0x658F7C11(1703902225) 
        p27 = re.compile(r'^spi: +(?P<spi>[\S]+)$')

        # transform: esp-256-aes esp-sha256-hmac , 
        p28 = re.compile(r'^transform: +(?P<transform>[\S\s]+).*,$')

        # in use settings ={Tunnel, }
        p29 = re.compile(r'^in use settings =+\{(?P<in_use_settings>[\w\,\s]+)\}$')

        # conn id: 2076, flow_id: CSR:76, sibling_flags FFFFFFFF80000048, crypto map: vpn-crypto-map
        p30 = re.compile(r'^conn id: +(?P<conn_id>\d+), +flow_id: +(?P<flow_id>\w+):(?P<flow_id_val>\d+), +sibling_flags +(?P<sibling_flags>[\w\d]+), +crypto map: +(?P<crypto_map>[\w\-\d]+)$')

        # sa timing: remaining key lifetime (k/sec): (4607999/83191) 
        p31 = re.compile(r'^sa timing.* +(?P<remaining_key_lifetime>[\S\s]+)$')

        # Kilobyte Volume Rekey has been disabled
        p32 = re.compile(r'^Kilobyte Volume Rekey has been +(?P<kilobyte_volume_rekey>[disabled|enabled]+)$')

        # IV size: 16 bytes
        p33 = re.compile(r'^IV size: +(?P<iv_size>[\w\s]+)$')

        # replay detection support: Y
        p34 = re.compile(r'^replay detection support: +(?P<replay_detection_support>\w+)$')

        # Status: ACTIVE(ACTIVE) 
        p35 = re.compile(r'^Status: +(?P<status>\S+)$')

        # inbound ah sas:
        p36 = re.compile(r'^inbound ah sas:$')

        # inbound pcp sas:
        p37 = re.compile(r'^inbound pcp sas:$')

        # outbound esp sas: 
        p38 = re.compile(r'^outbound esp sas:$')

        # outbound ah sas:
        p39 = re.compile(r'^outbound ah sas:$')

        # outbound pcp sas:
        p40 = re.compile(r'^outbound pcp sas:$')

        master_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # interface: GigabitEthernet3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                peer_dict = master_dict.setdefault('interface', {}).setdefault(group['interface'],{})
                count = 1
                continue
            
            # Crypto map tag: vpn-crypto-map, local addr 1.1.1.2
            m = p2.match(line)
            if m:
                peer_dict.update(m.groupdict())
                session_dict = peer_dict.setdefault('ident',{})
                continue

            # protected vrf: (none)
            m = p3.match(line)
            if m:
                ident_dict = session_dict.setdefault(count,{})
                count += 1
                ident_dict.update(m.groupdict())
                continue

            # local ident (addr/mask/prot/port): (20.20.20.0/255.255.255.0/0/0)
            m = p4.match(line)
            if m:
                local_ident = ident_dict.setdefault('local_ident',{})
                local_ident.update(m.groupdict())
                continue

            # remote ident (addr/mask/prot/port): (10.10.10.0/255.255.255.0/0/0)
            m = p5.match(line)
            if m:
                remote_ident = ident_dict.setdefault('remote_ident',{})
                remote_ident.update(m.groupdict())
                continue

            # current_peer 1.1.1.1 port 500
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group['port'] = int(group['port'])
                ident_dict.update(group)
                continue

            # PERMIT, flags={origin_is_acl,}
            m = p7.match(line)
            if m:
                ident_dict.update(m.groupdict())
                continue

            # #pkts encaps: 4, #pkts encrypt: 4, #pkts digest: 4
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts decaps: 4, #pkts decrypt: 4, #pkts verify: 4
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts compressed: 0, #pkts decompressed: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts not compressed: 0, #pkts compr. failed: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts not decompressed: 0, #pkts decompress failed: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #send errors 0, #recv errors 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts no sa (send) 0, #pkts invalid sa (rcv) 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts invalid prot (recv) 0, #pkts verify failed: 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts invalid identity (recv) 0, #pkts invalid len (rcv) 0 
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts replay rollover (send): 0, #pkts replay rollover (rcv) 0 
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # ##pkts replay failed (rcv): 0 
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts tagged (send): 0, #pkts untagged (rcv): 0 
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts not tagged (send): 0, #pkts not untagged (rcv): 0 
            m = p20.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # #pkts internal err (send): 0, #pkts internal err (recv) 0 
            m = p21.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ident_dict.update(group)
                continue

            # local crypto endpt.: 1.1.1.2, remote crypto endpt.: 1.1.1.1
            m = p22.match(line)
            if m:
                ident_dict.update(m.groupdict())
                continue

            # plaintext mtu 1438, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet3 
            m = p23.match(line)
            if m:
                group = m.groupdict()
                group['plaintext_mtu'] = int(group['plaintext_mtu'])
                group['path_mtu'] = int(group['path_mtu'])
                group['ip_mtu'] = int(group['ip_mtu'])
                ident_dict.update(group)
                continue

            # current outbound spi: 0x397C36EE(964441838)
            m = p24.match(line)
            if m:
                ident_dict.update(m.groupdict())
                continue

            # PFS (Y/N): N, DH group: none
            m = p25.match(line)
            if m:
                ident_dict.update(m.groupdict())
                continue

            # inbound esp sas:
            m = p26.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('inbound_esp_sas',{})
                continue
            
            # inbound ah sas:
            m = p36.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('inbound_ah_sas',{})
                continue

            # inbound pcp sas:
            m=p37.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('inbound_pcp_sas',{})
                continue

            # outbound esp sas:
            m = p38.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('outbound_esp_sas',{})
                continue

            # outbound ah sas:
            m = p39.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('outbound_ah_sas',{})
                continue

            # outbound pcp sas:
            m = p40.match(line)
            if m:
                prv_line = line
                sas_dict = ident_dict.setdefault('outbound_pcp_sas',{})
                continue

            # spi: 0x658F7C11(1703902225)
            m = p27.match(line)
            if m:
                group = m.groupdict()
                spi_dict = sas_dict.setdefault('spi',{}).setdefault(group['spi'],{})
                continue

            # transform: esp-256-aes esp-sha256-hmac ,
            m = p28.match(line)
            if m:
                group = m.groupdict()
                group = {k: v.strip() for k, v in group.items()}
                spi_dict.update(group)
                continue

            # in use settings ={Tunnel, } 
            m = p29.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

            # conn id: 2076, flow_id: CSR:76, sibling_flags FFFFFFFF80000048, crypto map: vpn-crypto-map 
            m = p30.match(line)
            if m:
                group = m.groupdict()
                group['conn_id'] = int(group['conn_id'])
                group['flow_id_val'] = int(group['flow_id_val'])
                spi_dict.update(group)
                continue

            # sa timing: remaining key lifetime (k/sec): (4607999/83191)
            m = p31.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

            # Kilobyte Volume Rekey has been disabled
            m = p32.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

            # IV size: 16 bytes 
            m = p33.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

            # replay detection support: Y 
            m = p34.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

            # Status: ACTIVE(ACTIVE)
            m = p35.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue

        return master_dict

# =================================================
#  Parser for 'show crypto ipsec sa'
# =================================================
class ShowCryptoIpsecSa(ShowCryptoIpsecSaDetail):
    '''Parser for:
        * 'show crypto ikev2 sa local {} detail'
    '''

    cli_command = "show crypto ipsec sa"

    def cli(self, ip_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# =================================================
#  Parser for 'show crypto ipsec sa peer {peer_address} detail'
# =================================================
class ShowCryptoIpsecSaPeerDetail(ShowCryptoIpsecSaDetail):
    '''Parser for:
        * 'show crypto ipsec sa peer {peer_address} detail'
    '''

    cli_command = "show crypto ipsec sa peer {peer_address} detail"

    def cli(self, peer_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# =================================================
#  Parser for 'show crypto ipsec sa peer {peer_address}'
# =================================================
class ShowCryptoIpsecSaPeer(ShowCryptoIpsecSaDetail):
    '''Parser for:
        * 'show crypto ipsec sa peer {peer_address}'
    '''

    cli_command = "show crypto ipsec sa peer {peer_address}"

    def cli(self, peer_address='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# ====================================================
#  Schema for show crypto sockets'
# ====================================================
class ShowCryptoSocketsSchema(MetaParser):
    """Schema for show crypto sockets"""
    schema = {
    'socket_connections': { 
        'sockets_in_listen_state': list,
        'total_socket_connections': int,
        Any(): {
            'peers': {
                'local_ip': str,
                'remote_ip': str
            },
            'local_ident': {
                'address': str,
                'mask': str,
                'port': int,
                'protocol': int
            },
            'remote_ident': {
                'address': str,
                'mask': str,
                'port': int,
                'protocol': int
            },
            'client_name': str,
            'client_state': str, 
            'socket_state': str,  
            'ipsec_profile': str,
            Optional('true_ident'): list
        }    
    }
}

# ==================================
#  Parser for 'show crypto sockets'
# ==================================
class ShowCryptoSockets(ShowCryptoSocketsSchema):
    """Parser for 
        * show crypto socket
    """

    cli_command = 'show crypto sockets'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        # initial return dictionary
        crypto_sockets_dict = {}

        # Number of Crypto Socket connections 4
        p1 = re.compile(r'^Number\s+of\s+Crypto\s+Socket\s+connections\s+(?P<socket_connections>(\d+))')

        # Tu1 Peers (local/remote): 85.45.1.1/10.0.0.2
        p2 = re.compile(r'^(?P<tunnel_name>[\S\s]+)\s+Peers\s+\(local\/remote\):\s+(?P<local_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\/(?P<remote_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))')

        # Local Ident  (addr/mask/port/prot): (85.45.3.1/255.255.255.255/0/47)
        p3 = re.compile(r'^Local\s+Ident\s+\(addr\/mask\/port\/prot\):\s+\((?P<local_ident_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\/(?P<local_ident_mask>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\/(?P<local_ident_port>(\d+))\/(?P<local_ident_protocol>(\d+))')

        # Remote Ident (addr/mask/port/prot): (10.0.0.2/255.255.255.255/0/47)
        p4 = re.compile(r'^Remote\s+Ident\s+\(addr\/mask\/port\/prot\):\s+\((?P<remote_ident_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\/(?P<remote_ident_mask>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\/(?P<remote_ident_port>(\d+))\/(?P<remote_ident_protocol>(\d+))')

        # IPSec Profile: "IPSEC_PROFILE"
        p5 = re.compile(r'^IPSec\s+Profile:\s+\"(?P<ipsec_profile>[\S\s]+)\"')
        
        # Socket State: Open
        p6 = re.compile(r'^Socket\s+State:\s+(?P<socket_state>[\S\s]+)')
        
        # Client: "TUNNEL SEC" (Client State: Active)
        p7 = re.compile(r'^Client:\s+\"(?P<client_name>[\S\s]+)\"\s+\(Client\s+State:\s+(?P<client_state>[\S\s]+)\)')

        # TRUE  ident (addr/mask/prot/port): {LOCAL -> REMOTE}
        p8 = re.compile(r'^TRUE\s+ident\s+\(addr\/mask\/prot\/port\):\s+', re.IGNORECASE)
        
        # Crypto Sockets in Listen state:
        p9 = re.compile(r'^Crypto\s+Sockets\s+in\s+Listen\s+state:')

        # Client: "TUNNEL SEC" Profile: "IPSEC_PROFILE" Map-name: "Tunnel20-head-0"
        p10 = re.compile(r'^Client:\s+\"(?P<name>[\S\s]+)\"\s+Profile:\s+\"(?P<client_state>[\S\s]+)\"\s+Map-name:\s+\"(?P<map_name>[\S\s]+)\"')
 
        true_ident = False
        sockets_in_listen_state = False

        result_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Number of Crypto Socket connections 4
            m = p1.match(line)
            if m:
                if 'total_socket_connections' not in crypto_sockets_dict:
                    result_dict = crypto_sockets_dict.setdefault('socket_connections', {})
                result_dict['total_socket_connections'] = int(m.groupdict()['socket_connections'])
                continue

            # Tu1 Peers (local/remote): 85.45.1.1/10.0.0.2
            m = p2.match(line)
            if m:
                true_ident = False
                tunnel_name = m.groupdict()['tunnel_name']
                socket_dict = result_dict.setdefault(tunnel_name, {}) 
                peers_dict = socket_dict.setdefault('peers', {})
                peers_dict['local_ip'] = m.groupdict()['local_ip']
                peers_dict['remote_ip'] = m.groupdict()['remote_ip']
                continue

            # Local Ident  (addr/mask/port/prot): (85.45.3.1/255.255.255.255/0/47)
            m = p3.match(line)
            if m:
                local_ident_dict = socket_dict.setdefault('local_ident', {})
                local_ident_dict['address'] = m.groupdict()['local_ident_ip']
                local_ident_dict['mask'] = m.groupdict()['local_ident_mask']
                local_ident_dict['port'] = int(m.groupdict()['local_ident_port'])
                local_ident_dict['protocol'] = int(m.groupdict()['local_ident_protocol'])
                continue 

            # Remote Ident (addr/mask/port/prot): (10.0.0.2/255.255.255.255/0/47)
            m = p4.match(line)
            if m:
                remote_ident_dict = socket_dict.setdefault('remote_ident', {})
                remote_ident_dict['address'] = m.groupdict()['remote_ident_ip']
                remote_ident_dict['mask'] = m.groupdict()['remote_ident_mask']
                remote_ident_dict['port'] = int(m.groupdict()['remote_ident_port'])
                remote_ident_dict['protocol'] = int(m.groupdict()['remote_ident_protocol'])
                continue

            # TRUE  ident (addr/mask/prot/port): {LOCAL -> REMOTE}
            m = p8.match(line)
            if m:
                true_ident = True
                socket_dict['true_ident'] = []
                continue

            # IPSec Profile: "IPSEC_PROFILE"
            m = p5.match(line)
            if m:
                true_ident = False
                socket_dict['ipsec_profile'] = m.groupdict()['ipsec_profile']
                continue

            # Socket State: Open 
            m = p6.match(line)
            if m:
                socket_dict['socket_state'] = m.groupdict()['socket_state']
                continue
            
            # Client: "TUNNEL SEC" (Client State: Active)
            m = p7.match(line)
            if m:
                socket_dict['client_name'] = m.groupdict()['client_name']
                socket_dict['client_state'] = m.groupdict()['client_state']
                continue

            if true_ident:
                socket_dict['true_ident'].append(line)
                continue

            # Crypto Sockets in Listen state:
            m = p9.match(line)
            if m:
                sockets_in_listen_state = True
                result_dict['sockets_in_listen_state'] = []
                continue

            # Client: "TUNNEL SEC" Profile: "IPSEC_PROFILE" Map-name: "Tunnel20-head-0"
            m = p10.match(line)
            if m and sockets_in_listen_state:
                result_dict['sockets_in_listen_state'].append(m.groupdict()['map_name'])
                continue

        return crypto_sockets_dict

# ====================================================
#  Schema for 'show crypto mib ipsec flowmib global'
# ====================================================
class ShowCryptoMibIpsecFlowmibGlobalSchema(MetaParser):
    """Schema for show crypto mib ipsec flowmib global"""
    schema = {
        'ipsec_flowmib_global': {
            'total_vrf': int,
            Any(): {
                'active_tunnels': int,
                'previous_tunnels': int,
                'in_octets': int,
                'out_octets': int,
                'in_packets': int,
                'out_packets': int,
                'uncompressed_encrypted_bytes': int,
                'in_packet_drops': int,
                'out_packet_drops': int,
                'in_replay_drops': int,
                'in_authentications': int,
                'out_authentications': int,
                'in_decrypts': int,
                'out_encrypts': int,
                'compressed_bytes': int,
                'uncompressed_bytes': int,
                'in_uncompressed_bytes': int,
                'out_uncompressed_bytes': int,
                'in_decrypt_failures': int,
                'out_encrypt_failures': int,
                'no_sa_failures': int,
                'protocol_use_failures': int,
                'system_capacity_failures': int,
                'in_auth_failures': int,
                'out_auth_failures': int
            }  
        }
    }
    
# ====================================================
#  Parser for 'show crypto mib ipsec flowmib global'
# ====================================================  
class ShowCryptoMibIpsecFlowmibGlobal(ShowCryptoMibIpsecFlowmibGlobalSchema):
    """Parser for 
        * show crypto mib ipsec flowmib global
    """

    cli_command = 'show crypto mib ipsec flowmib global'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        flowmib_global_dict = {}

        # vrf CC-INTERNET
        p1 = re.compile(r'^vrf\s+(?P<vrf_name>[\S\s]+)$')

        # Active Tunnels:                   2
        p2 = re.compile(r'^Active\s+Tunnels:\s+(?P<active_tunnels>\d+)$')

        # Previous Tunnels:                 16
        p3 = re.compile(r'^Previous\s+Tunnels:\s+(?P<previous_tunnels>\d+)$')

        # In octets:                        3551184
        p4 = re.compile(r'^In\s+octets:\s+(?P<in_octets>\d+)$')

        # Out octets:                       1817806
        p5 = re.compile(r'^Out\s+octets:\s+(?P<out_octets>\d+)$')

        # In packets:                       29214 
        p6 = re.compile(r'^In\s+packets:\s+(?P<in_packets>\d+)$')

        # Out packets:                      29208  
        p7 = re.compile(r'^Out\s+packets:\s+(?P<out_packets>\d+)$')

        # Uncompressed encrypted bytes:     1817806
        p8 = re.compile(r'^Uncompressed\s+encrypted\s+bytes:\s+(?P<uncompressed_encrypted_bytes>\d+)$')

        # In packets drops:                 0 
        p9 = re.compile(r'^In\s+packets\s+drops:\s+(?P<in_packet_drops>\d+)$')

        # Out packets drops:                0 
        p10 = re.compile(r'^Out\s+packets\s+drops:\s+(?P<out_packet_drops>\d+)$')
                    
        # In replay drops:                  0  
        p11 = re.compile(r'^In\s+replay\s+drops:\s+(?P<in_replay_drops>\d+)$')
                
        # In authentications:               29214    
        p12 = re.compile(r'^In\s+authentications:\s+(?P<in_authentications>\d+)$')

        # Out authentications:              29208        
        p13 = re.compile(r'^Out\s+authentications:\s+(?P<out_authentications>\d+)$')

        # In decrypts:                      29214        
        p14 = re.compile(r'^In\s+decrypts:\s+(?P<in_decrypts>\d+)$')

        # Out encrypts:                     29208     
        p15 = re.compile(r'^Out\s+encrypts:\s+(?P<out_encrypts>\d+)$')   

        # Compressed bytes:                 0
        p16 = re.compile(r'^Compressed\s+bytes:\s+(?P<compressed_bytes>\d+)$')

        # Uncompressed bytes:               0
        p17 = re.compile(r'^Uncompressed\s+bytes:\s+(?P<uncompressed_bytes>\d+)$')

        # In uncompressed bytes:            0
        p18 = re.compile(r'^In\s+uncompressed\s+bytes:\s+(?P<in_uncompressed_bytes>\d+)$')

        # Out uncompressed bytes:           0
        p19 = re.compile(r'^Out\s+uncompressed\s+bytes:\s+(?P<out_uncompressed_bytes>\d+)$')

        # In decrypt failures:              0            
        p20 = re.compile(r'^In\s+decrypt\s+failures:\s+(?P<in_decrypt_failures>\d+)$')

        # Out encrypt failures:             0            
        p21 = re.compile(r'^Out\s+encrypt\s+failures:\s+(?P<out_encrypt_failures>\d+)$')

        # No SA failures:                   0   
        p22 = re.compile(r'^No\s+SA\s+failures:\s+(?P<no_sa_failures>\d+)$')

        # Protocol use failures:            0   
        p23 = re.compile(r'^Protocol\s+use\s+failures:\s+(?P<protocol_use_failures>\d+)$')

        # System capacity failures:         0   
        p24 = re.compile(r'^System\s+capacity\s+failures:\s+(?P<system_capacity_failures>\d+)$')

        # In authentication failures:       0        
        p25 = re.compile(r'^In\s+authentication\s+failures:\s+(?P<in_auth_failures>\d+)$')

        # Out authentication failures:      0
        p26 = re.compile(r'^Out\s+authentication\s+failures:\s+(?P<out_auth_failures>\d+)$')
 
        vrf_count = 0
        result_dict = {}
        include_vrf = True

        for line in output.splitlines():
            line = line.strip()

            # vrf CC-INTERNET
            m = p1.match(line)
            if m:
                if 'total_vrf' not in flowmib_global_dict:
                    result_dict = flowmib_global_dict.setdefault('ipsec_flowmib_global', {})
                vrf_name = m.groupdict()['vrf_name']
                # Bug ID: CSCwa72431 - show crypto mib ipsec flowmib issues 
                # Ignore vrf names with ??? in the output
                if vrf_name == '???':
                    include_vrf = False
                    continue
                else:
                    include_vrf = True
                    vrf_count += 1
                result_dict['total_vrf'] = vrf_count
                vrf_name_dict = result_dict.setdefault(vrf_name, {})
                continue
            
            if include_vrf:
                # Active Tunnels:                   2
                m = p2.match(line)
                if m:
                    vrf_name_dict['active_tunnels'] = int(m.groupdict()['active_tunnels'])
                    continue

                # Previous Tunnels:                 16
                m = p3.match(line)
                if m:
                    vrf_name_dict['previous_tunnels'] = int(m.groupdict()['previous_tunnels'])
                    continue

                # In octets:                        3551184
                m = p4.match(line)
                if m:
                    vrf_name_dict['in_octets'] = int(m.groupdict()['in_octets'])
                    continue

                # Out octets:                       1817806
                m = p5.match(line)
                if m:
                    vrf_name_dict['out_octets'] = int(m.groupdict()['out_octets'])
                    continue

                # In packets:                       29214
                m = p6.match(line)
                if m:
                    vrf_name_dict['in_packets'] = int(m.groupdict()['in_packets'])
                    continue

                # Out packets:                      29208
                m = p7.match(line)
                if m:
                    vrf_name_dict['out_packets'] = int(m.groupdict()['out_packets'])
                    continue

                # Uncompressed encrypted bytes:     1817806
                m = p8.match(line)
                if m:
                    vrf_name_dict['uncompressed_encrypted_bytes'] = int(m.groupdict()['uncompressed_encrypted_bytes'])
                    continue

                # In packets drops:                 0
                m = p9.match(line)
                if m:
                    vrf_name_dict['in_packet_drops'] = int(m.groupdict()['in_packet_drops'])
                    continue

                # Out packets drops:                0
                m = p10.match(line)
                if m:
                    vrf_name_dict['out_packet_drops'] = int(m.groupdict()['out_packet_drops'])
                    continue

                # In replay drops:                  0
                m = p11.match(line)
                if m:
                    vrf_name_dict['in_replay_drops'] = int(m.groupdict()['in_replay_drops'])
                    continue

                # In authentications:               29214
                m = p12.match(line)
                if m:
                    vrf_name_dict['in_authentications'] = int(m.groupdict()['in_authentications'])
                    continue
                
                # Out authentications:              29208
                m = p13.match(line)
                if m:
                    vrf_name_dict['out_authentications'] = int(m.groupdict()['out_authentications'])
                    continue

                # In decrypts:                      29214
                m = p14.match(line)
                if m:
                    vrf_name_dict['in_decrypts'] = int(m.groupdict()['in_decrypts'])
                    continue

                # Out encrypts:                     29208
                m = p15.match(line)
                if m:
                    vrf_name_dict['out_encrypts'] = int(m.groupdict()['out_encrypts'])
                    continue

                # Compressed bytes:                 0
                m = p16.match(line)
                if m:
                    vrf_name_dict['compressed_bytes'] = int(m.groupdict()['compressed_bytes'])
                    continue

                # Uncompressed bytes:               0
                m = p17.match(line)
                if m:
                    vrf_name_dict['uncompressed_bytes'] = int(m.groupdict()['uncompressed_bytes'])
                    continue

                # In uncompressed bytes:            0
                m = p18.match(line)
                if m:
                    vrf_name_dict['in_uncompressed_bytes'] = int(m.groupdict()['in_uncompressed_bytes'])
                    continue

                # Out uncompressed bytes:           0
                m = p19.match(line)
                if m:
                    vrf_name_dict['out_uncompressed_bytes'] = int(m.groupdict()['out_uncompressed_bytes'])
                    continue

                # In decrypt failures:              0
                m = p20.match(line)
                if m:
                    vrf_name_dict['in_decrypt_failures'] = int(m.groupdict()['in_decrypt_failures'])
                    continue

                # Out encrypt failures:             0
                m = p21.match(line)
                if m:
                    vrf_name_dict['out_encrypt_failures'] = int(m.groupdict()['out_encrypt_failures'])
                    continue

                # No SA failures:                   0
                m = p22.match(line)
                if m:
                    vrf_name_dict['no_sa_failures'] = int(m.groupdict()['no_sa_failures'])
                    continue

                # Protocol use failures:            0
                m = p23.match(line)
                if m:
                    vrf_name_dict['protocol_use_failures'] = int(m.groupdict()['protocol_use_failures'])
                    continue

                # System capacity failures:         0
                m = p24.match(line)
                if m:
                    vrf_name_dict['system_capacity_failures'] = int(m.groupdict()['system_capacity_failures'])
                    continue

                # In authentication failures:       0
                m = p25.match(line)
                if m:
                    vrf_name_dict['in_auth_failures'] = int(m.groupdict()['in_auth_failures'])
                    continue

                # Out authentication failures:      0
                m = p26.match(line)
                if m:
                    vrf_name_dict['out_auth_failures'] = int(m.groupdict()['out_auth_failures'])
                    continue

        return flowmib_global_dict

# ====================================================
#  Schema for 'show crypto ipsec internal dual'
# ====================================================
class ShowCryptoIpsecInternalDualSchema(MetaParser):
    """Schema for show crypto ipsec internal dual"""
    schema = {
        'ipsec_internal_dual_statistics': {
            'success_stats': {
                'remove_traffic_filter': int, 
                'apply_traffic_filter': int
            },
            'error_stats': {
                'acl_retrieval': int,
                'ipv6_acl_insert': int,
                'invalid_parameters': int,
                'ipv6_ace_create': int,
                'ipv4_acl_insert': int,
                'no_ipv6_enabled': int,
                'apply_traffic_filter': int,
                'ipv4_ace_create': int
            }
        }
    }

# ====================================================
#  Parser for 'show crypto ipsec internal dual'
# ====================================================  
class ShowCryptoIpsecInternalDual(ShowCryptoIpsecInternalDualSchema):
    """Parser for 
        * show crypto ipsec internal dual
    """

    cli_command = 'show crypto ipsec internal dual'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ipsec_dualstack_stats_dict = {}

        #  ==== IPSEC Dual Stack Statistics ====
        p1 = re.compile(r'^====\s+IPSEC\s+Dual\s+Stack\s+Statistics\s+====')

        # SUCCESS Statistics
        p2 = re.compile(r'^SUCCESS\s+Statistics')

        #   Apply traffic filter success   : 134
        p3 = re.compile(r'^Apply\s+traffic\s+filter\s+success\s+:\s+(?P<apply_traffic_filter>\d+)$')

        #   Remove traffic filter success  : 134
        p4 = re.compile(r'^Remove\s+traffic\s+filter\s+success\s+:\s+(?P<remove_traffic_filter>\d+)$')

        # ERROR Statistics
        p5 = re.compile(r'^ERROR\s+Statistics')

        #   No IPv6 enabled                : 0
        p6 = re.compile(r'^No\s+IPv6\s+enabled\s+:\s+(?P<no_ipv6_enabled>\d+)$')

        #   Apply traffic filter failed    : 0
        p7 = re.compile(r'^Apply\s+traffic\s+filter\s+failed\s+:\s+(?P<apply_traffic_filter>\d+)$')

        #   IPv4 ace create failed         : 0
        p8 = re.compile(r'^IPv4\s+ace\s+create\s+failed\s+:\s+(?P<ipv4_ace_create>\d+)$')

        #   IPv4 ACL insert failed         : 0
        p9 = re.compile(r'^IPv4\s+ACL\s+insert\s+failed\s+:\s+(?P<ipv4_acl_insert>\d+)$')

        #   IPv6 ace create failed         : 0
        p10 = re.compile(r'^IPv6\s+ace\s+create\s+failed\s+:\s+(?P<ipv6_ace_create>\d+)$')

        #   IPv6 ACL insert failed         : 0
        p11 = re.compile(r'^IPv6\s+ACL\s+insert\s+failed\s+:\s+(?P<ipv6_acl_insert>\d+)$')

        #   Invalid parameters             : 0
        p12 = re.compile(r'^Invalid\s+parameters\s+:\s+(?P<invalid_parameters>\d+)$')

        #   ACL retrieval failed           : 0
        p13 = re.compile(r'^ACL\s+retrieval\s+failed\s+:\s+(?P<acl_retrieval>\d+)$')

        ipsec_dualstack_stats = False
        result_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #  ==== IPSEC Dual Stack Statistics ====
            m = p1.match(line)
            if m:
                #if 'ipsec_internal_dual_statistics' not in ipsec_dualstack_stats_dict:
                result_dict = ipsec_dualstack_stats_dict.setdefault('ipsec_internal_dual_statistics', {})
                ipsec_dualstack_stats = True
                continue

            # SUCCESS Statistics
            m = p2.match(line)
            if m and ipsec_dualstack_stats:
                stats_dict = result_dict.setdefault('success_stats', {}) 
                continue

            #   Apply traffic filter success   : 134
            m = p3.match(line)
            if m:
                stats_dict['apply_traffic_filter'] = int(m.groupdict()['apply_traffic_filter'])
                continue 

            #   Remove traffic filter success  : 134
            m = p4.match(line)
            if m:
                stats_dict['remove_traffic_filter'] = int(m.groupdict()['remove_traffic_filter'])
                continue

            # ERROR Statistics
            m = p5.match(line)
            if m and ipsec_dualstack_stats:
                stats_dict = result_dict.setdefault('error_stats', {}) 
                continue

            #   No IPv6 enabled                : 0
            m = p6.match(line)
            if m:
                stats_dict['no_ipv6_enabled'] = int(m.groupdict()['no_ipv6_enabled'])
                continue

            #   Apply traffic filter failed    : 0
            m = p7.match(line)
            if m:
                stats_dict['apply_traffic_filter'] = int(m.groupdict()['apply_traffic_filter'])
                continue

            #   IPv4 ace create failed         : 0
            m = p8.match(line)
            if m:
                stats_dict['ipv4_ace_create'] = int(m.groupdict()['ipv4_ace_create'])
                continue

            #   IPv4 ACL insert failed         : 0
            m = p9.match(line)
            if m:
                stats_dict['ipv4_acl_insert'] = int(m.groupdict()['ipv4_acl_insert'])
                continue

            #   IPv6 ace create failed         : 0
            m = p10.match(line)
            if m:
                stats_dict['ipv6_ace_create'] = int(m.groupdict()['ipv6_ace_create'])
                continue

            #   IPv6 ACL insert failed         : 0
            m = p11.match(line)
            if m:
                stats_dict['ipv6_acl_insert'] = int(m.groupdict()['ipv6_acl_insert'])
                continue

            #   Invalid parameters             : 0
            m = p12.match(line)
            if m:
                stats_dict['invalid_parameters'] = int(m.groupdict()['invalid_parameters'])
                continue

            #   ACL retrieval failed           : 0
            m = p13.match(line)
            if m:
                stats_dict['acl_retrieval'] = int(m.groupdict()['acl_retrieval'])
                ipsec_dualstack_stats = False
                continue

        return ipsec_dualstack_stats_dict


# =================================================
#  Schema for 'show crypto ipsec profile '
# =================================================
class ShowCryptoIpsecProfileSchema(MetaParser):
    """Schema for show crypto ipsec profile"""
    schema = {
        'ipsec_profile_name': {
            Any(): {
                    Optional('ikev2_profile_name'): str,
                    'security_association_lifetime': str,
                    'responder_only': str,
                    'psf': str,
                    'mixed_mode': str,
                    'tranform_sets': {
                        Any(): {
                            'transform_set_name': str,
                            'transform_set_method': str,
                        }
                    }
                }
        },
    }

# =================================================
#  Parser for 'show crypto ipsec profile'
# =================================================
class ShowCryptoIpsecProfile(ShowCryptoIpsecProfileSchema):
    """Parser for show crypto ipsec profile"""

    cli_command = ['show crypto ipsec profile']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # IPSEC profile nil_ips
        p1 = re.compile(r'^IPSEC profile\s*(?P<profile_name>\w+)$')

        # IKEv2 Profile: nil_ike_prof
        p2 = re.compile(r'^IKEv2 Profile\s*:\s*(?P<ikev2_profile_name>\w+)$')

        # Security association lifetime: 4608000 kilobytes/3600 seconds
        p3 = re.compile(r'^Security association lifetime\s*:\s*(?P<security_association_lifetime>[\d a-z\/]+)$')

        # Responder-Only (Y/N): N
        p4 = re.compile(r'^Responder-Only \(Y/N\)\s*:\s*(?P<responder_only>(Y|N))$')

        # PFS (Y/N): N
        p5 = re.compile(r'^PFS \(Y/N\):\s*(?P<psf>(Y|N))$')

        # Mixed-mode : Disabled
        p6 = re.compile(r'^Mixed-mode\s*:\s*(?P<mixed_mode>\w+)$')

        # Transform sets={
        p7 = re.compile(r'^Transform sets={$')

        # nil_tfs:  { esp-aes esp-sha-hmac  } ,
        p8 = re.compile(r'^(?P<transforset>\w+)\s*:\s*{\s*(?P<transform_set_name>[\w-]+)\s+(?P<transform_set_method>[\w-]+)\s*}\s*,$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                profile_name = groups['profile_name']
                profile_name_dict = ret_dict.setdefault('ipsec_profile_name',{}).setdefault(profile_name,{})
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ikev2_profile_name = groups['ikev2_profile_name']
                profile_name_dict['ikev2_profile_name'] = ikev2_profile_name
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                security_association_lifetime = groups['security_association_lifetime']
                profile_name_dict['security_association_lifetime'] = security_association_lifetime
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                responder_only = groups['responder_only']
                profile_name_dict['responder_only'] = responder_only
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                psf = groups['psf']
                profile_name_dict['psf'] = psf
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                mixed_mode = groups['mixed_mode']
                profile_name_dict['mixed_mode'] = mixed_mode
                continue

            m = p7.match(line)
            if m:
                transform_set_dict = profile_name_dict.setdefault('tranform_sets',{})
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                transforset = groups['transforset']
                transform_set_name = groups['transform_set_name']
                transform_set_method = groups['transform_set_method']
                transform_dict = transform_set_dict.setdefault(transforset,{})
                transform_dict['transform_set_name'] = transform_set_name
                transform_dict['transform_set_method'] = transform_set_method
                continue

        return ret_dict

# =================================================
# Schema for
#  Schema for 'show crypto ikev2 proposal'
# =================================================
class ShowCryptoIkev2ProposalSchema(MetaParser):
    """Schema for show crypto ikev2 proposal"""
    schema = {
        'proposal_name':{
            Any(): {
                    'encryption': str,
                    'integrity': str,
                    'prf': str,
                    'dh_group': list,
                }
        },
    }

# =================================================
# Parser for
#  Parser for 'show crypto ikev2 proposal'
# =================================================
class ShowCryptoIkev2Proposal(ShowCryptoIkev2ProposalSchema):
    """Parser for show crypto ikev2 proposal"""

    cli_command = ['show crypto ikev2 proposal']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # IKEv2 proposal: default
        p1 = re.compile(r'^IKEv2 proposal\s*:\s*(?P<proposal_name>.*)$')

        # Encryption : AES-CBC-256
        p2 = re.compile(r'^Encryption\s*:\s*(?P<encryption>[\w-]+)$')

        # Integrity  : SHA512 SHA384
        p3 = re.compile(r'^Integrity\s*:\s*(?P<integrity>.*)$')

        # PRF        : SHA512 SHA384
        p4 = re.compile(r'^PRF\s*:\s*(?P<prf>.*)$')

        # DH Group   : DH_GROUP_256_ECP/Group 19 DH_GROUP_2048_MODP/Group 14 DH_GROUP_521_ECP/Group 21 DH_GROUP_1536_MODP/Group 5
        p5 = re.compile(r'^DH Group\s*:\s*(?P<dh_group>.*)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # IKEv2 proposal: default
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                proposal_name = groups['proposal_name']
                proposal_name_dict = ret_dict.setdefault('proposal_name',{}).setdefault(proposal_name,{})
                continue

            # Encryption : AES-CBC-256
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                encryption = groups['encryption']
                proposal_name_dict['encryption'] = encryption
                continue

            # Integrity  : SHA512 SHA384
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                integrity = groups['integrity']
                proposal_name_dict['integrity'] = integrity
                continue

            # PRF        : SHA512 SHA384
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                prf = groups['prf']
                proposal_name_dict['prf'] = prf
                continue

            # DH Group   : DH_GROUP_256_ECP/Group 19 DH_GROUP_2048_MODP/Group 14 DH_GROUP_521_ECP/Group 21 DH_GROUP_1536_MODP/Group 5
            m = p5.match(line)
            if m:
                l2 = ''
                groups = m.groupdict()
                dh_group = groups['dh_group']
                dh_group = dh_group.split()
                dh_group_list = []
                for i in range(len(dh_group)):
                    if i==0 or i%2==0:
                        l2 = l2+dh_group[i]
                    else:
                        l2 = l2+' '+dh_group[i]
                        dh_group_list.append(l2)
                        l2 = ''
                proposal_name_dict['dh_group'] = dh_group_list
                continue

        return ret_dict

# =================================================
# Schema for
#  Schema for 'show crypto ikev2 policy'
# =================================================
class ShowCryptoIkev2PolicySchema(MetaParser):
    """Schema for show crypto ikev2 policy"""
    schema = {
        'policy_name':{
            Any(): {
                    'match_fvrf': str,
                    'match_address_local': str,
                    'proposal': str,
                }
        },
    }

# =================================================
# Parser for
#  Parser for 'show crypto ikev2 policy'
# =================================================
class ShowCryptoIkev2Policy(ShowCryptoIkev2PolicySchema):
    """Parser for show crypto ikev2 policy"""

    cli_command = ['show crypto ikev2 policy']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # IKEv2 policy : ikev2policy
        p1 = re.compile(r'^IKEv2 policy\s*:\s*(?P<policy_name>.*)$')

        # Match fvrf : global
        p2 = re.compile(r'^Match fvrf\s*:\s*(?P<match_fvrf>\w+)$')

        # Match address local : any
        p3 = re.compile(r'^Match address local\s*:\s*(?P<match_address_local>\w+)$')

        # Proposal    : ikev2proposal
        p4 = re.compile(r'^Proposal\s*:\s*(?P<proposal>.*)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # IKEv2 policy : ikev2policy
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                policy_name = groups['policy_name']
                policy_name_dict = ret_dict.setdefault('policy_name',{}).setdefault(policy_name,{})
                continue

            # Match fvrf : global
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                match_fvrf = groups['match_fvrf']
                policy_name_dict['match_fvrf'] = match_fvrf
                continue

            # Match address local : any
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                match_address_local = groups['match_address_local']
                policy_name_dict['match_address_local'] = match_address_local
                continue

            # Proposal    : ikev2proposal
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                proposal = groups['proposal']
                policy_name_dict['proposal'] = proposal
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto ikev2 sa '
# =================================================
class ShowCryptoIkev2SaSchema(MetaParser):
    """Schema for show crypto ikev2 sa"""
    schema = {
        'ipv4': {
            Any(): {
                    'tunnel_id': int,
                    'local_ip': str,
                    'local_port': int,
                    'remote_ip': str,
                    'remote_port': int,
                    'fvrf': str,
                    'ivrf': str,
                    'status': str,
                    'encryption': str,
                    'keysize': int,
                    'prf': str,
                    'hash': str,
                    'dh_group': int,
                    'auth_sign': str,
                    'auth_verify': str,
                    'life_time': int,
                    'active_time': int,
                    Optional('ce_id'): int,
                    Optional('session_id'): int,
                    Optional('local_spi'): str,
                    Optional('remote_spi'): str,
                    }
                },
        'ipv6': {}
    }

# =================================================
#  Parser for 'show crypto ikev2 sa '
# =================================================
class ShowCryptoIkev2Sa(ShowCryptoIkev2SaSchema):
    """Parser for show crypto ikev2 sa"""

    cli_command = ['show crypto ikev2 sa']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # IPv4 Crypto IKEv2  SA  
        p1 = re.compile(r'^IPv4 Crypto IKEv2 SA$')

        # IPv6 Crypto IKEv2  SA 
        p2 = re.compile(r'^IPv6 Crypto IKEv2 SA$')

        # 1         66.66.66.1/500        66.66.66.2/500        none/none            READY
        p3 = re.compile(r'^(?P<tunnel_id>\d+)\s+(?P<local_ip>[\w.]+)/(?P<local_port>\d+)\s+(?P<remote_ip>[\w.]+)/(?P<remote_port>\d+)\s+(?P<fvrf>\w+)/(?P<ivrf>\w+)\s+(?P<status>[\w]+)$')

        # Encr: AES-CBC, keysize: 128, PRF: SHA1, Hash: SHA96, DH Grp:16, Auth sign: PSK, Auth verify: PSK
        p4 = re.compile(r'^Encr:\s*(?P<encryption>[\w-]+),\s*keysize:\s*(?P<keysize>\d+),\s*PRF:\s*(?P<prf>\w+),\s*Hash:\s*(?P<hash>\w+),\s*DH Grp:(?P<dh_group>\d+),\s*Auth sign:\s*(?P<auth_sign>\w+),\s*Auth verify:\s*(?P<auth_verify>\w+)')

        # Life/Active Time: 86400/735 sec
        p5 = re.compile(r'^Life/Active Time:\s*(?P<life_time>\d+)/(?P<active_time>\d+)\s*sec$')

        # CE id: 0, Session-id: 5206
        p6 = re.compile(r'^CE id:\s*(?P<ce_id>\d+),\s*Session-id:\s*(?P<session_id>\d+)$')

        # Local spi: 1F7B76961C3A77ED Remote spi: 1298FDE074BD724C
        p7 = re.compile(r'^Local spi:\s*(?P<local_spi>[A-F\d]+)\s*Remote spi:\s*(?P<remote_spi>[A-F\d]+)$')

        for line in output.splitlines():
            line = line.strip()

            # IPv4 Crypto IKEv2  SA 
            m = p1.match(line)
            if m:
                ipv4_ikev2_dict = ret_dict.setdefault('ipv4',{})

            # IPv6 Crypto IKEv2  SA 
            m = p2.match(line)
            if m:
                ipv6_ikev2_dict = ret_dict.setdefault('ipv6',{})

            # 1         66.66.66.1/500        66.66.66.2/500        none/none            READY
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                tunnel_id = int(groups['tunnel_id'])
                local_ip = groups['local_ip']
                local_port = int(groups['local_port'])
                remote_ip = groups['remote_ip']
                remote_port = int(groups['remote_port'])
                fvrf = groups['fvrf']
                ivrf = groups['ivrf']
                status = groups['status']
                tunnel_dict = ipv4_ikev2_dict.setdefault(tunnel_id,{})

                tunnel_dict['tunnel_id'] = tunnel_id
                tunnel_dict['local_ip'] = local_ip
                tunnel_dict['local_port'] = local_port
                tunnel_dict['remote_ip'] = remote_ip
                tunnel_dict['remote_port'] = remote_port
                tunnel_dict['fvrf'] = fvrf
                tunnel_dict['ivrf'] = ivrf
                tunnel_dict['status'] = status

            # Encr: AES-CBC, keysize: 128, PRF: SHA1, Hash: SHA96, DH Grp:16, Auth sign: PSK, Auth verify: PSK
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                encryption = groups['encryption']
                keysize = int(groups['keysize'])
                prf = groups['prf']
                hash = groups['hash']
                dh_group = int(groups['dh_group'])
                auth_sign = groups['auth_sign']
                auth_verify = groups['auth_verify']

                tunnel_dict['encryption'] = encryption
                tunnel_dict['keysize'] = keysize
                tunnel_dict['prf'] = prf
                tunnel_dict['hash'] = hash
                tunnel_dict['dh_group'] = dh_group
                tunnel_dict['auth_sign'] = auth_sign
                tunnel_dict['auth_verify'] = auth_verify

            # Life/Active Time: 86400/735 sec
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                life_time = int(groups['life_time'])
                active_time = int(groups['active_time'])

                tunnel_dict['life_time'] = life_time
                tunnel_dict['active_time'] = active_time

            # CE id: 0, Session-id: 5206
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ce_id = int(groups['ce_id'])
                session_id = int(groups['session_id'])

                tunnel_dict['ce_id'] = ce_id
                tunnel_dict['session_id'] = session_id

            # Local spi: 1F7B76961C3A77ED Remote spi: 1298FDE074BD724C
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                local_spi = groups['local_spi']
                remote_spi = groups['remote_spi']

                tunnel_dict['local_spi'] = local_spi
                tunnel_dict['remote_spi'] = remote_spi

        return ret_dict

# =================================================
#  Schema for 'show crypto ikev2 stats exchange'
# =================================================
class ShowCryptoIkev2StatsExchangeSchema(MetaParser):
    """Schema for show crypto ikev2 stats exchange"""
    schema = {
        'exchanges':{
            Any(): {
                    'transmit_request': int,
                    'transmit_response': int,
                    'received_request': int,
                    'received_response': int
                }
        },
        'error_notify': {
            Any(): {
                    'transmit_request': int,
                    'transmit_response': int,
                    'received_request': int,
                    'received_response': int
            }
        },
        'other_notify': {
            Any(): {
                    'transmit_request': int,
                    'transmit_response': int,
                    'received_request': int,
                    'received_response': int
            }
        },
        'config_request': {
            Any(): {
                    'transmit': int,
                    'received': int
            }
        },
        'other_counters': {
            Any():{
                   'counter': int
            }
        }
    }

# =================================================
#  Parser for 'show crypto ikev2 stats exchange'
# =================================================
class ShowCryptoIkev2StatsExchange(ShowCryptoIkev2StatsExchangeSchema):
    """Parser for show crypto ikev2 stats exchange"""

    cli_command = ['show crypto ikev2 stats exchange']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # EXCHANGES
        p1 = re.compile(r'^EXCHANGES$')
        p1_a = re.compile(r'^ERROR NOTIFY$')
        p1_b = re.compile(r'^OTHER NOTIFY$')
        p1_c = re.compile(r'^CONFIG PAYLOAD TYPE\s+TX\s+RX$')
        p1_d = re.compile(r'^OTHER COUNTERS$')

        # IKE_SA_INIT 8618 0 0 5206
        p2 = re.compile(r'^(?P<message>\w+)\s+(?P<tx_req>\d+)\s+(?P<tx_res>\d+)\s+(?P<rx_req>\d+)\s+(?P<rx_res>\d+)$')

        # CFG_REQUEST 5206 0
        p3 = re.compile(r'^(?P<message>\w+)\s+(?P<tx>\d+)\s+(?P<rx>\d+)$')

        # NAT_INSIDE 3
        p4 = re.compile(r'^(?P<message>\w+)\s+(?P<count>\d+)$')

        ret_dict = {}

        exchnge_flag = 0
        error_notify_flag = 0
        other_notify_flag = 0

        for line in output.splitlines():
            line = line.strip()

            # EXCHANGES
            m = p1.match(line)
            if m:
                exchnge_flag = 1
                exchange_dict = ret_dict.setdefault('exchanges',{})
                continue

            # ERROR NOTIFY
            m = p1_a.match(line)
            if m:
                exchnge_flag = 0
                error_notify_flag = 1
                other_notify_flag = 0
                error_dict = ret_dict.setdefault('error_notify',{})
                continue

            # OTHER NOTIFY
            m = p1_b.match(line)
            if m:
                exchnge_flag = 0
                error_notify_flag = 0
                other_notify_flag = 1
                notify_dict = ret_dict.setdefault('other_notify',{})
                continue

            # CONFIG PAYLOAD TYPE TX RX
            m = p1_c.match(line)
            if m:
                exchnge_flag = 0
                error_notify_flag = 0
                other_notify_flag = 0
                config_dict = ret_dict.setdefault('config_request',{})
                continue

            # OTHER COUNTERS
            m = p1_d.match(line)
            if m:
                exchnge_flag = 0
                error_notify_flag = 0
                other_notify_flag = 0
                other_dict = ret_dict.setdefault('other_counters',{})
                continue

            # IKE_SA_INIT 8618 0 0 5206
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                tx_req = int(groups['tx_req'])
                tx_res = int(groups['tx_res'])
                rx_req = int(groups['rx_req'])
                rx_res = int(groups['rx_res'])
                if exchnge_flag:
                    exchange_counter_dict = exchange_dict.setdefault(groups['message'].lower(),{})
                    exchange_counter_dict['transmit_request'] = tx_req
                    exchange_counter_dict['transmit_response'] = tx_res
                    exchange_counter_dict['received_request'] = rx_req
                    exchange_counter_dict['received_response'] = rx_res
                if error_notify_flag:
                    error_counter_dict = error_dict.setdefault(groups['message'].lower(),{})
                    error_counter_dict['transmit_request'] = tx_req
                    error_counter_dict['transmit_response'] = tx_res
                    error_counter_dict['received_request'] = rx_req
                    error_counter_dict['received_response'] = rx_res
                if other_notify_flag:
                    notify_counter_dict = notify_dict.setdefault(groups['message'].lower(),{})
                    notify_counter_dict['transmit_request'] = tx_req
                    notify_counter_dict['transmit_response'] = tx_res
                    notify_counter_dict['received_request'] = rx_req
                    notify_counter_dict['received_response'] = rx_res
                continue
            # CFG_REQUEST 5206 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                tx = int(groups['tx'])
                rx = int(groups['rx'])
                config_counter_dict = config_dict.setdefault(groups['message'].lower(),{})
                config_counter_dict['transmit'] = tx
                config_counter_dict['received'] = rx
                continue
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                other_counter_dict = other_dict.setdefault(groups['message'].lower(),{})                
                counter = int(groups['count'])
                other_counter_dict['counter'] = counter
                continue

        return ret_dict


# =================================================
#  Schema for 'show crypto gdoi ks coop version '
# =================================================
class ShowCryptoGdoiKsCoopVersionSchema(MetaParser):
    """Schema for show crypto gdoi ks coop version"""
    schema = {
        "coop_ver": str,
        "ks_pol_ver": str,
        "gm_ver": str,
        "sid_ver": str
    }   

# ==============================
# Parser for
#   'show crypto gdoi ks coop version'
# ==============================

class ShowCryptoGdoiKsCoopVersion(ShowCryptoGdoiKsCoopVersionSchema):
    """
    Parser for
        * 'show crypto gdoi ks coop version'
    """

    cli_command = ['show crypto gdoi ks coop version']

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable    
        coop_dict = {}

        # Cooperative key server infra Version : 2.0.0 
        p1 = re.compile(r'Cooperative key server infra Version\s+:\s+(?P<coop_ver>\S+)$')

        # Client : KS_POLICY_CLIENT        Version : 2.0.0 
        p2 = re.compile(r'Client\s+:\s+KS_POLICY_CLIENT\s+Version\s+:\s+(?P<ks_pol_ver>\S+)$')

        # Client : GROUP_MEMBER_CLIENT     Version : 2.0.1 
        p3 = re.compile(r'Client\s+:\s+GROUP_MEMBER_CLIENT\s+Version\s+:\s+(?P<gm_ver>\S+)$')

        # Client : SID_CLIENT              Version : 1.0.1 
        p4 = re.compile(r'Client\s+:\s+SID_CLIENT\s+Version\s+:\s+(?P<sid_ver>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Cooperative key server infra Version : 2.0.0 
            m = p1.match(line)
            if m:
                coop_dict['coop_ver'] = m.groupdict()['coop_ver']
                continue

            # Client : KS_POLICY_CLIENT        Version : 2.0.0 
            m = p2.match(line)
            if m:
                coop_dict['ks_pol_ver'] = m.groupdict()['ks_pol_ver']
                continue

            # Client : GROUP_MEMBER_CLIENT     Version : 2.0.1 
            m = p3.match(line)
            if m:
                coop_dict['gm_ver'] = m.groupdict()['gm_ver']
                continue

            # Client : SID_CLIENT              Version : 1.0.1 
            m = p4.match(line)
            if m:
                coop_dict['sid_ver'] = m.groupdict()['sid_ver']
                continue

        return coop_dict  


# =================================================
#  Schema for 'show crypto gdoi'
# =================================================
class ShowCryptoGdoiSchema(MetaParser):
    """Schema for show crypto gdoi"""
    schema =  {
                "group_name":{
                    Any():{
                        "group_information":{
                            "crypto_path":str,
                            "group_identity":str,
                            "group_member":{
                                Any():{
                                    "active_tek_num":int,
                                    "allowable_rekey_cipher":str,
                                    "attempted_registration_count":int,
                                    "dp_error_monitoring":str,
                                    "fail_close_revert":str,
                                    "fvrf":str,
                                    "ipsec_init_reg_executed":int,
                                    "ipsec_init_reg_postponed":int,
                                    "ivrf":str,
                                    "last_rekey_seq_num":int,
                                    "last_rekey_server":str,
                                    "local_addr":str,
                                    "local_addr_port":str,
                                    "pfs_rekey_received":int,
                                    "re_register_time_sec":int,
                                    "registration":str,
                                    "rekey_acks_sent":int,
                                    "remote_addr":str,
                                    "remote_addr_port":int,
                                    "sa_track":str,
                                    "server_ip":str,
                                    "succeeded_registration_count":int,
                                    "uncicast_rekey_received":int,
                                    "version":str,
                                    "vrf":str
                                    }
                                },
                            "group_member_information":{
                                "acl_download_from_ks":{
                                    Any():{
                                        "acl_list":list
                                        }
                                    },
                                "acl_received_from_ks":str,
                                "rekeys_cumulative":{
                                    "after_latest_register":int,
                                    "rekey_acks_sents":int,
                                    "total_received":int
                                    }
                                },
                            "group_server_list":str,
                            "group_type":str,
                            "ipsec_sa_direction":str,
                            "kek_policy":{
                                "encrypt_algorithm":str,
                                "key_size":int,
                                "lifetime":int,
                                "rekey_transport_type":str,
                                "sig_hash_algorithm":str,
                                "sig_key_length":int
                            },
                            "key_management_path":str,
                            "kgs_policy":{
                                "reg_gm":{
                                    "local_addr":str
                                    }
                                },
                            "p2p_policy":{
                                "reg_gm":{
                                    "local_addr":str
                                    }
                                },
                            "rekeys_received":int,
                            "tek_policy":{
                                "interfaces":{
                                    Any():{
                                        "ipsec_sa":{
                                            "spi":{
                                                Any():{
                                                    "alg_key_size_bytes":int,
                                                    "sig_key_size_bytes":int,
                                                    "anti_replay_count":int,
                                                    "encaps":str,
                                                    "sa_remaining_key_lifetime":int,
                                                    "tag_method":str,
                                                    "transform":str
                                                    },
                                                Any():{
                                                    "alg_key_size_bytes":int,
                                                    "sig_key_size_bytes":int,
                                                    "anti_replay_count":int,
                                                    "encaps":str,
                                                    "sa_remaining_key_lifetime":int,
                                                    "tag_method":str,
                                                    "transform":str
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi'
# =================================================
class ShowCryptoGdoi(ShowCryptoGdoiSchema):
    """Parser for show crypto gdoi"""

    cli_command = ['show crypto gdoi']


    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Group Name               : getvpn1
        p1 = re.compile(r"^Group Name +: +(?P<group_name>\w+)$")

        # Group Identity           : 1223
        p2 = re.compile(r"^Group Identity +: +(?P<group_identity>\w+)$")

        # Group Type               : GDOI (ISAKMP)
        p3 = re.compile(r"^Group Type +: +(?P<group_type>[\w\s\S]+)$")

        # Crypto Path              : ipv4
        p4 = re.compile(r"^Crypto Path +: +(?P<crypto_path>\w+)$")

        # Key Management Path      : ipv4
        p5 = re.compile(r"^Key Management Path +: +(?P<key_management_path>\w+)$")

        # Rekeys received          : 25
        p6 = re.compile(r"^Rekeys received +: +(?P<rekeys_received>\w+)$")

        # IPSec SA Direction       : Both
        p7 = re.compile(r"^IPSec SA Direction +: +(?P<ipsec_sa_direction>\w+)$")

        # Group Server list       : 1.1.1.1
        p8 = re.compile(r"^Group Server list +: +(?P<group_server_list>[\d\.]+)$")

        # Group Member Information For Group getvpn1:
        p9 = re.compile(r"^Group Member.* +(?P<group>\w+):$")

        # ACL Received From KS     : gdoi_group_getvpn1_temp_acl
        p10 = re.compile(r"^ACL Received.* +(?P<acl_received_from_ks>\w+)$")

        # Group member             : 3.3.1.1         vrf: None
        p11 = re.compile(r"^Group member.* +: +(?P<group_member>[\d\.]+) +vrf: +(?P<vrf>[\w]+)$")

        # Local addr/port       : 3.3.1.1/848
        p12 = re.compile(r"^Local addr\/port +: +(?P<local_addr>[\d\.]+)\/(?P<local_addr_port>[\d]+)$")

        # Remote addr/port      : 1.1.1.1/848
        p13 = re.compile(r"^Remote addr\/port +: +(?P<remote_addr>[\d\.]+)\/(?P<remote_addr_port>[\d]+)$")

        # fvrf/ivrf             : None/None
        p14 = re.compile(r"^fvrf\/ivrf +: +(?P<fvrf>\w+)\/(?P<ivrf>\w+)$")

        # Version               : 1.0.26
        p15 = re.compile(r"^Version +: +(?P<version>[\d\.]+)$")

        # Registration status   : Registered
        p16 = re.compile(r"^Registration.* +(?P<registration>\w+)$")

        # Registered with       : 1.1.1.1
        p17 = re.compile(r"^Registered.* +(?P<server_ip>[\d\.]+)$")

        # Re-registers in       : 449 sec
        p18 = re.compile(r"^Re.* +(?P<re_register_time_sec>[\d]+) +sec$")

        # Succeeded registration: 1
        p19 = re.compile(r"^Succeeded.* +(?P<succeeded_registration_count>\d+)$")

        # Attempted registration: 1
        p20 = re.compile(r"^Attempted.* +(?P<attempted_registration_count>\d+)$")

        # Last rekey from       : 1.1.1.1
        p21 = re.compile(r"^Last rekey from.* +(?P<last_rekey_server>[\d\.]+)$")

        # Last rekey seq num    : 0
        p22 = re.compile(r"^Last rekey seq.* +(?P<last_rekey_seq_num>\d+)$")

        # Rekey ACKs sent       : 25
        p23 = re.compile(r"^Rekey ACKs sent.* +(?P<rekey_acks_sent>\d+)$")

        # Rekey Rcvd(hh:mm:ss)  : 00:01:30
        p24 = re.compile(r"^Rekey Rcvd.* +(?P<rekey_received_time>[\d\:]+)$")

        # PFS Rekey received    : 0
        p25 = re.compile(r"^PFS.* +(?P<pfs_rekey_received>\d+)$")

        # DP Error Monitoring   : OFF
        p26 = re.compile(r"^DP.* +(?P<dp_error_monitoring>\w+)$")

        # IPSEC init reg executed    : 0
        p27 = re.compile(r"^IPSEC init reg executed.* +(?P<ipsec_init_reg_executed>\d+)$")

        # IPSEC init reg postponed   : 0
        p28 = re.compile(r"^IPSEC init reg postponed.* +(?P<ipsec_init_reg_postponed>\d+)$")

        # Active TEK Number     : 2
        p29 = re.compile(r"^Active.* +(?P<active_tek_num>\d+)$")

        # SA Track (OID/status) : disabled
        p30 = re.compile(r"^SA.* +(?P<sa_track>[disabled|enabled]+)$")

        # Fail-Close Revert : Disabled
        p31 = re.compile(r"^Fail.* +(?P<fail_close_revert>[Disabled|Enabled]+)$")

        # allowable rekey cipher: any
        p32 = re.compile(r"^allowable.* +(?P<allowable_rekey_cipher>\w+)$")

        # allowable rekey hash  : any
        p33 = re.compile(r"^allowable rekey hash.* +(?P<allowable_rekey_hash>\w+)$")

        # allowable transformtag: any ESP
        p34 = re.compile(r"^allowable transformtag: +(?P<allowable_transformtag>[\w\s]+)$")

        # Total received        : 25
        p35 = re.compile(r"^Total received.* +(?P<total_received>\d+)$")

        # After latest register : 25
        p36 = re.compile(r"^After latest register.* +(?P<after_latest_register>\d+)$")

        # Rekey Acks sents      : 25
        p37 = re.compile(r"^Rekey Acks sents.* +(?P<rekey_acks_sents>\d+)$")

        # ACL Downloaded From KS 1.1.1.1:
        p38 = re.compile(r"^ACL Downloaded From KS.* +(?P<ks_server>[\d\.]+):$")

        # access-list   deny ip host 11.23.33.33 host 24.54.55.55
        # access-list   deny ip host 41.23.32.37 host 44.58.59.55
        # access-list   deny esp any any
        # access-list   deny udp any any port = 3784
        # access-list   deny udp any any port = 3785
        # access-list   deny udp any port = 3785 any
        # access-list   deny tcp any any port = 179
        # access-list   deny tcp any port = 179 any
        # access-list   deny tcp any any port = 22
        # access-list   deny tcp any port = 22 any
        # access-list   deny ospf any any
        # access-list   deny pim any 224.0.0.0 0.0.0.255
        # access-list   deny udp any any port = 123
        # access-list   deny udp any any port = 514
        # access-list   deny udp any port = 500 any port = 500
        # access-list   deny udp any port = 848 any
        # access-list   deny udp any any port = 848
        # access-list   deny ip any 10.90.0.0 0.0.255.255
        # access-list   deny ip 10.90.0.0 0.0.255.255 any
        # access-list   permit ip 25.25.0.0 0.0.255.255 15.15.0.0 0.0.255.255
        # access-list   permit ip 15.15.0.0 0.0.255.255 25.25.0.0 0.0.255.255
        # access-list   permit ip 16.16.0.0 0.0.255.255 26.26.0.0 0.0.255.255
        p39 = re.compile(r"^access-list.*$")

        # Rekey Transport Type     : Unicast
        p40 = re.compile(r"^Rekey Transport Type.*: (?P<rekey_transport_type>\w+)$")

        # Lifetime (secs)          : 1109
        p41 = re.compile(r"^Lifetime.*: (?P<lifetime>\d+)$")

        # Encrypt Algorithm        : AES
        p42 = re.compile(r"^Encrypt Algorithm.*: (?P<encrypt_algorithm>\w+)$")

        # Key Size                 : 256
        p43 = re.compile(r"^Key Size.*: (?P<key_size>\d+)$")

        # Sig Hash Algorithm       : HMAC_AUTH_SHA
        p44 = re.compile(r"^Sig Hash Algorithm.*: (?P<sig_hash_algorithm>\w+)$")

        # Sig Key Length (bits)    : 4400
        p45 = re.compile(r"^Sig Key Length.*: (?P<sig_key_length>\w+)$")

        # GigabitEthernet0/0/1:
        p46 = re.compile(r"^(?P<interface>[\S]+):$")

        # spi: 0x5A69F51E(1516893470)
        p47 = re.compile(r"^spi.* +(?P<spi>[\w\S]+)$")

        # transform: esp-256-aes esp-sha256-hmac
        p48 = re.compile(r"^transform.*: +(?P<transform>[\w\S\s]+)$")

        # sa timing:remaining key lifetime (sec): (510)
        p49 = re.compile(r"^sa timing.*\(+(?P<sa_remaining_key_lifetime>\d+)+\)$")

        # Anti-Replay(Counter Based) : 64
        p50 = re.compile(r"^Anti-Replay.*: +(?P<anti_replay_count>\d+)$")

        # tag method : disabled
        p51 = re.compile(r"^tag method.*: +(?P<tag_method>[disabled|enabled]+)$")

        # alg key size: 32 (bytes)
        p52 = re.compile(r"^alg key.*: +(?P<alg_key_size_bytes>[\d]+) +\(bytes\)$")

        # sig key size: 32 (bytes)
        p53 = re.compile(r"^sig key.*: +(?P<sig_key_size_bytes>[\d]+) +\(bytes\)$")

        # encaps: ENCAPS_TUNNEL
        p54 = re.compile(r"^encaps.*: +(?P<encaps>[\w\S]+)$")

        # KGS POLICY:
        p55 = re.compile(r"^KGS POLICY:$")

        # P2P POLICY:
        p56 = re.compile(r"^P2P POLICY:$")

        # REG_GM: local_addr 3.3.1.1
        p57 = re.compile(r"^REG_GM.* +(?P<local_addr>[\d\.]+)$")

        # Unicast rekey received: 25
        p58 = re.compile(r"^Unicast rekey .* +(?P<uncicast_rekey_received>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line=line.strip()
            
            # Group Name               : getvpn1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group_name', {}).setdefault(group['group_name'],{}).setdefault("group_information",{})
                continue
            
            # Group Identity           : 1223
            m = p2.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Group Type               : GDOI (ISAKMP)
            m = p3.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue

            # Crypto Path              : ipv4
            m = p4.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Key Management Path      : ipv4
            m = p5.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Rekeys received          : 25
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # IPSec SA Direction       : Both
            m = p7.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Group Server list       : 1.1.1.1
            m = p8.match(line)
            if m:
                group_dict.update(m.groupdict())
                continue
            
            # Group Member Information For Group getvpn1:
            m = p9.match(line)
            if m:
                mem_info_dict = group_dict.setdefault("group_member_information",{})
                continue
            
            # ACL Received From KS     : gdoi_group_getvpn1_temp_acl
            m = p10.match(line)
            if m:
                mem_info_dict.update(m.groupdict())
                continue
            
            # Group member             : 3.3.1.1         vrf: None
            m = p11.match(line)
            if m:
                group = m.groupdict()
                mem_dict = group_dict.setdefault("group_member",{}).setdefault(group['group_member'], {})
                mem_dict.update({'vrf' :group['vrf']})
                continue
            
            # Local addr/port       : 3.3.1.1/848
            m = p12.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Remote addr/port      : 1.1.1.1/848
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group['remote_addr_port'] = int(group['remote_addr_port'])
                mem_dict.update(group)
                continue
            
            # fvrf/ivrf             : None/None
            m = p14.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Version               : 1.0.26
            m = p15.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Registration status   : Registered
            m = p16.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Registered with       : 1.1.1.1
            m = p17.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Re-registers in       : 449 sec
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Succeeded registration: 1
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Attempted registration: 1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue

            # Last rekey from       : 1.1.1.1
            m = p21.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Last rekey seq num    : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Rekey ACKs sent       : 25
            m = p23.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Unicast rekey received: 25
            m = p58.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Rekey Rcvd(hh:mm:ss)  : 00:01:30
            m = p24.match(line)
            if m:
                mem_dict.update(group)
                continue
            
            # PFS Rekey received    : 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # DP Error Monitoring   : OFF
            m = p26.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # IPSEC init reg executed    : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # IPSEC init reg postponed   : 0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue
            
            # Active TEK Number     : 2
            m = p29.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                mem_dict.update(group)
                continue

            # SA Track (OID/status) : disabled
            m = p30.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Fail-Close Revert : Disabled
            m = p31.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # allowable rekey cipher: any
            m = p32.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
             # allowable rekey hash  : any
            m = p33.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # allowable transformtag: any ESP
            m = p34.match(line)
            if m:
                mem_dict.update(m.groupdict())
                continue
            
            # Total received        : 25
            m = p35.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict=mem_info_dict.setdefault("rekeys_cumulative", {})
                cum_dict.update(group)
                continue
            
            # After latest register : 25
            m = p36.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict.update(group)
                continue
            
            # Rekey Acks sents      : 25
            m = p37.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                cum_dict.update(group)
                continue
            
            # ACL Downloaded From KS 1.1.1.1:
            m = p38.match(line)
            if m:
                group = m.groupdict()
                acl_list = mem_info_dict.setdefault("acl_download_from_ks",{}).setdefault(group['ks_server'],{}).setdefault('acl_list',[])
                continue
            
            # access-list   permit ip 25.25.0.0 0.0.255.255 15.15.0.0 0.0.255.255
            # access-list   permit ip 15.15.0.0 0.0.255.255 25.25.0.0 0.0.255.255
            # access-list   permit ip 16.16.0.0 0.0.255.255 26.26.0.0 0.0.255.255
            m = p39.match(line)
            if m:
                acl_list.append(line)
                continue
            

            # Rekey Transport Type     : Unicast
            m = p40.match(line)
            if m:
                kek_policy_dict = group_dict.setdefault("kek_policy",{})
                kek_policy_dict.update(m.groupdict())
                continue
            

            # Lifetime (secs)          : 1109
            m = p41.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # Encrypt Algorithm        : AES
            m = p42.match(line)
            if m:
                kek_policy_dict.update(m.groupdict())
                continue
            
            # Key Size                 : 256
            m = p43.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # Sig Hash Algorithm       : HMAC_AUTH_SHA
            m = p44.match(line)
            if m:
                kek_policy_dict.update(m.groupdict())
                continue
            
            # Sig Key Length (bits)    : 4400
            m = p45.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_policy_dict.update(group)
                continue
            
            # GigabitEthernet0/0/1:
            m = p46.match(line)
            if m:
                group = m.groupdict()
                tek_policy_dict = group_dict.setdefault("tek_policy",{}).setdefault('interfaces',{}).setdefault(group['interface'],{})
                continue
            
            # spi: 0x5A69F51E(1516893470)
            m = p47.match(line)
            if m:
                group = m.groupdict()
                spi_dict = tek_policy_dict.setdefault('ipsec_sa', {}).setdefault('spi', {}).setdefault(group['spi'], {})
                continue
            

            # transform: esp-256-aes esp-sha256-hmac
            m = p48.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # sa timing:remaining key lifetime (sec): (510)
            m = p49.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # Anti-Replay(Counter Based) : 64
            m = p50.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            

            # tag method : disabled
            m = p51.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # alg key size: 32 (bytes)
            m = p52.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # sig key size: 32 (bytes)
            m = p53.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                spi_dict.update(group)
                continue
            
            # encaps: ENCAPS_TUNNEL
            m = p54.match(line)
            if m:
                spi_dict.update(m.groupdict())
                continue
            
            # KGS POLICY:
            m = p55.match(line)
            if m:
                kgs_policy_dict = group_dict.setdefault('kgs_policy', {}).setdefault('reg_gm', {})
                continue
            
            # P2P POLICY:
            m = p56.match(line)
            if m:
                p2p_policy_dict = group_dict.setdefault('p2p_policy', {}).setdefault('reg_gm', {})
                continue
            
            # REG_GM: local_addr 3.3.1.1
            m = p57.match(line)
            if m:
                if 'p2p_policy' not in group_dict:kgs_policy_dict.update(m.groupdict())
                else:p2p_policy_dict.update(m.groupdict())
                continue
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi detail'
# =================================================
class ShowCryptoGdoiDetail(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gdoi detail'
    '''
    cli_command = "show crypto gdoi detail"

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Parser for 'show crypto gdoi group {group_name}'
# =================================================
class ShowCryptoGdoiGroup(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gdoi group {group_name}'
    '''
    cli_command = "show crypto gdoi group {group_name}"

    def cli(self, group_name = '', output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Parser for 'show crypto gkm'
# =================================================
class ShowCryptoGkm(ShowCryptoGdoi):
    '''Parser for:
        * 'show crypto gkm'
    '''
    cli_command = "show crypto gkm"

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output = output)

# =================================================
#  Schema for 'show crypto gdoi ks policy'
# =================================================

class ShowCryptoGdoiKsPolicySchema(MetaParser):
    """Schema for show crypto gdoi ks policy"""
    schema =  {
                "key_server_policy":{
                    "group":{
                        Any():{
                            "handle":str,
                            "server":{
                                Any():{
                                    "handle":str,
                                    "kek_policy":{
                                        "spi":{
                                            Any():{
                                                "acknowledgement":str,
                                                "crypto_iv_length":int,
                                                "encrypt_alg":str,
                                                "key_size":int,
                                                "management_alg":str,
                                                "orig_life_secs":int,
                                                "remaining_life_secs":int,
                                                "sig_hash_algorithm":str,
                                                "sig_key_length":int,
                                                "sig_key_name":str,
                                                "sig_size":int,
                                                "time_to_rekey_sec":str
                                                }
                                            },
                                        "transport_type":str
                                        },
                                    "seq_num":int,
                                    "tek_policy":{
                                        "encaps":str,
                                        "spi":{
                                            Any():{
                                                "access_list":str,
                                                "alg_key_size":int,
                                                "antireplay_window_size":int,
                                                "elapsed_time_sec":int,
                                                "orig_life_secs":int,
                                                "override_life_sec":int,
                                                "remaining_life_secs":int,
                                                "sig_key_size":int,
                                                "tek_life_sec":int,
                                                Optional("time_to_rekey_sec"):str,
                                                "transform":str
                                                },
                                            }
                                        },
                                    "teks_num":int
                                    }
                                }
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi ks policy'
# =================================================
class ShowCryptoGdoiKsPolicy(ShowCryptoGdoiKsPolicySchema):
    """Parser for show crypto ikev2 policy"""

    cli_command = ['show crypto gdoi ks policy']

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # For group getvpn1 (handle: 0x40000002) server 1.1.1.1 (handle: 0x40000002):
        p1 = re.compile(r"^For group +(?P<group_name>\w+) +\(handle: +(?P<group_handle>[\w]+)\) +server +(?P<server_ip>[\d\.]+) +\(handle: +(?P<server_handle>\w+)\):$")

        # # of teks : 2  Seq num : 0
        p2 = re.compile(r"^# of teks : +(?P<teks_num>\d+) + Seq num : +(?P<seq_num>\d+)$")

        # KEK POLICY (transport type : Unicast)
        p3 = re.compile(r"^KEK POLICY +\(transport type : +(?P<transport_type>\w+)\)$")

        # spi : 0xEEB0E9A2BBD4C71AF1034F6B24EB8022
        p4 = re.compile(r"^spi : +(?P<spi>\w+)$")

        # management alg     : disabled      encrypt alg           : AES
        p5 = re.compile(r"^management alg.*: +(?P<management_alg>[\disbaled|enabled]+) +encrypt alg.*: +(?P<encrypt_alg>\w+)$")

        # crypto iv length   : 16            key size              : 32
        p6 = re.compile(r"^crypto iv length.*: +(?P<crypto_iv_length>\d+) +key size.*: +(?P<key_size>\d+)$")

        # orig life(sec)     : 1200          remaining life(sec)   : 787
        p7 = re.compile(r"^orig life.*: +(?P<orig_life_secs>\d+) +remaining.*: +(?P<remaining_life_secs>\d+)$")

        # time to rekey (sec): 552
        p8 = re.compile(r"^time to rekey.* +(?P<time_to_rekey_sec>[\d\S]+)$")

        # sig hash algorithm : enabled       sig key length        : 550
        p9 = re.compile(r"^sig hash algorithm.* +(?P<sig_hash_algorithm>[enabled|disabled]+) +sig key length.* +(?P<sig_key_length>\d+)$")

        # sig size           : 512
        p10 = re.compile(r"^sig size.*: +(?P<sig_size>\d+)$")

        # sig key name       : REKEYRSA
        p11 = re.compile(r"^sig key name.*: +(?P<sig_key_name>\w+)$")

        # acknowledgement    : Cisco
        p12 = re.compile(r"^acknowledgement.*: +(?P<acknowledgement>\w+)$")

        # TEK POLICY (encaps : ENCAPS_TUNNEL)
        p13 = re.compile(r"^TEK POLICY +\(encaps : +(?P<encaps>\w+)\)$")

        # spi                : 0xEE021924
        p14 = re.compile(r"^spi.*: +(?P<spi>\w+)$")

        # access-list        : acl1
        p15 = re.compile(r"^access-list.*: +(?P<access_list>\w+)$")

        # transform          : esp-256-aes esp-sha256-hmac
        p16 = re.compile(r"^transform.*: +(?P<transform>[\w\s\S]+)$")

        #  alg key size       : 32            sig key size          : 32
        p17 = re.compile(r"^alg key size.*: +(?P<alg_key_size>\d+) +sig key size.* +(?P<sig_key_size>\d+)$")

        # tek life(sec)      : 600           elapsed time(sec)     : 412
        p18 = re.compile(r"^tek life.*: +(?P<tek_life_sec>\d+) +elapsed time.* +(?P<elapsed_time_sec>\d+)$")

        # override life(sec) : 0             antireplay window size: 64
        p19 = re.compile(r"^override life.*: +(?P<override_life_sec>\d+) +antireplay window size.*: +(?P<antireplay_window_size>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # For group getvpn1 (handle: 0x40000002) server 1.1.1.1 (handle: 0x40000002):
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('key_server_policy', {}).setdefault('group', {}).setdefault(group['group_name'], {})
                group_dict.update({'handle':group['group_handle']})
                server_dict = group_dict.setdefault('server',{}).setdefault(group['server_ip'], {})
                server_dict.update({'handle':group['server_handle']})
                continue
            
            # # of teks : 2  Seq num : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                server_dict.update(group)
                continue

            # KEK POLICY (transport type : Unicast)
            m = p3.match(line)
            if m:
                kek_policy_dict = server_dict.setdefault('kek_policy', {})
                kek_policy_dict.update(m.groupdict())
                continue

            # spi : 0xEEB0E9A2BBD4C71AF1034F6B24EB8022
            m = p4.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict = kek_policy_dict.setdefault('spi',{}).setdefault(group['spi'], {})
                continue

            # management alg     : disabled      encrypt alg           : AES
            m = p5.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # crypto iv length   : 16            key size              : 32
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_spi_dict.update(group)
                continue
            
            # sig hash algorithm : enabled       sig key length        : 550
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group['sig_key_length'] = int(group['sig_key_length']) 
                kek_spi_dict.update(group)
                continue
            
            # sig size           : 512
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                kek_spi_dict.update(group)
                continue
            
            # sig key name       : REKEYRSA
            m = p11.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # acknowledgement    : Cisco
            m = p12.match(line)
            if m:
                group = m.groupdict()
                kek_spi_dict.update(group)
                continue
            
            # TEK POLICY (encaps : ENCAPS_TUNNEL)
            m = p13.match(line)
            if m:
                tek_policy_dict = server_dict.setdefault('tek_policy', {})
                tek_policy_dict.update(m.groupdict())
                continue
            
            # spi                : 0xEE021924
            m = p14.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict = tek_policy_dict.setdefault('spi',{}).setdefault(group['spi'], {})
                continue
            
            # access-list        : acl1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict.update(group)
                continue
            
            # transform          : esp-256-aes esp-sha256-hmac
            m = p16.match(line)
            if m:
                group = m.groupdict()
                tek_spi_dict.update(group)
                continue
            
            # alg key size       : 32            sig key size          : 32
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # tek life(sec)      : 600           elapsed time(sec)     : 412
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # override life(sec) : 0             antireplay window size: 64
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                tek_spi_dict.update(group)
                continue
            
            # orig life(sec)     : 1200          remaining life(sec)   : 787
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                if 'tek_policy' not in server_dict: kek_spi_dict.update(group)
                else: tek_spi_dict.update(group)
                continue
            
            # time to rekey (sec): 552
            # time to rekey (sec): 62
            # time to rekey (sec): n/a
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if 'tek_policy' not in server_dict: kek_spi_dict.update(group)
                else: tek_spi_dict.update(group)
                continue
        return master_dict

# =================================================
#  Schema for 'show crypto gdoi gm dataplan counter'
# =================================================
class ShowCryptoGdoiGmDataplanCounterSchema(MetaParser):
    """Schema for show crypto gdoi gm dataplan counter"""
    schema =  {
                "data_plane_statistics":{
                    "group":{
                        Any():{
                            "pkts_decrypt":int,
                            "pkts_encrypt":int,
                            "pkts_invalid_prot":int,
                            "pkts_no_sa":int,
                            "pkts_not_tagged":int,
                            "pkts_not_untagged":int,
                            "pkts_tagged":int,
                            "pkts_untagged":int,
                            "pkts_verify_fail":int
                            }
                        }
                    }
                }

# =================================================
#  Parser for 'show crypto gdoi gm dataplan counter'
# =================================================
class ShowCryptoGdoiGmDataplanCounter(ShowCryptoGdoiGmDataplanCounterSchema):
    """Parser for show crypto gdoi gm dataplan counter"""

    cli_command = ['show crypto gdoi gm dataplan counter']

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Data-plane statistics for group getvpn1:
        p1 = re.compile(r"^Data-plane statistics for group +(?P<group_name>[\w\S]+):$")

        # #pkts encrypt            : 21592009    #pkts decrypt            : 0
        p2 = re.compile(r"^#pkts encrypt.*: +(?P<pkts_encrypt>\d+) +#pkts decrypt.*: +(?P<pkts_decrypt>\d+)$")

        # #pkts tagged (send)      : 0        #pkts untagged (rcv)     : 0
        p3 = re.compile(r"^#pkts tagged.*: +(?P<pkts_tagged>\d+) +#pkts untagged.*: +(?P<pkts_untagged>\d+)$")

        # #pkts no sa (send)       : 0        #pkts invalid sa (rcv)   : 0
        p4 = re.compile(r"^#pkts no sa.*: +(?P<pkts_no_sa>\d+) +#pkts invalid sa.*: +(?P<pkts_untagged>\d+)$")

        # #pkts encaps fail (send) : 0        #pkts decap fail (rcv)   : 0
        p5 = re.compile(r"^#pkts encaps fail.*: +(?P<pkts_tagged>\d+) +#pkts decap fail.*: +(?P<pkts_untagged>\d+)$")

        # #pkts invalid prot (rcv) : 0        #pkts verify fail (rcv)  : 0
        p6 = re.compile(r"^#pkts invalid prot.*: +(?P<pkts_invalid_prot>\d+) +#pkts verify fail.*: +(?P<pkts_verify_fail>\d+)$")

        # #pkts not tagged (send)  : 0        #pkts not untagged (rcv) : 0
        p7 = re.compile(r"^#pkts not tagged.*: +(?P<pkts_not_tagged>\d+) +#pkts not untagged.*: +(?P<pkts_not_untagged>\d+)$")

        # #pkts internal err (send): 0        #pkts internal err (rcv) : 0
        p8 = re.compile(r"^#pkts internal err.*: +(?P<pkts_encrypt>\d+) +#pkts internal err.*: +(?P<pkts_decrypt>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Data-plane statistics for group getvpn1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('data_plane_statistics', {}).setdefault('group', {}).setdefault(group['group_name'], {})
                continue
            
            # #pkts encrypt            : 21592009    #pkts decrypt            : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # #pkts tagged (send)      : 0        #pkts untagged (rcv)     : 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts no sa (send)       : 0        #pkts invalid sa (rcv)   : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue
            
            # #pkts encaps fail (send) : 0        #pkts decap fail (rcv)   : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts invalid prot (rcv) : 0        #pkts verify fail (rcv)  : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts not tagged (send)  : 0        #pkts not untagged (rcv) : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

            # #pkts internal err (send): 0        #pkts internal err (rcv) : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_dict.update(group)
                continue

        return master_dict

# =================================================
# Schema for
#  Schema for 'show crypto eli all'
# =================================================
class ShowCryptoEliAllSchema(MetaParser):
    """Schema for show crypto eli all"""
    schema = {
            Optional("hardware_encryption"):str,
            Optional("crypto_engines_num"):int,
            "crypto_engine":{
                Any():{
                    "state":str,
                    Optional("capability"):str,
                    Optional("ikev2_session"):{
                        Optional("active"):int,
                        Optional("created"):int,
                        Optional("failed"):int,
                        Optional("max"):int
                    },
                    Optional("ike_session"):{
                        Optional("active"):int,
                        Optional("created"):int,
                        Optional("failed"):int,
                        Optional("max"):int
                    },
                    Optional("dh"):{
                        Optional("active"):int,
                        Optional("created"):int,
                        Optional("failed"):int,
                        Optional("max"):int
                    },
                    Optional("ipsec_session"):{
                        Optional("active"):int,
                        Optional("created"):int,
                        Optional("failed"):int,
                        Optional("max"):int
                    },
                    Optional("ssl_support"):str,
                    Optional("ssl_versions"):str,
                    Optional("max_ssl_connec"):int,
                    Optional("ssl_namespace"):int,
                    Optional("sslv3"):list,
                    Optional("tlsv1"):list,
                    Optional("dtlsv1"):list,
                },
            },
            Optional("number_dh_pregenerated"):int,
            Optional("dh_lifetime_seconds"):int,
            Optional("dh_calculations"):{
                Optional("p1"):int,
                Optional("ss"):int
            },
            Optional("crypto_eng"):{
                Optional("crypto_engine"):str,
                Optional("crypto_engine_num"):int,
                Optional("dh_in_free"):int,
                Optional("dh_in_freeing"):int,
                Optional("dh_in_use"):int,
            },
        }

# =================================================
# Parser for
#  Parser for 'show crypto eli all'
# =================================================
class ShowCryptoEliAll(ShowCryptoEliAllSchema):
    """Parser for show crypto eli all"""

    cli_command = ['show crypto eli all']

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Hardware Encryption : ACTIVE
        p1 = re.compile(r"^Hardware Encryption.* +(?P<hardware_encryption>\w+)$")

        # Number of crypto engines = 3
        p2 = re.compile(r"^Number of crypto engines = +(?P<crypto_engines_num>\d+)$")

        # CryptoEngine IOSXE-ESP(14) details: state = Active
        # CryptoEngine act2 details: state = Active
        # CryptoEngine Software Crypto Engine details: state = Active
        p3 = re.compile(r"^CryptoEngine +(?P<crypto_engine>[\w\S\s]+) details:.*= +(?P<state>\w+)$")

        # Capability    : DES, 3DES, AES, GCM, GMAC, RSA, IPv6, GDOI, FAILCLOSE, ESN
        p4 = re.compile(r"^Capability.*: +(?P<capability>[\w\S\s]+)$")

        # IPSec-Session :  6004 active, 40958 max, 0 failed, 414018 created
        p5 = re.compile(r"^IPSec-Session.*: +(?P<active>\d+) +active, +(?P<max>\d+) +max, +(?P<failed>\d+) +failed, +(?P<created>\d+) +created$")

        # SSL support   : Yes
        p6 = re.compile(r"^SSL support.*: (?P<ssl_support>[Yes|No]+)$")

        # SSL versions  : TLSv1.0
        p7 = re.compile(r"^SSL versions.*: (?P<ssl_versions>[\w\S]+)$")

        # Max SSL connec: 10000
        p8 = re.compile(r"^Max SSL connec.*: (?P<max_ssl_connec>\d+)$")

        # SSLv3.0 suites:
        p9 = re.compile(r"^SSLv3.*$")

        # TLSv1.0 suites:
        p10 = re.compile(r"^TLSv1.*$")

        # DTLSv1.0 suite:
        p11 = re.compile(r"^DTLSv1.*$")

        # TLS_RSA_WITH_3DES_EDE_CBC_SHA
        p12 = re.compile(r"^(?P<suites>\w+)$")

        # IKE-Session   :     0 active, 41058 max, 0 failed, 319288 created
        p13 = re.compile(r"^IKE-Session.*: +(?P<active>\d+) +active, +(?P<max>\d+) +max, +(?P<failed>\d+) +failed, +(?P<created>\d+) +created$")

        # IKEv2-Session :  3002 active, 41058 max, 0 failed, 319288 created
        p14 = re.compile(r"^IKEv2-Session.*: +(?P<active>\d+) +active, +(?P<max>\d+) +max, +(?P<failed>\d+) +failed, +(?P<created>\d+) +created$")

        # DH            :     0 active(0/0), 41008 max, 0 failed, 320010 created
        p15 = re.compile(r"^DH.*: +(?P<active>\d+) +active\S+, +(?P<max>\d+) +max, +(?P<failed>\d+) +failed, +(?P<created>\d+) +created$")

        # SSL namespace : 1
        p16 = re.compile(r"^SSL namespace.*: +(?P<ssl_namespace>\d+)$")

        # Number of DH's pregenerated = 4
        p17 = re.compile(r"^Number of DH's pregenerated = +(?P<number_dh_pregenerated>[0-9]+)$")

        # DH lifetime = 86400 seconds
        p18 = re.compile(r"^DH lifetime.*= +(?P<dh_lifetime_seconds>\d+) +seconds$")

        # DH calculations: P1 722, SS 319288
        p19 = re.compile(r"^DH calculations.*: +P1 +(?P<p1>\d+), +SS +(?P<ss>\d+)$")

        # crypto engine 1:Software Crypto Engine
        p20 = re.compile(r"^crypto engine +(?P<crypto_engine_num>\d+):+(?P<crypto_engine>[\w\s]+)$")

        # DH in use/freeing/free - 0/0/41008
        p21 = re.compile(r"^DH in use\/freeing\/free - +(?P<dh_in_use>\d+)\/(?P<dh_in_freeing>\d+)\/(?P<dh_in_free>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Hardware Encryption : ACTIVE
            m = p1.match(line)
            if m:
                master_dict.update(m.groupdict())
                continue
            
            # Number of crypto engines = 3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                master_dict.update(group)
                continue
            
            # CryptoEngine IOSXE-ESP(14) details: state = Active
            # CryptoEngine act2 details: state = Active
            # CryptoEngine Software Crypto Engine details: state = Active
            m = p3.match(line)
            if m:
                group = m.groupdict()
                crypto_dict = master_dict.setdefault('crypto_engine', {}).setdefault(group['crypto_engine'], {})
                crypto_dict.update({'state': group['state']})
                continue
            
            # Capability    : DES, 3DES, AES, GCM, GMAC, RSA, IPv6, GDOI, FAILCLOSE, ESN
            m = p4.match(line)
            if m:
                crypto_dict.update(m.groupdict())
                continue
            
            # IPSec-Session :  6004 active, 40958 max, 0 failed, 414018 created
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ipsec_session = crypto_dict.setdefault("ipsec_session", {})
                ipsec_session.update(group)
                continue

            # SSL support   : Yes
            m = p6.match(line)
            if m:
                crypto_dict.update(m.groupdict())
                continue
            
            # SSL versions  : TLSv1.0
            m = p7.match(line)
            if m:
                crypto_dict.update(m.groupdict())
                continue
            
            # Max SSL connec: 10000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                crypto_dict.update(group)
                continue

            # SSLv3.0 suites:
            m = p9.match(line)
            if m:
                suites = crypto_dict.setdefault("sslv3", [])
                continue
            
            # TLSv1.0 suites:
            m = p10.match(line)
            if m:
                suites = crypto_dict.setdefault("tlsv1", [])
                continue

            # DTLSv1.0 suite:
            m = p11.match(line)
            if m:
                suites = crypto_dict.setdefault("dtlsv1", [])
                continue

            # TLS_RSA_WITH_3DES_EDE_CBC_SHA
            m = p12.match(line)
            if m:
                group = m.groupdict()
                suites.append(group['suites'])
                continue
            
            # IKE-Session   :     0 active, 41058 max, 0 failed, 319288 created
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ike_session = crypto_dict.setdefault("ike_session", {})
                ike_session.update(group)
                continue
            
            # IKEv2-Session :  3002 active, 41058 max, 0 failed, 319288 created
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                ikev2_session = crypto_dict.setdefault("ikev2_session", {})
                ikev2_session.update(group)
                continue
            
            # DH            :     0 active(0/0), 41008 max, 0 failed, 320010 created
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                dh = crypto_dict.setdefault("dh", {})
                dh.update(group)
                continue
            
            # SSL namespace : 1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                crypto_dict.update(group)
                continue
            
            # Number of DH's pregenerated = 4
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                master_dict.update(group)
                continue

            # DH lifetime = 86400 seconds
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                master_dict.update(group)
                continue
            
            # DH calculations: P1 722, SS 319288
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                dh_calculation = master_dict.setdefault("dh_calculations", {})
                dh_calculation.update(group)
                continue

            # crypto engine 1:Software Crypto Engine
            m = p20.match(line)
            if m:
                group = m.groupdict()
                crypto_eng = master_dict.setdefault("crypto_eng", {})
                group['crypto_engine_num'] = int(group['crypto_engine_num'])
                crypto_eng.update(group)
                continue

            # DH in use/freeing/free - 0/0/41008
            m = p21.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                crypto_eng.update(group)
                continue

        return master_dict

# =================================================
#  Schema for 'show crypto mib ike flowmib tunnel'
# =================================================
class ShowCryptoMibIkeFlowmibTunnelSchema(MetaParser):
    """Schema for show crypto mib ike flowmib tunnel"""
    schema = {
        Any(): {
            Any(): {
                Any(): {
                    'index': str,
                    'local_type': str,
                    'local_address': str,
                    'remote_type': str,
                    'remote_address': str,
                    'negotiation_mode': str,
                    'diffie_hellman_grp': int,
                    'encryption_algorithm': str,
                    'hash_algorithm': str,
                    'auth_method': str,
                    'lifetime': int,
                    'active_time': str,
                    'policy_priority': int,
                    'keepalive_enabled': str,
                    'incoming': 
                    {
                        'in_octets': int,
                        'in_packets': int,
                        'in_drops': int,
                        'in_notifys': int,
                        'in_p2_exchanges': int,
                        'in_p2_exchg_invalids': int,
                        'in_p2_exchg_rejected': int,
                        'in_p2_sa_delete_requests': int
                        },
                    'outgoing': 
                    {
                        'out_octets': int,
                        'out_packets': int,
                        'out_drops': int,
                        'out_notifys': int,
                        'out_p2_exchgs': int,
                        'out_p2_exchgs_invalids': int,
                        'out_p2_exchgs_rejects': int,
                        'out_p2_sa_delete_requests': int
                        },
                    },
                },
            'total_vrf': int,
        }
    }

# ====================================================
#  Parser for 'show crypto mib ike flowmib tunnel'
# ====================================================
class ShowCryptoMibIkeFlowmibTunnel(ShowCryptoMibIkeFlowmibTunnelSchema):
    """Parser for
        * show crypto mib ike flowmib tunnel
    """

    cli_command = 'show crypto mib ike flowmib tunnel'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        flowmib_tunnel_dict = {}

        # vrf Global
        p1 = re.compile(r'^vrf\s+(?P<vrf_name>[\S\s]+)$')
        
        # Index:                       32248
        p2 = re.compile(r'^Index:\s+(?P<index>\d+)$')

        # Local type:                  ID_IPV4_ADDR 
        p3 = re.compile(r'^Local\s+type:\s+(?P<local_type>[\S\s]+)$')

        # Local address:               50.50.50.2
        p4 = re.compile(r'^Local\s+address:\s+(?P<local_address>[\S\s]+)$')

        # Remote type:                 ID_IPV4_ADDR
        p5 = re.compile(r'^Remote\s+type:\s+(?P<remote_type>[\S\s]+)$')

        # Remote address:              100.0.10.2
        p6 = re.compile(r'^Remote\s+address:\s+(?P<remote_address>[\S\s]+)$')

        # Negotiation mode:            IKEv2 
        p7 = re.compile(r'^Negotiation\s+mode:\s+(?P<negotiation_mode>[\S\s]+)$')

        # Diffie Hellman Grp:          16 
        p8 = re.compile(r'^Diffie\s+Hellman\s+Grp:\s+(?P<diffie_hellman_grp>\d+)$')
 
        # Encryption algo:             aes  
        p9 = re.compile(r'^Encryption\s+algo:\s+(?P<encryption_algorithm>[\S\s]+)$')

        # Hash algo:                   sha512
        p10 = re.compile(r'^Hash\s+algo:\s+(?P<hash_algorithm>[\S\s]+)$')

        # Auth method:                 localPskRemotePsk
        p11 = re.compile(r'^Auth\s+method:\s+(?P<auth_method>[\S\s]+)$')

        # Lifetime:                    86400
        p12 = re.compile(r'^Lifetime:\s+(?P<lifetime>\d+)$')

        # Active time:                 00:02:12
        p13 = re.compile(r'^Active\s+time:\s+(?P<active_time>[\S\s]+)$')

        # Policy priority:             0 
        p14 = re.compile(r'^Policy\s+priority:\s+(?P<policy_priority>\d+)$')

        # Keepalive enabled:           No   
        p15 = re.compile(r'^Keepalive\s+enabled:\s+(?P<keepalive_enabled>[\S\s]+)$')

        # In octets:                   5440    
        p16 = re.compile(r'^In\s+octets:\s+(?P<in_octets>\d+)$')

        # In packets:                  34
        p17 = re.compile(r'^In\s+packets:\s+(?P<in_packets>\d+)$')

        # In drops:                    0 
        p18 = re.compile(r'^In\s+drops:\s+(?P<in_drops>\d+)$')

        # In notifys:                  17 
        p19 = re.compile(r'^In\s+notifys:\s+(?P<in_notifys>\d+)$')

        # In P2 exchanges:             34 
        p20 = re.compile(r'^In\s+P2\s+exchanges:\s+(?P<in_P2_exchanges>\d+)$')

        # In P2 exchg invalids:        0
        p21 = re.compile(r'^In\s+P2\s+exchg\s+invalids:\s+(?P<in_P2_exchg_invalids>\d+)$')

        # In P2 exchg rejected:        0
        p22 = re.compile(r'^In\s+P2\s+exchg\s+rejected:\s+(?P<in_P2_exchg_rejected>\d+)$')

        # In P2 SA delete reqs:        0 
        p23 = re.compile(r'^In\s+P2\s+SA\s+delete\s+reqs:\s+(?P<in_P2_SA_delete_reqs>\d+)$')

        # Out octets:                  5712 
        p24 = re.compile(r'^Out\s+octets:\s+(?P<out_octets>\d+)$')

        # Out packets:                 34  
        p25 = re.compile(r'^Out\s+packets:\s+(?P<out_packets>\d+)$')

        # Out drops:                   0 
        p26 = re.compile(r'^Out\s+drops:\s+(?P<out_drops>\d+)$')

        # Out notifys:                 34  
        p27 = re.compile(r'^Out\s+notifys:\s+(?P<out_notifys>\d+)$')
 
        # Out P2 exchgs:               34 
        p28 = re.compile(r'^Out\s+P2\s+exchgs:\s+(?P<out_P2_exchgs>\d+)$')
 
        # Out P2 exchg invalids:       0
        p29 = re.compile(r'^Out\s+P2\s+exchg\s+invalids:\s+(?P<out_P2_exchgs_invalids>\d+)$')
 
        # Out P2 exchg rejects:        0
        p30 = re.compile(r'^Out\s+P2\s+exchg\s+rejects:\s+(?P<out_P2_exchgs_rejects>\d+)$')
 
        # Out P2 Sa delete requests:   17 
        p31 = re.compile(r'^Out\s+P2\s+Sa\s+delete\s+requests:\s+(?P<out_P2_Sa_delete_requests>\d+)$')


        vrf_count = 0
        result_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # vrf Global
            m = p1.match(line)
            if m:
                vrf_count += 1
                if 'total_vrf' not in flowmib_tunnel_dict:
                    result_dict = flowmib_tunnel_dict.setdefault('ike_flowmib_tunnel', {})
                result_dict['total_vrf'] = vrf_count
                vrf_name = m.groupdict()['vrf_name']
                vrf_name_dict = result_dict.setdefault(vrf_name, {})
                index_count = 0
                continue

            # Index:                       32248
            m = p2.match(line)
            if m:
                index_count += 1
                index_count_dict = vrf_name_dict.setdefault(str(index_count), {})
                index_count_dict['index'] = m.groupdict()['index']
                continue

            # Local type:                  ID_IPV4_ADDR
            m = p3.match(line)
            if m:
                index_count_dict['local_type'] = m.groupdict()['local_type']
                continue

            # Local address:               50.50.50.2
            m = p4.match(line)
            if m:
                index_count_dict['local_address'] = m.groupdict()['local_address']
                continue
            
            # Remote type:                 ID_IPV4_ADDR
            m = p5.match(line)
            if m:
                index_count_dict['remote_type'] = m.groupdict()['remote_type']
                continue

            # Remote address:              100.0.10.2
            m = p6.match(line)
            if m:
                index_count_dict['remote_address'] = m.groupdict()['remote_address']
                continue

            # Negotiation mode:            IKEv2 
            m = p7.match(line)
            if m:
                index_count_dict['negotiation_mode'] = m.groupdict()['negotiation_mode']
                continue

            # Diffie Hellman Grp:          16
            m = p8.match(line)
            if m:
                index_count_dict['diffie_hellman_grp'] = int(m.groupdict()['diffie_hellman_grp'])
                continue

            # Encryption algo:             aes
            m = p9.match(line)
            if m:
                index_count_dict['encryption_algorithm'] = m.groupdict()['encryption_algorithm']
                continue

            # Hash algo:                   sha512
            m = p10.match(line)
            if m:
                index_count_dict['hash_algorithm'] = m.groupdict()['hash_algorithm']
                continue

            # Auth method:                 localPskRemotePsk
            m = p11.match(line)
            if m:
                index_count_dict['auth_method'] = m.groupdict()['auth_method']
                continue

            # Lifetime:                    86400
            m = p12.match(line)
            if m:
                index_count_dict['lifetime'] = int(m.groupdict()['lifetime'])
                continue

            # Active time:                 00:02:12
            m = p13.match(line)
            if m:
                index_count_dict['active_time'] = m.groupdict()['active_time']
                continue

            # Policy priority:             0 
            m = p14.match(line)
            if m:
                index_count_dict['policy_priority'] = int(m.groupdict()['policy_priority'])
                continue

            # Keepalive enabled:           No
            m = p15.match(line)
            if m:
                index_count_dict['keepalive_enabled'] = m.groupdict()['keepalive_enabled']
                continue

            # In octets:                   5440   
            m = p16.match(line)
            if m:
                incoming_dict = index_count_dict.setdefault('incoming', {})
                incoming_dict['in_octets'] = int(m.groupdict()['in_octets'])
                continue

            # In packets:                  34
            m = p17.match(line)
            if m:
                incoming_dict['in_packets'] = int(m.groupdict()['in_packets'])
                continue

            # In drops:                    0
            m = p18.match(line)
            if m:
                incoming_dict['in_drops'] = int(m.groupdict()['in_drops'])
                continue

            # In notifys:                  17
            m = p19.match(line)
            if m:
                incoming_dict['in_notifys'] = int(m.groupdict()['in_notifys'])
                continue

            # In P2 exchanges:             34 
            m = p20.match(line)
            if m:
                incoming_dict['in_p2_exchanges'] = int(m.groupdict()['in_P2_exchanges'])
                continue

            # In P2 exchg invalids:        0
            m = p21.match(line)
            if m:
                incoming_dict['in_p2_exchg_invalids'] = int(m.groupdict()['in_P2_exchg_invalids'])
                continue

            # In P2 exchg rejected:        0
            m = p22.match(line)
            if m:
                incoming_dict['in_p2_exchg_rejected'] = int(m.groupdict()['in_P2_exchg_rejected'])
                continue

            # In P2 SA delete reqs:        0
            m = p23.match(line)
            if m:
                incoming_dict['in_p2_sa_delete_requests'] = int(m.groupdict()['in_P2_SA_delete_reqs'])
                continue

            # Out octets:                  5712
            m = p24.match(line)
            if m:
                outgoing_dict = index_count_dict.setdefault('outgoing', {})
                outgoing_dict['out_octets'] = int(m.groupdict()['out_octets'])
                continue

            # Out packets:                 34 
            m = p25.match(line)
            if m:
                outgoing_dict['out_packets'] = int(m.groupdict()['out_packets'])
                continue

            # Out drops:                   0
            m = p26.match(line)
            if m:
                outgoing_dict['out_drops'] = int(m.groupdict()['out_drops'])
                continue

            # Out notifys:                 34
            m = p27.match(line)
            if m:
                outgoing_dict['out_notifys'] = int(m.groupdict()['out_notifys'])
                continue

            # Out P2 exchgs:               34 
            m = p28.match(line)
            if m:
                outgoing_dict['out_p2_exchgs'] = int(m.groupdict()['out_P2_exchgs'])
                continue

            # Out P2 exchg invalids:       0
            m = p29.match(line)
            if m:
                outgoing_dict['out_p2_exchgs_invalids'] = int(m.groupdict()['out_P2_exchgs_invalids'])
                continue

            # Out P2 exchg rejects:        0 
            m = p30.match(line)
            if m:
                outgoing_dict['out_p2_exchgs_rejects'] = int(m.groupdict()['out_P2_exchgs_rejects'])
                continue

            # Out P2 Sa delete requests:   17    
            m = p31.match(line)
            if m:
                outgoing_dict['out_p2_sa_delete_requests'] = int(m.groupdict()['out_P2_Sa_delete_requests'])
                continue



        return flowmib_tunnel_dict


# ==============================
# Schema for
#   'show crypto ikev2 stats'
# ==============================
class ShowCryptoIkev2StatsSchema(MetaParser):
    """
    Schema for
        * 'show crypto ikev2 stats'
    """
    
    schema = {
        'ikev2_statistics': {
                'system_resource_limit': int,                                 
                'max_sa': int,
                'max_in_nego': int,
                'max_out_nego': int,
                'total_incoming_sa': int,
                'total_incoming_sa_active': int,
                'total_incoming_sa_negotiating': int,
                'total_outgoing_sa': int,           
                'total_outgoing_sa_active': int,
                'total_outgoing_sa_negotiating': int,
                'incoming_v2_requests': int,
                'incoming_requests_accept': int,
                'incoming_requests_reject': int,
                'outgoing_v2_requests': int,
                'outgoing_requests_accept': int,
                'outgoing_requests_reject': int,
                'rejected_v2_requests': int,
                'rejected_requests_rsrclow': int,
                'rejected_requests_salimit': int,
                'ikev2_packet_drop': int,
                'incoming_requests_drop_lowq': int,
                'incoming_cookie_challenge': {
                    'incoming_challenge_requests': int,
                    'incoming_challenge_accept': int,
                    'incoming_challenge_reject': int,
                    'incoming_challenge_no_cookie': int                   
                },
                'deleted_sessions_cert_revoke': int,
                Optional('active_qr_sessions'): int,
                Optional('qr_manual'): int,
                Optional('qr_dynamic'): int                
            },
        }
    

# =========================================================
#  Parser for 'show crypto ikev2 stats'
# =========================================================   
class ShowCryptoIkev2Stats(ShowCryptoIkev2StatsSchema):
    """
    Parser for
        * 'show crypto ikev2 stats'
    """
    
    # Defines a function to run the cli_command
    cli_command = 'show crypto ikev2 stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # System Resource Limit:   0        Max IKEv2 SAs: 0        Max in nego(in/out): 40/400
        p1 = re.compile(r'^System Resource Limit:\s+(?P<sr_limit>\d+)\s+Max IKEv2 SAs:\s+'
                        r'(?P<v2_sa>\d+)\s+Max in nego\(in\/out\):\s+'
                        r'(?P<in_nego>\d+)\/(?P<out_nego>\d+)$')
    
        # Total incoming IKEv2 SA Count:    0        active:        0        negotiating: 0
        p2 = re.compile(r'^Total incoming IKEv2 SA Count:\s+(?P<in_sa>\d+)\s+'
                        r'active:\s+(?P<in_sa_act>\d+)\s+negotiating:\s+(?P<in_sa_nego>\d+)$')
 
        # Total outgoing IKEv2 SA Count:    0        active:        0        negotiating: 0
        p3 = re.compile(r'^Total outgoing IKEv2 SA Count:\s+(?P<out_sa>\d+)\s+'
                        r'active:\s+(?P<out_sa_act>\d+)\s+negotiating:\s+(?P<out_sa_nego>\d+)$')

        # Incoming IKEv2 Requests: 0        accepted:      0        rejected:    0
        p4 = re.compile(r'^Incoming IKEv2 Requests:\s+(?P<in_req>\d+)\s+accepted:\s+'
                        r'(?P<in_accept>\d+)\s+rejected:\s+(?P<in_reject>\d+)$')

        # Outgoing IKEv2 Requests: 0        accepted:      0        rejected:    0
        p5 = re.compile(r'^Outgoing IKEv2 Requests:\s+(?P<out_req>\d+)\s+accepted:\s+'
                        r'(?P<out_accept>\d+)\s+rejected:\s+(?P<out_reject>\d+)$')

        # Rejected IKEv2 Requests: 0        rsrc low:      0        SA limit:    0 
        p6 = re.compile(r'^Rejected IKEv2 Requests:\s+(?P<rej_req>\d+)\s+rsrc low:\s+'
                        r'(?P<low_rsrc>\d+)\s+SA limit:\s+(?P<sa_limit>\d+)$')

        # IKEv2 packets dropped at dispatch: 0 
        p7 = re.compile(r'^IKEv2 packets dropped at dispatch:\s+(?P<pak_drop>\d+)$')

        # Incoming Requests dropped as LOW Q limit reached : 0
        p8 = re.compile(r'^Incoming Requests dropped as LOW Q limit reached :\s+(?P<drop_lowq>\d+)$')

        # Incoming IKEV2 Cookie Challenged Requests: 0 
        p9 = re.compile(r'^Incoming IKEV2 Cookie Challenged Requests:\s+(?P<chall_req>\d+)$')

        #     accepted: 0        rejected: 0        rejected no cookie: 0 
        p10 = re.compile(r'^accepted:\s+(?P<chall_acc>\d+)\s+rejected:\s+(?P<chall_rej>\d+)\s+'
                         r'rejected no cookie:\s+(?P<chall_rej_nocook>\d+)$')

        # Total Deleted sessions of Cert Revoked Peers: 0 
        p11 = re.compile(r'^Total Deleted sessions of Cert Revoked Peers:\s+(?P<del_sess_cert>\d+)$')

        # Sessions with Quantum Resistance: 1        Manual: 4294967291 Dynamic: 6
        p12 = re.compile(r'^Sessions with Quantum Resistance:\s+(?P<active_qr_sessions>\d+)\s+Manual:\s+(?P<qr_manual>\d+)\s+Dynamic:\s+(?P<qr_dynamic>\d+)$')

        # initial return dictionary

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # System Resource Limit:   0        Max IKEv2 SAs: 0        Max in nego(in/out): 40/400                               
            m = p1.match(line)
            if m:
                group = m.groupdict() 
                v2stat_dict = ret_dict.setdefault('ikev2_statistics', {})
                v2stat_dict.update({'system_resource_limit': int(group['sr_limit'])})
                v2stat_dict.update({'max_sa': int(group['v2_sa'])})
                v2stat_dict.update({'max_in_nego': int(group['in_nego'])})
                v2stat_dict.update({'max_out_nego': int(group['out_nego'])})
                continue 

            # Total incoming IKEv2 SA Count:    0        active:        0        negotiating: 0                                 
            m = p2.match(line)
            if m:
                group = m.groupdict()                 
                v2stat_dict.update({'total_incoming_sa': int(group['in_sa'])})
                v2stat_dict.update({'total_incoming_sa_active': int(group['in_sa_act'])})
                v2stat_dict.update({'total_incoming_sa_negotiating': int(group['in_sa_nego'])})
                continue

            # Total outgoing IKEv2 SA Count:    0        active:        0        negotiating: 0                                
            m = p3.match(line)
            if m:
                group = m.groupdict()                  
                v2stat_dict.update({'total_outgoing_sa': int(group['out_sa'])})
                v2stat_dict.update({'total_outgoing_sa_active': int(group['out_sa_act'])})
                v2stat_dict.update({'total_outgoing_sa_negotiating': int(group['out_sa_nego'])})
                continue

            # Incoming IKEv2 Requests: 0        accepted:      0        rejected:    0                                
            m = p4.match(line)
            if m:
                group = m.groupdict()                     
                v2stat_dict.update({'incoming_v2_requests': int(group['in_req'])})
                v2stat_dict.update({'incoming_requests_accept': int(group['in_accept'])})
                v2stat_dict.update({'incoming_requests_reject': int(group['in_reject'])})
                continue

            # Outgoing IKEv2 Requests: 0        accepted:      0        rejected:    0                               
            m = p5.match(line)
            if m:
                group = m.groupdict()                  
                v2stat_dict.update({'outgoing_v2_requests': int(group['out_req'])})
                v2stat_dict.update({'outgoing_requests_accept': int(group['out_accept'])})
                v2stat_dict.update({'outgoing_requests_reject': int(group['out_reject'])})
                continue

            # Rejected IKEv2 Requests: 0        rsrc low:      0        SA limit:    0                               
            m = p6.match(line)
            if m:
                group = m.groupdict()                                  
                v2stat_dict.update({'rejected_v2_requests': int(group['rej_req'])})
                v2stat_dict.update({'rejected_requests_rsrclow': int(group['low_rsrc'])})
                v2stat_dict.update({'rejected_requests_salimit': int(group['sa_limit'])})
                continue

            # IKEv2 packets dropped at dispatch: 0                               
            m = p7.match(line)
            if m:
                group = m.groupdict()                     
                v2stat_dict.update({'ikev2_packet_drop': int(group['pak_drop'])})
                continue

            # Incoming Requests dropped as LOW Q limit reached : 0                              
            m = p8.match(line)
            if m:
                group = m.groupdict()                  
                v2stat_dict.update({'incoming_requests_drop_lowq': int(group['drop_lowq'])})
                continue

            # Incoming IKEV2 Cookie Challenged Requests: 0                             
            m = p9.match(line)
            if m:
                group = m.groupdict()                    
                chall_dict = v2stat_dict.setdefault('incoming_cookie_challenge', {})
                chall_dict.update({'incoming_challenge_requests': int(group['chall_req'])})
                continue

            #     accepted: 0        rejected: 0        rejected no cookie: 0                           
            m = p10.match(line)
            if m:
                group = m.groupdict()                  
                chall_dict.update({'incoming_challenge_accept': int(group['chall_acc'])})
                chall_dict.update({'incoming_challenge_reject': int(group['chall_rej'])})
                chall_dict.update({'incoming_challenge_no_cookie': int(group['chall_rej_nocook'])})
                continue

            # Total Deleted sessions of Cert Revoked Peers: 0                               
            m = p11.match(line)
            if m:
                group = m.groupdict()                   
                v2stat_dict.update({'deleted_sessions_cert_revoke': int(group['del_sess_cert'])})
                continue

            # Sessions with Quantum Resistance: 1        Manual: 4294967291 Dynamic: 6
            m = p12.match(line)
            if m:
                group = m.groupdict()
                v2stat_dict.update({'active_qr_sessions': int(group['active_qr_sessions'])})
                v2stat_dict.update({'qr_manual': int(group['qr_manual'])})
                v2stat_dict.update({'qr_dynamic': int(group['qr_dynamic'])})
                continue

        return ret_dict


# ==============================
# Schema for
#   'show crypto call admission statistics'
# ==============================
class ShowCryptoCallAdmissionStatisticsSchema(MetaParser):
    """
    Schema for
        * 'show crypto call admission statistics'
    """
    
    schema = {
        'crypto_call_admission_statistics': {
                'system_resource_limit': int,                               
                'max_ike_sa': int,
                'max_in_nego': int,
                'total_ike_sa': int,
                'total_ike_sa_active': int,
                'total_ike_sa_negotiating': int,
                'incoming_ike_request': int,
                'incoming_request_accept': int,
                'incoming_request_reject': int,
                'outgoing_ike_request': int,
                'outgoing_request_accept': int,
                'outgoing_request_reject': int,
                'rejected_ike_request': int,
                'rejected_request_rsrc_low': int,
                'rejected_request_active_salimit': int,
                'in_neg_salimit': int,
                'ike_packet_drop_dispatch': int,
                'max_ipsec_sa': int,
                'total_ipsec_sa': int,
                'total_ipsec_sa_active': int,
                'total_ipsec_sa_negotiating': int,
                'incoming_ipsec_request': int,
                'incoming_ipsec_accept': int,
                'incoming_ipsec_reject': int,
                'outgoing_ipsec_request': int,
                'outgoing_ipsec_accept': int,
                'outgoing_ipsec_reject': int,                
                'phase_sa_under_negotiation': int
            },
        }
 
# =========================================================
#  Parser for 'show crypto call admission statistics'
# =========================================================   
class ShowCryptoCallAdmissionStatistics(ShowCryptoCallAdmissionStatisticsSchema):
    """
    Parser for
        * 'show crypto call admission statistics'
    """
    
    # Defines a function to run the cli_command
    cli_command = 'show crypto call admission statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # System Resource Limit:        0 Max IKE SAs:     0 Max in nego:    40
        p1 = re.compile(r'^System Resource Limit:\s+(?P<sr_limit>\d+)\s+Max IKE SAs:\s+'
                        r'(?P<v1_sa>\d+)\s+Max in nego:\s+(?P<in_nego>\d+)$')
    
        # Total IKE SA Count:        1001 active:       1001 negotiating:     0
        p2 = re.compile(r'^Total IKE SA Count:\s+(?P<ike_sa>\d+)\s+active:\s+'
                        r'(?P<ike_sa_act>\d+)\s+negotiating:\s+(?P<ike_sa_nego>\d+)$')
 
        # Incoming IKE Requests:  1057639 accepted:  1056101 rejected:     1538
        p3 = re.compile(r'^Incoming IKE Requests:\s+(?P<in_req>\d+)\s+accepted:\s+'
                        r'(?P<in_accept>\d+)\s+rejected:\s+(?P<in_reject>\d+)$')

        # Outgoing IKE Requests:        0 accepted:        0 rejected:        0
        p4 = re.compile(r'^Outgoing IKE Requests:\s+(?P<out_req>\d+)\s+accepted:\s+'
                        r'(?P<out_accept>\d+)\s+rejected:\s+(?P<out_reject>\d+)$')

        # Rejected IKE Requests:     1538 rsrc low:        0 Active SA limit: 0 
        p5 = re.compile(r'^Rejected IKE Requests:\s+(?P<rej_req>\d+)\s+rsrc low:\s+'
                        r'(?P<low_rsrc>\d+)\s+Active SA limit:\s+(?P<sa_limit>\d+)$')

        #      In-neg SA limit: 1538
        p6 = re.compile(r'^In-neg SA limit:\s+(?P<neg_sa_limit>\d+)$')

        # IKE packets dropped at dispatch:        0
        p7 = re.compile(r'^IKE packets dropped at dispatch:\s+(?P<pak_drop>\d+)$')

        # Max IPSEC SAs:     0
        p8 = re.compile(r'^Max IPSEC SAs:\s+(?P<sa_max>\d+)$')

        # Total IPSEC SA Count:        1081 active:       1075 negotiating:     6
        p9 = re.compile(r'^Total IPSEC SA Count:\s+(?P<ipsec_sa>\d+)\s+active:\s+'
                        r'(?P<secsa_act>\d+)\s+negotiating:\s+(?P<secsa_nego>\d+)$')
 
        # Incoming IPSEC Requests:   511759 accepted:   511759 rejected:        0
        p10 = re.compile(r'^Incoming IPSEC Requests:\s+(?P<in_sa_req>\d+)\s+accepted:\s+'
                        r'(?P<in_sa_accept>\d+)\s+rejected:\s+(?P<in_sa_reject>\d+)$')

        # Outgoing IPSEC Requests:     1214 accepted:     1214 rejected:        0
        p11 = re.compile(r'^Outgoing IPSEC Requests:\s+(?P<out_sa_req>\d+)\s+accepted:\s+'
                         r'(?P<out_sa_accept>\d+)\s+rejected:\s+(?P<out_sa_reject>\d+)$')

        # Phase1.5 SAs under negotiation:         0 
        p12 = re.compile(r'^Phase1.5 SAs under negotiation:\s+(?P<phase1_sa>\d+)$')

        # initial return dictionary

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # System Resource Limit:        0 Max IKE SAs:     0 Max in nego:    40                                 
            m = p1.match(line)
            if m:
                group = m.groupdict()  
                v2stat_dict = ret_dict.setdefault('crypto_call_admission_statistics', {})
                v2stat_dict.update({'system_resource_limit': int(group['sr_limit'])})
                v2stat_dict.update({'max_ike_sa': int(group['v1_sa'])})
                v2stat_dict.update({'max_in_nego': int(group['in_nego'])})
                continue

            # Total IKE SA Count:        1001 active:       1001 negotiating:     0                                 
            m = p2.match(line)
            if m:
                group = m.groupdict()                  
                v2stat_dict.update({'total_ike_sa': int(group['ike_sa'])})
                v2stat_dict.update({'total_ike_sa_active': int(group['ike_sa_act'])})
                v2stat_dict.update({'total_ike_sa_negotiating': int(group['ike_sa_nego'])})
                continue

            # Incoming IKE Requests:  1057639 accepted:  1056101 rejected:     1538                                 
            m = p3.match(line)
            if m:
                group = m.groupdict()                   
                v2stat_dict.update({'incoming_ike_request': int(group['in_req'])})
                v2stat_dict.update({'incoming_request_accept': int(group['in_accept'])})
                v2stat_dict.update({'incoming_request_reject': int(group['in_reject'])})
                continue

            # Outgoing IKE Requests:        0 accepted:        0 rejected:        0                                
            m = p4.match(line)
            if m:
                group = m.groupdict()                   
                v2stat_dict.update({'outgoing_ike_request': int(group['out_req'])})
                v2stat_dict.update({'outgoing_request_accept': int(group['out_accept'])})
                v2stat_dict.update({'outgoing_request_reject': int(group['out_reject'])})
                continue

            # Rejected IKE Requests:     1538 rsrc low:        0 Active SA limit: 0                                
            m = p5.match(line)
            if m:
                group = m.groupdict()                     
                v2stat_dict.update({'rejected_ike_request': int(group['rej_req'])})
                v2stat_dict.update({'rejected_request_rsrc_low': int(group['low_rsrc'])})
                v2stat_dict.update({'rejected_request_active_salimit': int(group['sa_limit'])})
                continue

            #      In-neg SA limit: 1538                               
            m = p6.match(line)
            if m:
                group = m.groupdict()                    
                v2stat_dict.update({'in_neg_salimit': int(group['neg_sa_limit'])})
                continue

            # IKE packets dropped at dispatch:        0                              
            m = p7.match(line)
            if m:
                group = m.groupdict()                     
                v2stat_dict.update({'ike_packet_drop_dispatch': int(group['pak_drop'])})
                continue

            # Max IPSEC SAs:     0                              
            m = p8.match(line)
            if m:
                v2stat_dict.update({'max_ipsec_sa': int(m.groupdict()['sa_max'])})
                continue

            # Total IPSEC SA Count:        1081 active:       1075 negotiating:     6                               
            m = p9.match(line)
            if m:
                group = m.groupdict()                   
                v2stat_dict.update({'total_ipsec_sa': int(group['ipsec_sa'])})
                v2stat_dict.update({'total_ipsec_sa_active': int(group['secsa_act'])})
                v2stat_dict.update({'total_ipsec_sa_negotiating': int(group['secsa_nego'])})
                continue

            # Incoming IPSEC Requests:   511759 accepted:   511759 rejected:        0                              
            m = p10.match(line)
            if m:
                group = m.groupdict()                
                v2stat_dict.update({'incoming_ipsec_request': int(group['in_sa_req'])})
                v2stat_dict.update({'incoming_ipsec_accept': int(group['in_sa_accept'])})
                v2stat_dict.update({'incoming_ipsec_reject': int(group['in_sa_reject'])})
                continue

            # Outgoing IPSEC Requests:     1214 accepted:     1214 rejected:        0                               
            m = p11.match(line)
            if m:
                group = m.groupdict()                     
                v2stat_dict.update({'outgoing_ipsec_request': int(group['out_sa_req'])})
                v2stat_dict.update({'outgoing_ipsec_accept': int(group['out_sa_accept'])})
                v2stat_dict.update({'outgoing_ipsec_reject': int(group['out_sa_reject'])})
                continue

            # Phase1.5 SAs under negotiation:         0
            m = p12.match(line)
            if m:
                group = m.groupdict()                    
                v2stat_dict.update({'phase_sa_under_negotiation': int(group['phase1_sa'])})
                continue

        return ret_dict

#===================================================
# Schema for 'show crypto session | count UP-ACTIVE'
#===================================================

class ShowCryptoSessionCountUpActiveSchema(MetaParser):
    schema = {
        'total_number_of_active_sessions': {
            'active_crypto_session_count': int
        }
    }

#====================================================
#  Parser for 'show crypto session | count UP-ACTIVE'
#====================================================

class ShowCryptoSessionCountUpActive(ShowCryptoSessionCountUpActiveSchema):

    cli_command = 'show crypto session | count UP-ACTIVE'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # Total number of groups:   831
        p1 = re.compile(r'^Number\s+of\s+lines\s+which\s+match\s+regexp\s+=\s+(?P<active_crypto_session_count>\d+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_number_of_active_sessions_dict = ret_dict.setdefault('total_number_of_active_sessions', {})
                total_number_of_active_sessions_dict['active_crypto_session_count'] = int(group['active_crypto_session_count'])

        return ret_dict

# =================================================
#  Schema for 'show crypto gkm gm replay'
# =================================================

class ShowCryptogkmgmreplaySchema(MetaParser):
    """Schema for 'show crypto gkm gm replay' """
    
    schema = {
        'anti_replay_information': {
            'group': {
                Any(): {
                    'time_based_replay': {
                        Optional('enable'): str,
                        Optional('replay_value'): str,
                        Optional('input_packets'): int,
                        Optional('output_packets'): int,
                        Optional('input_error_packets'): int,
                        Optional('output_error_packets'): int,
                        Optional('time_sync_error'): int,
                        Optional('max_time_delta'): str,
                        Optional('tbar_error_history'): {
                            'tbar_error': str
                        },
                    },
                },
            },
        },
    }


# =================================================
#  Parser for 'show crypto gkm gm replay'
# =================================================

class ShowCryptogkmgmreplay(ShowCryptogkmgmreplaySchema):
    
    """Parser for 'show crypto gkm gm replay' """
    
    cli_command = 'show crypto gkm gm replay'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Anti-replay Information For Group bw600:
        p1 = re.compile(r'^Anti-replay Information For Group (?P<group>[\w\d\-]+):$')

        # Timebased Replay:
        p2 = re.compile(r'^Timebased Replay:$')

        #       is not enabled
        p3 = re.compile(r'is not enabled$')

        # Replay Value : 3611735.21 secs
        p4 = re.compile(r'^Replay Value :\s(?P<replay_value>[\w\s\.]+)$')

        # Input Packets : 2753845832 Output Packets : 3668218697
        p5 = re.compile(r'^Input Packets :\s+(?P<input_packets>[\d]+)\s+Output Packets :\s+(?P<output_packets>[\d]+)$')

        # Input Error Packets : 0 Output Error Packets : 0
        p6 = re.compile(r'^Input Error Packets :\s+(?P<input_error_packets>\d+)\s+Output Error Packets :\s+(?P<output_error_packets>\d+)$')

        # Time Sync Error : 0 Max time delta : 0.00 secs
        p7 = re.compile(r'^Time Sync Error :\s+(?P<time_sync_error>\d+)\s+Max time delta :\s+(?P<max_time_delta>[\w\.\s]+)$')

        # TBAR Error History (sampled at 10pak/min):
        p8 = re.compile(r'^TBAR Error History \(sampled at 10pak\/min\):')

        #               No TBAR errors detected
        p9 = re.compile(r'No TBAR errors detected$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            # Anti-replay Information For Group bw600:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('anti_replay_information', {}).setdefault('group', {}).setdefault(group['group'], {})
                continue

            # Timebased Replay:
            m = p2.match(line)
            if m:
                time_dict = group_dict.setdefault('time_based_replay', {})
                continue
            
            #       is not enabled
            m = p3.match(line)
            if m:
                time_dict.update({'enable': 'Not enabled'})
                continue

            # Replay Value : 3611735.21 secs
            m = p4.match(line)
            if m:
                group = m.groupdict()
                time_dict.update({'replay_value': group['replay_value']})
                continue

            # Input Packets : 2753845832 Output Packets : 3668218697
            m = p5.match(line)
            if m:
                group = m.groupdict()
                time_dict.update({'input_packets': int(group['input_packets'])})
                time_dict.update({'output_packets': int(group['output_packets'])})
                continue

            # Input Error Packets : 0 Output Error Packets : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                time_dict.update({'input_error_packets': int(group['input_error_packets'])})
                time_dict.update({'output_error_packets': int(group['output_error_packets'])})
                continue

            # Time Sync Error : 0 Max time delta : 0.00 secs
            m = p7.match(line)
            if m:
                group = m.groupdict()
                time_dict.update({'time_sync_error': int(group['time_sync_error'])})
                time_dict.update({'max_time_delta': group['max_time_delta']})
                continue

            # TBAR Error History (sampled at 10pak/min):
            m = p8.match(line)
            if m:
                prv_line = line
                tbar_dict = time_dict.setdefault('tbar_error_history', {})
                continue

            #               No TBAR errors detected
            m = p9.match(line)
            if m:
                pvr_line = line
                tbar_dict.update({'tbar_error':'No errors detected'})
                continue

        return master_dict



# ==============================
# Schema for
#   'show crypto gdoi feature dp-recovery'
# ==============================
class ShowCryptoGdoiFeatureSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi feature dp-recovery'
    """

    schema = {
        'group': {
            Any():{
                'key_server':{
                    Any():{
                        'key_server_id': str,
                        'key_version': str,
                        'key_feature_supported': str
                    },
                },
                'group_member':{
                    Any():{
                        'group_member_id': str,
                        'group_member_version': str,
                        'group_feature_supported': str
                    },                   
                },
            },
        },
    }


# =================================================
#  Parser for 'show crypto gdoi feature'
# =================================================

class ShowCryptoGdoiFeature(ShowCryptoGdoiFeatureSchema):
    
    """Parser for 'show crypto gdoi feature' """
    
    cli_command = 'show crypto gdoi feature'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Group Name: getvpn1
        p1 = re.compile(r'^Group Name:\s(?P<group>[\S]+)$')

        #     Key Server ID       Version   Feature Supported
        p2 = re.compile(r'Key Server ID \s+Version\s+Feature\sSupported')

        #         15.15.15.1          1.0.26         Yes
        p3 = re.compile(r'(?P<key_server_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<key_version>[\d\.]+)\s+(?P<key_feature_supported>[\w]+)$')

        #    Group Member ID     Version   Feature Supported
        p4 = re.compile(r'Group Member ID\s+Version\s+Feature\sSupported')

        #         25.25.25.1          1.0.25         Yes
        p5 = re.compile(r'(?P<group_member_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<group_member_version>[\d\.]+)\s+(?P<group_feature_supported>[\w]+)$')

        master_dict = {}
        server_flag = False
        member_flag = False
        for line in output.splitlines():

            line = line.strip()
            
            # Group Name: getvpn1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                continue
                
            #     Key Server ID       Version   Feature Supported
            m = p2.match(line)
            if m:
                group = m.groupdict()
                server_dict = group_dict.setdefault('key_server', {})
                server_flag = True
                continue

            #         1.1.1.1          1.0.27         Yes
            if server_flag:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ser_count_dict = server_dict.setdefault(len(server_dict)+1, {})
                    ser_count_dict.update({'key_server_id': group['key_server_id']})
                    ser_count_dict.update({'key_version': group['key_version']})
                    ser_count_dict.update({'key_feature_supported': group['key_feature_supported']})                    
                    continue

            #    Group Member ID     Version   Feature Supported
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member_dict = group_dict.setdefault('group_member', {})
                server_flag = False
                member_flag = True
                continue

            #        3.3.1.1          1.0.26         Yes
            if member_flag:
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    count_dict = group_member_dict.setdefault(len(group_member_dict)+1, {})
                    count_dict.update({'group_member_id' : group['group_member_id']})
                    count_dict.update({'group_member_version': group['group_member_version']})
                    count_dict.update({'group_feature_supported': group['group_feature_supported']})
                    continue
                       
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi feature dp-recovery'
# =================================================
class ShowCryptoGdoiFeatureDpRecovery(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature dp-recovery'
    '''

    cli_command = "show crypto gdoi feature dp-recovery"

# =================================================
#  Parser for 'show crypto gdoi feature ckm'
# =================================================
class ShowCryptoGdoiFeatureCkm(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature ckm'
    '''

    cli_command = "show crypto gdoi feature ckm"

# =================================================
#  Parser for 'show crypto gdoi feature suite-b'
# =================================================
class ShowCryptoGdoiFeatureSuiteB(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature suite-b'
    '''

    cli_command = "show crypto gdoi feature suite-b"

# =================================================
#  Parser for 'show crypto gdoi feature policy-replace'
# =================================================
class ShowCryptoGdoiFeaturePolicyReplace(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature policy-replace'
    '''

    cli_command = "show crypto gdoi feature policy-replace"

# =================================================
#  Parser for 'show crypto gdoi feature gm-removal'
# =================================================
class ShowCryptoGdoiFeatureGmRemoval(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gm-removal'
    '''

    cli_command = "show crypto gdoi feature gm-removal"

# =================================================
#  Parser for 'show crypto gdoi feature gdoi-mib'
# =================================================
class ShowCryptoGdoiFeatureGdoiMib(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gdoi-mib'
    '''

    cli_command = "show crypto gdoi feature gdoi-mib"

# =================================================
#  Parser for 'show crypto gdoi feature gdoi-interop-ack'
# =================================================
class ShowCryptoGdoiFeatureGdoiInteropAck(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature gdoi-interop-ack'
    '''

    cli_command = "show crypto gdoi feature gdoi-interop-ack"

# =================================================
#  Parser for 'show crypto gdoi feature ip-d3p'
# =================================================
class ShowCryptoGdoiFeatureIpD3p(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature ip-d3p'
    '''

    cli_command = "show crypto gdoi feature ip-d3p"

# =================================================
#  Parser for 'show crypto gdoi feature long-sa-lifetime'
# =================================================
class ShowCryptoGdoiFeatureLongSaLifetime(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature long-sa-lifetime'
    '''

    cli_command = "show crypto gdoi feature long-sa-lifetime"

# =================================================
#  Parser for 'show crypto gdoi feature pfs'
# =================================================
class ShowCryptoGdoiFeaturePfs(ShowCryptoGdoiFeature):
    '''Parser for:
        * 'show crypto gdoi feature pfs'
    '''

    cli_command = "show crypto gdoi feature pfs"

    

# =================================================
# Schema for
#  Schema for 'show crypto gdoi gm'
# =================================================
class ShowCryptoGdoiGmSchema(MetaParser):
    """schema for show crypto gdoi gm"""

    schema = {
        'group_member': {
            Any(): {
                'direction': str, 
                'acl_recieved': str,
                'group_member_ip': str,
                'vrf': str,
                'local_ip': str,
                'local_port': int,
                'remote_ip': str,
                'remote_port': int,
                'fvrf': str,
                'ivrf': str,
                'version': str,
                'registration_status': str,
                'registered_ip': str,
                Optional('registered_time'): str,
                Optional('registration_succeded'): int,
                Optional('registration_attempt'): int,
                Optional('rekey_ip'): str,
                Optional('rekey_seq_num'): int,
                Optional('unicast_rekeys_recieved'): int,
                Optional('ack_unicast_key'): int,
                Optional('rekey_recieved_time'): str,
                Optional('pfs_rekey_recieved'): int,
                Optional('dp_error_monitoring'): str,
                Optional('ipsec_init_reg_executed'): int,
                Optional('ipsec_init_reg_postponed'): int,
                Optional('active_tek_number'): int,
                Optional('sa_track_status'): str,
                Optional('fail_close_revert'): str
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi gm'
# ===================================================
class ShowCryptoGdoiGm(ShowCryptoGdoiGmSchema):

    """Parser for show crypto gdoi gm"""

    cli_command = 'show crypto gdoi gm'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Group Member Information For Group getvpn1: 
        p1 = re.compile(r'^Group +Member +Information +For +Group +(?P<group_member>[\d\w]+)')
        #    IPSec SA Direction       : Both
        p2 = re.compile(r'^IPSec +SA +Direction +: +(?P<direction>[\w]+)$')
        #    ACL Received From KS     : gdoi_group_getvpn1_temp_acl
        p3 = re.compile(r'^ACL Received From KS     : (?P<acl_recieved>[\w\d_-]+)')
        #    Group member             : 3.3.1.1         vrf: None
        p4 = re.compile(r'^Group +member +: +(?P<group_member_ip>[\d.]+) +vrf: +(?P<vrf>[\w\d]+)')        
        #       Local addr/port       : 3.3.1.1/848
        p5 = re.compile(r'^Local addr.port +: +(?P<local_ip>[\d.]+).(?P<local_port>[\d]+)')
        #       Remote addr/port      : 1.1.1.1/848
        p6 = re.compile(r'^Remote +addr.port +: +(?P<remote_ip>[\d.]+).(?P<remote_port>[\d]+)')
        #       fvrf/ivrf             : None/None
        p7 = re.compile(r'^fvrf.ivrf +: +(?P<fvrf>[\d\w]+).(?P<ivrf>[\d\w]+)')
        #       Version               : 1.0.26
        p8 = re.compile(r'^Version +: +(?P<version>[\d.]+)')
        #       Registration status   : Registered
        p9 = re.compile(r'^Registration +status +: +(?P<registration_status>[\w]+)')
        #       Registered with       : 1.1.1.1
        p10 = re.compile(r'^Registered +with +: +(?P<registered_ip>[\d.]+)')
        #       Re-registers in       : 518 sec
        p11 = re.compile(r'^Re\-registers +in +: +(?P<registered_time>[\d\w ]+)')
        #       Succeeded registration: 1
        p12 = re.compile(r'^Succeeded +registration: +(?P<registration_succeded>[\d]+)')
        #       Attempted registration: 1
        p13 = re.compile(r'^Attempted +registration: +(?P<registration_attempt>[\d]+)')
        #       Last rekey from       : 1.1.1.1
        p14 = re.compile(r'^Last +rekey +from +: +(?P<rekey_ip>[\d.]+)')
        #       Last rekey seq num    : 1
        p15 = re.compile(r'^Last +rekey +seq +num +: +(?P<rekey_seq_num>[\d]+)')
        #       Unicast rekey received: 26
        p16 = re.compile(r'^Unicast +rekey +received: +(?P<unicast_rekeys_recieved>[\d]+)')
        #       Rekey ACKs sent       : 26
        p17 = re.compile(r'^Rekey +ACKs +sent +: +(?P<ack_unicast_key>[\d]+)')
        #       Rekey Rcvd(hh:mm:ss)  : 00:00:19
        p18 = re.compile(r'^Rekey +Rcvd.hh:mm:ss. +: +(?P<rekey_recieved_time>[\d:]+)')
        #       PFS Rekey received    : 0
        p19 = re.compile(r'^PFS +Rekey +received +: +(?P<pfs_rekey_recieved>[\d]+)')
        #       DP Error Monitoring   : OFF
        p20 = re.compile(r'^DP +Error +Monitoring +: +(?P<dp_error_monitoring>[\w]+)')
        #       IPSEC init reg executed    : 0
        p21 = re.compile(r'^IPSEC +init +reg +executed +: +(?P<ipsec_init_reg_executed>[\d]+)')
        #       IPSEC init reg postponed   : 0
        p22 = re.compile(r'^IPSEC +init +reg +postponed +: +(?P<ipsec_init_reg_postponed>[\d]+)')
        #       Active TEK Number     : 2
        p23 = re.compile(r'^Active +TEK +Number +: +(?P<active_tek_number>[\d]+)')
        #       SA Track (OID/status) : disabled
        p24 = re.compile(r'^SA +Track +.OID.status. +: +(?P<sa_track_status>[\w]+)')
        #       Fail-Close Revert : Disabled
        p25 = re.compile(r'^Fail.Close +Revert +: +(?P<fail_close_revert>[\w]+)')

        # initial return dictionary
        ret_dict = {}
  
        for line in out.splitlines():
            line=line.strip()
            #Group Member Information For Group getvpn1:
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                group_member = ret_dict.setdefault('group_member', {}).setdefault(group['group_member'], {})           
                continue

            #    IPSec SA Direction       : Both            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'direction': group['direction']})
                continue

            #    ACL Received From KS     : gdoi_group_getvpn1_temp_acl            
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'acl_recieved': group['acl_recieved']})
                continue

            #    Group member             : 3.3.1.1         vrf: None
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'group_member_ip': group['group_member_ip']})
                group_member.update({'vrf': group['vrf']})
                continue                

            #Local addr/port       : 3.3.1.1/848
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'local_ip': group['local_ip']})
                group_member.update({'local_port': int(group['local_port'])})
                continue            

            #       Remote addr/port      : 1.1.1.1/848
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'remote_ip': group['remote_ip']})
                group_member.update({'remote_port': int(group['remote_port'])})
                continue
                
            #       fvrf/ivrf             : None/None
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'fvrf': group['fvrf']})
                group_member.update({'ivrf': group['ivrf']})
                continue
                
            #       Version               : 1.0.26
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'version': group['version']})
                continue

            #       Registration status   : Registered
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_status': group['registration_status']})
                continue

            #       Registered with       : 1.1.1.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registered_ip': group['registered_ip']})
                continue

            #Re-registers in       : 518 sec
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registered_time': group['registered_time']})
                continue

            #       Succeeded registration: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_succeded': int(group['registration_succeded'])})
                continue

            #       Attempted registration: 1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'registration_attempt': int(group['registration_attempt'])})
                continue

            #       Last rekey from       : 1.1.1.1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_ip': group['rekey_ip']})
                continue

            #       Last rekey seq num    : 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_seq_num': int(group['rekey_seq_num'])})
                continue

            #       Unicast rekey received: 26
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'unicast_rekeys_recieved': int(group['unicast_rekeys_recieved'])})
                continue

            #       Rekey ACKs sent       : 26
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ack_unicast_key': int(group['ack_unicast_key'])})
                continue

            #       Rekey Rcvd(hh:mm:ss)  : 00:00:19
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'rekey_recieved_time': group['rekey_recieved_time']})
                continue

            #       PFS Rekey received    : 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'pfs_rekey_recieved': int(group['pfs_rekey_recieved'])})
                continue

            #       DP Error Monitoring   : OFF
            m = p20.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'dp_error_monitoring': group['dp_error_monitoring']})
                continue

            #       IPSEC init reg executed    : 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ipsec_init_reg_executed': int(group['ipsec_init_reg_executed'])})
                continue

            #       IPSEC init reg postponed   : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'ipsec_init_reg_postponed': int(group['ipsec_init_reg_postponed'])})
                continue

            #       Active TEK Number     : 2
            m = p23.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'active_tek_number': int(group['active_tek_number'])})
                continue

            #       SA Track (OID/status) : disabled
            m = p24.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'sa_track_status': group['sa_track_status']})
                continue

            #       Fail-Close Revert : Disabled
            m = p25.match(line)
            if m:
                group = m.groupdict()
                group_member.update({'fail_close_revert': group['fail_close_revert']})
                continue        
        return ret_dict

# =================================================
#  Schema for 'show crypto sockets internal'
# =================================================

class ShowCryptoSocketsInternalSchema(MetaParser):
    """Schema for show crypto sockets internal"""
    schema = {
        'sockets':{
            'Socket Messages':{
                'Open Socket':int,
                'Close Socket':int,
                'Listen Start':int,
                'Listen Stop':int,
                'SS Connect':int,
                'SS Connect Socket':int,
                'SS End Message':int,
                'unknown':int
            },
            'Listen SM Stats':{
                'Message Stats':{
                    'Create Listener Map':int,
                    'Detach Listener Map':int
                }
            },
            'IPSec Events':{
                'Socket Up':int,
                'Socket down':int
            }
        }
    }

# =================================================
#  Parser for 'show crypto sockets internal'
# =================================================

class ShowCryptoSocketsInternal(ShowCryptoSocketsInternalSchema):
    """Parser for show crypto show crypto sockets internal"""

    cli_command = ['show crypto sockets internal']

    def cli(self,output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Crypto Secure Socket Messages
        p1 = re.compile(r'(?P<messages_seciton>Crypto Secure Socket Messages)')

        #  Open Socket               : 4994      Close Socket              : 14378  
        p2 = re.compile(r'Open Socket\s+:\s+(?P<opn_sokt>\d+)\s+Close Socket\s+:\s+(?P<cls_sokt>\d+)')

        #  Listen Start              : 1         Listen Stop               : 0   
        p3 = re.compile(r'Listen Start\s+:\s+(?P<lstn_strt>\d+)\s+Listen Stop\s+:\s+(?P<lstn_stp>\d+)')
        
        #  SS Connect                : 0         SS Connect Socket         : 0  
        p4 = re.compile(r'SS Connect\s+:\s+(?P<ss_cnct>\d+)\s+SS Connect Socket\s+:\s+(?P<cnct_sokt>\d+)')

        #  SS End Message            : 0         unknown                   : 0  
        p5 = re.compile(r'SS End Message\s+:\s+(?P<ss_end_msg>\d+)\s+unknown\s+:\s+(?P<unkn>\d+)')

        # Crypto Secure Socket Listen SM Stats
        p6 = re.compile(r'^(?P<listn_sm_stats_seciton>Crypto Secure Socket Listen SM Stats)$')

        # Message Stats
        p7 = re.compile(r'^(?P<msg_sts_seciton>Message Stats)$')

        #  Create Listener Map       : 1           Detach Listener Map       : 0    
        p8 = re.compile(r'Create Listener Map\s+:\s+(?P<listn_map>\d+)\s+Detach Listener Map\s+:\s+(?P<dtch_listn_map>\d+)')

        # Crypto Secure Socket IPSec Events
        p9 = re.compile(r'^(?P<ipsec_evnt_seciton>Crypto Secure Socket IPSec Events)$')
        
        #  Socket Up                 : 21513     Socket down               : 14316  
        p10 = re.compile(r'Socket Up\s+:\s+(?P<sokt_up>\d+)\s+Socket down\s+:\s+(?P<sokt_down>\d+)')
        m7=False
        for line in out.splitlines():
            line = line.strip()
            # Crypto Secure Socket Messages
            m = p1.search(line)
            if m:
                ret_dict['Socket Messages'] = {}
                continue
            
            #  Open Socket               : 4994      Close Socket              : 14378
            m = p2.match(line)
            if m:
                ret_dict['Socket Messages']['Open Socket'] = int(m.groupdict()['opn_sokt'])
                ret_dict['Socket Messages']['Close Socket'] = int(m.groupdict()['cls_sokt'])
                continue
            
            #  Listen Start              : 1         Listen Stop               : 0
            m = p3.match(line)
            if m:
                ret_dict['Socket Messages']['Listen Start'] = int(m.groupdict()['lstn_strt'])
                ret_dict['Socket Messages']['Listen Stop'] = int(m.groupdict()['lstn_stp'])
                continue

            #  SS Connect                : 0         SS Connect Socket         : 0
            m = p4.match(line)
            if m:
                ret_dict['Socket Messages']['SS Connect'] = int(m.groupdict()['ss_cnct'])
                ret_dict['Socket Messages']['SS Connect Socket'] = int(m.groupdict()['cnct_sokt'])
                continue

            #  SS End Message            : 0         unknown                   : 0
            m = p5.match(line)
            if m:
                ret_dict['Socket Messages']['SS End Message'] = int(m.groupdict()['ss_end_msg'])
                ret_dict['Socket Messages']['unknown'] = int(m.groupdict()['unkn'])
                continue

            # Crypto Secure Socket Listen SM Stats
            m = p6.match(line)
            if m:
                ret_dict['Listen SM Stats'] = {}
                Listen_SM_Stats=True
                continue
            
            # Message Stats
            m = p7.match(line)
            if m and Listen_SM_Stats:
                ret_dict['Listen SM Stats']['Message Stats'] = {}
                Listen_SM_Stats=False
                Listen_SM_Stats_Message_Stats = True
                continue
            
            #  Create Listener Map       : 1           Detach Listener Map       : 0
            m = p8.match(line)
            if m and Listen_SM_Stats_Message_Stats:
                ret_dict['Listen SM Stats']['Message Stats']['Create Listener Map'] = int(m.groupdict()['listn_map'])
                ret_dict['Listen SM Stats']['Message Stats']['Detach Listener Map'] = int(m.groupdict()['dtch_listn_map'])
                Listen_SM_Stats_Message_Stats = False
                continue

             # Crypto Secure Socket IPSec Events
            m = p9.match(line)
            if m:
                ret_dict['IPSec Events'] = {}
                continue

            #  Socket Up                 : 21513     Socket down               : 14316 
            m = p10.match(line)
            if m:
                ret_dict['IPSec Events']['Socket Up'] = int(m.groupdict()['sokt_up'])
                ret_dict['IPSec Events']['Socket down'] = int(m.groupdict()['sokt_down'])
                continue

        try:
            final_dict={'sockets':ret_dict}
            return final_dict
        except Exception:
            return {}

# ============================================================================
# Schema for 'show crypto ipsec internal | include PALHWcreate_ipsec_sa_by_q'
# ============================================================================

class ShowCryptoIpsecPALHWcreate_ipsec_sa_by_qSchema(MetaParser):
    schema = {
        'total_internal_counters': {
            'internal_counter_list': int
        }
    }

# =============================================================================
#  Parser for 'show crypto ipsec internal | include PALHWcreate_ipsec_sa_by_q'
# =============================================================================

class ShowCryptoIpsecPALHWcreate_ipsec_sa_by_q(ShowCryptoIpsecPALHWcreate_ipsec_sa_by_qSchema):

    cli_command = 'show crypto ipsec internal | include PALHWcreate_ipsec_sa_by_q'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # PALHWcreate_ipsec_sa_by_q |913873|12797964|0    |0    |913873|12797964|14   ||0    |0    |0    |0    |0    |0    |0    |0    |0    |0 
        p1 = re.compile(r'^PALHWcreate_ipsec_sa_by_q[\s\S]+\|\|(?P<counters>\d+)\s*?[\|\d\s]+$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_internal_counters_dict = ret_dict.setdefault('total_internal_counters', {})
                total_internal_counters_dict['internal_counter_list'] = int(group['counters'])

        return ret_dict

# ===================================================
# Schema for 'show crypto isakmp sa | count ACTIVE'
# ===================================================

class ShowCryptoIsakmpSaCountActiveSchema(MetaParser):
    schema = {
        'total_number_of_active_sessions': {
            'active_crypto_isakmpsa_count': int
        }
    }

# ====================================================
#  Parser for 'show crypto isakmp sa | count ACTIVE'
# ====================================================

class ShowCryptoIsakmpSaCountActive(ShowCryptoIsakmpSaCountActiveSchema):

    cli_command = 'show crypto isakmp sa | count ACTIVE'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # Number of lines which match regexp = 2016
        p1 = re.compile(r'^Number\s+of\s+lines\s+which\s+match\s+regexp\s+=\s+(?P<active_crypto_isakmpsa_count>\d+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 2016
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_number_of_active_sessions_dict = ret_dict.setdefault('total_number_of_active_sessions', {})
                total_number_of_active_sessions_dict['active_crypto_isakmpsa_count'] = int(group['active_crypto_isakmpsa_count'])

        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi ks'
# =================================================
class ShowCryptoGdoiKsSchema(MetaParser):
    """schema for show crypto gdoi ks"""
    schema = {
        'crypto_gdoi_ks': {
            'total_group_members': int,
            'crypto_gdoi_ks_group': {
                'key_server_group_name': str,
                'group_name': str,
                'reauth_status': str,
                'group_identity': int,
                'group_type': str,
                'group_members': int,
                'rekey_ack_config': str,
                'direction': str,
                'd3p_window_status': str,
                'sr_factor': int,
                'ckm_status': str,
                'acl_configured': {
                    'acl_name': str
                },
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks'
# ===================================================
class ShowCryptoGdoiKs(ShowCryptoGdoiKsSchema):
    """Parser for show crypto gdoi ks"""
    cli_command = 'show crypto gdoi ks'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        #Total group members registered to this box: 2
        p1 = re.compile(r'^Total +group +members +registered +to +this +box: +(?P<total_group_members>[\d]+)$')
        #Key Server Information For Group getvpn1:
        p2 = re.compile(r'^Key +Server +Information +For +Group +(?P<key_server_group_name>[\w\d]+):$')
        #    Group Name               : getvpn1
        p3 = re.compile(r'Group +Name +: +(?P<group_name>[\w\d]+)$')
        #    Re-auth on new CRL       : Disabled
        p4 = re.compile(r'^Re.auth +on +new +CRL +: +(?P<reauth_status>[\w]+)$')
        #    Group Identity           : 1223
        p5 = re.compile(r'^Group +Identity +: +(?P<group_identity>[\d]+)$')
        #    Group Type               : GDOI (ISAKMP)
        p6 = re.compile(r'^Group +Type +: +(?P<group_type>[\w \(\)]+)$')
        #    Group Members            : 2
        p7 = re.compile(r'^Group +Members +: +(?P<group_members>[\d]+)$')
        #    Rekey Acknowledgement Cfg: Cisco
        p8 = re.compile(r'^Rekey +Acknowledgement +Cfg: +(?P<rekey_ack_config>[\w]+)$')
        #    IPSec SA Direction       : Both
        p9 = re.compile(r'^IPSec +SA +Direction +: +(?P<direction>[\w]+)$')
        #    IP D3P Window            : Disabled
        p10 = re.compile(r'IP +D3P +Window +: +(?P<d3p_window_status>[\w]+)$')
        #    Split Resiliency Factor  : 0
        p11 = re.compile(r'^Split +Resiliency +Factor +: +(?P<sr_factor>[\d]+)$')
        #    CKM status               : Disabled
        p12 = re.compile(r'^CKM +status +: +(?P<ckm_status>[\w]+)$')
        #    ACL Configured:
        #        access-list acl1
        p13 = re.compile(r'^access.list +(?P<acl_name>[\w\d]+)$')

        ret_dict = {}
  
        for line in output.splitlines():
            line = line.strip()
            #Total group members registered to this box: 2
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                crypto_gdoi_ks = ret_dict.setdefault('crypto_gdoi_ks', {})
                crypto_gdoi_ks.update({'total_group_members': int(group['total_group_members'])})
                continue

            #Key Server Information For Group getvpn1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group = crypto_gdoi_ks.setdefault('crypto_gdoi_ks_group', {})
                crypto_gdoi_ks_group.update({'key_server_group_name': group['key_server_group_name']})
                continue

            #    Group Name               : getvpn1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_name': group['group_name']})
                continue

            #    Re-auth on new CRL       : Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'reauth_status': group['reauth_status']})
                continue

            #    Group Identity           : 1223
            m = p5.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_identity': int(group['group_identity'])})
                continue
                
            #    Group Type               : GDOI (ISAKMP)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_type': group['group_type']})
                continue
                
            #    Group Members            : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'group_members': int(group['group_members'])})
                continue

            #    Rekey Acknowledgement Cfg: Cisco
            m = p8.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'rekey_ack_config': group['rekey_ack_config']})
                continue

            #    IPSec SA Direction       : Both
            m = p9.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'direction': group['direction']})
                continue

            #    IP D3P Window            : Disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'d3p_window_status': group['d3p_window_status']})
                continue

            #    Split Resiliency Factor  : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'sr_factor': int(group['sr_factor'])})
                continue

            #    CKM status               : Disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_ks_group.update({'ckm_status': group['ckm_status']})
                continue

            #    ACL Configured:
            #        access-list acl1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                acl_configured = crypto_gdoi_ks_group.setdefault('acl_configured', {})
                acl_configured.update({'acl_name': group['acl_name']})
                continue
        
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi rekey sa'
# =================================================
class ShowCryptoGdoiRekeySaSchema(MetaParser):
    """schema for show crypto gdoi rekey sa"""
    
    schema = {
        'getvpn_rekey': {
            Any(): {
                'dst_ip': str,
                'src_ip': str,
                'connection_id': int,
                'rekey_status': str
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi rekey sa'
# ===================================================
class ShowCryptoGdoiRekeySa(ShowCryptoGdoiRekeySaSchema):
    """Parser for show crypto gdoi rekey sa"""
    
    cli_command = 'show crypto gdoi rekey sa'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # dst             src             conn-id         status
        p0 = re.compile(r'dst +src +conn.id +status')

        # 3.3.1.1         1.1.1.1         1712            ACTIVE
        p1 = re.compile(r'(?P<dst_ip>[\d.]+) +(?P<src_ip>[\d.]+) +(?P<connection_id>[\d]+) +(?P<rekey_status>[\w]+)')
        
        ret_dict = {}
  
        for line in output.splitlines():
            line=line.strip()
            
            m = p0.match(line)
            if m:
                group = m.groupdict()
                getvpn_rekey = ret_dict.setdefault('getvpn_rekey', {})
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()                
                count_dict = getvpn_rekey.setdefault(len(getvpn_rekey)+1, {})
                count_dict.update({'dst_ip': group['dst_ip']})
                count_dict.update({'src_ip': group['src_ip']})
                count_dict.update({'connection_id': int(group['connection_id'])})
                count_dict.update({'rekey_status': group['rekey_status']})                
                continue
        
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi rekey sa detail'
# =================================================
class ShowCryptoGdoiRekeySaDetailSchema(MetaParser):
    """schema for show crypto gdoi rekey sa detail"""
    schema = {
        'kek_sa_db_stats': {
            'num_active': int,
            'num_malloc': int,
            'num_free': int,
            'kek_policy': {
                'transport_type': str,
                'local_addr': str,
                'local_port': int,
                'remote_details': {
                    'remote_addr': str,
                    'remote_port': int,
                    'spi': str,
                    'mgmt_alg_status': str,
                    'encrypt_alg': str,
                    'crypto_iv_length': int,
                    'key_size': int,
                    'orig_life': int,
                    'sig_hash_alg_status': str,
                    'sig_key_length': int,
                    'sig_size': int,
                    'ack': str,
                    'connection_type': str,
                    'connection_id': int,
                    'seq_num': int,
                    'prev_seq_num': int,
                    'handle': int,
                    'interface_type': str,
                    'group_name': str
                },
            },
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi rekey sa detail'
# ===================================================
class ShowCryptoGdoiRekeySaDetail(ShowCryptoGdoiRekeySaDetailSchema):

    """Parser for show crypto gdoi rekey sa detail"""

    cli_command = 'show crypto gdoi rekey sa detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # num_active = 1
        p1 = re.compile(r'num_active += +(?P<num_active>[\d]+)')
        
        # num_malloc = 107
        p2 = re.compile(r'num_malloc += +(?P<num_malloc>[\d]+)')
        
        # num_free = 105
        p3 = re.compile(r'num_free += +(?P<num_free>[\d]+)')
        
        #  KEK POLICY (transport type : Unicast)
        p4 = re.compile(r'KEK +POLICY +.transport +type +: +(?P<transport_type>[\w]+).')
        
        #   Local addr/port : 26.26.26.1/848
        p5 = re.compile(r'Local +addr.port +: +(?P<local_addr>[\d.]+).(?P<local_port>[\d]+)')
        
        #   Remote addr/port : 15.15.15.1/848
        p6 = re.compile(r'Remote +addr.port +: +(?P<remote_addr>[\d.]+).(?P<remote_port>[\d]+)')
        
        #    spi : 0x5C78568A11D464C47E9268A1D9A8787D
        p7 = re.compile(r'spi +: +(?P<spi>[\w\d]+)')
        
        #    management alg     : disabled    encrypt alg       : AES       
        p8 = re.compile(r'management +alg +: +(?P<mgmt_alg_status>[\w]+) +encrypt +alg +: +(?P<encrypt_alg>[\w]+)')
        
        #    crypto iv length   : 16          key size          : 32      
        p9 = re.compile(r'crypto +iv +length +: +(?P<crypto_iv_length>[\d]+)  +key +size +: +(?P<key_size>[\d]+)')
        
        #    orig life(sec)     : 0         
        p10 = re.compile(r'orig +life.sec. +: +(?P<orig_life>[\d]+)')
        
        #    sig hash algorithm : enabled     sig key length    : 294     
        p11 = re.compile(r'sig +hash +algorithm +: +(?P<sig_hash_alg_status>[\w]+) +sig +key +length +: +(?P<sig_key_length>[\d]+)')
        
        #    sig size           : 256
        p12 = re.compile(r'sig +size +: +(?P<sig_size>[\d]+)')
        
        #    acknowledgement    : Cisco
        p13 = re.compile(r'acknowledgement +: +(?P<ack>[\w]+)')
        
        #    conn_id (IKEv1)    : 1138
        p14 = re.compile(r'conn_id +.(?P<connection_type>[\w\d]+). +: +(?P<connection_id>[\d]+)')
        
        #    seq num            : 0           prev seq num      : 0       
        p15 = re.compile(r'seq +num +: +(?P<seq_num>[\d]+) +prev +seq +num +: +(?P<prev_seq_num>[\d]+)')
        
        #    handle             : 40000072  
        p16 = re.compile(r'handle +: +(?P<handle>[\d]+)')
        
        #    Interface          : GigabitEthernet
        p17 = re.compile(r'Interface +: +(?P<interface_type>[\w]+)')
        
        #    Group Name         : GV-GROUP1
        p18 = re.compile(r'Group +Name +: +(?P<group_name>[\d\w._-]+)')

        ret_dict = {}
  
        for line in output.splitlines():
            line=line.strip()
            m = p1.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats = ret_dict.setdefault('kek_sa_db_stats', {})
                kek_sa_db_stats.update({'num_active': int(group['num_active'])})
                continue

            m = p2.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats.update({'num_malloc': int(group['num_malloc'])})
                continue

            m = p3.match(line) 
            if m:
                group = m.groupdict()
                kek_sa_db_stats.update({'num_free': int(group['num_free'])})
                continue

            m = p4.match(line) 
            if m:
                group = m.groupdict()
                kek_policy = kek_sa_db_stats.setdefault('kek_policy', {})
                kek_policy.update({'transport_type': group['transport_type']})
                continue

            m = p5.match(line) 
            if m:
                group = m.groupdict()
                kek_policy.update({'local_addr': group['local_addr']})
                kek_policy.update({'local_port': int(group['local_port'])})
                continue

            m = p6.match(line) 
            if m:
                group = m.groupdict()
                remote_details = kek_policy.setdefault('remote_details', {})
                remote_details.update({'remote_addr': group['remote_addr']})
                remote_details.update({'remote_port': int(group['remote_port'])})
                continue

            m = p7.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'spi': group['spi']})
                continue

            m = p8.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'mgmt_alg_status': group['mgmt_alg_status']})
                remote_details.update({'encrypt_alg': group['encrypt_alg']})
                continue

            m = p9.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'crypto_iv_length': int(group['crypto_iv_length'])})
                remote_details.update({'key_size': int(group['key_size'])})
                continue

            m = p10.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'orig_life': int(group['orig_life'])})
                continue

            m = p11.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'sig_hash_alg_status': group['sig_hash_alg_status']})
                remote_details.update({'sig_key_length': int(group['sig_key_length'])})
                continue

            m = p12.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'sig_size': int(group['sig_size'])})
                continue

            m = p13.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'ack': group['ack']})
                continue

            m = p14.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'connection_type': group['connection_type']})
                remote_details.update({'connection_id': int(group['connection_id'])})
                continue

            m = p15.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'seq_num': int(group['seq_num'])})
                remote_details.update({'prev_seq_num': int(group['prev_seq_num'])})
                continue

            m = p16.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'handle': int(group['handle'])})
                continue

            m = p17.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'interface_type': group['interface_type']})
                continue

            m = p18.match(line) 
            if m:
                group = m.groupdict()
                remote_details.update({'group_name': group['group_name']})
                continue
            
        return ret_dict

# =================================================
#  Schema for 'show tunnel protection statistics'
# =================================================
class ShowTunnelProtectionStatisticsSchema(MetaParser):
    """schema for show tunnel protection statistics"""

    schema = {
        'tunnel_prot_stats': {
            'message_stats': {
                'sent': {
                    'listen_start': int,
                    'listen_stop': int,
                    'socket_open': int,
                    'socket_close': int
                },
                'recieved': {
                    'general_error': int,
                    'socket_error': int,
                    'socket_ready': int,
                    'socket_up': int,
                    'socket_down': int,
                    'mtu_changed': int,
                    'listen_ready': int,
                    'other': int
                },
            },
            'error_stats': {
                'recieved': {
                    'listen_start': int,
                    'listen_stop': int,
                    'socket_open': int,
                    'socket_close': int,
                    'connection_timeout': int
                },
            },
            'data_stats': {
                'sent': {
                    'cef_packet_drop': int,
                    'ps_packet_drop': int
                },
                'recieved': {
                    'ps_packet_drop': int,
                    'clear_packet_drop': int
                }
            }
        }
    }

# ===================================================
#  Parser for 'show tunnel protection statistics'
# ===================================================
class ShowTunnelProtectionStatistics(ShowTunnelProtectionStatisticsSchema):

    """Parser for show tunnel protection statistics"""

    cli_command = 'show tunnel protection statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        #------------------------- Message Statistics -------------------------
        p1_0 = re.compile(r'-+ +Message +Statistics +-+')
        #   Sent:
        #      Listen Start   : 1    Listen Stop    : 0    Socket Open    : 0    
        p1 = re.compile(r'Listen +Start +: +(?P<listen_start>[\d]+) +Listen +Stop +: +(?P<listen_stop>[\d]+) +Socket +Open +: +(?P<socket_open>[\d]+)')

        #      Socket Close   : 0    
        p2 = re.compile(r'Socket +Close +: +(?P<socket_close>[\d+])')
        #   Rcvd:
        #      General Error  : 0    Socket Error   : 0    Socket Ready   : 0    
        p3 = re.compile(r'General +Error +: +(?P<general_error>[\d]+) +Socket +Error +: +(?P<socket_error>[\d]+) +Socket +Ready +: +(?P<socket_ready>[\d]+)')
        #      Socket Up      : 0    Socket Down    : 0    MTU Changed    : 0    
        p4 = re.compile(r'Socket Up +: +(?P<socket_up>[\d]+) +Socket +Down +: +(?P<socket_down>[\d]) +MTU +Changed +: +(?P<mtu_changed>[\d]+)')
        #      Listen Ready   : 1    Other          : 0    
        p5 = re.compile(r'Listen +Ready +: +(?P<listen_ready>[\d]+) +Other +: +(?P<other>[\d]+)')
        #-------------------------- Error Statistics --------------------------
        p6_0 = re.compile(r'-+ +Error +Statistics +-+')
        #   Rcvd:
        #      Listen Start   : 0    Listen Stop    : 0    Socket Open    : 0    
        p6 = re.compile(r'Listen +Start +: +(?P<listen_start>[\d]+) +Listen +Stop +: (?P<listen_stop>[\d]+) +Socket +Open +: +(?P<socket_open>[\d]+)')
        #      Socket Close   : 0    Conn Timeout   : 0    
        p7 = re.compile(r'Socket +Close +: +(?P<socket_close>[\d]+) +Conn +Timeout +: +(?P<connection_timeout>[\d]+)')
        #------------ Data Statistics(Other than IPSec protection) ------------
        p8_0 = re.compile(r'-+ +Data +Statistics.Other +than +IPSec +protection. +-+')
        #   Sent:
        #      cef pkt drops  : 0    ps pkt drops   : 0    
        p8 = re.compile(r'cef +pkt +drops +: +(?P<cef_packet_drop>[\d]+) +ps +pkt +drops +: +(?P<ps_packet_drop>[\d]+)')
        #   Rcvd:
        #      ps pkt drops   : 0    clear pkt drops: 0    
        p9 = re.compile(r'ps +pkt +drops +: +(?P<ps_packet_drop>[\d]+) +clear +pkt +drops: +(?P<clear_packet_drop>[\d]+)')

        ret_dict = {}
        message_stats = False
        error_stats = False
        data_stats = False
  
        for line in output.splitlines():
            line=line.strip()
            
            m = p1_0.match(line)
            if m:
                message_stats = True
                continue

            if message_stats:
                m = p1.match(line) 
                if m:
                    group = m.groupdict()
                    tunnel_prot_stats = ret_dict.setdefault('tunnel_prot_stats', {})
                    message_stats = tunnel_prot_stats.setdefault('message_stats', {})
                    sent = message_stats.setdefault('sent', {})
                    sent.update({'listen_start': int(group['listen_start'])})
                    sent.update({'listen_stop': int(group['listen_stop'])})
                    sent.update({'socket_open': int(group['socket_open'])})
                    continue

                m = p2.match(line) 
                if m:
                    group = m.groupdict()
                    sent.update({'socket_close': int(group['socket_close'])})
                    continue

                m = p3.match(line) 
                if m:
                    group = m.groupdict()
                    recieved = message_stats.setdefault('recieved', {})
                    recieved.update({'general_error': int(group['general_error'])})
                    recieved.update({'socket_error': int(group['socket_error'])})
                    recieved.update({'socket_ready': int(group['socket_ready'])})
                    continue

                m = p4.match(line) 
                if m:
                    group = m.groupdict()
                    recieved.update({'socket_up': int(group['socket_up'])})
                    recieved.update({'socket_down': int(group['socket_down'])})
                    recieved.update({'mtu_changed': int(group['mtu_changed'])})                
                    continue

                m = p5.match(line) 
                if m:
                    group = m.groupdict()
                    recieved.update({'listen_ready': int(group['listen_ready'])})
                    recieved.update({'other': int(group['other'])})
                    message_stats = False
                    continue

            m = p6_0.match(line)
            if m:
                error_stats = True
                continue

            if error_stats:
                m = p6.match(line) 
                if m:
                    group = m.groupdict()
                    error_stats = tunnel_prot_stats.setdefault('error_stats', {})
                    recieved = error_stats.setdefault('recieved', {})
                    recieved.update({'listen_start': int(group['listen_start'])})
                    recieved.update({'listen_stop': int(group['listen_stop'])})
                    recieved.update({'socket_open': int(group['socket_open'])})
                    continue

                m = p7.match(line) 
                if m:
                    group = m.groupdict()
                    recieved.update({'socket_close': int(group['socket_close'])})
                    recieved.update({'connection_timeout': int(group['connection_timeout'])})                    
                    error_stats = False
                    continue

            m = p8_0.match(line)
            if m:
                data_stats = True
                continue

            if data_stats:
                m = p8.match(line) 
                if m:
                    group = m.groupdict()
                    data_stats = tunnel_prot_stats.setdefault('data_stats', {})
                    sent = data_stats.setdefault('sent', {})
                    sent.update({'cef_packet_drop': int(group['cef_packet_drop'])})
                    sent.update({'ps_packet_drop': int(group['ps_packet_drop'])})
                    continue

                m = p9.match(line) 
                if m:
                    group = m.groupdict()
                    recieved = data_stats.setdefault('recieved', {})
                    recieved.update({'ps_packet_drop': int(group['ps_packet_drop'])})
                    recieved.update({'clear_packet_drop': int(group['clear_packet_drop'])})                    
                    data_stats = False
                    continue
        
        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm identifier'
# =================================================
class ShowCryptoGdoiGmIdentifierSchema(MetaParser):
    """Schema for show crypto gdoi gm identifier"""
    schema = {
        'group':{
            Any(): {
                Any(): {
                    'vrf_name': str,
                    'transform_mode': str,
                    'no_of_sid': int,
                    'current_sid': str
                    },
                },
            },
        }

# =================================================
#  Parser for 'show crypto gdoi gm identifier'
# =================================================
class ShowCryptoGdoiGmIdentifier(ShowCryptoGdoiGmIdentifierSchema):
    """Parser for show crypto gdoi gm identifier"""

    cli_command = ['show crypto gdoi gm identifier']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GM Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^GM Sender ID \(SID\) Information for Group\s*(?P<group_name>\S+):$')

        # Group Member: 44.44.44.1       vrf: None
        p2 = re.compile(r'^Group Member:\s*(?P<group_member>[\S]+)\s*vrf:\s*(?P<vrf_name>[\S]+)$')

        # Transform Mode                  : Non-Counter (Non-Suite-B)
        p3 = re.compile(r'^Transform Mode\s*:\s*(?P<transform_mode>[\w\s\(\)-]+)$')

        # of SIDs Last Requested        : 0
        p4 = re.compile(r'^# of SIDs Last Requested\s*:\s*(?P<no_of_sid>[\d]+)$')

        # CURRENT SIDs: None
        p5 = re.compile(r'^CURRENT SIDs:\s*(?P<current_sid>[\S]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # GM Sender ID (SID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                group_name = groups['group_name']
                group_name_dict = ret_dict.setdefault('group',{}).setdefault(group_name,{})
                continue

            # Group Member: 44.44.44.1       vrf: None
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict = group_name_dict.setdefault(groups['group_member'],{})
                group_member_dict.update({'vrf_name': groups['vrf_name']})
                continue
        

            # Transform Mode                  : Non-Counter (Non-Suite-B)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue

            # of SIDs Last Requested        : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_member_dict.update(group)
                continue

            # CURRENT SIDs: None
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue        
       
        return ret_dict 

# =========================================
#  Schema for 'show crypto gdoi ks detail'
# =========================================
class ShowCryptoGdoiKsDetailSchema(MetaParser):
    """schema for show crypto gdoi ks detail"""

    schema = {
        'group_members_registered': int,
        Any(): {
            'group_name': str,
            're_auth_on_new_crl': str,
            'group_identity': int,
            'group_type': str,
            'group_members': int,
            'rekey_acknowledgement_cfg': str,
            'ipsec_sa_direction': str,
            'ip_d3p_window': str,
            'split_resiliency_factor': int,
            'ckm_status': str,
            'acl_configured': {
                'access_list': str,
            },
            'redundancy': {
                'redundancy_mode': str,
                'local_address': str,
                'local_priority': int,
                'local_ks_status': str,
                'local_ks_role': str,
                'local_ks_version': str,
                'local_coop_version': str
            }
        }     
    }

# ===================================================
#  Parser for 'show crypto gdoi ks detail'
# ===================================================
class ShowCryptoGdoiKsDetail(ShowCryptoGdoiKsDetailSchema):

    """Parser for 'show crypto gdoi ks detail"""

    cli_command = 'show crypto gdoi ks detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Total group members registered to this box: 12
        p1 = re.compile(r'^Total\s+group\s+members\s+registered\s+to\s+this\s+box:+\s(?P<group_members_registered>\d+)$')
        # Key Server Information For Group bw6000:
        p2 = re.compile(r'^Key\s+Server\s+Information\s+For\s+Group\s+(?P<key_server_group>\S+):$')
        # Group Name               : bw6000
        p3 = re.compile(r'^Group\s+Name\s+:\s+(?P<group_name>\S+)$')
        # Re-auth on new CRL       : Disabled
        p4 = re.compile(r'^Re-auth\s+on\s+new\s+CRL\s+:\s+(?P<re_auth_on_new_crl>\w+)$')
        # Group Identity           : 6000
        p5 = re.compile(r'^Group\s+Identity\s+:\s+(?P<group_identity>\d+)$')
        # Group Type               : GDOI (ISAKMP)
        p6 = re.compile(r'^Group\s+Type\s+:\s+GDOI\s+\((?P<group_type>\S+)\)$')
        # Group Members            : 2
        p7 = re.compile(r'^Group\s+Members\s+:\s+(?P<group_members>\d+)$')
        # Rekey Acknowledgement Cfg: Cisco
        p8 = re.compile(r'^Rekey\s+Acknowledgement\s+Cfg:\s+(?P<rekey_acknowledgement_cfg>\w+)$')
        # IPSec SA Direction       : Both
        p9 = re.compile(r'^IPSec\s+SA\s+Direction\s+:\s+(?P<ipsec_sa_direction>\w+)$')
        # IP D3P Window            : Disabled
        p10 = re.compile(r'^IP\s+D3P\s+Window\s+:\s+(?P<ip_d3p_window>\w+)$')
        # Split Resiliency Factor  : 0
        p11 = re.compile(r'^Split\s+Resiliency\s+Factor\s+:\s+(?P<split_resiliency_factor>\d+)$')
        # CKM status               : Disabled
        p12 = re.compile(r'^CKM\s+status\s+:\s+(?P<ckm_status>\w+)$')
        # ACL Configured: 
        # access-list bw600-crypto-policy
        p13 = re.compile(r'^access-list\s+(?P<access_list>\S+)$')
        # Redundancy               : Configured
        p14 = re.compile(r'^Redundancy\s+:\s+(?P<redundancy_mode>\w+)$')
        # Local Address        : 15.15.15.1
        p15 =  re.compile(r'^Local\s+Address\s+:\s+(?P<local_address>\S+)$')
        # Local Priority       : 245
        p16 = re.compile(r'^Local\s+Priority\s+:\s+(?P<local_priority>\d+)$')
        # Local KS Status      : Alive
        p17 = re.compile(r'^Local\s+KS\s+Status\s+:\s+(?P<local_ks_status>\w+)$')
        # Local KS Role        : Primary
        p18 = re.compile(r'^Local\s+KS\s+Role\s+:\s+(?P<local_ks_role>\w+)$')
        # Local KS Version     : 1.0.27
        p19 = re.compile(r'^Local\s+KS\s+Version\s+:\s+(?P<local_ks_version>\S+)$')
        # Local COOP Version   : 1.0.8 
        p20 = re.compile(r'^Local\s+COOP\s+Version\s+:\s+(?P<local_coop_version>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Total group members registered to this box: 12
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'group_members_registered': int(group['group_members_registered'])})
                continue

            # Key Server Information For Group bw6000:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_name = group['key_server_group']
                server_dict = ret_dict.setdefault(group_name, {})
                continue

            # Group Name               : bw6000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_name': group['group_name']})
                continue

            # Re-auth on new CRL       : Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'re_auth_on_new_crl': group['re_auth_on_new_crl']})
                continue
             
            # Group Identity           : 6000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_identity': int(group['group_identity'])})
                continue

            # Group Type               : GDOI (ISAKMP)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_type': group['group_type']})
                continue

            # Group Members            : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'group_members': int(group['group_members'])})
                continue

            # Rekey Acknowledgement Cfg: Cisco
            m = p8.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'rekey_acknowledgement_cfg': group['rekey_acknowledgement_cfg']})
                continue

            # IPSec SA Direction       : Both
            m = p9.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ipsec_sa_direction': group['ipsec_sa_direction']})
                continue

            # IP D3P Window            : Disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ip_d3p_window': group['ip_d3p_window']})
                continue

            # Split Resiliency Factor  : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'split_resiliency_factor': int(group['split_resiliency_factor'])})
                continue

            # CKM status               : Disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                server_dict.update({'ckm_status': group['ckm_status']})
                continue

            # access-list bw600-crypto-policy
            m = p13.match(line)
            if m:
                group = m.groupdict()
                access_list_dict = server_dict.setdefault('acl_configured', {})
                access_list_dict.update({'access_list': group['access_list']})
                continue

            # Redundancy               : Configured
            m = p14.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict = server_dict.setdefault('redundancy', {})
                redundancy_dict.update({'redundancy_mode': group['redundancy_mode']})
                continue

            # Local Address        : 15.15.15.1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_address': group['local_address']})
                continue

            # Local Priority       : 245
            m = p16.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_priority': int(group['local_priority'])})
                continue

            # Local KS Status      : Alive
            m = p17.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_status': group['local_ks_status']})
                continue

            # Local KS Role        : Primary
            m = p18.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_role': group['local_ks_role']})
                continue

            # Local KS Version     : 1.0.27
            m = p19.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_ks_version': group['local_ks_version']})
                continue

            # Local COOP Version   : 1.0.8
            m = p20.match(line)
            if m:
                group = m.groupdict()
                redundancy_dict.update({'local_coop_version': group['local_coop_version']})
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm pubkey'
# =================================================
class ShowCryptoGdoiGmPubkeySchema(MetaParser):
    """Schema for show crypto gdoi gm pubkey"""
    schema = {
        'gdoi_group': {
            Any(): {
                Optional(Any()): {
                    Optional('ks_ipaddress'): str,
                    Optional('conn_id'): int,
                    Optional('my_cookie'): str,
                    Optional('his_cookie'): str,
                    Optional('key_data'): {
                        Optional('key_data_info'): list
                        }
                    }
                }
            }
        }


# =================================================
#  Parser for 'show crypto gdoi gm pubkey'
# =================================================
class ShowCryptoGdoiGmPubkey(ShowCryptoGdoiGmPubkeySchema):
    """Parser for show crypto gdoi gm pubkey"""

    cli_command = ['show crypto gdoi gm pubkey']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GDOI Group: bw6000
        p1 = re.compile(r'^GDOI\s*Group:\s*(?P<group_name>\S+)$')

        # KS IP Address: 15.15.15.1
        p2 = re.compile(r'^KS\s*IP\s*Address:\s*(?P<ks_ipaddress>\S+)$')

        # conn-id: 44334    my-cookie:C5AC6039    his-cookie:A440633E
        p3 = re.compile(r'^conn-id:\s*(?P<conn_id>\d+)\s*my-cookie:\s*(?P<my_cookie>\S+)\s*his-cookie:\s*(?P<his_cookie>\S+)$')

        # Key Data:
        p4 = re.compile(r'^(?P<key_data_info>[0-9A-Z\s]+)$')


        for line in output.splitlines():
            line = line.strip()

            # GDOI Group: bw6000
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('gdoi_group', {}).setdefault(group_name, {})
                count = 0
                continue

            # KS IP Address: 15.15.15.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ks_dict = group_name_dict.setdefault(count, {})
                ks_dict['ks_ipaddress'] = group['ks_ipaddress']
                count +=1
                continue


            # conn-id: 44334    my-cookie:C5AC6039    his-cookie:A440633E
            m = p3.match(line)
            if m:
                ks_dict['conn_id'] = int(m.groupdict()['conn_id'])
                ks_dict['my_cookie'] = m.groupdict()['my_cookie']
                ks_dict['his_cookie'] = m.groupdict()['his_cookie']
                continue

            # Key Data:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_data_dict = ks_dict.setdefault('key_data', {})
                key_data_dict_full = key_data_dict.setdefault('key_data_info', [])
                key_data_dict_full.append(group['key_data_info'])
                continue

        return ret_dict

# =================================================
#  Schema for 'show crypto gdoi gm rekey detail'
# =================================================
class ShowCryptoGdoiGmRekeyDetailSchema(MetaParser):
    """Schema for show crypto gdoi gm rekey detail"""
    schema = {
        'gdoi_group':{
            Any(): {
                    'rekeys_cumulative': int,
                    'rekeys_registration': int,
                    'rekey_acks_sent': int,
                    'rekey_sa_information': {
                        Any(): {
                            'dst': str,
                            'src': str,
                            'conn_id': str,
                            'my_cookie': str,
                            'his_cookie': str                            
                        }
                    }
                }
            }
        }

# =================================================
#  Parser for 'show crypto gdoi gm rekey detail'
# =================================================
class ShowCryptoGdoiGmRekeyDetail(ShowCryptoGdoiGmRekeyDetailSchema):
    """Parser for show crypto gdoi gm rekey detail"""

    cli_command = ['show crypto gdoi gm rekey detail']
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # Group bw6000 (Unicast)
        p1 = re.compile(r'^Group\s*(?P<group_name>\S+)\s*\(Unicast\)$')

        # Number of Rekeys received (cumulative)       : 0
        p2 = re.compile(r'^Number\s*of\s*Rekeys\s*received\s*\(cumulative\)\s*:\s*(?P<rekeys_cumulative>\d+)$')

        # Number of Rekeys received after registration : 0
        p3 = re.compile(r'^Number\s*of\s*Rekeys\s*received\s*after\s*registration\s*:\s*(?P<rekeys_registration>\d+)$')

        # Number of Rekey Acks sent                    : 0
        p4 = re.compile(r'^Number\s*of\s*Rekey\s*Acks\s*sent\s*:\s*(?P<rekey_acks_sent>\d+)$')
        
        # New     : 41.41.41.1      15.15.15.1       44327   14C40DC1   88AD3ACA
        p5 = re.compile(r'^(?P<state>(New|Current|Previous))\s*:\s*(?P<dst>[\S]+)\s*(?P<src>[\S]+)\s*(?P<conn_id>[\S]+)\s*(?P<my_cookie>[\S]+)\s*(?P<his_cookie>[\S]+)$')
        

        for line in output.splitlines():
            line = line.strip()

            # Group bw6000 (Unicast)
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('gdoi_group', {}).setdefault(group_name, {})
                continue

            # Number of Rekeys received (cumulative)       : 0
            m = p2.match(line)
            if m:
                group_name_dict['rekeys_cumulative'] = int(m.groupdict()['rekeys_cumulative'])
                continue
        
            # Number of Rekeys received after registration : 0
            m = p3.match(line)
            if m:
                group_name_dict['rekeys_registration'] = int(m.groupdict()['rekeys_registration'])                       
                continue
        
            # Number of Rekey Acks sent                    : 0
            m = p4.match(line)
            if m:
                group_name_dict['rekey_acks_sent'] = int(m.groupdict()['rekey_acks_sent'])  
                continue

            # Rekey (KEK) SA information :
            m = p5.match(line)
            if m:
                state = m.groupdict()['state']             
                rekey_data_dict = group_name_dict.setdefault('rekey_sa_information', {}).setdefault(state, {})
                rekey_data_dict['dst'] = m.groupdict()['dst']
                rekey_data_dict['src'] = m.groupdict()['src']
                rekey_data_dict['conn_id'] = m.groupdict()['conn_id']
                rekey_data_dict['my_cookie'] = m.groupdict()['my_cookie']
                rekey_data_dict['his_cookie'] = m.groupdict()['his_cookie']                                              
                continue

        
        return ret_dict        

# =================================================
#  Schema for 'show crypto gdoi ks coop detail'
# =================================================
class ShowCryptoGdoiKsCoopDetailSchema(MetaParser):
    """schema for show crypto gdoi ks coop detail"""
    schema = {
        'crypto_gdoi_group_name': {
            Any(): {
                'group_handle': int,
                'local_key_server_handle': int,
                Optional('redundancy_state'): str,
                Optional('local_address'): str,
                Optional('local_priority'): int,
                Optional('local_ks_role'): str,
                Optional('local_ks_status'): str,
                Optional('local_ks_version'): str,
                Optional('local_coop_version'): str,
                Optional('primary_timers'): {
                    Optional('primary_refresh_policy_time'): int,
                    Optional('remaining_time'): int,
                    Optional('per_user_timer_remaining_time'): int,
                    Optional('antireplay_sequence_number'): int,
                },
                Optional('secondary_timers'): {
                    Optional('sec_primary_periodic_time'): int,
                    Optional('remaining_time'): int,
                    Optional('retries'): int,
                    Optional('invalid_ann_pst_recvd'): int,
                    Optional('new_gm_temp_blk_enforced'): str,
                    Optional('per_user_timer_remaining_time'): int,
                    Optional('antireplay_sequence_number'): int,
                },
                Optional(Any()): {
                    Optional('server_handle'): int,
                    Optional('peer_address'): str,
                    Optional('peer_version'): str,
                    Optional('peer_coop_version'): str,
                    Optional('coop_protocol'): str,
                    Optional('peer_priority'): int,
                    Optional('peer_ks_role'): str,
                    Optional('peer_ks_status'): str,
                    Optional('antireplay_sequence_number'): int,
                    Optional('ike_status'): str,
                    Optional('counters'): {
                        Optional('ann_msgs_sent'): int,
                        Optional('ann_msgs_sent_with_reply_request'): int,
                        Optional('ann_msgs_recv'): int,
                        Optional('ann_msgs_recv_with_reply_request'): int,
                        Optional('packet_sent_drops'): int,
                        Optional('packet_recv_drops'): int,
                        Optional('total_bytes_sent'): int,
                        Optional('total_bytes_recv'): int
                    }
                }
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks coop detail'
# ===================================================
class ShowCryptoGdoiKsCoopDetail(ShowCryptoGdoiKsCoopDetailSchema):
    """Parser for show crypto gdoi ks coop detail"""
    cli_command = 'show crypto gdoi ks coop detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Crypto Gdoi Group Name :g1
        p1 = re.compile(r'^Crypto\s+Gdoi\s+Group\s+Name +:(?P<crypto_gdoi_group_name>\S+)$')
        # Group handle: 1073741826, Local Key Server handle: 1073741826
        p2 = re.compile(r'^Group\s+handle:\s+(?P<group_handle>\d+),\s+Local\s+Key\s+Server\s+handle:\s+(?P<local_key_server_handle>\d+)$')
        # *NO* redundancy configured for this group
        p3 = re.compile(r'\*(?P<redundancy_state>NO)\*\s+redundancy\s+configured\s+for\s+this\s+group')
        # Local Address: 10.78.106.116
        p4 = re.compile(r'^Local\s+Address:\s+(?P<local_address>\S+)$')
        # Local Priority: 100
        p5 = re.compile(r'^Local\s+Priority:\s+(?P<local_priority>\d+)$')
        # Local KS Role: Primary , Local KS Status: Alive
        p6 = re.compile(r'^Local\s+KS\s+Role:\s+(?P<local_ks_role>\w+)\s+,\s+Local\s+KS\s+Status:\s+(?P<local_ks_status>\w+)$')
        # Local KS version: 1.0.27
        p7 = re.compile(r'^Local\s+KS\s+version:\s+(?P<local_ks_version>\S+)$')
        # Local COOP version: 1.0.8
        p8 = re.compile(r'^Local\s+COOP\s+version:\s+(?P<local_coop_version>\S+)$')
        # Primary Refresh Policy Time: 20
        p9 = re.compile(r'^Primary\s+Refresh\s+Policy\s+Time:\s+(?P<primary_refresh_policy_time>\d+)$')
        # Remaining Time: 14
        p10 = re.compile(r'^Remaining\s+Time:\s+(?P<remaining_time>\d+)$')
        # Per-user timer remaining time: 0
        p11 = re.compile(r'^Per-user\s+timer\s+remaining\s+time:\s+(?P<per_user_timer_remaining_time>\d+)$')
        # Antireplay Sequence Number: 79
        p12 = re.compile(r'^Antireplay\s+Sequence\s+Number:\s+(?P<antireplay_sequence_number>\d+)$')
        # Session 1:
        p13 = re.compile(r'^Session\s+(?P<session_id>\d+):$')
        # Server handle: 1073741827
        p14 = re.compile(r'^Server\s+handle:\s+(?P<server_handle>\d+)$')
        # Peer Address: 10.78.106.117
        p15 = re.compile(r'^Peer\s+Address:\s+(?P<peer_address>\S+)$')
        # Peer Version: 1.0.27
        p16 = re.compile(r'^Peer\s+Version:\s+(?P<peer_version>\S+)$')
        # Peer COOP version: 1.0.8
        p17 = re.compile(r'^Peer\s+COOP\s+version:\s+(?P<peer_coop_version>\S+)$')
        # COOP Protocol: base
        p18 = re.compile(r'^COOP\s+Protocol:\s+(?P<coop_protocol>\S+)$')
        # Peer Priority: 90
        p19 = re.compile(r'^Peer\s+Priority:\s+(?P<peer_priority>\d+)$')
        # Peer KS Role: Secondary , Peer KS Status: Alive
        p20 = re.compile(r'^Peer\s+KS\s+Role:\s+(?P<peer_ks_role>\w+)\s+,\s+Peer\s+KS\s+Status:\s+(?P<peer_ks_status>\w+)$')
        # IKE status: Established
        p21 = re.compile(r'^IKE\s+status:\s+(?P<ike_status>\w+)$')
        # Ann msgs sent: 122
        p22 = re.compile(r'^Ann\s+msgs\s+sent:\s+(?P<ann_msgs_sent>\d+)$')
        # Ann msgs sent with reply request: 1
        p23 = re.compile(r'^Ann\s+msgs\s+sent\s+with\s+reply\s+request:\s+(?P<ann_msgs_sent_with_reply_request>\d+)$')
        # Ann msgs recv: 4
        p24 =  re.compile(r'^Ann\s+msgs\s+recv:\s+(?P<ann_msgs_recv>\d+)$')
        # Ann msgs recv with reply request: 1
        p25 = re.compile(r'^Ann\s+msgs\s+recv\s+with\s+reply\s+request:\s+(?P<ann_msgs_recv_with_reply_request>\d+)$')
        # Packet sent drops: 1
        p26 = re.compile(r'^Packet\s+sent\s+drops:\s+(?P<packet_sent_drops>\d+)$')
        # Packet Recv drops: 0
        p27 = re.compile(r'^Packet\s+Recv\s+drops:\s+(?P<packet_recv_drops>\d)$')
        # Total bytes sent: 104495
        p28 = re.compile(r'^Total\s+bytes\s+sent:\s+(?P<total_bytes_sent>\d+)$')
        # Total bytes recv: 2130
        p29 = re.compile(r'^Total\s+bytes\s+recv:\s+(?P<total_bytes_recv>\d+)$')
        # Sec Primary Periodic Time: 30
        p30 = re.compile(r'^Sec Primary.*: +(?P<sec_primary_periodic_time>\d+)$')
        # Remaining Time: 11, Retries: 0
        p31 = re.compile(r'^Remaining Time: +(?P<remaining_time>\d+), +Retries: +(?P<retries>\d+)$')
        # Invalid ANN PST recvd: 0
        p32 = re.compile(r'^Invalid.*: +(?P<invalid_ann_pst_recvd>\d+)$')
        # New GM Temporary Blocking Enforced?: No
        p33 = re.compile(r'^New.*?: +(?P<new_gm_temp_blk_enforced>\w+)$')

        ret_dict = {}
        reply_num = 0
        for line in output.splitlines():
            line = line.strip()
            # Crypto Gdoi Group Name :g1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group_id = group['crypto_gdoi_group_name']
                crypto_gdoi_group = ret_dict.setdefault('crypto_gdoi_group_name', {}).setdefault(crypto_gdoi_group_id, {})
                reply_num = 0
                continue

            # Group handle: 1073741826, Local Key Server handle: 1073741826
            m = p2.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'group_handle': int(group['group_handle'])})
                crypto_gdoi_group.update({'local_key_server_handle': int(group['local_key_server_handle'])})
                continue

            # *NO* redundancy configured for this group
            m = p3.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'redundancy_state': group['redundancy_state']})
                continue

            # Local Address: 10.78.106.116
            m = p4.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_address': group['local_address']})
                continue

            # Local Priority: 100
            m = p5.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_priority': int(group['local_priority'])})
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p6.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_ks_role': group['local_ks_role']})
                crypto_gdoi_group.update({'local_ks_status': group['local_ks_status']})
                continue

            # Local KS version: 1.0.27
            m = p7.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_ks_version': group['local_ks_version']})
                continue

            # Local COOP version: 1.0.8
            m = p8.match(line)
            if m:
                group = m.groupdict()
                crypto_gdoi_group.update({'local_coop_version': group['local_coop_version']})
                continue

            # Primary Refresh Policy Time: 20
            m = p9.match(line)
            if m:
                group = m.groupdict()
                primary_timer_dict = crypto_gdoi_group.setdefault('primary_timers', {})
                primary_timer_dict.update({'primary_refresh_policy_time': int(group['primary_refresh_policy_time'])})
                continue

            # Sec Primary Periodic Time: 30
            m = p30.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict = crypto_gdoi_group.setdefault('secondary_timers', {})
                secondary_timer_dict.update({'sec_primary_periodic_time': int(group['sec_primary_periodic_time'])})
                continue

            # Remaining Time: 11, Retries: 0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                secondary_timer_dict.update(group)
                continue

            # Invalid ANN PST recvd: 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict.update({'invalid_ann_pst_recvd': int(group['invalid_ann_pst_recvd'])})
                continue

            # New GM Temporary Blocking Enforced?: No
            m = p33.match(line)
            if m:
                group = m.groupdict()
                secondary_timer_dict.update(group)
                continue

            # Remaining Time: 14
            m = p10.match(line)
            if m:
                group = m.groupdict()
                primary_timer_dict.update({'remaining_time': int(group['remaining_time'])})
                continue

            # Per-user timer remaining time: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if 'primary_timers' in crypto_gdoi_group:
                    primary_timer_dict.update({'per_user_timer_remaining_time': int(group['per_user_timer_remaining_time'])})
                elif 'secondary_timers' in crypto_gdoi_group:
                    secondary_timer_dict.update({'per_user_timer_remaining_time': int(group['per_user_timer_remaining_time'])})
                continue

            # Antireplay Sequence Number: 124
            m = p12.match(line)
            if (reply_num == 0):
                if m:
                    group = m.groupdict()
                    if 'primary_timers' in crypto_gdoi_group:
                        primary_timer_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    elif 'secondary_timers' in crypto_gdoi_group:
                        secondary_timer_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    reply_num += 1
                    continue

            # Session 1:
            m = p13.match(line)
            if m:
                group = m.groupdict()
                session_id = group['session_id']
                session_dict = ret_dict.setdefault('crypto_gdoi_group_name', {}).setdefault(crypto_gdoi_group_id,\
                        {}).setdefault(session_id, {})
                continue

            # Server handle: 1073741827
            m = p14.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'server_handle': int(group['server_handle'])})
                continue

            # Peer Address: 10.78.106.117
            m = p15.match(line)
            if m:
                group =m.groupdict()
                session_dict.update({'peer_address': group['peer_address']})
                continue

            # Peer Version: 1.0.27
            m = p16.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_version': group['peer_version']})
                continue

            # Peer COOP version: 1.0.8
            m = p17.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_coop_version': group['peer_coop_version']})
                continue

            # COOP Protocol: base
            m = p18.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'coop_protocol': group['coop_protocol']})
                continue

            # Peer Priority: 90
            m = p19.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_priority': int(group['peer_priority'])})
                continue

            # Peer KS Role: Secondary , Peer KS Status: Alive
            m = p20.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'peer_ks_role': group['peer_ks_role']})
                session_dict.update({'peer_ks_status': group['peer_ks_status']})
                continue

            # Antireplay Sequence Number: 5
            m = p12.match(line)
            if (reply_num == 1):
                if m:
                    group = m.groupdict()
                    session_dict.update({'antireplay_sequence_number': int(group['antireplay_sequence_number'])})
                    continue

            # IKE status: Established
            m = p21.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'ike_status': group['ike_status']})
                continue

            # Ann msgs sent: 122
            m = p22.match(line)
            if m:
                group = m.groupdict()
                counter_dict = session_dict.setdefault('counters', {})
                counter_dict.update({'ann_msgs_sent': int(group['ann_msgs_sent'])})
                continue

            # Ann msgs sent with reply request: 1
            m = p23.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_sent_with_reply_request': int(group['ann_msgs_sent_with_reply_request'])})
                continue

            # Ann msgs recv: 4
            m = p24.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_recv': int(group['ann_msgs_recv'])})
                continue

            #Ann msgs recv with reply request: 1
            m = p25.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'ann_msgs_recv_with_reply_request': int(group['ann_msgs_recv_with_reply_request'])})
                continue

            # Packet sent drops: 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'packet_sent_drops': int(group['packet_sent_drops'])})
                continue

            # Packet Recv drops: 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'packet_recv_drops': int(group['packet_recv_drops'])})
                continue

            # Total bytes sent: 104495
            m = p28.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'total_bytes_sent': int(group['total_bytes_sent'])})
                continue

            # Total bytes recv: 2130
            m = p29.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({'total_bytes_recv': int(group['total_bytes_recv'])})

        return ret_dict

# ======================================================================================
#  Schema for 'show crypto gdoi ks identifier' and 'show crypto gdoi ks identifier detail'
# ======================================================================================
class ShowCryptoGdoiKsIdentifierSchema(MetaParser):
    """schema for:
        show crypto gdoi ks identifier
        show crypto gdoi ks identifier detail
    """

    schema = {
        'ks_sender_info': {
            Any(): {
                'transform_mode': str,
                're_initializing': str,
                'sid_length': int,
                'current_kssid_in_use': str,
                'last_gmsid_used': str,
                Optional('kssid_assigned'): str,
                Optional('kssid_used'): str,
                Optional('kssid_used_old'): str,
                Optional('available_kssid'): str,
                Optional('remining_sid'): str
            }
        }
    }

# ======================================================================================
#  Parser for 'show crypto gdoi ks identifier' and 'show crypto gdoi ks identifier detail'
# ======================================================================================
class ShowCryptoGdoiKsIdentifierSuperParser(ShowCryptoGdoiKsIdentifierSchema):
    ''' Parser for:
        show crypto gdoi ks identifier
        show crypto gdoi ks identifier detail
    '''

    def cli(self, output = None):

        res_dict = {}

        # KS Sender ID (KSSID) Information for Group bw6000:
        p1 = re.compile(r'^KS\s+Sender\s+ID\s+\(KSSID\)\s+Information\s+for\s+Group\s+(?P<ks_sender_id>\S+):$')
        # Transform Mode           : Non-Counter (Non-Suite-B)
        p2 = re.compile(r'^Transform\s+Mode\s+:\s+(?P<transform_mode>\S+)\s+\(\S+\)$')
        # Re-initializing          : No
        p3 = re.compile(r'^Re-initializing\s+:\s+(?P<re_initializing>\w+)$')
        # SID Length (Group Size)  : 24 bits (MEDIUM)
        p4 = re.compile(r'^SID\s+Length\s+\(Group\s+Size\)\s+:\s+(?P<sid_length>\d+)\s+bits\s+\(\S+\)$')
        # Current KSSID In-Use     : none
        p5 = re.compile(r'^Current KSSID\s+In-Use\s+:\s+(?P<current_kssid_in_use>\S+)$')
        # Last GMSID Used          : none
        p6 = re.compile(r'^Last\s+GMSID\s+Used\s+:\s+(?P<last_gmsid_used>\S+)$')
        # KSSID(s) Assigned        : none
        p7 = re.compile(r'^KSSID\(s\)\s+Assigned\s+:\s+(?P<kssid_assigned>\S+)$')
        # KSSID(s) Used            : none
        p8 = re.compile(r'^KSSID\(s\)\s+Used\s+:\s+(?P<kssid_used>\S+)$')
        # KSSID(s) Used (Old)      : none
        p9 = re.compile(r'^KSSID\(s\)\s+Used\s+\(Old\)\s+:\s+(?P<kssid_used_old>\S+)$')
        # Available KSSID(s)       : none
        p10 = re.compile(r'^Available\s+KSSID\(s\)\s+:\s+(?P<available_kssid>\S+)$')
        # REMAINING SIDs: none
        p11 = re.compile(r'^REMAINING\s+SIDs:\s+(?P<remining_sid>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # KS Sender ID (KSSID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ks_sender_id = group['ks_sender_id']
                ks_dict = res_dict.setdefault('ks_sender_info', {}).setdefault(ks_sender_id, {})
                continue

            # Transform Mode           : Non-Counter (Non-Suite-B)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'transform_mode': group['transform_mode']})
                continue

            # Re-initializing          : No
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'re_initializing': group['re_initializing']})
                continue

            # SID Length (Group Size)  : 24 bits (MEDIUM)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'sid_length': int(group['sid_length'])})
                continue

            # Current KSSID In-Use     : none
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'current_kssid_in_use': group['current_kssid_in_use']})
                continue

            # Last GMSID Used          : none
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'last_gmsid_used': group['last_gmsid_used']})
                continue

            # KSSID(s) Assigned        : none
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_assigned': group['kssid_assigned']})
                continue

            # KSSID(s) Used            : none
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_used': group['kssid_used']})
                continue

            # KSSID(s) Used (Old)      : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'kssid_used_old': group['kssid_used_old']})
                continue

            # Available KSSID(s)       : none
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'available_kssid': group['available_kssid']})
                continue

            # REMAINING SIDs: none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ks_dict.update({'remining_sid': group['remining_sid']})
                continue

        return res_dict


class ShowCryptoGdoiKsIdentifier(ShowCryptoGdoiKsIdentifierSuperParser):
    ''' Parser for:
        show crypto gdoi ks identifier
    '''
    cli_command = 'show crypto gdoi ks identifier'

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowCryptoGdoiKsIdentifierDetail(ShowCryptoGdoiKsIdentifierSuperParser):
    ''' Parser for:
        show crypto gdoi ks identifier detail
    '''
    cli_command = 'show crypto gdoi ks identifier detail'

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# ===================================================
#  Schema for 'show crypto gdoi gm identifier detail'
# ===================================================

class ShowCryptoGdoiGmIdentifierDetailSchema(MetaParser):
    """Schema for show crypto gdoi gm identifier detail"""

    schema = {
        'group': {
            Any(): {
                Any(): {
                    'vrf_name': str,
                    'transform_mode': str,
                    'transform_name': str,
                    'no_of_sid': int,
                    'current_sid': str,
                    'next_sid_request': {
                        'tek_lifetime_sec': int,
                        'sid_length': int,
                        'sid_group_size': str
                    }
                }   
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi gm identifier detail'
# ===================================================

class ShowCryptoGdoiGmIdentifierDetail(ShowCryptoGdoiGmIdentifierDetailSchema):
    """Parser for show crypto gdoi gm identifier detail"""

    cli_command = ['show crypto gdoi gm identifier detail'] 

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # GM Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^GM Sender ID \(SID\) Information for Group\s*(?P<group_name>\S+):$')

        # Group Member: 44.44.44.1       vrf: None
        p2 = re.compile(r'^Group Member:\s*(?P<group_member>[\S]+)\s*vrf:\s*(?P<vrf_name>[\S]+)$')

        # Transform Mode                  : Non-Counter (Non-Suite-B)
        p3 = re.compile(r'^Transform Mode\s*:\s*(?P<transform_mode>[\w-]*)\s*\((?P<transform_name>[\w-]*)\)$')

        # of SIDs Last Requested        : 0
        p4 = re.compile(r'^# of SIDs Last Requested\s*:\s*(?P<no_of_sid>[\d]+)$')

        # CURRENT SIDs: None
        p5 = re.compile(r'^CURRENT SIDs:\s*(?P<current_sid>[\S]+)$')

        # TEK Lifetime                  : 4873 sec
        p6 = re.compile(r'^TEK Lifetime\s*:\s*(?P<tek_lifetime>[\w]+)\s*sec$')

        # SID Length (Group Size)       : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\)\s*:\s*(?P<sid_length>[\d]+)\s*bits\s*\((?P<group_size>[\w]+)\)$')        

        for line in output.splitlines():
            line = line.strip()

            # GM Sender ID (SID) Information for Group bw6000:
            m = p1.match(line)
            if m:
                group_name = m.groupdict()['group_name']
                group_name_dict = ret_dict.setdefault('group',{}).setdefault(group_name,{})
                continue

            # Group Member: 44.44.44.1       vrf: None
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict = group_name_dict.setdefault(groups['group_member'],{})
                group_member_dict.update({'vrf_name': groups['vrf_name']})
                continue
        

            # Transform Mode                  : Non-Counter (Non-Suite-B)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue

            # of SIDs Last Requested        : 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                groups = {k: int(v) for k, v in groups.items()}
                group_member_dict.update(groups)
                continue

            # CURRENT SIDs: None
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                group_member_dict.update(groups)
                continue        
        
            # TEK Lifetime                  : 4873 sec
            m = p6.match(line)
            if m:
                next_sid_request_dict = group_member_dict.setdefault('next_sid_request', {})
                next_sid_request_dict['tek_lifetime_sec'] = int(m.groupdict()['tek_lifetime'])
                continue                
 
            # SID Length (Group Size)       : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                next_sid_request_dict['sid_length'] = int(m.groupdict()['sid_length'])
                next_sid_request_dict['sid_group_size'] = m.groupdict()['group_size']
                continue                
     
        return ret_dict


# ==============================
# Schema for
#   'show crypto gdoi ks coop identifier detail'
# ==============================

class ShowCryptoGdoiKsCoopIdentifierDetailSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks coop identifier detail'
    """
    schema = {
        'group': {
            Any():{
                Or('local', 'peer'): {
                    'ks_role': str,
                    'ks_status': str,
                    'address': str,
                    'next_sid_client_operation': str,
                    're_initializing': str,
                    'kssid_overlap': str,
                    'sid_length_cfg': str,
                    'sid_length_used': str,
                    'current_kssid_inuse': str,
                    'kssids_assigned': str,
                    'kssids_used': str,
                    'old_kssids_used': str
                }
            }
        }
    }

# ========================================================
#  Parser for 'show crypto gdoi ks coop identifier detail'
# ========================================================

class ShowCryptoGdoiKsCoopIdentifierDetail(ShowCryptoGdoiKsCoopIdentifierDetailSchema):
    
    """Parser for 'show crypto gdoi ks coop identifier detail'"""
    
    cli_command = 'show crypto gdoi ks coop identifier detail'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # COOP-KS Sender ID (SID) Information for Group g1:
        p1 = re.compile(r'^COOP-KS Sender ID \(SID\) Information for Group (?P<group>[\w\d\-]+):$')

        # Local KS Role: Primary , Local KS Status: Alive
        p2 = re.compile(r'^Local KS Role:\s+(?P<ks_role>[\w]+)\s+\,\s+Local KS Status:\s+(?P<ks_status>[\w]+)$')

        # Local Address : 10.78.106.116
        p3 = re.compile(r'^Local Address\s+:\s+(?P<address>\d+\.\d+\.\d+\.\d+)$')

        # Next SID Client Operation : NOTIFY
        p4 = re.compile(r'^Next SID Client Operation\s+:\s+(?P<next_sid_client_operation>[A-Z]+)$')

        # Re-initializing : No
        p5 = re.compile(r'^Re-initializing\s+:\s+(?P<re_initializing>[\w]+)$')

        # KSSID Overlap : No
        p6 = re.compile(r'^KSSID Overlap\s+:\s+(?P<kssid_overlap>[\w]+)$')

        # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\) Cfg\s+:\s+(?P<sid_length_cfg>[\s\w\(\)]+)$')

        # SID Length (Group Size) Used : 24 bits (MEDIUM)
        p8 = re.compile(r'^SID Length \(Group Size\) Used\s+:\s+(?P<sid_length_used>[\s\w\(\)]+)$')

        # Current KSSID In-Use : none
        p9 = re.compile(r'^Current KSSID In-Use\s+:\s+(?P<current_kssid_inuse>[a-z]+)$')

        # KSSID(s) Assigned : none
        p10 = re.compile('^KSSID\(s\) Assigned\s+:\s+(?P<kssids_assigned>[a-z]+)$')

        # KSSID(s) Used : none
        p11 = re.compile('^KSSID\(s\) Used\s+:\s+(?P<kssids_used>[a-z]+)$')

        # Old KSSID(s) Used : none
        p12 = re.compile('^Old KSSID\(s\) Used\s+:\s+(?P<old_kssids_used>[a-z]+)$')

        # Peer KS Role: Secondary , Peer KS Status: Alive
        p13 = re.compile('^Peer KS Role:\s+(?P<ks_role>[\w]+)\s\, Peer KS Status:\s+(?P<ks_status>[\w]+)$')

        # Peer Address : 10.78.106.117
        p14 = re.compile('^Peer Address\s+:\s+(?P<address>\d+\.\d+\.\d+\.\d+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            # GCOOP-KS Sender ID (SID) Information for Group g1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                local_dict = group_dict.setdefault('local', {})
                target_dict = local_dict
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p2.match(line)
            if m:
                group = m.groupdict()                    
                target_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Local Address : 10.78.106.116
            m = p3.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'address': group['address']})
                continue

            # Next SID Client Operation : NOTIFY
            m = p4.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'next_sid_client_operation': group['next_sid_client_operation']})
                continue

            # Re-initializing : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'re_initializing': group['re_initializing']})
                continue

            # KSSID Overlap : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'kssid_overlap': group['kssid_overlap']})
                continue

            # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'sid_length_cfg': group['sid_length_cfg']})
                continue

            # SID Length (Group Size) Used : 24 bits (MEDIUM)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'sid_length_used': group['sid_length_used']})
                continue

            # Current KSSID In-Use : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'current_kssid_inuse': group['current_kssid_inuse']})
                continue
            # KSSID(s) Assigned : none
            m = p10.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'kssids_assigned': group['kssids_assigned']})
                continue

            # KSSID(s) Used : none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'kssids_used': group['kssids_used']})
                continue

            # Old KSSID(s) Used : none
            m = p12.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'old_kssids_used': group['old_kssids_used']})
                continue

            # Peer KS Role: Secondary , Peer KS Status: Alive
            m = p13.match(line)
            if m:
                group = m.groupdict(line)
                target_dict = group_dict.setdefault('peer', {})
                target_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Peer Address : 10.78.106.117
            m = p14.match(line)
            if m:
                group = m.groupdict(line)
                target_dict.update({'address': group['address']})
                continue
 
        return master_dict

# ==============================
# Schema for 'show crypto ikev2 stats psh'
# ==============================

class ShowCryptoIkev2StatsPshSchema(MetaParser):
    """
    Schema for
        * 'show crypto ikev2 stats psh'
    """
    schema = {
         'ikev2_stats_psh':{
            'psh_requested': int,
            'psh_request_success': int,
            'psh_return_requested': int,
            'psh_return_success': int
        }
    }


# ========================================================
#  Parser for 'show crypto ikev2 stats psh'
# ========================================================

class ShowCryptoIkev2StatsPsh(ShowCryptoIkev2StatsPshSchema):
    
    """Parser for 'show crypto ikev2 stats psh'"""
    
    cli_command = 'show crypto ikev2 stats psh'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # ------------------IKEV2 PSH STATS----------------------
        p1 = re.compile(r'-+IKEV2 PSH STATS-+')

        # ikev2 psh requested: 99
        p2 = re.compile(r'^ikev2 psh requested:\s+(?P<psh_requested>\d+)$')

        # ikev2 psh request success: 99
        p3 = re.compile(r'^ikev2 psh request success:\s+(?P<psh_request_success>\d+)$')

        # ikev2 psh return requested: 92
        p4 = re.compile(r'^ikev2 psh return requested:\s+(?P<psh_return_requested>\d+)$')

        # ikev2 psh return success: 92
        p5 = re.compile(r'^ikev2 psh return success:\s+(?P<psh_return_success>\d+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            #  ------------------IKEV2 PSH STATS----------------------
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ike_dict = master_dict.setdefault('ikev2_stats_psh', {})
                continue

            # ikev2 psh requested: 99
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ike_dict.update({'psh_requested': int(group['psh_requested'])})
                continue

            # ikev2 psh request success: 99
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ike_dict.update({'psh_request_success': int(group['psh_request_success'])})
                continue

            # ikev2 psh return requested: 92
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ike_dict.update({'psh_return_requested': int(group['psh_return_requested'])})
                continue

            # ikev2 psh return success: 92
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ike_dict.update({'psh_return_success': int(group['psh_return_success'])})
                continue
                
        return master_dict

# ==================================
# Schema for
#   'show crypto gdoi feature set'
# ==================================
class ShowCryptoGdoiFeatureSetSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi feature'
    """

    schema = {
        'group': {
            Any():{
                'key_server':{
                    Any():{
                        'key_server_id': str,
                        'key_version': str,
                        'key_feature_supported': str
                    },
                },
                'group_member':{
                    Any():{
                        'group_member_id': str,
                        'group_member_version': str,
                        'group_feature_supported': str
                    },                   
                },
            },
        },
    }


# =================================================
#  Parser for 'show crypto gdoi feature set'
# =================================================

class ShowCryptoGdoiFeatureSet(ShowCryptoGdoiFeatureSetSchema):
    
    """Parser for 'show crypto gdoi feature' """
    
    cli_command = 'show crypto gdoi feature'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Group Name: bw6000
        p1 = re.compile(r'^Group Name:\s(?P<group>[\S]+)$')

        #     Key Server ID       Version   Feature Supported
        p2 = re.compile(r'Key Server ID \s+Version\s+Feature\sSupported')

        #         15.15.15.1          1.0.27         Yes
        p3 = re.compile(r'(?P<key_server_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<key_version>[\d\.]+)\s+(?P<key_feature_supported>[\w]+)$')

        #    Group Member ID     Version   Feature Supported
        p4 = re.compile(r'Group Member ID\s+Version\s+Feature\sSupported')

        #         25.25.25.1          1.0.25         Yes
        p5 = re.compile(r'(?P<group_member_id>\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})\s+(?P<group_member_version>[\d\.]+)\s+(?P<group_feature_supported>[\w]+)$')

        master_dict = {}
        server_flag = False
        member_flag = False
        for line in output.splitlines():

            line = line.strip()
            
            # Group Name: bw6000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                continue
                
            #     Key Server ID       Version   Feature Supported
            m = p2.match(line)
            if m:
                group = m.groupdict()
                server_dict = group_dict.setdefault('key_server', {})
                server_flag = True
                continue

            #         1.1.1.1          1.0.27         Yes
            if server_flag:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ser_count_dict = server_dict.setdefault(len(server_dict)+1, {})
                    ser_count_dict.update({'key_server_id': group['key_server_id']})
                    ser_count_dict.update({'key_version': group['key_version']})
                    ser_count_dict.update({'key_feature_supported': group['key_feature_supported']})                    
                    continue

            #    Group Member ID     Version   Feature Supported
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_member_dict = group_dict.setdefault('group_member', {})
                server_flag = False
                member_flag = True
                continue

            #        3.3.1.1          1.0.26         Yes
            if member_flag:
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    count_dict = group_member_dict.setdefault(len(group_member_dict)+1, {})
                    count_dict.update({'group_member_id' : group['group_member_id']})
                    count_dict.update({'group_member_version': group['group_member_version']})
                    count_dict.update({'group_feature_supported': group['group_feature_supported']})
                    continue
                       
        return master_dict

# =================================================
#  Parser for 'show crypto gdoi feature crl-check'
# =================================================
class ShowCryptoGdoiFeatureCrlCheck(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature crl-check'
    '''

    cli_command = "show crypto gdoi feature crl-check"

# =================================================
#  Parser for 'show crypto gdoi feature cts-sgt'
# =================================================
class ShowCryptoGdoiFeatureCtsSgt(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature cts-sgt'
    '''

    cli_command = "show crypto gdoi feature cts-sgt"

# =================================================
#  Parser for 'show crypto gdoi feature gikev2'
# =================================================
class ShowCryptoGdoiFeatureGikev2(ShowCryptoGdoiFeatureSet):
    '''Parser for:
        * 'show crypto gdoi feature gikev2'
    '''

    cli_command = "show crypto gdoi feature gikev2"

# ========================================
# Schema for
#   'show crypto gdoi ks coop identifier'
# ========================================

class ShowCryptoGdoiKsCoopIdentifierSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks coop identifier'
    """
    schema = {
        'group': {
            Any():{
                'local': {
                    'ks_role': str,
                    'ks_status': str,
                    'address': str,
                    'next_sid_client_operation': str,
                    're_initializing': str,
                    'kssid_overlap': str,
                    'sid_length_cfg': str,
                    'sid_length_used': str,
                    'current_kssid_inuse': str,
                    'kssids_assigned': str,
                    'kssids_used': str,
                    'old_kssids_used': str
                }
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks coop identifier'
# ===================================================

class ShowCryptoGdoiKsCoopIdentifier(ShowCryptoGdoiKsCoopIdentifierSchema):
    
    """Parser for show crypto gdoi ks coop identifier """
    
    cli_command = 'show crypto gdoi ks coop identifier'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # COOP-KS Sender ID (SID) Information for Group bw6000:
        p1 = re.compile(r'^COOP-KS Sender ID \(SID\) Information for Group (?P<group>[\w\d\-]+):$')

        # Local KS Role: Primary   , Local KS Status: Alive
        p2 = re.compile(r'^Local KS Role: (?P<ks_role>[\w]+)\s*\, Local KS Status: (?P<ks_status>[\w]+)$')

        # Local Address                : 15.15.15.1
        p3 = re.compile(r'^Local Address\s*: (?P<address>\d+\.\d+\.\d+\.\d+)$')

        # Next SID Client Operation    : NOTIFY
        p4 = re.compile(r'^Next SID Client Operation\s*: (?P<next_sid_client_operation>[A-Z]+)$')

        # Re-initializing              : No
        p5 = re.compile(r'^Re-initializing\s*: (?P<re_initializing>[\w]+)$')

        # KSSID Overlap                : No
        p6 = re.compile(r'^KSSID Overlap\s*: (?P<kssid_overlap>[\w]+)$')

        # SID Length (Group Size) Cfg  : 24 bits (MEDIUM)
        p7 = re.compile(r'^SID Length \(Group Size\) Cfg\s*: (?P<sid_length_cfg>[\s\w\(\)]+)$')

        # SID Length (Group Size) Used : 24 bits (MEDIUM)
        p8 = re.compile(r'^SID Length \(Group Size\) Used\s*: (?P<sid_length_used>[\s\w\(\)]+)$')

        # Current KSSID In-Use         : none
        p9 = re.compile(r'^Current KSSID In-Use\s*: (?P<current_kssid_inuse>[a-z]+)$')

        # KSSID(s) Assigned            : none
        p10 = re.compile(r'^KSSID\(s\) Assigned\s*: (?P<kssids_assigned>[a-z]+)$')

        # KSSID(s) Used                : none
        p11 = re.compile(r'^KSSID\(s\) Used\s*: (?P<kssids_used>[a-z]+)$')

        # Old KSSID(s) Used            : none
        p12 = re.compile(r'^Old KSSID\(s\) Used\s*: (?P<old_kssids_used>[a-z]+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()
            
            # GCOOP-KS Sender ID (SID) Information for Group g1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group', {}).setdefault(group['group'], {})
                local_dict = group_dict.setdefault('local', {})
                continue

            # Local KS Role: Primary , Local KS Status: Alive
            m = p2.match(line)
            if m:
                group = m.groupdict()                    
                local_dict.update({'ks_role': group['ks_role'], 'ks_status': group['ks_status']})
                continue

            # Local Address : 10.78.106.116
            m = p3.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'address': group['address']})
                continue

            # Next SID Client Operation : NOTIFY
            m = p4.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'next_sid_client_operation': group['next_sid_client_operation']})
                continue

            # Re-initializing : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'re_initializing': group['re_initializing']})
                continue

            # KSSID Overlap : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'kssid_overlap': group['kssid_overlap']})
                continue

            # SID Length (Group Size) Cfg : 24 bits (MEDIUM)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'sid_length_cfg': group['sid_length_cfg']})
                continue

            # SID Length (Group Size) Used : 24 bits (MEDIUM)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'sid_length_used': group['sid_length_used']})
                continue

            # Current KSSID In-Use : none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'current_kssid_inuse': group['current_kssid_inuse']})
                continue
                
            # KSSID(s) Assigned : none
            m = p10.match(line)
            if m:
                group = m.groupdict(line)
                local_dict.update({'kssids_assigned': group['kssids_assigned']})
                continue

            # KSSID(s) Used : none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                local_dict.update({'kssids_used': group['kssids_used']})
                continue

            # Old KSSID(s) Used : none
            m = p12.match(line)
            if m:
                group = m.groupdict(line)
                local_dict.update({'old_kssids_used': group['old_kssids_used']})
                continue
    
        return master_dict

# =================================================
#  Schema for 'show crypto gdio ipsec sa'
# =================================================
class ShowCryptogdoiIpsecSaSchema(MetaParser):
    """Schema for 'show crypto gdoi ipsec sa' """

    schema = {
        'sa_created_for_group': {
            Any():{
                'interface': {
                    Any():{
                        'protocol':{
                            Any():{
                                Any():{
                                    'local_ident': str,
                                    'local_port': int,
                                    'remote_ident': str,
                                    'remote_port': int,
                                    'direction': str,
                                    'replay':{
                                        'method': str,
                                        'window': int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =================================================
#  Parser for 'show crypto gdio ipsec sa'
# =================================================

class ShowCryptogdoiIpsecSa(ShowCryptogdoiIpsecSaSchema):

    """Parser for 'show crypto gdoi ipsec sa' """

    cli_command = 'show crypto gdoi ipsec sa'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #SA created for group getvpn1:
        p1 = re.compile(r'^SA +created +for +group (?P<sa_created_for_group>[\w\d]+):$')
        #   GigabitEthernat0/0/1:
        p2 = re.compile(r'(?P<interface>[\w\d\/]+):$')
        #protocol = ip
        p3 = re.compile(r'^protocol\s= (?P<protocol>\w{2,})$')
        #local ident  = 11.23.33.33, port = 0
        p4 = re.compile(r'^local.* +(?P<local_ident>[ANY|0-9\.\/]+), +port = (?P<port>[\d]+)$')
        #remote ident = 24.54.55.55, port = 0
        p5 = re.compile(r'^remote.* +(?P<remote_ident>[ANY|0-9\.\/]+), +port = (?P<remote_port>[\d]+)$')
        #direction: Both, replay(method/window): Counter/64
        p6 = re.compile(r'^direction: (?P<direction>[\w]+), +replay.*: +(?P<method>[\w]+)\/(?P<window>[\d]+)$')

        master_dict = {}

        for line in output.splitlines():

            line = line.strip()

            # SA created for group getvpn1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('sa_created_for_group', {}).setdefault(group['sa_created_for_group'], {})
                continue

            # GigabitEthernat0/0/1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inter_dict = group_dict.setdefault('interface', {}).setdefault(group['interface'], {})
                protocol_dict = inter_dict.setdefault('protocol', {})
                continue

            # protocol = ip
            m = p3.match(line)
            if m:
                group = m.groupdict()
                session_dict = protocol_dict.setdefault(group['protocol'], {})
                ident_dict = session_dict.setdefault(len(session_dict)+1, {})
                continue

            # local ident  = 11.23.33.33, port = 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'local_ident': group['local_ident'], 'local_port': int(group['port'])})
                continue

            # remote ident = 24.54.55.55, port = 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'remote_ident': group['remote_ident'], 'remote_port': int(group['remote_port'])})
                continue

            # direction: Both, replay(method/window): Counter/64
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ident_dict.update({'direction': group['direction']})
                replay_dict = ident_dict.setdefault('replay',{})
                replay_dict.update({'method': group['method'], 'window': int(group['window'])})
                continue

        return master_dict

# ========================================
# Schema for
#   'show crypto gdoi ks acl'
# ========================================
class ShowCryptoGdoiKsAclSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks acl'
    """
    schema = {
        "group_name": {
            Any(): {
                Optional("configured_acl"): list,
                Optional("configured_acl_locally"): list
            }
        }
    }

# ===================================================
#  Parser for 'show crypto gdoi ks acl'
# ===================================================
class ShowCryptoGdoiKsAcl(ShowCryptoGdoiKsAclSchema):
    """Parser for show crypto gdoi ks Acl """
    
    cli_command = 'show crypto gdoi ks acl'

    def cli(self, output = None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Group Name: bw6000
        p1 = re.compile(r"^Group Name: +(?P<group_name>[\d\S]+)$")

        # Configured ACL:
        p2 = re.compile(r"^Configured ACL:$")

        # Group Name               : getvpn1
        p3 = re.compile(r"^access-list .*$")

        # ACL Configured Locally:
        p4 = re.compile(r"^ACL Configured Locally:.*$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Group Name: bw6000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault('group_name', {}).setdefault(group['group_name'], {})
                continue

            # Configured ACL:
            m = p2.match(line)
            if m:
                acl_list = group_dict.setdefault('configured_acl', [])
                continue
            
            # Group Name               : getvpn1
            m = p4.match(line)
            if m:
                acl_list = group_dict.setdefault('configured_acl_locally', [])
                continue
            
            # ACL Configured Locally:
            m = p3.match(line)
            if m:
                acl_list.append(line)
                continue
    
        return master_dict

# ===================================================
#  Parser for 'show crypto gdoi gm acl local'
# ===================================================
class ShowCryptoGdoiGmAclLocal(ShowCryptoGdoiKsAcl):
    ''' Parser for:
        show crypto gdoi gm acl local
    '''
    cli_command = 'show crypto gdoi gm acl local'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# ========================================
# Schema for
#   'show crypto gdoi ks members'
# ========================================
class ShowCryptoGdoiKsMembersSchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks members'
    """
    schema = {
        "groups": {
            Any(): {
                "group_members": {
                    Any(): {
                        "gm_state": str,
                        "gm_version": str,
                        "group_id": int,
                        "group_name": str,
                        Optional("group_type"): str,
                        Optional("key_server_id"): str,
                        Optional("rcvd_seq_num"): {
                            Optional("seq1"): int,
                            Optional("seq2"): int,
                            Optional("seq3"): int,
                            Optional("seq4"): int,
                        },
                        "rekey_acks_missed": int,
                        "rekey_acks_rcvd": int,
                        "rekeys_retries": int,
                        "rekeys_sent": int,
                        Optional("sent_seq_num"): {
                            Optional("seq1"): int,
                            Optional("seq2"): int,
                            Optional("seq3"): int,
                            Optional("seq4"): int,
                        }
                    },
                },
                "last_rekey_duration": int,
                "rekeys_sent": int,
                "retransmits_num": int,
            },
        },
    }

# ===================================================
#  Parser for 'show crypto gdoi ks members'
# ===================================================
class ShowCryptoGdoiKsMembers(ShowCryptoGdoiKsMembersSchema):
    """Parser for show crypto gdoi ks members"""
    
    cli_command = 'show crypto gdoi ks members'
	
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Number of rekeys sent for group bw-suiteB-v6 : 0
        p2 = re.compile(r"^Number of rekeys sent for group +(?P<group_name>[\w\d\-]+).*: +(?P<rekeys_sent>\d+)$")

        # Number of retransmits during the last rekey for group bw-suiteB-v6 : 0
        p3 = re.compile(r"^Number of retransmits.* +(?P<group_name>[\w\d\-]+).*: +(?P<retransmits_num>\d+)$")

        # Duration of the last rekey for group bw-suiteB-v6 : 1 msec
        p4 = re.compile(r"^Duration.* +(?P<group_name>[\w\d\-]+).*: +(?P<last_rekey_duration>\d+) +msec$")

        # Group Member ID    : 44.44.44.1  GM Version: 1.0.25
        p5 = re.compile(r"^Group Member ID.*: +(?P<group_member_id>[\d\.]+).* +GM Version: +(?P<gm_version>[\d\.]+)$")

        # Group ID          : 2002
        p6 = re.compile(r"^Group ID.*: +(?P<group_id>[\d\.]+)$")

        # Group Name        : bw-suiteB-v6
        p7 = re.compile(r"^Group Name.*: +(?P<group_name>[\d\S]+)$")

        # Group Type        : GDOI (ISAKMP)
        p8 = re.compile(r"^Group Type.*: +(?P<group_type>[\s\S]+)$")

        # GM State          : Registered
        p9 = re.compile(r"^GM State.*: +(?P<gm_state>[\w]+)$")

        # Key Server ID     : 16.16.16.1
        p10 = re.compile(r"^Key Server ID.*: +(?P<key_server_id>[\d\.]+)$")

        # Rekeys sent       : 0
        p11 = re.compile(r"^Rekeys sent.*: +(?P<rekeys_sent>\d+)$")

        # Rekeys retries    : 0
        p12 = re.compile(r"^Rekeys retries.*: +(?P<rekeys_retries>\d+)$")

        # Rekey Acks Rcvd   : 0
        p13 = re.compile(r"^Rekey Acks Rcvd.*: +(?P<rekey_acks_rcvd>\d+)$")

        # Rekey Acks missed : 0
        p14 = re.compile(r"^Rekey Acks missed.*: +(?P<rekey_acks_missed>\d+)$")

        # Sent seq num : 0     0     0     0
        p15 = re.compile(r"^Sent seq num.*: +(?P<seq1>\d+) +(?P<seq2>\d+) +(?P<seq3>\d+) +(?P<seq4>\d+)$")

        # Rcvd seq num : 0     0     0     0
        p16 = re.compile(r"^Rcvd seq num.*: +(?P<seq1>\d+) +(?P<seq2>\d+) +(?P<seq3>\d+) +(?P<seq4>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Number of rekeys sent for group bw-suiteB-v6 : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_dict = master_dict.setdefault("groups", {}).setdefault(group['group_name'], {})
                group_dict.update({'rekeys_sent': int(group['rekeys_sent'])})
                continue
            
            # Number of retransmits during the last rekey for group bw-suiteB-v6 : 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group_dict.update({'retransmits_num': int(group['retransmits_num'])})
                continue
            
            # Duration of the last rekey for group bw-suiteB-v6 : 1 msec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group_dict.update({'last_rekey_duration': int(group['last_rekey_duration'])})
                continue
            
            # Group Member ID    : 44.44.44.1  GM Version: 1.0.25
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group_id_dict = group_dict.setdefault("group_members", {}).setdefault(group['group_member_id'], {})
                group_id_dict.update({"gm_version": group['gm_version']})
                continue

            # Group ID          : 2002
            m = p6.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Group Name        : bw-suiteB-v6
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Group Type        : GDOI (ISAKMP)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # GM State          : Registered
            m = p9.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Key Server ID     : 16.16.16.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                group_id_dict.update(group)
                continue

            # Rekeys sent       : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekeys retries    : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekey Acks Rcvd   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue

            # Rekey Acks missed : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                group_id_dict.update(group)
                continue
            
            # Sent seq num : 0     0     0     0    
            m = p15.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                sent_seq_dict = group_id_dict.setdefault("sent_seq_num", {})
                sent_seq_dict.update(group)
                continue

            # Rcvd seq num : 0     0     0     0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items()}
                rcvd_seq_dict = group_id_dict.setdefault("rcvd_seq_num", {})
                rcvd_seq_dict.update(group)
                continue
            
        return master_dict

# ===================================================
#  Parser for 'show crypto gdoi ks members ip {member_ip}'
# ===================================================
class ShowCryptoGdoiKsMembersIp(ShowCryptoGdoiKsMembers):
    ''' Parser for:
        show crypto gdoi ks members {member_ip}
    '''
    cli_command = 'show crypto gdoi ks members {member_ip}'

    def cli(self, member_ip='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)

# ========================================
# Schema for
#   'show crypto gdoi ks members summary'
# ========================================
class ShowCryptoGdoiKsMembersSummarySchema(MetaParser):
    """
    Schema for
        * 'show crypto gdoi ks members summary'
    """
    schema = {
        "group_member_information": {
            "groups": {
                Any(): {
                    "key_server_ids": {
                        Any(): {
                            Optional("gmdb_state"): str,
                            Optional("group_members"): int,
                            Optional("members"): {
                                Optional(Any()): {
                                    Optional("rekey_ack_missed"): int,
                                    Optional("rekey_sent"): int,
                                    Optional("version"): str,
                                }
                            },
                        },
                    },
                    "group_id": int,
                    "group_members": int,
                },
            },
        },
    }

# ========================================
#   Parser for 'show crypto gdoi ks members summary'
# ========================================
class ShowCryptoGdoiKsMembersSummary(ShowCryptoGdoiKsMembersSummarySchema):
    """Parser for show crypto gdoi ks members summary"""
    
    cli_command = 'show crypto gdoi ks members summary'
	
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Group Member Information :
        p1 = re.compile(r"^Group Member Information.*$")

        # Group Name: bw6000_eft, ID: 1122, Group Members: 2
        p2 = re.compile(r"^Group Name: +(?P<group_name>[\S]+), +ID: +(?P<group_id>\d+), +Group Members: +(?P<group_members>\d+)$")

        # Key Server ID: 16.16.16.1, GMDB state: REDUNDANT, Group Members: 1
        p3 = re.compile(r"^Key Server ID: +(?P<key_server_id>[\d\.]+), +GMDB state: +(?P<gmdb_state>\w+), +Group Members: +(?P<group_members>\d+)$")

        # 42.42.42.1   1.0.25         0               0
        p4 = re.compile(r"^(?P<member_id>[\d\.]+) +(?P<version>[\d\.]+) +(?P<rekey_sent>\d+) +(?P<rekey_ack_missed>\d+)$")

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Group Member Information :
            m = p1.match(line)
            if m:
                group_mem_dict = master_dict.setdefault("group_member_information", {}).setdefault("groups", {})
                continue
            
            # Group Name: bw6000_eft, ID: 1122, Group Members: 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_dict = group_mem_dict.setdefault(group['group_name'], {})
                group_dict.update({'group_id':int(group['group_id'])})
                group_dict.update({'group_members':int(group['group_members'])})
                continue
            
            # Key Server ID: 16.16.16.1, GMDB state: REDUNDANT, Group Members: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                key_server_id = group_dict.setdefault("key_server_ids", {}).setdefault(group['key_server_id'], {})
                key_server_id.update({'gmdb_state':group['gmdb_state']})
                key_server_id.update({'group_members':int(group['group_members'])})
                continue

            # 42.42.42.1   1.0.25         0               0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                memeber_dict = key_server_id.setdefault("members", {}).setdefault(group['member_id'], {})
                memeber_dict.update({'version':group['version']})
                memeber_dict.update({'rekey_sent':int(group['rekey_sent'])})
                memeber_dict.update({'rekey_ack_missed':int(group['rekey_ack_missed'])})
                continue
        return master_dict


# ========================================
# Schema for
#   'show crypto key mypubkey all'
#   'show crypto key mypubkey rsa'
#   'show crypto key mypubkey ec'
#   'show crypto key mypubkey rsa {key_name}'
#   'show crypto key mypubkey ec {key_name}'
# ========================================
class ShowCryptoKeyMypubkeyMasterSchema(MetaParser):
    """
    Schema for
        * 'show crypto key mypubkey all'
        * 'show crypto key mypubkey ec'
        * 'show crypto key mypubkey rsa'
        * 'show crypto key mypubkey ec {key_name}'
        * 'show crypto key mypubkey rsa {key_name}'
    """
    schema = {
        "keys": {
            Any(): {
                "key_name": str,
                "key_type": {
                    Any(): {
                        "key": str,
                        "key_data": list,
                        Optional("redundancy"): str,
                        Optional("storage_device"): str,
                        Optional("usage"): str
                    }
                },
                "keypairgen_time": str
            }
        }
    }

# ========================================
#   Parser for 'show crypto key mypubkey all'
# ========================================


class ShowCryptoKeyMypubkeyAll(ShowCryptoKeyMypubkeyMasterSchema):
    """Parser for show crypto key mypubkey all"""

    cli_command = 'show crypto key mypubkey all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # % Key pair was generated at: 06:51:40 UTC Aug 30 2022
        p1 = re.compile(r'^% Key pair.*: +(?P<keypairgen_time>[\S\s]+)$')

        # Key name: test
        p2 = re.compile(r'^Key name: +(?P<key_name>\S+)$')

        # Key type: RSA KEYS
        p3 = re.compile(r'^Key type: +(?P<key_type>[\s\S]+)$')

        # Storage Device: private-config
        p4 = re.compile(r'^Storage Device: +(?P<storage_device>[\s\S]+)$')

        # Usage: General Purpose Key
        p5 = re.compile(r'^Usage: +(?P<usage>[\s\S]+)$')

        # Key is not exportable. Redundancy enabled.
        p6 = re.compile(
            r'^Key is +(?P<key>[not exportable|exportable]+). +Redundancy +(?P<redundancy>[enabled|not enabled]+).$'
        )

        # Key is not exportable.
        p7 = re.compile(r'^Key is +(?P<key>[not exportable|exportable]+).$')

        # F2BC3B97 278C61D5 6700528C 59FF9BD2 A01F83E1 0123A7C5 638D212C FCA5AD92
        # C907010D 1D1776D8 09DDECE9 80A88D97 109A4C88 B0F85889 F379B628 4E9E0434
        p8 = re.compile(r'^(?P<key_data>[0-9A-Z\s]+)$')

        ret_dict = {}
        entry = 1
        for line in output.splitlines():
            line = line.strip()

            # % Key pair was generated at: 06:51:40 UTC Aug 30 2022
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                entry_dict = ret_dict.setdefault('keys',
                                                 {}).setdefault(entry, {})
                entry_dict.update(groups)
                entry += 1
                continue

            # Key name: test
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entry_dict.update(groups)
                continue

            # Key type: RSA KEYS
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key_dict = entry_dict.setdefault("key_type", {}).setdefault(
                    groups['key_type'], {})
                continue

            # Storage Device: private-config
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_dict.update(group)
                continue

            # Usage: General Purpose Key
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                key_dict.update(groups)
                continue

            # Key is not exportable. Redundancy enabled.
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                key_dict.update(groups)
                continue

            # Key is not exportable.
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                key_dict.update(groups)
                continue


            # F2BC3B97 278C61D5 6700528C 59FF9BD2 A01F83E1 0123A7C5 638D212C FCA5AD92
            # C907010D 1D1776D8 09DDECE9 80A88D97 109A4C88 B0F85889 F379B628 4E9E0434
            # B9020301 0001
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                key_data = key_dict.setdefault("key_data", [])
                key_data.append(groups['key_data'])
                continue

        return ret_dict


# ===================================================
#  Parser for 'show crypto key mypubkey rsa'
# ===================================================


class ShowCryptoKeyMypubkeyRsa(ShowCryptoKeyMypubkeyAll):
    ''' Parser for:
        show crypto key mypubkey rsa
    '''
    cli_command = 'show crypto key mypubkey rsa'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


# ===================================================
#  Parser for 'show crypto key mypubkey ec'
# ===================================================


class ShowCryptoKeyMypubkeyEc(ShowCryptoKeyMypubkeyAll):
    ''' Parser for:
        show crypto key mypubkey ec
    '''
    cli_command = 'show crypto key mypubkey ec'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


# ===================================================
#  Parser for 'show crypto key mypubkey rsa {key_name}'
# ===================================================


class ShowCryptoKeyMypubkeyRsaKeyName(ShowCryptoKeyMypubkeyAll):
    ''' Parser for:
        show crypto key mypubkey rsa {key_name}
    '''
    cli_command = 'show crypto key mypubkey rsa {key_name}'

    def cli(self, key_name='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


# ===================================================
#  Parser for 'show crypto key mypubkey ec {key_name}'
# ===================================================


class ShowCryptoKeyMypubkeyEcKeyName(ShowCryptoKeyMypubkeyAll):
    ''' Parser for:
        show crypto key mypubkey ec {key_name}
    '''
    cli_command = 'show crypto key mypubkey ec {key_name}'

    def cli(self, key_name='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


# =================================================
#  Schema for 'show crypto ikev2 performance'
# =================================================
class ShowCryptoIkev2PerformanceSchema(MetaParser):
    """Schema for show crypto ikev2 performance """
    schema = {
        "crypto_isakmp_performance_stats": {
            Any(): {
                Any(): {
                    'sample_size': int,
                    'tps_avg': int,
                    'tps_min': int,
                    'tps_max': int,
                    'cpu_avg': int,
                    'cpu_min': int,
                    'cpu_max': int,
                }
            }
        },
        Any(): {
            Any(): {
                "sample_size": int,
                "avg": int,
                "min": int,
                "max": int,
            }
        },
        "summary": {
            Any(): {
                "exchange_setup_value": int,
                Any(): {
                    "value": int,
                    "percentage": int
                }
            }
        }
    }

# ============================================
#   Parser for 'show crypto ikev2 performance'
# ============================================
class ShowCryptoIkev2Performance(ShowCryptoIkev2PerformanceSchema):
    """Parser for show crypto ikev2 performance"""

    cli_command = 'show crypto ikev2 performance'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Crypto ISAKMP Performance Stats (tps):
        # Crypto ISAKMP Packet Stats (pps):
        # Crypto IKEv2 Packet Queue Stats (milliseconds):
        # Crypto ISAKMP Protocol Stats (microseconds):
        # Crypto Engine Stats (microseconds):
        # External Service Stats (microseconds):
        # Summary (microsecs):
        p1 = re.compile(r"^(?P<stats_type>[\S\s]+)\(\w+\):$")

        # Ingress:               SampleSize tps/avg min max cpu/avg min max
        # Egress:                SampleSize tps/avg min max cpu/avg min max
        p2 = re.compile(r"^(?P<tps>Ingress|Egress):.*$")

        # IKE Established                 0       0   0   0       0   0   0
        # IPSEC Child Establishe          0       0   0   0       0   0   0
        # IKE Child Established           0       0   0   0       0   0   0
        # IKE Established                 0       0   0   0       0   0   0
        # IPSEC Child Establishe          0       0   0   0       0   0   0
        # IKE Child Established           0       0   0   0       0   0   0
        p3 = re.compile(r"^(?P<type>.*Est.*)\s+(?P<sample_size>\S+)\s+(?P<tps_avg>\S+)\s+(?P<tps_min>\S+)\s+(?P<tps_max>\S+)\s+(?P<cpu_avg>\S+)+\s+(?P<cpu_min>\S+)\s+(?P<cpu_max>\S+)$")

        # Incoming IKE Packets            0       0   0   0
        # -Init                           0       0   0   0
        # -Auth                           0       0   0   0
        # NO NAME                         0       0   0   0
        # NO NAME                         0       0   0   0
        # -Child                          0       0   0   0
        # -Info                           0       0   0   0
        # -Default                        0       0   0   0
        # Egress IKE Attempted            0       0   0   0
        # Packet Queue[0]             73614          0          0       1008
        # Packet Queue[1]                 0          0          0          0
        # Packet Queue[2]                 0          0          0          0
        # Packet Queue[3]                 0          0          0          0
        # Packet Queue[4]                 0          0          0          0
        # Packet Queue[5]                 0          0          0          0
        # Packet Queue[6]                 0          0          0          0
        # R INIT PROC                     0          0          0          0
        # I INIT_PROC                     0          0          0          0
        # R AUTH PROC                     0          0          0          0
        # I AUTH PROC                     0          0          0          0
        # R INIT INT                      0          0          0          0
        # I AUTH INT                      0          0          0          0
        # R AUTH INT                      0          0          0          0
        # I INIT SEND                     0          0          0          0
        # R INIT SEND                     0          0          0          0
        # I AUTH SEND                     0          0          0          0
        # R AUTH SEND                     0          0          0          0
        # R INIT Wire                     0          0          0          0
        # I AUTH Wire                     0          0          0          0
        # R AUTH Wire                     0          0          0          0
        # R COOKIE INT                    0          0          0          0
        # R COOKIE SEND                   0          0          0          0
        # R KE INT                        0          0          0          0
        # R KE SEND                       0          0          0          0
        # I IKE CHILD PROC                0          0          0          0
        # I IPSEC CHILD PROC              0          0          0          0
        # R IKE CHILD PROC                0          0          0          0
        # R IPSEC CHILD PROC              0          0          0          0
        # R IKE CHILD Wire                0          0          0          0
        # R IPSEC CHILD Wire              0          0          0          0
        # I IKE CHILD SEND                0          0          0          0
        # I IPSEC CHILD SEND              0          0          0          0
        # R IKE CHILD SEND                0          0          0          0
        # R IPSEC CHILD SEND              0          0          0          0
        # R IKE CHILD INT                 0          0          0          0
        # R IPSEC CHILD INT               0          0          0          0
        # I IKE CHILD INT                 0          0          0          0
        # I IPSEC CHILD INT               0          0          0          0
        # DH Create                       0          0          0          0
        # DH Share Secret                 0          0          0          0
        # DH Delete                       0          0          0          0
        # Create IKE SA                   0          0          0          0
        # Delete IKE SA                   0          0          0          0
        # PS Key Auth Generation          0          0          0          0
        # RSA Public Key Auth Ge          0          0          0          0
        # IKE Encrypt                     0          0          0          0
        # IKE Decrypt                     0          0          0          0
        # IKE HMAC                        0          0          0          0
        # IPSEC Create Key                0          0          0          0
        # IPSEC Delete SA                 0          0          0          0
        # Public Key Sign                 0          0          0          0
        # Public Key Verify               0          0          0          0
        # Public Key Encrypt              0          0          0          0
        # Public Key Decrypt              0          0          0          0
        # Get IKE Policy                  0          0          0          0
        # Get Pre-shared Key              0          0          0          0
        # Get Config Mode Data            0          0          0          0
        # Set Config Mode Data            0          0          0          0
        # Received EAP                    0          0          0          0
        # Recieved Client EAP             0          0          0          0
        # Verify Certificate              0          0          0          0
        # Fetch Certificate               0          0          0          0
        # Get IPSEC Policy                0          0          0          0
        # NO NAME                         0          0          0          0
        # Redirect Check                  0          0          0          0
        # Redirect Acceptance Ch          0          0          0          0
        # NO NAME                         0          0          0          0
        # NO NAME                         0          0          0          0
        p5 = re.compile(r"^(?P<stats_type>[\S\s]+)\s+(?P<sample_size>\d+)\s+(?P<avg>\d+)\s+(?P<min>\d+)\s+(?P<max>\d+)$")

        # Main Exchange Setup:            0
        # Child Exchange Setup:            0
        p6 = re.compile(r"^(?P<exchange_setup>Main|Child).*:\s+(?P<exchange_value>\d+)$")

        # Child Processing:                0 -> 0%
        # Transmission:                    0 -> 0%
        # Main Processing:                0 -> 0%
        # On IPC Queue:                   0 -> 0%
        # Transmission:                   0 -> 0%
        p7 = re.compile(r"^(?P<processing_type>[\w\s]+):\s+(?P<value>\d+)\s+->\s+(?P<percentage>\d+)%$")

        ret_dict = {}
        var = 0
        for line in output.splitlines():
            line = line.strip()

            # Crypto ISAKMP Performance Stats (tps):
            # Crypto ISAKMP Packet Stats (pps):
            # Crypto IKEv2 Packet Queue Stats (milliseconds):
            # Crypto ISAKMP Protocol Stats (microseconds):
            # Crypto Engine Stats (microseconds):
            # External Service Stats (microseconds):
            # Summary (microsecs):
            m = p1.match(line)
            if m:
                group = m.groupdict()
                stats_type = group['stats_type'].lower().strip().replace(' ', '_')
                crypto_perf_dict = ret_dict.setdefault(stats_type,  {})
                continue

            # Ingress:               SampleSize tps/avg min max cpu/avg min max
            # Egress:                SampleSize tps/avg min max cpu/avg min max
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tps_type = group['tps'].lower().replace(' ', '_')
                group_dict = crypto_perf_dict.setdefault(tps_type, {})
                continue

            # IKE Established                 0       0   0   0       0   0   0
            # IPSEC Child Establishe          0       0   0   0       0   0   0
            # IKE Child Established           0       0   0   0       0   0   0
            # IKE Established                 0       0   0   0       0   0   0
            # IPSEC Child Establishe          0       0   0   0       0   0   0
            # IKE Child Established           0       0   0   0       0   0   0
            m =  p3.match(line)
            if m:
                group = m.groupdict()
                proto_type = group['type'].lower().strip().replace(' ', '_')
                proto_dict = group_dict.setdefault(proto_type, {})
                proto_dict.update({'sample_size': int(group['sample_size'])})
                proto_dict.update({'tps_avg': int(group['tps_avg'])})
                proto_dict.update({'tps_min': int(group['tps_min'])})
                proto_dict.update({'tps_max': int(group['tps_max'])})
                proto_dict.update({'cpu_avg': int(group['cpu_avg'])})
                proto_dict.update({'cpu_min': int(group['cpu_min'])})
                proto_dict.update({'cpu_max': int(group['cpu_max'])})
                continue

            # Incoming IKE Packets            0       0   0   0
            # -Init                           0       0   0   0
            # -Auth                           0       0   0   0
            # NO NAME                         0       0   0   0
            # NO NAME                         0       0   0   0
            # -Child                          0       0   0   0
            # -Info                           0       0   0   0
            # -Default                        0       0   0   0
            # Egress IKE Attempted            0       0   0   0
            # Packet Queue[0]             75416          0          0       1008
            # Packet Queue[1]                 0          0          0          0
            # Packet Queue[2]                 0          0          0          0
            # Packet Queue[3]                 0          0          0          0
            # Packet Queue[4]                 0          0          0          0
            # Packet Queue[5]                 0          0          0          0
            # Packet Queue[6]                 0          0          0          0
            # R INIT PROC                     0          0          0          0
            # I INIT_PROC                     0          0          0          0
            # R AUTH PROC                     0          0          0          0
            # I AUTH PROC                     0          0          0          0
            # R INIT INT                      0          0          0          0
            # I AUTH INT                      0          0          0          0
            # R AUTH INT                      0          0          0          0
            # I INIT SEND                     0          0          0          0
            # R INIT SEND                     0          0          0          0
            # I AUTH SEND                     0          0          0          0
            # R AUTH SEND                     0          0          0          0
            # R INIT Wire                     0          0          0          0
            # I AUTH Wire                     0          0          0          0
            # R AUTH Wire                     0          0          0          0
            # R COOKIE INT                    0          0          0          0
            # R COOKIE SEND                   0          0          0          0
            # R KE INT                        0          0          0          0
            # R KE SEND                       0          0          0          0
            # I IKE CHILD PROC                0          0          0          0
            # I IPSEC CHILD PROC              0          0          0          0
            # R IKE CHILD PROC                0          0          0          0
            # R IPSEC CHILD PROC              0          0          0          0
            # R IKE CHILD Wire                0          0          0          0
            # R IPSEC CHILD Wire              0          0          0          0
            # I IKE CHILD SEND                0          0          0          0
            # I IPSEC CHILD SEND              0          0          0          0
            # R IKE CHILD SEND                0          0          0          0
            # R IPSEC CHILD SEND              0          0          0          0
            # R IKE CHILD INT                 0          0          0          0
            # R IPSEC CHILD INT               0          0          0          0
            # I IKE CHILD INT                 0          0          0          0
            # I IPSEC CHILD INT               0          0          0          0
            # DH Create                       0          0          0          0
            # DH Share Secret                 0          0          0          0
            # DH Delete                       0          0          0          0
            # Create IKE SA                   0          0          0          0
            # Delete IKE SA                   0          0          0          0
            # PS Key Auth Generation          0          0          0          0
            # RSA Public Key Auth Ge          0          0          0          0
            # IKE Encrypt                     0          0          0          0
            # IKE Decrypt                     0          0          0          0
            # IKE HMAC                        0          0          0          0
            # IPSEC Create Key                0          0          0          0
            # IPSEC Delete SA                 0          0          0          0
            # Public Key Sign                 0          0          0          0
            # Public Key Verify               0          0          0          0
            # Public Key Encrypt              0          0          0          0
            # Public Key Decrypt              0          0          0          0
            # Get IKE Policy                  0          0          0          0
            # Get Pre-shared Key              0          0          0          0
            # Get Config Mode Data            0          0          0          0
            # Set Config Mode Data            0          0          0          0
            # Received EAP                    0          0          0          0
            # Recieved Client EAP             0          0          0          0
            # Verify Certificate              0          0          0          0
            # Fetch Certificate               0          0          0          0
            # Get IPSEC Policy                0          0          0          0
            # NO NAME                         0          0          0          0
            # Redirect Check                  0          0          0          0
            # Redirect Acceptance Ch          0          0          0          0
            # NO NAME                         0          0          0          0
            # NO NAME                         0          0          0          0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                stats_type = group['stats_type'].lower().strip().replace(' ', '_').\
                        replace('-', "").replace('[', "").replace(']', "")
                if stats_type == 'no_name':
                    stats_type = stats_type + '_' + str(var)
                    var += 1
                ike_dict = crypto_perf_dict.setdefault(stats_type, {})
                ike_dict.update({'sample_size': int(group['sample_size'])})
                ike_dict.update({'avg': int(group['avg'])})
                ike_dict.update({'min': int(group['min'])})
                ike_dict.update({'max': int(group['max'])})
                continue

            # Child Exchange Setup:            0
            # Main Exchange Setup:            0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                exchange_setup = group['exchange_setup'].lower().strip()
                exchange_dict = crypto_perf_dict.setdefault(exchange_setup, {})
                exchange_dict.update({'exchange_setup_value': int(group['exchange_value'])})
                continue

            # Child Processing:                0 -> 0%
            # Transmission:                    0 -> 0%
            # Main Processing:                0 -> 0%
            # On IPC Queue:                   0 -> 0%
            # Transmission:                   0 -> 0%
            m = p7.match(line)
            if m:
                group = m.groupdict()
                processing_type = group['processing_type'].lower().strip().replace(' ', '_')
                process_dict = exchange_dict.setdefault(processing_type, {})
                process_dict.update({'value':  int(group['value'])})
                process_dict.update({'percentage':  int(group['percentage'])})
                continue

        return ret_dict
