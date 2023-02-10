from math import atan2,pi,atan

a = [4,6]
b = [10,10]
red = [a[0]-b[0],a[1]-b[1]]
blue = [b[0]-a[0],b[1]-a[1]]
theta2 = atan2(red[1],red[0])
theta1 = atan2(blue[1],blue[0])
rad2deg = 180/pi

print("theta1[deg] : {}, theta2[deg] : {}".format(theta1*rad2deg,theta2*rad2deg))