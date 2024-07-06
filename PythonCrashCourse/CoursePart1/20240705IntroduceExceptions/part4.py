from pathlib import Path
import json

path = Path(__file__).parent / "num.json"
text = path.read_text()
num = json.loads(text)
print(f"I know, your number is: {num}")