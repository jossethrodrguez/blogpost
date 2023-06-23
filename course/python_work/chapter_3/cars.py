cars = ["bmw", "audi", "toyota", "subaru"]
# Temporal change:
print(f"\nNormal order: {cars}")
print(f"\nList on order: {sorted(cars)}")
print(f"\nNormal order: {cars}")
cars.reverse()
print(f"\nList on reverse order: {cars}")

# Permanent change:
print(cars) # Normal order
cars.sort()
print(cars) # Alphabetical
cars.sort(reverse = True)
print(cars) # Reverse-Alphabetical order order

print(f"Quantity of items: {len(cars)}")
