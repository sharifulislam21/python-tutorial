#find roots of quadratic equation

import cmath

a = 1
b = 5
c = 6

#calucalte the discriminant
d = (b**2) - (4*a*c)
print("Discriminant : ", d)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("Roots are: ", root1," ", root2)