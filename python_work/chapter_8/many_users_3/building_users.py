
def build_user(list_of_users = {}):
    
    print("\n-- NEW USER --\n")
    username = input("Input usename: ").strip()
    
    list_of_users[username] = {
            'first name': (input("Type the first name: ").title()).strip(),
            'last last': (input("Type the last name: ").title()).strip(),
            }
    