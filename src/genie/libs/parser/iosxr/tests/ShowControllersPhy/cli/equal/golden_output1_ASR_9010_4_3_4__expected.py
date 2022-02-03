expected_output = {
   "interface":{
      "TenGigE0/0/0/0":{
         "present":True,
         "eeprom_port":"0",
         "xcvr_type": "XFP",
         "connector_type":"LC",
         "encoding":"64B/66B, SONET Scrambled, NRZ,",
         "vendor_info":{
            "vendor_name":"CISCO-OPNEXT",
            "vendor_oui":"00.0b.40",
            "vendor_part_number":"TRF5013FN-CB030   (rev.: 00)",
            "vendor_serial_number":"ONT152811DQ"
         },
         "laser_wavelength":"1310.000 nm",
         "operational_status":{
            "module":{
               "threshold_values":{
                  "temperature":{
                     "alarm_high":"90.000",
                     "warning_high":"85.000",
                     "warning_low":"-5.000",
                     "alarm_low":"-10.000"
                  },
                  "voltage":{
                     "alarm_high":"0.000 Volt",
                     "warning_high":"0.000 Volt",
                     "warning_low":"0.000 Volt",
                     "alarm_low":"0.000 Volt"
                  }
               },
               "current_values":{
                  "temperature":"33.074",
                  "voltage":"0.000 Volt"
               }
            },
            "optical_lanes":{
               "threshold_values":{
                  "tx_power":{
                     "alarm_high":"0.89120 mW (-0.50025 dBm)",
                     "warning_high":"0.79430 mW (-1.00015 dBm)",
                     "warning_low":"0.25110 mW (-6.00153 dBm)",
                     "alarm_low":"0.22380 mW (-6.50140 dBm)"
                  },
                  "rx_power":{
                     "alarm_high":"1.25890 mW (0.99991 dBm)",
                     "warning_high":"1.12200 mW (0.49993 dBm)",
                     "warning_low":"0.03630 mW (-14.40093 dBm)",
                     "alarm_low":"0.03230 mW (-14.90797 dBm)"
                  }
               },
               "current_values":{
                  "lane_0":{
                     "laser_bias_current":"53.036 mAmps",
                     "tx_power":"0.56140 mW (-2.50728 dBm)",
                     "rx_power":"0.43100 mW (-3.65523 dBm)"
                  }
               }
            }
         }
      },
   }
}