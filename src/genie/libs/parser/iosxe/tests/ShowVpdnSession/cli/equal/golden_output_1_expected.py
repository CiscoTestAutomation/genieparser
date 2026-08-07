expected_output = {
 "vpdn": {
  "l2tp": {
   "total_tunnels": "X",
   "total_sessions": "Y",
   "sessions": [
    {
     "local_id": 4,
     "remote_id": 691,
     "tunnel_id": 13695,
     "interface": "Se0/0",
     "username": "user@domain.com",
     "state": "est",
     "last_change": "00:06:00",
     "unique_id": 4
    }
   ]
  },
  "l2f": {
   "total_tunnels": "X",
   "total_sessions": "Y",
   "sessions": [
    {
     "clid": 1,
     "mid": 2,
     "username": "user@domain.com",
     "interface": "SSS Circuit",
     "state": "open",
     "unique_id": 10
    }
   ]
  },
  "pppoe": {
   "total_tunnels": "X",
   "total_sessions": "Y",
   "sessions": [
    {
     "uid": 3,
     "sid": 1,
     "remote_mac": "0030.949b.b4a0",
     "local_mac": "0010.7b90.0840",
     "outgoing_interface": "Fa2/0",
     "interface": "N/A",
     "vast": None,
     "session_state": "CNCT_FWDED"
    },
    {
     "uid": 6,
     "sid": 2,
     "remote_mac": "0030.949b.b4a0",
     "local_mac": "0010.7b90.0840",
     "outgoing_interface": "Fa2/0",
     "interface": "Vi1.1",
     "vast": "UP",
     "session_state": "CNCT_PTA"
    }
   ]
  }
 }
}