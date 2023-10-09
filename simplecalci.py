import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an Entry widget for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create a StringVar to store the result
result = tk.StringVar()
result.set("")

# Create a Label to display the result
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=1, column=0, columnspan=4)

# Define the buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 2
col = 0

for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20,
              command=lambda t=button_text: entry.insert(tk.END, t) if t != '=' else evaluate_expression()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter main loop
root.mainloop()