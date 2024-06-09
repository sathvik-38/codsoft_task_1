tasks=[]

def addTask():
    task=input("Please Enter the Task : ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")
    
def deleteTask():
    listTasks()
    try:
        taskToDelete=int(input("Choose the number you want to Delete"))
        if taskToDelete>=0 and taskToDelete< len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed")
        else:
            print(f"Task '{taskToDelete}' was not found")
    except:
        print("Invlid input Given")

 
def listTasks():
    if not tasks:
        print("There are not tasks inserted in it ??")
    else:
        print("Current Tasks are Listed here")
        for index, task in enumerate(tasks):
            print(f"Task {index} . 1{task}")
        


if __name__=="__main__":
    print("Welcome to the To Do List !")
    while True:
        print("\n")
        print("Please select any option from the list")
        print("-----------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice=input("Enter the choice: ")
        
        if (choice== "1"):
            addTask()
        elif (choice== "2"):
            deleteTask()
        elif (choice== "3"):
            listTasks()
        elif (choice== "4"):
            break
        else:
            print("Invalid choice Try again")
    print("Thanks !")
