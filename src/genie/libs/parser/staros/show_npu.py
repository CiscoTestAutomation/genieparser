"""starOS implementation of show_npu_utilization_table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowNpuSchema(MetaParser):
    """Schema for show npu utilization table"""

    schema = {
        'npu_utilization_table': {
            Any(): {
                'NPU NOW': str,
                'NPU MIN5': str,
                'NPU MIN15': str
            },
        }    
    }


class ShowNpu(ShowNpuSchema):
    """Parser for show npu utilization table"""

    cli_command = 'show npu utilization table'

    """
 ---------npu--------
     npu     now   5min  15min
--------  ------ ------ ------
 05/0/01      0%     0%     0%
 05/0/02      0%     0%     0%
 05/0/03      0%     0%     0%
 05/0/04      0%     0%     0%
 06/0/01      0%     0%     0%
 06/0/02      0%     0%     0%
 06/0/03      0%     0%     0%
 06/0/04      0%     0%     0%

       ---------npu--------
card     now   5min  15min
----  ------ ------ ------
   1      0%     0%     0%
   2     57%    59%    59%
   3     56%    57%    57%
   4     60%    58%    58%
   5     58%    58%    58%
   6     57%    58%    58%
   7     58%    57%    57%
  10     49%    48%    49%
  11     48%    47%    47%
  12     47%    47%    47%
  13     49%    48%    48%
  14     47%    46%    46%
  15     45%    47%    46%
  16      0%     0%     0%             
    
    """
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command).strip()
        else:
            out = output
        
        # initial return dictionary
        npu_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        pattern = re.compile(r'^(?P<npu>\s+\d+.\d+.\d+.)\s+(?P<npu_now>\d+.)\s+(?P<npu_min5>\d+.)\s+(?P<npu_min15>\d+.)', re.MULTILINE)
        pattern2 =  re.compile(r'^(?P<npu>\s+\d+)\s+(?P<npu_now>\d+.)\s+(?P<npu_min5>\d+.)\s+(?P<npu_min15>\d+.)', re.MULTILINE)

        for line in out.splitlines(): #Split a string into a list where each line is a list item
            m = pattern.match(line)
            if m:
                if 'npu_utilization_table' not in npu_dict:
                    result_dict = npu_dict.setdefault('npu_utilization_table',{})
                 #Assigning values based on regex groups    
                npu = m.groupdict()['npu']
                npu_now = m.groupdict()['npu_now']
                npu_min5 = m.groupdict()['npu_min5']
                npu_min15 = m.groupdict()['npu_min15']

                #Writing in dictionary
                result_dict[npu] = {}
                result_dict[npu]['NPU NOW'] = npu_now
                result_dict[npu]['NPU MIN5'] = npu_min5
                result_dict[npu]['NPU MIN15'] = npu_min15
                
            m1= pattern2.match(line)
            if m1:
                if 'npu_utilization_table' not in npu_dict:
                    result_dict = npu_dict.setdefault('npu_utilization_table',{})
                #Assigning values based on regex groups    
                npu = m1.groupdict()['npu']
                npu_now = m1.groupdict()['npu_now']
                npu_min5 = m1.groupdict()['npu_min5']
                npu_min15 = m1.groupdict()['npu_min15']

                #Writing in dictionary
                result_dict[npu] = {}
                result_dict[npu]['NPU NOW'] = npu_now
                result_dict[npu]['NPU MIN5'] = npu_min5
                result_dict[npu]['NPU MIN15'] = npu_min15
        return npu_dict
