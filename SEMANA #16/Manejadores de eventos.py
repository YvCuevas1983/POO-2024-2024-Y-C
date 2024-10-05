import tkinter as tk
from tkinter import messagebox, Listbox, END

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones para la gestión de tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.toggle_task_completion)
        self.complete_button.pack(side=tk.LEFT, padx=(20, 10), pady=5)

        self.uncomplete_button = tk.Button(root, text="Desmarcar Tarea", command=self.toggle_task_completion)
        self.uncomplete_button.pack(side=tk.LEFT, padx=(10, 10), pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=(10, 20), pady=5)

        # Lista para mostrar tareas
        self.tasks_listbox = Listbox(root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

        # Eventos adicionales
        self.tasks_listbox.bind('<Double-1>', lambda event: self.toggle_task_completion())

        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task_text = self.task_entry.get().strip()  # Obtiene el texto de entrada
        if task_text:
            self.tasks.append(task_text)  # Agrega la tarea a la lista
            self.update_tasks_list()  # Actualiza la vista de tareas
            self.task_entry.delete(0, END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")  # Advertencia si está vacío

    def toggle_task_completion(self):
        """Marca o desmarca una tarea como completada."""
        try:
            selected_index = self.tasks_listbox.curselection()[0]  # Obtiene la tarea seleccionada
            task_text = self.tasks[selected_index]  # Obtiene el texto de la tarea seleccionada

            # Cambia el estado de completada
            if task_text.startswith("[✓] "):
                self.tasks[selected_index] = task_text[4:]  # Desmarcar
            else:
                self.tasks[selected_index] = "[✓] " + task_text  # Marcar como completada

            self.update_tasks_list()  # Actualiza la vista de tareas
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")  # Advertencia si no hay selección

    def delete_task(self):
        """Elimina una tarea seleccionada."""
        try:
            selected_index = self.tasks_listbox.curselection()[0]  # Obtiene la tarea seleccionada
            del self.tasks[selected_index]  # Elimina la tarea
            self.update_tasks_list()  # Actualiza la vista de tareas
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")  # Advertencia si no hay selección

    def update_tasks_list(self):
        """Actualiza la vista de la lista de tareas."""
        self.tasks_listbox.delete(0, END)  # Limpia la lista actual
        for task in self.tasks:
            self.tasks_listbox.insert(END, task)  # Inserta cada tarea en la lista

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManager(root)  # Inicia la aplicación
    root.mainloop()  # Mantiene la ventana abierta