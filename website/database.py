from pymongo import MongoClient

def get_database():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['task_manager']
        print("Connected to MongoDB successfully!")
        return db
    except Exception as e:
        print("Could not connect to MongoDB:", e)
        return None

def get_users_collection():
    db = get_database()
    if db is not None:  # Use explicit None check
        return db['users']
    else:
        print("Database connection failed.")
        return None

def get_tasks_collection():
    db = get_database()
    if db is not None:  # Use explicit None check
        return db['tasks']
    else:
        print("Database connection failed.")
        return None
