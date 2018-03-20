"""show_crypto.py
   * show crypto pki certificates <WORD>

"""
import re

from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from parser.utils.common import Common


class ShowCryptoPkiCertificatesSchema(MetaParser):
    """Schema for show crypto pki certificates <WORD>"""
    schema = {
        'trustpoints': {
            Any(): {
                'associated_trustpoints':{
                    Any(): { # certificate, ca_certificate                    
                        'status': str,
                        'serial_number_in_hex': str,
                        'usage': str,
                        'issuer': {
                            'cn': str,
                            'o': str
                        },
                        'subject': {
                            Optional('name'): str,
                            Optional('serial_number'): str,
                            Optional('pid'): str,
                            'cn': str,
                            Optional('o'): str,
                        },
                        'crl_distribution_points': str,
                        'validity_date': {
                            'start_date':str,
                            'end_date': str
                        }
                    },
                }
            },
        }
    }


class ShowCryptoPkiCertificates(ShowCryptoPkiCertificatesSchema):
    """Parser for show crypto pki certificates <WORD>"""

    def cli(self, trustpoint_name=''):
         # get output from device
        out = self.device.execute('show crypto pki certificates {}'\
                .format(trustpoint_name)) if trustpoint_name else \
                     self.device.execute('show crypto pki certificates')

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^((?P<cer>Certificate)|(?P<ca_cer>CA +Certificate))$')
        p2 = re.compile(r'^Status: +(?P<status>\w+)$')
        p3 = re.compile(r'^Certificate +Serial +Number +\(hex\): +(?P<serial_number_in_hex>\w+)$')
        p4 = re.compile(r'^Certificate Usage: +(?P<usage>[\w\s]+)$')
        p5 = re.compile(r'^((?P<issuer>Issuer)|(?P<subject>Subject)|(?P<validity_date>Validity +Date)):$')
        p6 = re.compile(r'^cn\=(?P<cn>[\w\s\-]+)$')
        p7 = re.compile(r'^o\=(?P<o>[\w\s]+)$')
        p8 = re.compile(r'^Name: +(?P<name>.*)$')
        p9 = re.compile(r'^Serial +Number: *'
                          'PID: *(?P<pid>[\w\-]+) +'
                          'SN: *(?P<serial_number>[\w\-]+)$')
        p10 = re.compile(r'(?P<crl_distribution_points>^http:[\w\/\:\.]+)$')
        p11 = re.compile(r'^((?P<start_date>start +date)|(?P<end_date>end +date)): +(?P<value>.*)$')
        p12 = re.compile(r'^Associated +Trustpoints: +(?P<trustpoints>[\w\-]+)( +Trustpool)?$')

        for line in out.splitlines():
            line = line.strip()
            
            # Certificate
            # CA Certificate
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cer_type = 'certificate' if group.get('cer', {}) else 'ca_certificate'
                cer_dict = ret_dict.setdefault(cer_type, {})
                continue
            
            # Status: Available
            m = p2.match(line)
            if m:
                cer_dict['status'] = m.groupdict()['status']
                continue
            
            # Certificate Serial Number (hex): 793B572700000003750B
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
            m = p6.match(line)
            if m:
                sub_dict['cn'] = m.groupdict()['cn']
                continue
            
            # o=Cisco
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
