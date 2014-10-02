import numpy as np

# Earth Raduis
A = 6.371e6  # m

# rotation rate
Om = 7.292e-5 # s^-1

# gravity
g = 9.81 # m  s^-2

def f_coriolis(lat):
    """Calculate the coriolis parameter. 
    Latutude is assumed to be in degrees"""
    return 2*Om*np.sin(np.radians(lat))
