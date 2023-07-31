available_toppings = ['peperroni', 'napolitan', 'mushrooms', 
                      'green peppers', 'extra cheese', 'olives', 'pineapple']

request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in available_toppings:
            print(f"Adding {request_topping}.")
    else: 
        print(f"Sorry, we don't have {request_topping}.")

print("\nFinished making your pizza!")
