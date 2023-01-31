expected_output = {
   "HundredGigE1/6/0/5":{
      "access_vlan":"1",
      "access_vlan_name":"default",
      "admin_ethertype":"0x9100",
      "oper_ethertype": "0x9100",
      "encapsulation":{
         "administrative_encapsulation":"dot1q",
         "native_vlan":"200",
         "native_vlan_name":"VLAN0200",
         "operational_encapsulation":"dot1q"
      },
      "native_vlan_tagging":False,
      "negotiation_of_trunk":True,
      "operational_mode":"trunk",
      "private_vlan":{
         "encapsulation":"dot1q",
         "native_vlan_tagging":True
      },
      "switchport_enable":True,
      "switchport_mode":"trunk",
      "trunk_vlans":"all"
   }
} 
