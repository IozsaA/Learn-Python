from database import Database

class Saveable:
    def to_dict(self):
        return {
        }

    def save(self):
        Database.insert(self.to_dict())
