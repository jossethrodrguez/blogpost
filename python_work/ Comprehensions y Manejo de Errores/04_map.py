# MAP( )
# La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.

# Sintaxis.
# map(function, iterables)

# Con esto vamos hacer unos deliciosos tacos, para ello utilizáremos maps()

def ingredientes(a, b):
  return a + " es a " + b

menu = list(map(ingredientes, ('carne', 'maiz', 'aguacate'), ('molida', 'tacos', 'guacamole')))

print(list(menu))

# _Producción_
['carne es a molida', 'maiz es a tacos', 'aguacate es a guacamole']


items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items)) 

print(new_items)   
print(items)