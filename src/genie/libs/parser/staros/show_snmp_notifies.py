"""starOS implementation of show_snmp_notifies.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
#from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSNMPNotifiesSchema(MetaParser):
    """Schema for show snmp notifies"""
    schema = {
	'statistics': {
		'summary': {
			'Total number of notifications' : str,
			'Last notification sent' : str,
			'Notification sending is' : str,
			'Notifications last disabled': str,
			'Notifications in current period' : str,
			'Notifications in previous period' : str,
			'Notification monitor period' : str,
			'Total number of notifications Disabled' : str,
			},
		'traps': {
			Any(): {
				'Gen': str,
				'Disc': str,
				'Disable': str,
				'Last Generated': str,
			    },
		    },
	    }
    }

class ShowNotifies(ShowSNMPNotifiesSchema):
    """Parser for show cloud performance dinet"""

    cli_command = 'show snmp notifies'

    """
    SNMP Notification Statistics:
      Total number of notifications   : 4030051
      Last notification sent          : Thursday April 04 14:41:03 ART 2024
      Notification sending is         : enabled
      Notifications last disabled     : Wednesday January 03 14:46:04 ART 2024
      Notifications have never been cleared
      Notifications in current period : 0
      Notifications in previous period: 0
      Notification monitor period     : 300 seconds

    Trap Name                            #Gen #Disc  Disable Last Generated      
    ----------------------------------- ----- -----  ------- --------------------
    CardRebootRequest                       8     0       0  2024:03:20:00:48:43 
    CardUp                                 55     0       0  2024:03:20:01:08:18 
    CardRemoved                             8     0       0  2024:03:06:00:17:41 
    CardInserted                           23     0       0  2024:03:06:00:38:46 
    CardBootFailed                          1     0       0  2022:10:25:21:14:21 
    PortLinkDown                          954     0       0  2024:03:20:01:08:10 
    PortLinkUp                           1234     0       0  2024:03:20:01:08:19 
    CLISessionStart                     788368 62669    6564  2024:04:04:14:48:10 
    CLISessionEnd                       788523 62675    6506  2024:04:04:14:46:35 
    CardActive                             74     0       0  2024:03:20:01:08:10 
    CardDown                               32     0       0  2024:03:20:01:08:10 
    GGSNServiceStart                        1     0       0  2022:10:25:21:17:45 
    LongDurTimerExpiry                  19486297 19486297       0  2024:04:04:14:48:07 
    ManagerFailure                        234     0       0  2024:03:06:00:12:39 
    NTPPeerUnreachable                      2     0       0  2022:11:17:23:38:15 
    NTPSyncLost                             6     0       0  2023:08:18:01:47:45 
    CardStandby                            54     0       0  2024:03:20:01:08:18 
    NTPPeerReachable                       20     0       0  2024:02:01:12:44:48 
    NTPSyncEstablished                      9     0       0  2024:02:01:12:44:52 
    BGPPeerSessionUp                      166     0       0  2024:01:03:03:53:15 
    BGPPeerSessionDown                     82     0       9  2024:01:03:03:27:31 
    CardSPOFAlarm                         323    54       0  2024:03:20:00:54:47 
    CardSPOFClear                         323     0       0  2024:03:20:01:08:22 
    LoginFailure                         1304   228      10  2024:04:04:06:03:05 
    TaskFailed                            222     0       0  2024:02:01:12:44:42 
    TaskRestart                           216     0       0  2024:02:01:12:44:42 
    Heartbeat                            5795     0       0  2024:04:04:14:40:57 
    SessMgrRecoveryComplete               247     0       0  2024:02:08:19:37:24 
    DiameterPeerDown                     6568     0     106  2024:04:03:22:39:54 
    DiameterPeerUp                       6459     0     160  2024:04:03:22:39:55 
    ThreshStorageUtilization                9     0       0  2024:03:21:00:58:00 
    ThreshClearStorageUtilization           9     0       0  2024:03:21:09:09:00 
    PortDown                              113     0       0  2024:03:20:01:08:10 
    PortUp                                145     0       0  2024:03:20:01:08:19 
    SystemStartup                           1     0       0  2022:10:25:21:17:44 
    DiameterCapabilitiesExchangeSuccess  6459     0     160  2024:04:03:22:39:55 
    CertValid                               1     0       0  2022:10:25:21:16:28 
    FTPFailure                          1441627     0 1032998  2024:04:04:14:41:03 
    StorageFailed                           1     0       0  2023:09:27:08:27:51 
    RaidStarted                             4     0       0  2023:09:27:08:36:27 
    RaidDegraded                            6     0       0  2023:12:13:00:12:50 
    RaidRecovered                           4     0       0  2023:12:13:08:58:08 
    PGWServiceStart                         1     0       0  2022:10:25:21:17:45 
    SGWServiceStart                         1     0       0  2022:10:25:21:17:45 
    EGTPServiceStart                        3     0       0  2022:10:25:21:17:46 
    ManagerRestart                        315     0       0  2024:02:08:19:37:35 
    EGTPCPathFail                       155306 24108    4643  2024:04:04:14:48:07 
    EGTPCPathFailClear                  283126 31050   11185  2024:04:04:14:45:35 
    EGTPUPathFail                       1564181 207498   23408  2024:04:04:14:45:58 
    EGTPUPathFailClear                  469457 17507    4345  2024:04:04:14:40:06 
    LocalUserAdded                          4     0       0  2022:10:25:21:17:17 
    TestModeEntered                        10     0       0  2023:10:10:03:53:04 
    CPUWarn                                97     0       1  2024:03:22:00:11:42 
    CPUWarnClear                           97     0       1  2024:03:22:00:12:02 
    CPUOver                                 3     0       0  2024:01:21:16:08:02 
    CPUOverClear                            3     0       0  2024:01:21:16:08:32 
    SwitchoverStart                         1     0       0  2023:09:27:08:34:02 
    SwitchoverComplete                      3     0       0  2023:09:27:08:34:04 
    MigrateStart                           17     0       0  2024:03:20:00:54:43 
    MigrateComplete                        17     0       0  2024:03:20:01:08:10 
    BFDSessionUp                         1266     0       0  2024:03:22:20:17:14 
    BFDSessionDown                       1040     0       0  2024:03:22:20:17:12 
    BGPPeerSessionIPv6Up                   22     0       0  2024:01:03:03:53:22 
    BGPPeerSessionIPv6Down                 10     0       1  2024:01:03:03:27:20 
    CapacityReached                         6     0       0  2022:12:07:06:14:03 
    DisabledEventIDs                        1     0       0  2023:08:17:17:27:27 
    NicBondChange                          61     0       0  2024:03:21:02:08:45 
    ServiceLossDetected                    25     0       0  2022:12:07:06:12:39 
    CiscoMwsServiceStart                    9     0       0  2022:10:25:21:17:46 
    EntStateOperEnabled                   200     0      14  2024:03:20:01:08:19 
    EntStateOperDisabled                   98     0       0  2024:03:20:01:08:10 
    CiscoFruInserted                       23     0      23  2024:03:06:00:38:46 
    CiscoFruRemoved                         8     0       8  2024:03:06:00:17:41 
    CiscoFlashCopyCompletionTrap            2     0       2  2023:12:06:09:56:59 
    CiscoFlashMiscOpCompletionTrap         44     0      44  2024:01:22:11:41:18 
    CseHaRestartNotify                      2     0       2  2024:02:01:12:44:42 
    CseFailSwCoreNotify                   254     0     254  2024:03:31:10:59:19 
    CseFailSwCoreNotifyExtended           254     0     254  2024:03:31:10:59:19 

    Total number of notifications Disabled  : 1090698
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial return dictionary
        notifications_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        pattern1 = re.compile(r'^\s+Total number of notifications\s+:\s+(?P<Total>\d+)' , re.MULTILINE)
        pattern2 = re.compile(r'^\s+Last notification sent\s+:\s+(?P<Last_sent>\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\d+)' , re.MULTILINE)
        pattern3 = re.compile(r'^\s+Notification sending is\s+:\s+(?P<Sending>\w+)' , re.MULTILINE)
        pattern4 = re.compile(r'^\s+Notifications last disabled\s+:\s+(?P<Last_disable>\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\w+\s+\d+)' , re.MULTILINE)
        pattern5 = re.compile(r'^\s+Notifications in current period\s+:\s+(?P<Current_period>\d+)' , re.MULTILINE)
        pattern6 = re.compile(r'^\s+Notifications in previous period:\s+(?P<Previous_period>\d+)' , re.MULTILINE)
        pattern7 = re.compile(r'^\s+Notification monitor period\s+:\s+(?P<Monitor_period>\d+\s+\w+)' , re.MULTILINE)
        pattern8 = re.compile(r'^Total number of notifications Disabled\s+:\s+(?P<Notif_disabled>\d+)' , re.MULTILINE)
        pattern9= re.compile(r'^\s*(?P<Trap>\w[\w\s]*\w|\w)\s+(?P<Gen>\d+)\s+(?P<Disc>\d+)\s+(?P<Disable>\d+)\s+(?P<Last_Generated>\d{4}:\d{2}:\d{2}:\d{2}:\d{2}:\d{2})\s*$' , re.MULTILINE)

        #For Loop to get all the values from output
        for match in out.splitlines(): #Split a string into a list where each line is a list item
            m= pattern1.match(match) #Matching values in pattern1
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                total_notifications = m.groupdict()['Total'].strip()

                result_dict['Total number of notifications']= total_notifications
                continue
            m= pattern2.match(match) #Matching values in pattern2
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                last_not_sent = m.groupdict()['Last_sent'].strip()

                result_dict['Last notification sent']= last_not_sent
                continue

            m= pattern3.match(match) #Matching values in pattern3
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                notif_sending = m.groupdict()['Sending'].strip()

                result_dict['Notification sending is']= notif_sending
                continue

            m= pattern4.match(match) #Matching values in pattern4
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                notif_last_dis = m.groupdict()['Last_disable'].strip()

                result_dict['Notifications last disabled']= notif_last_dis
                continue
            
            m= pattern5.match(match) #Matching values in pattern5
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                notif_curr_period = m.groupdict()['Current_period'].strip()

                result_dict['Notifications in current period']= notif_curr_period
                continue
            
            m= pattern6.match(match) #Matching values in pattern6
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                notif_pre_period = m.groupdict()['Previous_period'].strip()

                result_dict['Notifications in previous period']= notif_pre_period
                continue
            
            m= pattern7.match(match) #Matching values in pattern7
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                notif_mon_period = m.groupdict()['Monitor_period'].strip()

                result_dict['Notification monitor period']= notif_mon_period
                continue
            
            m= pattern8.match(match) #Matching values in pattern8
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'summary' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('summary',{})
                
                #Defining variables that get values matched for every regex
                total_not_disabled = m.groupdict()['Notif_disabled'].strip()

                notifications_dict['statistics']['summary']['Total number of notifications Disabled'] = total_not_disabled
                continue
            
            m= pattern9.match(match) #Matching values in pattern8
            if m:
                if 'statistics' not in notifications_dict:
                    result_dict = notifications_dict.setdefault('statistics',{})
                if 'traps' not in notifications_dict['statistics']:
                    result_dict = notifications_dict['statistics'].setdefault('traps',{})
                
                #Defining variables that get values matched for every regex
                trap = m.groupdict()['Trap'].strip()
                generated = m.groupdict()['Gen'].strip()
                disc = m.groupdict()['Disc'].strip()
                disable = m.groupdict()['Disable'].strip()
                last_generated = m.groupdict()['Last_Generated'].strip()

                result_dict[trap] = {#Last entry for the dictionary
                    'Gen' : generated,
                    'Disc' : disc,
                    'Disable' : disable,
                    'Last Generated': last_generated
                }
        return notifications_dict
