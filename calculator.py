from tkinter import *
from ui import *

# Main function to start the calculator
def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("332x270")
    
    create_ui(root)  # Create the UI components
    
    root.mainloop()

if __name__ == "__main__":
    main()
