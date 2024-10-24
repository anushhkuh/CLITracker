import json
import os

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
else:
    tasks = {"tasks": []}

def display_menu():
    print("Welcome to the CLI tracker!\n")
    print("---Menu---\n")
    print("add - for adding new tasks\n")
    print("delete- to delete a task\n")
    print("update - to update a task\n")
    print("mark-in-progress - to mark as progress or done\n")
    print("list todo - tasks that are yet to be done\n")
    print("list in-progress -  showing tasks in progress\n")
    print("list done - completed tasks\n")
    operation = input()


def switch(operation):
    if operation == "add":
        add()
    elif operation == "delete":
        delete()
    elif operation =="update":
        update()
    elif operation == "mark-in-progress":
        markInProgress()
    elif operation == "list todo":
        todo()
    elif operation == "list in-progress":
        inProgress()
    elif operation == "done":
        done()
    else:
        print("invalid input!")



def add():
    add_input = input("What task would you like to add?")
    new_task = {
        "id": len(tasks["tasks"]) + 1,
        "description": add_input,
        "status": "incomplete"
    }

    tasks["tasks"].append(new_task)
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)

def delete():
    task_ID = int(input("ID of the task to be deleted?"))
    tasks["tasks"] = [task for task in tasks["tasks"] if task["id"] != task_ID]

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task {task_ID} deleted successfully.")

def update():
    task_id = int(input("Enter the ID of the task to update: "))
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            new_description = input("Enter the new description: ")
            task["description"] = new_description

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} updated successfully.")
            return

    print(f"Task {task_id} not found.")

def markInProgress():
    task_id = int(input("Enter the ID of the task to mark: "))
    status = input("Enter 'in progress' or 'done': ").lower()
    if status not in ["in progress", "done"]:
        print("Invalid status.")
        return

    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task["status"] = status

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} marked as {status}.")
            return

    print(f"Task {task_id} not found.")

def todo():
    print("Tasks to be done:")
    for task in tasks["tasks"]:
        if task["status"] == "incomplete":
            print(f"ID: {task['id']}, Description: {task['description']}")

def inProgress():
    print("Tasks in progress:")
    for task in tasks["tasks"]:
        if task["status"] == "in progress":
            print(f"ID: {task['id']}, Description: {task['description']}")

def done():
    print("Completed tasks:")
    for task in tasks["tasks"]:
        if task["status"] == "done":
            print(f"ID: {task['id']}, Description: {task['description']}")

print("Welcome to the CLI tracker!")

running = True
while running:
    display_menu()
    operation = input("\nEnter your operation: ").lower()
    running = switch(operation)

print("Goodbye! The program has stopped.")