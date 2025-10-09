expected_output = {
  "subscriber_session_information": {
    "ip_address": "11.11.11.2",
    "session_id": "000123456",
    "state": "Active",
    "username": "user@example.com",
    "mac_address": "aa:bb:cc:dd:ee:ff",
    "interface": "GigabitEthernet0/0/1",
    "vrf": "default",
    "service_policy": "qos_policy",
    "authentication_status": "Authenticated",
    "session_duration": "00:45:23",
    "last_status_change": "2023-10-05 14:30:00 UTC",
    "accounting_method": "Radius",
    "accounting_status": "Accounting-Active",
    "total_input_packets": 123456,
    "total_output_packets": 654321,
    "total_input_bytes": 12345678,
    "total_output_bytes": 87654321
  },
  "additional_subscriber_attributes": {
    0: {
      "attribute_type": "Custom",
      "attribute_value": "Value"
    },
    1: {
      "attribute_type": "Location",
      "attribute_value": "New York"
    }
  },
  "subscriber_feature_information": {
    0: {
      "feature_name": "QoS",
      "feature_status": "Enabled",
      "feature_configuration": "Standard"
    },
    1: {
      "feature_name": "Firewall",
      "feature_status": "Disabled"
    }
  }
}
