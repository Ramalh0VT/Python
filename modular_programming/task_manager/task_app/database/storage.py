import os

# dynamic path to ensure the text file is always found
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_data.txt")

def store_task(task_to_be_added):
    try:
        with open(FILE_PATH, "a") as f:
            f.write(task_to_be_added + "\n")
            print("Task added successfully!")
    except Exception as e:
        print(f"Error saving task: {e}")

def task_deleter():
    print("sh")

def tasks_data():
    print("sh")

if __name__ == "__main__":
    # Test code
    pife = "Test Task"
    store_task(pife)