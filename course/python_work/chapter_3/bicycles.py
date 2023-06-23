bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0].title())  # Return the first item.
print(bicycles[1].title())  # Return the second item.
print(bicycles[-1].title())  # Return the last item.

bicycles.insert(1, "Cobra")
print(bicycles)
print(bicycles[1])
del bicycles[1]
print(bicycles[1])

message = f"My first bicycle was a {bicycles[2].title()}.\n"
print(message)

bicycles.append("ducati")
print(bicycles)

popped_bicycle = bicycles.pop()
print(bicycles)
print(f"Popped Bicycle: {popped_bicycle.title()}.\n")

popped_bicycle = bicycles.pop(0)
print(f"Popped Bicycle: {popped_bicycle.title()}.\n")
print(bicycles)

bicycles.remove("redline")
print(bicycles)
