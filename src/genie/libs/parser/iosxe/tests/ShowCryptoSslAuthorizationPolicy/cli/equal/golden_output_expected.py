expected_output = {
  "policies": {
    "EmployeePolicy": {
      "rule": "AllowAccess",
      "user_group": "Employees",
      "permissions": "Full Access",
      "source": "Internal Network",
      "destination": "All Networks",
      "action": "Permit"
    },
    "GuestPolicy": {
      "rule": "LimitedAccess",
      "user_group": "Guests",
      "permissions": "Restricted Access",
      "source": "Guest VLAN",
      "destination": "Limited Networks",
      "action": "Permit"
    },
    "AdminPolicy": {
      "rule": "AdminAccess",
      "user_group": "Administrators",
      "permissions": "Full Access",
      "source": "Any",
      "destination": "All Networks",
      "action": "Permit"
    }
  }
}
