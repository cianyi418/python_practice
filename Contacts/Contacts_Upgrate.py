# 建立通訊錄 建立一個字典，讓使用者輸入名字與電話號碼，並可以查詢或新增聯絡人。
import json
import os

# Path to the JSON file that will store the contacts
json_file_path = 'ContactPersonList.json'

# Load the contacts from a JSON file
if os.path.exists(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
            if not isinstance(contacts, dict): #comfirm the contacts is a dict
                contacts = {}
    except json.JSONDecodeError:
        contacts = {}
        print("Error decoding JSON file. Starting with an empty contact list.")
else:
    contacts = {}
    print("JSON file not found. Starting with an empty contact list.")

# Save the contacts to a JSON file
def save_contacts():
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)
    print("Contacts saved to", json_file_path)

while True:
    print("\nChoose an option:")
    print("1. Search for a contact")
    print("2. Add a contact")
    print("3. Delete a contact")
    print("4. Show all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        name = input("Enter the name of the contact: ").strip().lower()
        found = False
        for contact_name, phone in contacts.items():
            if contact_name.lower() == name:
                print(f"{contact_name}'s phone number is {phone}")
                found = True
                break
        else:
            print(f"{name} not found in contacts")

    elif choice == '2':
        name = input("Enter the name of the contact: ").strip()
        if not name:
            print("Name cannot be empty, please try again")
            continue
        if name.lower() in (contact_name.lower() for contact_name in contacts):
            print(f"{name} already exists, the phone number is {contacts[name]}")
        else:
            phone = input("Enter the phone number: ").strip()
            if not phone.isdigit():
                print("Phone number must be a number, please try again")
                continue

            contacts[name] = phone
            print(f"{name} added to contacts")
            save_contacts()
            

    elif choice == '3':
        name = input("Enter the name of the contact you want to delete: ").strip()
        found = False
        for contact_name in list(contacts.keys()):
            if contact_name.lower() == name.lower():
                del contacts[contact_name]
                print(f"{contact_name} has been deleted from contacts")
                found = True
                save_contacts()
                break
        if not found:
            print(f"{name} not found in contacts")    

    elif choice == '4':
        if contacts:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again")
