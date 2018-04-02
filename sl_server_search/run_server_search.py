import sys

from server_list import ServerList

csv_file = sys.argv[1]
server_list = ServerList(csv_file)

unit_size = input("Select 1U, 2U, or 4U server (integer only):")
server_list.filter('Unit Size', unit_size)
proc = input("What processor?:")
server_list.filter('Proc', proc)

print('Here are the available Drive Controllers:')
drive_controllers = server_list.get_available_options('Drive Controller')
