import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any
# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================
# Schema for 'show isdn status serial {interface}'
# ==============================================
class ShowIsdnStatusSerialSchema(MetaParser):
    """Schema for 'show isdn status serial {interface}'"""
    schema = {
        'global_isdn_switchtype': str,
        'interface': {
            Any(): {  # Interface name
                'dsl': int,
                'interface_isdn_switchtype': str,
                'layer_1_status': str,
                'layer_2_status': {
                    'tei': int,
                    'ces': int,
                    'sapi': int,
                    'state': str,
                },
                'layer_3_status': {
                    'active_layer_3_calls': int,
                },
                'active_dsl_ccbs': int,
                'free_channel_mask': str,
                'number_of_l2_discards': int,
                'l2_session_id': int,
                'total_allocated_isdn_ccbs': int,
            }
        }
    }


# ==============================================
# Parser for 'show isdn status serial {interface}'
# ==============================================
class ShowIsdnStatusSerial(ShowIsdnStatusSerialSchema):
    """Parser for 'show isdn status serial {interface}'"""

    cli_command = 'show isdn status serial {interface}'

    def cli(self, interface="", output=None, device=""):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command.format(interface=interface))

        ret_dict = {}

        # Global ISDN Switchtype = primary-5ess
        p1 = re.compile(r'^Global\s+ISDN\s+Switchtype\s+=\s+(?P<switchtype>\S+)$')

        # ISDN Serial1/1/0:15 interface
        p2 = re.compile(r'^ISDN\s+(?P<interface>\S+)\s+interface$')

        # dsl 0, interface ISDN Switchtype = primary-5ess
        p3 = re.compile(r'^dsl\s+(?P<dsl>\d+),\s+interface\s+ISDN\s+Switchtype\s+=\s+(?P<switchtype>\S+)$')

        # Layer 1 Status:
        p4 = re.compile(r'^Layer\s+1\s+Status:$')

        # ACTIVE
        p5 = re.compile(r'^(?P<layer1_status>\w+)$')

        # Layer 2 Status:
        p6 = re.compile(r'^Layer\s+2\s+Status:$')

        # TEI = 0, Ces = 1, SAPI = 0, State = MULTIPLE_FRAME_ESTABLISHED
        p7 = re.compile(r'^TEI\s+=\s+(?P<tei>\d+),\s+Ces\s+=\s+(?P<ces>\d+),\s+SAPI\s+=\s+(?P<sapi>\d+),\s+State\s+=\s+(?P<state>\S+)$')

        # Layer 3 Status:
        p8 = re.compile(r'^Layer\s+3\s+Status:$')

        # 0 Active Layer 3 Call(s)
        p9 = re.compile(r'^(?P<active_calls>\d+)\s+Active\s+Layer\s+3\s+Call\(s\)$')

        # Active dsl 0 CCBs = 0
        p10 = re.compile(r'^Active\s+dsl\s+(?P<dsl>\d+)\s+CCBs\s+=\s+(?P<ccbs>\d+)$')

        # The Free Channel Mask:  0x80FF7FFF
        p11 = re.compile(r'^The\s+Free\s+Channel\s+Mask:\s+(?P<mask>\S+)$')

        # Number of L2 Discards = 0, L2 Session ID = 9
        p12 = re.compile(r'^Number\s+of\s+L2\s+Discards\s+=\s+(?P<discards>\d+),\s+L2\s+Session\s+ID\s+=\s+(?P<session_id>\d+)$')

        # Total Allocated ISDN CCBs = 0
        p13 = re.compile(r'^Total\s+Allocated\s+ISDN\s+CCBs\s+=\s+(?P<ccbs>\d+)$')

        # State tracking variables
        current_interface = None
        waiting_for_layer1 = False
        waiting_for_layer2 = False
        waiting_for_layer3 = False

        for line in output.splitlines():
            line = line.strip()

            # Global ISDN Switchtype = primary-5ess
            m = p1.match(line)
            if m:
                ret_dict['global_isdn_switchtype'] = m.group('switchtype')
                continue

            # ISDN Serial1/1/0:15 interface
            m = p2.match(line)
            if m:
                interface_name = m.group('interface')
                current_interface = ret_dict.setdefault('interface', {}).setdefault(interface_name, {})
                continue

            # dsl 0, interface ISDN Switchtype = primary-5ess
            m = p3.match(line)
            if m and current_interface is not None:
                current_interface['dsl'] = int(m.group('dsl'))
                current_interface['interface_isdn_switchtype'] = m.group('switchtype')
                continue

            # Layer 1 Status:
            m = p4.match(line)
            if m:
                waiting_for_layer1 = True
                continue

            # ACTIVE (Layer 1 status value)
            m = p5.match(line)
            if m and waiting_for_layer1 and current_interface is not None:
                current_interface['layer_1_status'] = m.group('layer1_status')
                waiting_for_layer1 = False
                continue

            # Layer 2 Status:
            m = p6.match(line)
            if m:
                waiting_for_layer2 = True
                continue

            # TEI = 0, Ces = 1, SAPI = 0, State = MULTIPLE_FRAME_ESTABLISHED
            m = p7.match(line)
            if m and waiting_for_layer2 and current_interface is not None:
                layer2_dict = current_interface.setdefault('layer_2_status', {})
                layer2_dict['tei'] = int(m.group('tei'))
                layer2_dict['ces'] = int(m.group('ces'))
                layer2_dict['sapi'] = int(m.group('sapi'))
                layer2_dict['state'] = m.group('state')
                waiting_for_layer2 = False
                continue

            # Layer 3 Status:
            m = p8.match(line)
            if m:
                waiting_for_layer3 = True
                continue

            # 0 Active Layer 3 Call(s)
            m = p9.match(line)
            if m and waiting_for_layer3 and current_interface is not None:
                layer3_dict = current_interface.setdefault('layer_3_status', {})
                layer3_dict['active_layer_3_calls'] = int(m.group('active_calls'))
                waiting_for_layer3 = False
                continue

            # Active dsl 0 CCBs = 0
            m = p10.match(line)
            if m and current_interface is not None:
                current_interface['active_dsl_ccbs'] = int(m.group('ccbs'))
                continue

            # The Free Channel Mask:  0x80FF7FFF
            m = p11.match(line)
            if m and current_interface is not None:
                current_interface['free_channel_mask'] = m.group('mask')
                continue

            # Number of L2 Discards = 0, L2 Session ID = 9
            m = p12.match(line)
            if m and current_interface is not None:
                current_interface['number_of_l2_discards'] = int(m.group('discards'))
                current_interface['l2_session_id'] = int(m.group('session_id'))
                continue

            # Total Allocated ISDN CCBs = 0
            m = p13.match(line)
            if m and current_interface is not None:
                current_interface['total_allocated_isdn_ccbs'] = int(m.group('ccbs'))
                continue

        return ret_dict
