players = ["charles", "martina", "michael", "florence", "eli"]

print("\nThe WINNERS are:")
for player in players[:3]:
    print(f"\tThe {players.index(player) + 1}th place is: {player.title()}")

print("The last places was:")
for player in players[-2:]:
    print(f"\tThe {players.index(player) + 1}th place is: {player.title()}")

players.sort()
print("\nThe new WINNERS are:")
for player in players[:3]:
    print(f"\tThe {players.index(player) + 1}th place is: {player.title()}")

print("The last places was:")
for player in players[-2:]:
    print(f"\tThe {players.index(player) + 1}th place is: {player.title()}")


