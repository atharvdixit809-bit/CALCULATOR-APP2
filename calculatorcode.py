import tkinter as tk
import math


# -----------------------------
# Calculator settings
# -----------------------------
angle_mode = "DEG"


# -----------------------------
# Main window
# -----------------------------
root = tk.Tk()
root.title("Advanced PC Calculator")
root.geometry("1080x720")
root.configure(bg="#0e172b")
root.resizable(True, True)


# -----------------------------
# Colors
# -----------------------------
BG = "#0e172b"
PANEL = "#1e2a3d"
DISPLAY_BG = "#07101e"
NUMBER = "#304056"
BLUE = "#2160dc"
GREEN = "#079c6b"
RED = "#f34343"
ORANGE = "#ffad0b"
TEXT = "white"


# -----------------------------
# Functions
# -----------------------------
def insert(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])


def calculate():
    try:
        expression = display.get()

        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        expression = expression.replace("^", "**")
        expression = expression.replace("mod", "%")

        result = eval(
            expression,
            {
                "__builtins__": {},
                "sqrt": math.sqrt
            }
        )

        if isinstance(result, float):
            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 12)

        clear()
        display.insert(0, str(result))

    except:
        clear()
        display.insert(0, "Error")


def trig(function):
    try:
        value = float(display.get())

        if angle_mode == "DEG":
            value = math.radians(value)

        if function == "sin":
            result = math.sin(value)

        elif function == "cos":
            result = math.cos(value)

        elif function == "tan":
            result = math.tan(value)

        clear()
        display.insert(0, str(round(result, 12)))

    except:
        clear()
        display.insert(0, "Error")


def logarithm():
    try:
        value = float(display.get())
        result = math.log10(value)

        clear()
        display.insert(0, str(round(result, 12)))

    except:
        clear()
        display.insert(0, "Error")


def natural_log():
    try:
        value = float(display.get())
        result = math.log(value)

        clear()
        display.insert(0, str(round(result, 12)))

    except:
        clear()
        display.insert(0, "Error")


def square_root():
    try:
        value = float(display.get())
        result = math.sqrt(value)

        clear()
        display.insert(0, str(round(result, 12)))

    except:
        clear()
        display.insert(0, "Error")


def power():
    insert("^")


def set_angle(mode):
    global angle_mode
    angle_mode = mode


def keyboard(event):
    key = event.keysym

    if event.char in "0123456789.+-*/()%":
        insert(event.char)

    elif event.char == "^":
        insert("^")

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()


# -----------------------------
# Theme changing
# -----------------------------
def change_theme(color):
    equals_button.config(bg=color)

    for button in green_buttons:
        button.config(bg=color)


# -----------------------------
# Header
# -----------------------------
header = tk.Frame(root, bg=PANEL)
header.pack(fill="x", padx=20, pady=(15, 0))

title = tk.Label(
    header,
    text="Advanced PC Calculator",
    font=("Arial", 20, "bold"),
    bg=PANEL,
    fg=TEXT
)

title.pack(side="left", padx=10, pady=12)


# -----------------------------
# Color buttons
# -----------------------------
colors_frame = tk.Frame(header, bg=PANEL)
colors_frame.pack(side="right", padx=10)


colors = [
    "#29a9df",
    "#2db0df",
    "#27c993",
    "#ef6c80",
    "#7c8ee8",
    "#8de51e",
    "#c59bea",
    "#929aa8",
    "#f07070",
    "#74c1e7",
    "#c43ee1",
    "#ffb719"
]


# -----------------------------
# Main area
# -----------------------------
main = tk.Frame(root, bg=PANEL)
main.pack(fill="both", expand=True, padx=20, pady=(0, 15))


# -----------------------------
# Tabs
# -----------------------------
tabs = tk.Frame(main, bg=PANEL)
tabs.pack(anchor="w", padx=10, pady=10)


def tab_button(text):
    return tk.Button(
        tabs,
        text=text,
        bg=NUMBER,
        fg=TEXT,
        activebackground="#25a9e0",
        activeforeground="black",
        relief="flat",
        padx=15,
        pady=8,
        font=("Arial", 10)
    )


calculator_tab = tab_button("Calculator")
length_tab = tab_button("Length")
shape2d_tab = tab_button("2D Shapes")
shape3d_tab = tab_button("3D Shapes")

calculator_tab.config(bg="#25a9e0", fg="black")

calculator_tab.pack(side="left", padx=3)
length_tab.pack(side="left", padx=3)
shape2d_tab.pack(side="left", padx=3)
shape3d_tab.pack(side="left", padx=3)


# -----------------------------
# Content
# -----------------------------
content = tk.Frame(main, bg=PANEL)
content.pack(fill="both", expand=True, padx=10)


# -----------------------------
# Calculator side
# -----------------------------
calculator_frame = tk.Frame(content, bg=PANEL)
calculator_frame.pack(side="left", fill="both", expand=True)


# Display
display = tk.Entry(
    calculator_frame,
    bg=DISPLAY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    font=("Arial", 25),
    justify="right",
    relief="flat"
)

display.pack(fill="x", pady=(0, 5), ipady=8)


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(calculator_frame, bg=PANEL)
button_frame.pack(fill="both", expand=True)


green_buttons = []


def make_button(text, command, color=NUMBER):
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        bg=color,
        fg=TEXT,
        activebackground="#50627a",
        activeforeground=TEXT,
        relief="flat",
        font=("Arial", 12),
        bd=0
    )

    return button


# Scientific buttons
buttons = [
    ("sin", lambda: trig("sin"), GREEN),
    ("cos", lambda: trig("cos"), GREEN),
    ("tan", lambda: trig("tan"), GREEN),
    ("π", lambda: insert("π"), GREEN),
    ("AC", clear, RED),

    ("log", logarithm, GREEN),
    ("ln", natural_log, GREEN),
    ("√", square_root, GREEN),
    ("xʸ", power, GREEN),
    ("⌫", backspace, RED),

    ("7", lambda: insert("7"), NUMBER),
    ("8", lambda: insert("8"), NUMBER),
    ("9", lambda: insert("9"), NUMBER),
    ("÷", lambda: insert("/"), BLUE),
    ("mod", lambda: insert("%"), BLUE),

    ("4", lambda: insert("4"), NUMBER),
    ("5", lambda: insert("5"), NUMBER),
    ("6", lambda: insert("6"), NUMBER),
    ("×", lambda: insert("*"), BLUE),
    ("^", lambda: insert("^"), BLUE),

    ("1", lambda: insert("1"), NUMBER),
    ("2", lambda: insert("2"), NUMBER),
    ("3", lambda: insert("3"), NUMBER),
    ("−", lambda: insert("-"), BLUE),
    ("(", lambda: insert("("), BLUE),

    ("0", lambda: insert("0"), NUMBER),
    (".", lambda: insert("."), NUMBER),
    ("e", lambda: insert("e"), NUMBER),
    ("+", lambda: insert("+"), BLUE),
    (")", lambda: insert(")"), BLUE),
]


for index, (text, command, color) in enumerate(buttons):

    row = index // 5
    column = index % 5

    button = make_button(text, command, color)

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    if color == GREEN:
        green_buttons.append(button)


for i in range(5):
    button_frame.columnconfigure(i, weight=1)

for i in range(6):
    button_frame.rowconfigure(i, weight=1)


# -----------------------------
# Degree / Radian
# -----------------------------
angle_frame = tk.Frame(calculator_frame, bg=PANEL)
angle_frame.pack(fill="x", pady=5)


deg_button = tk.Button(
    angle_frame,
    text="Deg",
    command=lambda: set_angle("DEG"),
    bg=GREEN,
    fg=TEXT,
    relief="flat",
    font=("Arial", 11)
)

rad_button = tk.Button(
    angle_frame,
    text="Rad",
    command=lambda: set_angle("RAD"),
    bg=GREEN,
    fg=TEXT,
    relief="flat",
    font=("Arial", 11)
)

deg_button.pack(side="left", fill="x", expand=True, padx=3, ipady=7)
rad_button.pack(side="left", fill="x", expand=True, padx=3, ipady=7)


# -----------------------------
# Equals
# -----------------------------
equals_button = tk.Button(
    calculator_frame,
    text="=",
    command=calculate,
    bg=ORANGE,
    fg="black",
    relief="flat",
    font=("Arial", 14, "bold")
)

equals_button.pack(
    anchor="w",
    pady=5,
    ipadx=35,
    ipady=5
)


# -----------------------------
# Help section
# -----------------------------
help_frame = tk.Frame(
    content,
    bg=PANEL,
    width=330
)

help_frame.pack(side="right", fill="both", padx=(15, 10))
help_frame.pack_propagate(False)


tk.Label(
    help_frame,
    text="How to use",
    bg=PANEL,
    fg=TEXT,
    font=("Arial", 16, "bold")
).pack(anchor="nw", pady=5)


instructions = """
• Type numbers and operators using
  buttons or your keyboard.

• sin, cos and tan work in degrees
  or radians.

• Use parentheses for complex
  expressions.

Examples:

  sin(30) in Deg mode → 0.5

  2^10 → 1024

  π × 5^2 → area of circle
  radius 5
"""


tk.Label(
    help_frame,
    text=instructions,
    bg=PANEL,
    fg="#d8e0eb",
    justify="left",
    anchor="nw",
    font=("Arial", 11),
    wraplength=320
).pack(fill="both", expand=True)


# -----------------------------
# Color buttons
# -----------------------------
for color in colors:

    button = tk.Button(
        colors_frame,
        bg=color,
        width=2,
        height=1,
        relief="flat",
        command=lambda c=color: change_theme(c)
    )

    button.pack(side="left", padx=3)


# -----------------------------
# Keyboard
# -----------------------------
root.bind("<Key>", keyboard)


# -----------------------------
# Start application
# -----------------------------
root.mainloop()