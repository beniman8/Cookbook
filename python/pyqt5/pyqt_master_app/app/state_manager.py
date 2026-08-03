import json, os
FILE="data/app_state.json"

def save_state(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE,"w") as f:
        json.dump(data,f)

def load_state():
    if not os.path.exists(FILE): return {}
    with open(FILE) as f:
        return json.load(f)
