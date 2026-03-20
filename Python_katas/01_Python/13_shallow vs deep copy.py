"""
=========================================
SHALLOW COPY vs DEEP COPY IN DICTIONARIES
=========================================

WHY COPYING MATTERS?
--------------------
When you copy a dictionary, you must decide:
• Do you want a NEW independent dictionary?
• Or a copy that still shares nested objects?

SHALLOW COPY
------------
Uses:
    new_dict = old_dict.copy()
    OR
    new_dict = dict(old_dict)

Behavior:
    ✔ Top-level keys and values are copied
    ✘ Nested objects (lists, dicts) are NOT copied
      → They still reference the same object

DEEP COPY
---------
Uses:
    from copy import deepcopy
    new_dict = deepcopy(old_dict)

Behavior:
    ✔ Everything is fully copied
    ✔ Nested objects become independent
"""

from copy import deepcopy

# Original dictionary
original = {
    "name": "Prajwal",
    "skills": ["Python", "C", "JavaScript"],   # Nested list
    "details": {
        "age": 21,
        "city": "Pune"
    }
}

print("Original Dictionary:")
print(original, "\n")

# -----------------------------------
# SHALLOW COPY
# -----------------------------------
shallow_copy = original.copy()

# Modify nested list in shallow copy
shallow_copy["skills"].append("Machine Learning")

# Modify nested dictionary in shallow copy
shallow_copy["details"]["age"] = 22

print("After modifying SHALLOW COPY:")
print("Original:", original)
print("Shallow Copy:", shallow_copy)
print("\nObservation: Nested changes affect BOTH → shared references\n")

# -----------------------------------
# DEEP COPY
# -----------------------------------
deep_copy = deepcopy(original)

# Modify nested objects in deep copy
deep_copy["skills"].append("Deep Learning")
deep_copy["details"]["city"] = "Mumbai"

print("After modifying DEEP COPY:")
print("Original:", original)
print("Deep Copy:", deep_copy)
print("\nObservation: Changes do NOT affect original → fully independent copy\n")

print("--- END OF SHALLOW vs DEEP COPY DEMO ---")
