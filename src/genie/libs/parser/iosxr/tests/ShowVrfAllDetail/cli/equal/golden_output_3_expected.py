
expected_output = {
   "**nVSatellite":{
      "vrf_mode":"regular",
      "description":"not set",
      "interfaces":[
         "nV-Loopback0"
      ],
      "address_family":{
         "ipv4 unicast":{
            
         },
         "ipv6 unicast":{
            
         }
      }
   },
   "INET_MASIVO_GPON":{
      "route_distinguisher":"11664:125000182",
      "vrf_mode":"regular",
      "description":"not set",
      "address_family":{
         "ipv4 unicast":{
            "route_target":{
               "11664:180":{
                  "route_target":"11664:180",
                  "rt_type":"import"
               },
               "11664:181":{
                  "route_target":"11664:181",
                  "rt_type":"import"
               },
               "11664:182":{
                  "route_target":"11664:182",
                  "rt_type":"both"
               }
            },
            "route_policy":{
               "import":"INET_GPON_IN_OLLEROS",
               "export":"INET_GPON_OUT_OLLEROS"
            }
         },
         "ipv6 unicast":{
            
         }
      }
   },
   "INET_MASIVO_HFC":{
      "route_distinguisher":"11664:125000154",
      "vrf_mode":"regular",
      "description":"-- Conexion a ngry01rt33--",
      "interfaces":[
         "Bundle-Ether100.600"
      ],
      "address_family":{
         "ipv4 unicast":{
            "route_target":{
               "11664:154":{
                  "route_target":"11664:154",
                  "rt_type":"both"
               }
            }
         },
         "ipv6 unicast":{
            
         }
      }
   },
   "UPLINK_MASIVO_GPON":{
      "route_distinguisher":"11664:125000180",
      "vrf_mode":"regular",
      "description":"not set",
      "interfaces":[
         "Bundle-Ether100.500"
      ],
      "address_family":{
         "ipv4 unicast":{
            "route_target":{
               "11664:182":{
                  "route_target":"11664:182",
                  "rt_type":"import"
               },
               "11664:180":{
                  "route_target":"11664:180",
                  "rt_type":"export"
               }
            }
         },
         "ipv6 unicast":{
            
         }
      }
   }
}