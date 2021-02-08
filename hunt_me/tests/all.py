"""hunt_me Tests

This module contains various tests.
"""
from tests.base import SherlockBaseTest
import unittest


class hunt_meDetectTests(hunt_meBaseTest):
    def test_detect_true_via_message(self):
        """Test Username Does Exist (Via Message).

        This test ensures that the "message" detection mechanism of
        ensuring that a Username does exist works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        N/A.
        Will trigger an assert if detection mechanism did not work as expected.
        """

        site = 'BinarySearch'
        site_data = self.site_data_all[site]

        #Ensure that the site's detection method has not changed.
        self.assertEqual("message", site_data["errorType"])

        self.username_check([site_data["username_claimed"]],
                            [site],
                            exist_check=True
                           )

        return

    def test_detect_false_via_message(self):
        """Test Username Does Not Exist (Via Message).

        This test ensures that the "message" detection mechanism of
        ensuring that a Username does *not* exist works properly.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
