import json
from app.config import DB_PATH

class DBService:
    def __init__(self):
        self.db_path = DB_PATH

    def read_db(self):
        with open(self.db_path, "r") as f:
            return json.load(f)

    def write_db(self, data):
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=2)
