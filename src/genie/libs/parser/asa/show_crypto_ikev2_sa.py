"""
show_crypto_ikev2_sa.py
Parser for the following command:
    * show crypto ikev2 sa
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional)

class ShowCryptoIkev2SaSchema(MetaParser):
    """Schema for 
        * show crypto ikev2 sa
    """

    schema = {
        'sessions': {
            Any(): {
                'session_id': int,
                'status': str,
                'ike_count': int,
                'child_sa_count': int,
				'tunnels': {
                    Any(): {
                        'tunnel_id': int,
                        'local': str,
                        'remote': str,
                        'status': str,
                        'role': str,
                        'encryption_algorithm': str,
                        'hashing_algorithm': str,
                        'dh_group': int,
                        'authentication_sign': str,
                        'authentication_verify': str,
                        'lifetime': int,
                        'activetime': int,
                        'child_sa': {
                            Any(): {
                                'local_selector': str,
                                'remote_selector': str,
                                'esp_in': str,
                                'esp_out': str
                            }
                        }
                    },
                },
            },
        },
    }

class ShowCryptoIkev2Sa(ShowCryptoIkev2SaSchema):
    '''Parser for
        * show crypto ikev2 sa
    '''

    cli_command = 'show crypto ikev2 sa'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        dict_sessions = parsed_dict.setdefault('sessions', {})
        child_sa_index = 0

        p1 = re.compile(
            r'^Session-id:(?P<session_id>[\d]),\s'
            r'Status:(?P<status>[A-Za-z\-]{1,}),\s'
            r'IKE\scount:(?P<ike_count>[\d]),\s'
            r'CHILD\scount:(?P<child_count>[\d])$'
        )

        p2 = re.compile(
            r'^(?P<tunnel_id>\d+)\s+(?P<local>\S+)\s+'
            r'(?P<remote>\S+)\s+(?P<status>\w+)\s+(?P<role>\w+)$'
        )

        p3 = re.compile(
            r'^Encr:\s+(?P<encr>\S+),\s+Hash:\s+(?P<hash>\S+),\s+'
            r'DH\sGrp:(?P<dh_group>\d+),\s+Auth\ssign:\s+(?P<auth_sign>\S+),\s+'
            r'Auth\sverify:\s+(?P<auth_verify>\S+)$'
        )

        p4 = re.compile(
            r'^Life\/Active\sTime:\s+'
            r'(?P<life_time>\d+)\/(?P<active_time>\d+)\s+sec$'
        )

        p5 = re.compile(
            r'^Child\ssa:\slocal\sselector\s+(?P<local_selector>.*)$'
        )

        p6 = re.compile(
            r'^remote\sselector\s+(?P<remote_selector>.*)$'
        )

        p7 = re.compile(
            r'^ESP\sspi\sin\/out:\s+(?P<esp_in>\S+)\/(?P<esp_out>\S+)$'
        )

        out = out.splitlines()
        if not out:
            return

        for line in out:
            line = line.strip()

            m = p1.match(line)

            if m:
                group = m.groupdict()
                session_id = int(group['session_id'])
                status = group['status']
                ike_count = int(group['ike_count'])
                child_sa_count = int(group['child_count'])
                dict_session = dict_sessions.setdefault(session_id, {})
                dict_session.update({'session_id': session_id})
                dict_session.update({'status': status})
                dict_session.update({'ike_count': ike_count})
                dict_session.update({'child_sa_count': child_sa_count})
                dict_tunnels = dict_session.setdefault('tunnels', {})
                continue

            m = p2.match(line)

            if m:
                group = m.groupdict()
                tunnel_id = int(group['tunnel_id'])
                local = group['local']
                remote = group['remote']
                status = group['status']
                role = group['role']
                dict_tunnel = dict_tunnels.setdefault('{}-{}'.format(local, remote), {})
                dict_tunnel.update({'tunnel_id': tunnel_id})
                dict_tunnel.update({'local': local})
                dict_tunnel.update({'remote': remote})
                dict_tunnel.update({'status': status})
                dict_tunnel.update({'role': role})
                continue

            m = p3.match(line)

            if m:
                group = m.groupdict()
                encr_alg = group['encr']
                hash_alg = group['hash']
                dh_group = int(group['dh_group'])
                auth_sign = group['auth_sign']
                auth_verify = group['auth_verify']
                dict_tunnel.update({'encryption_algorithm': encr_alg})
                dict_tunnel.update({'hashing_algorithm': hash_alg})
                dict_tunnel.update({'dh_group': dh_group})
                dict_tunnel.update({'authentication_sign': auth_sign})
                dict_tunnel.update({'authentication_verify': auth_verify})
                continue

            m = p4.match(line)

            if m:
                group = m.groupdict()
                life_time = int(group['life_time'])
                active_time = int(group['active_time'])
                dict_tunnel.update({'lifetime': life_time})
                dict_tunnel.update({'activetime': active_time})
                child_sas = dict_tunnel.setdefault('child_sa', {})
                child_sa_index = 0
                continue

            m = p5.match(line)

            if m:
                group = m.groupdict()
                local_selector = group['local_selector']
                child_sa = child_sas.setdefault(child_sa_index, {})
                child_sa.update({'local_selector': local_selector})
                child_sa_index = child_sa_index + 1
                continue


            m = p6.match(line)

            if m:
                group = m.groupdict()
                remote_selector = group['remote_selector']
                child_sa.update({'remote_selector': local_selector})
                continue


            m = p7.match(line)

            if m:
                group = m.groupdict()
                esp_in = group['esp_in']
                esp_out = group['esp_out']

                child_sa.update({'esp_in': esp_in})
                child_sa.update({'esp_out': esp_out})
                continue
                
        return parsed_dict

