from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re

# ======================================================
# Schema for 'show service sap-using'
# ======================================================

class ShowServiceSapUsingSchema(MetaParser):
    """schema for show service sap-using"""
    schema = {
        'total': int,
        'sap': {
            Any(): {
                'service_id': int,
                'ingress_qos': int,
                'egress_qos': int,
                'ingress_filter': str,
                'egress_filter': str,
                'admin_state': str,
                'oper_state': str,
            }
        }
    }

class ShowServiceSapUsing(ShowServiceSapUsingSchema):
    """ Parser for show service sap-using"""
    cli_command = 'show service sap-using'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # 2/1/6:10.*                      10         1     none    1     none   Up   Up
        # 2/1/2:8.1                       181        1     none    1     none   Up   Down
        # 2/1/2:3101.3101                 1121       3501  none    3501  none   Up   Down
        # 2/1/6:*.*                    1121       1     none    1     none   Up   Up
        # 2/1/6:3101.*                    1121       4503  none    4503  none   Up   Up
        # lag-2:4000.*                    1122       1     none    1     none   Up   Up
        # lag-1:400.1                    1221       1     none    1     none   Up   Up
        p1 = re.compile(r'(?P<sap>\S+)'
                        r' +(?P<service>\d+) +(?P<ing_qos>\d+) +(?P<ing_filter>\S+)'
                        r' +(?P<egr_qos>\d+) +(?P<egr_filter>\S+)' 
                        r' +(?P<admin>Up|Down)\s+(?P<oper>Up|Down)')

        # Number of SAPs : 8
        p2 = re.compile(r'^Number of SAPs : (?P<total>\d+)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # 2/1/6:10.*                      10         1     none    1     none   Up   Up
            # 2/1/2:8.1                       181        1     none    1     none   Up   Down
            # 2/1/2:3101.3101                 1121       3501  none    3501  none   Up   Down
            # 2/1/6:*.*                    1121       1     none    1     none   Up   Up
            # 2/1/6:3101.*                    1121       4503  none    4503  none   Up   Up
            # lag-2:4000.*                    1122       1     none    1     none   Up   Up
            # lag-1:400.1                    1221       1     none    1     none   Up   Up

            m = p1.match(line)
            if m:
                group = m.groupdict()
                sap=group['sap']
                result_dict.setdefault('sap', {}).setdefault(sap,{})
                result_dict['sap'][sap].update({'service_id': int(group['service'])})
                result_dict['sap'][sap].update({'ingress_qos': int(group['ing_qos'])})
                result_dict['sap'][sap].update({'egress_qos': int(group['egr_qos'])})
                result_dict['sap'][sap].update({'ingress_filter': (group['ing_filter'])})
                result_dict['sap'][sap].update({'egress_filter': (group['egr_filter'])})
                result_dict['sap'][sap].update({'admin_state': (group['admin'])})
                result_dict['sap'][sap].update({'oper_state': (group['oper'])})
                continue

            # Number of SAPs : 8

            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['total'] = int(group['total'])

        return result_dict
