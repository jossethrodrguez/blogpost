car_brands = ['toyota', 'honda', 'bmw', 'ford',
              'chevrolet', 'audi', 'mercedes-benz', 'volkswagen']
car_user = input("Which car brand do you want?: " )
car_user = (car_user.strip()).lower()

if car_user in car_brands:
    print("\nOf course, we have that brand")
else:
    print("\nSorry, there isn't that brand")
