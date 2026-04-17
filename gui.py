import tkinter as tk #we will import tkinter which will allow us to use a gui
from main import half_adder, full_adder, save_calculation, load_calculations, search_calculation, sort_calculations
#we import the functions from the main file in order to keep the gui and main files seperate this makes the program more robust and versatile

# Here we create the main window and title it
window = tk.Tk()
window.title("Half Adder & Full Adder Simulator")
window.geometry("500x600")

# This is the label for the title
title = tk.Label(window, text=" Binary Adder Simulator", font = ("Arial",16))
title.pack(pady=10)

# === HALF ADDER SECTION ===
half_frame = tk.Frame( window, bg="f0f0f0")
half_frame.pack(padx=10 , pady=10 , fill="both" , expand=False)

tk