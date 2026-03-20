"""
Json Module:
To run any of below functions just uncomment the calling of code
"""
import json

#TO Load data from json file
FILE='data.json'
def Load_data(FileName):
    try:
        with open(FileName,'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return "File not found"

#print(Load_data(FILE))

#To save data:
Data=[{"id":1,"name":"Jhon","age":18},{"id":2,"name":"Alice","age":19},{"id":3,"name":"Bob","age":20}]
def Save_data(FileName,data):
    with open(FileName,'w') as f:
        json.dump(data,f,indent=4)

#Save_data(FILE,Data)

#To insert new record:
def Add_data(NewData):
    db=Load_data(FILE)
    for p in db:
        if p['id'] ==NewData['id'] and p['name']==NewData['name']:
            print(f"The data with id: {NewData['id']} and name: {NewData['name']} already exists!")
            return
    db.append(NewData)
    Save_data(FILE, db)
    print(f"The data with id: {NewData['id']} and name: {NewData['name']} has been added!")

# new_data={"id":5,"name":"Raju","age":19}
# Add_data(new_data)

#To find record by id:
def Get_Record(ID):
    db=Load_data(FILE)
    for p in db:
        if p['id'] == ID:
            return p
    return "Record not found!"

# print(Get_Record(5))

#Deleting record:
def Delete_Record(ID):
    db=Load_data(FILE)
    new_data=[]
    for p in db:
        if p['id'] != ID:
            new_data.append(p)
    Save_data(FILE, new_data)
    if new_data==db:
        print(f"The data with id: {ID} does not found!")
    else:
        print(f"The data with id: {ID} has been deleted!")

# Delete_Record(5)

#Update By id
def Update_Record(ID,**changes):
    db=Load_data(FILE)
    for p in db:
        if p['id'] == ID:
            p.update(changes)
            break
    if db==Load_data(FILE):
        print("Record not found!")
    else:
        Save_data(FILE, db)
        print(f"The data with id: {ID} has been updated!")

# Update_Record(1,name="Nikhil",age=16)
