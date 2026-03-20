"""
pickle_module_demo.py

This script covers:
- pickle.dump / pickle.load (files)
- pickle.dumps / pickle.loads (strings)
- Pickling built-in Python objects
- Pickling custom classes
- Using highest protocol
- Basic safety note
"""

import pickle

# 1. PICKLING (serializing) Python objects to a file
data = ['apple', 'banana', 42, {'key': 'value'}, (1, 2, 3)]

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
print("1. Pickled data saved to 'data.pkl'")

# 2. UNPICKLING (deserializing) Python objects from a file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print("2. Loaded data from 'data.pkl':")
print(loaded_data)

# 3. PICKLING to a bytes object (in memory)
pickled_bytes = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print("3. Pickled bytes (in-memory):", pickled_bytes[:60], "...")  # show partial bytes

# 4. UNPICKLING from bytes
unpickled_obj = pickle.loads(pickled_bytes)
print("4. Unpickled object from bytes:", unpickled_obj)

# 5. Pickling custom classes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

users = [User("Alice", 30), User("Bob", 25)]

with open('users.pkl', 'wb') as file:
    pickle.dump(users, file)
print("5. Pickled list of User objects to 'users.pkl'.")

with open('users.pkl', 'rb') as file:
    loaded_users = pickle.load(file)
print("Loaded users:")
print(loaded_users)

# 6. SAFETY NOTE
print("\n*** Safety Notice ***")
print("Never unpickle data received from an untrusted or unauthenticated source!")
print("Pickle can execute arbitrary code during unpickling, which is a security risk.\n")

# 7. Raising error on loading large files (a simple safe_unpickle example)
import os

def safe_unpickle(filename, max_mb=5):
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(f"File too large: {size_mb:.2f} MB")
    with open(filename, 'rb') as f:
        return pickle.load(f)

try:
    obj = safe_unpickle('data.pkl')
    print("Safe unpickle succeeded:", obj)
except Exception as e:
    print("Safe unpickle error:", e)

# 8. You can pickle many Python types: lists, dicts, sets, tuples, classes, functions (if top-level)

# Summary message
print("\n--- End of pickle module demo ---")
