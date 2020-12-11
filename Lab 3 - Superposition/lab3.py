from __future__ import division 
from visual import *

#constants
constant = 9e9
scalefactor = 1e-21
e = 1.6e-19

#objects
positive = sphere(pos=vector(-5e-11,0,0), radius=1e-11, color=color.red)
negative = sphere(pos=vector(5e-11,0,0), radius=1e-11, color=color.blue)

#initial values
obslocation = vector(2e-10,0,0)
theta = 0

#calculations

while theta < 2*pi:
## calculate new vector value for obslocation, using this angle
    rhat = vector(cos(theta), sin(theta),0)
    obslocation = mag(obslocation) * rhat
## use superposition principle to calculate Enet at obslocation
    rpos  = obslocation - positive.pos
    Epos = constant * e / mag(rpos)**2 * norm(rpos)
    rneg = obslocation - negative.pos
    Eneg = constant * -e / mag(rneg)**2 * norm(rneg)
    Enet = Epos + Eneg
## print values of obslocation, and Enet vector
    print "Enet is ", Enet
    print "obslocation is", obslocation
## create an arrow to display Enet at obslocation, and scale it
    arrow(pos=obslocation, axis = Enet*scalefactor, color = color.orange)
## calculate new value of theta
    theta = theta + pi/6

theta = 0
obslocation = vector(2e-10,0,0)
while theta < 2*pi:
## calculate new vector value for obslocation, using this angle
    rhat = vector(cos(theta), 0, sin(theta))
    obslocation = mag(obslocation) * rhat
## use superposition principle to calculate Enet at obslocation
    rpos  = obslocation - positive.pos
    Epos = constant * e / mag(rpos)**2 * norm(rpos)
    rneg = obslocation - negative.pos
    Eneg = constant * -e / mag(rneg)**2 * norm(rneg)
    Enet = Epos + Eneg
## print values of obslocation, and Enet vector
    print "Enet is ", Enet
    print "obslocation is", obslocation
## create an arrow to display Enet at obslocation, and scale it
    arrow(pos=obslocation, axis = Enet*scalefactor, color = color.orange)
## calculate new value of theta
    theta = theta + pi/6


#doubling distance on the axis
    obslocation1 = vector(2e-10,0,0)
    obslocation2 = vector(4e-10,0,0)
    rpos1  = obslocation1 - positive.pos
    Epos1 = constant * e / mag(rpos1)**2 * norm(rpos1)
    rneg1 = obslocation1 - negative.pos
    Eneg1 = constant * -e / mag(rneg1)**2 * norm(rneg1)
    Enet1 = Epos1 + Eneg1
    rpos2  = obslocation2 - positive.pos
    Epos2 = constant * e / mag(rpos2)**2 * norm(rpos2)
    rneg2 = obslocation2 - negative.pos
    Eneg2 = constant * -e / mag(rneg2)**2 * norm(rneg2)
    Enet2 = Epos2 + Eneg2
    ratio1 = mag(Enet1)/mag(Enet2)
    print "ratio 1 is ", ratio1
    
#doubling distance perpendicular
    obslocation1 = vector(0, 2e-10,0)
    obslocation2 = vector(0, 4e-10,0)
    rpos1  = obslocation1 - positive.pos
    Epos1 = constant * e / mag(rpos1)**2 * norm(rpos1)
    rneg1 = obslocation1 - negative.pos
    Eneg1 = constant * -e / mag(rneg1)**2 * norm(rneg1)
    Enet1 = Epos1 + Eneg1
    rpos2  = obslocation2 - positive.pos
    Epos2 = constant * e / mag(rpos2)**2 * norm(rpos2)
    rneg2 = obslocation2 - negative.pos
    Eneg2 = constant * -e / mag(rneg2)**2 * norm(rneg2)
    Enet2 = Epos2 + Eneg2
    ratio2 = mag(Enet1)/mag(Enet2)
    print "ratio 2 is ", ratio2    
    
#doubling distance off an axis
    a = sqrt( (2e-10)**2/2 )
    obslocation1 = vector(a, a,0)
    obslocation2 = vector(2*a, 2*a,0)
    rpos1  = obslocation1 - positive.pos
    Epos1 = constant * e / mag(rpos1)**2 * norm(rpos1)
    rneg1 = obslocation1 - negative.pos
    Eneg1 = constant * -e / mag(rneg1)**2 * norm(rneg1)
    Enet1 = Epos1 + Eneg1
    rpos2  = obslocation2 - positive.pos
    Epos2 = constant * e / mag(rpos2)**2 * norm(rpos2)
    rneg2 = obslocation2 - negative.pos
    Eneg2 = constant * -e / mag(rneg2)**2 * norm(rneg2)
    Enet2 = Epos2 + Eneg2
    ratio3 = mag(Enet1)/mag(Enet2)
    print "ratio 3 is ", ratio3

#average of all 3 ratios
    avg = (ratio1 + ratio2 + ratio3) / 3
    print "The average ratio is ", avg
