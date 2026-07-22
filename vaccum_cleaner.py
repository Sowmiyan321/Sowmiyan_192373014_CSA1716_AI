rooms = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

while True:

    if rooms[location] == 'Dirty':
        print(f"Cleaning Room {location}")
        rooms[location] = 'Clean'
    else:
        print(f"Room {location} is already Clean")

    if all(status == 'Clean' for status in rooms.values()):
        print("\nAll rooms are clean.")
        break

    location = 'B' if location == 'A' else 'A'

print("\nFinal Room Status:")
print(rooms)