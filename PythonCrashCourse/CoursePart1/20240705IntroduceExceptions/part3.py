from pathlib import Path
import json

path = Path(__file__).parent / "num.json"

def new_user():
    str = input("write 3 your favourite numbers: ")
    list = str.split()
    for x in range(0, len(list)):
        list[x] = int(list[x])
    temp = json.dumps(list)
    path.write_text(temp)

if not path.exists():
    new_user()
else:
    text = path.read_text()
    num = json.loads(text)
    print(f"I know, your numbers are: {num}")
