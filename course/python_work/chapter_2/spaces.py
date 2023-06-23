favorite_lenguage = " python "

print(favorite_lenguage.rstrip())   #remove extra white space from the left
print(favorite_lenguage.lstrip())   #remove extra white space from the right
print(favorite_lenguage.strip())    #remove extra white space from both sides

# Removing prefixes:
url = "https://nostarch.com"
print(url)
simple_url = url.removeprefix("https://")
print(simple_url)

# Removing suffixes:
file = "python_notes.txt"
print(file)
simple_file = file.removesuffix(".txt")
print(simple_file)
