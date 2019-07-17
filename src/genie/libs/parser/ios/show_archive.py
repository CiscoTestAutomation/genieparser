''' show_archive.py

IOSXE parsers for the following show commands:
    * show archive
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_archive import ShowArchive as ShowArchive_iosxe,\
											     ShowArchiveConfigDifferences as ShowArchiveConfigDifferences_iosxe, \
												 ShowArchiveConfigIncrementalDiffs as ShowArchiveConfigIncrementalDiffs_iosxe

class ShowArchive(ShowArchive_iosxe):
    """ Parser for show archive """
    pass

class ShowArchiveConfigDifferences(ShowArchiveConfigDifferences_iosxe):
    """ Parser for the following commands:
        * show archive config differences
        * show archive config differences {fileA} {fileB}
        * show archive config differences {fileA}
    """
    pass

class ShowArchiveConfigIncrementalDiffs(ShowArchiveConfigIncrementalDiffs_iosxe):
    """ Parser for show archive config incremental-diffs <fileA>"""
    pass