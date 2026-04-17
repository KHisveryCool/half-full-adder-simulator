# Import tkinter libraries for GUI functionality
# tk.simpledialog is part of tkinter used for dialog boxes
# Reference: https://docs.python.org/3/library/dialog.html
import tkinter.simpledialog as simpledialog
import tkinter as tk #we will import tkinter which will allow us to use a gui
from main import half_adder, full_adder, save_calculation, load_calculations, search_calculation, sort_calculations
#we import the functions from the main file in order to keep the gui and main files seperate this makes the program more robust and versatile

# ===== CREATE MAIN WINDOW =====
# Here we create the main window and title it
window = tk.Tk()
window.title("Half Adder & Full Adder Simulator")
window.geometry("500x600")

# ===== TITLE LABEL =====
# This is the label for the title
title = tk.Label(window, text=" Binary Adder Simulator", font = ("Arial",16))
title.pack(pady=10)

# ===== HALF ADDER SECTION =====
# Create a frame for the half adder section with light grey background
half_frame = tk.Frame( window, bg="#f0f0f0") 
half_frame.pack(padx=10 , pady=10 , fill="both" , expand=False)

# Add title label for half adder
tk.Label(half_frame, text= "Half Adder", font = ("Arial", 12, "bold"), bg="#f0f0f0").pack()

# Create input field for first binary digit (A)
tk.Label(half_frame, text="Input A (0 or 1):", bg="#f0f0f0").pack()
half_a = tk.Entry(half_frame, width=10)
half_a.pack()

# Create input field for second binary digit (B)
tk.Label(half_frame, text="Input B (0 or 1):", bg="#f0f0f0").pack()
half_b = tk.Entry(half_frame, width=10)
half_b.pack()

# Create label to display the result
half_result = tk.Label(half_frame, text="Result: ", bg="#f0f0f0")
half_result.pack(pady=10)
