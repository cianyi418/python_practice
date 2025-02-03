# 建立通訊錄 建立一個字典，讓使用者輸入名字與電話號碼，並可以查詢或新增聯絡人。
import json
import os

# Path to the JSON file that will store the contacts
json_file_path = 'ContactPersonList.json'

# Load the contacts from a JSON file
if os.path.exists(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            contacts = json.load(file)
            print("Current contacts:", contacts)
    except json.JSONDecodeError:
        contacts = []
        print("Error decoding JSON file. Starting with an empty contact list.")
else:
    contacts = []
    print("JSON file not found. Starting with an empty contact list.")

while True:
    person_name = input("Please enter the name of the person you want to look up (or type 'exit' to quit): ").strip() #strip() 是 Python 字符串方法之一，用於移除字符串開頭和結尾的空白字符（包括空格、制表符、換行符等）。這個方法不會改變原字符串，而是返回一個新的字符串。
    if person_name.lower() == "exit":
        break
    
    found = False
    for contact in contacts:
        if contact['name'].lower() == person_name.lower():
            print(f"The phone number of, {contact['name']}, is {contact['phone']}")
            found = True
            break
    if not found:
        print("The person", person_name, "is not in the contact list.")
        phone_number = input("Please enter the phone number of " + person_name + ": ").split()[0]
        new_contact = {'name': person_name, 'phone': phone_number}
        contacts.append(new_contact)
        print(person_name, "has been added to the contact list.") 

# Save the contacts to a JSON file
with open(json_file_path, 'w') as file:
    json.dump(contacts, file, indent=4)
    print("Contacts saved to", json_file_path)

print("Current contcts", contacts)