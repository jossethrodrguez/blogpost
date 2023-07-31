# Making users.

aeinstain = {
   'first': 'albert',
   'last': 'einstein',
   'location': 'princeton',
   }

mcurie = {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    }

users = {
    'einstein': aeinstain,
    'mcurie': mcurie,
        }

# Showing users info.
for username, user_info  in users.items():
    print(f"\nUsername: {username}")
    print(f"\tFullname: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tLocation: {user_info['location'].title()}")
