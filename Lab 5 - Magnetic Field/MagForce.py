from __future__ import division
from visual import *
## INITIAL VALUE OF B
B0 = vector(0,0.2,0)
## THIS CODE DRAWS A FLOOR AND DISPLAYS THE MAGNETIC FIELD *************
xmax = .4
dx = .1
yg = -.1
for x in arange(-xmax, xmax+dx, dx):
    curve(pos=[(x,yg,-xmax),(x,yg,xmax)], color=(.7,.7,.7))
for z in arange(-xmax, xmax+dx, dx):
    curve(pos=[(-xmax,yg,z),(xmax,yg,z)],color=(.7,.7,.7))
bscale = 1
for x in arange(-xmax, xmax+dx, 2*dx):
    for z in arange(-xmax, xmax+dx, 2*dx):
        arrow(pos=(x,yg,z), axis=B0*bscale, color=(0,.8,.8))
## YOUR PROGRAM BEGINS HERE ##*******************************************
deltat = 1e-11
t = 0

particle = sphere(pos = vector(0,0.15,0.3), radius = .01, color = color.red)
velocity = vector(-2e6*2, 0, 0)
mproton = 1.7e-27
pproton = velocity * mproton
qproton = 1.6e-19
Fnet = vector(0,0,0)
trail = curve(color = particle.color)

while t < 3.34e-7:
    rate(10000)
    ## Insert the necessary steps inside the loop below to update the particle's position and velocity
    ## a) Add code to calculate the needed quantities to update the particle's velocity
    Fnet = qproton*cross(velocity, B0)
    ## b) Add code to update the particle's velocity
    pproton = pproton + Fnet*deltat
    velocity = pproton/mproton
    ## c) Update the position of the proton (movies in a straight line initially).
    particle.pos = particle.pos + velocity*deltat

    radius = (mproton*mag(velocity)**2)/mag(Fnet)
    trail.append(pos=particle.pos)
    
    t=t+deltat

print radius
