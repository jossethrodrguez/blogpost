usernames = ["admin","john_doe", "jane_smith", "alex_123", "emma_wilson"]

if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello admin, would you i like a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
