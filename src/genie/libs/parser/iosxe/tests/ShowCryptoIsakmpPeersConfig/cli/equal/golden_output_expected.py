expected_output = {
  "peers": {
    "192.168.1.1": {
      "key_exchange": "IKEv1",
      'authentication_method': 'Pre-Shared Key',
      "encryption": "AES-256",
      "hashing": "SHA-256",
      "dh_group": "Group 14",
      "lifetime": 86400,
      "local_id": "router.local",
      "remote_id": "peer.remote"
    },
    "192.168.2.1": {
      "key_exchange": "IKEv2",
      "authentication_method": "RSA-SIG",
      "encryption": "AES-128",
      "hashing": "SHA-1",
      "dh_group": "Group 5",
      "lifetime": 28800,
      "local_id": "router.local",
      "remote_id": "peer.remote"
    }
  }
}
