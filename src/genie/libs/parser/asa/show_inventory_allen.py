''' show_inventory.py

ASA parserr for the following show commands:
    * show inventory
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema


# Schema for 'show inventory'
# =============================================
class ShowInventorySchema(MetaParser):
    """Schema for
        * show inventory
    """

    schema = {
        'inventory': {
        	'name': str,
        	'descr': str,
        	'pid': str,
        	'vid': str,
        	'sn': str
        }
    }

# =============================================
# Parser for 'show inventory'
# =============================================
class ShowInventory(ShowInventorySchema):
    """Parser for
        * show interface summary
    """

    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Name: "module 2", DESCR: "WS-SVC-ASASM-1 Adaptive Security Appliance Service Module"
        p1 = re.compile(r'^Name: +"(?P<name>[\w\d\ \.\(\)\-]+)+"+,* +DESCR:+ "'
        	'+(?P<descr>[\w\d\ \.\(\)\-]+)+"$')

		# PID: WS-SVC-ASA-SM1    , VID: V02     , SN: SAL2052037Y
        p2 = re.compile(r'^PID: +(?P<pid>[\w\d\.\(\)\-]+)+[\ ]+, +VID: '
        	'+(?P<vid>[\w\d\.\(\)\-]+)+[\ ]+,+[\ ]+SN: +(?P<sn>[\w\d\ \.\(\)\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Name: "module 2", DESCR: "WS-SVC-ASASM-1 Adaptive Security Appliance Service Module"
            m = p1.match(line)
            if m:
            	groups = m.groupdict()
            	dict_inventory = ret_dict.setdefault('inventory', {})
            	dict_inventory.update({'name': groups['name']})
            	dict_inventory.update({'descr': groups['descr']})
            	continue

            # PID: WS-SVC-ASA-SM1    , VID: V02     , SN: SAL2052037Y
            m = p2.match(line)
            if m:
            	groups = m.groupdict()
            	dict_inventory.update({'pid': groups['pid']})
            	dict_inventory.update({'vid': groups['vid']})
            	dict_inventory.update({'sn': groups['sn']})
            	continue

        return ret_dict