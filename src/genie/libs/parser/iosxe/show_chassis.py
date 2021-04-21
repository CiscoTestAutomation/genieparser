import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================
# Schema for:
#  * 'show chassis'
# =================
class ShowChassisSchema(MetaParser):
    """Schema for show chassis."""

    schema = {
        "chassis_mac_address": str,
        "mac_wait_time": str,
        "redun_port_type": str,
        "chassis_index" : {
            int : {
                "role": str,
                "mac_address": str,
                "priority": int,
                "hw_version": str,
                "current_state": str,
                "ip_address": str
            }
        }
    }


# =================
# Parser for:
#  * 'show chassis'
# =================
class ShowChassis(ShowChassisSchema):
    """Parser for show chassis"""

    cli_command = ['show chassis']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output=output

        # Chassis/Stack Mac Address : 58bf.eaff.be5c - Local Mac Address
        # Mac persistency wait time: Indefinite
        # Local Redundancy Port Type: Twisted Pair
        #                                             H/W   Current
        # Chassis#   Role    Mac Address     Priority Version  State                 IP
        # -------------------------------------------------------------------------------------
        # 1       Standby  58bf.eaff.be5c     2      V02     Ready                169.254.168.52
        # *2       Active   58bf.eaff.875c     1      V02     Ready                169.254.168.54


        # Chassis/Stack Mac Address : 58bf.eaff.d8cc - Local Mac Address
        p_chassis_mac = re.compile(r"^Chassis/Stack\s+Mac\s+Address\s+:\s+(?P<chassis_mac>\S+)\s+-\s+Local\s+Mac\s+Address$")

        # Mac persistency wait time: Indefinite
        p_mac_wait = re.compile(r"^Mac\s+persistency\s+wait\s+time:\s+(?P<mac_time>\S+)$")

        # Local Redundancy Port Type: FIBRE
        p_redun_port_type = re.compile(r"^Local\s+Redundancy\s+Port\s+Type:\s+(?P<port_type>.*)$")

        # H/W   Current
        p_header_1 = re.compile(r"^H\/W\s+Current$")

        # Chassis#   Role    Mac Address     Priority Version  State                 IP
        p_header_2 = re.compile(r"^Chassis#\s+Role\s+Mac\s+Address\s+Priority\s+Version\s+State\s+IP$")

        # -------------------------------------------------------------------------------------
        p_delimiter = re.compile(r"^-------------------------------------------------------------------------------------$")

        # *1       Active   58bf.eaff.d8cc     2      V02     Ready                169.254.130.6
        p_chassis_count = re.compile(
        r"^(?P<slot>\S+)\s+(?P<role>\S+)\s+(?P<mac>\S+)\s+(?P<priority>\d+)\s+(?P<hw_version>\S+)\s+(?P<state>\S+)\s+(?P<ip>\S+)$")

        chassis_obj = {}

        for line in output.splitlines():
            line = line.strip()
            # Chassis/Stack Mac Address : 58bf.eaff.d8cc - Local Mac Address
            if p_chassis_mac.match(line):
                match = p_chassis_mac.match(line)
                chassis_obj["chassis_mac_address"] = match.group("chassis_mac")
                continue
            # Mac persistency wait time: Indefinite
            elif p_mac_wait.match(line):
                match = p_mac_wait.match(line)
                chassis_obj["mac_wait_time"] = match.group("mac_time")
                continue
            # Local Redundancy Port Type: FIBRE
            elif p_redun_port_type.match(line):
                match = p_redun_port_type.match(line)
                chassis_obj["redun_port_type"] = match.group("port_type")
                continue
            # H/W   Current
            elif p_header_1.match(line):
                continue
            # Chassis#   Role    Mac Address     Priority Version  State                 IP
            elif p_header_2.match(line):
                match = p_header_2.match(line)
                continue
            # -------------------------------------------------------------------------------------
            elif p_delimiter.match(line):
                match = p_delimiter.match(line)
                continue
            # *1       Active   58bf.eaff.d8cc     2      V02     Ready                169.254.130.6
            elif p_chassis_count.match(line):
                match = p_chassis_count.match(line)
                if not chassis_obj.get("chassis_index"):
                    chassis_obj.update({"chassis_index" : {}})
                group = match.groupdict()
                slot = int(group["slot"].replace("*", " ").strip())
                role = group["role"]
                mac_addres = group["mac"]
                priority = int(group["priority"])
                hw_version = group["hw_version"]
                current_state = group["state"]
                ip_address = group["ip"]
                chassis_obj["chassis_index"].update({ slot: {} })
                chassis_obj["chassis_index"][slot].update({ "role" : role })
                chassis_obj["chassis_index"][slot].update({ "mac_address" : mac_addres })
                chassis_obj["chassis_index"][slot].update({ "priority" : priority })
                chassis_obj["chassis_index"][slot].update({ "hw_version" : hw_version })
                chassis_obj["chassis_index"][slot].update({ "current_state" : current_state })
                chassis_obj["chassis_index"][slot].update({ "ip_address" : ip_address })

        return chassis_obj

# =====================
# Schema for:
#  * 'show chassis rmi'
# =====================
class ShowChassisRmiSchema(MetaParser):
    """Schema for show chassis rmi."""

    schema = {
        "chassis_mac_address": str,
        "mac_wait_time": str,
        "redun_port_type": str,
        "chassis_index" : {
            int : {
                "role": str,
                "mac_address": str,
                "priority": int,
                "hw_version": str,
                "current_state": str,
                "ip_address": str,
                "rmi_ip": str
            }
        }
    }


# =====================
# Parser for:
#  * 'show chassis rmi'
# =====================
class ShowChassisRmi(ShowChassisRmiSchema):
    """Parser for show chassis rmi"""

    cli_command = 'show chassis rmi'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Chassis/Stack Mac Address : 4ce1.75ff.3a92 - Local Mac Address
        # Mac persistency wait time: Indefinite
        # Local Redundancy Port Type: FIBRE
        #                                             H/W   Current
        # Chassis#   Role    Mac Address     Priority Version  State                 IP                RMI-IP
        # --------------------------------------------------------------------------------------------------------
        # *1       Active   4ce1.75ff.3a92     2      V02     Ready                169.254.138.6      10.8.138.6
        # 2       Standby  4ce1.75ff.2392     1      V02     Ready                169.254.138.7      10.8.138.7


        # Chassis/Stack Mac Address : a453.0eff.dc7a - Local Mac Address
        p_chassis_mac = re.compile(r"^Chassis/Stack\s+Mac\s+Address\s+:\s+(?P<chassis_mac>\S+)\s+-\s+Local\s+Mac\s+Address$")

        # Mac persistency wait time: Indefinite
        p_mac_wait = re.compile(r"^Mac\s+persistency\s+wait\s+time:\s+(?P<mac_time>\S+)$")

        # Local Redundancy Port Type: FIBRE
        p_redun_port_type = re.compile(r"^Local\s+Redundancy\s+Port\s+Type:\s+(?P<port_type>.*)$")

        # H/W   Current
        p_header_1 = re.compile(r"^H\/W\s+Current$")

        # Chassis#   Role    Mac Address     Priority Version  State                 IP                RMI-IP
        p_header_2 = re.compile(r"^Chassis#\s+Role\s+Mac\s+Address\s+Priority\s+Version\s+State\s+IP\s+RMI-IP$")

        # -------------------------------------------------------------------------------------
        p_delimiter = re.compile(r"^-+$")

        # *1       Active   4ce1.75ff.3a92     2      V02     Ready                169.254.138.6      10.8.138.6
        p_chassis_count = re.compile(r"^(?P<slot>\S+)\s+(?P<role>\S+)\s+(?P<mac>\S+)\s+(?P<priority>\d+)\s+(?P<hw_version>\S+)\s+(?P<state>\S+)\s+(?P<ip>\S+)\s+(?P<rmi_ip>\S+)$")

        chassis_obj = {}

        for line in output.splitlines():
            line = line.strip()
            # Chassis/Stack Mac Address : 58bf.eaff.d8cc - Local Mac Address
            m_chassis_mac = p_chassis_mac.match(line)
            if m_chassis_mac:
                chassis_obj["chassis_mac_address"] = m_chassis_mac.group("chassis_mac")
                continue
            # Mac persistency wait time: Indefinite
            m_mac_wait = p_mac_wait.match(line)
            if m_mac_wait:
                chassis_obj["mac_wait_time"] = m_mac_wait.group("mac_time")
                continue
            # Local Redundancy Port Type: Twisted Pair
            m_redun_port = p_redun_port_type.match(line)
            if m_redun_port:
                chassis_obj["redun_port_type"] = m_redun_port.group("port_type")
                continue
            # H/W   Current
            if p_header_1.match(line):
                continue
            # Chassis#   Role    Mac Address     Priority Version  State                 IP                RMI-IP
            if p_header_2.match(line):
                continue
            # -------------------------------------------------------------------------------------
            if p_delimiter.match(line):
                continue
            # *1       Active   a453.0eff.dc7a     2      V02     Ready                10.32.168.52       NA
            m_chassis_count = p_chassis_count.match(line)
            if m_chassis_count:
                group = m_chassis_count.groupdict()
                entry_dict = chassis_obj.setdefault("chassis_index", {})
                slot = int(group["slot"].replace("*", " ").strip())
                entry_dict.update(
                            { int(slot) : {
                                "role" : group["role"],
                                "mac_address" : group["mac"],
                                "priority" : int(group["priority"]),
                                "hw_version" : group["hw_version"],
                                "current_state" : group["state"],
                                "ip_address" : group["ip"],
                                "rmi_ip": group["rmi_ip"]
                                }
                            }
                        )

        return chassis_obj
