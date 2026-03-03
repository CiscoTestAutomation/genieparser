expected_output = {
 "acl": {
  "outbound": {
   "name": "outbound",
   "type": "extended",
   "aces": {
    10: {
     "sequence": 10,
     "actions": {
      "forwarding": "permit"
     },
     "protocol": "tcp",
     "source": {
      "address": "100.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "destination": {
      "address": "200.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "matches": 1000
    },
    20: {
     "sequence": 20,
     "actions": {
      "forwarding": "deny"
     },
     "protocol": "udp",
     "source": {
      "address": "100.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "destination": {
      "address": "200.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "matches": 0
    }
   }
  }
 }
}