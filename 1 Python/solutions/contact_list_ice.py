# contact_list_ice.py
contact_list = []   # global contact_list variable
keys = []           # global contact_list keys variable

def read_csv_to_dict(file_path):
    """ setting global contact_list with csv as list of dictionaries
    """
    global contact_list, keys
    with open(file_path) as f:
        rows = f.read().split('\n')

    list_of_dicts = []
    keys = rows[0].split(',')

    for row in rows:
        if rows.index(row) == 0: # skip first row
            continue
        # if row == keys: # another way to do this
        row = row.split(',')
        row_dict = dict(zip(keys, row))
        list_of_dicts.append(row_dict)

    contact_list = list_of_dicts


def save_dict_to_csv(source, destination_path):
    """ writes source list of dictionaries to csv at destination_path
    """
    pass


def find_contact_index(name):
    """ name: string
    returns index of contact given name
    """
    global contact_list
    index = None
    for i in range(len(contact_list)):
        contact = contact_list[i]
        if name == contact['name']:
            index = i
            break
    return index


def create_contact(contact):
    """ contact: dict 
    adds contact to contact_list
    """
    global contact_list
    contact_list.append(contact)
    return contact


def retrieve_contact(name):
    """ name: string
    finds contact given name from contact_list
    returns contact data
    """
    global contact_list
    index = find_contact_index(name)
    if index is not None:
        return contact_list[index]
    return 'Contact does not exist.'


def update_contact(name, updated_data):
    """ name: string
    updated_data: dict
    updates contact with updated_data
    """
    global contact_list
    # 1. find the contact with the name
    index = find_contact_index(name)
    if index is not None:
    # 2. update that contact dict with updated_data
        contact = contact_list[index]
        contact.update(updated_data)
        return contact
    return 'Contact does not exist.'


def delete_contact(name):
    """ name: string
    deletes contact given name
    """
    global contact_list 
    index = find_contact_index(name)
    if index is not None:   
        contact = contact_list.pop(index)
        return f"Removed {contact['name']}"
    return 'Contact does not exist.'


def print_contact_list():
    """ prints all contacts
    """
    global contact_list
    for contact in contact_list:
        print(contact)


def repl():
    """ REPL user interface for contact list
    """
    global contact_list, keys
    valid_inputs = ['a', 'all', 'c', 'create', 'r', 'read', 'u', 'update', 'd', 'delete', 'x', 'exit', 'q', 'quit']
    while True:
        print("Welcome to your contact list. ")

        while True:
            user_in = input("Enter (c)reate, (r)ead, (u)pdate, or (d)elete to update your contact list, (a)ll to print all contacts, or e(x)it to quit: ").lower().strip()
            if user_in in valid_inputs:
                break

        if user_in.startswith('r') or user_in.startswith('u') or user_in.startswith('d'):
            name = input("Enter the contact's name: ")

        if user_in.startswith('c'):
            contact = {}
            for key in keys:
                val = input(f"{key}: ")
                contact[key] = val
            print(create_contact(contact))

        elif user_in.startswith('r'):
            contact = retrieve_contact(name)
            print(contact)

        elif user_in.startswith('u'):
            pass

        elif user_in.startswith('d'):
            contact = delete_contact(name)
            print(contact)

        elif user_in.startswith('a'):
            print_contact_list()

        elif user_in in ['x', 'exit', 'q', 'quit']:
            break


def main():
    read_csv_to_dict('contact_list.csv')
    print(keys)
    repl()
    # # print(contact_list)
    # print(find_contact_index('george'))
    # print(retrieve_contact('danny devito'))
    # print(retrieve_contact('george foreman'))
    # contact = {'name':'stevphen', 'age':99, 'occupation':'retired'}
    # create_contact(contact)
    # print(update_contact('ham', {'occupation': 'chicken'}))
    # print(update_contact('hamlet', {'occupation': 'chicken'}))
    # print(delete_contact('george'))
    # print(delete_contact('gggg'))
    # for item in contact_list:
    #     print(item)     

main()