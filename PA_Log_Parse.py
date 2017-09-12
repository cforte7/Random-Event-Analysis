from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open('test.txt') as f:
	data = f.read()


data = [x.lstrip('\t').split('\n\t') for x in data.split('\n}\n{\n')]


dmg = []
targets = []
exclude = ['mid','bot','top','tower4']
pa = []
for x in data:
	try:
		if x[0] == 'type: 0' and (x[3] == 'attacker_name: npc_dota_hero_phantom_assassin' or x[4] == 'attacker_name: npc_dota_hero_phantom_assassin') and x[1].split('_')[-1] not in exclude:
			pa.append(x)
			dmg.append(x[11].split('value: ')[1])
			
			if [x[1],x[2]] not in targets:
				targets.append([x[1],x[2]])
			
	except IndexError:
		pass
dmg = np.array(dmg[13:])

#no proc: 24,25
#proc: 56,57,58

bernoulli = []

for x in dmg:   #convert damage into bernouli trial 1=success, 0=failure
	if int(x) <=25:
		bernoulli.append(str(0))
	else:
		bernoulli.append(str(1))


bernstr = (''.join(bernoulli)).split('1')
lengths = {}
su = 0
for x in bernoulli:
	su+= int(x)

print(su/len(bernoulli))
for x in set(bernstr):  #construct dictionary based on observed quantites
	lengths[len(x)] = 0

for x in bernstr:  #record number of occurences of each observation type
	lengths[len(x)] += 1



