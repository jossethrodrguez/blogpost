pizza_0 = {
        'crust': 'thick',
        'topping': ['mushrooms', 'extra cheese'],
        }

print(f"You ordered a {pizza_0['crust']}-crust pizza "
      "with the following topping: ")

for topping in pizza_0['topping']:
    print(f"\t* {topping}")
