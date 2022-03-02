################################################################################
#                                                                              #
#                      Cisco Systems Proprietary Software                      #
#        Not to be distributed without consent from Test Technology            #
#                               Cisco Systems, Inc.                            #
#                                                                              #
################################################################################
#                            genie.libs.parser Internal Makefile
#
# Author:
#   pyats-support@cisco.com
#
# Support:
#   pyats-support@cisco.com
#
# Version:
#   v21.8
#
# Date:
#   August 2021
#
# About This File:
#   This script will build the genie.libs.parser package for
#   distribution in PyPI server
#
# Requirements:
#	1. Module name is the same as package name.
#	2. setup.py file is stored within the module folder
################################################################################

# Variables
PKG_NAME      = genie.libs.parser
BUILD_DIR     = $(shell pwd)/__build__
DIST_DIR      = $(BUILD_DIR)/dist
PYTHON        = python3
TESTCMD       = runAll --path=$(shell pwd)/tests
TESTFLD       = pyats run job folder_parsing_job.py --no-mail
TESTDEVAT     = pyats run job folder_parsing_job.py -e ${BINOS_ROOT}/atests/cisco/pyats/libs/genie/external_parser --no-mail
BUILD_CMD     = $(PYTHON) setup.py bdist_wheel --dist-dir=$(DIST_DIR)
PYPIREPO      = pypitest
PYLINT_CMD	  = pylintAll
CYTHON_CMD	  = compileAll
INDEX_URL     = https://pyats-pypi.cisco.com/simple
TRUSTED_HOST  = pyats-pypi.cisco.com

# Development pkg requirements
RELATED_PKGS = genie.libs.parser
DEPENDENCIES = xmltodict requests

ifeq ($(MAKECMDGOALS), devnet)
	BUILD_CMD += --devnet
endif

.PHONY: clean package distribute develop undevelop help devnet\
        docs test install_build_deps uninstall_build_deps distribute_staging\
        distribute_staging_external

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "package                       Build the package"
	@echo "test                          Test the package"
	@echo "distribute                    Distribute the package to internal Cisco PyPi server"
	@echo "distribute_staging            Distribute build pkgs to staging area"
	@echo "distribute_staging_external   Distribute build pkgs to external staging area"
	@echo "clean                         Remove build artifacts"
	@echo "develop                       Build and install development package"
	@echo "undevelop                     Uninstall development package"
	@echo "docs                          Build Sphinx documentation for this package"
	@echo "devnet                        Build DevNet package."
	@echo "install_build_deps            install pyats-distutils"
	@echo "uninstall_build_deps          Remove pyats-distutils"
	@echo "compile		 		         Compile all python modules to c"
	@echo "coverage_all			         Run code coverage on all test files"
	@echo "pylint_all			         Run python linter on all python modules"
	@echo "json					         Build json files"
	@echo "changelogs			         Build compiled changelog file"
	@echo ""
	@echo "     --- build arguments ---"
	@echo " DEVNET=true              build for devnet style (cythonized, no ut)"

compile:
	@echo ""
	@echo "Compiling to C code"
	@echo --------------------------
	@pip install --index-url=$(INDEX_URL) --trusted-host $(TRUSTED_HOST) cisco-distutils --upgrade || true
	$(CYTHON_CMD)
	@echo "Done Compiling"
	@echo ""
	@echo "Done."
	@echo ""

coverage_all:
	@echo ""
	@echo "Running Code coverage on all unittests"
	@echo ---------------------------------------
	@$(TESTCMD) --path tests/ --coverage --no-refresh
	@echo ""
	@echo "Done."
	@echo ""

pylint_all:
	@echo ""
	@echo "Running Pylint on all modules"
	@echo "-----------------------------"
	@$(PYLINT_CMD)
	@echo "Done linting"
	@echo ""
	@echo "Done."
	@echo ""

devnet: package
	@echo "Completed building DevNet packages"
	@echo ""

install_build_deps:
	@pip install --upgrade pip setuptools wheel

uninstall_build_deps:
	@echo "Nothing to do"

docs:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "No documentation for $(PKG_NAME)"
	@echo ""

test:
	@pip install --index-url=$(INDEX_URL) --trusted-host $(TRUSTED_HOST) cisco-distutils --upgrade || true
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Unittests runs"
	@if [ -d "${BINOS_ROOT}/atests/cisco/pyats/libs/genie/external_parser" ]; then \
		$(TESTCMD) && cd tests && $(TESTFLD) && cd ${BINOS_ROOT}/atests/cisco/pyats/libs/genie/external_parser/tests && $(TESTDEVAT); \
	else \
		$(TESTCMD) && cd tests && $(TESTFLD); \
	fi


package:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building $(PKG_NAME) distributable: $@"
	@echo ""

	$(BUILD_CMD)

	@echo ""
	@echo "Completed building: $@"
	@echo ""
	@echo "Done."
	@echo ""

develop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building and installing $(PKG_NAME) development distributable: $@"
	@echo ""

	@pip uninstall -y $(RELATED_PKGS) || true
	@pip install $(DEPENDENCIES)

	@$(PYTHON) setup.py develop --no-deps

	@echo ""
	@echo "Completed building and installing: $@"
	@echo ""
	@echo "Done."
	@echo ""

undevelop:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Uninstalling $(PKG_NAME) development distributable: $@"
	@echo ""

	@$(PYTHON) setup.py develop --no-deps -q --uninstall

	@echo ""
	@echo "Completed uninstalling: $@"
	@echo ""
	@echo "Done."
	@echo ""

clean:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Removing make directory: $(BUILD_DIR)"
	@rm -rf $(BUILD_DIR) $(DIST_DIR)
	@echo ""
	@echo "Removing build artifacts ..."
	@$(PYTHON) setup.py clean
	@echo ""
	@echo "Done."
	@echo ""

distribute:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Copying all distributable to $(PROD_PKGS)"
	@test -d $(DIST_DIR) || { echo "Nothing to distribute! Exiting..."; exit 1; }
	@ssh -q $(PROD_USER) 'test -e $(PROD_PKGS)/$(PKG_NAME) || mkdir $(PROD_PKGS)/$(PKG_NAME)'
	@scp $(DIST_DIR)/* $(PROD_USER):$(PROD_PKGS)/$(PKG_NAME)/
	@echo ""
	@echo "Done."
	@echo ""

distribute_staging:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Copying all distributable to $(STAGING_PKGS)"
	@test -d $(DIST_DIR) || { echo "Nothing to distribute! Exiting..."; exit 1; }
	@ssh -q $(PROD_USER) 'test -e $(STAGING_PKGS)/$(PKG_NAME) || mkdir $(STAGING_PKGS)/$(PKG_NAME)'
	@scp $(DIST_DIR)/* $(PROD_USER):$(STAGING_PKGS)/$(PKG_NAME)/
	@echo ""
	@echo "Done."
	@echo ""

distribute_staging_external:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Copying all distributable to $(STAGING_EXT_PKGS)"
	@test -d $(DIST_DIR) || { echo "Nothing to distribute! Exiting..."; exit 1; }
	@ssh -q $(PROD_USER) 'test -e $(STAGING_EXT_PKGS)/$(PKG_NAME) || mkdir $(STAGING_EXT_PKGS)/$(PKG_NAME)'
	@scp $(DIST_DIR)/* $(PROD_USER):$(STAGING_EXT_PKGS)/$(PKG_NAME)/
	@echo ""
	@echo "Done."
	@echo ""

json:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Generating Parser json file"
	@echo ""
	@$(PYTHON) -c "from genie.json.make_json import make_genieparser; make_genieparser()"
	@echo ""
	@echo "Done."
	@echo ""

changelogs:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Generating changelog file"
	@echo ""
	@$(PYTHON) -c "from ciscodistutils.make_changelog import main; main('./changelog/undistributed', './changelog/undistributed.rst')"
	@echo ""
	@echo "Done."
	@echo ""
