def print_help():
    help_command = dict()
    help_command['help'] = 'Show this help'
    help_command['quit'] = 'Quit the program'
    help_command['add'] = 'Crete a new contact'
    help_command['list'] = 'Show list of all contacts'
    help_command['delete'] = 'Delete single contact'
    help_command['edit'] = 'Edit existing contact'

    for command in help_command:
        print(command, '\t-\t', help_command[command])


def add_contact():
    name = input('Enter a name: ')
    phonenumber = input('Enter a phone number: ')
    phonebook[name] = phonenumber
    print(name, 'was successfully added to the phone book.')
    print_list()

def print_list():
    for name in phonebook:
        print(name, '\t-\t', phonebook[name])


def delete_contact():
    print_list()
    name_or_number = input('Enter phone number or full name: ')
    name = find_name(name_or_number)

    try:
        phonebook[name]
    except:
        return print(name_or_number, 'is not found!')

    del phonebook[name]
    print(name_or_number, 'was successfully removed from the phone book.')
    print_list()


def edit_contact():
    print_list()
    name_or_number = input('Enter phone number or full name: ')
    name = find_name(name_or_number)

    try:
        phonebook[name]
    except:
        return print(name, 'is not found!')

    new_name = input('Enter a new name: ')
    new_phonenumber = input('Enter a new phone number: ')

    phonebook[new_name] = phonebook.pop(name)
    phonebook[new_name] = new_phonenumber

    print(new_name, 'was successfully edited from the phone book.')
    print_list()


def find_name(name_or_number):
    name = ''
    if name_or_number.isdigit():
        for key in phonebook:
            if name_or_number == phonebook[key]:
                name = key
    else:
        name = name_or_number
    return name


# Create a list
phonebook = {}
phonebook['Alice'] = '12345'
phonebook['Bob'] = '56789'

# Enter a command
command = ''
while command != 'quit':
    command = input('Enter a command (h for help): ')
    if command == 'h' or command == 'help':
        print_help()
    elif command == 'add':
        add_contact()
    elif command == 'list':
        print_list()
    elif command == 'delete':
        delete_contact()
    elif command == 'edit':
        edit_contact()
    elif command == 'quit':
        print('The phone book is closed.')
    else:
        print('Invalid command!')
