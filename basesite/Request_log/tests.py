'''Django test for Request_log module'''

from django.test import TestCase


class SimpleTest(TestCase):
    '''base class for test '''

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)
