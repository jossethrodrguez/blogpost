person_0 = {
        'first_name': 'cristiano',
        'last_name': 'ronaldo',
        'age': 38,
        'city': 'madeira',
        }
#person_0['number'] = 7
#person_0['girl'] = 'georgina'
#
#print(person_0.get('girl', 'single'))
for masa, value in person_0.items():
    str_convert = str(value)
    print(f"{masa}: {str_convert.title()}")

masa = ['mortadela', 'zuero']
print(masa)
masa.clear()

print(masa)
