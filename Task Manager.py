import csv
from collections import deque

class Task:
    #Initializing a task with title, description, and a default status of 'Pending'
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'Pending'  # Default status for a new task

    #Mark a task as complete by updating its status
    def mark_complete(self):
        self.status = 'Complete'

class TaskManager:
    def __init__(self):
        #Using a deque to manage tasks
        self.tasks = deque()

    #Add a new task to the queue
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    #Mark the first task in the queue as complete
    def complete_task(self):
        if self.tasks:
            task = self.tasks.popleft()  #Removes and returns the first task
            task.mark_complete()
            print(f"Task '{task.title}' marked as complete.")
        else:
            print("No tasks to complete.")

    #Display all pending tasks
    def display_pending_tasks(self):
        print("\nPending Tasks:")
        pending_tasks = [task for task in self.tasks if task.status == 'Pending']
        if pending_tasks:
            for i, task in enumerate(pending_tasks, start=1):
                print(f"{i}. Title: {task.title}, Description: {task.description}, Status: {task.status}")
        else:
            print("No pending tasks.")

    #Save all tasks to a CSV file
    def save_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Description', 'Status'])  #Header for the CSV file
                for task in self.tasks:
                    writer.writerow([task.title, task.description, task.status])
            print(f"Tasks saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

#Example
task_manager = TaskManager()

#Adding tasks
task_manager.add_task("Complete Assignment", "Finish the Python assignment by tonight")
task_manager.add_task("Prepare Presentation", "Prepare slides for the project presentation")
task_manager.add_task("Email Client", "Send updated project report to the client")

#Display pending tasks
task_manager.display_pending_tasks()

#Complete a task
task_manager.complete_task()

#Display pending tasks again
task_manager.display_pending_tasks()

#Save tasks to a CSV file
task_manager.save_to_csv("tasks.csv")
