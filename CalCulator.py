# CalCulator
# Import the Tkinter library for creating GUI applications
import tkinter as Tk

# Global variable to store the current calculation
calculation = ""

# Function to add a symbol (number/operator) to the current calculation
def add_to_calculation(Symbol):
    global calculation  # Access the global calculation variable
    calculation += str(Symbol)  # Append the symbol to the calculation string
    text_result.delete(1.0, "end") # Clear the display field
    text_result.insert("1.0", calculation)  # Update the display with the new calculation

# Function to evaluate the current calculation
    global calculation   # Access the global calculation variable
    try:
        result = str(eval(calculation))  # Evaluate the mathematical expression
        calculation = ""  # Reset the calculation after evaluating
        text_result.delete(1.0, "end")  # Clear the display field
        text_result.insert("1.0", result) # Display the result
    except:
        clear_field()  # Clear the field in case of an error
        text_result.insert("1.0", "Error")  # Display an error message

        
# Function to clear the entire input field
def clear_field():
    global calculation  # Access the global calculation variable
    calculation = ""  # Reset calculation
    text_result.delete(1.0, "end")  # Clear the display field
    
# Function to handle backspace logic
def backspace():
    global calculation  # Access the global calculation variable
    if calculation:  # Only delete if there is something to delete
        calculation = calculation[:-1]  # Remove the last character
        text_result.delete(1.0, "end")  # Clear the display field
        text_result.insert("1.0", calculation)  # Update the display

# Create the main window of the application    
root = Tk.Tk()
root.title("Calculator") # Set the title of the window
root.geometry("300x375") # Set the dimensions of the window

# Create a text widget to display the input and output
text_result = Tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Create buttons for numbers and assign their commands
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

# Create buttons for operations and assign their commands
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

# Create the equal button to evaluate the calculation
btn_equal = Tk.Button(root, text="=", command=evaluate_calculation, width=6, font=("Arial", 14))
btn_equal.grid(row=5, column=4)

# Create the decimal point button
btn_decimal = Tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=1)

# Create the clear button to reset the input field
btn_clear = Tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=7, column=1)

# Create the backspace button to delete the last character
btn_backspace = Tk.Button(root, text="\u2190", command=backspace, width=5, font=("Arial", 14))
btn_backspace.grid(row=7, column=3)

# Start the main event loop to run the application
root.mainloop()
