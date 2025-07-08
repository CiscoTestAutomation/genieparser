expected_output={
    "sno":{
        1:{
            "event":"REPLACE",
            "result":"Failure",
            "username":"campus",
            "timestamp":"05/15 18:13:46",
            "target_config":"checkpoint1"
        },
        2:{
            "event":"ROLLBACK-ON-FL",
            "result":"Failure",
            "username":"campus",
            "timestamp":"05/15 18:11:42",
            "target_config":"snapshot.cfg"
        },
        3:{
            "event":"ROLLBACK",
            "result":"Success",
            "username":"campus",
            "timestamp":"05/15 18:11:11",
            "target_config":"checkpoint1"
        }
    }
}