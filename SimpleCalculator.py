import tkinter as tk

def on_button_click(button_value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(button_value))

def clear_entry():
    entry_var.set("")

def backspace():
    current_text = entry_var.get()
    entry_var.set(current_text[:-1])

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget to display the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Define the buttons and their positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place the buttons in the grid
for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 14),
                       command=lambda text=button_text: on_button_click(text) if text != "=" else calculate_result())
    button.grid(row=row, column=col, sticky="nsew")

# Create additional buttons
backspace_button = tk.Button(root, text="←", padx=20, pady=20, font=("Arial", 14), command=backspace)
backspace_button.grid(row=3, column=4,rowspan=2,sticky="nsew")

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 14), command=clear_entry)
clear_button.grid(row=1, column=4,rowspan=2, sticky="nsew")

# Configure row and column weights to make the entry and buttons expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
