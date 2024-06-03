import math

#Distance coordinates are given according to Triangular design. 
#To see how the points and thus the distances relate to oneanother please check drawings provided in ISBEP rapport of Gerrit Dirk Lakerveld 2024
#If linear motor is detached remeasure all distances and angles again to have a accurate set of Inverse Kinematics.


BD = 140 
AG = 950
CG = 300
CD = 610
L0 = 600 #Unextende length of the linear actuator.  remesure just to be sure 
alpha = math.radians(15)
deflection = 213
decoder_position= 1000000

#Angle to encoder
theta = math.radians(90) #Elevation input value
beta = math.radians(180) #Azimuth input value

AC = math.sqrt(AG**2 + CG**2)
gamma = math.asin(CG/AC)

AD = math.sqrt(AC**2 + CD**2 - 2*AC*CD*math.cos(gamma + theta + gamma))
AB = math.sqrt(AD**2 + BD**2)

motor_extension = AB-L0
angle_to_encoder_elevation = round((decoder_position/deflection)*motor_extension)
angle_to_encoder_azimuth = round(beta*2302000/360)

#encoder to angle
elevation_encoder = 10000
azimuth_encoder = 10000

encoder_to_angle_elivation = math.acos(((elevation_encoder*deflection/decoder_position+L0)**2 - BD**2 - AC**2 - CD**2)/(-2*AC*CD)) - alpha - gamma
encoder_to_angle_azimuth = azimuth_encoder*360/2302000

print(encoder_to_angle_elivation)