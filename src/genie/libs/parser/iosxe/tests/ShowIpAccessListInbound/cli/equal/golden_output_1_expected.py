expected_output = {
 "acls": {
  "inbound": {
   "name": "inbound",
   "type": "extended",
   "aces": {
    "10": {
     "sequence": 10,
     "action": "deny",
     "protocol": "tcp",
     "source": {
      "address": "200.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "destination": {
      "address": "100.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "matches": 0
    },
    "20": {
     "sequence": 20,
     "action": "permit",
     "protocol": "udp",
     "source": {
      "address": "200.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "destination": {
      "address": "100.1.1.0",
      "wildcard_bits": "0.0.0.255"
     },
     "matches": 0
    }
   }
  }
 }
}