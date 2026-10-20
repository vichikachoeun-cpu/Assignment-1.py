# Custom Exception
class TaskAlreadyDoneError(Exception):
    pass


# Base Class Task
class Task:

    # Constructor
    def init(self, title, task_id, priority):
        self.title = title
        self.task_id = task_id
        self.priority = priority
        self.__is_done = False

    # Check if task is completed
    def is_done(self):
        return self.__is_done

    # Mark task as done
    def mark_done(self):
        if self.__is_done:
            raise TaskAlreadyDoneError("This task is already completed.")
        self.__is_done = True

    # Mark task as not done
    def mark_undone(self):
        self.__is_done = False

    # Get priority label
    def get_priority_label(self):
        if self.priority == 1:
            return "High"
        elif self.priority == 2:
            return "Medium"
        else:
            return "Low"

    # Display task information
    def display_info(self):
        status = "Done" if self.__is_done else "Pending"

        print("Task ID:", self.task_id)
        print("Title:", self.title)
        print("Priority:", self.get_priority_label())
        print("Status:", status)


# WorkTask Class
class WorkTask(Task):

    # Constructor
    def init(self, title, task_id, priority, deadline):
        super().init(title, task_id, priority)
        self.deadline = deadline

    # Override display_info()
    def display_info(self):
        super().display_info()
        print("Deadline:", self.deadline)


# PersonalTask Class
class PersonalTask(Task):

    # Constructor
    def init(self, title, task_id, priority, category):
        super().init(title, task_id, priority)
        self.category = category

    # Override priority label
    def get_priority_label(self):
        if self.priority == 1:
            return "Important"
        elif self.priority == 2:
            return "Medium"
        else:
            return "Low"

    # Override display_info()
    def display_info(self):
        super().display_info()
        print("Category:", self.category)


# TodoList Class
class TodoList:

    # Constructor
    def init(self):
        self.tasks = {}

    # Add task
    def add_task(self, task):

        if task.task_id in self.tasks:
            raise ValueError("Task ID already exists.")

        self.tasks[task.task_id] = task

    # Find task
    def find_task(self, task_id):
        return self.tasks.get(task_id)

    # Remove task
    def remove_task(self, task_id):

        if task_id not in self.tasks:
            raise ValueError("Task ID does not exist.")

        del self.tasks[task_id]

    # Complete task
    def complete_task(self, task_id):

        task = self.find_task(task_id)

        if task is None:
            raise ValueError("Task ID does not exist.")

        task.mark_done()

    # Show all tasks
    def show_all_tasks(self):

        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        for task in self.tasks.values():
            print("------------------")
            task.display_info()

    # Show pending tasks
    def show_pending_tasks(self):

        found = False

        for task in self.tasks.values():
            if not task.is_done():
                print("------------------")
                task.display_info()
                found = True

        if not found:
            print("No pending tasks.")

    # Show completed tasks
    def show_completed_tasks(self):

        found = False

        for task in self.tasks.values():
            if task.is_done():
                print("------------------")
                task.display_info()
                found = True

        if not found:
            print("No completed tasks.")

    # Get tasks by priority
    def get_tasks_by_priority(self, priority):

        found = False

        for task in self.tasks.values():
            if task.priority == priority:
                print("------------------")
                task.display_info()
                found = True

        if not found:
            print("No tasks with that priority .")

    # Show progress
    def get_progress(self):

        total = len(self.tasks)

        if total == 0:
            print("No tasks in the list.")
            return

        completed = 0

        for task in self.tasks.values():
            if task.is_done():
                completed += 1

        percentage = (completed / total) * 100

        print("\n--- Progress Report ---")
        print("Completed:", completed, "of", total, "tasks")
        print("Progress:", round(percentage, 2), "%")


# Create TodoList Object
todo = TodoList()

# Main Program
while True:

    print("\n===== To-Do List Menu =====")
    print("1. Add work task")
    print("2. Add personal task")
    print("3. Complete a task")
    print("4. Show all tasks")
    print("5. Show pending tasks")
    print("6. Show completed tasks")
    print("7. Show tasks by priority")
    print("8. Show progress")
    print("9. Remove task")
    print("10. Exit")

    try:

        choice = int(input("Enter your choice: "))

        # Add Work Task
        if choice == 1:

            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")

            priority = int(input("Enter Priority (1-High, 2-Medium, 3-Low): "))

            if priority not in [1, 2, 3]:
                raise ValueError("Priority must be 1, 2, or 3.")

            deadline = input("Enter Deadline: ")

            task = WorkTask(title, task_id, priority, deadline)

            todo.add_task(task)

            print("Work task added successfully.")

        # Add Personal Task
        elif choice == 2:

            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")

            priority = int(input("Enter Priority (1-High, 2-Medium, 3-Low): "))

            if priority not in [1, 2, 3]:
                raise ValueError("Priority must be 1, 2, or 3.")

            category = input("Enter Category: ")

            task = PersonalTask(title, task_id, priority, category)

            todo.add_task(task)

            print("Personal task added successfully.")

        # Complete Task
        elif choice == 3:

            task_id = input("Enter Task ID: ")

            todo.complete_task(task_id)

            print("Task marked as completed.")

        # Show All Tasks
        elif choice == 4:
            todo.show_all_tasks()

        # Show Pending Tasks
        elif choice == 5:
            todo.show_pending_tasks()

        # Show Completed Tasks
        elif choice == 6:
            todo.show_completed_tasks()

        # Show Tasks By Priority
        elif choice == 7:

            priority = int(input("Enter Priority (1,2,3): "))

            if priority not in [1, 2, 3]:
                raise ValueError("Priority must be 1, 2, or 3.")

            todo.get_tasks_by_priority(priority)

        # Show Progress
        elif choice == 8:
            todo.get_progress()

        # Remove Task
        elif choice == 9:

            task_id = input("Enter Task ID: ")

            todo.remove_task(task_id)

            print("Task removed successfully.")

        # Exit
        elif choice == 10:

            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    # Error handling
    except ValueError as e:
        print("Error:", e)

    except TaskAlreadyDoneError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)