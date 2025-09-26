"""starOS implementation of show_card_table.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCloudSchema(MetaParser):
    """Schema for show cloud performance summary"""

    schema = {
        'cloud_performance': {
            'Dinet': {
                Any(): {
                    'Current': {
                        'Rx': str,
                        'Tx':str,
                            },
                    '5min': {
                        'Rx': str,
                        'Tx':str,
                            },
                    '15min':{
                        'Rx': str,
                        'Tx':str,
                            },    
                        },
                    },
            'Port': {
                Any(): {
                    'Current': {
                        'Rx': str,
                        'Tx':str,
                            },
                    '5min': {
                        'Rx': str,
                        'Tx':str,
                            },
                    '15min': {
                        'Rx': str,
                        'Tx':str,
                            },    
                        },
                    },
                }
            } 


class ShowCloud(ShowCloudSchema):
    """Parser for show cloud performance summary"""

    cli_command = 'show cloud performance summary'

    """
    ----- Average DINet Performance (in Mbps) -----
    Card       Current           5min             15min
            Rx       Tx      Rx       Tx       Rx     Tx
    -----  ------- -------  ------- -------  ------- -------
    1     58.433  2.149    57.447  2.285    57.518  2.214   
    2     171.808 64.844   104.556 93.002   108.333 89.524  
    3     2770    2835     2728    2968     2793    2957    
    4     2807    3036     2788    2985     2747    3022    
    5     0.000   0.000    0.000   0.000    0.000   0.000   
    6     2848    2865     2712    2927     2743    2940    
    7     207.381 2856     243.307 2888     239.416 2923    
    8     2863    2861     2818    2922     2835    2938    
    9     74.205  2886     74.026  2871     73.945  2870    
    10     2809    3124     2773    3044     2762    2945    
    11     2629    2979     2713    2962     2764    2991    
    12     2545    3630     2647    3576     2628    3648    
    13     2757    1183     2900    1201     2902    1238    
    14     2790    1202     2804    1223     2841    1247    
    15     2853    1462     2965    1416     2931    1390    
    16     2885    1170     2950    1222     2948    1207    
    17     2763    1324     2807    1328     2834    1331    

    --- Average Aggregated Port Performance (in Mbps) ---
    Card       Current           5min             15min
            Rx       Tx      Rx       Tx       Rx     Tx
    -----  ------- -------  ------- -------  ------- -------
    1     0.000   0.000    0.000   0.000    0.000   0.000   
    2     0.008   0.035    0.251   21.400   0.248   21.513  
    3     2674    2583     2757    2510     2739    2553    
    4     2800    2564     2762    2554     2830    2541    
    5     2604    2440     2750    2440     2772    2474    
    6     2654    2607     2721    2482     2736    2515    
    7     2646    0.133    2672    28.039   2712    29.608  
    8     2649    2623     2715    2597     2731    2605    
    9     2736    0.040    2708    0.040    2705    0.040   
    10     2907    2564     2848    2544     2752    2545    
    11     2722    2367     2700    2435     2739    2491    
    12     3281    2377     3249    2491     3337    2486    
    13     863.871 2358     913.634 2534     942.468 2512    
    14     901.845 2418     919.626 2417     951.579 2460    
    15     1173    2476     1142    2590     1119    2563    
    16     871.308 2498     920.274 2543     913.015 2552    
    17     1039    2387     1040    2437     1045    2455 
    """
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        cloud_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the header of the second table
        second_table_header_pattern = re.compile(r'--- Average Aggregated Port Performance \(in Mbps\) ---')

        # Find the position where the second table starts
        second_table_start = second_table_header_pattern.search(out).start()

        # Separate the data into two parts for each table
        first_table_data = out[:second_table_start]  # Data before the header of the second table
        second_table_data = out[second_table_start:]  # Data from the header of the second table and after  

        # Define the regex pattern for matching the rows with values
        pattern = re.compile(r'^(?P<Card>\s+\d+)\s+(?P<Current_Rx>\d+.\d+)\s+(?P<Current_Tx>\d+.\d+)\s+(?P<Fivemin_Rx>\d+.\d+)\s+(?P<Fivemin_Tx>\d+.\d+)\s+(?P<Fifteenmin_Rx>\d+.\d+)\s+(?P<Fifteenmin_Tx>\d+.\d+)', re.MULTILINE)

        for match in first_table_data.splitlines():
            m = pattern.match(match)
            if m:
                if 'cloud_performance' not in cloud_dict:
                    result_dict = cloud_dict.setdefault('cloud_performance',{})
                if 'Dinet' not in cloud_dict['cloud_performance']:
                    result_dict = cloud_dict['cloud_performance'].setdefault('Dinet',{})#Setdefault lo utilizo cuando tengo las llaves definidas.
  
                card = m.groupdict()['Card'].strip()
                current_rx = m.groupdict()['Current_Rx'].strip()
                current_tx = m.groupdict()['Current_Tx'].strip()
                fivemin_rx = m.groupdict()['Fivemin_Rx'].strip()
                fivemin_tx = m.groupdict()['Fivemin_Tx'].strip()
                fifteen_rx = m.groupdict()['Fifteenmin_Rx'].strip()
                fifteen_tx = m.groupdict()['Fifteenmin_Tx'].strip()

                result_dict[card] = {}#Se utiliza cuando tengo el Any()

                if 'Current' not in result_dict[card]:
                    result_dict[card]['Current'] = {
                        'Rx': current_rx,
                        'Tx': current_tx
                    }
                if '5min' not in result_dict[card]:
                    result_dict[card]['5min'] = {
                        'Rx': fivemin_rx,
                        'Tx': fivemin_tx
                    }
                if '15min' not in result_dict[card]:
                    result_dict[card]['15min'] = {
                        'Rx': fifteen_rx,
                        'Tx': fifteen_tx
                    }
        
        for match in second_table_data.splitlines():
            m = pattern.match(match)
            if m:
                if 'cloud_performance' not in cloud_dict:
                    result_dict = cloud_dict.setdefault('cloud_performance',{})
                if 'Port' not in cloud_dict['cloud_performance']:
                    result_dict = cloud_dict['cloud_performance'].setdefault('Port',{})#Setdefault lo utilizo cuando tengo las llaves definidas.
      
                card = m.groupdict()['Card'].strip()
                current_rx = m.groupdict()['Current_Rx'].strip()
                current_tx = m.groupdict()['Current_Tx'].strip()
                fivemin_rx = m.groupdict()['Fivemin_Rx'].strip()
                fivemin_tx = m.groupdict()['Fivemin_Tx'].strip()
                fifteen_rx = m.groupdict()['Fifteenmin_Rx'].strip()
                fifteen_tx = m.groupdict()['Fifteenmin_Tx'].strip()

                result_dict[card] = {}#Se utiliza cuando tengo el Any()
                if 'Current' not in result_dict[card]:
                    result_dict[card]['Current'] = {
                        'Rx': current_rx,
                        'Tx': current_tx
                    }
                if '5min' not in result_dict[card]:
                    result_dict[card]['5min'] = {
                        'Rx': fivemin_rx,
                        'Tx': fivemin_tx
                    }
                if '15min' not in result_dict[card]:
                    result_dict[card]['15min'] = {
                        'Rx': fifteen_rx,
                        'Tx': fifteen_tx
                    }
  
        return cloud_dict

