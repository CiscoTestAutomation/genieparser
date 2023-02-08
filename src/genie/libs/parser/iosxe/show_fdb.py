"""show_fdb.py
   supported commands:
     *  show mac address-table
     *  show mac address-table vlan {vlan}
     *  show mac address-table aging-time
     *  show mac address-table learning
     *  show mac address-table interface {interface}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common
import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

class ShowMacAddressTableSchema(MetaParser):
    """Schema for show mac address-table"""
    schema = {
        'mac_table': {
            'vlans': {
                Any(): {
                    'vlan': Or(int, str),
                    'mac_addresses': {
                        Any(): {
                            'mac_address': str,
                            Optional('drop'): {
                                'drop': bool,
                                'entry_type': str
                            },
                            Optional('interfaces'): {
                                Any(): {
                                    'interface': str,
                                    'entry_type': str,
                                    Optional('protocols'): list,
                                    Optional('entry'): str,
                                    Optional('learn'): str,
                                    Optional('age'): int
                                }
                            }
                        }
                    }
                }
            }
        },
        Optional('total_mac_addresses'): int,
    }

class ShowMacAddressTable(ShowMacAddressTableSchema):
    """Parser for show mac address-table"""

    cli_command = ['show mac address-table',
                   'show mac address-table vlan {vlan}',
                   'show mac address-table interface {interface}']

    def cli(self, vlan='', interface='', output=None):
        if output is None:
            # get output from device
            if vlan:
                out = self.device.execute(self.cli_command[1].format(vlan=vlan))
            elif interface:
                out = self.device.execute(self.cli_command[2].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = mac_dict = {}
        entry_type = entry = learn = age = ''

        # Total Mac Addresses for this criterion: 93
        p1 = re.compile(r'^Total +Mac +Addresses +for +this +criterion: +(?P<val>\d+)$')

        # 10    aaaa.bbff.8888    STATIC      Gi1/0/8 Gi1/0/9
        # 20    aaaa.bbff.8888    STATIC      Drop
        # All    0100.0cff.999a    STATIC      CPU
        p2 = re.compile(r'^(?P<entry>[\w\*] )?\s*(?P<vlan>All|[\d\-]+) +(?P<mac>[\w.]+)'
                        r' +(?P<entry_type>\w+) +(?P<intfs>\S+|[^\s]+\s[^\s]+)$')

        # Gi1/9,Gi1/10,Gi1/11,Gi1/12
        #               Router,Switch
        p3 = re.compile(r'^(?P<intfs>(vPC Peer-Link)?[\w\/\,\(\)]+)$')

        # *  101  44dd.eeff.55bb   dynamic  Yes         10   Gi1/40
        # *  102  aa11.bbff.ee55    static  Yes          -   Gi1/2,Gi1/4,Gi1/5,Gi1/6
        # *  400  0000.0000.0000    static  No           -   vPC Peer-Link
        # *  ---  0000.0000.0000    static  No           -   Router
        p4 = re.compile(r'^(?P<entry>[\w\*] )?\s*(?P<vlan>All|[\d\-]+) +(?P<mac>[\w.]+)'
                        r' +(?P<entry_type>\w+) +(?P<learn>\w+) +(?P<age>[\d\-\~]+) '
                        r'+(?P<intfs>(vPC )?[\w\/\,\-\(\)\s]+)$')

        # 964    0000.0000.0000   dynamic ip,ipx                Router
        p5 = re.compile(r'^(?P<entry>[\w\*] )?\s*(?P<vlan>All|[\d\-]+) '
                        r'+(?P<mac>[\w.]+) +(?P<entry_type>\w+) '
                        r'+(?P<protocols>[\w\,]+) '
                        r'+(?P<intfs>\S+|[^\s]+\s[^\s]+)$')
        
        for line in out.splitlines():
            line = line.strip()

            # Total Mac Addresses for this criterion: 93
            m = p1.match(line)
            if m:
                ret_dict.update({'total_mac_addresses': int(m.groupdict()['val'])})
                continue

            # 10    aaaa.bbff.8888    STATIC      Gi1/0/8 Gi1/0/9
            # 20    aaaa.bbff.8888    STATIC      Drop
            # All    0100.0cff.999a    STATIC      CPU
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac = group['mac']
                vlan = int(group['vlan']) if re.search('\d+', group['vlan']) \
                                          else group['vlan'].lower()
                intfs = group['intfs'].strip()
                vlan_dict = ret_dict.setdefault('mac_table', {}) \
                .setdefault('vlans', {}).setdefault(str(vlan), {})
                vlan_dict['vlan'] = vlan
                mac_dict = vlan_dict.setdefault('mac_addresses', {}) \
                                    .setdefault(mac, {})
                mac_dict.update({'mac_address': mac})

                if 'drop' in intfs.lower():
                    drop_dict = mac_dict.setdefault('drop', {})
                    drop_dict.update({'drop': True})
                    drop_dict.update({'entry_type': group['entry_type'].lower()})
                    continue

                for intf in intfs.replace(' ',',').split(','):
                    intf = Common.convert_intf_name(intf)
                    intf_dict = mac_dict.setdefault('interfaces', {}) \
                                        .setdefault(intf, {})
                    intf_dict.update({'interface': intf})
                    entry_type = group['entry_type'].lower()
                    intf_dict.update({'entry_type': entry_type})
                    if group['entry']:
                        entry = group['entry'].strip()
                        intf_dict.update({'entry': entry})
                continue

            # Gi1/9,Gi1/10,Gi1/11,Gi1/12
            #               Router,Switch
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intfs = group['intfs'].strip()

                if 'drop' in intfs.lower():
                    drop_dict = mac_dict.setdefault('drop', {})
                    drop_dict.update({'drop': True})
                    drop_dict.update({'entry_type': entry_type})
                    continue

                for intf in intfs.split(','):
                    intf = Common.convert_intf_name(intf)
                    intf_dict = mac_dict.setdefault('interfaces', {}) \
                                        .setdefault(intf, {})
                    intf_dict.update({'interface': intf})
                    intf_dict.update({'entry_type': entry_type})
                    if entry:
                        intf_dict.update({'entry': entry})
                    if learn:
                        intf_dict.update({'learn': learn})
                    if age:
                        intf_dict.update({'age': age})
                continue

            # *  101  44dd.eeff.55bb   dynamic  Yes         10   Gi1/40
            # *  102  aa11.bbff.ee55    static  Yes          -   Gi1/2,Gi1/4,Gi1/5,Gi1/6
            # *  400  0000.0000.0000    static  No           -   vPC Peer-Link
            # *  ---  0000.0000.0000    static  No           -   Router
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac = group['mac']
                vlan = int(group['vlan']) if re.search('\d+', group['vlan']) \
                                          else group['vlan'].lower()
                intfs = group['intfs'].strip()
                vlan_dict = ret_dict.setdefault('mac_table', {}) \
                .setdefault('vlans', {}).setdefault(str(vlan), {})
                vlan_dict['vlan'] = vlan
                mac_dict = vlan_dict.setdefault('mac_addresses', {}) \
                                    .setdefault(mac, {})
                mac_dict.update({'mac_address': mac})

                if 'drop' in intfs.lower():
                    drop_dict = mac_dict.setdefault('drop', {})
                    drop_dict.update({'drop': True})
                    drop_dict.update({'entry_type': group['entry_type'].lower()})
                    continue

                for intf in intfs.split(','):
                    intf = Common.convert_intf_name(intf)
                    intf_dict = mac_dict.setdefault('interfaces', {}) \
                                        .setdefault(intf, {})
                    intf_dict.update({'interface': intf})
                    entry_type = group['entry_type'].lower()
                    intf_dict.update({'entry_type': entry_type})
                    if group['entry']:
                        entry = group['entry'].strip()
                        intf_dict.update({'entry': entry})
                    if group['learn']:
                        learn = group['learn']
                        intf_dict.update({'learn': learn})
                    if group['age']:
                        if group['age'].isdigit():
                            age = int(group['age'])
                            intf_dict.update({'age': age})
                        else:
                            age = None
                continue

            # 964    0000.0000.0000   dynamic ip,ipx                Router
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mac = group['mac']
                vlan = int(group['vlan']) if re.search('\d+', group['vlan']) \
                                          else group['vlan'].lower()
                intfs = group['intfs'].strip()
                vlan_dict = ret_dict.setdefault('mac_table', {}) \
                .setdefault('vlans', {}).setdefault(str(vlan), {})
                vlan_dict['vlan'] = vlan
                mac_dict = vlan_dict.setdefault('mac_addresses', {}) \
                                    .setdefault(mac, {})
                mac_dict.update({'mac_address': mac})

                if 'drop' in intfs.lower():
                    drop_dict = mac_dict.setdefault('drop', {})
                    drop_dict.update({'drop': True})
                    drop_dict.update({'entry_type': group['entry_type'].lower()})
                    continue

                for intf in intfs.replace(' ',',').split(','):
                    intf = Common.convert_intf_name(intf)
                    intf_dict = mac_dict.setdefault('interfaces', {}) \
                                        .setdefault(intf, {})
                    intf_dict.update({'interface': intf})
                    entry_type = group['entry_type'].lower()
                    intf_dict.update({'entry_type': entry_type})
                    if group['entry']:
                        entry = group['entry'].strip()
                        intf_dict.update({'entry': entry})

                    if group['protocols']:
                        intf_dict.update({'protocols': group['protocols'].split(',')})
                continue

        return ret_dict


class ShowMacAddressTableAgingTimeSchema(MetaParser):
    """Schema for show mac address-table aging-time"""
    schema = {
        'mac_aging_time': int,
        Optional('vlans'): {
            Any(): {
                'mac_aging_time': int,
                'vlan': Or(int, str)
            }
        }
    }

class ShowMacAddressTableAgingTime(ShowMacAddressTableAgingTimeSchema):
    """Parser for show mac address-table aging-time"""

    cli_command = 'show mac address-table aging-time'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Global +Aging +Time: +(?P<time>\d+)$')
        p2 = re.compile(r'^(?P<vlan>\w+) +(?P<time>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Global Aging Time:    0
            m = p1.match(line)
            if m:
                ret_dict.update({'mac_aging_time': int(m.groupdict()['time'])})
                continue

            # Vlan    Aging Time
            # ----    ----------
            #   10      10
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vlan = int(group['vlan']) if re.search('\d+', group['vlan']) \
                else group['vlan'].lower()

                vlan_dict = ret_dict.setdefault('vlans', {}) \
                .setdefault(str(vlan), {})
                vlan_dict.update({'vlan': vlan})
                vlan_dict.update({'mac_aging_time': int(m.groupdict()['time'])})
                continue

        return ret_dict


class ShowMacAddressTableLearningSchema(MetaParser):
    """Schema for show mac address-table learning"""
    schema = {
        'vlans': {
            Any(): {
                'mac_learning': bool,
                'vlan': Or(int, str)
            }
        }
    }

class ShowMacAddressTableLearning(ShowMacAddressTableLearningSchema):
    """Parser for show mac address-table learning"""

    cli_command = 'show mac address-table learning'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Learning +disabled +on +vlans: +(?P<vlans>[\w\,\-\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Learning disabled on vlans: 10,101-103,105
            m = p1.match(line)
            if m:
                vlans = m.groupdict()['vlans']
                # generate the list of the vlans
                vlans = vlans.split(',')
                vlan_list = []
                for vlan in vlans:
                    vlan_list.append(vlan) if '-' not in vlan else \
                        vlan_list.extend(list(range(int(vlan.split('-')[0]), \
                            int(vlan.split('-')[1]) + 1)))
                for vlan in vlan_list:
                    try:
                        vlan = int(vlan)
                    except Exception:
                        vlan = vlan.lower()
                    ret_dict.setdefault('vlans', {}).setdefault(str(vlan), {}) \
                                                    .setdefault('mac_learning', False)
                    ret_dict.setdefault('vlans', {}).setdefault(str(vlan), {}) \
                                                    .setdefault('vlan', vlan)
                continue

        return ret_dict


# ====================================================================
#  Schema for 'show mac address-table address 0017.0100.0001 vlan 10'
# ====================================================================
class ShowMacAddressMacVlanSchema(MetaParser):
    """Schema for show mac address-table address 0017.0100.0001 vlan 10"""
    
    schema = {'macAddress':
                 {Any(): 
                     {'VlanID' : str,
                      'Type'   : str,     
                      'Ports'  : str
                    }
                },
            }

# ====================================================================
#  Parser for 'show mac address-table address 20bb.c05e.5351 vlan 100'
# ====================================================================
class ShowMacAddressMacVlan(ShowMacAddressMacVlanSchema):

    """ Parser for show mac address-table address 0017.0100.0001 vlan 10"""

    cli_command = 'show mac address-table address {mac} vlan {vlan}'

    def cli(self, mac="", vlan="", output=None):
       
        if output is None:
            cmd = self.cli_command.format(mac=mac,vlan=vlan)
            # Execute command to get output from device       
            out = self.device.execute(cmd)
        else:
            out = output

        # 10    0017.0100.0001    DYNAMIC     Fo1/0/24
        p1 = re.compile(r'^(?P<vlanid>\d+) +(?P<mac>[\w\.]+) +(?P<type>\w+) +(?P<port>\S+)$')
        
        # initial variables
        ret_dict = {}
        
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # 10    0017.0100.0001    DYNAMIC     Fo1/0/24
            m = p1.match(line)
            if m:
                group    = m.groupdict()
                vlanId  = group['vlanid']
                macAddr = group['mac']
                typ     = group['type']
                intf    = group['port']

                final_dict = ret_dict.setdefault('macAddress',{}).setdefault(macAddr,{})
                final_dict['VlanID'] = vlanId
                final_dict['Type']   = typ
                final_dict['Ports']  = intf
                continue

        return ret_dict



# ======================================================
# Parser for 'show mac address-table notification change '
# ======================================================

class ShowMacAddressTableNotificationChangeSchema(MetaParser):
    """Schema for show mac address-table notification change"""

    schema = {
        'mac_notification_feature': str,
        'Int_btwn_notifictn_trps': str,
        'no_of_mac_addr_added': str,
        'no_of_mac_addr_rmvd': str,
        'no_of_notifictns': str,
        'max_no_of_entries': str,
        'current_history_tablen': str,
        'mac_notificatn_trps': str,
    }

class ShowMacAddressTableNotificationChange(ShowMacAddressTableNotificationChangeSchema):
    """Parser for show mac address-table notification change"""

    cli_command = 'show mac address-table notification change'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # MAC Notification Feature is Disabled on the switch
        p1 = re.compile(r"^MAC\s+Notification\s+Feature\s+is\s+(?P<mac_notification_feature>\w+)\s+on\s+the\s+switch$")
        # Interval between Notification Traps : 1 secs
        p2 = re.compile(r"^Interval\s+between\s+Notification\s+Traps\s+:\s+(?P<Int_btwn_notifictn_trps>\d+)\s+secs$")
        # Number of MAC Addresses Added : 0
        p3 = re.compile(r"^Number\s+of\s+MAC\s+Addresses\s+Added\s+:\s+(?P<no_of_mac_addr_added>\d+)$")
        # Number of MAC Addresses Removed : 0
        p4 = re.compile(r"^Number\s+of\s+MAC\s+Addresses\s+Removed\s+:\s+(?P<no_of_mac_addr_rmvd>\d+)$")
        # Number of Notifications sent to NMS : 0
        p5 = re.compile(r"^Number\s+of\s+Notifications\s+sent\s+to\s+NMS\s+:\s+(?P<no_of_notifictns>\d+)$")
        # Maximum Number of entries configured in History Table : 1
        p6 = re.compile(r"^Maximum\s+Number\s+of\s+entries\s+configured\s+in\s+History\s+Table\s+:\s+(?P<max_no_of_entries>\d+)$")
        # Current History Table Length : 0
        p7 = re.compile(r"^Current\s+History\s+Table\s+Length\s+:\s+(?P<current_history_tablen>\d+)$")
        # MAC Notification Traps are Enabled
        p8 = re.compile(r"^MAC\s+Notification\s+Traps\s+are\s+(?P<mac_notificatn_trps>\w+)$")

        ret_dict = {}

        for line in output.splitlines():

            # MAC Notification Feature is Disabled on the switch
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['mac_notification_feature'] = dict_val['mac_notification_feature']
                continue

            # Interval between Notification Traps : 1 secs
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['Int_btwn_notifictn_trps'] = dict_val['Int_btwn_notifictn_trps']
                continue

            # Number of MAC Addresses Added : 0
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['no_of_mac_addr_added'] = dict_val['no_of_mac_addr_added']
                continue

            # Number of MAC Addresses Removed : 0
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['no_of_mac_addr_rmvd'] = dict_val['no_of_mac_addr_rmvd']
                continue

            # Number of Notifications sent to NMS : 0
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['no_of_notifictns'] = dict_val['no_of_notifictns']
                continue

            # Maximum Number of entries configured in History Table : 1
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['max_no_of_entries'] = dict_val['max_no_of_entries']
                continue

            # Current History Table Length : 0
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['current_history_tablen'] = dict_val['current_history_tablen']
                continue

            # MAC Notification Traps are Enabled
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['mac_notificatn_trps'] = dict_val['mac_notificatn_trps']
                continue


        return ret_dict



# ======================================================
# Parser for 'show mac address-table notification change interface {interface}'
# ======================================================

class ShowMacAddressTableNotificationChangeInterfaceSchema(MetaParser):
    """Schema for show mac address-table notification change interface HundredGigE 2/0/25"""

    schema = {
        'mac_notification_feature': str,
        'interface': str,
        'mac_added_trap': str,
        'mac_rmvd_trap': str,
    }


class ShowMacAddressTableNotificationChangeInterface(ShowMacAddressTableNotificationChangeInterfaceSchema):
    """Parser for show mac address-table notification change interface HundredGigE 2/0/25"""

    cli_command = 'show mac address-table notification change interface {interface}'

    def cli(self, interface= '', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # MAC Notification Feature is Disabled on the switch
        p1 = re.compile(r"^MAC\s+Notification\s+Feature\s+is\s+(?P<mac_notification_feature>\w+)\s+on\s+the\s+switch$")
        # HundredGigE2/0/25              Disabled       Disabled        
        p2 = re.compile(r"^(?P<interface>\S+)\s+(?P<mac_added_trap>\w+)\s+(?P<mac_rmvd_trap>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # MAC Notification Feature is Disabled on the switch
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['mac_notification_feature'] = dict_val['mac_notification_feature']
                continue

            # HundredGigE2/0/25              Disabled       Disabled        
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['interface'] = dict_val['interface']
                ret_dict['mac_added_trap'] = dict_val['mac_added_trap']
                ret_dict['mac_rmvd_trap'] = dict_val['mac_rmvd_trap']
                continue
        
        return ret_dict