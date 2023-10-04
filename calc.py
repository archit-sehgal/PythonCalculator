import tkinter as tk

def create_button(parent, text, row, column, command=None):
    button = tk.Button(parent, text=text, bg=btnColor, width=7,
                       height=3, font=font_style, fg=text_color, command=command)
    button.grid(row=row, column=column)
    return button

def clear_display():
    display.delete(0, "end")

def append_to_display(label):
    current_text = display.get()
    display.delete(0, "end")
    display.insert("end", current_text + label)

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
    except Exception as e:
        result = "Error"
    display.delete(0, "end")
    display.insert("end", result)

a = tk.Tk()
a.title("Calculator")
a.geometry("285x343")

btnColor = "red"
font_style = ("Helvetica", 10, "bold")
text_color = "#fff"

display = tk.Entry(a)
display.grid(columnspan=4, ipadx=80, ipady=10)

buttons_data = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("+", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("-", 2, 3),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
    ("*", 3, 3),
    ("0", 4, 0),
    ("clear", 4, 1),
    ("=", 4, 2),
    ("/", 4, 3),
    (".", 5, 0)
]

buttons = []

for label, row, column in buttons_data:
    if label == "clear":
        button = create_button(a, label, row, column, command=clear_display)
    elif label == "=":
        button = create_button(a, label, row, column, command=calculate)
    else:
        button = create_button(a, label, row, column, command=lambda label=label: append_to_display(label))
    buttons.append(button)

a.mainloop()
