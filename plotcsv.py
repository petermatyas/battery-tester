#! /usr/bin/python

import matplotlib.pyplot as plt
import csv
import numpy as np

time = []
ubat1 = []
ubat2 = []
ibat1 = []
ibat2 = []
R1 = []
R2 = []
P1 = []
P2 = []

firstLine = True

with open('batterylog.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		if firstLine:
			firstLine = False
			#print("R1\tP1\t")
		else:
			u1 = float(row[1])
			i1 = float(row[2])
			u2 = float(row[4])
			i2 = float(row[5])
			time.append(int(row[0]))
			ubat1.append(float(row[1]))
			ibat1.append(float(row[2]))
			ubat2.append(float(row[4]))
			ibat2.append(float(row[5]))
			
			if (i1 == 0): 
				R1.append(0)
				P1.append(0)
			else:
				R1.append(u1 / i1)
				P1.append(u1 * i1)
			if (i2 == 0):
				R2.append(0)
				P2.append(0)	
			else:		
				R2.append(u2 / i2)		
				P2.append(u2 * i2)
			
			#print(str(R1) + "\t" + str(P1))
file.close

fig = plt.figure()
ax = fig.add_subplot(211)
bx = fig.add_subplot(212)
ax2 = ax.twinx()
bx2 = bx.twinx()

lns1 = ax.plot(time,ubat1, label='Ubat1', color='blue',  linestyle='-')
lns2 = ax.plot(time,ubat2, label='Ubat2', color='red',  linestyle='-')
lns3 = ax2.plot(time,ibat1, label='Ibat1', color='blue',  linestyle='--')
lns4 = ax2.plot(time,ibat2, label='Ibat2', color='red',  linestyle='--')
lns5 = bx.plot(time,R1, label='R1', color='blue',  linestyle='-')
lns6 = bx.plot(time,R2, label='R2', color='red',  linestyle='-')
lns7 = bx2.plot(time,P1, label='P1', color='blue',  linestyle='--')
lns8 = bx2.plot(time,P2, label='P2', color='red',  linestyle='--')

ax.set_xlabel("time [minutes]")
ax.set_ylabel("voltage [V]")
ax.set_ylim([0,1.6])
ax2.set_ylabel("current [A]")
ax2.set_ylim([0,0.6])
bx.set_ylabel("Resistacne [Ohm]")
bx2.set_ylabel("Power [W]")
bx2.set_ylim([0,1])

lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

lns2 = lns5+lns6+lns6+lns7
labs = [l.get_label() for l in lns2]
bx.legend(lns2, labs, loc=0)

area1 = np.trapz(ibat1)
area1 = area1 / 60 * 1000
area2 = np.trapz(ibat2)
area2 = area2 / 60 * 1000


ax.text(1, 1.2, "bat1: " + str("%.2f" % area1) + " mAh")
ax.text(1, 1, "bat2: " + str("%.2f" % area2) + " mAh")
print(area1)
print(area2)
plt.show()


