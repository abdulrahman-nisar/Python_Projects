tasks=[]

##Function to add a task to the list
def add_task():
    task=input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task ' {task} ' added successfully")

##Function to remove a task from the list
def delete_task():
    
    list_tasks()
    if tasks:
        try:
           task_to_delete=int(input("Enter the task number to delete: "))

           if 0<task_to_delete<=len(tasks):

            tasks.pop(task_to_delete-1)
            print(f"Task #{task_to_delete} deleted successfully.")

           else:
            print(f"Task #{task_to_delete} does not exist.")   

        except ValueError:
           print("Invalid input. Please enter a valid task number.")
    else:
        print("No tasks to delete.")
         
##Function to list all the tasks
def list_tasks():

    if not tasks:
        print("No tasks to display.")
        return False

    else:
        print("Current tasks:")

        for index,task in enumerate(tasks):
            print(f"{index+1}# {task}")
    return True




if __name__ == "__main__":
    ##Create a loop to run the app
    while True:
        print("\nPlease select one  of the following options:")
        print("----------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Exit")
        choice=input("Enter your choice:")

        if(choice=="1"):
            add_task()

        elif(choice=="2"):
            delete_task()

        elif(choice=="3"): 
            list_tasks()

        elif(choice=="4"):  
            break

        else:
            print("Invalid choice. Please try again.")    

