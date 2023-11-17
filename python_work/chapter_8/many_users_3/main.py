from list_users import list_user
from building_users import build_user
from show_user_info import show_info

users = {}
flag = True

while flag:
    print("\n-- OPTIONS -- \n1. List Users \n2. Build user \n3. Show Users information  \n4. Quit")
    task_selected  = input("What do you want to do? (input index option): ")
    task_selected = int(task_selected)
    
    
    if task_selected == 1:
        list_user(users)
    elif task_selected == 2:
        build_user(users)
    elif  task_selected == 3:
        show_info(users)
    elif task_selected == 4:
        flag = False
        print("\n-- GOODBYE -- \n")
    else:
        print("Please, Just input the given options. \n")