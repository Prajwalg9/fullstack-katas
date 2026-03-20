import sqlite3
import pandas as pd

conn=sqlite3.connect("TO_DO.db")
cursor=conn.cursor()
table="CREATE TABLE IF NOT EXISTS TO_DO(SR INTEGER PRIMARY KEY AUTOINCREMENT,Task TEXT NOT NULL,Status TEXT NOT NULL,Task_added_at DATETIME DEFAULT (datetime('now', 'localtime')))"
cursor.execute(table)
conn.commit()

def add_task(task_list):
    status = "Incomplete"
    for task in task_list:
        insert_task = cursor.execute("INSERT INTO TO_DO(Task,Status) VALUES (?,?)",(task,status))
        conn.commit()
        print("Task Added!\n")


def view_tasks():
    tasks_data="SELECT * FROM TO_DO"
    df=pd.read_sql_query(tasks_data,conn)
    print(f"\nYour Tasks:\n{df}\n")


def set_status(index):
    status = "Completed"
    cursor.execute("UPDATE TO_DO SET Status = ? WHERE SR = ?",(status,index))
    conn.commit()
    print("Status Updated!")
    view_tasks()

def delete_task(index):
    confirm=input("Are you sure want to delete the task ? (y/n) : ")
    if(confirm.lower()=="y"):
        delete_task = cursor.execute("DELETE FROM TO_DO WHERE SR = ?", (index,))
        conn.commit()
        print("Task Deleted!")
        view_tasks()
    elif(confirm.lower()=="n"):
        print("Task Not Deleted!")
    else:
        print("Invalid Choice")

def main():
    print("welcome to To Do App")
    print("-Here you can add your tasks\n")
    while True:
        print("Select an option by index: ")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Set task as completed")
        print("4. Delete task")
        print("5. Quit\n")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            tasks = int(input("How many tasks would you like to add? : "))
            task_list=[]
            for i in range(tasks):
                task = input("Enter your tasks followed by enter: ")
                task_list.append(task)
            add_task(task_list)

        elif(choice==2):
            view_tasks()

        elif(choice==3):
            view_tasks()
            index=int(input("Enter index of the task to set it as completed: "))
            set_status(index)

        elif (choice == 4):
            view_tasks()
            index = int(input("Enter index of the task to delete it: "))
            delete_task(index)

        elif(choice==5):
            print("Goodbye")
            break

        else:
            print("Invalid choice")
            continue


if __name__ == "__main__":
    main()