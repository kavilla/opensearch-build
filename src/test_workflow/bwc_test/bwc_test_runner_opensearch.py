# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import logging
import os

from manifests.bundle_manifest import BundleManifest
from manifests.test_manifest import TestManifest
from test_workflow.bwc_test.bwc_test_runner import BwcTestRunner
from test_workflow.bwc_test.bwc_test_suite import BwcTestSuite
from test_workflow.test_args import TestArgs


class BwcTestRunnerOpenSearch(BwcTestRunner):

    def __init__(self, args: TestArgs, test_manifest: TestManifest):
        super().__init__(args, test_manifest)
        self.properties.bundle_manifest = BundleManifest.from_urlpath(args.paths.get("opensearch", os.getcwd()))  
        logging.info("Entering BWC test for OpenSearch")

    def __create_test_suite__(self, component, test_config, work_dir):
        return BwcTestSuite(
            self.properties.bundle_manifest, 
            work_dir.name,
            component
        )
