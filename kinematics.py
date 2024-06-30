import sys, gpiozero, math, time

# Distance coordinates are given according to Triangular design
# To see how the points and thus the distances relate to oneanother please check drawings provided in ISBEP rapport of Gerrit Dirk Lakerveld 2024
# If linear motor is detached remeasure all distances and angles again to have a accurate set of Inverse Kinematics
# Constants
BD = 140
AG = 950
CG = 300
CD = 610
L0 = 600 # Unextended length of the linear actuator
AC = math.sqrt(AG**2 + CG**2)
gamma = math.asin(CG/AC)
alpha = math.radians(15)
deflection = 213
decoder_position= 1000000
ENCODER_CONST = 520000

# Table Pins
table_encoder = gpiozero.RotaryEncoder(23, 24, max_steps=0)
table_pwm = gpiozero.PWMOutputDevice(13)
table_dir = gpiozero.DigitalOutputDevice(16)

# Arm Pins
arm_encoder = gpiozero.RotaryEncoder(14, 15, max_steps=0)
arm_pwm = gpiozero.PWMOutputDevice(12)
arm_dir = gpiozero.DigitalOutputDevice(7)

def start(table_angle, table_direction, table_pwm,
	arm_angle, arm_direction, arm_pwm):
	# Calculating angles
	beta = math.radians(table_angle)
	theta = math.radians(arm_angle)
	AD = math.sqrt(AC**2 + CD**2 - 2*AC*CD*math.cos(alpha + theta + gamma))
	AB = math.sqrt(AD**2 + BD**2)
	motor_extension = AB-L0
	table_steps = round(beta*ENCODER_CONST/360)
	arm_steps = round((decoder_position/deflection)*motor_extension)

	# Initializing condition variables
	calculated_table_angle = 0
	calculated_arm_angle = 0

	print("\n\n> Moving table and arm <\nPress [CTRL + C] to stop the program\n\n")

	try:
		# Starting table movement
		table_dir.value = table_direction
		table_pwm.value = table_pwm

		# Starting arm movement
		arm_dir.value = arm_direction
		arm_pwm.value = arm_pwm

		while (table_angle > calculated_table_angle and
			arm_angle > calculated_arm_angle):
			calculated_table_angle = abs(table_encoder.steps*360/ENCODER_CONST)
			calculated_arm_angle = abs((arm_encoder.steps/deflection)*motor_extension)
			sys.stdout.write(f"\rSteps Table = {table_encoder.steps:^6d}/{table_steps}\t\tCalculated Table Angle = {calculated_table_angle:.2f}/{table_angle}\t\t\rSteps Arm = {arm_encoder.steps:^6d}/{arm_steps}\t\tCalculated Arm Angle = {calculated_arm_angle:.2f}/{arm_angle}")
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.stdout.flush()
		sys.stdout.write(f"\rStopped: Steps Table = {table_encoder.steps:^6d}/{table_steps}\t\tCalculated Table Angle = {calculated_table_angle:.2f}/{table_angle}\t\t\rSteps Arm = {arm_encoder.steps:^6d}/{arm_steps}\t\tCalculated Arm Angle = {calculated_arm_angle:.2f}/{arm_angle}")
	stop()
	sys.exit()

def stop():
	# Closing table pins
	table_encoder.close()
	table_pwm.close()
	table_dir.close()

	# Closing arm pins
	arm_encoder.close()
	arm_pwm.close()
	arm_dir.close()

def main():
	start(int(input("Table angle [0...360]: ")),
	        int(input("Table direction (Clockwise or Counter-clockwise) [0/1]: ")),
	        float(input("Table speed [0...1]: ")),
	        int(input("Arm angle [0...360]: ")),
	        int(input("Arm direction (Clockwise or Counter-clockwise) [0/1]: ")),
                float(input("Arm Speed [0...1]: ")))

if __name__ == "__main__":
	print("###########################")
	print("#Temporary Kinematics Test#")
	print("###########################")
	main()