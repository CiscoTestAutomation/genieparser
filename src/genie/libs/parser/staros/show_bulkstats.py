"""starOS implementation of show bulkstats.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, Or, ListOf

class ShowbulkstatsSchema(MetaParser):
    """Schema for show bulkstats"""

    schema = {
        'bulkstats_info': {
            Any(): {
                'Records Collected': str,
                'Records Transmitted': str,
                'Last Succesful transfer':{
                    Optional('Year'):str,
                    Optional('Month'):str,
                    Optional('Day'): str,
                    Optional('Time'):str,
                },
                'Last Attemped transfer':{
                    Optional('Year'):str,
                    Optional('Month'):str,
                    Optional('Day'): str,
                    Optional('Time'):str,
                },
            }
        } 
    }


class Showbulkstats(ShowbulkstatsSchema):
    """Parser for show bulkstats"""

    cli_command = 'show bulkstats'

    """
  File 2
    Remote File Format:            /opt/csvdrop_matrix/%host%_bulkstats_Matrix_%localdate%_%localtime%_%localtz%_15_15.csv
    File Header:                   Version-21.25,%ipaddr%,%date%-%time%,%localdate%-%localtime%,%localtz%,%localtzoffset%,%localdate3%-%localtime3%,%swbuild%,EPC
    File Footer:                   EndOfFile
    Bulkstats Receivers:
        Primary: 10.32.250.81 using SFTP with username csvuser
    File Statistics:
      Records awaiting transmission: 0
      Bytes awaiting transmission:   0
      Total records collected:       40507697
      Total bytes collected:         5360711792
      Total records transmitted:     40507697
      Total bytes transmitted:       5361426812
      Total records discarded:       0
      Total bytes discarded:         0
      Last transfer time required:   0 second(s)
      Last successful transfer:      Monday July 25 16:00:31 CDT 2022
      Last successful tx recs:       5991
      Last successful tx bytes:      794656
      Last attempted transfer:       Monday July 25 16:00:31 CDT 2022

  File 3
    Remote File Format:            /opt/csvdrop/%host%_bulkstats_%localdate%_%localtime%_%localtz%_15_15.csv
    File Header:                   Version-21.25,%ipaddr%,%date%-%time%,%localdate%-%localtime%,%localtz%,%localtzoffset%,%localdate3%-%localtime3%,%swbuild%,EPC
    File Footer:                   EndOfFile
    Bulkstats Receivers:
        Primary: 10.32.250.81 using SFTP with username csvuser
    File Statistics:
      Records awaiting transmission: 0
      Bytes awaiting transmission:   0
      Total records collected:       41249503
      Total bytes collected:         5458617091
      Total records transmitted:     41249503
      Total bytes transmitted:       5459331709
      Total records discarded:       0
      Total bytes discarded:         0
      Last transfer time required:   1 second(s)
      Last successful transfer:      Monday July 25 16:00:31 CDT 2022
      Last successful tx recs:       5991
      Last successful tx bytes:      794656
      Last attempted transfer:       Monday July 25 16:00:31 CDT 2022

    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        bulk_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'\s{2}File\s(?P<file>\d+)')
        p1 = re.compile(r'\s{6}Total\srecords\scollected:\s+(?P<collect>\d+)')
        p2 = re.compile(r'\s{6}Total\srecords\stransmitted:\s+(?P<transmitted>\d+)')
        p3 = re.compile(r'\s{6}Last\ssuccessful\stransfer:\s+\w+\s(?P<s_month>\w+)\s(?P<s_day>\d+)\s(?P<s_time>\d+:\d+:\d+)\s\w+\s(?P<s_year>\d+)|\s{6}(?P<no>No)\ssuccessful\sdata\stransfers')
        p4 = re.compile(r'\s{6}Last\sattempted\stransfer:\s+\w+\s(?P<a_month>\w+)\s(?P<a_day>\d+)\s(?P<a_time>\d+:\d+:\d+)\s\w+\s(?P<a_year>\d+)|\s{6}(?P<no>No)\sattempted\sdata\stransfers')

        for line in out.splitlines():
            m = p0.match(line)
            if m:
                if 'bulkstats_info' not in bulk_dict:
                    result_dict = bulk_dict.setdefault('bulkstats_info',{})
                file = m.groupdict()['file']
                result_dict[file] = {}

            m = p1.match(line)
            if m:
                if 'bulkstats_info' not in bulk_dict:
                    result_dict = bulk_dict.setdefault('bulkstats_info',{})
                collect = m.groupdict()['collect']
                result_dict[file]['Records Collected'] = collect
            m = p2.match(line)
            if m:
                if 'bulkstats_info' not in bulk_dict:
                    result_dict = bulk_dict.setdefault('bulkstats_info',{})
                transmitted = m.groupdict()['transmitted']
                result_dict[file]['Records Transmitted'] = transmitted
            m = p3.match(line)
            if m:
                if 'bulkstats_info' not in bulk_dict:
                    result_dict = bulk_dict.setdefault('bulkstats_info',{})
                if 'Last Succesful transfer' not in bulk_dict['bulkstats_info'][file]:
                    result_dict[file].setdefault('Last Succesful transfer',{})
                s_month = m.groupdict()['s_month']
                s_day = m.groupdict()['s_day']
                s_year = m.groupdict()['s_year']
                s_time = m.groupdict()['s_time']
                no = m.groupdict()['no']
                if no:
                    continue
                result_dict[file]['Last Succesful transfer']['Year'] = s_year
                result_dict[file]['Last Succesful transfer']['Month'] = s_month
                result_dict[file]['Last Succesful transfer']['Day'] = s_day
                result_dict[file]['Last Succesful transfer']['Time'] = s_time
                    
            m = p4.match(line)
            if m:
                if 'bulkstats_info' not in bulk_dict:
                    result_dict = bulk_dict.setdefault('bulkstats_info',{})
                if 'Last Attemped transfer' not in bulk_dict['bulkstats_info'][file]:
                    result_dict[file].setdefault('Last Attemped transfer',{})
                a_month = m.groupdict()['a_month']
                a_day = m.groupdict()['a_day']
                a_year = m.groupdict()['a_year']
                a_time = m.groupdict()['a_time']
                no= m.groupdict()['no']
                if no:
                    continue
                result_dict[file]['Last Attemped transfer']['Year'] = a_year
                result_dict[file]['Last Attemped transfer']['Month'] = a_month
                result_dict[file]['Last Attemped transfer']['Day'] = a_day
                result_dict[file]['Last Attemped transfer']['Time'] = a_time

        return bulk_dict