#! /usr/bin/python

import os
import datetime
import time
import serial
import schedule		# pip install schedule

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)
directory = "/home/peti/"

ulimit = 0.5

voltage1 = 0.0
voltage2 = 0.0
current1 = 0.0
current2 = 0.0
r1 = 0.0
r2 = 0.0



t1 = datetime.datetime.now()

def request():
	# open/create log file	
	file = open(directory + "batterylog.csv", "a")

	if os.stat(directory + "batterylog.csv").st_size == 0:
		file.write("time(minutes),ubat1[V],ibat1[A],r1[Ohm],ubat2[V],ibat2[A],r2[Ohm]\n")
	#timeing
	t2 = datetime.datetime.now()
	now = int((t2 - t1).total_seconds() / 60.0)
	
	#query starts
	ser.write("status\n")
	

	#query I1
	ser.write("ibat1\n")
	current1 = ser.readline()
	print(str(current1))
	current1 = current1.rstrip()
	current1 = 0	
	print(str(current1))
	
	#query I2
	ser.write("ibat2\n")
	current2 = ser.readline()
	current2 = current2.rstrip()
	print(current2)

	if (float(current1) > 0):
		#query U1
		ser.write("ubat1\n")
		voltage1 = ser.readline()
		voltage1 = voltage1.rstrip()

		#query r1
		ser.write("r1")
		r1 = ser.readline()
		r1 = r1.rstrip()


	if (float(current2) > 0):
		#query U2
		ser.write("ubat2")
		voltage2 = ser.readline()
		voltage2 = voltage2.rstrip()

		#query r2
		ser.write("r2")
		r2 = ser.readline()
		r2 = r2.rstrip()


	#print data to screen
	print(t2)	
	if (float(current1) == 0):
		print("No Battery1")
		voltage1 = 0
		current1 = 0
		r1 = 0
	else:
		print("Ubat1: " + voltage1)		
		print("Ibat1: " + current1)
		print("r1: " + r1)

	if (current2 == 0):
		print("No Battery2")
		voltage2 = 0
		current2 = 0
		r2 = 0
	else:
		print("Ubat2: " + voltage2)
		print("Ibat2: " + current2)
		print("r2: " + r2)

	#write data to csv
	file.write(str(now) + "," + str(voltage1) + "," + str(current1) + "," + str(r1) + "," + str(voltage2) + "," + str(current2) + "," + str(r2) + "\n")
	
	file.close
	
schedule.every(1).minutes.do(request)

request()
while (((current1 > 0) and (current2 > 0)) or ((voltage1 < ulimit) and (voltage2 < ulimit))):
    schedule.run_pending()
    time.sleep(1)

