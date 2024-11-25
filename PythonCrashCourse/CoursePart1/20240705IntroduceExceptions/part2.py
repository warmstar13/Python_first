from pathlib import Path
import json
numbers = {"x": 5, "y": 4}
path = Path(__file__).parent / 'numbers.json'
contents = json.dumps(numbers)
path.write_text(contents)