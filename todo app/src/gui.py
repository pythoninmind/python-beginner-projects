import tkinter as tk
from tkinter import ttk, messagebox
from storage import load_tasks, save_tasks


class TodoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To‑Do App")
        self.root.geometry("600x400")

        self.tasks = load_tasks()

        # --- UI Elements ---
        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # List of Tasks
        self.tree = ttk.Treeview(self.frame, columns=("category", "priority", "deadline"), show="headings")
        self.tree.heading("category", text="Category")
        self.tree.heading("priority", text="Priority")
        self.tree.heading("deadline", text="Deadline")
        self.tree.pack(fill="both", expand=True)

        self.load_tree()

        # Buttons
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Add Task", command=self.add_task_window).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Manage Tasks", command=self.edit_task_window).grid(row=0, column=2, padx=5)

    # --- load tasks into GUI ---
    def load_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for t in self.tasks:
            self.tree.insert("", "end", iid=t["id"], values=(t["category"], t["priority"], t["deadline"]))

    # --- add Tasks ---
    def add_task_window(self):
        win = tk.Toplevel(self.root)
        win.title("New Task")

        tk.Label(win, text="Title").pack()
        title_entry = tk.Entry(win)
        title_entry.pack()

        tk.Label(win, text="Category").pack()
        category_entry = tk.Entry(win)
        category_entry.pack()

        tk.Label(win, text="Priority (Low/Medium/High)").pack()
        priority_entry = tk.Entry(win)
        priority_entry.pack()

        tk.Label(win, text="Deadline (YYYY-MM-DD)").pack()
        deadline_entry = tk.Entry(win)
        deadline_entry.pack()

        def save_new():
            new_task = {
                "id": len(self.tasks) + 1,
                "title": title_entry.get(),
                "category": category_entry.get(),
                "priority": priority_entry.get(),
                "deadline": deadline_entry.get(),
                "done": False
            }
            self.tasks.append(new_task)
            save_tasks(self.tasks)
            self.load_tree()
            win.destroy()

        ttk.Button(win, text="Save", command=save_new).pack(pady=10)

    # --- Delete Task ---
    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please choose a Task.")
            return

        task_id = int(selected[0])
        self.tasks = [t for t in self.tasks if t["id"] != task_id]

        save_tasks(self.tasks)
        self.load_tree()

    # --- manage Tasks ---
    def edit_task_window(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Fehler", "Please choose a Task.")
            return

        task_id = int(selected[0])
        task = next(t for t in self.tasks if t["id"] == task_id)

        win = tk.Toplevel(self.root)
        win.title("Manage Tasks")

        tk.Label(win, text="Titel").pack()
        title_entry = tk.Entry(win)
        title_entry.insert(0, task["title"])
        title_entry.pack()

        tk.Label(win, text="Category").pack()
        category_entry = tk.Entry(win)
        category_entry.insert(0, task["category"])
        category_entry.pack()

        tk.Label(win, text="Priority").pack()
        priority_entry = tk.Entry(win)
        priority_entry.insert(0, task["priority"])
        priority_entry.pack()

        tk.Label(win, text="Deadline").pack()
        deadline_entry = tk.Entry(win)
        deadline_entry.insert(0, task["deadline"])
        deadline_entry.pack()

        def save_edit():
            task["title"] = title_entry.get()
            task["category"] = category_entry.get()
            task["priority"] = priority_entry.get()
            task["deadline"] = deadline_entry.get()

            save_tasks(self.tasks)
            self.load_tree()
            win.destroy()

        ttk.Button(win, text="Save", command=save_edit).pack(pady=10)


def start_gui():
    root = tk.Tk()
    app = TodoGUI(root)
    root.mainloop()
