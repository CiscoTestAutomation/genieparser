
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use


class FnvReadSchema(MetaParser):
    """Schema for fnvread"""
    schema = {
        'pod': {
            Any(): {
                'node': {
                    Any(): {
                        'address': str,
                        'disabled': str,
                        'active': str,
                        'occupied': str,
                        'permanent': str,
                        'model': str,
                        'node_role': str,
                        'node_type': str,
                        'fabric_id': int,
                        'node': int,
                        'pod': int
                    }
                }
            }
        }
    }


class FnvRead(FnvReadSchema):

    cli_command = 'fnvread'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #         id               address  disabled    active  occupied permanent              model  nodeRole  nodeType  fabricId     podId
        #     101(1)      10.0.32.64/32(1)     NO(1)    YES(1)    YES(1)    YES(1)N9K-C93240YC-FX2(1)      2(1)      0(1)      1(1)      1(1)
        p1 = re.compile(r'(?P<node>\d+){0}(?P<address>\S+){0}(?P<disabled>\S+){0}(?P<active>\S+){0}(?P<occupied>\S+){0}(?P<permanent>\S+){0}(?P<model>\S+){0}(?P<node_role>\S+){0}(?P<node_type>\S+){0}(?P<fabric_id>\S+){0}(?P<pod>\S+){0}'.format(r'\(\d+\)\s*'))

        fnv_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                node_dict = fnv_dict.setdefault(
                    'pod', {}).setdefault(
                        int(groups['pod']), {}).setdefault(
                            'node', {}).setdefault(
                                int(groups['node']), {})
                node_dict.update({'address': groups['address']})
                node_dict.update({'disabled': groups['disabled']})
                node_dict.update({'active': groups['active']})
                node_dict.update({'occupied': groups['occupied']})
                node_dict.update({'permanent': groups['permanent']})
                node_dict.update({'model': groups['model']})
                node_dict.update({'node_role': groups['node_role']})
                node_dict.update({'node_type': groups['node_type']})
                node_dict.update({'fabric_id': int(groups['fabric_id'])})
                node_dict.update({'pod': int(groups['pod'])})
                node_dict.update({'node': int(groups['node'])})

        return fnv_dict
