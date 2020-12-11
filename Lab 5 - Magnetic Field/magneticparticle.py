from __future__ import division
from visual import *

## Constants

# In this section, define any constants you may need
magconst = 1e-7
q = -1.6e-19
scalefactor = 2e-9

## Objects

#Change the initial vector position of the proton below:
proton = sphere(pos=vector(3e-10,0,0), radius=1e-11, color=color.red)

#Change the observation location (position of the tail of the arrow) below:
barrow1=arrow(pos=vector(0,8e-11,0), axis=vector(0,0,0), color=color.cyan)

#Add more arrows to find magnetic field at other observation locations.
#Set axis to (0,0,0) initially and update it in the loop.
barrow2 = arrow(pos=vector(0, -8e-11, 0), axis=vector(0,0,0), color = color.cyan)
barrow3 = arrow(pos=vector(0, 0, 8e-11), axis=vector(0,0,0), color = color.cyan)
barrow4 = arrow(pos=vector(0, 0, -8e-11), axis=vector(0,0,0), color = color.cyan)


## Initial values

velocity = vector(-5.2e4,0,0) # Enter the proton's velocity
deltat = 1e-17 # Adjust if program runs too slowly or too quickly

scene.autoscale=0 #Turns off autoscaling.  Set to 1 to turn it back on.


## Loop

while proton.x<5e-10:
    rate(100)
    # For each magnetic field vector:
    # 1. Calculate r and rhat
    r1 = barrow1.pos - proton.pos
    r1mag = mag(r1)
    r1hat = norm(r1)
    r2 = barrow2.pos - proton.pos
    r2mag = mag(r2)
    r2hat = norm(r2)
    r3 = barrow3.pos - proton.pos
    r3mag = mag(r3)
    r3hat = norm(r3)
    r4 = barrow4.pos - proton.pos
    r4mag = mag(r4)
    r4hat = norm(r4)
    # 2. Calculate the magnetic field vector
    crossProduct1 = cross(velocity, r1hat)
    B1 = q*crossProduct1*magconst/r1mag**2
    crossProduct2 = cross(velocity, r2hat)
    B2 = q*crossProduct2*magconst/r2mag**2
    crossProduct3 = cross(velocity, r3hat)
    B3 = q*crossProduct3*magconst/r3mag**2
    crossProduct4 = cross(velocity, r4hat)
    B4 = q*crossProduct4*magconst/r4mag**2
    # 3. Calculate the new axis of the arrow.  Scale it appropriately.
    barrow1.axis = B1*scalefactor
    barrow2.axis = B2*scalefactor
    barrow3.axis = B3*scalefactor
    barrow4.axis = B4*scalefactor

    # Update the proton's position
    proton.pos = proton.pos + velocity*deltat
