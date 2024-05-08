

import json
singer_albums = {}

def add_singer_album(singer_name, album_name):
    singer_albums[singer_name] = album_name
    print(f"Zpěvák '{singer_name}' a album '{album_name}' byly přidány.")

def delete_singer_album(singer_name):
    if singer_name in singer_albums:
        del singer_albums[singer_name]
        print(f"Zpěvák '{singer_name}' byl odstraněn.")
    else:
        print(f"Zpěvák '{singer_name}' nenalezen.")

def find_singer_album(singer_name):
    if singer_name in singer_albums:
        print(f"Album zpěváka '{singer_name}': {singer_albums[singer_name]}")
    else:
        print(f"Zpěvák '{singer_name}' nenalezen.")

def edit_singer_album(singer_name, new_album_name):
    if singer_name in singer_albums:
        singer_albums[singer_name] = new_album_name
        print(f"Album zpěváka '{singer_name}' bylo změněno na '{new_album_name}'.")
    else:
        print(f"Zpěvák '{singer_name}' nenalezen.")

def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(singer_albums, file)
    print("Data byla uložena.")

def load_data(filename):
    global singer_albums
    with open(filename, 'r') as file:
        singer_albums = json.load(file)
    print("Data byla načtena.")




add_singer_album("Karel Gott", "Dotek Lásky")
add_singer_album("Lucie Bílá", "Lucerna")


print("\n--- Vyhledání alba ---")
find_singer_album("Lucie Bílá")

print("\n--- Úprava alba ---")
edit_singer_album("Lucie Bílá", "Bílé Vánoce")
find_singer_album("Lucie Bílá")

print("\n--- Odstranění alba ---")
delete_singer_album("Karel Gott")
find_singer_album("Karel Gott")

print("\n--- Uložení a načtení dat ---")
save_data("singer_albums.json")
singer_albums = {}
print("Původní data:", singer_albums)
load_data("singer_albums.json")
print("Načtená data:", singer_albums)
