from pathlib import Path

curpath = Path(__file__).parent / 'learned.txt'

text = curpath.read_text()
print(text)
text = text.replace("I ", "You ") 
for str in text.splitlines():
    print(str)