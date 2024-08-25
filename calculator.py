from tkinter import *

root = Tk()  # create root window
root.title("Calculator")
root.geometry("332x270")

#input box for entering the numbers
expression = Entry(root, width=50, borderwidth=5)
expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#function to add the numbers to the input box
def button_click(number):
    current = expression.get()
    expression.delete(0, END)
    expression.insert(0, str(current) + str(number))

def button_delete():
    expression.delete(0, END)

def button_backspace():
    current = expression.get()
    expression.delete(len(current)-1, END)

def button_add():
    first_number = expression.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    expression.delete(0, END)

def button_subtract():
    first_number = expression.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    expression.delete(0, END)

def button_multiply():
    first_number = expression.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    expression.delete(0, END)

def button_divide():
    first_number = expression.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    expression.delete(0, END)

def change_sign():
    first_number = expression.get()
    expression.delete(0, END)
    expression.insert(0, float(first_number) * -1)

def button_exponent():
    first_number = expression.get()
    global f_num
    global math
    math = "exponent"
    f_num = float(first_number)
    expression.delete(0, END)

def button_equal():
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

#number buttons widgets
button_1 = Button(root, text="1", padx=30, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=10, command=lambda: button_click(0))

#operator buttons widgets
button_add = Button(root, text="+", padx=31, pady=10, command=button_add)
button_minus = Button(root, text="-", padx=32, pady=10, command=button_subtract)
button_multiply = Button(root, text="x", padx=32, pady=10, command=button_multiply)
button_divide = Button(root, text="/", padx=32, pady=10, command=button_divide)
button_equal = Button(root, text="=", padx=70, pady=10, command=button_equal)
button_delete = Button(root, text="Del", padx=25, pady=10, command=button_delete)
button_changeSign = Button(root, text="+/-", padx=24, pady=10, command=change_sign)
button_backspace = Button(root, text="<-", padx=26, pady=10, command=button_backspace)
button_exponent = Button(root, text="^", padx=31, pady=10, command=button_exponent)

#put the buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_0.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_exponent.grid(row=5, column=3)

button_changeSign.grid(row=1, column=0)
button_delete.grid(row=1, column=1)
button_backspace.grid(row=1, column=2)
button_add.grid(row=1, column=3)

root.mainloop()
