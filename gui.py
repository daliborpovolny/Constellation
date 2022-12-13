import formulas
from tkinter import *
from tkinter import messagebox

global_pady = 2

OPTIONS = []

for k in formulas.planets.keys():
    OPTIONS.append(k)


root = Tk()
root.title("Constellation Builder")
root.geometry("700x400")

# Welcome sign
welcome_label = Label(root, text = "Welcome To Constellation Builder!", font=("fixedsys"))
welcome_label.grid(row=0, column=(0), pady=global_pady, columnspan = 2)

# Planet choice
planet_choice_data = StringVar(root)
planet_choice_data.set("  please select  ") # default value (earth)
planet_label = Label(root, text = "Planet of choice")
planet_choice_menu = OptionMenu(root, planet_choice_data, *OPTIONS)

planet_label.grid(row=1, column=0, sticky="w", pady=global_pady)
planet_choice_menu.grid(row=1, column=1, sticky="w", pady=global_pady)

# Satellite number choice

satellite_label = Label(root, text = "Number of satellites")
satellite_entry = Entry(root)

satellite_label.grid(row=2, column=0, sticky="w", pady=global_pady)
satellite_entry.grid(row=2, column=1, sticky="w", pady=global_pady)

# Orbital altitude choice

orbital_altitude_label = Label(root, text= "Orbital Altitude")
orbital_altitude_entry = Entry(root,)

orbital_altitude_label.grid(row=3, column=0, sticky="w", pady=global_pady)
orbital_altitude_entry.grid(row=3, column=1, sticky="w", pady=global_pady)

# Dive orbit
dive_orbit_value = IntVar()

dive_orbit_label = Label(root, text= "Dive orbit")
dive_orbit_checkbox = Checkbutton(root, variable=dive_orbit_value, offvalue=3, onvalue=2)

dive_orbit_label.grid(row=4, column=0, sticky="w", pady=global_pady)
dive_orbit_checkbox.grid(row=4, column=1, pady=global_pady)


def displayResults():
    # try:
    #     altitude = int(orbital_altitude_entry.get())
    #     number = int(satellite_entry.get())
    # except:
    #     messagebox.showerror(f"Orbital altitude and number of satellites can't be in text form")
    #     return

    # mode = dive_orbit_value.get()
    # planet = planet_choice_menu.selection_get()

    # print(altitude, number, mode, planet)
    print("ran")


#calculate
calculate = Button(text="calculate", activebackground="#b3b3b3", command=displayResults())
calculate.grid(row=5, column=0, pady=global_pady, columnspan=2)



mainloop()