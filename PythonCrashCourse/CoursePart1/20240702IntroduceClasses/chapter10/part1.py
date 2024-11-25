from pathlib import Path

curpath = Path(__file__).parent
path = curpath / 'new_text.txt'
text = path.read_text()
print(text)
print(type(path))
list = text.splitlines()
string = ''
for str in list:
    str = str.strip()
    string += str
print(string)

for x in string:
    print(x)

# x = "123456"
# print(x[1:3])

# for x in range(1, 5):
#     x -= 1
#     print(x)