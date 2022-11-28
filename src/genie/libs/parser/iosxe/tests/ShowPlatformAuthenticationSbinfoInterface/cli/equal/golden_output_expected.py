expected_output={
"sb_info": {
  "sb_access_vlan": 1,
  "sb_voice_vlan": 100,
  "conf_access_vlan": 1,
  "conf_voice_vlan": 100,
  "oper_access_vlan": 1,
  "oper_voice_vlan": 100,
  "def_host_access": 1,
  "auth_in_vp": True,
  "client_count": 1,
  "vlan_count": 2,
  "port_ctrl_enable": True,
  "cdp_bypass_enable": True,
  "port_mode": "CLOSED",
  "ctrl_dir": "BOTH"
 },
 "mac": {
  "Gi1/0/24": {
   "int": "Gi1/0/24",
   "mac": "001b.0c18.918d",
   "domain": "VOICE",
   "vlan": 100,
   "clent_handle": "0x94000008",
   "port_open": "0x0002",
   "flags": "None"
  }
 },
 "int_vlan": {
  "1": {
   "int": "Gi1/0/24",
   "vlan": 1,
   "domain": "DATA",
   "user_count": 1,
   "fwd_count": 0,
   "client_count": 0,
   "vp_state": 2,
   "flags": "None"
  },
  "100": {
   "int": "Gi1/0/24",
   "vlan": 100,
   "domain": "VOICE",
   "user_count": 2,
   "fwd_count": 1,
   "client_count": 1,
   "vp_state": 8,
   "flags": "None"
  }
 }
}
