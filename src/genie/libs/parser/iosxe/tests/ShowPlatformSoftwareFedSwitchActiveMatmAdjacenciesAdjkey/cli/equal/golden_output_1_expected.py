expected_output = {
   "adj_id":{
      3849:{
         "if_number":"0x420065",
         "vni_id":200199,
         "len":60,
         "vlan_id":99,
         "encap":"VXLAN",
         "link_type":"V4",
         "source_ip":"172.11.1.1",
         "destination_ip":"172.11.1.22",
         "si_handle":"0x7f95815d74d8",
         "ri_handle":"0x7f95815a4528",
         "l3_mri_handle":"0x0",
         "di_handle":"0x0",
         "object_type":"UC"
      }
   },
   "created_time":"2023/01/24 05:25:43.658",
   "last_modified":"2023/01/24 05:25:43.658",
   "current_time":"2023/01/24 07:52:27.709",
   "asic_instance":{
      0:{
         "ri":226,
         "rewrite_type":"AL_RRM_REWRITE_LVX_IPV4_L2_PAYLOAD_ENCAP_EPG(116)",
         "mapped_ri":"LVX_L3_ENCAP_L2_PAYLOAD_EPG(135)",
         "src_ip":"172.11.1.1",
         "dst_ip":"172.11.1.22",
         "dst_mac":"0x9f:0x00:0x00",
         "src_mac":"0x00:0x00:0x00",
         "ipv4_ttl":0,
         "iid_present":0,
         "lisp_iid":200199,
         "lisp_flags":0,
         "dst_port":4789,
         "update_l3if":0,
         "is_ttl_prop":0,
         "l3if_le":"126 (0)",
         "port_le":"318 (0)",
         "vlan_le":"68 (0)"
      },
      1:{
         "ri":226,
         "rewrite_type":"AL_RRM_REWRITE_LVX_IPV4_L2_PAYLOAD_ENCAP_EPG(116)",
         "mapped_ri":"LVX_L3_ENCAP_L2_PAYLOAD_EPG(135)",
         "src_ip":"172.11.1.1",
         "dst_ip":"172.11.1.22",
         "dst_mac":"0x9f:0x00:0x00",
         "src_mac":"0x00:0x00:0x00",
         "ipv4_ttl":0,
         "iid_present":0,
         "lisp_iid":200199,
         "lisp_flags":0,
         "dst_port":4789,
         "update_l3if":0,
         "is_ttl_prop":0,
         "l3if_le":"126 (0)",
         "port_le":"318 (0)",
         "vlan_le":"68 (0)"
      }
   }
}
