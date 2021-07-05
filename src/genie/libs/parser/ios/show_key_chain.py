'''show_key_chain.py
IOS parsers for the following show commands:
    * show key chain
'''

from genie.libs.parser.iosxe.show_key_chain import ShowKeyChain as \
                                                   ShowKeyChain_iosxe



class ShowKeyChain(ShowKeyChain_iosxe):
    ''' Parser for "show key chain" '''
    pass

