from tkinter import *
from operations import *

# Function to create the UI components
def create_ui(root):
    # Input box for entering the numbers
    expression = Entry(root, width=50, borderwidth=5)
    expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Number buttons
    button_1 = Button(root, text="1", padx=30, pady=10, command=lambda: button_click(expression, 1))
    button_2 = Button(root, text="2", padx=30, pady=10, command=lambda: button_click(expression, 2))
    button_3 = Button(root, text="3", padx=30, pady=10, command=lambda: button_click(expression, 3))
    button_4 = Button(root, text="4", padx=30, pady=10, command=lambda: button_click(expression, 4))
    button_5 = Button(root, text="5", padx=30, pady=10, command=lambda: button_click(expression, 5))
    button_6 = Button(root, text="6", padx=30, pady=10, command=lambda: button_click(expression, 6))
    button_7 = Button(root, text="7", padx=30, pady=10, command=lambda: button_click(expression, 7))
    button_8 = Button(root, text="8", padx=30, pady=10, command=lambda: button_click(expression, 8))
    button_9 = Button(root, text="9", padx=30, pady=10, command=lambda: button_click(expression, 9))
    button_0 = Button(root, text="0", padx=30, pady=10, command=lambda: button_click(expression, 0))

    # Operator buttons
    button_add_op = Button(root, text="+", padx=31, pady=10, command=lambda: button_add(expression))
    button_minus_op = Button(root, text="-", padx=32, pady=10, command=lambda: button_subtract(expression))
    button_multiply_op = Button(root, text="x", padx=32, pady=10, command=lambda: button_multiply(expression))
    button_divide_op = Button(root, text="/", padx=32, pady=10, command=lambda: button_divide(expression))
    button_equal_op = Button(root, text="=", padx=70, pady=10, command=lambda: button_equal(expression))
    button_delete_op = Button(root, text="Del", padx=25, pady=10, command=lambda: button_delete(expression))
    button_changeSign = Button(root, text="+/-", padx=24, pady=10, command=lambda: change_sign(expression))
    button_backspace_op = Button(root, text="<-", padx=26, pady=10, command=lambda: button_backspace(expression))
    button_exponent_op = Button(root, text="^", padx=31, pady=10, command=lambda: button_exponent(expression))

    # Place the buttons on the grid
    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_divide_op.grid(row=4, column=3)

    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_multiply_op.grid(row=3, column=3)

    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_minus_op.grid(row=2, column=3)

    button_0.grid(row=5, column=0)
    button_equal_op.grid(row=5, column=1, columnspan=2)
    button_exponent_op.grid(row=5, column=3)

    button_changeSign.grid(row=1, column=0)
    button_delete_op.grid(row=1, column=1)
    button_backspace_op.grid(row=1, column=2)
    button_add_op.grid(row=1, column=3)
