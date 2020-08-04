# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema

class ShowSslproxyStatusSchema(MetaParser):
    ''' Schema for show sslproxy status'''
    schema = {
        'configuration': {
            'ca_cert_bundle': str,
            'ca_tp_label': str,
            'cert_lifetime': int,
            'ec_key_type': str,
            'rsa_key_modulus': int,
            'cert_revocation': str,
            'expired_cert': str,
            'untrusted_cert': str,
            'unknown_status': str,
            'unsupported_protocol_ver': str,
            'unsupported_cipher_suites': str,
            'failure_mode_action': str,
            'min_tls_ver': str,
        },
        'status': {
            'ssl_proxy_operational_state': str,
            'tcp_proxy_operational_state': str,
            'clear_mode': str,
        }
    }


class ShowSslproxyStatus(ShowSslproxyStatusSchema):

    """ Parser for "show sslproxy status" """
    
    cli_command = "show sslproxy status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Configuration
        p1 = re.compile(r'^Configuration$')

        # Status
        p2 = re.compile(r'^Status$')

        # CA Cert Bundle                 : /bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem
        # CA TP Label                    : PROXY-SIGNING-CA
        # Cert Lifetime                  : 730
        # EC Key type                    : P256
        # RSA Key Modulus                : 2048
        # Cert Revocation                : NONE
        # Expired Cert                   : drop
        # Untrusted Cert                 : drop
        # Unknown Status                 : drop
        # Unsupported Protocol Ver       : drop
        # Unsupported Cipher Suites      : drop
        # Failure Mode Action            : close
        # Min TLS Ver                    : TLS Version 1.1
        # SSL Proxy Operational State    : RUNNING
        # TCP Proxy Operational State    : RUNNING
        # Clear Mode                     : FALSE
        p3 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Configuration
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                configuration_dict = parsed_dict.setdefault('configuration', {})
                last_dict_ptr = configuration_dict
                continue

            # Status
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                status_dict = parsed_dict.setdefault('status', {})
                last_dict_ptr = status_dict
                continue

            # CA Cert Bundle                 : /bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem
            # CA TP Label                    : PROXY-SIGNING-CA
            # Cert Lifetime                  : 730
            # EC Key type                    : P256
            # RSA Key Modulus                : 2048
            # Cert Revocation                : NONE
            # Expired Cert                   : drop
            # Untrusted Cert                 : drop
            # Unknown Status                 : drop
            # Unsupported Protocol Ver       : drop
            # Unsupported Cipher Suites      : drop
            # Failure Mode Action            : close
            # Min TLS Ver                    : TLS Version 1.1
            # SSL Proxy Operational State    : RUNNING
            # TCP Proxy Operational State    : RUNNING
            # Clear Mode                     : FALSE
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict