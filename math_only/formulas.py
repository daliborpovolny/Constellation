import math
import numpy

grav_constant = 6.67430E-11

planets = { 
    "mercury": {
        "diameter": 4879,
        "mass": 58000000,
        "grav_par": 22032.09E19,
    },
    "venus": {
        "diameter": 12104,
        "mass": 108000000,
        "grav_par": 324859E9,
    },
    "earth": {
        "diameter":12756,
        "mass": 555,
        "grav_par": 398600.436E9,
    },
    "mars": {
        "diameter":6792,
        "mass": 555,
        "grav_par": 42828.37362E9,
    },
    "jupiter": {
        "diameter":142984,
        "mass": 555,
        "grav_par": 126686531.9E9,
    },
    "saturn": {
        "diameter":120536,
        "grav_par": 37931206.23E9,
        "mass": 555,
    },
    "uranus": {
        "diameter":51118,
        "mass": 555,
        "grav_par": 5793951.3E9,
    },
    "neptun": {
        "diameter":49528,
        "mass": 555,
        "grav_par": 6835099.97E9,
    }
}

def get_grav_par(celestial_body):

    #body_mass = planets["celestial_body"]["mass"]      #acceses the dictionary to get the mass of ce_body  ----  grav_par is now stored in dic instead of being calculated
    #grav_par = grav_constant * body_mass    

    grav_par = planets[celestial_body]["grav_par"]
    
    return grav_par

def get_orb_perigee(semimajor_axis, apogee): #semimajor axis in meters
    perigee = 2*semimajor_axis - apogee

    return perigee # in meters

def get_orb_period(semimajor_axis, celestial_body): #semimajor axis is always the same for certain orbital period, this goes both ways | semimajor_axis is in meters
    grav_par = get_grav_par(celestial_body)
    orb_period = (2*math.pi)*math.sqrt((semimajor_axis**3)/grav_par)

    return orb_period # in seconds

def get_semimajor_axis(orb_period, celestial_body): #semimajor axis is always the same for certain orbital period, this goes both ways | orb_period is in seconds
    grav_par = get_grav_par(celestial_body)
    semimajor_axis = (((orb_period**2)*grav_par)/(4*math.pi**2))**(1/3)

    return semimajor_axis # in meters

def get_transfer_orb(distance, number, mode, celestial_body):  
    # returns orbital parameters for transfer orbit, takes in the distance at apogee, number of sattelites, type of transfer orbit
    # transfer orbit type 1 is the quickest with lowest perigee, type 2 has higher perigee albeit with longer deployment time, type 3 has transfer orbit higher than the final orbit
    
    celestial_body_radius = planets[celestial_body]["diameter"]/2 * 1000 # times 1000 because it needs to be in meters but is in kilometers
    orb_period = get_orb_period(distance + celestial_body_radius, celestial_body)

    if mode == 1:
        trans_orb_period = (1/number)*  orb_period
    elif mode == 2:
        trans_orb_period = (1-1/number)* orb_period
    elif mode ==3:
        trans_orb_period = (1+1/number)* orb_period
    else:
        print("mode not defined correctly")
        
    trans_orb_sm_axis = get_semimajor_axis(trans_orb_period, celestial_body)
    trans_orb_perigee = get_orb_perigee(trans_orb_sm_axis, distance)
    orbital_parameters = [distance, trans_orb_perigee - celestial_body_radius]

    return orbital_parameters 



