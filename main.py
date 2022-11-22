from formulas import *

def main():
    print("-----------------------------------------\nWelcome to the Constellation Builder 0.1!\n-----------------------------------------")
    print("\nWhich celestial body would you like to build you constellation around?")
    celestial_body = get_choice(["earth", "mercury", "mars", "venus", "jupiter", "saturn", "uranus", "neptune"])
    print("\nChoose type of transfer orbit \n 1 is the fastest but is too steep \n 2 is the overall best option and still offers quick deployment speed \n 3 is the slowest but your sattelites wont need much fuel to get to the final orbit")
    transfer_orb_type = get_range([1,3])
    print("\nAt which altitude would you like your constellation to be? this value does not include radius of main body")
    altitude = get_range([0, math.inf])
    print("\nAnd finnaly how many sattelites will be in your consellation?")
    number_of_satellites = get_range([0, math.inf])
    
    get_transfer_orb(altitude, number_of_satellites, transfer_orb_type, celestial_body)

def get_transfer_orb(distance, number, mode, celestial_body, test_mode = False):

    # returns orbital parameters for transfer orbit, takes in the distance at apogee, number of sattelites, type of transfer orbit and celestial body
    # transfer orbit type 1 is the quickest with lowest perigee, type 2 has higher perigee albeit with longer deployment time, type 3 has transfer orbit higher than the final orbit

    celestial_body_radius = planets[celestial_body]["radius"]                
    final_orb_period = get_orb_period(distance + celestial_body_radius, celestial_body)

    trans_orb_period = get_trans_orb_period(final_orb_period, number, mode)

    trans_orb_sm_axis = get_semimajor_axis(trans_orb_period, celestial_body)
    trans_orb_perigee = get_orb_perigee(trans_orb_sm_axis, distance, celestial_body_radius)

    dv = dv_needed_for_circularization(celestial_body, trans_orb_perigee + celestial_body_radius, distance + celestial_body_radius)
    
    atmosphere = has_atmosphere(celestial_body)

    if test_mode != True:
        if trans_orb_perigee <= atmosphere:
            print(f"-----------\nFATAL ERROR\n----------- \n transfer orbit too low, your sattelite bus will burn up \n change type of transfer orbit or increase alltitude of the whole sattelite network")
            print(f" transfer orbit perigee is {trans_orb_perigee} meters")
            print(f" transfer orbit perigee needs to be {abs(trans_orb_perigee - atmosphere)} meters higher")
        
        if get_lowest_point(number, distance + celestial_body_radius) < celestial_body_radius:
            print(f"-------\nWARNING\n------- \n line of sight lines are broken \n lowest point on the lines is {celestial_body_radius - get_lowest_point(number, distance + celestial_body_radius)} below ground \n ")
        else:
            print(f"transfer orbit parameters OK \n transfer orbit perigee is {trans_orb_perigee} meters\n final orbit altitude is {distance} meters\n DeltaV required to circularize is {dv}")
    
    return [distance, trans_orb_perigee, dv]

def get_choice(choices): #data type stands for data type of answer not data type of choices
    choice = ""

    while choice not in choices:
        choice = input(f" Possible choices are {choices} \n").lower()

    return choice

def get_range(values):

    while True:

        choice = input(f"select number in range from {values[0]} to {values[1]} \n")
        try:
            choice = float(choice)
            if values[0] <= choice <= values[1]:
                return choice
        except:
            pass

main()
