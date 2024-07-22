from colorama import init, Fore, Style

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def phone_user(args, contacts):
    [name] = args
    
    phone = contacts.get(name)

    if phone:
      return f"{name}: {phone}"
    else:
        return "Not found phone"
    
def all_users(contacts):
    for name, phone in contacts.items():
        print(f"{Fore.GREEN}Name: {Fore.CYAN}{name}, {Fore.GREEN}Phone: {Fore.CYAN}{phone}{Style.RESET_ALL}") 

def main():
    init()

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_user(args, contacts))
        elif command == "all":
            print(all_users(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
