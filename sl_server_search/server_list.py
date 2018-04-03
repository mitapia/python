from sl_file import SLFile

class ServerList:
    """List of servers available for provisioning

    Attributes:
        csv_file: csv file containing list of server to be searched
    """

    def __init__(self, csv_file):
        """Return a new ServerList object"""
        self.server_list = SLFile.convert_csv_to_dict_list(csv_file)

    def filter(self, column_name, list_of_values_to_filter):
        """Return the new filtered list"""
        new_server_list = []
        for item in self.server_list:
            if any(value in item[column_name] for value in list_of_values_to_filter):
                new_server_list.append(item)
        self.server_list = new_server_list
        return self.server_list

    def get_available_options(self, column_name):
        """Return the Set of available values of specified column from server_list"""
        available_options_set = set()
        for item in self.server_list:
            available_options_set.add(item[column_name])
        return available_options_set

    def available_count(self):
        """Return a count of all available servers in current server_list"""
        return len(self.server_list)

    def get_first(self):
        """Returns the first server on list."""
        return self.server_list[0]