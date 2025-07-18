from pathlib import Path
import random

quotes_path = Path("data/quotes.txt")
quotes = quotes_path.read_text(encoding="utf-8").splitlines()
print(random.choice(quotes))