from formulas import *



def get_transfer_orb(distance, number, mode, celestial_body): 

    # returns orbital parameters for transfer orbit, takes in the distance at apogee, number of sattelites, type of transfer orbit and celestial body
    # transfer orbit type 1 is the quickest with lowest perigee, type 2 has higher perigee albeit with longer deployment time, type 3 has transfer orbit higher than the final orbit

    celestial_body_radius = planets[celestial_body]["radius"]                   
    final_orb_period = get_orb_period(distance + celestial_body_radius, celestial_body)

    trans_orb_period = get_trans_orb_period(final_orb_period, number, mode)

    trans_orb_sm_axis = get_semimajor_axis(trans_orb_period, celestial_body)
    trans_orb_perigee = get_orb_perigee(trans_orb_sm_axis, distance, celestial_body_radius)

    dv = dv_needed_for_circularization(celestial_body, trans_orb_perigee + celestial_body_radius, distance + celestial_body_radius)

    
    orbital_parameters = [distance, trans_orb_perigee, dv]
    
    return orbital_parameters 
