if 'a' == 'a':
    print('true')

name = 'alex'
if name.title() == "Alex":
    print('true')

list = ['1', '2', '4']

if '3' not in list:
    print('NO')

dict = {5: True, "10": "yes"}
dict[10] = 'booua'
dict[True] = 15
print(dict[True])

# for n in range(1, 5), m in range(1, 10):
#     print(n)

dict = {"Minskoye more": "Belarus", "Nile": "Egypt", "Amazonka": "South America"}
for k, v in dict.items():
    print(f"{k} is located in {v}")

for k in dict:
    print(k)

for v in dict.values():
    print(v)

list = {'1', '2', 1}

for i in list:
    print(i)

cat = {"hair": "fluffy", "eyes": "small", "size": "tiny"}
dog = {"hair": "fluffy", "eyes": "broad", "size": "enormous"}
mouse = {"hair": "no hair", "eyes": "jealous", "size": "mcnuggets"}
pets = (cat, dog, mouse)
for i in pets:
    for k, v in i.items():
        print(f"the {k} is {v}")