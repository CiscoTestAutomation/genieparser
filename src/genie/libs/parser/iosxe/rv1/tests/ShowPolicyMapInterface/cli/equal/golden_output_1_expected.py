expected_output = {
 "interface": {
  "TenGigabitEthernet0/0/15": {
   "service_policy": {
    "output": {
     "wred": {
      "class_map": {
       "prec1": {
        "match_mode": "match-all",
        "packets": 0,
        "bytes": 0,
        "rate": {
         "interval_minutes": 5,
         "offered_bps": 0,
         "drop_bps": 0
        },
        "match": "precedence 1",
        "queueing": True,
        "queue_limit": {
         "packets": 640
        },
        "queue_counters": {
         "queue_depth": 0,
         "total_drops": 0,
         "no_buffer_drops": 0
        },
        "output_packets": 0,
        "output_bytes": 0,
        "shape": {
         "type": "average",
         "cir_bps": 1000000000,
         "bc_bytes": 10000000,
         "be_bytes": 10000000,
         "target_rate_bps": 1000000000
        }
       },
       "prec2": {
        "match_mode": "match-all",
        "packets": 0,
        "bytes": 0,
        "rate": {
         "interval_minutes": 5,
         "offered_bps": 0,
         "drop_bps": 0
        },
        "match": "precedence 2",
        "queueing": True,
        "queue_limit": {
         "bytes": 5120
        },
        "queue_counters": {
         "queue_depth": 0,
         "total_drops": 0,
         "no_buffer_drops": 0
        },
        "output_packets": 0,
        "output_bytes": 0,
        "shape": {
         "type": "average",
         "cir_bps": 20000000,
         "bc_bytes": 80000,
         "be_bytes": 80000,
         "target_rate_bps": 20000000
        }
       },
       "prec3": {
        "match_mode": "match-all",
        "packets": 0,
        "bytes": 0,
        "rate": {
         "interval_minutes": 5,
         "offered_bps": 0,
         "drop_bps": 0
        },
        "match": "precedence 3",
        "queueing": True,
        "queue_limit": {
         "ms": 10,
         "bytes": 375000
        },
        "queue_counters": {
         "queue_depth": 0,
         "total_drops": 0,
         "no_buffer_drops": 0
        },
        "output_packets": 0,
        "output_bytes": 0,
        "bandwidth_kbps": 300000,
        "shape": {
         "type": "average",
         "cir_bps": 1000000000,
         "bc_bytes": 4000000,
         "be_bytes": 4000000,
         "target_rate_bps": 1000000000
        },
        "random_detect": {
         "exp_weight_constant": 9,
         "exp_weight_constant_fraction": "1/512",
         "mean_queue_depth": {
          "ms": 0,
          "bytes": 0
         },
         "classes": {
          0: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 2, "bytes": 93750},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          1: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 2, "bytes": 105468},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          2: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 3, "bytes": 117187},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          3: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 2, "bytes": 75000},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          4: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 3, "bytes": 140625},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          5: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 4, "bytes": 152343},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          6: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 4, "bytes": 164062},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          },
          7: {
           "transmitted": {"pkts": 0, "bytes": 0},
           "random_drop": {"pkts": 0, "bytes": 0},
           "tail_drop": {"pkts": 0, "bytes": 0},
           "minimum_threshold": {"ms": 4, "bytes": 175781},
           "maximum_threshold": {"ms": 5, "bytes": 187500},
           "mark_prob": "1/10"
          }
         }
        }
       },
       "class-default": {
        "match_mode": "match-any",
        "packets": 0,
        "bytes": 0,
        "rate": {
         "interval_minutes": 5,
         "offered_bps": 0,
         "drop_bps": 0
        },
        "match": "any",
        "queue_limit": {
         "packets": 41666
        },
        "queue_counters": {
         "queue_depth": 0,
         "total_drops": 0,
         "no_buffer_drops": 0
        },
        "output_packets": 0,
        "output_bytes": 0
       }
      }
     }
    }
   }
  }
 }
}