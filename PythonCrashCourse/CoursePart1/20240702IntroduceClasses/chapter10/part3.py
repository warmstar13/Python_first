from pathlib import Path

curpath = Path(__file__).parent / "guests.txt"
name_guest = ''
string = ""
while True:
    name_guest = input("Please, write your first and last name: ")
    if name_guest == "q":
        break
    string += name_guest + '\n'
curpath.write_text(string)