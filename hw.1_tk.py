import tkinter as tk

def create_repl():
  # Get template name and project name from entry boxes
  template_name = template_entry.get()
  project_name = project_entry.get()

  # Create a new window
  new_window = tk.Toplevel(root)
  new_window.title(project_name)

  # Create a large textbox
  textbox = tk.Text(new_window, wrap=tk.WORD)
  textbox.pack(expand=True, fill="both")

  # Add a subheading
  subheading_label = tk.Label(new_window, text="main.py")
  subheading_label.pack()

  # Create a "Finished" button
  finished_button = tk.Button(new_window, text="Finished", command=new_window.destroy)
  finished_button.pack()

# Create main window
root = tk.Tk()
root.title("Repl Creator")

# Create labels and entry boxes
template_label = tk.Label(root, text="Pick a template:")
template_label.pack()
template_entry = tk.Entry(root)
template_entry.pack()

project_label = tk.Label(root, text="Name your project:")
project_label.pack()
project_entry = tk.Entry(root)
project_entry.pack()

# Create "Create Repl" button
create_button = tk.Button(root, text="Create Repl", command=create_repl)
create_button.pack()

root.mainloop()

root.destroy()