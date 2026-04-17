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

# Function to calculate half adder result when button is clicked
def calculate_half():
    try:
        # Get the values from input fields and convert to integers
        a = int(half_a.get())
        b = int(half_b.get())
        # Call the half_adder function from main.py
        result = half_adder(a, b)
        # If result is valid, display it and save to file
        if result:
            half_result.config(text=f"Sum: {result[0]}, Carry: {result[1]}")
            save_calculation("Half Adder", (a, b), result)
        else:
            half_result.config(text="Error: Invalid input")
    except ValueError:
        # If user enters non-integer, show error message
        half_result.config(text="Error: Enter 0 or 1")

# Create button to calculate half adder
tk.Button(half_frame, text="Calculate Half Adder", command=calculate_half, bg="#003366", fg="white", width=20).pack(pady=5)

# ===== FULL ADDER SECTION =====
# Create a frame for the full adder section with light blue background
full_frame = tk.Frame(window, bg="#e8f4f8")
full_frame.pack(padx=10, pady=10, fill="both", expand=False)

# Add title label for full adder
tk.Label(full_frame, text="Full Adder", font=("Arial", 12, "bold"), bg="#e8f4f8").pack()

# Create input field for first binary digit (A)
tk.Label(full_frame, text="Input A (0 or 1):", bg="#e8f4f8").pack()
full_a = tk.Entry(full_frame, width=10)
full_a.pack()

# Create input field for second binary digit (B)
tk.Label(full_frame, text="Input B (0 or 1):", bg="#e8f4f8").pack()
full_b = tk.Entry(full_frame, width=10)
full_b.pack()

# Create input field for carry in from previous addition
tk.Label(full_frame, text="Carry In (0 or 1):", bg="#e8f4f8").pack()
full_carry_in = tk.Entry(full_frame, width=10)
full_carry_in.pack()

# Create label to display the result
full_result = tk.Label(full_frame, text="Result: ", bg="#e8f4f8")
full_result.pack(pady=10)

# Function to calculate full adder result when button is clicked
def calculate_full():
    try:
        # Get the values from input fields and convert to integers
        a = int(full_a.get())
        b = int(full_b.get())
        carry_in = int(full_carry_in.get())
        # Call the full_adder function from main.py
        result = full_adder(a, b, carry_in)
        # If result is valid, display it and save to file
        if result:
            full_result.config(text=f"Sum: {result[0]}, Carry Out: {result[1]}")
            save_calculation("Full Adder", (a, b, carry_in), result)
        else:
            full_result.config(text="Error: Invalid input")
    except ValueError:
        # If user enters non-integer, show error message
        full_result.config(text="Error: Enter 0 or 1")

# Create button to calculate full adder
tk.Button(full_frame, text="Calculate Full Adder", command=calculate_full, bg="#003366", fg="white", width=20).pack(pady=5)

# ===== UTILITY BUTTONS SECTION =====
# Function to search for calculations in the file
def show_search():
    search_val = tk.simpledialog.askstring("Search", "Enter value to search:")
    # If user enters a search term, call the search function
    if search_val:
        search_calculation(search_val)

# Function to sort all calculations
def show_sort():
    sort_calculations()

# Function to load and display all saved calculations
def show_load():
    load_calculations()

# Create a frame for utility buttons
button_frame = tk.Frame(window)
button_frame.pack(padx=10, pady=10)

# Create search button
tk.Button(button_frame, text="Search", command=show_search, width=15).pack(side=tk.LEFT, padx=5)

# Create sort button
tk.Button(button_frame, text="Sort", command=show_sort, width=15).pack(side=tk.LEFT, padx=5)

# Create load history button
tk.Button(button_frame, text="Load History", command=show_load, width=15).pack(side=tk.LEFT, padx=5)

# Create exit button with red background
exit_btn = tk.Button(window, text="Exit", command=window.quit, bg="#cc0000", fg="white", width=15)
exit_btn.pack(pady=10)

# Start the application and keep the window running
window.mainloop()
