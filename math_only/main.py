from formulas import *

radius = planets["earth"]["diameter"]/2 *1000
test = get_orb_period(600000 + radius, "earth")
test2 = get_grav_par("earth")
print(test,radius, test2)
