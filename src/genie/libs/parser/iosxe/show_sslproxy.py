from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
import re
import genie.parsergen as pg


class ShowSslproxyStatusSchema(MetaParser):
    ''' Schema for show sslproxy status'''
    schema = {
        'ca_cert_bundle': str,
        'ca_tp_label': str,
        'cert_lifetime': int,
        'rsa_key_modulus': int,
        'cert_revocation': str,
        'expired_cert': str,
        'untrusted_cert': str,
        'unsupported_protocol_ver': str,
        'unsupported_cipher_suites': str,
        'failure_mode_action': str,
        'min_tls_ver': str,
        'ssl_proxy_operational_state': str,
        'tcp_proxy_operational_state': str,
        'clear_mode': str}


class ShowSslproxyStatus(ShowSslproxyStatusSchema):

    """ Parser for "show sslproxy status" """
    
    cli_command = "show sslproxy status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # show sslproxy status                                                                                                                 
        # CA Cert Bundle                 : /bootflash/vmanage-admin/apache.pem                                                
        # CA TP Label                    : PROXY-SIGNING-CA                                                                   
        # Cert Lifetime                  : 730                                                                                
        # RSA Key Modulus                : 2048                                                                               
                                                                                                                            
        # Cert Revocation                : NONE                                                                               
        # Expired Cert                   : drop                                                                               
        # Untrusted Cert                 : drop                                                                               
        # Unsupported Protocol Ver       : drop                                                                               
                                                                                                                            
        # Unsupported Cipher Suites      : drop                                                                               
        # Failure Mode Action            : close                                                                              
        # Min TLS Ver                    : TLS Version 1                                                                      
                                                                                                             
        # SSL Proxy Operational State    : RUNNING                                                                            
        # TCP Proxy Operational State    : RUNNING                                                                            
        # Clear Mode                     : FALSE

        p1 = re.compile(r'^(?P<key>[\s\w]+): +(?P<value>[\/\w\d\.\-\s]+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].strip().replace('-', '_').replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                parsed_dict.update({key: value})

        return parsed_dict