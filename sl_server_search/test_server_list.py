import unittest

from server_list import ServerList
from test_sl_file import sample_server_list

class TestServerList(unittest.TestCase):
    """Test for 'server_list.py'."""

    def test_filter(self):
        """Can it return the correct server(s)?"""
        full_list = ServerList('hardwareSearchResults_tinyEdited.csv')
        filtered_result1 = full_list.filter('HW ID', '2')
        self.assertDictEqual(filtered_result1[0], sample_server_list[1])

        fresh_full_list = ServerList('hardwareSearchResults_tinyEdited.csv')
        filtered_result2 = fresh_full_list.filter('Unit Size', '1')
        self.assertDictEqual(filtered_result2[0], sample_server_list[1])
        self.assertDictEqual(filtered_result2[1], sample_server_list[2])

    def test_stacking_filter(self):
        """Can we get a list with multiple filter applied?"""
        server_list = ServerList('hardwareSearchResults_tinyEdited.csv')
        first_filter = server_list.filter('Mobo', 'X10DRU')
        self.assertEqual(len(first_filter), 2)

        second_filter = server_list.filter('Drive Controller', 'Onboard')
        self.assertDictEqual(second_filter[0], sample_server_list[2])

    def test_get_available_options(self):
        """Can we retrieve a list of the available options for a given column"""
        server_list = ServerList('hardwareSearchResults_tinyEdited.csv')
        returned_set = server_list.get_available_options('Drives')
        expected_set = {'ST10', 'ST36'}
        self.assertSetEqual(returned_set, expected_set)

if __name__ == '__main__':
    unittest.main()