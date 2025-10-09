expected_output = {
  "subscriber_session_information": {
    "mac_address": "aaaa.bbbb.1111",
    "ip_address": "11.11.11.2",
    "session_id": "000123456",
    "state": "Active",
    "interface": "GigabitEthernet0/0/1",
    "vrf": "default",
    "username": "user@example.com",
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
  "subscriber_attributes": {
    0: {
      "attribute_type": "Location",
      "attribute_value": "New York"
    }
  },
  "subscriber_features": {
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
