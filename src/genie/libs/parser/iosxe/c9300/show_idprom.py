"""
IOSXE C9300 parsers for the following show commands:
    * show idprom
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# ============================
#  Schema for 'show idprom interface <interface>'
# ============================

class ShowIdpromInterfaceSchema(MetaParser):
    """Schema for show idprom interface {interface}"""
    schema = {
        'sfp_info': {
            'vendor_name': str,
            'cisco_part_number': str,
            'vendor_revision': str,
            'serial_number': str,
            'product_identifier': str,
            'connector_type': str,
        },
        'extended_id_fileds': {
            'options': str,
            'br_max': str,
            'br_min': str,
            'date_code': int,
            'diag_monitoring': str,
            'internally_calibrated': str,
            'exeternally_calibrated': str,
            'rx_power_measurement': str,
            'address_change': str,
            'cc_ext': str
        },
        'other_information': {
            'chk_for_link_status': str,
            'flow_control_receive': str,
            'flow_control_send': str,
            'administrative_speed': str,
            'administrative_duplex': str,
            'operational_speed': str,
            'operational_duplex': str
        }
    }

# ============================
#  Parser for 'show idprom interface <interface>'
# ============================

class ShowIdpromInterface(ShowIdpromInterfaceSchema):
    """Parser for show idprom interface <interface>"""

    cli_command = [
        'show idprom interface {interface}'
    ]

    def cli(self, interface, output=None):
        if output is None:
            cmd = self.cli_command[0].format(interface=interface)
            output = self.device.execute(cmd)

        ret_dict = {}

        # General SFP Information
        p1 = re.compile(
            r'^General SFP Information$')

        # Vendor Name           :   CISCO-EXCELIGHT
        p1_1 = re.compile(
            r'^Vendor +Name\s+:\s+(?P<vendor_name>.*)$')

        # Vendor Part Number    :   SPP5101SR-C1 
        p1_2 = re.compile(
            r'^Vendor +Part +Number\s+:\s+(?P<part_number>.*)$')

        # Vendor Revision       :   0x41 0x20 0x20 0x20
        p1_3 = re.compile(
            r'^Vendor +Revision\s+\:\s+(?P<vendor_revision>[0-9a-fA-Fx ]+)$')

        # Vendor Serial Number  :   ECL1249000S 
        p1_4 = re.compile(
            r'^Vendor +Serial +Number\s+:\s+(?P<serial_number>.*)$')

        # Identifier            :   SFP/SFP+
        p1_5 = re.compile(
            r'^Identifier\s+:\s+(?P<product_identifier>.*)$')

        # Connector             :   LC connector
        p1_6 = re.compile(
            r'^Connector\s+:\s+(?P<connector_type>[\w\s]+)$')
        
        # Extended ID Fields
        p2 = re.compile(r'^Extended ID Fields$')

        # Options               :   0x00 0x1A
        p2_0 = re.compile(
            r'^Options\s+:\s+(?P<options>[\w\s]+)$')
        
        # BR, max               :   0x00
        p2_1 = re.compile(
            r'^BR, max\s+:\s+(?P<br_max>[\w\s]+)$')
        
        # BR, min               :   0x00
        p2_2 = re.compile(
            r'^BR, min\s+:\s+(?P<br_min>[\w\s]+)$')
        
        # Date code             :   161031
        p2_3 = re.compile(
            r'^Date code\s+:\s+(?P<date_code>\d+)$')
        
        # Diag monitoring       :   Implemented
        p2_4 = re.compile(
            r'^Diag monitoring\s+:\s+(?P<diag_monitoring>[\w\s]+)$')
        
        # Internally calibrated :   Yes
        p2_5 = re.compile(
            r'^Internally calibrated\s+:\s+(?P<internally_calibrated>\w+)$')
        
        # Exeternally calibrated:   No
        p2_6 = re.compile(
            r'^Exeternally calibrated\s*:\s+(?P<exeternally_calibrated>\w+)$')
        
        # Rx.Power measurement  :   Avg.Power
        p2_7 = re.compile(
            r'^Rx.Power measurement\s+:\s+(?P<rx_power_measurement>.+)$')
        
        # Address Change        :   Not Required
        p2_8 = re.compile(
            r'^Address Change\s+:\s+(?P<address_change>[\w\s]+)$')
        
        # CC_EXT                :   0x32
        p2_9 = re.compile(
            r'^CC_EXT\s+:\s+(?P<cc_ext>\w+)$')
        
        # Other Information
        p3 = re.compile(r'^Other Information$')
        
        # Chk for link status   : 00
        p3_0 = re.compile(
            r'^Chk for link status\s+:\s+(?P<chk_for_link_status>\w+)$')
        
        # Flow control Receive  : ON
        p3_1 = re.compile(
            r'^Flow control Receive\s+:\s+(?P<flow_control_receive>[\w\s]+)$')
        
        # Flow control Send     : Off
        p3_2 = re.compile(
            r'^Flow control Send\s+:\s+(?P<flow_control_send>[\w\s]+)$')
        
        # Administrative Speed  : 10000
        p3_3 = re.compile(
            r'^Administrative Speed\s+:\s+(?P<administrative_speed>\w+)$')
        
        # Administrative Duplex : full
        p3_4 = re.compile(
            r'^Administrative Duplex\s+:\s+(?P<administrative_duplex>[\w\s]+)$')
        
        # Operational Speed     : 10000
        p3_5 = re.compile(
            r'^Operational Speed\s+:\s+(?P<operational_speed>\w+)$')
        
        # Operational Duplex    : full
        p3_6 = re.compile(
            r'^Operational Duplex\s+:\s+(?P<operational_duplex>[\w\s]+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # General SFP Information
            m = p1.match(line)
            if m:
                sfp_info_dict = ret_dict.setdefault('sfp_info',{})

            # Vendor Name           :   CISCO-EXCELIGHT
            m = p1_1.match(line)
            if m:
                sfp_info_dict['vendor_name'] = m.groupdict()['vendor_name']
                continue

            # Vendor Part Number    :   SPP5101SR-C1 
            m = p1_2.match(line)
            if m:
                sfp_info_dict['cisco_part_number'] = m.groupdict()['part_number']
                continue

            # Vendor Revision       :   0x41 0x20 0x20 0x20
            m = p1_3.match(line)
            if m:
                sfp_info_dict['vendor_revision'] = m.groupdict()['vendor_revision']
                continue

            # Vendor Serial Number  :   ECL1249000S 
            m = p1_4.match(line)
            if m:
                sfp_info_dict['serial_number'] = m.groupdict()['serial_number']
                continue

            # Identifier            :   SFP/SFP+
            m = p1_5.match(line)
            if m:
                sfp_info_dict['product_identifier'] = m.groupdict()['product_identifier']
                continue

            # Connector             :   LC connector
            m = p1_6.match(line)
            if m:
                sfp_info_dict['connector_type'] = m.groupdict()['connector_type']
                continue

            # Extended ID Fields
            m = p2.match(line)
            if m:
                extended_id_fileds = ret_dict.setdefault('extended_id_fileds',{})
                continue
            
            # Options               :   0x00 0x1A
            m = p2_0.match(line)
            if m:
                extended_id_fileds['options'] = m.groupdict()['options']
                continue
            
            # BR, max               :   0x00
            m = p2_1.match(line)
            if m:
                extended_id_fileds['br_max'] = m.groupdict()['br_max']
                continue
            
            # BR, min               :   0x00
            m = p2_2.match(line)
            if m:
                extended_id_fileds['br_min'] = m.groupdict()['br_min']
                continue
            
            # Date code             :   161031
            m = p2_3.match(line)
            if m:
                extended_id_fileds['date_code'] = int(m.groupdict()['date_code'])
                continue
            
            # Diag monitoring       :   Implemented
            m = p2_4.match(line)
            if m:
                extended_id_fileds['diag_monitoring'] = m.groupdict()['diag_monitoring']
                continue
            
            # Internally calibrated :   Yes
            m = p2_5.match(line)
            if m:
                extended_id_fileds['internally_calibrated'] = m.groupdict()['internally_calibrated']
                continue
            
            # Exeternally calibrated:   No
            m = p2_6.match(line)
            if m:
                extended_id_fileds['exeternally_calibrated'] = m.groupdict()['exeternally_calibrated']
                continue
            
            # Rx.Power measurement  :   Avg.Power
            m = p2_7.match(line)
            if m:
                extended_id_fileds['rx_power_measurement'] = m.groupdict()['rx_power_measurement']
                continue
            
            # Address Change        :   Not Required
            m = p2_8.match(line)
            if m:
                extended_id_fileds['address_change'] = m.groupdict()['address_change']
                continue
            
            # CC_EXT                :   0x32
            m = p2_9.match(line)
            if m:
                extended_id_fileds['cc_ext'] = m.groupdict()['cc_ext']
                continue

            # Other Information
            m = p3.match(line)
            if m:
                other_information = ret_dict.setdefault('other_information',{})
                continue

            # Chk for link status   : 00
            m = p3_0.match(line)
            if m:
                other_information['chk_for_link_status'] = m.groupdict()['chk_for_link_status']
                continue
            
            # Flow control Receive  : ON
            m = p3_1.match(line)
            if m:
                other_information['flow_control_receive'] = m.groupdict()['flow_control_receive']
                continue
            
            # Flow control Send     : Off
            m = p3_2.match(line)
            if m:
                other_information['flow_control_send'] = m.groupdict()['flow_control_send']
                continue
            
            # Administrative Speed  : 10000
            m = p3_3.match(line)
            if m:
                other_information['administrative_speed'] = m.groupdict()['administrative_speed']
                continue
            
            # Administrative Duplex : full
            m = p3_4.match(line)
            if m:
                other_information['administrative_duplex'] = m.groupdict()['administrative_duplex']
                continue
            
            # Operational Speed     : 10000
            m = p3_5.match(line)
            if m:
                other_information['operational_speed'] = m.groupdict()['operational_speed']
                continue
            
            # Operational Duplex    : full
            m = p3_6.match(line)
            if m:
                other_information['operational_duplex'] = m.groupdict()['operational_duplex']
                continue

        return ret_dict
    
# ==========================
# Schema for:
#  * 'show idprom tan switch {number}'
#  * 'show idprom tan'
# ==========================
class ShowIdpromTanSchema(MetaParser):
    """Schema for:
        show idprom tan switch {switch_num}
        show idprom tan switch all
        show idprom tan"""

    schema = {
        'switch': {
            Any(): {
                'switch_num': int,
                'part_num': str,
                'revision_num': Or(int, str),
            },
        }
    }
    
class ShowIdpromTan(ShowIdpromTanSchema):
    """Parser for:
        show idprom tan switch {switch_num}
        show idprom tan switch all
        show idprom tan
         """

    cli_command = ['show idprom tan switch {switch_num}',
                    'show idprom tan']

    def cli(self, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # Switch 01 ---------
        p1 = re.compile(r"^Switch\s+(?P<switch_num>\d+)$")
        # Module 1 Idprom:
        p1_startrek = re.compile(r"^Module\s+(?P<switch_num>\d+)\s+Idprom:$")

        # Top Assy. Part Number           : 68-101195-01
        p2 = re.compile(r"^Top\s+Assy.\s+Part\s+Number\s+:\s+(?P<part_num>\d+-\d+-\d+)$")

        # Top Assy. Revision Number       : 31
        p3 = re.compile(r"^Top\s+Assy.\s+Revision\s+Number\s+:\s+(?P<revision_num>\w+)$")
        # Top Assy. Revision      : 31
        p3_startrek = re.compile(r"^Top\s+Assy.\s+Revision\s+:\s+(?P<revision_num>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Switch 01 ---------
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                switch_var = dict_val['switch_num']
                switch_group = ret_dict.setdefault('switch', {})
                sw_dict = ret_dict['switch'].setdefault(switch_var, {})
                sw_dict['switch_num'] = int(switch_var)
                continue

            #Module 1 Idprom:
            m = p1_startrek.match(line)
            if m:
                dict_val = m.groupdict()
                switch_var = dict_val['switch_num']
                switch_group = ret_dict.setdefault('switch', {})
                sw_dict = ret_dict['switch'].setdefault(switch_var, {})
                sw_dict['switch_num'] = int(switch_var)
                continue

            # Top Assy. Part Number           : 68-101195-01
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                part_num_var = dict_val['part_num']
                sw_dict['part_num'] = part_num_var
                continue

            # Top Assy. Revision Number       : D0
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                revision_part_num = dict_val['revision_num']
                try:
                    sw_dict['revision_num'] = int(revision_part_num)
                except ValueError:
                    sw_dict['revision_num'] = revision_part_num
                continue

            # Top Assy. Revision      : D0
            m = p3_startrek.match(line)
            if m:
                dict_val = m.groupdict()
                revision_part_num = dict_val['revision_num']
                try:
                    sw_dict['revision_num'] = int(revision_part_num)
                except ValueError:
                    sw_dict['revision_num'] = revision_part_num
                break
                

        return ret_dict 
