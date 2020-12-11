from __future__ import division
from visual import *

#words
list_of_words = ['crocodile','rhino','zebra', 'bison']
print(list_of_words)

for thisword in list_of_words:
    print 'I see a', thisword, 'over there.'


#numbers
list_numbers = [1, 3, 5, 7, 9]
print(list_numbers)
for odd in list_numbers:
    print odd**2

#spheres
list_of_spheres = [sphere(pos=(-9,0,0)), sphere(pos=(9,0,0)), sphere(pos=(0,9,0)),
sphere(pos=(0,-9,0)), sphere(pos=(0,0,9)), sphere(pos=(0,0,-9))]
print(list_of_spheres)

for thisball in list_of_spheres:
    rate(2)
    thisball.color = color.blue
    thisball.radius = 0.1
    #thisball.pos = thisball.pos + vector(1, -1, 2)
print(thisball.pos)


#boxes
list_of_boxes = [ ] ## create an empty list
n = 0 ## counter for number of boxes
nmax = 5 ## number of boxes we want
while n < nmax:
    rate(2)
    list_of_boxes.append(box(pos=(2*n,0,0))) ## add a box
    n = n + 1 ## count this box
print(list_of_boxes)


#arrows
list_of_arrows = [ ]
n = 0
nmax = len(list_of_spheres)

while n < nmax:
    rate(2)
    thissphere = list_of_spheres[n]
    arrowpos = thissphere.pos + vector(1,0,0)
    list_of_arrows.append(arrow(pos=arrowpos, axis = vector(5,0,0), color = color.yellow))
    n = n + 1
print list_of_arrows    
