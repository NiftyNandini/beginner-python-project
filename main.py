import tkinter as tk

# Function to update expression in the text entry box
def update_expression(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to evaluate the final expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the text entry box
def clear_entry():
    entry.delete(0, tk.END)

# Function to create the main calculator window
def create_calculator():
    root = tk.Tk()
    root.title("Simple Calculator")
    
    # Set a fixed window size and disable resizing
    root.geometry("400x500")
    root.resizable(False, False)

    # Configure the entry box
    global entry
    entry = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    # List of buttons in the calculator
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    # Create and arrange buttons in the grid
    for (text, row, col) in buttons:
        if text == '=':
            tk.Button(root, text=text, padx=20, pady=20, bd=8, fg='black', bg='lightgreen',
                      command=evaluate_expression).grid(row=row, column=col, sticky="nsew")
        else:
            tk.Button(root, text=text, padx=20, pady=20, bd=8, fg='black', bg='lightgray',
                      command=lambda b=text: update_expression(b)).grid(row=row, column=col, sticky="nsew")

    # Create a clear button that spans across the bottom row
    tk.Button(root, text='C', padx=20, pady=20, bd=8, fg='black', bg='lightcoral',
              command=clear_entry).grid(row=5, column=0, columnspan=4, sticky="nsew")

    # Disable resizing the rows and columns to keep the layout fixed
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

# Run the calculator
create_calculator()
