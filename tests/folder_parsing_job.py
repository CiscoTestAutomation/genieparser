import os
import sys
import argparse
from ats.datastructures.logic import And, Not, Or

from pyats.easypy import run
import genie.libs.parser.utils.unittests as unittests


def main(runtime):
    my_parser = argparse.ArgumentParser(description="Optional arguments for 'nose'-like tests")

    my_parser.add_argument('-o', "--operating_system",
                        type=str,
                        help='The OS you wish to filter on',
                        default=None)
    my_parser.add_argument('-c', "--class_name",
                        type=str,
                        help="The Class you wish to filter on, (not the Test File)",
                        default=None)
    my_parser.add_argument('-t', "--token",
                        type=str,
                        help="The Token associated with the class, such as 'asr1k'",
                        default=None)
    my_parser.add_argument('-f', "--display_failed",
                        help="Displaying only failed classes",
                        default=None,
                        action='store_true')
    my_parser.add_argument('-n', "--number",
                       type=int,
                       help="The specific unittest we want to run, such as '25'",
                       default=None)
                       
    args, unknown = my_parser.parse_known_args(sys.argv[1:])
    _os = args.operating_system

    _class = args.class_name

    _token = args.token

    _display_only_failed = args.display_failed

    _number = args.number
    run(testscript = unittests.__file__,
        runtime = runtime,
        _os=_os,
        _class=_class,
        _token=_token,
        _display_only_failed=_display_only_failed,
        _number=_number)

if __name__ == '__main__':
    unittests.run_tests()