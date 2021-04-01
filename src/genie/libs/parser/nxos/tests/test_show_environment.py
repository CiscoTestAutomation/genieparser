#Python
import unittest
from unittest.mock import Mock

#ATS
from pyats.topology import Device
from pyats.topology import loader

#Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# nxos show_environment
from genie.libs.parser.nxos.show_environment import ShowEnvironment, ShowEnvironmentFan, ShowEnvironmentFanDetail, ShowEnvironmentPower, ShowEnvironmentPowerDetail, ShowEnvironmentTemperature


# ===========================================
# Unit test for 'show environment'
# ===========================================
class TestShowEnvironment(unittest.TestCase):
	'''unit test for "show environment"'''
	device = Device(name='aDevice')

	golden_output={'execute.return_value': '''
			Fan:
			---------------------------------------------------------------------------
			Fan             Model                Hw     Direction       Status
			---------------------------------------------------------------------------
			Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
			Fan2(sys_fan2)  N9K-C9508-FAN        0.6020 front-to-back   Ok
			Fan3(sys_fan3)  N9K-C9508-FAN        0.6020 front-to-back   Ok
			Fan_in_PS1                           --     front-to-back   Ok
			Fan_in_PS2                           --     front-to-back   Ok
			Fan_in_PS3                           --     front-to-back   Ok
			Fan_in_PS4                           --     front-to-back   Ok
			Fan_in_PS5                           --     front-to-back   Shutdown
			Fan_in_PS6                           --     front-to-back   Shutdown
			Fan_in_PS7                           --     front-to-back   Ok
			Fan_in_PS8                           --     front-to-back   Ok
			Fan Zone Speed: Zone 1: 0x41
			Fan Air Filter : NotSupported


			Power Supply:
			Voltage: 12 Volts
			Power                      Actual             Actual        Total
			Supply    Model            Output             Input        Capacity     Status
			                           (Watts )           (Watts )     (Watts )
			-------  ----------  ---------------  ------  ----------  --------------------
			1        N9K-PAC-3000W-B      1083 W             1147 W      3000 W      Ok
			2        N9K-PAC-3000W-B      1090 W             1157 W      3000 W      Ok
			3        N9K-PAC-3000W-B      1101 W             1164 W      3000 W      Ok
			4        N9K-PAC-3000W-B      1143 W             1214 W      3000 W      Ok
			5        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
			6        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
			7        N9K-PAC-3000W        1087 W             1143 W      3000 W      Ok
			8        N9K-PAC-3000W-B       130 W              175 W      3000 W      Ok


			                                  Actual        Power
			Module    Model                     Draw    Allocated    Status
			                                 (Watts )     (Watts )
			-------  -------------------  -----------  -----------  --------------
			1        N9K-X9736Q-FX           398.00 W     936.00 W    Powered-Up
			2        N9K-X9736C-FX           378.00 W     756.00 W    Powered-Up
			3        N9K-X9732C-EXM          566.00 W     816.00 W    Powered-Up
			4        N9K-X9732C-EXM          566.00 W     816.00 W    Powered-Up
			5        N9K-X9732C-EXM          567.00 W     816.00 W    Powered-Up
			6        N9K-X9732C-EXM          617.00 W     816.00 W    Powered-Up
			7        N9K-X9732C-EXM          615.00 W     816.00 W    Powered-Up
			8        N9K-X9736C-FX           375.00 W     756.00 W    Powered-Up
			Xb21     xbar                      N/A          0.00 W    Absent
			Xb22     N9K-C9508-FM-E          176.00 W     564.00 W    Powered-Up
			Xb23     N9K-C9508-FM-E          180.00 W     564.00 W    Powered-Up
			Xb24     N9K-C9508-FM-E          205.00 W     564.00 W    Powered-Up
			Xb25     N9K-C9508-FM-E            N/A        564.00 W    Powered-Dn
			Xb26     N9K-C9508-FM-E          201.00 W     564.00 W    Powered-Up
			27       N9K-SUP-A                65.00 W      90.00 W    Powered-Up
			28       N9K-SUP-A                57.00 W      90.00 W    Powered-Up
			29       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
			30       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
			fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
			fan2     N9K-C9508-FAN            83.00 W     249.00 W    Powered-Up
			fan3     N9K-C9508-FAN           109.00 W     249.00 W    Powered-Up

			N/A - Per module power not available


			Power Usage Summary:
			--------------------
			Power Supply redundancy mode (configured)                Non-Redundant(combined)
			Power Supply redundancy mode (operational)               Non-Redundant(combined)

			Total Power Capacity (based on configured mode)            18000.00 W
			Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
			Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
			Total Power of all Inputs (cumulative)                     18000.00 W
			Total Power Output (actual draw)                           5637.00 W
			Total Power Input (actual draw)                            6003.00 W
			Total Power Allocated (budget)                             10327.00 W
			Total Power Available for additional modules               7673.00 W



			Temperature:
			--------------------------------------------------------------------
			Module   Sensor        MajorThresh   MinorThres   CurTemp     Status
			                       (Celsius)     (Celsius)    (Celsius)
			--------------------------------------------------------------------
			1        CPU             85              75          52         Ok
			1        HOM0            105             95          73         Ok
			1        HOM1            105             95          81         Ok
			1        HOM2            105             95          81         Ok
			1        HOM3            105             95          81         Ok
			1        VRM1            110             100         62         Ok
			1        VRM2            110             100         63         Ok
			1        VRM3            110             100         54         Ok
			1        VRM4            110             100         54         Ok
			2        CPU             85              75          48         Ok
			2        HOM0            105             95          69         Ok
			2        HOM1            105             95          77         Ok
			2        HOM2            105             95          77         Ok
			2        HOM3            105             95          77         Ok
			2        VRM1            110             100         57         Ok
			2        VRM2            110             100         60         Ok
			2        VRM3            110             100         46         Ok
			2        VRM4            110             100         48         Ok
			3        CPU             85              75          41         Ok
			3        SUG0            105             95          60         Ok
			3        SUG1            105             95          70         Ok
			3        SUG2            105             95          55         Ok
			3        SUG3            105             95          64         Ok
			3        VRM1            110             100         54         Ok
			3        VRM2            110             100         57         Ok
			3        VRM3            110             100         50         Ok
			3        VRM4            110             100         50         Ok
			4        CPU             85              75          36         Ok
			4        SUG0            105             95          57         Ok
			4        SUG1            105             95          68         Ok
			4        SUG2            105             95          54         Ok
			4        SUG3            105             95          64         Ok
			4        VRM1            110             100         53         Ok
			4        VRM2            110             100         52         Ok
			4        VRM3            110             100         49         Ok
			4        VRM4            110             100         50         Ok
			5        CPU             85              75          38         Ok
			5        SUG0            105             95          55         Ok
			5        SUG1            105             95          64         Ok
			5        SUG2            105             95          52         Ok
			5        SUG3            105             95          61         Ok
			5        VRM1            110             100         50         Ok
			5        VRM2            110             100         50         Ok
			5        VRM3            110             100         51         Ok
			5        VRM4            110             100         47         Ok
			6        CPU             85              75          43         Ok
			6        SUG0            105             95          58         Ok
			6        SUG1            105             95          67         Ok
			6        SUG2            105             95          51         Ok
			6        SUG3            105             95          72         Ok
			6        VRM1            110             100         56         Ok
			6        VRM2            110             100         55         Ok
			6        VRM3            110             100         52         Ok
			6        VRM4            110             100         53         Ok
			7        CPU             85              75          38         Ok
			7        SUG0            105             95          62         Ok
			7        SUG1            105             95          87         Ok
			7        SUG2            105             95          54         Ok
			7        SUG3            105             95          68         Ok
			7        VRM1            110             100         54         Ok
			7        VRM2            110             100         55         Ok
			7        VRM3            110             100         53         Ok
			7        VRM4            110             100         51         Ok
			8        CPU             85              75          41         Ok
			8        HOM0            105             95          52         Ok
			8        HOM1            105             95          59         Ok
			8        HOM2            105             95          59         Ok
			8        HOM3            105             95          59         Ok
			8        VRM1            110             100         48         Ok
			8        VRM2            110             100         48         Ok
			8        VRM3            110             100         40         Ok
			8        VRM4            110             100         40         Ok
			22       CPU             85              75          45         Ok
			22       LAC0            105             95          65         Ok
			22       LAC1            105             95          60         Ok
			22       VRM1            110             100         69         Ok
			22       VRM2            110             100         69         Ok
			23       CPU             85              75          46         Ok
			23       LAC0            105             95          67         Ok
			23       LAC1            105             95          62         Ok
			23       VRM1            110             100         69         Ok
			23       VRM2            110             100         69         Ok
			24       CPU             85              75          50         Ok
			24       LAC0            105             95          74         Ok
			24       LAC1            105             95          61         Ok
			24       VRM1            110             100         76         Ok
			24       VRM2            110             100         76         Ok
			26       CPU             85              75          39         Ok
			26       LAC0            105             95          59         Ok
			26       LAC1            105             95          55         Ok
			26       VRM1            110             100         58         Ok
			26       VRM2            110             100         58         Ok
			27       OUTLET          75              55          34         Ok
			27       INLET           60              42          22         Ok
			27       CPU             90              80          34         Ok
			28       OUTLET          75              55          33         Ok
			28       INLET           60              42          22         Ok
			28       CPU             90              80          30         Ok
			29       CPU             105             95          45         Ok
			30       CPU             105             95          48         Ok
		'''
    }

	golden_parsed_output= {
	    "fans": {
	        "Fan1(sys_fan1)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan2(sys_fan2)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan3(sys_fan3)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan_in_PS1": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS2": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS3": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS4": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS5": {"direction": "front-to-back", "hw": "--", "status": "Shutdown"},
	        "Fan_in_PS6": {"direction": "front-to-back", "hw": "--", "status": "Shutdown"},
	        "Fan_in_PS7": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS8": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "fan_air_filter": "NotSupported",
	        "fan_zone_speed": "Zone 1: 0x41",
	    },
	    "power": {
	        "modules": {
	            "1": {
	                "actual_drawn": "398.00",
	                "allocated_power": 936.0,
	                "model": "N9K-X9736Q-FX",
	                "status": "Powered-Up",
	            },
	            "2": {
	                "actual_drawn": "378.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "27": {
	                "actual_drawn": "65.00",
	                "allocated_power": 90.0,
	                "model": "N9K-SUP-A",
	                "status": "Powered-Up",
	            },
	            "28": {
	                "actual_drawn": "57.00",
	                "allocated_power": 90.0,
	                "model": "N9K-SUP-A",
	                "status": "Powered-Up",
	            },
	            "29": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "3": {
	                "actual_drawn": "566.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "30": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "4": {
	                "actual_drawn": "566.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "5": {
	                "actual_drawn": "567.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "6": {
	                "actual_drawn": "617.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "7": {
	                "actual_drawn": "615.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "8": {
	                "actual_drawn": "375.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "Xb22": {
	                "actual_drawn": "176.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb23": {
	                "actual_drawn": "180.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb24": {
	                "actual_drawn": "205.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb26": {
	                "actual_drawn": "201.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "fan1": {
	                "actual_drawn": "81.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan2": {
	                "actual_drawn": "83.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan3": {
	                "actual_drawn": "109.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	        },
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 1147,
	                "actual_output_watts": 1083,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "2": {
	                "actual_input_watts": 1157,
	                "actual_output_watts": 1090,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "3": {
	                "actual_input_watts": 1164,
	                "actual_output_watts": 1101,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "4": {
	                "actual_input_watts": 1214,
	                "actual_output_watts": 1143,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "5": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "6": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "7": {
	                "actual_input_watts": 1143,
	                "actual_output_watts": 1087,
	                "model": "N9K-PAC-3000W",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "8": {
	                "actual_input_watts": 175,
	                "actual_output_watts": 130,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 12000.0,
	            "total_grid_b_power_watts": 6000.0,
	            "total_power_allocated_watts": 10327.0,
	            "total_power_available_watts": 7673.0,
	            "total_power_capacity_watts": 18000.0,
	            "total_power_cumulative_watts": 18000.0,
	            "total_power_input_watts": 6003.0,
	            "total_power_output_watts": 5637.0,
	        },
	        "voltage": 12,
	    },
	    "temperature": {
	        "1": {
	            "CPU": {
	                "current_temp_celsius": 52,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "HOM0": {
	                "current_temp_celsius": 73,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM1": {
	                "current_temp_celsius": 81,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM2": {
	                "current_temp_celsius": 81,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM3": {
	                "current_temp_celsius": 81,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 62,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 63,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "2": {
	            "CPU": {
	                "current_temp_celsius": 48,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "HOM0": {
	                "current_temp_celsius": 69,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM1": {
	                "current_temp_celsius": 77,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM2": {
	                "current_temp_celsius": 77,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM3": {
	                "current_temp_celsius": 77,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 57,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 60,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 46,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 48,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "22": {
	            "CPU": {
	                "current_temp_celsius": 45,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "LAC0": {
	                "current_temp_celsius": 65,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "LAC1": {
	                "current_temp_celsius": 60,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 69,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 69,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "23": {
	            "CPU": {
	                "current_temp_celsius": 46,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "LAC0": {
	                "current_temp_celsius": 67,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "LAC1": {
	                "current_temp_celsius": 62,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 69,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 69,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "24": {
	            "CPU": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "LAC0": {
	                "current_temp_celsius": 74,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "LAC1": {
	                "current_temp_celsius": 61,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 76,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 76,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "26": {
	            "CPU": {
	                "current_temp_celsius": 39,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "LAC0": {
	                "current_temp_celsius": 59,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "LAC1": {
	                "current_temp_celsius": 55,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 58,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 58,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "27": {
	            "CPU": {
	                "current_temp_celsius": 34,
	                "major_threshold_celsius": 90,
	                "minor_threshold_celsius": 80,
	                "status": "Ok",
	            },
	            "INLET": {
	                "current_temp_celsius": 22,
	                "major_threshold_celsius": 60,
	                "minor_threshold_celsius": 42,
	                "status": "Ok",
	            },
	            "OUTLET": {
	                "current_temp_celsius": 34,
	                "major_threshold_celsius": 75,
	                "minor_threshold_celsius": 55,
	                "status": "Ok",
	            },
	        },
	        "28": {
	            "CPU": {
	                "current_temp_celsius": 30,
	                "major_threshold_celsius": 90,
	                "minor_threshold_celsius": 80,
	                "status": "Ok",
	            },
	            "INLET": {
	                "current_temp_celsius": 22,
	                "major_threshold_celsius": 60,
	                "minor_threshold_celsius": 42,
	                "status": "Ok",
	            },
	            "OUTLET": {
	                "current_temp_celsius": 33,
	                "major_threshold_celsius": 75,
	                "minor_threshold_celsius": 55,
	                "status": "Ok",
	            },
	        },
	        "29": {
	            "CPU": {
	                "current_temp_celsius": 45,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            }
	        },
	        "3": {
	            "CPU": {
	                "current_temp_celsius": 41,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "SUG0": {
	                "current_temp_celsius": 60,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG1": {
	                "current_temp_celsius": 70,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG2": {
	                "current_temp_celsius": 55,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG3": {
	                "current_temp_celsius": 64,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 57,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "30": {
	            "CPU": {
	                "current_temp_celsius": 48,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            }
	        },
	        "4": {
	            "CPU": {
	                "current_temp_celsius": 36,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "SUG0": {
	                "current_temp_celsius": 57,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG1": {
	                "current_temp_celsius": 68,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG2": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG3": {
	                "current_temp_celsius": 64,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 53,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 52,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 49,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "5": {
	            "CPU": {
	                "current_temp_celsius": 38,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "SUG0": {
	                "current_temp_celsius": 55,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG1": {
	                "current_temp_celsius": 64,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG2": {
	                "current_temp_celsius": 52,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG3": {
	                "current_temp_celsius": 61,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 50,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 51,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 47,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "6": {
	            "CPU": {
	                "current_temp_celsius": 43,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "SUG0": {
	                "current_temp_celsius": 58,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG1": {
	                "current_temp_celsius": 67,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG2": {
	                "current_temp_celsius": 51,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG3": {
	                "current_temp_celsius": 72,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 56,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 55,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 52,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 53,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "7": {
	            "CPU": {
	                "current_temp_celsius": 38,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "SUG0": {
	                "current_temp_celsius": 62,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG1": {
	                "current_temp_celsius": 87,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG2": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "SUG3": {
	                "current_temp_celsius": 68,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 55,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 53,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 51,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	        "8": {
	            "CPU": {
	                "current_temp_celsius": 41,
	                "major_threshold_celsius": 85,
	                "minor_threshold_celsius": 75,
	                "status": "Ok",
	            },
	            "HOM0": {
	                "current_temp_celsius": 52,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM1": {
	                "current_temp_celsius": 59,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM2": {
	                "current_temp_celsius": 59,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "HOM3": {
	                "current_temp_celsius": 59,
	                "major_threshold_celsius": 105,
	                "minor_threshold_celsius": 95,
	                "status": "Ok",
	            },
	            "VRM1": {
	                "current_temp_celsius": 48,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM2": {
	                "current_temp_celsius": 48,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM3": {
	                "current_temp_celsius": 40,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	            "VRM4": {
	                "current_temp_celsius": 40,
	                "major_threshold_celsius": 110,
	                "minor_threshold_celsius": 100,
	                "status": "Ok",
	            },
	        },
	    },
	}



	golden_output_1 = {'execute.return_value': '''
		Fan:
		---------------------------------------------------------------------------
		Fan             Model                Hw     Direction       Status
		---------------------------------------------------------------------------
		Fan1(sys_fan1)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan2(sys_fan2)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan3(sys_fan3)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan4(sys_fan4)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan_in_PS1                           --     none            None
		Fan_in_PS2      --                   --     front-to-back   Ok
		Fan Zone Speed: Zone 1: 0x80
		Fan Air Filter : NotSupported


		Power Supply:
		Voltage: 12 Volts
		Power                      Actual             Actual        Total
		Supply    Model            Output             Input        Capacity     Status
		                           (Watts )           (Watts )     (Watts )
		-------  ----------  ---------------  ------  ----------  --------------------
		1        ------------            0 W                0 W         0 W   Absent
		2        NXA-PAC-650W-PI       126 W              140 W       650 W      Ok


		Power Usage Summary:
		--------------------
		Power Supply redundancy mode (configured)                Non-Redundant(combined)
		Power Supply redundancy mode (operational)               Non-Redundant(combined)

		Total Power Capacity (based on configured mode)             650.00 W
		Total Grid-A (first half of PS slots) Power Capacity          0.00 W
		Total Grid-B (second half of PS slots) Power Capacity       650.00 W
		Total Power of all Inputs (cumulative)                      650.00 W
		Total Power Output (actual draw)                            126.00 W
		Total Power Input (actual draw)                             140.00 W
		Total Power Allocated (budget)                                N/A
		Total Power Available for additional modules                  N/A



		Temperature:
		--------------------------------------------------------------------
		Module   Sensor        MajorThresh   MinorThres   CurTemp     Status
		                       (Celsius)     (Celsius)    (Celsius)
		--------------------------------------------------------------------
		1        FRONT           70              42          24         Ok
		1        BACK            80              70          31         Ok
		1        CPU             90              80          43         Ok
		1        Sugarbowl       100             90          54         Ok

	'''
	}

	golden_parsed_output_1 = {
	    "fans": {
	        "Fan1(sys_fan1)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan2(sys_fan2)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan3(sys_fan3)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan4(sys_fan4)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan_in_PS1": {"direction": "none", "hw": "--", "status": "None"},
	        "Fan_in_PS2": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "fan_air_filter": "NotSupported",
	        "fan_zone_speed": "Zone 1: 0x80",
	    },
	    "power": {
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "------------",
	                "status": "Absent",
	                "total_capacity_watts": 0,
	            },
	            "2": {
	                "actual_input_watts": 140,
	                "actual_output_watts": 126,
	                "model": "NXA-PAC-650W-PI",
	                "status": "Ok",
	                "total_capacity_watts": 650,
	            },
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 0.0,
	            "total_grid_b_power_watts": 650.0,
	            "total_power_capacity_watts": 650.0,
	            "total_power_cumulative_watts": 650.0,
	            "total_power_input_watts": 140.0,
	            "total_power_output_watts": 126.0,
	        },
	        "voltage": 12,
	    },
	    "temperature": {
	        "1": {
	            "BACK": {
	                "current_temp_celsius": 31,
	                "major_threshold_celsius": 80,
	                "minor_threshold_celsius": 70,
	                "status": "Ok",
	            },
	            "CPU": {
	                "current_temp_celsius": 43,
	                "major_threshold_celsius": 90,
	                "minor_threshold_celsius": 80,
	                "status": "Ok",
	            },
	            "FRONT": {
	                "current_temp_celsius": 24,
	                "major_threshold_celsius": 70,
	                "minor_threshold_celsius": 42,
	                "status": "Ok",
	            },
	            "Sugarbowl": {
	                "current_temp_celsius": 54,
	                "major_threshold_celsius": 100,
	                "minor_threshold_celsius": 90,
	                "status": "Ok",
	            },
	        }
	    },
	}



	
	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironment(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironment(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output_1)


#=======================================
# unittest for show environment fan
#=======================================
class TestShowEnvironmentFan(unittest.TestCase):
	'''unit test for "show environment fan"'''
	device = Device(name='aDevice')


	golden_output={'execute.return_value': '''
		Fan:
		---------------------------------------------------------------------------
		Fan             Model                Hw     Direction       Status
		---------------------------------------------------------------------------
		Fan1(sys_fan1)  ----------           --     front-to-back   Absent
		Fan2(sys_fan2)  ----------           --     front-to-back   Absent
		Fan3(sys_fan3)  ----------           --     front-to-back   Absent
		Fan_in_PS1                           --     front-to-back   None
		Fan_in_PS2                           --     front-to-back   None
		Fan_in_PS3                           --     front-to-back   None
		Fan_in_PS4                           --     front-to-back   None
		Fan_in_PS5                           --     front-to-back   None
		Fan_in_PS6                           --     front-to-back   None
		Fan_in_PS7                           --     front-to-back   None
		Fan_in_PS8                           --     front-to-back   None
		Fan Zone Speed: Zone 1: 0xff
		Fan Air Filter : NotSupported

	'''
	}

	golden_parsed_output = {   
	        'fans': {   'Fan1(sys_fan1)': {   'direction': 'front-to-back',
                        'hw': '--',
                        'model': '----------',
                        'status': 'Absent'},
            'Fan2(sys_fan2)': {   'direction': 'front-to-back',
                        'hw': '--',
                        'model': '----------',
                        'status': 'Absent'},
            'Fan3(sys_fan3)': {   'direction': 'front-to-back',
                        'hw': '--',
                        'model': '----------',
                        'status': 'Absent'},
            'Fan_in_PS1': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS2': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS3': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS4': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS5': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS6': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS7': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'Fan_in_PS8': {   'direction': 'front-to-back',
                              'hw': '--',
                              'status': 'None'},
            'fan_air_filter': 'NotSupported',
            'fan_zone_speed': 'Zone 1: 0x'
           	}
    }

	golden_output_1= {'execute.return_value': '''
		Fan:
		---------------------------------------------------------------------------
		Fan             Model                Hw     Direction       Status
		---------------------------------------------------------------------------
		Fan1(sys_fan1)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan2(sys_fan2)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan3(sys_fan3)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan4(sys_fan4)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan_in_PS1                           --     none            None
		Fan_in_PS2      --                   --     front-to-back   Ok
		Fan Zone Speed: Zone 1: 0x80
		Fan Air Filter : NotSupported
	'''
	}

	golden_parsed_output_1 = {
	    "fans": {
	        "Fan1(sys_fan1)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan2(sys_fan2)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan3(sys_fan3)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan4(sys_fan4)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan_in_PS1": {"direction": "none", "hw": "--", "status": "None"},
	        "Fan_in_PS2": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "fan_air_filter": "NotSupported",
	        "fan_zone_speed": "Zone 1: 0x80",
	    }
	}

	
	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironmentFan(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironmentFan(device=self.device)
		parsed_output = obj.parse()


		self.assertEqual(parsed_output, self.golden_parsed_output_1)

#==========================================
# unittest for show environment fan detail
#==========================================
class TestShowEnvironmentFanDetail(unittest.TestCase):
	'''unit test for "show environment fan detail"'''
	device = Device(name='aDevice')

	golden_output={'execute.return_value': '''
		Fan:
		---------------------------------------------------------------------------
		Fan             Model                Hw     Direction       Status
		---------------------------------------------------------------------------
		Fan1(sys_fan1)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan2(sys_fan2)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan3(sys_fan3)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan4(sys_fan4)  NXA-FAN-30CFM-B      --     front-to-back   Ok
		Fan_in_PS1                           --     none            None
		Fan_in_PS2      --                   --     front-to-back   Ok
		Fan Zone Speed: Zone 1: 0x80
		Fan Air Filter : NotSupported
		Fan:
		------------------------------------------------------------------
		 Fan Name          Fan Num   Fan Direction   Speed(%)  Speed(RPM)
		------------------------------------------------------------------
		Fan1(sys_fan1)      fan1    front-to-back    49        5934
		Fan1(sys_fan1)      fan2    front-to-back    40        4511
		Fan2(sys_fan2)      fan1    front-to-back    51        6199
		Fan2(sys_fan2)      fan2    front-to-back    40        4568
		Fan3(sys_fan3)      fan1    front-to-back    51        6171
		Fan3(sys_fan3)      fan2    front-to-back    41        4691
		Fan4(sys_fan4)      fan1    front-to-back    50        6081
		Fan4(sys_fan4)      fan2    front-to-back    40        4534

	'''
	}

	golden_parsed_output = {
	    "fans": {
	        "Fan1(sys_fan1)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan2(sys_fan2)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan3(sys_fan3)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan4(sys_fan4)": {
	            "direction": "front-to-back",
	            "hw": "--",
	            "model": "NXA-FAN-30CFM-B",
	            "status": "Ok",
	        },
	        "Fan_in_PS1": {"direction": "none", "hw": "--", "status": "None"},
	        "Fan_in_PS2": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "fan_air_filter": "NotSupported",
	        "fan_zone_speed": "Zone 1: 0x80",
	        "ps_fans": {},
	        "sys_fans": {
	            "Fan1(sys_fan1)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 49,
	                    "speed_rpm": 5934,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 40,
	                    "speed_rpm": 4511,
	                },
	            },
	            "Fan2(sys_fan2)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 51,
	                    "speed_rpm": 6199,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 40,
	                    "speed_rpm": 4568,
	                },
	            },
	            "Fan3(sys_fan3)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 51,
	                    "speed_rpm": 6171,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 41,
	                    "speed_rpm": 4691,
	                },
	            },
	            "Fan4(sys_fan4)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 50,
	                    "speed_rpm": 6081,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 40,
	                    "speed_rpm": 4534,
	                },
	            },
	        },
	    }
	}


	golden_output_1= {'execute.return_value': '''
		Fan:
		---------------------------------------------------------------------------
		Fan             Model                Hw     Direction       Status
		---------------------------------------------------------------------------
		Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
		Fan2(sys_fan2)  N9K-C9508-FAN        0.6020 front-to-back   Ok
		Fan3(sys_fan3)  N9K-C9508-FAN        0.6020 front-to-back   Ok
		Fan_in_PS1                           --     front-to-back   Ok
		Fan_in_PS2                           --     front-to-back   Ok
		Fan_in_PS3                           --     front-to-back   Ok
		Fan_in_PS4                           --     front-to-back   Ok
		Fan_in_PS5                           --     front-to-back   Shutdown
		Fan_in_PS6                           --     front-to-back   Shutdown
		Fan_in_PS7                           --     front-to-back   Ok
		Fan_in_PS8                           --     front-to-back   Ok
		Fan Zone Speed: Zone 1: 0x37
		Fan Air Filter : NotSupported
		Fan:
		------------------------------------------------------------------
		 Fan Name          Fan Num   Fan Direction   Speed(%)  Speed(RPM)
		------------------------------------------------------------------
		Fan1(sys_fan1)      fan1    front-to-back    39        2500
		Fan1(sys_fan1)      fan2    front-to-back    85        3294
		Fan1(sys_fan1)      fan3    front-to-back    51        3245
		Fan1(sys_fan1)      fan4    front-to-back    75        2909
		Fan1(sys_fan1)      fan5    front-to-back    41        2603
		Fan1(sys_fan1)      fan6    front-to-back    84        3272
		Fan2(sys_fan2)      fan1    front-to-back    51        3280
		Fan2(sys_fan2)      fan2    front-to-back    61        2362
		Fan2(sys_fan2)      fan3    front-to-back    41        2653
		Fan2(sys_fan2)      fan4    front-to-back    82        3183
		Fan2(sys_fan2)      fan5    front-to-back    52        3331
		Fan2(sys_fan2)      fan6    front-to-back    69        2677
		Fan3(sys_fan3)      fan1    front-to-back    52        3310
		Fan3(sys_fan3)      fan2    front-to-back    70        2730
		Fan3(sys_fan3)      fan3    front-to-back    69        4361
		Fan3(sys_fan3)      fan4    front-to-back    75        2915
		Fan3(sys_fan3)      fan5    front-to-back    40        2588
		Fan3(sys_fan3)      fan6    front-to-back    85        3300

		Fan Speed (Power Supply):
		--------------------------------------------------------------------------
		Fan in PSU        Fan1 Speed(RPM)     Fan2 Speed(RPM)
		--------------------------------------------------------------------------
		Fan_in_PS1            7978                8537
		Fan_in_PS2            8021                8473
		Fan_in_PS3            7978                8451
		Fan_in_PS4            7978                8537
		Fan_in_PS5            ---                 ---
		Fan_in_PS6            ---                 ---
		Fan_in_PS7            7978                8516
		Fan_in_PS8            8064                8537
	'''
	}

	golden_parsed_output_1 = {
	    "fans": {
	        "Fan1(sys_fan1)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan2(sys_fan2)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan3(sys_fan3)": {
	            "direction": "front-to-back",
	            "hw": "0.6020",
	            "model": "N9K-C9508-FAN",
	            "status": "Ok",
	        },
	        "Fan_in_PS1": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS2": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS3": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS4": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS5": {"direction": "front-to-back", "hw": "--", "status": "Shutdown"},
	        "Fan_in_PS6": {"direction": "front-to-back", "hw": "--", "status": "Shutdown"},
	        "Fan_in_PS7": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "Fan_in_PS8": {"direction": "front-to-back", "hw": "--", "status": "Ok"},
	        "fan_air_filter": "NotSupported",
	        "fan_zone_speed": "Zone 1: 0x37",
	        "ps_fans": {
	            "Fan_in_PS1": {"fan1_speed": 7978, "fan2_speed": 8537},
	            "Fan_in_PS2": {"fan1_speed": 8021, "fan2_speed": 8473},
	            "Fan_in_PS3": {"fan1_speed": 7978, "fan2_speed": 8451},
	            "Fan_in_PS4": {"fan1_speed": 7978, "fan2_speed": 8537},
	            "Fan_in_PS7": {"fan1_speed": 7978, "fan2_speed": 8516},
	            "Fan_in_PS8": {"fan1_speed": 8064, "fan2_speed": 8537},
	        },
	        "sys_fans": {
	            "Fan1(sys_fan1)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 39,
	                    "speed_rpm": 2500,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 85,
	                    "speed_rpm": 3294,
	                },
	                "fan3": {
	                    "direction": "front-to-back",
	                    "speed_percent": 51,
	                    "speed_rpm": 3245,
	                },
	                "fan4": {
	                    "direction": "front-to-back",
	                    "speed_percent": 75,
	                    "speed_rpm": 2909,
	                },
	                "fan5": {
	                    "direction": "front-to-back",
	                    "speed_percent": 41,
	                    "speed_rpm": 2603,
	                },
	                "fan6": {
	                    "direction": "front-to-back",
	                    "speed_percent": 84,
	                    "speed_rpm": 3272,
	                },
	            },
	            "Fan2(sys_fan2)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 51,
	                    "speed_rpm": 3280,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 61,
	                    "speed_rpm": 2362,
	                },
	                "fan3": {
	                    "direction": "front-to-back",
	                    "speed_percent": 41,
	                    "speed_rpm": 2653,
	                },
	                "fan4": {
	                    "direction": "front-to-back",
	                    "speed_percent": 82,
	                    "speed_rpm": 3183,
	                },
	                "fan5": {
	                    "direction": "front-to-back",
	                    "speed_percent": 52,
	                    "speed_rpm": 3331,
	                },
	                "fan6": {
	                    "direction": "front-to-back",
	                    "speed_percent": 69,
	                    "speed_rpm": 2677,
	                },
	            },
	            "Fan3(sys_fan3)": {
	                "fan1": {
	                    "direction": "front-to-back",
	                    "speed_percent": 52,
	                    "speed_rpm": 3310,
	                },
	                "fan2": {
	                    "direction": "front-to-back",
	                    "speed_percent": 70,
	                    "speed_rpm": 2730,
	                },
	                "fan3": {
	                    "direction": "front-to-back",
	                    "speed_percent": 69,
	                    "speed_rpm": 4361,
	                },
	                "fan4": {
	                    "direction": "front-to-back",
	                    "speed_percent": 75,
	                    "speed_rpm": 2915,
	                },
	                "fan5": {
	                    "direction": "front-to-back",
	                    "speed_percent": 40,
	                    "speed_rpm": 2588,
	                },
	                "fan6": {
	                    "direction": "front-to-back",
	                    "speed_percent": 85,
	                    "speed_rpm": 3300,
	                },
	            },
	        },
	    }
	}


	
	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironmentFanDetail(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironmentFanDetail(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output_1)

#=======================================
# unittest for show environment power
#=======================================
class TestShowEnvironmentPower(unittest.TestCase):
	'''unit test for "show environment fan"'''
	device = Device(name='aDevice')


	golden_output={'execute.return_value': '''
		Power Supply:
		Voltage: 12 Volts
		Power                      Actual             Actual        Total
		Supply    Model            Output             Input        Capacity     Status
		                           (Watts )           (Watts )     (Watts )
		-------  ----------  ---------------  ------  ----------  --------------------
		1        ------------            0 W                0 W         0 W   Absent
		2        NXA-PAC-650W-PI       126 W              140 W       650 W      Ok


		Power Usage Summary:
		--------------------
		Power Supply redundancy mode (configured)                Non-Redundant(combined)
		Power Supply redundancy mode (operational)               Non-Redundant(combined)

		Total Power Capacity (based on configured mode)             650.00 W
		Total Grid-A (first half of PS slots) Power Capacity          0.00 W
		Total Grid-B (second half of PS slots) Power Capacity       650.00 W
		Total Power of all Inputs (cumulative)                      650.00 W
		Total Power Output (actual draw)                            126.00 W
		Total Power Input (actual draw)                             140.00 W
		Total Power Allocated (budget)                                N/A
		Total Power Available for additional modules                  N/A
	'''
	}

	golden_parsed_output = {
	    "power": {
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "------------",
	                "status": "Absent",
	                "total_capacity_watts": 0,
	            },
	            "2": {
	                "actual_input_watts": 140,
	                "actual_output_watts": 126,
	                "model": "NXA-PAC-650W-PI",
	                "status": "Ok",
	                "total_capacity_watts": 650,
	            },
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 0.0,
	            "total_grid_b_power_watts": 650.0,
	            "total_power_capacity_watts": 650.0,
	            "total_power_cumulative_watts": 650.0,
	            "total_power_input_watts": 140.0,
	            "total_power_output_watts": 126.0,
	        },
	        "voltage": 12,
	    }
	}


	golden_output_1= {'execute.return_value': '''
		Power Supply:
		Voltage: 12 Volts
		Power                      Actual             Actual        Total
		Supply    Model            Output             Input        Capacity     Status
		                           (Watts )           (Watts )     (Watts )
		-------  ----------  ---------------  ------  ----------  --------------------
		1        N9K-PAC-3000W-B      1076 W             1133 W      3000 W      Ok
		2        N9K-PAC-3000W-B      1083 W             1136 W      3000 W      Ok
		3        N9K-PAC-3000W-B      1090 W             1150 W      3000 W      Ok
		4        N9K-PAC-3000W-B      1133 W             1210 W      3000 W      Ok
		5        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
		6        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
		7        N9K-PAC-3000W        1080 W             1143 W      3000 W      Ok
		8        N9K-PAC-3000W-B       126 W              168 W      3000 W      Ok


		                                  Actual        Power
		Module    Model                     Draw    Allocated    Status
		                                 (Watts )     (Watts )
		-------  -------------------  -----------  -----------  --------------
		1        N9K-X9736Q-FX           387.00 W     936.00 W    Powered-Up
		2        N9K-X9736C-FX           379.00 W     756.00 W    Powered-Up
		3        N9K-X9732C-EXM          568.00 W     816.00 W    Powered-Up
		4        N9K-X9732C-EXM          576.00 W     816.00 W    Powered-Up
		5        N9K-X9732C-EXM          565.00 W     816.00 W    Powered-Up
		6        N9K-X9732C-EXM          597.00 W     816.00 W    Powered-Up
		7        N9K-X9732C-EXM          620.00 W     816.00 W    Powered-Up
		8        N9K-X9736C-FX           362.00 W     756.00 W    Powered-Up
		Xb21     xbar                      N/A          0.00 W    Absent
		Xb22     N9K-C9508-FM-E          176.00 W     564.00 W    Powered-Up
		Xb23     N9K-C9508-FM-E          180.00 W     564.00 W    Powered-Up
		Xb24     N9K-C9508-FM-E          205.00 W     564.00 W    Powered-Up
		Xb25     N9K-C9508-FM-E            N/A        564.00 W    Powered-Dn
		Xb26     N9K-C9508-FM-E          201.00 W     564.00 W    Powered-Up
		27       N9K-SUP-A                60.00 W      90.00 W    Powered-Up
		28       supervisor                N/A          0.00 W    Powered-Up
		29       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
		30       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
		fan1     N9K-C9508-FAN            76.00 W     249.00 W    Powered-Up
		fan2     N9K-C9508-FAN            86.00 W     249.00 W    Powered-Up
		fan3     N9K-C9508-FAN           101.00 W     249.00 W    Powered-Up

		N/A - Per module power not available


		Power Usage Summary:
		--------------------
		Power Supply redundancy mode (configured)                Non-Redundant(combined)
		Power Supply redundancy mode (operational)               Non-Redundant(combined)

		Total Power Capacity (based on configured mode)            18000.00 W
		Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
		Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
		Total Power of all Inputs (cumulative)                     18000.00 W
		Total Power Output (actual draw)                           5591.00 W
		Total Power Input (actual draw)                            5943.00 W
		Total Power Allocated (budget)                             10327.00 W
		Total Power Available for additional modules               7673.00 W
	'''
	}

	golden_parsed_output_1 = {
	    "power": {
	        "modules": {
	            "1": {
	                "actual_drawn": "387.00",
	                "allocated_power": 936.0,
	                "model": "N9K-X9736Q-FX",
	                "status": "Powered-Up",
	            },
	            "2": {
	                "actual_drawn": "379.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "27": {
	                "actual_drawn": "60.00",
	                "allocated_power": 90.0,
	                "model": "N9K-SUP-A",
	                "status": "Powered-Up",
	            },
	            "29": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "3": {
	                "actual_drawn": "568.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "30": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "4": {
	                "actual_drawn": "576.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "5": {
	                "actual_drawn": "565.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "6": {
	                "actual_drawn": "597.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "7": {
	                "actual_drawn": "620.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "8": {
	                "actual_drawn": "362.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "Xb22": {
	                "actual_drawn": "176.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb23": {
	                "actual_drawn": "180.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb24": {
	                "actual_drawn": "205.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb26": {
	                "actual_drawn": "201.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "fan1": {
	                "actual_drawn": "76.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan2": {
	                "actual_drawn": "86.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan3": {
	                "actual_drawn": "101.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	        },
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 1133,
	                "actual_output_watts": 1076,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "2": {
	                "actual_input_watts": 1136,
	                "actual_output_watts": 1083,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "3": {
	                "actual_input_watts": 1150,
	                "actual_output_watts": 1090,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "4": {
	                "actual_input_watts": 1210,
	                "actual_output_watts": 1133,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "5": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "6": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "7": {
	                "actual_input_watts": 1143,
	                "actual_output_watts": 1080,
	                "model": "N9K-PAC-3000W",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "8": {
	                "actual_input_watts": 168,
	                "actual_output_watts": 126,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 12000.0,
	            "total_grid_b_power_watts": 6000.0,
	            "total_power_allocated_watts": 10327.0,
	            "total_power_available_watts": 7673.0,
	            "total_power_capacity_watts": 18000.0,
	            "total_power_cumulative_watts": 18000.0,
	            "total_power_input_watts": 5943.0,
	            "total_power_output_watts": 5591.0,
	        },
	        "voltage": 12,
	    }
	}


	
	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironmentPower(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironmentPower(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output_1)


#=======================================
# unittest for show environment power detail
#=======================================
class TestShowEnvironmentPowerDetail(unittest.TestCase):
	'''unit test for "show environment fan"'''
	device = Device(name='aDevice')


	golden_output={'execute.return_value': '''
		Power Supply:
		Voltage: 12 Volts
		Power                      Actual             Actual        Total
		Supply    Model            Output             Input        Capacity     Status
		                           (Watts )           (Watts )     (Watts )
		-------  ----------  ---------------  ------  ----------  --------------------
		1        ------------            0 W                0 W         0 W   Absent
		2        NXA-PAC-650W-PI       126 W              140 W       650 W      Ok


		Power Usage Summary:
		--------------------
		Power Supply redundancy mode (configured)                Non-Redundant(combined)
		Power Supply redundancy mode (operational)               Non-Redundant(combined)

		Total Power Capacity (based on configured mode)             650.00 W
		Total Grid-A (first half of PS slots) Power Capacity          0.00 W
		Total Grid-B (second half of PS slots) Power Capacity       650.00 W
		Total Power of all Inputs (cumulative)                      650.00 W
		Total Power Output (actual draw)                            126.00 W
		Total Power Input (actual draw)                             140.00 W
		Total Power Allocated (budget)                                N/A
		Total Power Available for additional modules                  N/A


		Power Usage details:
		--------------------
		Power reserved for Supervisor(s):                             N/A
		Power reserved for Fabric, SC Module(s):                      N/A
		Power reserved for Fan Module(s):                             N/A
		Total power reserved for Sups,SCs,Fabrics,Fans:               N/A

		Are all inlet cords connected: No

		Power supply details:
		---------------------
		PS_2 total capacity:     650 W   Voltage:12V

		Pin:140.00W  Vin:236.00V    Iin:0.62A    Pout:126.00W    Vout:12.01V    Iout:10.50A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits


	'''
	}

	golden_parsed_output = {
	    "power": {
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "------------",
	                "status": "Absent",
	                "total_capacity_watts": 0,
	            },
	            "2": {
	                "actual_input_watts": 140,
	                "actual_output_watts": 126,
	                "model": "NXA-PAC-650W-PI",
	                "status": "Ok",
	                "total_capacity_watts": 650,
	            },
	        },
	        "power_supply_details": {
	            "PS_2": {
	                "Iin": 0.62,
	                "Iout": 10.5,
	                "Pin": 140.0,
	                "Pout": 126.0,
	                "Vin": 236.0,
	                "Vout": 12.01,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 650,
	                "voltage": 12,
	            }
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
            "power_usage_details":{
            	"power_reserved_for_sup_watts" : "N/A",
            	"power_reserved_for_fabric_sc_watts": "N/A",
            	"power_reserved_for_fan_module_watts": "N/A",
            	"total_power_reserved_watts": "N/A",
            	"all_inlet_cords_connected": "No" 
            },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 0.0,
	            "total_grid_b_power_watts": 650.0,
	            "total_power_capacity_watts": 650.0,
	            "total_power_cumulative_watts": 650.0,
	            "total_power_input_watts": 140.0,
	            "total_power_output_watts": 126.0,
	        },
	        "voltage": 12,
	    }
	}


	golden_output_1= {'execute.return_value': '''
		Power Supply:
		Voltage: 12 Volts
		Power                      Actual             Actual        Total
		Supply    Model            Output             Input        Capacity     Status
		                           (Watts )           (Watts )     (Watts )
		-------  ----------  ---------------  ------  ----------  --------------------
		1        N9K-PAC-3000W-B      1076 W             1133 W      3000 W      Ok
		2        N9K-PAC-3000W-B      1083 W             1147 W      3000 W      Ok
		3        N9K-PAC-3000W-B      1090 W             1154 W      3000 W      Ok
		4        N9K-PAC-3000W-B      1133 W             1217 W      3000 W      Ok
		5        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
		6        N9K-PAC-3000W-B         0 W                0 W         0 W   Shutdown
		7        N9K-PAC-3000W        1076 W             1143 W      3000 W      Ok
		8        N9K-PAC-3000W-B       126 W              175 W      3000 W      Ok


		                                  Actual        Power
		Module    Model                     Draw    Allocated    Status
		                                 (Watts )     (Watts )
		-------  -------------------  -----------  -----------  --------------
		1        N9K-X9736Q-FX           388.00 W     936.00 W    Powered-Up
		2        N9K-X9736C-FX           375.00 W     756.00 W    Powered-Up
		3        N9K-X9732C-EXM          574.00 W     816.00 W    Powered-Up
		4        N9K-X9732C-EXM          567.00 W     816.00 W    Powered-Up
		5        N9K-X9732C-EXM          570.00 W     816.00 W    Powered-Up
		6        N9K-X9732C-EXM          599.00 W     816.00 W    Powered-Up
		7        N9K-X9732C-EXM          612.00 W     816.00 W    Powered-Up
		8        N9K-X9736C-FX           370.00 W     756.00 W    Powered-Up
		Xb21     xbar                      N/A          0.00 W    Absent
		Xb22     N9K-C9508-FM-E          176.00 W     564.00 W    Powered-Up
		Xb23     N9K-C9508-FM-E          180.00 W     564.00 W    Powered-Up
		Xb24     N9K-C9508-FM-E          205.00 W     564.00 W    Powered-Up
		Xb25     N9K-C9508-FM-E            N/A        564.00 W    Powered-Dn
		Xb26     N9K-C9508-FM-E          201.00 W     564.00 W    Powered-Up
		27       N9K-SUP-A                60.00 W      90.00 W    Powered-Up
		28       N9K-SUP-A                59.00 W      90.00 W    Powered-Up
		29       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
		30       N9K-SC-A                 14.00 W      25.20 W    Powered-Up
		fan1     N9K-C9508-FAN            76.00 W     249.00 W    Powered-Up
		fan2     N9K-C9508-FAN            79.00 W     249.00 W    Powered-Up
		fan3     N9K-C9508-FAN           102.00 W     249.00 W    Powered-Up

		N/A - Per module power not available


		Power Usage Summary:
		--------------------
		Power Supply redundancy mode (configured)                Non-Redundant(combined)
		Power Supply redundancy mode (operational)               Non-Redundant(combined)

		Total Power Capacity (based on configured mode)            18000.00 W
		Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
		Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
		Total Power of all Inputs (cumulative)                     18000.00 W
		Total Power Output (actual draw)                           5588.00 W
		Total Power Input (actual draw)                            5971.00 W
		Total Power Allocated (budget)                             10327.00 W
		Total Power Available for additional modules               7673.00 W


		Power Usage details:
		--------------------
		Power reserved for Supervisor(s):                              180 W
		Power reserved for Fabric, SC Module(s):                      2870 W
		Power reserved for Fan Module(s):                              740 W
		Total power reserved for Sups,SCs,Fabrics,Fans:               3799 W

		Are all inlet cords connected: No

		Power supply details:
		---------------------
		PS_1 total capacity:    3000 W   Voltage:12V

		Pin:1133.12W  Vin:236.07V    Iin:4.84A    Pout:1076.82W    Vout:12.08V    Iout:89.74A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits

		PS_2 total capacity:    3000 W   Voltage:12V

		Pin:1147.20W  Vin:235.48V    Iin:4.89A    Pout:1083.86W    Vout:12.10V    Iout:90.03A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits

		PS_3 total capacity:    3000 W   Voltage:12V

		Pin:1154.24W  Vin:235.19V    Iin:4.91A    Pout:1090.90W    Vout:12.04V    Iout:90.91A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits

		PS_4 total capacity:    3000 W   Voltage:12V

		Pin:1217.58W  Vin:236.66V    Iin:5.11A    Pout:1133.12W    Vout:12.10V    Iout:93.84A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits

		PS_5 total capacity:       0 W   Voltage:12V

		Pin:0.00W  Vin:0.00V    Iin:0.00A    Pout:0.00W    Vout:0.00V    Iout:0.00A

		Cord not connected
		Software-Alarm: No
		Hardware alarm_bits reg0:20, reg2: 1,
		Reg0 bit5: No input detected
		Reg2 bit0: Vin out of range

		PS_6 total capacity:       0 W   Voltage:12V

		Pin:28.15W  Vin:0.00V    Iin:0.17A    Pout:0.00W    Vout:0.00V    Iout:0.00A

		Cord not connected
		Software-Alarm: No
		Hardware alarm_bits reg0:28, reg2: 1,
		Reg0 bit3: Fan Fault
		Reg0 bit5: No input detected
		Reg2 bit0: Vin out of range

		PS_7 total capacity:    3000 W   Voltage:12V

		Pin:1143.68W  Vin:236.07V    Iin:4.89A    Pout:1076.82W    Vout:12.08V    Iout:90.03A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits

		PS_8 total capacity:    3000 W   Voltage:12V

		Pin:175.95W  Vin:236.95V    Iin:0.81A    Pout:126.68W    Vout:12.11V    Iout:11.14A

		Cord connected to 220V AC
		Software-Alarm: No
		Hardware alarm_bits
	'''
	}

	golden_parsed_output_1 = {
	    "power": {
	        "modules": {
	            "1": {
	                "actual_drawn": "388.00",
	                "allocated_power": 936.0,
	                "model": "N9K-X9736Q-FX",
	                "status": "Powered-Up",
	            },
	            "2": {
	                "actual_drawn": "375.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "27": {
	                "actual_drawn": "60.00",
	                "allocated_power": 90.0,
	                "model": "N9K-SUP-A",
	                "status": "Powered-Up",
	            },
	            "28": {
	                "actual_drawn": "59.00",
	                "allocated_power": 90.0,
	                "model": "N9K-SUP-A",
	                "status": "Powered-Up",
	            },
	            "29": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "3": {
	                "actual_drawn": "574.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "30": {
	                "actual_drawn": "14.00",
	                "allocated_power": 25.2,
	                "model": "N9K-SC-A",
	                "status": "Powered-Up",
	            },
	            "4": {
	                "actual_drawn": "567.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "5": {
	                "actual_drawn": "570.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "6": {
	                "actual_drawn": "599.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "7": {
	                "actual_drawn": "612.00",
	                "allocated_power": 816.0,
	                "model": "N9K-X9732C-EXM",
	                "status": "Powered-Up",
	            },
	            "8": {
	                "actual_drawn": "370.00",
	                "allocated_power": 756.0,
	                "model": "N9K-X9736C-FX",
	                "status": "Powered-Up",
	            },
	            "Xb22": {
	                "actual_drawn": "176.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb23": {
	                "actual_drawn": "180.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb24": {
	                "actual_drawn": "205.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "Xb26": {
	                "actual_drawn": "201.00",
	                "allocated_power": 564.0,
	                "model": "N9K-C9508-FM-E",
	                "status": "Powered-Up",
	            },
	            "fan1": {
	                "actual_drawn": "76.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan2": {
	                "actual_drawn": "79.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	            "fan3": {
	                "actual_drawn": "102.00",
	                "allocated_power": 249.0,
	                "model": "N9K-C9508-FAN",
	                "status": "Powered-Up",
	            },
	        },
	        "power_supply": {
	            "1": {
	                "actual_input_watts": 1133,
	                "actual_output_watts": 1076,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "2": {
	                "actual_input_watts": 1147,
	                "actual_output_watts": 1083,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "3": {
	                "actual_input_watts": 1154,
	                "actual_output_watts": 1090,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "4": {
	                "actual_input_watts": 1217,
	                "actual_output_watts": 1133,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "5": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "6": {
	                "actual_input_watts": 0,
	                "actual_output_watts": 0,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Shutdown",
	                "total_capacity_watts": 0,
	            },
	            "7": {
	                "actual_input_watts": 1143,
	                "actual_output_watts": 1076,
	                "model": "N9K-PAC-3000W",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	            "8": {
	                "actual_input_watts": 175,
	                "actual_output_watts": 126,
	                "model": "N9K-PAC-3000W-B",
	                "status": "Ok",
	                "total_capacity_watts": 3000,
	            },
	        },
	        "power_supply_details": {
	            "PS_1": {
	                "Iin": 4.84,
	                "Iout": 89.74,
	                "Pin": 1133.12,
	                "Pout": 1076.82,
	                "Vin": 236.07,
	                "Vout": 12.08,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	            "PS_2": {
	                "Iin": 4.89,
	                "Iout": 90.03,
	                "Pin": 1147.2,
	                "Pout": 1083.86,
	                "Vin": 235.48,
	                "Vout": 12.1,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	            "PS_3": {
	                "Iin": 4.91,
	                "Iout": 90.91,
	                "Pin": 1154.24,
	                "Pout": 1090.9,
	                "Vin": 235.19,
	                "Vout": 12.04,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	            "PS_4": {
	                "Iin": 5.11,
	                "Iout": 93.84,
	                "Pin": 1217.58,
	                "Pout": 1133.12,
	                "Vin": 236.66,
	                "Vout": 12.1,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	            "PS_5": {
	                "Iin": 0.0,
	                "Iout": 0.0,
	                "Pin": 0.0,
	                "Pout": 0.0,
	                "Vin": 0.0,
	                "Vout": 0.0,
	                "connected_to": "None",
	                "cord_connected": False,
	                "hardware_alarm": "reg0:20, reg2: " "1,",
	                "hw_registers": [
	                    {"Reg0 bit5": "No " "input " "detected"},
	                    {"Reg2 bit0": "Vin " "out " "of " "range"},
	                ],
	                "software_alarm": "No",
	                "total_capacity_watts": 0,
	                "voltage": 12,
	            },
	            "PS_6": {
	                "Iin": 0.17,
	                "Iout": 0.0,
	                "Pin": 28.15,
	                "Pout": 0.0,
	                "Vin": 0.0,
	                "Vout": 0.0,
	                "connected_to": "None",
	                "cord_connected": False,
	                "hardware_alarm": "reg0:28, reg2: " "1,",
	                "hw_registers": [
	                    {"Reg0 bit3": "Fan " "Fault"},
	                    {"Reg0 bit5": "No " "input " "detected"},
	                    {"Reg2 bit0": "Vin " "out " "of " "range"},
	                ],
	                "software_alarm": "No",
	                "total_capacity_watts": 0,
	                "voltage": 12,
	            },
	            "PS_7": {
	                "Iin": 4.89,
	                "Iout": 90.03,
	                "Pin": 1143.68,
	                "Pout": 1076.82,
	                "Vin": 236.07,
	                "Vout": 12.08,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	            "PS_8": {
	                "Iin": 0.81,
	                "Iout": 11.14,
	                "Pin": 175.95,
	                "Pout": 126.68,
	                "Vin": 236.95,
	                "Vout": 12.11,
	                "connected_to": "220",
	                "cord_connected": True,
	                "hardware_alarm": "",
	                "software_alarm": "No",
	                "total_capacity_watts": 3000,
	                "voltage": 12,
	            },
	        },
	        "power_supply_mode": {
	            "config_mode": "Non-Redundant(combined)",
	            "oper_mode": "Non-Redundant(combined)",
	        },
	        "power_usage_details":{
            	"power_reserved_for_sup_watts" : "180",
            	"power_reserved_for_fabric_sc_watts": "2870",
            	"power_reserved_for_fan_module_watts": "740",
            	"total_power_reserved_watts": "3799",
            	"all_inlet_cords_connected": "No" 
            },
	        "power_usage_summary": {
	            "total_grid_a_power_watts": 12000.0,
	            "total_grid_b_power_watts": 6000.0,
	            "total_power_allocated_watts": 10327.0,
	            "total_power_available_watts": 7673.0,
	            "total_power_capacity_watts": 18000.0,
	            "total_power_cumulative_watts": 18000.0,
	            "total_power_input_watts": 5971.0,
	            "total_power_output_watts": 5588.0,
	        },
	        "voltage": 12,
	    }
	}


	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironmentPowerDetail(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironmentPowerDetail(device=self.device)
		parsed_output = obj.parse()

		self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ===========================================
# Unit test for 'show environment temperature'
# ===========================================
class TestShowEnvironmentTemperature(unittest.TestCase):
	'''unit test for "show environment temperature"'''
	device = Device(name='aDevice')

	empty_output = {'execute.return_value': ''}

	golden_output={'execute.return_value': '''
			show environment temperature
			Temperature:
			--------------------------------------------------------------------
			Module   Sensor        MajorThresh   MinorThres   CurTemp     Status
			                       (Celsius)     (Celsius)    (Celsius)
			--------------------------------------------------------------------
			1        CPU             85              75          50         Ok
			1        HOM0            105             95          70         Ok
			1        HOM1            105             95          79         Ok
			1        HOM2            105             95          79         Ok
			1        HOM3            105             95          79         Ok
			1        VRM1            110             100         59         Ok
			1        VRM2            110             100         60         Ok
			1        VRM3            110             100         54         Ok
			1        VRM4            110             100         54         Ok
			2        CPU             85              75          46         Ok
			2        HOM0            105             95          65         Ok
			2        HOM1            105             95          73         Ok
			2        HOM2            105             95          73         Ok
			2        HOM3            105             95          73         Ok
			2        VRM1            110             100         55         Ok
			2        VRM2            110             100         57         Ok
			2        VRM3            110             100         46         Ok
			2        VRM4            110             100         49         Ok
			3        CPU             85              75          41         Ok
			3        SUG0            105             95          57         Ok
			3        SUG1            105             95          68         Ok
			3        SUG2            105             95          55         Ok
			3        SUG3            105             95          65         Ok
			3        VRM1            110             100         54         Ok
			3        VRM2            110             100         56         Ok
			3        VRM3            110             100         50         Ok
			3        VRM4            110             100         50         Ok
			4        CPU             85              75          36         Ok
			4        SUG0            105             95          57         Ok
			4        SUG1            105             95          68         Ok
			4        SUG2            105             95          54         Ok
			4        SUG3            105             95          65         Ok
			4        VRM1            110             100         53         Ok
			4        VRM2            110             100         52         Ok
			4        VRM3            110             100         50         Ok
			4        VRM4            110             100         50         Ok
			5        CPU             85              75          39         Ok
			5        SUG0            105             95          55         Ok
			5        SUG1            105             95          64         Ok
			5        SUG2            105             95          53         Ok
			5        SUG3            105             95          62         Ok
			5        VRM1            110             100         50         Ok
			5        VRM2            110             100         51         Ok
			5        VRM3            110             100         51         Ok
			5        VRM4            110             100         47         Ok
			6        CPU             85              75          42         Ok
			6        SUG0            105             95          57         Ok
			6        SUG1            105             95          67         Ok
			6        SUG2            105             95          51         Ok
			6        SUG3            105             95          73         Ok
			6        VRM1            110             100         53         Ok
			6        VRM2            110             100         53         Ok
			6        VRM3            110             100         52         Ok
			6        VRM4            110             100         53         Ok
			7        CPU             85              75          38         Ok
			7        SUG0            105             95          62         Ok
			7        SUG1            105             95          88         Ok
			7        SUG2            105             95          54         Ok
			7        SUG3            105             95          69         Ok
			7        VRM1            110             100         53         Ok
			7        VRM2            110             100         55         Ok
			7        VRM3            110             100         53         Ok
			7        VRM4            110             100         51         Ok
			8        CPU             85              75          40         Ok
			8        HOM0            105             95          52         Ok
			8        HOM1            105             95          59         Ok
			8        HOM2            105             95          59         Ok
			8        HOM3            105             95          59         Ok
			8        VRM1            110             100         48         Ok
			8        VRM2            110             100         48         Ok
			8        VRM3            110             100         40         Ok
			8        VRM4            110             100         40         Ok
			22       CPU             85              75          46         Ok
			22       LAC0            105             95          65         Ok
			22       LAC1            105             95          60         Ok
			22       VRM1            110             100         69         Ok
			22       VRM2            110             100         69         Ok
			23       CPU             85              75          47         Ok
			23       LAC0            105             95          67         Ok
			23       LAC1            105             95          62         Ok
			23       VRM1            110             100         69         Ok
			23       VRM2            110             100         69         Ok
			24       CPU             85              75          49         Ok
			24       LAC0            105             95          72         Ok
			24       LAC1            105             95          62         Ok
			24       VRM1            110             100         74         Ok
			24       VRM2            110             100         74         Ok
			26       CPU             85              75          39         Ok
			26       LAC0            105             95          58         Ok
			26       LAC1            105             95          55         Ok
			26       VRM1            110             100         57         Ok
			26       VRM2            110             100         57         Ok
			27       OUTLET          75              55          33         Ok
			27       INLET           60              42          22         Ok
			27       CPU             90              80          33         Ok
			28       OUTLET          75              55          32         Ok
			28       INLET           60              42          21         Ok
			28       CPU             90              80          29         Ok
			29       CPU             105             95          45         Ok
			30       CPU             105             95          47         Ok
		'''
    }

	golden_parsed_output= {
	    "1": {
	        "CPU": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "HOM0": {
	            "current_temp_celsius": 70,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM1": {
	            "current_temp_celsius": 79,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM2": {
	            "current_temp_celsius": 79,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM3": {
	            "current_temp_celsius": 79,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 59,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 60,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "2": {
	        "CPU": {
	            "current_temp_celsius": 46,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "HOM0": {
	            "current_temp_celsius": 65,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM1": {
	            "current_temp_celsius": 73,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM2": {
	            "current_temp_celsius": 73,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM3": {
	            "current_temp_celsius": 73,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 55,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 46,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 49,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "22": {
	        "CPU": {
	            "current_temp_celsius": 46,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "LAC0": {
	            "current_temp_celsius": 65,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "LAC1": {
	            "current_temp_celsius": 60,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 69,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 69,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "23": {
	        "CPU": {
	            "current_temp_celsius": 47,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "LAC0": {
	            "current_temp_celsius": 67,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "LAC1": {
	            "current_temp_celsius": 62,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 69,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 69,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "24": {
	        "CPU": {
	            "current_temp_celsius": 49,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "LAC0": {
	            "current_temp_celsius": 72,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "LAC1": {
	            "current_temp_celsius": 62,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 74,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 74,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "26": {
	        "CPU": {
	            "current_temp_celsius": 39,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "LAC0": {
	            "current_temp_celsius": 58,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "LAC1": {
	            "current_temp_celsius": 55,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "27": {
	        "CPU": {
	            "current_temp_celsius": 33,
	            "major_threshold_celsius": 90,
	            "minor_threshold_celsius": 80,
	            "status": "Ok",
	        },
	        "INLET": {
	            "current_temp_celsius": 22,
	            "major_threshold_celsius": 60,
	            "minor_threshold_celsius": 42,
	            "status": "Ok",
	        },
	        "OUTLET": {
	            "current_temp_celsius": 33,
	            "major_threshold_celsius": 75,
	            "minor_threshold_celsius": 55,
	            "status": "Ok",
	        },
	    },
	    "28": {
	        "CPU": {
	            "current_temp_celsius": 29,
	            "major_threshold_celsius": 90,
	            "minor_threshold_celsius": 80,
	            "status": "Ok",
	        },
	        "INLET": {
	            "current_temp_celsius": 21,
	            "major_threshold_celsius": 60,
	            "minor_threshold_celsius": 42,
	            "status": "Ok",
	        },
	        "OUTLET": {
	            "current_temp_celsius": 32,
	            "major_threshold_celsius": 75,
	            "minor_threshold_celsius": 55,
	            "status": "Ok",
	        },
	    },
	    "29": {
	        "CPU": {
	            "current_temp_celsius": 45,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        }
	    },
	    "3": {
	        "CPU": {
	            "current_temp_celsius": 41,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "SUG0": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG1": {
	            "current_temp_celsius": 68,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG2": {
	            "current_temp_celsius": 55,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG3": {
	            "current_temp_celsius": 65,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 56,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "30": {
	        "CPU": {
	            "current_temp_celsius": 47,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        }
	    },
	    "4": {
	        "CPU": {
	            "current_temp_celsius": 36,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "SUG0": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG1": {
	            "current_temp_celsius": 68,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG2": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG3": {
	            "current_temp_celsius": 65,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 52,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "5": {
	        "CPU": {
	            "current_temp_celsius": 39,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "SUG0": {
	            "current_temp_celsius": 55,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG1": {
	            "current_temp_celsius": 64,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG2": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG3": {
	            "current_temp_celsius": 62,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 50,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 51,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 51,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 47,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "6": {
	        "CPU": {
	            "current_temp_celsius": 42,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "SUG0": {
	            "current_temp_celsius": 57,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG1": {
	            "current_temp_celsius": 67,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG2": {
	            "current_temp_celsius": 51,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG3": {
	            "current_temp_celsius": 73,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 52,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "7": {
	        "CPU": {
	            "current_temp_celsius": 38,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "SUG0": {
	            "current_temp_celsius": 62,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG1": {
	            "current_temp_celsius": 88,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG2": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "SUG3": {
	            "current_temp_celsius": 69,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 55,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 53,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 51,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	    "8": {
	        "CPU": {
	            "current_temp_celsius": 40,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "HOM0": {
	            "current_temp_celsius": 52,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM1": {
	            "current_temp_celsius": 59,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM2": {
	            "current_temp_celsius": 59,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM3": {
	            "current_temp_celsius": 59,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 48,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 48,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 40,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 40,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    },
	}



	golden_output_1 = {'execute.return_value': '''
		show environment temperature module 1
		Temperature:
		--------------------------------------------------------------------
		Module   Sensor        MajorThresh   MinorThres   CurTemp     Status
		                       (Celsius)     (Celsius)    (Celsius)
		--------------------------------------------------------------------
		1        CPU             85              75          48         Ok
		1        HOM0            105             95          68         Ok
		1        HOM1            105             95          77         Ok
		1        HOM2            105             95          77         Ok
		1        HOM3            105             95          77         Ok
		1        VRM1            110             100         58         Ok
		1        VRM2            110             100         59         Ok
		1        VRM3            110             100         54         Ok
		1        VRM4            110             100         54         Ok
	'''
	}

	golden_parsed_output_1 = {
	    "1": {
	        "CPU": {
	            "current_temp_celsius": 48,
	            "major_threshold_celsius": 85,
	            "minor_threshold_celsius": 75,
	            "status": "Ok",
	        },
	        "HOM0": {
	            "current_temp_celsius": 68,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM1": {
	            "current_temp_celsius": 77,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM2": {
	            "current_temp_celsius": 77,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "HOM3": {
	            "current_temp_celsius": 77,
	            "major_threshold_celsius": 105,
	            "minor_threshold_celsius": 95,
	            "status": "Ok",
	        },
	        "VRM1": {
	            "current_temp_celsius": 58,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM2": {
	            "current_temp_celsius": 59,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM3": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	        "VRM4": {
	            "current_temp_celsius": 54,
	            "major_threshold_celsius": 110,
	            "minor_threshold_celsius": 100,
	            "status": "Ok",
	        },
	    }
	}



	def test_empty(self):
		self.maxDiff = None
		self.device = Mock(**self.empty_output)
		obj = ShowEnvironmentTemperature(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()
	
	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowEnvironmentTemperature(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowEnvironmentTemperature(device=self.device)
		parsed_output = obj.parse(module=1)

		self.assertEqual(parsed_output, self.golden_parsed_output_1)



if __name__ == '__main__':
    unittest.main()
