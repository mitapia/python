import csv

class SLFile:
    """File of list of servers in CSV format obtain from Softlayer Hardware Search."""

    def convert_csv_to_dict_list(csv_file):
        """Returns a list of dictionary items from the csv_file"""
        server_list = []
        with open(csv_file) as full_server_info:
            server_info_reader = csv.DictReader(full_server_info)
            for row in server_info_reader:
                # make sure only inventory servers are displayed
                if row['Hardware Status'] == 'INVENTORY' and row['Hardware Function'] == 'Web Server':
                    reduced_server_info = {
                        'HW ID': row['Hardware Id'],
                        'Location': row['Location'],
                        'SL Tag': row['SoftLayer Serial Number'],
                        'Manufacturer': row['Manufacturer'],
                        'Drive Capacity': row['Drive Capacity'],
                        'Unit Size': row['Unit Size'],
                        'Proc': row['Processor Model (Expand Row to view additional models)'],
                        'Drives': row['Hard Drive Model (Expand Row to view additional models)'],
                        'RAM': row['Ram Model (Expand Row to view additional models)'],
                        'Mobo': row['Motherboard Model'],
                        'Drive Controller': row['Drive Controller Model (Expand Row to view additional models)'],
                        'Days Old': row['Days old']
                    }
                    server_list.append(reduced_server_info)

        return server_list