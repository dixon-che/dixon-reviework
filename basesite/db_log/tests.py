'''Django test for db_log module'''

from django.test import TestCase


class SimpleTest(TestCase):
    '''base class for test '''

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)
