from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open('PA_Game1.txt') as f:
	data = f.read()

data = data[1:-2].split('\n}\n{')
data2 = []

for x in data:
	data2.append(x.split('\n\t'))

dmg = []
i=0
for x in data2:
	x.pop(0)
	try:
		if x[0] == 'type: 0' and x[3] == 'attacker_name: npc_dota_hero_phantom_assassin' and x[5] != 'inflictor: ':
			dmg.append(x)
			i += 1
			print(x[11]+', attack number '+str(i))
	except IndexError:
		pass
dmg = np.array(dmg)


#d_mva = pd.rolling_mean(dmg, 30)
#plot = plt.plot(dmg)
#plot_avg = plt.plot(d_mva)
#plt.show()




'''
#289.218
#first value is the damage
#second value is the end health
'''
