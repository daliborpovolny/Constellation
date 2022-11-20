import math

grav_constant = 6.67430E-11

planets = { 
    "mercury": {
        "radius": 2439700,
        "mass": 0.330E24,
        "grav_par": 2.2031780000000021E13,
    },
    "venus": {
        "radius": 6051800,
        "mass": 4.87E24,
        "grav_par": 3.2485859200000006E14,
        "atmosphere": 145000.0,
    },
    "earth": {
        "radius":6049000,
        "mass": 5.97E24,
        "grav_par": 3.9860043543609598E14,
        "atmosphere": 140000.0,
    },
    "mars": {
        "radius":3396200,
        "mass": 0.642E24,
        "grav_par": 4.282837362069909E13,
        "atmosphere": 125000.0,
    },
    "jupiter": {
        "radius":71492000,
        "mass": 1898E24,
        "grav_par": 126686531.9E9,
        "atmosphere": 1550000.0,
    },
    "saturn": {
        "radius":57216000,
        "grav_par": 3.793120749865224E16,
        "mass": 555,
        "atmosphere": 2000000.0,
    },
    "uranus": {
        "radius":25559000,
        "mass": 86.8E24,
        "grav_par": 5.793951322279009E15,
        "atmosphere": 1400000.0
    },
    "neptun": {
        "radius":24764000,
        "mass": 102E24,
        "grav_par": 6.835099502439672E15,
        "atmosphere": 1250000.0
    }
}

def get_grav_par(celestial_body):

    body_mass = planets[celestial_body]["mass"]      #acceses the dictionary to get the mass of ce_body
    grav_par = grav_constant * body_mass    
    
    return grav_par

def get_orb_perigee(semimajor_axis, apogee, celestial_body_radius): #semimajor axis in meters
    perigee = (2*semimajor_axis - (apogee + celestial_body_radius)) - celestial_body_radius

    return perigee # in meters

def get_orb_period(semimajor_axis, celestial_body): 
    #semimajor axis is always the same for certain orbital period, this goes both ways | semimajor_axis is in meters
    grav_par = get_grav_par(celestial_body)
    orb_period = (2*math.pi)*math.sqrt((semimajor_axis**3)/grav_par)

    return orb_period # in seconds

def get_semimajor_axis(orb_period, celestial_body): 
    #semimajor axis is always the same for certain orbital period, this goes both ways | orb_period is in seconds
    grav_par = get_grav_par(celestial_body)
    semimajor_axis = ((orb_period* math.sqrt(grav_par))/(2*math.pi))**(2/3)

    return semimajor_axis # in meters

def get_trans_orb_period(final_orbit_period, number_of_sattelites, type):

    if type == 1:
        trans_orb_period = (1/number_of_sattelites)*  final_orbit_period
    elif type == 2:
        trans_orb_period = (1-1/number_of_sattelites)* final_orbit_period
    elif type ==3:
        trans_orb_period = (1+1/number_of_sattelites)* final_orbit_period
    else:
        print("mode not defined correctly")
        trans_orb_period = 0

    return trans_orb_period

def dv_needed_for_circularization(celestial_body, starting_orb_radius, final_orb_radius):
    grav_par = get_grav_par(celestial_body)
    
    v = math.sqrt(grav_par/final_orb_radius)*(1- (math.sqrt((2*starting_orb_radius) / (starting_orb_radius + final_orb_radius))))

    return abs(v) #change in velocity doesn not have a direction

def get_lowest_point(n_of_satellites, orbital_radius):
    alpha = math.radians(360 / n_of_satellites)

    side_between_satellites = math.sqrt((2*(orbital_radius**2))-(2*orbital_radius**2 *math.cos(alpha)))
    
    lowest_point = math.sqrt((orbital_radius**2)-((side_between_satellites*0.5)**2))

    return lowest_point