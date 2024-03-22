expected_output={
 "event_logging": {
  "client_mac": "001b.0c18.918d",
  "state": "EV_SESSION_AUTHZ_SUCCESS",
  "count": 196,
  "id": 3
 },
 "mac_logs": {
  'Dest': {
             'dest': 'Msg',
             'msg_type': 'Type',
             'result': 'Result',
             'src': 'Dest',
             'timestamp': 'Timestamp              Src',
  },
  "RCL_CLIENT": {
   "timestamp": "Sep/29  12:14:51:777",
   "src": "RCL_CLIENT",
   "dest": "RCL",
   "msg_type": "EV_SESSION_START",
   "result": "EV_PASS"
  },
  "SM_CLIENT": {
   "timestamp": "Sep/29  12:14:51:777",
   "src": "SM_CLIENT",
   "dest": "SM",
   "msg_type": "EV_SESSION_CREATE",
   "result": "EV_PASS"
  },
  "SM": {
   "timestamp": "Sep/29  12:14:51:778",
   "src": "SM",
   "dest": "BM",
   "msg_type": "EV_BM_NEW_CLIENT_CB",
   "result": "EV_PASS"
  },
  "RCL": {
   "timestamp": "Sep/29  12:14:51:778",
   "src": "SM",
   "dest": "SM_CLIENT",
   "msg_type": "EV_NEW_SESSION_CB",
   "result": "EV_PASS"
  },
  "SVM": {
   "timestamp": "Sep/29  12:14:51:779",
   "src": "SM",
   "dest": "SM_CLIENT",
   "msg_type": "EV_RAISE_PRE_EVENT_CB",
   "result": "EV_PASS"
  },
  "DOT01X": {
   "timestamp": "Sep/29  12:14:51:779",
   "src": "DOT01X",
   "dest": "CLIENT",
   "msg_type": "EV_EAP_REQ_TX",
   "result": "EV_PASS"
  },
  "CLIENT": {
   "timestamp": "Sep/29  12:14:51:787",
   "src": "SM",
   "dest": "AAA_COORD",
   "msg_type": "EV_AAA_REQUEST",
   "result": "EV_PASS"
  },
  "AAA_CLIENT": {
   "timestamp": "Sep/29  12:14:51:787",
   "src": "AAA_CLIENT",
   "dest": "AAA_CORE",
   "msg_type": "EV_AAA_REQUEST_RECEIVED",
   "result": "EV_PASS"
  },
  "RAD_CLIENT": {
   "timestamp": "Sep/29  12:14:51:788",
   "src": "RAD_CLIENT",
   "dest": "RAD_SERVER",
   "msg_type": "EV_AAA_RAD_REQUEST_SENT",
   "result": "EV_PASS"
  },
  "RAD_SERVER": {
   "timestamp": "Sep/29  12:14:51:793",
   "src": "RAD_SERVER",
   "dest": "RAD_CLIENT",
   "msg_type": "EV_AAA_RAD_RESPONSE_RECEIVED",
   "result": "EV_PASS"
  },
  "AAA_CORE": {
   "timestamp": "Sep/29  12:14:51:793",
   "src": "AAA_CORE",
   "dest": "AAA_CLIENT",
   "msg_type": "EV_AAA_RESPONSE_SENT",
   "result": "EV_PASS"
  },
  "AAA_COORD": {
   "timestamp": "Sep/29  12:14:51:873",
   "src": "SM",
   "dest": "SM_CLIENT",
   "msg_type": "EV_UNAUTHORIZE_CB",
   "result": "EV_PASS"
  }
 }
}
