'''
Problem 4: Read the name, address, email and phone number
of a person through the keyboard and print the details.


Input Format:
Line 1: Name
Line 2: Address
Line 3: Email
Line 4: Phone

Output Format:
Name: [Name]
Address: [Address]
Email: [Email]
Phone: [Phone]
'''

def print_person_details():
    # TODO: Read details
    # name = input("Please enter your name: ")
    # print(type(name))
    name = input()
    address = input()
    email = input()
    phone = input()

    # Print formatted output
    print(name)
    print(address)
    print(email)
    print(phone)



if __name__ == "__main__":
    print_person_details()