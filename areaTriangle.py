#area of triangle

a = 3
b = 4
c = 5

#calculate semi-perimeter
s = (a + b  + c) / 2

#area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('Area of triangle : ', area)