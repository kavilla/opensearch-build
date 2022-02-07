# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import os

from test_workflow.bwc_test.bwc_test_suite import BwcTestSuite


class BwcTestSuiteOpenSearchDashboards(BwcTestSuite):

    def __init__(
        self, 
        work_dir,
        component,
        test_config,
        test_recorder,
        manifest
    ):

        super().__init__(
            self, 
            work_dir,
            component,
            test_config,
            test_recorder,
            manifest
        )

    @property
    def test_artifact_files(self):
        return {
            "cypress-videos": os.path.join(self.repo_work_dir, "cypress", "videos"),
            "cypress-screenshots": os.path.join(self.repo_work_dir, "cypress", "screenshots"),
            "cypress-report": os.path.join(self.repo_work_dir, "cypress", "results"),
        }
