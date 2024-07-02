from pathlib import Path

path = Path('text.txt')
text = path.read_text()
print(text)
