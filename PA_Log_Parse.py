from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

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
dist = []

for x in bernstr:  #construct list based on observed quantites for geometric
	if len(x) not in lengths:
		lengths[len(x)] = 1
	else:
		lengths[len(x)] += 1
	dist.append(len(x)+1)


tru_geo = np.random.geometric(.15,size=len(dist))
geo_dict = {}

for x in tru_geo.tolist():
	if x not in geo_dict:
		geo_dict[x] = 1
	else:
		geo_dict[x] += 1

axes = plt.gca()
axes.set_xlim([0, 16])

plt.subplot(211)
plt.xlabel('Trials until success')
plt.ylabel('Percent Occurance')

plt.bar([x for x in geo_dict],[geo_dict[y]/len(dist)*100 for y in geo_dict],color = 'red')
plt.subplot(212)
plt.xlabel('Trials until success')
plt.ylabel('Percent Occurance')
plt.bar([x for x in lengths],[lengths[y]/len(dist)*100 for y in lengths])
plt.show()


end = stats.ks_2samp(dist,tru_geo)




