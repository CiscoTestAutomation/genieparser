expected_output = {
   "interface": {
      "GigabitEthernet0/4/0/0":{
         "present":True,
         "eeprom_port": "0",
         "xcvr_type":"SFP",
         "ethernet_compliance_codes":"1000BASE-LX",
         "encoding":"8B10B",
         "nominal_bit_rate":"1300 Mbps",
         "vendor_info":{
            "vendor_name":"CISCO-FINISAR",
            "vendor_oui":"00.90.65",
            "vendor_part_number":"FTRJ1319P1BTL-C6 (rev.: C   )",
            "vendor_serial_number":"FNS15411WEH"
         },
         "laser_wavelength":"1310 nm (fraction: 0.00 nm)",
         "date_code":"11/10/07  lot code:",
         "operational_status":{
            "module":{
               "threshold_values":{
                  "temperature":{
                     "alarm_high":"+110.000 C",
                     "warning_high":"+93.000 C",
                     "warning_low":"-30.000 C",
                     "alarm_low":"-40.000 C"
                  },
                  "voltage":{
                     "alarm_high":"3.900 Volt",
                     "warning_high":"3.700 Volt",
                     "warning_low":"2.900 Volt",
                     "alarm_low":"2.700 Volt"
                  }
               },
               "current_values":{
                  "temperature":"30.145",
                  "voltage":"3.314 Volt"
               }
            },
            "optical_lanes":{
               "current_values":{
                  "lane_0":{
                     "laser_bias_current":"21.370 mAmps",
                     "tx_power":"0.20960 mW (-6.78609 dBm)",
                     "rx_power":"0.000 mW (<-40.00 dBm)"
                  }
               }
            }
         },
         "part_number":"10-2144-01 (ver.: V01 )",
         "product_id":"SFP-GE-L"
      },
   }
}