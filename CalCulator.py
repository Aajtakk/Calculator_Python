# CalCulator

import tkinter as Tk

calculation = ""

def add_to_calculation(Symbol):
    global calculation
    calculation += str(Symbol)
    text_result.delete(1.0, "end")
    text_result.insert("1.0", calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert("1.0", result)
    except:
        clear_field()
        text_result.insert("1.0", "Error")

        

def clear_field():
    global calculation
    calculation = ""  # Reset calculation
    text_result.delete(1.0, "end")
    
# Function to handle backspace logic
def backspace():
    global calculation
    if calculation:  # Only delete if there is something to delete
        calculation = calculation[:-1]  # Remove the last character
        text_result.delete(1.0, "end")
        text_result.insert("1.0", calculation)
    
root = Tk.Tk()
root.title("Calculator")
root.geometry("300x375")

text_result = Tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = Tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = Tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = Tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = Tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = Tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = Tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = Tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = Tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = Tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = Tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = Tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=7, column=2)
btn_minus = Tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=5, column=3)
btn_mul = Tk.Button(root, text="X", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=6, column=1)
btn_div = Tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=6, column=2)
btn_mod = Tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14))
btn_mod.grid(row=6, column=3)
btn_equal = Tk.Button(root, text="=", command=evaluate_calculation, width=6, font=("Arial", 14))
btn_equal.grid(row=5, column=4)
btn_decimal = Tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=1)
btn_clear = Tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=7, column=1)
btn_backspace = Tk.Button(root, text="\u2190", command=backspace, width=5, font=("Arial", 14))
btn_backspace.grid(row=7, column=3)
root.mainloop()