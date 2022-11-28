import formulas
from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

OPTIONS = []

for k in formulas.planets.keys():
    OPTIONS.append(k)


root = Tk()
root.title("Constellation Builder GUI")
root.geometry("700x400")

# Planet choice
planet_choice_data = StringVar(root)
planet_choice_data.set("nothing yet") # default value (earth)
planet_label = Label(root, text = "Planet of choice")
planet_choice_menu = OptionMenu(root, planet_choice_data, *OPTIONS)

planet_label.grid(row=0, column=0, sticky="w")
planet_choice_menu.grid(row=0, column=1)

# Satellite number choice
satellite_label = Label(root, text = "Number of satellites")
satellite_entry = Entry(root)

satellite_label.grid(row=1, column=0, sticky="w")
satellite_entry.grid(row=1, column=1)

# Orbital altitude choice
orbital_altitude_label = Label(root, text= "Orbital Altitude")
orbital_altitude_entry = Entry(root)

orbital_altitude_label.grid(row=2, column=0, sticky="w")
orbital_altitude_entry.grid(row=2, column=1)

# Dive orbit
dive_orbit_value = IntVar()

dive_orbit_label = Label(root, text= "Dive orbit")
dive_orbit_checkbox = Checkbutton(root, variable=dive_orbit_value)

dive_orbit_label.grid(row=3, column=0, sticky="w")
dive_orbit_checkbox.grid(row=3, column=1)




mainloop()