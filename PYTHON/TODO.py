
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"TASK '{task}' added.")

def remove_task(task):
    if task in todo_list:
       todo_list.remove(task)
       print(f"TASK '{task}' removed.")
    else:
        print(f"TASK '{task}' not found.")

def show_task():
    if todo_list:
        print("Your to_do list:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("Your to do list is empty.")

while True:
    print("\n1. ADD TASK\n2. REMOVE TASK\n3. SHOW TASK\n4. EXIT")
    choice = input("ENTER TASK: ")
    if choice == '1':
        task = input("ENTER TASK:")
        add_task(task)
    elif choice == '2':
        task = input("ENTER TASK:")
        remove_task(task)
    elif choice == '3':
        show_task()
    elif choice == '4':
       break
    else:
        print("invalid choice")

    

    

