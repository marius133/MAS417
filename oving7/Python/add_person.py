import addressbook_pb2


address_book = addressbook_pb2.AddressBook()

person = address_book.people.add()

person.name = input("Name: ")
person.id = int(input("ID: "))
person.email = input("Email: ")

with open("addressbook.bin", "wb") as file:
    file.write(address_book.SerializeToString())

print(address_book)