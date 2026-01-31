from task_app.database.storage import store_task

def create_task():
    while True:
        task = input("Type your task: \n")
        if task == "":
            print("You must type something, the task can't be nothing")
        else:
            store_task(task)
            break
        
def remove_task():
    while True:
        task_to_remove = input("Type the task you want to be removed: \n")
        if task_to_remove == "":
            print("You must type something, you can't remove an empty task.")
        else:
            break

def check_tasks():
    print("sh")

if __name__ == "__main__":
    create_task()