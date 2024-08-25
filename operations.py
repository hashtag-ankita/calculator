from tkinter import *
from ui import *

# Function to add numbers to the input box
def button_click(expression, number):
    current = expression.get()
    expression.delete(0, END)
    expression.insert(0, str(current) + str(number))

def button_delete(expression):
    expression.delete(0, END)

def button_backspace(expression):
    current = expression.get()
    expression.delete(len(current)-1, END)

def button_add(expression):
    first_number = expression.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    expression.delete(0, END)

def button_subtract(expression):
    first_number = expression.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    expression.delete(0, END)

def button_multiply(expression):
    first_number = expression.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    expression.delete(0, END)

def button_divide(expression):
    first_number = expression.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    expression.delete(0, END)

def change_sign(expression):
    first_number = expression.get()
    expression.delete(0, END)
    expression.insert(0, float(first_number) * -1)

def button_exponent(expression):
    first_number = expression.get()
    global f_num
    global math
    math = "exponent"
    f_num = float(first_number)
    expression.delete(0, END)

def button_equal(expression):
    second_number = expression.get()
    expression.delete(0, END)
    
    if math == "addition":
        result = f_num + float(second_number)
    elif math == "subtraction":
        result = f_num - float(second_number)
    elif math == "multiplication":
        result = f_num * float(second_number)
    elif math == "division":
        result = f_num / float(second_number)
    elif math == "exponent":
        result = f_num ** float(second_number)

    expression.insert(0, result)
