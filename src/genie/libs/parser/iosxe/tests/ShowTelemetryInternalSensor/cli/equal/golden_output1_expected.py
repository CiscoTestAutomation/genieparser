expected_output = {
  "instance": {
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
