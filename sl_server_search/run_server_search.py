import sys, webbrowser

from server_list import ServerList

def exit_if_zero_available():
    if server_list.available_count() == 0:
        print('No servers with these specification where found. Exiting.')
        exit()

def select_component_options(column_name):
    options = list(server_list.get_available_options(column_name))
    if len(options) == 1 :
        print("This is the only " + column_name + " component found:\n" + options[0] + "\n")
    else:
        print("The following components where found:\n")
        for index, component in enumerate(options):
            print('[' + str(index) + ']  ' + component)
        selected_index_string = input("\nSelect at least one component. \n"
                                      "Only enter integer, use comma to separate multiple options:")
        selected_index_list = selected_index_string.split(',')  # convert string into list for use in filter

        selected_options_list = []
        for index in selected_index_list:
            selected_options_list.append(options[int(index)])

        server_list.filter(column_name, selected_options_list)


csv_file = sys.argv[1]
server_list = ServerList(csv_file)

unit_size = [input("Select 1U, 2U, or 4U server (integer only):")]
server_list.filter('Unit Size', unit_size)
exit_if_zero_available()

proc = [input("What processor?:")]
server_list.filter('Proc', proc)
exit_if_zero_available()
select_component_options('Proc')
select_component_options('Drive Controller')
select_component_options('RAM')
select_component_options('Drives')

selected_server = server_list.get_first()
print('Server Found:')
print('{0:10} {1}'.format('HW ID', selected_server['HW ID']))
hwo = 'https://internal.softlayer.com/Hardware/update/' + selected_server['HW ID']
webbrowser.open(hwo)
