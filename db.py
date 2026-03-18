import json

DB_FILE = "db.json"

def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user(user_id):
    db = load_db()
    if str(user_id) not in db:
        db[str(user_id)] = {"coins": 100}
        save_db(db)
    return db[str(user_id)]

def update_coin(user_id, amount):
    db = load_db()
    user = get_user(user_id)
    user["coins"] += amount
    db[str(user_id)] = user
    save_db(db)