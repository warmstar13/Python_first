# import this
#
# print(10 ** 400 - 1)

# The next piece of code tests if the uppercase letters are meaning that the variable is constant
# MAXNUM = 10
# MAXNUM += 1
# print(MAXNUM) # bla bla bla

#names = ['artsiom', 'kirek', 'garik', "kirek"]
#print(f"Hello, my dear {names[0]}")
#print(f"Hello, my dear {names[1]}")
#print(f"Hello, my dear {names[-1]}")
#print(names)
#names.remove('kirek')
#print(names)

guests = ['luise', 'pedro', 'watson']
print(f"Dear {guests[0]}, asking you for a dinner")
print(f"Dear {guests[1]}, asking you for a dinner")
print(f"Dear {guests[2]}, asking you for a dinner")
print(f"sadly, {guests[0]} can't visit us")
guests.remove('luise')
guests.insert(0, "mario")
print(f"Dear {guests[0]}, asking you for a dinner")
print(f"Dear {guests[1]}, asking you for a dinner")
print(f"Dear {guests[2]}, asking you for a dinner")
print("I found a bigger table")
guests.insert(0, "volod")
guests.insert(3, 'keglya')
guests.append('clown')
print(f"Dear {guests[0]}, asking you for a dinner")
print(f"Dear {guests[1]}, asking you for a dinner")
print(f"Dear {guests[2]}, asking you for a dinner")
print(f"Dear {guests[3]}, asking you for a dinner")
print(f"Dear {guests[4]}, asking you for a dinner")
print(f"Dear {guests[5]}, asking you for a dinner")

print("Facepalm, only 2 guests today")
sad_person = guests.pop()
print(f"{sad_person}, not today(")
sad_person = guests.pop()
print(f"{sad_person}, not today(")
sad_person = guests.pop()
print(f"{sad_person}, not today(")
sad_person = guests.pop()
print(f"{sad_person}, not today(")
print(f"{guests}, you are still invited")
del guests[0]
del guests[0]
print(guests)