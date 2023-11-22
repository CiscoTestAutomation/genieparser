expected_output = {
    'bp_crimson_statistics': {
        'Initialized            ': 'Yes', 
	"Config database init'd ": 'Yes', 
	'Config DB restorable   ': 'Yes', 
	'Config DB persist      ': 'Yes', 
	'Config Lock mgr DBID   ': '5', 
	"Oper database init'd   ": 'Yes', 
	'Oper Lock mgr DBID     ': '6', 
	'Garbage collections    ': '0'
    },  
    'bp_svl_crimson_statistics': {
	'Config notify mgr ID     ': '2', 
	"Config dyn tables reg'd  ": '3', 
	'Config dyn reg failures  ': '0', 
	"Config dyn tables dereg'd": '0', 
	'Config dereg deferred    ': '0', 
	'Config dereg failures    ': '0', 
	'Config table updates     ': '16', 
	'Config applied           ': '56', 
	'Config skipped           ': '8', 
	'Oper notify mgr DBID     ': '3', 
	"Oper dyn tables reg'd    ": '1',
	'Oper dyn reg failures    ': '0', 
	"Oper dyn tables dereg'd  ": '0',
	"Oper dereg's deferred    ": '0',
	'Oper dereg failures      ': '0', 
	'Oper table updates       ': '10', 
	'Dyn table failures       ': '0', 
	'Dyn table dereg failures ': '0', 
	'Pending notifications    ': '0', 
	'Notifications highwater  ': '9',
	'Notifications processed  ': '145', 
	'Notification failures    ': '0'
    },
    'bp_remote_db_statistics': {
        'get_requests': {
        'Total Requests    ': '6284',
        'Pending Requests  ': '0',
        'Timed Out Requests': '0',
        'Failed Requests   ': '0'
        },
        'set_requests': {
        'Total Requests    ': '26',
        'Pending Requests  ': '0',
        'Timed Out Requests': '0',
        'Failed Requests   ': '0'
        },
        'in_progress_requests': {
        'Type             ': 'NONE',
        'DB ID            ': '0',
        'Batch ID         ': '0',
        'OP ID            ': '0',
        'Task PID         ': '0'
        },
        'dbal_response_time': {
        'max_(ms)': 49
        },
        'record_free_failures': {
        'Total failures   ': '0'
        }
    }
}
