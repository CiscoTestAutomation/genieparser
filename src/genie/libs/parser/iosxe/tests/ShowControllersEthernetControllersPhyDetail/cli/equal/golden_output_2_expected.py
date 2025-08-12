expected_output = {
  'interface': 'Te1/0/1',
  'if_id': '1032',
  'phy_registers': {
    '0': {
      'register_number': '0000c011',
      'hex_bit_value': '0a0f',
      'register_name': 'Firmware Revision 1 (Dev 1)',
      'bits': '0000101000001111'
    },
    '1': {
      'register_number': '0000c012',
      'hex_bit_value': '0900',
      'register_name': 'Firmware Revision 1 (Dev 1)',
      'bits': '0000100100000000'
    },
    '2': {
      'register_number': '00002002',
      'hex_bit_value': '002b',
      'register_name': 'Phy(M:DFC) ID (Dev 4)',
      'bits': '0000000000101011'
    },
    '3': {
      'register_number': '00002003',
      'hex_bit_value': '0bc3',
      'register_name': 'Phy(M:DFC) ID (Dev 4)',
      'bits': '0000101111000011'
    },
    '4': {
      'register_number': '0000f000',
      'hex_bit_value': '20c8',
      'register_name': 'C Unit Mode Config (Dev 1f)',
      'bits': '0010000011001000'
    },
    '5': {
      'register_number': '0000f001',
      'hex_bit_value': '0049',
      'register_name': 'C Unit Port Control1 (Dev 1f)',
      'bits': '0000000001001001'
    },
    '6': {
      'register_number': '0000f007',
      'hex_bit_value': '1009',
      'register_name': 'C Unit Port Control2 (Dev 1f)',
      'bits': '0001000000001001'
    },
    '7': {
      'register_number': '00000000',
      'hex_bit_value': '2040',
      'register_name': 'T Unit PMA Control1 (Dev 1)',
      'bits': '0010000001000000'
    },
    '8': {
      'register_number': '00000001',
      'hex_bit_value': '0006',
      'register_name': 'T Unit PMA Status1 (Dev 1)',
      'bits': '0000000000000110'
    },
    '9': {
      'register_number': '00000007',
      'hex_bit_value': '0009',
      'register_name': 'T Unit 10G PMA Control2 (Dev 1)',
      'bits': '0000000000001001'
    },
    '10': {
      'register_number': '00000008',
      'hex_bit_value': '9301',
      'register_name': 'T Unit 10G PMA Status2 (Dev 1)',
      'bits': '1001001100000001'
    },
    '11': {
      'register_number': '0000000a',
      'hex_bit_value': '0000',
      'register_name': 'T Unit 10G PMA Sig Det (Dev 1)',
      'bits': '0000000000000000'
    },
    '12': {
      'register_number': '0000000b',
      'hex_bit_value': '41a4',
      'register_name': 'T Unit PMA Extend Ability (Dev 1)',
      'bits': '0100000110100100'
    },
    '13': {
      'register_number': '00000015',
      'hex_bit_value': '0003',
      'register_name': 'T Un 2.5G/5G PMA Ext Abil (Dev 1)',
      'bits': '0000000000000011'
    },
    '14': {
      'register_number': '0000c034',
      'hex_bit_value': '4812',
      'register_name': 'T Un NBASE-T Dshift Ctrl (Dev 1)',
      'bits': '0100100000010010'
    },
    '15': {
      'register_number': '0000c035',
      'hex_bit_value': '0000',
      'register_name': 'T Un NBASE-T Dshift Stat (Dev 1)',
      'bits': '0000000000000000'
    },
    '16': {
      'register_number': '00000000',
      'hex_bit_value': '2040',
      'register_name': 'T Unit PCS Control (Dev 3)',
      'bits': '0010000001000000'
    },
    '17': {
      'register_number': '00000001',
      'hex_bit_value': '0006',
      'register_name': 'T Unit PCS status (Dev 3)',
      'bits': '0000000000000110'
    },
    '18': {
      'register_number': '00000004',
      'hex_bit_value': '00c1',
      'register_name': 'T Unit Speed Ablity (Dev 3)',
      'bits': '0000000011000001'
    },
    '19': {
      'register_number': '00000007',
      'hex_bit_value': '000b',
      'register_name': 'T Unit PCS Cntrl2 (Dev 3)',
      'bits': '0000000000001011'
    },
    '20': {
      'register_number': '00000008',
      'hex_bit_value': 'b008',
      'register_name': 'T Unit PCS status2 (Dev 3)',
      'bits': '1011000000001000'
    },
    '21': {
      'register_number': '00000014',
      'hex_bit_value': '000e',
      'register_name': 'T Unit PCS EEE Capab1 (Dev 3)',
      'bits': '0000000000001110'
    },
    '22': {
      'register_number': '00000015',
      'hex_bit_value': '0003',
      'register_name': 'T Unit PCS EEE Capab2 (Dev 3)',
      'bits': '0000000000000011'
    },
    '23': {
      'register_number': '00000020',
      'hex_bit_value': '0000',
      'register_name': 'T Unit NBASE PCS status1 (Dev 3)',
      'bits': '0000000000000000'
    },
    '24': {
      'register_number': '00000021',
      'hex_bit_value': '0000',
      'register_name': 'T Unit NBASE PCS status2 (Dev 3)',
      'bits': '0000000000000000'
    },
    '25': {
      'register_number': '00008000',
      'hex_bit_value': '0060',
      'register_name': 'T Unit Copper Control1 (Dev 3)',
      'bits': '0000000001100000'
    },
    '26': {
      'register_number': '00008001',
      'hex_bit_value': '0000',
      'register_name': 'T Unit Copper Control2 (Dev 3)',
      'bits': '0000000000000000'
    },
    '27': {
      'register_number': '00008002',
      'hex_bit_value': '4090',
      'register_name': 'T Unit Copper Control3 (Dev 3)',
      'bits': '0100000010010000'
    },
    '28': {
      'register_number': '00008003',
      'hex_bit_value': '0049',
      'register_name': 'T Unit Copper Control4 (Dev 3)',
      'bits': '0000000001001001'
    },
    '29': {
      'register_number': '00008008',
      'hex_bit_value': 'ac40',
      'register_name': 'T Unit Copper Status1 (Dev 3)',
      'bits': '1010110001000000'
    },
    '30': {
      'register_number': '00008009',
      'hex_bit_value': '0000',
      'register_name': 'T Unit Copper Status2 (Dev 3)',
      'bits': '0000000000000000'
    },
    '31': {
      'register_number': '00000000',
      'hex_bit_value': '3000',
      'register_name': 'T Unit AutoNeg Control (Dev 7)',
      'bits': '0011000000000000'
    },
    '32': {
      'register_number': '00000001',
      'hex_bit_value': '002d',
      'register_name': 'T Unit AutoNeg Status (Dev 7)',
      'bits': '0000000000101101'
    },
    '33': {
      'register_number': '00000010',
      'hex_bit_value': '1d41',
      'register_name': 'T Unit AutoNeg Advt (Dev 7)',
      'bits': '0001110101000001'
    },
    '34': {
      'register_number': '00000013',
      'hex_bit_value': 'c1e1',
      'register_name': 'T Unit LP AutoNeg Advt (Dev 7)',
      'bits': '1100000111100001'
    },
    '35': {
      'register_number': '00000020',
      'hex_bit_value': '1181',
      'register_name': 'T Un MultiBase-T AN Ctrl1 (Dev 7)',
      'bits': '0001000110000001'
    },
    '36': {
      'register_number': '00000021',
      'hex_bit_value': '0000',
      'register_name': 'T Un MultiBase-T AN Stat1 (Dev 7)',
      'bits': '0000000000000000'
    },
    '37': {
      'register_number': '00000040',
      'hex_bit_value': '000c',
      'register_name': 'T Un MultiBase-T AN Ctrl2 (Dev 7)',
      'bits': '0000000000001100'
    },
    '38': {
      'register_number': '00000041',
      'hex_bit_value': '0000',
      'register_name': 'T Un MultiBase-T AN Stat2 (Dev 7)',
      'bits': '0000000000000000'
    },
    '39': {
      'register_number': '00008000',
      'hex_bit_value': '0210',
      'register_name': 'T Unit 1G AutoNeg Cntrl (Dev 7)',
      'bits': '0000001000010000'
    },
    '40': {
      'register_number': '00008001',
      'hex_bit_value': '3b00',
      'register_name': 'T Unit 1G AutoNeg Status (Dev 7)',
      'bits': '0011101100000000'
    },
    '41': {
      'register_number': '0000800c',
      'hex_bit_value': '0001',
      'register_name': 'T Unit Fast Retrain Adv (Dev 7)',
      'bits': '0000000000000001'
    },
    '42': {
      'register_number': '0000800d',
      'hex_bit_value': '0000',
      'register_name': 'T Unit Fast Retrain Stat (Dev 7)',
      'bits': '0000000000000000'
    },
    '43': {
      'register_number': '00001000',
      'hex_bit_value': '0000',
      'register_name': 'H 802.3 AN Cntrl (Dev 7)',
      'bits': '0000000000000000'
    },
    '44': {
      'register_number': '00001001',
      'hex_bit_value': '000c',
      'register_name': 'H 802.3 AN Status (Dev 7)',
      'bits': '0000000000001100'
    },
    '45': {
      'register_number': '0000f003',
      'hex_bit_value': '0004',
      'register_name': 'H Unit Serdes Cntrl (Dev 4)',
      'bits': '0000000000000100'
    },
    '46': {
      'register_number': '0000f004',
      'hex_bit_value': '0004',
      'register_name': 'H Unit Serdes Cntrl2 (Dev 4)',
      'bits': '0000000000000100'
    },
    '47': {
      'register_number': '0000f00b',
      'hex_bit_value': '0000',
      'register_name': 'H Unit FIFO and CRC Int (Dev 4)',
      'bits': '0000000000000000'
    },
    '48': {
      'register_number': '00001000',
      'hex_bit_value': '2040',
      'register_name': 'H Unit 10GPCS Cntrl1 (Dev 4)',
      'bits': '0010000001000000'
    },
    '49': {
      'register_number': '00001001',
      'hex_bit_value': '0006',
      'register_name': 'H Unit 10GPCS Status1 (Dev 4)',
      'bits': '0000000000000110'
    },
    '50': {
      'register_number': '00001008',
      'hex_bit_value': '8001',
      'register_name': 'H Unit 10GPCS Status2 (Dev 4)',
      'bits': '1000000000000001'
    },
    '51': {
      'register_number': '00001020',
      'hex_bit_value': '100d',
      'register_name': 'H Unit 10GPCS PRBS Stat1 (Dev 4)',
      'bits': '0001000000001101'
    },
    '52': {
      'register_number': '00001021',
      'hex_bit_value': '8000',
      'register_name': 'H Unit 10GPCS BER Status2 (Dev 1)',
      'bits': '1000000000000000'
    },
    '53': {
      'register_number': '0000f0c9',
      'hex_bit_value': '7383',
      'register_name': 'H Unit IPG FIFO CTRL Reg(Dev 4)',
      'bits': '0111001110000011'
    },
    '54': {
      'register_number': '00002000',
      'hex_bit_value': '0140',
      'register_name': 'H Sgmii PCS Cntr (Dev 4)',
      'bits': '0000000101000000'
    },
    '55': {
      'register_number': '00002001',
      'hex_bit_value': '0149',
      'register_name': 'H Sgmii PCS status (Dev 4)',
      'bits': '0000000101001001'
    },
    '56': {
      'register_number': '0000f0a0',
      'hex_bit_value': '0064',
      'register_name': 'USXGMII AN Register (Dev 4)',
      'bits': '0000000001100100'
    },
    '57': {
      'register_number': '0000f0a1',
      'hex_bit_value': '5200',
      'register_name': 'USXGMII AN overwrite (Dev 4)',
      'bits': '0101001000000000'
    },
    '58': {
      'register_number': '0000f0a2',
      'hex_bit_value': '9401',
      'register_name': 'USXGMII AN LP (Dev 4)',
      'bits': '1001010000000001'
    },
    '59': {
      'register_number': '0000f0a3',
      'hex_bit_value': '0000',
      'register_name': 'USXGMII AN Reg 2 (Dev 4)',
      'bits': '0000000000000000'
    },
    '60': {
      'register_number': '0000f0a4',
      'hex_bit_value': '1080',
      'register_name': 'USXGMII AN Reg 2 (Dev 4)',
      'bits': '0001000010000000'
    },
    '61': {
      'register_number': '0000f0a5',
      'hex_bit_value': '4502',
      'register_name': 'USXGMII AN Reg 3 (Dev 4)',
      'bits': '0100010100000010'
    },
    '62': {
      'register_number': '0000f0a6',
      'hex_bit_value': 'd401',
      'register_name': 'USXGMII AN base page (Dev 4)',
      'bits': '1101010000000001'
    }
  }
}
