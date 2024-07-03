from pathlib import Path

curpath = Path(__file__).parent
path = curpath / 'new_text.txt'
text = path.read_text()
print(text)
print(type(text))