# ContactList.py
# self.__contact_list.py implemented as class

class ContactList:

    def __init__(self):
        self.__contact_list = []

    def __len__(self):
        return len(self.__contact_list)

    def __str__(self):
        return str(self.__contact_list)

    def get_contact_list(self):
        return self.__contact_list

    def set_contact_list(self, modified_list):
        self.__contact_list = modified_list

    def read_csv_to_dict(self, file_path):
        """ setting global self.__contact_list with csv as list of dictionaries
        """
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

        self.__contact_list = list_of_dicts


    def save_dict_to_csv(self, destination_path):
        """ writes contact list of dictionaries to csv at destination_path
        """
        csv = ','.join(keys) + '\n'

        for contact in self.__contact_list:
            row = contact.values()
            csv += ','.join(row) + '\n' # turn list into comma separated string

        with open(destination_path, 'w') as f:
            f.write(csv)    


    def __find_contact_index(self, name):
        """ name: string
        returns index of contact given name
        """
        index = None
        for i in range(len(self.__contact_list)):
            contact = self.__contact_list[i]
            if name == contact['name']:
                index = i
                break
        return index


    def create_contact(self, contact):
        """ contact: dict 
        adds contact to self.__contact_list
        """
        self.__contact_list.append(contact)
        return contact


    def retrieve_contact(self, name):
        """ name: string
        finds contact given name from self.__contact_list
        returns contact data
        """
        index = self.__find_contact_index(name)
        if index is not None:
            return self.__contact_list[index]
        return 'Contact does not exist.'


    def update_contact(self, name, updated_data): 
        """ name: string
        updated_data: dict
        updates contact with updated_data
        """
        # 1. find the contact given name
        index = self.__find_contact_index(name)
        if index is not None:
        # 2. update that contact with the updated_data dict
            contact = self.__contact_list[index]
            contact.update(updated_data)
            return contact
        return 'Contact does not exist.'


    def delete_contact(self, name):
        """ name: string
        deletes contact given name
        """
        index = self.__find_contact_index(name)
        if index is not None:   
            contact = self.__contact_list.pop(index)
            return f"Removed {contact['name']}"
        return 'Contact does not exist.'


    def print_all(self):
        """ prints all contacts
        """
        for contact in self.__contact_list:
            print(contact['name'])

