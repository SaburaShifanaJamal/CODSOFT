import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
FILE_NAME = 'tasks.json'
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []
def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)
def add_task():
    description = simpledialog.askstring("Add Task", "Enter the task description:")
    if description:
        tasks.append({
            'description': description,
            'is_done': False
        })
        save_data(tasks)
        update_listbox()
def edit_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Edit Task", "No task selected.")
        return
    index = selected_index[0]
    new_description = simpledialog.askstring("Edit Task", "Enter the new task description:")
    if new_description:
        tasks[index]['description'] = new_description
        save_data(tasks)
        update_listbox()
def remove_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Remove Task", "No task selected.")
        return
    index = selected_index[0]
    tasks.pop(index)
    save_data(tasks)
    update_listbox()
def mark_as_done():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Mark as Done", "No task selected.")
        return
    index = selected_index[0]
    tasks[index]['is_done'] = True
    save_data(tasks)
    update_listbox()
def show_done_tasks():
    completed_tasks = [task for task in tasks if task['is_done']]
    if not completed_tasks:
        messagebox.showinfo("Completed Tasks", "No tasks have been completed.")
        return
    completed_text = '\n'.join(task['description'] for task in completed_tasks)
    messagebox.showinfo("Completed Tasks", completed_text)
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "DONE" if task['is_done'] else "PENDING"
        task_listbox.insert(tk.END, f"{task['description']} [{status}]")
root = tk.Tk()
root.title("Task Manager")
tasks = load_data()
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)
btn_edit = tk.Button(root, text="Edit Task", command=edit_task)
btn_edit.pack(pady=5)
btn_remove = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove.pack(pady=5)
btn_done = tk.Button(root, text="Mark as Done", command=mark_as_done)
btn_done.pack(pady=5)
btn_show_done = tk.Button(root, text="Show Completed Tasks", command=show_done_tasks)
btn_show_done.pack(pady=5)
task_listbox = tk.Listbox(root, width=60, height=15)
task_listbox.pack(pady=10)
update_listbox()
root.mainloop()
