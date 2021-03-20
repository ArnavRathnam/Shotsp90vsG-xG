import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import lines as mlines


with open ('data.csv', mode="r", encoding="utf-8-sig") as csv_file:
	#with open(filepath, mode="r", encoding="utf-8-sig") as csv_file:

	csv_reader = csv.DictReader(csv_file)
	Shotsp90 = []
	GxG = []
	names = []
	newName = []
	row = next(csv_reader)
	for row in csv_reader:
		if(row['Pos'] == 'FW' or row['Pos'] == 'MFFW' or row['Pos'] == 'FWMF'):
			if(float(row['90s']) >= 5):
				Shotsp90.append(float(row['Sh/90']))
				GxG.append(float(row['G-xG']))
				names.append(row['Player'])

count = 0

for name in names:
	result = name.index('\\')
	sName = name[0:result]
	newName.append(sName)

plt.xlim((-5,5))
plt.ylim((.5,4))

plt.style.use('ggplot')
plt.title('Shots per 90 minutes vs Goals - Expected Goals')
plt.xlabel('Goals - Expected Goals')
plt.ylabel('Shots per 90 minutes')
plt.scatter(GxG,Shotsp90, s=10, c='black')

for x,y,z in zip(GxG,Shotsp90,newName):
	fontsize = 20;
	label = f"{z}"
	plt.annotate(label,(x,y),textcoords="offset points",xytext = (0,2), ha = 'center', fontsize = 5)

plt.plot([0,0],[0.5,2.25], linewidth = .5, linestyle = '--', color='red')
plt.plot([-5,0],[2.25,2.25], linewidth = .5, linestyle = '--', color='red')
plt.plot([0,0],[2.25,4], linewidth = .5, linestyle = '--', color='lime')
plt.plot([0,5],[2.25,2.25], linewidth = .5, linestyle = '--', color='lime')

plt.annotate("Takes a lot of shots \n Is a good finisher", (3.8,3.75), ha = 'center', fontsize = 7, color = 'lime')
plt.annotate("Doesn't shoot a lot \n Is a good finisher", (3.8,0.75), ha = 'center', fontsize = 7, color = 'blue')
plt.annotate("Takes a lot of shots \n Is not a good finisher", (-3.8,3.75), ha = 'center', fontsize = 7, color = 'blue')
plt.annotate("Doesn't shoot a lot \n Is not a good finisher", (-3.8,0.75), ha = 'center', fontsize = 7, color = 'red')

plt.show()
	