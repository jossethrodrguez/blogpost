my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("ice cream")
my_foods.remove("falafel")

print(f"My favorite foods are:")
for food in my_foods:
    print(f"\t* {food}")

print(f"My friend's favorite foods are:")
for food in friend_foods:
    print(f"\t* {food}")
