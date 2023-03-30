expected_output = {
        "defaultPort" : {
            "interfaces": ["GigabitEthernet1/1","GigabitEthernet1/2","GigabitEthernet1/3","GigabitEthernet1/4","GigabitEthernet1/5","GigabitEthernet1/6","GigabitEthernet1/7","GigabitEthernet1/9","GigabitEthernet1/10","GigabitEthernet1/11","GigabitEthernet1/12","GigabitEthernet1/13","GigabitEthernet1/14","GigabitEthernet1/15","GigabitEthernet1/16","GigabitEthernet1/17","GigabitEthernet1/18","GigabitEthernet1/19","GigabitEthernet1/20"],
            "alarms":"not-operating",
            "syslog":"not-operating",
            "notifies":"not-operating",
            "relay_major":""
            },
        "kali":{
            "interfaces": ["GigabitEthernet1/8"],
            "alarms":"link-fault, not-forwarding, not-operating",
            "syslog":"",
            "notifies":"",
            "relay_major":"link-fault, not-forwarding, not-operating"
            }
        }
    
