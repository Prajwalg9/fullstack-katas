class contact:
    phone_directory=[]
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        contact.phone_directory.append(self)

    @staticmethod
    def validate_contact(number):
        if (len(number)==10 or len(number)==12) and number.isdigit():
            return True
        else:
            return False

    def show_details(self):
        print(f"Name: {self.name}\nPhone: {self.phone}")

    @classmethod
    def display(cls):
        if len(cls.phone_directory)>0:
            for directory in cls.phone_directory:
                directory.show_details()
        else:
            print("⚠️ No contact found!")

    @classmethod
    def search(cls,name):
        for directory in contact.phone_directory:
            if name != directory.name:
                continue
            else:
                print(f"{directory.name} Phone number: {directory.phone}")
                break
        print(f"⚠️ {name} not found in contact list!")



n_contacts=int(input("Enter the number of contacts to be added:"))
if n_contacts<=0:
    print("value should be a positive integer")
    n_contacts = int(input("Enter the number of contacts to be added:"))
for i in range(n_contacts):
    name=input("Enter the contact name:")
    phone=input("Enter the contact phone:")
    if contact.validate_contact(phone):
        contact(name,phone)
    else:
        print(f"⚠️ {phone} is not a valid Phone number!")
        continue
contact.display()

contact.search("Radha")