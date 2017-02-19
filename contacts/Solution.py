
class ContactNode(object):

    def __init__(self, letters = None):
        self.letters = letters
        self.children = {}
        self.number_of_occurences = 1

    def expand(self):
        if not self.letters:
            return
        self.children[self.letters[0]] = ContactNode(self.letters[1:])
        self.letters = None

class ContactApp(object):
    def __init__(self):
        self.root = ContactNode()

    def add_contact(self, contact):
        contact_node = self.root
        for i in range(len(contact)):
            letter = contact[i]
            if letter not in contact_node.children:
                new_contact_node = ContactNode(letters = contact[i + 1:])
                contact_node.children[letter] = new_contact_node
                break
            else:
                contact_node = contact_node.children[letter]
                contact_node.expand()
                contact_node.number_of_occurences += 1

    def get_number_of_occurences(self, contact):
        contact_node = self.root
        for letter in contact:
            if letter not in contact_node.children:
                return 0
            contact_node = contact_node.children[letter]
            contact_node.expand()
        return contact_node.number_of_occurences


n = int(input().strip())
contact_app = ContactApp()

for i in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        contact_app.add_contact(contact)
    else:
        print(contact_app.get_number_of_occurences(contact))
