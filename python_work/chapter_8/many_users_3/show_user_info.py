
def show_info(list_of_user = {}):
    print("\n-- SHOW USERS INFORMATION -- \n")
    
    if list_of_user:
        for key, value in list_of_user.items():
            print(f"\nUsername: {key}")
            for k, v in value.items():
                print(f"{k.title()} : {v.title()}")
    else:
        print("There isn't users yet.")