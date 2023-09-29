# Syntax:
# {key:value for var in iterable}
# Example:
# {i : i * 2 for i in range(1, 5)}

# names = ['nico', 'zule', "santi"]
# edades = [12,56,98]
# new_dict = {names[i]:edades[i] for i in range(len(names))}

# names = ['nico', 'zule', "santi"]
# edades = [12,56,98]
# new_dict=dict(zip(names,edades))

# new_dict = {name: age for (name, age) in zip(names, age)}

# {key:value for var in iterable if condition}
# Example:
# import random
# countries = ['col', 'mex', 'bol', 'pe']

# population_v2 = { country: random.randint(1, 100)  for country in countries}
# print(population_v2)

# result = { country: population for (country, population) in population_v2.items() if population > 50 }
# print(result)

# text = 'Hola, soy Nicolas'
# unique = { c: c.upper() for c in text if c in 'aeiou' }
# print(unique)

# text = "Hola a todos, esta es una cadena de texto de prueba."
# unique = { c: text.count(c) for c in text if c in 'aeiou' }
