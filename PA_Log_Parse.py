from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math

with open('test.txt') as f:
	data = f.read()


data = [x.lstrip('\t}\n').split('\n\t') for x in data.split('\n}\n{\n')]


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
		dist.append(len(x)+1)
		lengths[len(x)] += 1
tru_geo = np.random.geometric(.15,size=len(dist))
geo_dict = {}
for x in tru_geo.tolist():
	if x-1 not in geo_dict:
		geo_dict[x-1] = 1
	else:
		geo_dict[x-1] += 1


axes = plt.gcf()


plt.subplot(121)
plt.xlabel('Trials until success')
plt.ylabel('Percent Occurance')
plt.title('Random Samples from \n True Geometric Population')
plt.bar([x for x in geo_dict if x < 18],[geo_dict[y]/len(dist)*100 for y in geo_dict if y < 18],color = 'red')



plt.subplot(122)
plt.xlabel('Trials until success')
plt.ylabel('Percent Occurance')
plt.title('Sample from Dota 2 Events')
plt.bar([x for x in lengths],[lengths[y]/len(dist)*100 for y in lengths])
#plt.show()


end = stats.ks_2samp(dist,tru_geo)
end2 = stats.anderson_ksamp((dist,tru_geo))
ks_critical = (1.035)/(math.sqrt(len(dist))-.01+(.83/math.sqrt(len(dist))))


print('Ho:The two sets of data Come from the same population.')
print('Ha:The two sets of data do not come from the same population.\n')
print('The Test Statistic for the Kolmogorov-Smirnov Test is:'+str(end[0])+'\nThe P value is:'+str(end[1]))

print('Critical value for alpha = .01 is '+str(ks_critical))


print('\n')
print('The Test Statistic for the Anderson-Darling test is:'+str(end2[0]))
print('The Critical values for the Anderson Darling test are:')
significane = ['25%','10%','5%','2.5%','1%']
for x in range(len(significane)):
	print('      For '+significane[x]+' significane level: '+str(end2[1][x]))
print('We Reject Ho for both tests at alpha = .01 because the test statistic \nfor both tests are above associated the critical values.')



