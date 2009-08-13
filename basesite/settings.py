''' Custom project settings.'''

from basesite.default_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Aleksey', 'dixon.che@gmail.com'),
)

MANAGERS = ADMINS

TEST_RUNNER = 'basesite.test_runner.run_tests_with_coverage'
# TEST_RUNNER = "basesite.coverage_runner.run_tests"
# COVERAGE_REPORT_PATH = SITE_ROOT + 'coverage_report'
