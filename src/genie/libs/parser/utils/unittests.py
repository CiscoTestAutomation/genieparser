"""Testing strategy for dynamic testing via folder structure."""

# Python
import os
import re
import sys
import glob
import json
import logging
import inspect
import pathlib
import argparse
import traceback
import importlib
from unittest.mock import Mock

# pyATS
from pyats import aetest
from pyats.easypy import run
from pyats.easypy import runtime
from pyats.log.utils import banner
from pyats.log.colour import FgColour
from pyats.aetest.loop import Iteration
from pyats.datastructures import TreeNode
from pyats.datastructures import AttrDict
from pyats.easypy.email import TEST_RESULT_ROW
from pyats.log.utils import banner, str_shortener
from pyats.aetest.reporter import StandaloneReporter

# Genie
from genie.utils.diff import Diff
from genie.libs import parser as _parser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.utils.common import format_output

log = logging.getLogger(__name__)
glo_values = AttrDict

EXCLUDE_CLASSES = {
    'nxos': ['RunBashTop']  # reason: use bash shell
}


#===========================================================================
#                            Helper Functions
#===========================================================================
def read_from_file(file_path):
    """Helper function to read from a file."""
    with open(file_path, "r") as f:
        return f.read()


def read_json_file(file_path):
    """Helper function to read in json."""
    with open(file_path) as f:
        data = json.load(f)
    return data


def read_python_file(file_path):
    """Helper function to read in a Python file, and look for expected_output."""
    _module = importlib.machinery.SourceFileLoader("expected",
                                                   file_path).load_module()
    return getattr(_module, "expected_output")


def get_operating_systems(_os):
    """Helper Script to get operating systems."""
    if _os:
        return [_os]
    EXCLUDED_FOLDERS = ['__pycache__', 'utils']
    # Gather all folders in our running directory and get their parsers
    return [
        f.path.replace('./', '') for f in os.scandir('.')
        if f.is_dir() and f.path.replace('./', '') not in EXCLUDED_FOLDERS
    ]


# The get_tokens function dynamically finds tokens by leveraging globs. This
# works based on the deterministic folder structure. Within a given OS root folder one can
# determine that a sub folder is in fact a token, if there is a "tests" directory. Upon removing
# the .py via [-2], there is now a list of files to import from.
def get_tokens(folder):
    return [
        path.split("/")[-2] for path in glob.glob(str(folder / '*' / 'tests'))
    ]


def get_files(folder, token=None):
    files = []
    for parse_file in glob.glob(str(folder / "*.py")):
        if parse_file.endswith("__init__.py"):
            continue
        if parse_file.startswith("_"):
            continue
        files.append({"parse_file": parse_file, "token": token})
    return files


#===========================================================================
#                            Final Output
#===========================================================================
# Build a testcase tree using anything that isn't passed
RESULT_ROW = "{name:<{max_len}s}{result:>24s}"
RESULT_COLOUR = {
    'passed': FgColour.BRIGHT_GREEN,
    'failed': FgColour.BRIGHT_RED,
    'errored': FgColour.BRIGHT_BLUE,
    'skipped': FgColour.BRIGHT_CYAN,
}


def failed_build_tree(section, parent_node, level=0):
    """
    Builds a tree for displaying items mimicking linux tree command.
    """
    # max_len is calculated to align all the result values on the
    # right regardless of indentation from TreeNode. (80 char width)
    max_len = 66 - level * 4
    # Determine if ran with harness or not
    if runtime.job:
        if section.type == 'Step':
            name = str_shortener('%s: %s' % (section.id, section.name),
                                 max_len)
        else:
            name = str_shortener(section.id, max_len)
        section_node = TreeNode(
            RESULT_ROW.format(
                name=name,
                # result = RESULT_COLOUR[str(section.result)].apply(str(section.result).upper()),
                result=str(section.result).upper(),
                max_len=max_len))
        result = section.result.value
        sections = section.sections
    else:
        section_node = TreeNode(
            RESULT_ROW.format(name=str_shortener(section['name'], max_len),
                              result=RESULT_COLOUR[str(
                                  section['result'])].apply(
                                      str(section['result']).upper()),
                              max_len=max_len))

        result = section['result'].value
        sections = section['sections']

    # Determine if we're only looking to display failures or not
    parsed_args = _parse_args()
    if (parsed_args['_display_only_failed'] and result not in ['passed']
            or not parsed_args['_display_only_failed']):
        parent_node.add_child(section_node)

    # Recursive indentation
    for child_section in sections:
        if level < 2:
            failed_build_tree(child_section, section_node, level + 1)
        else:
            failed_build_tree(child_section, parent_node, level)


# Handles output for standalone run
class FailedReporter(StandaloneReporter):
    def __init__(self):
        super().__init__()

    def log_summary(self):
        log.root.setLevel(0)
        if self.section_details:
            log.info(banner("Unittest results"))
            log.info(' %-70s%10s ' %
                     ('SECTIONS/TESTCASES', 'RESULT'.center(10)))
            log.info('-' * 80)

            report = TreeNode('.')
            for section in self.section_details:
                failed_build_tree(section, report)

            if str(report) == '.':
                log.info(' %-70s%10s ' %
                         ('ALL UNITTESTS', 'PASSED'.center(10)))
            else:
                log.info(str(report))

            log.info(banner("Summary"))
            for k in sorted(self.summary.keys()):

                log.info(' {name:<58}{num:>20} '.format(
                    name='Number of {}'.format(k.upper()),
                    num=self.summary[k]))
            log.info(' {name:<58}{num:>20} '.format(name='Total Number',
                                                    num=self.summary.total))
            log.info(' {name:<58}{num:>19.1f}% '.format(
                name='Success Rate', num=self.summary.success_rate))
            log.info('-' * 80)
            if glo_values.missingCount > 0:
                log.info(' {name:<58}{num:>20} '.format(
                    name='Total Parsers Missing Unittests',
                    num=glo_values.missingCount))
                log.info('-' * 80)

                if glo_values.missingParsers:
                    log.info("\n".join(glo_values.missingParsers),
                             extra={'colour': 'yellow'})
                    log.info('-' * 80)

            log.info(' {name:<58}{num:>20} '.format(
                name='Total Passing Unittests', num=glo_values.parserPassed))
            log.info(' {name:<58}{num:>20} '.format(
                name='Total Failed Unittests', num=glo_values.parserFailed))
            log.info(' {name:<58}{num:>20} '.format(
                name='Total Errored Unittests', num=glo_values.parserErrored))
            log.info(' {name:<58}{num:>20} '.format(
                name='Total Unittests', num=glo_values.parserTotal))
            log.info('-' * 80)

            if (hasattr(glo_values, '_class_exists')
                    and not glo_values._class_exists):
                parsed_args = _parse_args()
                log.info(f'`{parsed_args["_class"]}` does not exist',
                         extra={'colour': 'yellow'})
                log.info('-' * 80)

        else:
            log.info(banner('No Results To Show'))


# Handles output for pyats run job
def generate_email_reports():

    # Retrieve testsuite from ReportServer
    testsuite = runtime.details()

    summary_entries = []
    detail_trees = []

    # Parse run details from ReportServer into nice human-readable formats
    for task in testsuite.tasks:
        # New task tree
        task_tree = TreeNode('%s: %s' % (task.id, task.name))
        for section in task.sections:
            # Add to summary
            summary_entries.append(
                TEST_RESULT_ROW.format(name=str_shortener(
                    '%s: %s.%s' % (task.id, task.name, section.id), 70),
                                       result=str(section.result).upper(),
                                       max_len=70))

            # Build task report tree
            failed_build_tree(section, task_tree)
        # Add task tree to details tree list
        detail_trees.append(task_tree)

    # Format details for email
    task_summary = '\n'.join(summary_entries) or\
                    'Empty - did something go wrong?'
    task_details = '\n'.join(map(str, detail_trees)) or\
                    'Empty - did something go wrong?'

    if str(task_details) == 'Task-1: unittests':
        task_details = ' %-70s%10s ' % ('ALL UNITTESTS', 'PASSED'.center(10))

    # Add details to email contents
    if runtime.mail_report:
        runtime.mail_report.contents['Task Result Summary'] = task_summary
        runtime.mail_report.contents['Task Result Details'] = task_details
        # ? I've yet to find a way to make this work. Problem is this function gets called independent of the file
        # runtime.mail_report.contents['Total Parsers Missing Unittests'] = f"{glo_values.missingCount}\n{'-'*80}"
        # runtime.mail_report.contents['Total Parsers Missing Unittests'] = f"{glo_values._class_exists}\n{'-'*80}"


#===========================================================================
#                            Testcase Generators
#===========================================================================
class OSGenerator(object):
    def __init__(self, loopee, operating_system):
        self.operating_system = operating_system

    def __iter__(self):
        """Sets the uid of each os step to its name"""
        for os_data in self.operating_system:
            yield Iteration(uid=os_data[0],
                            parameters={"operating_system": os_data})


class ParserGenerator(object):
    def __init__(self, loopee, data):
        self.data = data

    def __iter__(self):
        """Sets the uid of each parser step to its class name. Adds token if it exists"""
        for d in self.data:
            if not re.match(f'{d["operating_system"]}_\S+',
                            d['local_class'].__module__):
                continue
            if d['token']:
                yield Iteration(
                    uid=f"{d['local_class'].__name__} -> {d['token']}",
                    parameters={"data": d})
            else:
                yield Iteration(uid=d['local_class'].__name__,
                                parameters={"data": d})


#===========================================================================
#                            OS Testcase
#===========================================================================
class SuperFileBasedTesting(aetest.Testcase):
    """Standard pyats testcase class."""
    def __init__(self, *args, **kwargs):
        # init parent
        super().__init__(*args, **kwargs)
        glo_values.missingCount = 0
        glo_values.parserPassed = 0
        glo_values.parserFailed = 0
        glo_values.parserErrored = 0
        glo_values.parserTotal = 0
        glo_values.missingParsers = []

    @aetest.setup
    def setup(self, _os, _class, _token, _display_only_failed, _number,
              _external_folder, _show_missing_unittests):

        # If _class is passed then check to see if it even exists
        if _class:
            glo_values._class_exists = False

        operating_systems = get_operating_systems(_os)

        self.parsers = {}

        for operating_system in operating_systems:

            self.parsers_list = self.parsers.setdefault(
                operating_system, list())

            if _external_folder:
                base_folder = _external_folder / operating_system
            else:
                base_folder = pathlib.Path(
                    f"{pathlib.Path(_parser.__file__).parent}/{operating_system}"
                )

            # Please refer to get_tokens comments for the how, the what is a genie token, such as
            # "asr1k" or "c3850" to provide namespaced parsing.
            tokens = get_tokens(base_folder)
            parse_files = list(get_files(base_folder))
            for token in tokens:
                parse_files.extend(get_files(base_folder / token, token))
            # Get all of the root level files
            for details in parse_files:
                parse_file = details["parse_file"]
                token = details["token"]
                # Load all of the classes in each of those files, and search for classes
                # that have a `cli` method
                _module = None
                module_name = os.path.basename(parse_file[:-len(".py")])
                if token:
                    module_name = f"{operating_system}_{token}_{module_name}"
                else:
                    module_name = f"{operating_system}_{module_name}"
                _module = importlib.machinery.SourceFileLoader(
                    module_name, parse_file).load_module()
                for name, local_class in inspect.getmembers(_module):
                    if token:
                        folder_root_equal = pathlib.Path(
                            f"{operating_system}/{token}/{name}/cli/equal")
                        folder_root_empty = pathlib.Path(
                            f"{operating_system}/{token}/{name}/cli/empty")
                    else:
                        folder_root_equal = pathlib.Path(
                            f"{operating_system}/{name}/cli/equal")
                        folder_root_empty = pathlib.Path(
                            f"{operating_system}/{name}/cli/empty")

                    # This is used in conjunction with the arguments that are run at command line, to skip over all tests you are
                    # not concerned with. Basically, it allows a user to not have to wait for 100s of tests to run, to run their
                    # one test.
                    if _token and _token != token:
                        continue
                    # Same as previous, however, for class
                    if _class and _class != name:
                        continue
                    if _class:
                        glo_values._class_exists = True
                    # Each "globals()" is checked to see if it has a cli attribute, if so, assumed to be a parser. The _osxe, is
                    # since the ios module often refers to the iosxe parser, leveraging this naming convention.
                    if hasattr(local_class,
                               "cli") and not name.endswith("_iosxe"):

                        if not folder_root_equal.exists():
                            if _show_missing_unittests or _class:
                                if token:
                                    log.warning(
                                        f'Equal unittests for {operating_system}-> {token} -> {name} don\'t exist'
                                    )
                                    glo_values.missingParsers.append(
                                        f" {operating_system} -> {token} -> {name}"
                                    )
                                else:
                                    log.warning(
                                        f'Equal unittests for {operating_system} -> {name} don\'t exist'
                                    )
                                    glo_values.missingParsers.append(
                                        f" {operating_system} -> {name}")
                            glo_values.missingCount += 1
                            continue

                        # skips over classes that do not contain the local variable cli_command
                        # this works to ignore outdated classes that use tcl
                        if not hasattr(local_class, 'cli_command') and not hasattr(local_class, 'parser_command'):
                            if _show_missing_unittests:
                                log.warning(
                                    f"{operating_system} {local_class.__name__} has no cli_command or parser_command defined."
                                )
                            continue

                        self.parsers_list.append({
                            "local_class":
                            local_class,
                            "operating_system":
                            operating_system,
                            "display_only_failed":
                            _display_only_failed,
                            "token":
                            token,
                            "number":
                            _number,
                            "show_missing_unittests":
                            _show_missing_unittests,
                        })

        aetest.loop.mark(ParserTest,
                         operating_system=self.parsers.items(),
                         generator=OSGenerator)


#===========================================================================
#                            Parser Testcase
#===========================================================================
class ParserTest(aetest.Testcase):
    # removes screenhandler from root, but tasklog handler
    # is kept to allow all logs to be visible in the report
    def remove_logger(self):
        if log.root.handlers:
            self.temporary_screen_handler = log.root.handlers.pop(0)

    # adds screenhandler back to root
    def add_logger(self):
        if self.temporary_screen_handler:
            log.root.handlers.insert(0, self.temporary_screen_handler)

    # Decorator function. Calls remove_logger if _display_only_failed flag if used
    # and screenhandler is in log.root.handlers
    def screen_log_handling(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            if self.parameters[
                    '_display_only_failed'] and self.temporary_screen_handler in log.root.handlers:
                self.remove_logger()

        return wrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.temporary_screen_handler = None
        if self.parameters['_display_only_failed']:
            self.remove_logger()

    @aetest.setup
    def setup(self, operating_system):
        self.uid = operating_system[0]
        self.data = operating_system[1]

        aetest.loop.mark(self.test, data=self.data, generator=ParserGenerator)

    @aetest.test
    def test(self, data, steps):
        local_class = data['local_class']
        operating_system = data['operating_system']
        _display_only_failed = data['display_only_failed']
        token = data['token']
        _number = data['number']
        name = local_class.__name__
        if token:
            msg = f"{operating_system} -> Token -> {token} -> {name}"
        else:
            msg = f"{operating_system} -> {name}"
        with steps.start(msg, continue_=True) as class_step:
            if name not in EXCLUDE_CLASSES.get(operating_system, []):
                with class_step.start(
                        f"Test Golden -> {operating_system} -> {name}",
                        continue_=True,
                ) as golden_steps:
                    self.test_golden(golden_steps, local_class,
                                     operating_system, _display_only_failed,
                                     token, _number)

                with class_step.start(
                        f"Test Empty -> {operating_system} -> {name}",
                        continue_=True,
                ) as empty_steps:
                    self.test_empty(empty_steps, local_class, operating_system,
                                    token)
            else:
                class_step.skipped(
                    f"Parser class {name} is in EXCLUDE_CLASSES.")

    @screen_log_handling
    def test_golden(self,
                    steps,
                    local_class,
                    operating_system,
                    display_only_failed=None,
                    token=None,
                    number=None):
        """Test step that finds any output named with _output.txt, and compares to similar named .py file."""
        if token:
            folder_root = pathlib.Path(
                f"{operating_system}/{token}/{local_class.__name__}/cli/equal")
        else:
            folder_root = pathlib.Path(
                f"{operating_system}/{local_class.__name__}/cli/equal")

        # Get list of output files to parse and sort
        convert = lambda text: int(text) if text.isdigit() else text
        aph_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
        if number and not operating_system or not local_class:
            output_glob = sorted(
                glob.glob(f"{folder_root}/golden_output{number}_output.txt"),
                key=aph_key,
            )
        else:
            output_glob = sorted(glob.glob(f"{folder_root}/*_output.txt"),
                                 key=aph_key)

        all_txt_glob = sorted(glob.glob(f"{folder_root}/*.txt"), key=aph_key)

        unacceptable_filenames = [
            fil for fil in all_txt_glob if fil not in output_glob
        ]

        if len(output_glob) == 0:
            steps.failed(
                f"No files found in appropriate directory for {local_class}")

        # Look for any files ending with _output.txt, presume the user defined name from that (based
        # on truncating that _output.txt suffix) and obtaining expected results and potentially an arguments file

        for user_defined in output_glob:
            glo_values.parserTotal += 1
            user_test = os.path.basename(user_defined[:-len("_output.txt")])
            if token:
                msg = f"Gold -> {operating_system} -> Token {token} -> {local_class.__name__} -> {user_test}"
            else:
                msg = f"Gold -> {operating_system} -> {local_class.__name__} -> {user_test}"

            with steps.start(msg, continue_=True):
                golden_output_str = read_from_file(
                    f"{folder_root}/{user_test}_output.txt")
                golden_output = {
                    "execute.return_value": golden_output_str,
                    "expect.return_value": golden_output_str,
                }

                golden_parsed_output = read_python_file(
                    f"{folder_root}/{user_test}_expected.py")
                arguments = {}
                if os.path.exists(f"{folder_root}/{user_test}_arguments.json"):
                    arguments = read_json_file(
                        f"{folder_root}/{user_test}_arguments.json")

                device = Mock(**golden_output)
                obj = local_class(device=device)
                try:
                    parsed_output = obj.parse(**arguments)
                except Exception as e:
                    parsed_output = {}
                    self.add_logger()
                    log.error(traceback.format_exc(), extra={'colour': 'red'})
                    self.remove_logger()
                    glo_values.parserErrored += 1

                # Use Diff method to get the difference between
                # what is expected and the parsed output
                dd = Diff(golden_parsed_output, parsed_output)
                dd.findDiff()
                if parsed_output != golden_parsed_output:
                    glo_values.parserFailed += 1

                    # if -f flag provided, then add the screen handler back into
                    # the root.handlers to displayed failed tests. Decorator removes
                    # screen handler from root.handlers after failed tests are displayed
                    # to stdout
                    if display_only_failed:
                        self.add_logger()
                        log.info(banner(msg), extra={'colour': 'red'})

                    # Format expected and parsed output in a nice format
                    parsed_json_data = format_output(parsed_output)
                    golden_parsed_output_json_data = format_output(
                        golden_parsed_output)

                    # Display device output, parsed output, and golden_output of failed tests
                    log.info(banner("The following is the actual raw output"))
                    log.info(f"{golden_output['execute.return_value']}\n\n", extra={'colour': 'yellow'})

                    log.info(banner("The following is the expected parsed output"))
                    log.info(f"{golden_parsed_output_json_data}\n\n", extra={'colour': 'yellow'})

                    log.info(banner("The following is the actual parsed output"))
                    log.info(f"{parsed_json_data}\n\n", extra={'colour': 'yellow'})

                    log.info(banner("The following is the diff between expected and actual outputs"))
                    log.info(str(dd)+"\n\n", extra={'colour': 'yellow'})

                    if display_only_failed:
                        self.remove_logger()

                    raise AssertionError("Device output and expected output do not match")
                else:
                    glo_values.parserPassed += 1
                    # If tests pass, display the device output in debug mode
                    # But first check if the screen handler is removed, if it is
                    # put it back into the root otherwise just display to stdout
                    if (self.temporary_screen_handler in log.root.handlers
                            or self.temporary_screen_handler is None):
                        logging.debug(banner(msg))
                        logging.debug(
                            "\nThe following is the device output for the passed parser:\n{}\n"
                            .format(golden_output['execute.return_value']),
                            extra={'colour': 'yellow'})

                    else:
                        self.add_logger()
                        logging.debug(banner(msg))
                        logging.debug(
                            "\nThe following is the device output for the passed parser:\n{}\n"
                            .format(golden_output['execute.return_value']),
                            extra={'colour': 'yellow'})
                        self.remove_logger()
        if unacceptable_filenames:
            for unacc_fil in unacceptable_filenames:
                unacc_fil_name = pathlib.Path(unacc_fil).name
                msg = f"{unacc_fil_name} does not follow the filename schema and will not be ran..."
                with steps.start(msg, continue_=True) as step:
                    if (self.temporary_screen_handler in log.root.handlers
                            or self.temporary_screen_handler is None):
                        log.info(
                            f"Filename should be `{unacc_fil_name.split('.')[0]}_expected.txt`",
                            extra={'colour': 'yellow'})
                    else:
                        self.add_logger()
                        log.info(msg, extra={'colour': 'yellow'})
                        log.info(
                            f"Filename should be `{unacc_fil_name.split('.')[0]}_expected.txt`",
                            extra={'colour': 'yellow'})
                        self.remove_logger()
                    step.failed()

    @screen_log_handling
    def test_empty(self,
                   steps,
                   local_class,
                   operating_system,
                   token=None,
                   display_only_failed=None):
        """Test step that looks for empty output."""
        if token:
            folder_root = pathlib.Path(
                f"{operating_system}/{token}/{local_class.__name__}/cli/empty")
        else:
            folder_root = pathlib.Path(
                f"{operating_system}/{local_class.__name__}/cli/empty")
        output_glob = glob.glob(f"{folder_root}/*_output.txt")

        all_txt_glob = sorted(glob.glob(f"{folder_root}/*.txt"))

        unacceptable_filenames = [
            fil for fil in all_txt_glob if fil not in output_glob
        ]

        for user_defined in output_glob:
            glo_values.parserTotal += 1
            user_test = os.path.basename(user_defined[:-len("_output.txt")])
            if token:
                msg = f"Empty -> {operating_system} -> {token} -> {local_class.__name__} -> {user_test}"
            else:
                msg = f"Empty -> {operating_system} -> {local_class.__name__} -> {user_test}"
            with steps.start(msg, continue_=True) as step_within:

                try:
                    empty_output_str = read_from_file(
                        f"{folder_root}/{user_test}_output.txt")
                except Exception:
                    empty_output_str = ""
                empty_output = {
                    "execute.return_value": empty_output_str,
                    "expect.return_value": empty_output_str,
                }
                arguments = {}
                if os.path.exists(f"{folder_root}/{user_test}_arguments.json"):
                    arguments = read_json_file(
                        f"{folder_root}/{user_test}_arguments.json")
                device = Mock(**empty_output)
                obj = local_class(device=device)
                try:
                    obj.parse(**arguments)
                    # if -f flag provided, then add the screen handler back into
                    # the root.handlers to display failed tests. Decorator removes
                    # screen handler from root.handlers after failed tests are displayed
                    # to stdout
                    if display_only_failed:
                        self.add_logger()
                    glo_values.parserFailed += 1
                    step_within.failed(
                        f"File parsed, when expected not to for {local_class}")
                except SchemaEmptyParserError:
                    glo_values.parserPassed += 1
                    return True
                except AttributeError:
                    glo_values.parserPassed += 1
                    return True
                except Exception:
                    glo_values.parserErrored += 1
                    raise

        if unacceptable_filenames:
            for unacc_fil in unacceptable_filenames:
                unacc_fil_name = pathlib.Path(unacc_fil).name
                msg = f"{unacc_fil_name} does not follow the filename schema and will not be ran..."
                with steps.start(msg, continue_=True) as step:
                    if self.temporary_screen_handler not in log.root.handlers and self.temporary_screen_handler != None:
                        self.add_logger()
                        log.info(msg, extra={'colour': 'yellow'})
                        log.info(
                            f"Filename should be `{unacc_fil_name.split('.')[0]}_expected.txt`",
                            extra={'colour': 'yellow'})
                        self.remove_logger()
                    else:
                        log.info(
                            f"Filename should be `{unacc_fil_name.split('.')[0]}_expected.txt`",
                            extra={'colour': 'yellow'})
                    step.failed()

    @aetest.cleanup
    def cleanup(self, _display_only_failed=None, _show_missing_unittests=None):
        if _display_only_failed:
            self.add_logger()
        if _show_missing_unittests and glo_values.missingCount > 0:
            self.failed('Unittests are missing')


#===========================================================================
#                            Main Section
#===========================================================================


# Function for parsing cli arguments
def _parse_args(operating_system=None,
                class_name=None,
                token=None,
                display_only_failed=None,
                number=None,
                external_folder=None,
                show_missing_unittests=None,
                o=None,
                c=None,
                t=None,
                f=None,
                n=None,
                e=None,
                **kwargs):

    # Create the parser
    my_parser = argparse.ArgumentParser(
        description="Optional arguments for 'nose'-like tests")

    my_parser.add_argument('-o',
                           "--operating_system",
                           type=str,
                           help='The OS you wish to filter on',
                           default=None or operating_system or o)
    my_parser.add_argument(
        '-c',
        "--class_name",
        type=str,
        help="The Class you wish to filter on, (not the Test File)",
        default=None or class_name or c)
    my_parser.add_argument(
        '-t',
        "--token",
        type=str,
        help="The Token associated with the class, such as 'asr1k'",
        default=None or token or t)
    my_parser.add_argument('-f',
                           "--display_only_failed",
                           help="Displaying only failed classes",
                           action='store_true',
                           default=False or display_only_failed or f)
    my_parser.add_argument(
        '-n',
        "--number",
        type=int,
        help="The specific unittest we want to run, such as '25'",
        default=None or number or n)
    my_parser.add_argument('-e',
                           "--external-folder",
                           type=pathlib.Path,
                           help="An external parser folder to work with",
                           default=None or external_folder or e)
    my_parser.add_argument("--show-missing-unittests",
                           action='store_true',
                           help="Print out parsers that are missing unittests",
                           default=None or show_missing_unittests)
    args = my_parser.parse_known_args()[0]

    _os = args.operating_system
    _class = args.class_name
    _token = args.token
    _display_only_failed = args.display_only_failed
    _number = args.number
    _external_folder = args.external_folder
    _show_missing_unittests = args.show_missing_unittests

    return {
        "_os": _os,
        "_class": _class,
        "_token": _token,
        "_display_only_failed": _display_only_failed,
        "_number": _number,
        "_external_folder": _external_folder,
        "_show_missing_unittests": _show_missing_unittests,
    }


def main(**kwargs):

    parsed_args = _parse_args(**kwargs)

    if parsed_args['_number'] and not parsed_args['_class']:
        sys.exit("Unittest number provided but missing supporting arguments:"
                 "\n* '-c' or '--class_name' for the parser class"
                 "\n* '-o' or '--operating_system' for operating system")

    if runtime.job:
        # Used for `pyats run job folder_parsing_job.py`
        runtime.generate_email_reports = generate_email_reports
        run(testscript=__file__, runtime=runtime, **parsed_args)
    else:
        # Used for `python folder_parsing_job.py`
        result = aetest.main(testable=__file__,
                             runtime=runtime,
                             reporter=FailedReporter(),
                             **parsed_args)
        aetest.exit_cli_code(result)


if __name__ == "__main__":
    main()
