import tkinter as tk

# ========== Configurations ==========
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "white"

# ========== State ==========
A = None
B = None
operator = None
new_input = True

# ========== Functions ==========
def clear_all():
    global A, B, operator, new_input
    A = None
    B = None
    operator = None
    new_input = True
    label["text"] = "0"

def remove_zero_decimal(num):
    return str(int(num)) if num == int(num) else str(num)

def button_clicked(value):
    global A, B, operator, new_input

    # --- Operator Buttons ---
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                try:
                    numA = float(A)
                    numB = float(B)
                    result = 0
                    if operator == "+":
                        result = numA + numB
                    elif operator == "-":
                        result = numA - numB
                    elif operator == "×":
                        result = numA * numB
                    elif operator == "÷":
                        if numB == 0:
                            raise ZeroDivisionError
                        result = numA / numB
                    label["text"] = remove_zero_decimal(result)
                except:
                    label["text"] = "Error"
                A = None
                operator = None
                B = None
                new_input = True
        else:
            if not new_input:
                A = label["text"]
            operator = value
            new_input = True

    # --- Top Buttons ---
    elif value in top_symbols:
        try:
            current = float(label["text"])
            if value == "AC":
                clear_all()
            elif value == "+/-":
                label["text"] = remove_zero_decimal(-current)
            elif value == "%":
                label["text"] = remove_zero_decimal(current / 100)
            elif value == "√":
                if current >= 0:
                    label["text"] = remove_zero_decimal(current ** 0.5)
                else:
                    label["text"] = "Error"
            new_input = True
        except:
            label["text"] = "Error"
            new_input = True

    # --- Number / Decimal ---
    else:
        if new_input:
            if value == ".":
                label["text"] = "0."
            else:
                label["text"] = value
            new_input = False
        else:
            if value == "." and "." in label["text"]:
                return
            label["text"] += value

# ========== GUI Setup ==========
root = tk.Tk()
root.title("macOS Calculator")
root.resizable(False, False)
root.configure(bg=color_black)

frame = tk.Frame(root, bg=color_black)
frame.pack()

label = tk.Label(frame, text="0", font=("Arial", 45), background=color_black,
                 foreground=color_white, anchor="e", width=17, padx=10)
label.grid(row=0, column=0, columnspan=4, sticky="we")

# ========== Buttons ==========
for r, row in enumerate(button_values):
    for c, char in enumerate(row):
        btn = tk.Button(
            frame,
            text=char,
            font=("Arial", 24),
            width=5,
            height=2,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda val=char: button_clicked(val)
        )

        # --- Colors ---
        if char in top_symbols:
            btn.config(bg=color_light_gray, fg=color_black)
        elif char in right_symbols:
            btn.config(bg=color_orange, fg=color_white)
        else:
            btn.config(bg=color_dark_grey, fg=color_white)

        btn.grid(row=r + 1, column=c, padx=1, pady=1, sticky="nsew")

# Make grid expand
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

# ========== Center the Window ==========
root.update()
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f"{w}x{h}+{x}+{y}")

# ========== Start ==========
root.mainloop()
