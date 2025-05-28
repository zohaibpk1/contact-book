#empty dicitionary
contacts = {}
while True:
    print('\nContact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact') 
    print('7. Exit')
    
    choice = input('Enter your choice ') 
    
    if choice == '1':
        name = input("enter your name = ")
        if name in contacts:
            print(f'contact name {name} already exists!')
        else:
            age = input('enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
    
    elif choice == '2':
        name = input("Enter the name to view: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Age: {contacts[name]['age']}")
            print(f"Email: {contacts[name]['email']}")
            print(f"Mobile: {contacts[name]['mobile']}")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter the name to update: ")
        if name in contacts:
            print("Enter new details (leave blank to keep current value):")
            age = input(f"Enter age [{contacts[name]['age']}]: ")
            email = input(f"Enter email [{contacts[name]['email']}]: ")
            mobile = input(f"Enter mobile number [{contacts[name]['mobile']}]: ")
            if age:
                contacts[name]['age'] = int(age)
            if email:
                contacts[name]['email'] = email
            if mobile:
                contacts[name]['mobile'] = mobile
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == '5':
        search = input("Enter name to search: ")
        found = False
        for name in contacts:
            if search.lower() in name.lower():
                print(f"Name: {name}")
                print(f"Age: {contacts[name]['age']}")
                print(f"Email: {contacts[name]['email']}")
                print(f"Mobile: {contacts[name]['mobile']}")
                found = True
        if not found:
            print("No matching contact found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        