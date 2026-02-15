class toDoListApp:
    def __init__(self):
        self.tasksList = []

    '''Loads the file (tasks.txt) and appends each line into tasksList line-by-line'''
    def loadFile(self, filename):
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                task = line.strip()
                if task:
                    self.tasksList.append(task)

    '''Saves each task from the tasksList into the file (tasks.txt) line-by-line'''
    def saveFile(self, filename):
        with open(filename, "w", encoding='utf-8') as f:
            for task in self.tasksList:
                f.write(task + "\n")

    '''Adds a new task to the tasksList. Ensures entered task data cannot be an empty string. Variable inputTask is used
     to append user input to the tasksList as long as input is non-empty'''
    def addTask(self):
        inputTask = input("Enter task: ")
        if inputTask != "":
            self.tasksList.append(inputTask)
            print("Task successfully added.")
        else:
            print("Task data cannot be empty")

    '''Allows the user to update task information (the user may overwrite the selected task to add details, a date,
    or a new task entirely). Variable taskNumToUpdate is used to ensure user input is valid, and to update the existing 
    index (taskNumToUpdate - 1). If valid, the variable newTask is used to replace the existing task in the tasksList'''
    def updateTask(self):
        if not self.tasksList:                # Ensures the taskList is non-empty
            print("No items are in the list.")
        else:
            self.listTasks()
            taskNumToUpdate = input("Enter task number to update: ")
            if taskNumToUpdate.isdigit():            # Ensures the taskNumberToUpdate is a number
                taskNumToUpdate = int(taskNumToUpdate)
                if taskNumToUpdate <= len(self.tasksList) and taskNumToUpdate > 0:        # Ensures the taskNumToUpdate is a valid task number
                    newTask = input("Enter updated task information: ")
                    if newTask != "":
                        self.tasksList[taskNumToUpdate - 1] = newTask
                        print("Task successfully updated.")
                    else:
                        print("Updated task data cannot be empty.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    '''Allows the user to mark a task as complete. The task will remain in the list with a checkmark next to it.
    Variable taskNumToMarkComplete is used to ensure user input is valid, and to add a checkmark next to the task
    using the index (taskNumToMarkComplete - 1).'''
    def markTaskCompleted(self):
        if not self.tasksList:          # Ensures the taskList is non-empty
            print("No items are in the list.")
        else:
            self.listTasks()
            taskNumToMarkComplete = input("Enter task # to mark complete: ")
            if taskNumToMarkComplete.isdigit():         # Ensures the taskNumToMarkComplete is a number
                taskNumToMarkComplete = int(taskNumToMarkComplete)
                if taskNumToMarkComplete <= len(self.tasksList) and taskNumToMarkComplete > 0:          # Ensures the taskNumToMark Complete is a valid task number
                    self.tasksList[taskNumToMarkComplete - 1] = self.tasksList[taskNumToMarkComplete - 1] + " ✅"
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    '''Lists all tasks from the tasksList and then the user selects the task number they want to delete. Variable
    taskToDelete is used to ensure user input is valid, and to delete the task item using the index (taskToDelete - 1).'''
    def deleteTask(self):
        if not self.tasksList:              # Ensures the taskList is non-empty
            print("No items are in the list.")
        else:
            self.listTasks()
            taskToDelete = input("Enter task # to delete: ")
            if taskToDelete.isdigit():              # Ensures the taskToDelete is a number
                taskToDelete = int(taskToDelete)
                if taskToDelete <= len(self.tasksList) and taskToDelete > 0:             # Ensures the taskToDelete is a valid task number
                    self.tasksList.pop(taskToDelete - 1)
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    '''Lists all tasks from the tasksList as long as the tasksList is non-empty. Each task is on it's own line with 
    it's own number.'''
    def listTasks(self):
        if self.tasksList:          # Ensures tasksList is non-empty
            for index, task in enumerate(self.tasksList):
                print(f"{index + 1}. {task}")
        else:
            print("No data has been added to the list.")

def main():
    todo = toDoListApp()

    print("Welcome to the To-Do List Application!")

    '''Calls the loadFile() method which loads a file called tasks.txt. If there is no file to load, outputs that we
    are starting with a new list.'''
    try:
        todo.loadFile("tasks.txt")
    except FileNotFoundError:
        print("Task data not found. Starting with an empty list.")

    '''Main menu of the application. Numbers 1-6 entered by the user corresponds to the listed menu options. Any other
    input will not be accepted.'''
    while True:
        print("\nPlease choose from the following options:")
        print("1. Add a new task.")
        print("2. Update an existing task.")
        print("3. Mark a task completed.")
        print("4. Delete an existing task.")
        print("5. List all tasks.")
        print("6. Quit.")

        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            todo.addTask()

        elif userChoice == "2":
            todo.updateTask()

        elif userChoice == "3":
            todo.markTaskCompleted()

        elif userChoice == "4":
            todo.deleteTask()

        elif userChoice == "5":
            todo.listTasks()

        elif userChoice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    todo.saveFile("tasks.txt")

if __name__ == "__main__":
    main()
