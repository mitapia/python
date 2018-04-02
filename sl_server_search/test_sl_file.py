import unittest

from sl_file import SLFile

sample_server_list = [
    {'HW ID': '1',
     'Location': 'dal07.sr01.rk86.sl16',
     'SL Tag': 'SL65498',
     'Manufacturer': 'SuperMicro',
     'Drive Capacity': '12',
     'Unit Size': '2',
     'Proc': '2650',
     'Drives': 'ST36',
     'RAM': '16GB',
     'Mobo': 'X10DRU',
     'Drive Controller': 'LSI',
     'Days Old': ''},

    {'HW ID': '2',
     'Location': 'dal07.sr01.rk01.sl38',
     'SL Tag': 'SL987654',
     'Manufacturer': 'SuperMicro',
     'Drive Capacity': '4',
     'Unit Size': '1',
     'Proc': '2620',
     'Drives': 'ST10',
     'RAM': '4GB',
     'Mobo': 'X9DRI',
     'Drive Controller': 'Onboard',
     'Days Old': ''},

    {'HW ID': '3',
     'Location': 'dal07.sr01.rk74.sl26',
     'SL Tag': 'SL98745',
     'Manufacturer': 'SuperMicro',
     'Drive Capacity': '4',
     'Unit Size': '1',
     'Proc': '2650',
     'Drives': 'ST10',
     'RAM': '8GB',
     'Mobo': 'X10DRU',
     'Drive Controller': 'Onboard',
     'Days Old': ''},
]

class TestSLFile(unittest.TestCase):
    """Test for 'sl_file.py'."""

    def test_convert_csv_to_dict_list(self):
        """Can it make the appropriate list out of the csv_file?"""
        returned_list = SLFile.convert_csv_to_dict_list('hardwareSearchResults_tinyEdited.csv')
        for i in range(0,3):
            self.assertDictEqual(returned_list[i], sample_server_list[i])

if __name__ == '__main__':
    unittest.main()