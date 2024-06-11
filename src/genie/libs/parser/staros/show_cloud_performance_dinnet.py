"""starOS implementation of show_card_table.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
#from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCloudDinetSchema(MetaParser):
    """Schema for show cloud performance dinet"""
    schema = {
        'cloud_per_dinet': {
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
                }
            }

class ShowCloud(ShowCloudDinetSchema):
#class ShowCloud():
    """Parser for show cloud performance dinet"""

    cli_command = 'show cloud performance dinet'

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
    """

    def cli(self, output=None):
        if output is None:
            salida = self.device.execute(self.cli_command)
        else:
            salida = output
        
        # initial return dictionary
        dinet_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        pattern = re.compile(r'^(?P<Card>\s+\d+)\s+(?P<Current_Rx>\d+.\d+)\s+(?P<Current_Tx>\d+.\d+)\s+(?P<Fivemin_Rx>\d+.\d+)\s+(?P<Fivemin_Tx>\d+.\d+)\s+(?P<Fifteenmin_Rx>\d+.\d+)\s+(?P<Fifteenmin_Tx>\d+.\d+)', re.MULTILINE)

        for match in salida.splitlines():
            m = pattern.match(match)
            if m:
                if 'cloud_per_dinet' not in dinet_dict:
                    result_dict = dinet_dict.setdefault('cloud_per_dinet',{})
                if 'Dinet' not in dinet_dict['cloud_per_dinet']:
                    result_dict = dinet_dict['cloud_per_dinet'].setdefault('Dinet',{})#Setdefault lo utilizo cuando tengo las llaves definidas.
                
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
        return dinet_dict
