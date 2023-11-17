
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"This a {self.name}!, and we are a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

angelicas_restaurant = Restaurant("Angelica's Restaurant", "Buffet")
angelicas_restaurant.describe_restaurant()
