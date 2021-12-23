import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ====================
# Schema for:
#  * 'show capwap client rcb'
# ====================
class ShowCapwapClientRcbSchema(MetaParser):

    """Schema for show capwap client rcb"""

    schema = {
            "admin_state": str,
            "operation_state": str,
            "name": str,
            "swver": str,
            "hwver": str,
            "mwar_ap_mgr_ip": str,
            "mwar_name": str,
            "mwar_hw_ver": str,            
            "location": str,
            "ap_mode": str,
            "ap_sub_mode": str,
            "capwap_path_mtu": str,
            "software_initiated_reload_reason": str,
            "active_window_size": str,
            "oob_image_download": str,
            "capwap_udp_lite": str,            
            "ip_prefer_mode": str,
            "ap_link_dtls_encryption": str,
            "ap_tcp_mss_adjust": str,
            "ap_tcp_mss_size": str,
            "linkauditing": str,
            "ap_group_name": str,            
            "capwap_disconnect_reason":
            {
                "controller_last_sent": str,
            },
            "cisco_trustsec_config":
            {
                "ap_inline_tagging_mode": str,
                "ap_sgacl_enforcement": str,
                "ap_override_status": str,
            },
            "total_flash_writes_since_boot": str,
            "ble_module_admin_state": str,
            "hyperlocation_admin_state": str         
            }

# ====================
# Parser for:
#  * 'show capwap client rcb'
# ====================
class ShowCapwapClientRcb(ShowCapwapClientRcbSchema):

    cli_command = 'show capwap client rcb'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
                
        capwap_client_rcb_dict = {}
        
        # AdminState                         : ADMIN_ENABLED
        p1 = re.compile(r"^AdminState\s+:\s+(?P<admin_state>.*)$")
        
        # OperationState                     : UP
        p2 = re.compile(r"^OperationState\s+:\s+(?P<operation_state>.*)$")
        
        # Name                               : AP188B.4500.5EE8
        p3 = re.compile(r"^Name\s+:\s+(?P<name>.*)$")
        
        # SwVer                              : 17.7.0.59
        p4 = re.compile(r"^SwVer\s+:\s+(?P<swver>.*)$")
        
        # HwVer                              : 1.0.0.0
        p5 = re.compile(r"^HwVer\s+:\s+(?P<hwver>.*)$")
        
        # MwarApMgrIp                        : 9.4.62.51
        p6 = re.compile(r"^MwarApMgrIp\s+:\s+(?P<mwar_ap_mgr_ip>.*)$")
        
        # MwarName                           : vidya-ewlc-5
        p7 = re.compile(r"^MwarName\s+:\s+(?P<mwar_name>.*)$")
        
        # MwarHwVer                          : 0.0.0.0
        p8 = re.compile(r"^MwarHwVer\s+:\s+(?P<mwar_hw_ver>.*)$")
        
        # Location                           : default location
        p9 = re.compile(r"^Location\s+:\s+(?P<location>.*)$")
        
        # ApMode                             : FlexConnect
        p10 = re.compile(r"^ApMode\s+:\s+(?P<ap_mode>.*)$")    
        
        # ApSubMode                          : Not Configured
        p11 = re.compile(r"^ApSubMode\s+:\s+(?P<ap_sub_mode>.*)$")  
        
        # CAPWAP Path MTU                    : 1485
        p12 = re.compile(r"^CAPWAP\s+Path\s+MTU\s+:\s+(?P<capwap_path_mtu>.*)$")
        
        # Software Initiated Reload Reason   : Controller Reload command
        p13 = re.compile(r"^Software\s+Initiated\s+Reload\s+Reason\s+:\s+(?P<software_initiated_reload_reason>.*)$")
        
        # Active Window Size                 : 1
        p14 = re.compile(r"^Active\s+Window\s+Size\s+:\s+(?P<active_window_size>.*)$")
        
        # OOB Image Download         : Enabled
        p15 = re.compile(r"^OOB\s+Image\s+Download\s+:\s+(?P<oob_image_download>.*)$")
        
        # CAPWAP UDP-Lite                    : Enabled
        p16 = re.compile(r"^CAPWAP\s+UDP-Lite\s+:\s+(?P<capwap_udp_lite>.*)$")
        
        # IP Prefer-mode                     : IPv4
        p17 = re.compile(r"^IP\s+Prefer-mode\s+:\s+(?P<ip_prefer_mode>.*)$")
        
        # AP Link DTLS Encryption            : ON
        p18 = re.compile(r"^AP\s+Link\s+DTLS\s+Encryption\s+:\s+(?P<ap_link_dtls_encryption>.*)$")
        
        # AP TCP MSS Adjust                  : Enabled
        p19 = re.compile(r"^AP\s+TCP\s+MSS\s+Adjust\s+:\s+(?P<ap_tcp_mss_adjust>.*)$")
        
        # AP TCP MSS size                    : 600
        p20 = re.compile(r"^AP\s+TCP\s+MSS\s+size\s+:\s+(?P<ap_tcp_mss_size>.*)$")
        
        # LinkAuditing                       : disabled
        p21 = re.compile(r"^LinkAuditing\s+:\s+(?P<linkauditing>.*)$")
        
        # AP Group Name                      : default-group
        p22 = re.compile(r"^AP\s+Group\s+Name\s+:\s+(?P<ap_group_name>.*)$")
        
        # Controller Last Sent: No value set
        p23 = re.compile(r"^Controller\s+Last\s+Sent:\s+(?P<controller_last_sent>.*)$")
               
        # AP Inline Tagging Mode            : Enabled
        p24 = re.compile(r"^AP\s+Inline\s+Tagging\s+Mode\s+:\s+(?P<ap_inline_tagging_mode>.*)$")
        
        # AP Sgacl Enforcement              : Enabled
        p25 = re.compile(r"^AP\s+Sgacl\s+Enforcement\s+:\s+(?P<ap_sgacl_enforcement>.*)$")
        
        # AP Override Status                : Disabled
        p26 = re.compile(r"^AP\s+Override\s+Status\s+:\s+(?P<ap_override_status>.*)$")
        
        # Total Flash Writes Since Boot      : 377
        p27 = re.compile(r"^Total\s+Flash\s+Writes\s+Since\s+Boot\s+:\s+(?P<total_flash_writes_since_boot>.*)$")
        
        # BLE Module Admin State             : Disabled
        p28 = re.compile(r"^BLE\s+Module\s+Admin\s+State\s+:\s+(?P<ble_module_admin_state>.*)$")
        
        # Hyperlocation Admin State          : Disabled
        p29 = re.compile(r"^Hyperlocation\s+Admin\s+State\s+:\s+(?P<hyperlocation_admin_state>.*)$")

        controller_last = {}
        capwap_disconnect = {"capwap_disconnect_reason":{}}
        cisco_trustsec = {}
        cisco_trustsec_config = {}

        for line in output.splitlines():
            line = line.strip() 
            # AdminState                         : ADMIN_ENABLED                                      
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                admin_state = groups['admin_state']
                capwap_client_rcb_dict.update({'admin_state': admin_state})
                continue                
        
            # OperationState                     : UP
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                operation_state = groups['operation_state']
                capwap_client_rcb_dict.update({'operation_state': operation_state})
                continue
        
            # Name                               : AP188B.4500.5EE8 
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                name = groups['name']
                capwap_client_rcb_dict.update({'name': name})
                continue
                
            # SwVer                              : 17.7.0.59
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                swver = groups['swver']
                capwap_client_rcb_dict.update({'swver': swver})
                continue
                
            # HwVer                              : 1.0.0.0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                hwver = groups['hwver']
                capwap_client_rcb_dict.update({'hwver': hwver})
                continue
                
            # MwarApMgrIp                        : 9.4.62.51
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                mwar_ap_mgr_ip = groups['mwar_ap_mgr_ip']
                capwap_client_rcb_dict.update({'mwar_ap_mgr_ip': mwar_ap_mgr_ip})
                continue
                
            # MwarName                           : vidya-ewlc-5
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                mwar_name = groups['mwar_name']
                capwap_client_rcb_dict.update({'mwar_name': mwar_name})
                continue
                
            # MwarHwVer                          : 0.0.0.0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                mwar_hw_ver = groups['mwar_hw_ver']
                capwap_client_rcb_dict.update({'mwar_hw_ver': mwar_hw_ver})
                continue
        
            # Location                           : default location
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                location = groups['location']
                capwap_client_rcb_dict.update({'location': location})
                continue
        
            # ApMode                             : FlexConnect  
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ap_mode = groups['ap_mode']
                capwap_client_rcb_dict.update({'ap_mode': ap_mode})
                continue
        
            # ApSubMode                          : Not Configured
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                ap_sub_mode = groups['ap_sub_mode']
                capwap_client_rcb_dict.update({'ap_sub_mode': ap_sub_mode})
                continue
        
            # CAPWAP Path MTU                    : 1485
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                capwap_path_mtu = groups['capwap_path_mtu']
                capwap_client_rcb_dict.update({'capwap_path_mtu': capwap_path_mtu})
                continue
        
            # Software Initiated Reload Reason   : Controller Reload command
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                software_initiated_reload_reason = groups['software_initiated_reload_reason']
                capwap_client_rcb_dict.update({'software_initiated_reload_reason': software_initiated_reload_reason})
                continue
        
            # Active Window Size                 : 1
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                active_window_size = groups['active_window_size']
                capwap_client_rcb_dict.update({'active_window_size': active_window_size})
                continue
            
            # OOB Image Download         : Enabled  # OOB Image Download 
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                oob_image_download = groups['oob_image_download']
                capwap_client_rcb_dict.update({'oob_image_download': oob_image_download})
                continue
         
            # CAPWAP UDP-Lite                    : Enabled
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                capwap_udp_lite = groups['capwap_udp_lite']
                capwap_client_rcb_dict.update({'capwap_udp_lite': capwap_udp_lite})
                continue
        
            # IP Prefer-mode                     : IPv4
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                ip_prefer_mode = groups['ip_prefer_mode']
                capwap_client_rcb_dict.update({'ip_prefer_mode': ip_prefer_mode})
                continue
        
            # AP Link DTLS Encryption            : ON
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                ap_link_dtls_encryption = groups['ap_link_dtls_encryption']
                capwap_client_rcb_dict.update({'ap_link_dtls_encryption': ap_link_dtls_encryption})
                continue
        
            # AP TCP MSS Adjust                  : Enabled
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                ap_tcp_mss_adjust = groups['ap_tcp_mss_adjust']
                capwap_client_rcb_dict.update({'ap_tcp_mss_adjust': ap_tcp_mss_adjust})
                continue
        
            # AP TCP MSS size                    : 600
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                ap_tcp_mss_size = groups['ap_tcp_mss_size']
                capwap_client_rcb_dict.update({'ap_tcp_mss_size': ap_tcp_mss_size})
                continue
        
            # LinkAuditing                       : disabled 
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                linkauditing = groups['linkauditing']
                capwap_client_rcb_dict.update({'linkauditing': linkauditing})
                continue
        
            # AP Group Name                      : default-group
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                ap_group_name = groups['ap_group_name']
                capwap_client_rcb_dict.update({'ap_group_name': ap_group_name})
                continue
        
            # Controller Last Sent: No value set
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                controller_last_sent = groups['controller_last_sent']
                controller_last["controller_last_sent"] = controller_last_sent
                capwap_disconnect["capwap_disconnect_reason"] = controller_last
                capwap_client_rcb_dict.update(capwap_disconnect)
                continue
        
            # AP Inline Tagging Mode            : Enabled
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                ap_inline_tagging_mode = groups['ap_inline_tagging_mode']
                cisco_trustsec["ap_inline_tagging_mode"] = ap_inline_tagging_mode
                continue
        
            # AP Sgacl Enforcement              : Enabled
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                ap_sgacl_enforcement = groups['ap_sgacl_enforcement']
                cisco_trustsec["ap_sgacl_enforcement"] = ap_sgacl_enforcement
                continue
        
            # AP Override Status                : Disabled
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                ap_override_status = groups['ap_override_status']
                cisco_trustsec["ap_override_status"] = ap_override_status
                cisco_trustsec_config["cisco_trustsec_config"] = cisco_trustsec
                capwap_client_rcb_dict.update(cisco_trustsec_config)
                continue
        
            # Total Flash Writes Since Boot      : 377
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                total_flash_writes_since_boot = groups['total_flash_writes_since_boot']
                capwap_client_rcb_dict.update({'total_flash_writes_since_boot': total_flash_writes_since_boot})
                continue
        
            # BLE Module Admin State             : Disabled
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                ble_module_admin_state = groups['ble_module_admin_state']
                capwap_client_rcb_dict.update({'ble_module_admin_state': ble_module_admin_state})
                continue
        
            # Hyperlocation Admin State          : Disabled
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                hyperlocation_admin_state = groups['hyperlocation_admin_state']
                capwap_client_rcb_dict.update({'hyperlocation_admin_state': hyperlocation_admin_state})
                continue
        # Return final output in dictionary format        
        return capwap_client_rcb_dict
