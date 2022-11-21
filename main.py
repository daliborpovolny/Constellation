from formulas import *

def main():
    mode = get_choice(["1", "2", "3"])
    altitude = get_choice(1)

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
        if trans_orb_perigee <= celestial_body_radius + atmosphere:
            print(f"FATAL ERROR \n transfer orbit too low \n change type of transfer orbit or increase alltitude of the whole sattelite network")
            print(f"transfer orbit perigee needs to be {abs(trans_orb_perigee - celestial_body_radius - atmosphere)} higher")
        
        if get_lowest_point(number, distance + celestial_body_radius) < celestial_body_radius:
            print(f"WARNING \n los lines are broken \n lowest point on the lines is {celestial_body_radius - get_lowest_point(number, distance + celestial_body_radius)} below ground \n ")
        else:
            print(f"transfer orbit parameters OK \n transfer orbit perigee is {trans_orb_perigee} \n final orbit altitude is {distance} /n DeltaV required to circularize is {dv}")
    
    return [distance, trans_orb_perigee, dv]

def get_choice(choices):
    choice = ""
    while choice not in choices:
        choice = input("Choose one of [%s]: " % ", ".join(choices))
    return choice

main()

