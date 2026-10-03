import addressbook_pb2


address_book = addressbook_pb2.AddressBook()

with open("addressbook.bin", "rb") as file:
    address_book.ParseFromString(file.read())

print(address_book)