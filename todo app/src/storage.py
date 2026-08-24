# save JSON file
import json
from pathlib import Path

# search file tasks.json 
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"

# create functions
# function for loading tasks
def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["tasks"]

# function to save tasks
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"tasks": tasks}, f, indent=4)
