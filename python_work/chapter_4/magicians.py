magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"\n{magician.title()}, That was a great trick!")
    print(f"I can't wait to see you next trick, {magician.title()}!")

print(magician)

print("\nReverse magicians order:" )
magicians.reverse()
for magician in magicians:
    print(f"\n{magician.title()}, That was a great trick!")
    print(f"I can't wait to see you next trick, {magician.title()}!")


print(magician)
