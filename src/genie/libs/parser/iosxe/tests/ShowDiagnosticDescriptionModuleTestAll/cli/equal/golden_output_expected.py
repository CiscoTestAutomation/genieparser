expected_output = {
    'diag_test': {
        'module': {
            1: {
                'TestGoldPktLoopback': 'The GOLD packet Loopback test verifies the MAC level loopbackfunctionality. In this test, a GOLD packet, for which ASICprovides the support in hardware, is sent. The packet loops backat MAC level and is matched against the stored packet. It is anon-disruptive test.', 
                'TestFantray': 'This test verifies all fan modules have been inserted and workingproperly on the board. It is a non-disruptive test and can berun as a health monitoring test.', 
                'TestPhyLoopback': 'The PHY Loopback test verifies the PHY level loopbackfunctionality. In this test, a packet is sent which loops backat PHY level and is matched against the stored packet. It is adisruptive test and cannot be run as a health monitoring test.', 
                'TestThermal': 'This test verifies the temperature reading from the sensor isbelow the yellow temperature threshold. It is a non-disruptivetest and can be run as a health monitoring test.'
            }
        }
    }
}  