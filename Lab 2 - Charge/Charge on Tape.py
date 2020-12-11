from __future__ import division
from visual import *

## constants
oofpez = 9e9
qproton = -1.6e-19
scalefactor = 1e-20

print oofpez

## objects
particle = sphere(pos = vector(1e-10,0,0), radius = 2e-11, color = color.blue)

## initial values
obslocation = vector(3.1e-10, -2.1e-10,0)
obs2 = vector(-2e-10,0,0)
obs3 = vector(4e-10,0,0)
obs4 = vector(1e-10,0,3e-10)
obs5 = vector(1e-10,0,-3e-10)
obs6 = vector(1e-10,-3e-10,0)
obs7 = vector(1e-10,3e-10,0)

## calculations
r = obslocation - particle.pos
print "the relative position vector is", r
ra = arrow (pos = particle.pos, axis = r, color = color.green)

rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
print "the magnitude of r is", rmag

rhat = r / rmag
print "unit vector rhat is", rhat

rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
print "Electric field vector is", E
ea = arrow(pos = obslocation, axis = scalefactor*E, color=color.orange)

## label first observation
labele = label(pos=obslocation + ea.axis/2, text="E")
labelr = label(pos=particle.pos + r/2, text="r")

## more locations
r = obs2 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs2, axis = scalefactor*E, color=color.orange)

r = obs3 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs3, axis = scalefactor*E, color=color.orange)

r = obs4 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs4, axis = scalefactor*E, color=color.orange)

r = obs5 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs5, axis = scalefactor*E, color=color.orange)

r = obs6 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs6, axis = scalefactor*E, color=color.orange)

r = obs7 - particle.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
rhat = r / rmag
rmagsq = rmag * rmag
E = (oofpez * qproton / rmagsq) * rhat
ea = arrow(pos = obs7, axis = scalefactor*E, color=color.orange)

