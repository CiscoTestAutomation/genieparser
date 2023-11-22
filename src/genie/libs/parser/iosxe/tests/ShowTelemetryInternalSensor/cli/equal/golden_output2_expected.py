expected_output = {
  "instance": {
    2147483651: {
      "sensor_type": {
        "type": "yang-push periodic",
        "filter_type": "xpath",
        "filter_selector": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status|/mdt-oper-v2-data/mdt-subscriptions"
      },
      "data_collector": {
        "dc0": {
          "dc_type": "confd periodic",
          "sub_filter": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
        },
        "dc1": {
          "dc_type": "ei_do periodic",
          "sub_filter": "/mdt-oper-v2-data/mdt-subscriptions"
        }
      }
    },
    2147483650: {
      "sensor_type": {
        "type": "yang-push periodic",
        "filter_type": "xpath",
        "filter_selector": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
      },
      "data_collector": {
        "dc0": {
          "dc_type": "confd periodic",
          "sub_filter": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
        }
      }
    },
    2147483649: {
      "sensor_type": {
        "type": "yang-push periodic",
        "filter_type": "xpath",
        "filter_selector": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
      },
      "data_collector": {
        "dc0": {
          "dc_type": "confd periodic",
          "sub_filter": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
        }
      }
    },
    2147483648: {
      "sensor_type": {
        "type": "yang-push periodic",
        "filter_type": "xpath",
        "filter_selector": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
      },
      "data_collector": {
        "dc0": {
          "dc_type": "confd periodic",
          "sub_filter": "/if:interfaces-state/interface[name=\"GigabitEthernet0/0\"]/oper-status"
        }
      }
    }
  }
}
