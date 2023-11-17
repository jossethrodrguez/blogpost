# Module to list users:

def list_user(list_of_users = {}):
    print("\n-- LIST OF USERS --")
    
    if list_of_users:
        for key in list_of_users.keys():
            print(f"\t* {key}")
    else:
        print("There isn't users yet.")