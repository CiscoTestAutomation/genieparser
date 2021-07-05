expected_output = {
   "events":{
      "SSID 0":{
         1:{
            "ssid":"SSID 0",
            "event_type":"fsm_run",
            "event_name":"ACTIVE_REGISTER",
            "fsm_name":" Feature Table",
            "fsm_state":"running",
            "timestamp":"[Fri Jun 18 22:14:40.000]"
         },
         2:{
            "ssid":"SSID 0",
            "event_type":"fsm_transition",
            "event_name":"ACTIVE_REGISTER",
            "state":"READY",
            "prev_state":"CREATING",
            "timestamp":"[Fri Jun 18 22:14:40.000]"
         },
         3:{
            "ssid":"SSID 0",
            "event_type":"fsm_run",
            "event_name":"MAC_ACTIVITY",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         },
         4:{
            "ssid":"SSID 0",
            "event_type":"fsm_transition",
            "event_name":"MAC_ACTIVITY",
            "state":"MAC-REACHABLE",
            "prev_state":"MAC-STALE",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         }
      },
      "SSID 1":{
         1:{
            "ssid":"SSID 1",
            "event_type":"fsm_run",
            "event_name":"ACTIVE_REGISTER",
            "fsm_name":" Feature Table",
            "fsm_state":"running",
            "timestamp":"[Fri Jun 18 22:14:40.000]"
         },
         2:{
            "ssid":"SSID 1",
            "event_type":"fsm_transition",
            "event_name":"ACTIVE_REGISTER",
            "state":"READY",
            "prev_state":"CREATING",
            "timestamp":"[Fri Jun 18 22:14:40.000]"
         },
         3:{
            "ssid":"SSID 1",
            "event_type":"bt_entry",
            "entry_state":"Created Entry origin",
            "Static MAC":"000a.000a.000a",
            "IPV4":"1.1.1.1",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         },
         4:{
            "ssid":"SSID 1",
            "event_type":"fsm_run",
            "event_name":"LLA_RCV",
            "fsm_name":" Binding table",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         },
         5:{
            "ssid":"SSID 1",
            "event_type":"fsm_transition",
            "event_name":"LLA_RCV",
            "state":"REACHABLE",
            "prev_state":"CREATING",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         },
         6:{
            "ssid":"SSID 1",
            "event_type":"bt_entry",
            "entry_state":"changed origin",
            "Static MAC":"000a.000a.000a",
            "IPV4":"1.1.1.1",
            "timestamp":"[Wed Jun 30 17:03:14.000]"
         },
         7:{
            "ssid":"SSID 1",
            "event_type":"fsm_run",
            "event_name":"T2_REACHABLE_TIMER",
            "fsm_name":" Binding table",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:08:24.000]"
         },
         8:{
            "ssid":"SSID 1",
            "event_type":"fsm_run",
            "event_name":"INACTIVE",
            "fsm_name":" Binding table",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:08:24.000]"
         },
         9:{
            "ssid":"SSID 1",
            "event_type":"fsm_transition",
            "event_name":"INACTIVE",
            "state":"STALE",
            "prev_state":"REACHABLE",
            "timestamp":"[Wed Jun 30 17:08:24.000]"
         },
         10:{
            "ssid":"SSID 1",
            "event_type":"bt_entry",
            "entry_state":"changed origin",
            "Static MAC":"000a.000a.000a",
            "IPV4":"1.1.1.1",
            "timestamp":"[Wed Jun 30 17:08:24.000]"
         }
      },
      "SSID 2":{
         1:{
            "ssid":"SSID 2",
            "event_type":"fsm_run",
            "event_name":"ACTIVE_REGISTER",
            "fsm_name":" Feature Table",
            "fsm_state":"running",
            "timestamp":"[Fri Jun 25 19:52:11.000]"
         },
         2:{
            "ssid":"SSID 2",
            "event_type":"fsm_transition",
            "event_name":"ACTIVE_REGISTER",
            "state":"READY",
            "prev_state":"CREATING",
            "timestamp":"[Fri Jun 25 19:52:11.000]"
         }
      },
      "SSID 1000000":{
         1:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_run",
            "event_name":"MAC_T1",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:08:14.000]"
         },
         2:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_transition",
            "event_name":"MAC_T1",
            "state":"MAC-VERIFY",
            "prev_state":"MAC-REACHABLE",
            "timestamp":"[Wed Jun 30 17:08:14.000]"
         },
         3:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_run",
            "event_name":"MAC_R2",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Wed Jun 30 17:08:14.000]"
         },
         4:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_transition",
            "event_name":"MAC_R2",
            "state":"MAC-STALE",
            "prev_state":"MAC-VERIFY",
            "timestamp":"[Wed Jun 30 17:08:14.000]"
         },
         5:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_run",
            "event_name":"MAC_T3",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Thu Jul 01 19:08:15.000]"
         },
         6:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_run",
            "event_name":"MAC_R2",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Thu Jul 01 19:08:15.000]"
         },
         7:{
            "ssid":"SSID 1000000",
            "event_type":"fsm_run",
            "event_name":"MAC_T5",
            "fsm_name":" sisf_mac_fsm",
            "fsm_state":"running",
            "timestamp":"[Thu Jul 01 19:08:16.000]"
         }
      }
   }
}