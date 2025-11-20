expected_output = {
  "process": "ospfv3-1",
  "instance": "default",
  "router_id": "192.168.0.5",
  "areas": {
    "0": {
      "area_id": 0,
      "num_nodes": 6,
      "nodes": {
        "192.168.0.3": {
          "node_id": "192.168.0.3",
          "root": false,
          "pseudo": false,
          "num_prefixes": 1,
          "prefixes": [
            "192:168::3/128",
          ],
          "flags": [
            "ABR",
          ],
        },
        "192.168.0.4": {
          "node_id": "192.168.0.4",
          "root": false,
          "pseudo": false,
          "num_prefixes": 2,
          "prefixes": [
            "192:168::4/128",
            "192:168:1::4/128",
          ],
        },
        "192.168.0.4/35": {
          "node_id": "192.168.0.4/35",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "34:34:1::/64",
          ],
        },
        "192.168.0.5": {
          "node_id": "192.168.0.5",
          "root": true,
          "pseudo": false,
          "num_prefixes": 1,
          "prefixes": [
            "192:168::5/128",
          ],
          "flags": [
            "ABR",
            "ASBR",
          ],
        },
        "192.168.0.5/63": {
          "node_id": "192.168.0.5/63",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "45:45:1::/64",
          ],
        },
        "192.168.0.5/65": {
          "node_id": "192.168.0.5/65",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "35:35:1::/64",
          ],
        },
      },
    },
    "1": {
      "area_id": 1,
      "num_nodes": 18,
      "nodes": {
        "192.168.0.1": {
          "node_id": "192.168.0.1",
          "root": false,
          "pseudo": false,
          "num_prefixes": 2,
          "prefixes": [
            "192:168::1/128",
            "192:168:1::1/128",
          ],
          "flags": [
            "ASBR",
          ],
        },
        "192.168.0.2": {
          "node_id": "192.168.0.2",
          "root": false,
          "pseudo": false,
          "num_prefixes": 2,
          "prefixes": [
            "192:168::2/128",
            "192:168:1::2/128",
          ],
        },
        "192.168.0.2/35": {
          "node_id": "192.168.0.2/35",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "12:12:1::/64",
          ],
        },
        "192.168.0.2/66": {
          "node_id": "192.168.0.2/66",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "12:12:2::/64",
          ],
        },
        "192.168.0.3": {
          "node_id": "192.168.0.3",
          "root": false,
          "pseudo": false,
          "num_prefixes": 1,
          "prefixes": [
            "192:168:1::3/128",
          ],
          "flags": [
            "ABR",
          ],
        },
        "192.168.0.3/35": {
          "node_id": "192.168.0.3/35",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "13:13:1::/64",
          ],
        },
        "192.168.0.3/65": {
          "node_id": "192.168.0.3/65",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "23:23:2::/64",
          ],
        },
        "192.168.0.3/66": {
          "node_id": "192.168.0.3/66",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "23:23:1::/64",
          ],
        },
        "192.168.0.5": {
          "node_id": "192.168.0.5",
          "root": true,
          "pseudo": false,
          "num_prefixes": 1,
          "prefixes": [
            "192:168:1::5/128",
          ],
          "flags": [
            "ABR",
            "ASBR",
          ],
        },
        "192.168.0.5/35": {
          "node_id": "192.168.0.5/35",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "15:15:1::/64",
          ],
        },
        "192.168.0.5/64": {
          "node_id": "192.168.0.5/64",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "35:35:2::/64",
          ],
        },
        "192.168.0.5/66": {
          "node_id": "192.168.0.5/66",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "25:25:1::/64",
          ],
        },
        "192.168.0.6": {
          "node_id": "192.168.0.6",
          "root": false,
          "pseudo": false,
          "num_prefixes": 2,
          "prefixes": [
            "192:168::6/128",
            "192:168:1::6/128",
          ],
        },
        "192.168.0.6/35": {
          "node_id": "192.168.0.6/35",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "16:16:1::/64",
          ],
        },
        "192.168.0.6/63": {
          "node_id": "192.168.0.6/63",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "56:56:3::/64",
          ],
        },
        "192.168.0.6/64": {
          "node_id": "192.168.0.6/64",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "56:56:2::/64",
          ],
        },
        "192.168.0.6/65": {
          "node_id": "192.168.0.6/65",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "56:56:1::/64",
          ],
        },
        "192.168.0.6/66": {
          "node_id": "192.168.0.6/66",
          "root": false,
          "pseudo": true,
          "num_prefixes": 1,
          "prefixes": [
            "36:36:1::/64",
          ],
        },
      },
    },
    "2": {
      "area_id": 2,
      "num_nodes": 1,
      "nodes": {
        "192.168.0.5": {
          "node_id": "192.168.0.5",
          "root": true,
          "pseudo": false,
          "num_prefixes": 1,
          "prefixes": [
            "192:168:2::5/128",
          ],
          "flags": [
            "ABR",
            "ASBR",
          ],
        },
      },
    },
  },
}
