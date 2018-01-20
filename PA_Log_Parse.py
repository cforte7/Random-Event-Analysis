from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import seaborn as sns



with open('test.txt') as f:
	data = f.read()


data = [x.lstrip('\t{\n').split('\n\t') for x in data.split('\n}\n{\n')]
dmg = []


targets = []
exclude = ['mid','bot','top','tower4']
pa = []
for x in data:
	try:
		if x[0] == 'type: 0' and (x[3] == 'attacker_name: npc_dota_hero_phantom_assassin' or x[4] == 'attacker_name: npc_dota_hero_phantom_assassin'):
			dmg_val = x[11].split('value: ')[1]
			dmg_val = int(dmg_val)
			dmg.append(dmg_val)
	except IndexError:
		pass

dmg = np.array(dmg)
dmg_count = np.unique(dmg,return_counts=True)

x_axis1 = np.arange(5)
plt.figure(1)
plt.xlabel('Damage Delt')
plt.ylabel('Occurances')
plt.title('Total Occurances of Each Damage Value')
#sns.barplot(x_axis1,dmg_count[1])
plt.xticks(x_axis1,dmg_count[0])
#plt.show()

dmg = np.array(dmg[13:])

bernoulli = []
for x in dmg:   #convert damage into bernouli trial 1=success, 0=failure
	if int(x) <=25:
		bernoulli.append(str(0))
	else:
		bernoulli.append(str(1))

bernoulli_count = np.unique(bernoulli,return_counts=True)
x_axis2 = np.arange(2)
plt.figure(2)
plt.ylabel('Occurances')
plt.title('Total Occurances of Bernoulli Success/Failure')
sns.barplot(x_axis2,bernoulli_count[1])
plt.xticks(x_axis2,('Failure','Success'))
#plt.show()

bernoulli = ''.join(bernoulli)
bern_list = (bernoulli).split('1')
bern_list = [int(len(x)) for x in bern_list]

sample_data = {}

for x in bern_list:  #construct dictionary based on observed quantites for geometric
	if x not in sample_data:
		sample_data[x] = 1
	else:
		sample_data[x] += 1

tru_geo = np.random.geometric(.15,size=len(bern_list))
geo_dict = {}

for x in tru_geo.tolist():
	if x-1 not in geo_dict:
		geo_dict[x-1] = 1
	else:
		geo_dict[x-1] += 1



#Create Histograms of observed values from Sample as well as 

x_axis1 = [x for x in geo_dict if x < 18]
y_axis1 = [geo_dict[y]/len(bern_list)*100 for y in geo_dict if y < 18]

plt.figure(2)
plt.subplot(121)
plt.xlabel('Failures before success')
plt.ylabel('Percent Occurance')
plt.title('Random Samples from \n True Geometric Population')
plt.bar(x_axis1,y_axis1,color = 'red')


x_axis2 = [x for x in sample_data]
y_axis2 = [sample_data[y]/len(bern_list)*100 for y in sample_data]

plt.subplot(122)
plt.xlabel('Failures before success')
plt.ylabel('Percent Occurance')
plt.title('Sample from Dota 2 Events')
plt.bar(x_axis2,y_axis2)
plt.show()

'''
fig, ax = plt.subplots(figsize=(8, 4))
plt.xlabel('x line')
plt.ylabel('y line')
size_cum = len(np.unique(bern_list))
n, bins, patches = ax.hist(tru_geo, size_cum, normed=1, histtype='step',cumulative=True, label='Empirical')
plt.show()
'''

#2 Sample KS Test
end = stats.ks_2samp(bern_list,tru_geo)
#ks_critical = (1.035)/(math.sqrt(len(bern_list)-.01+(.83/math.sqrt(len(bern_list)))))
ks_critical = 1.63*math.sqrt((len(bern_list)+len(tru_geo))/(len(bern_list)*len(tru_geo)))
print('Ho:The two sets of data Come from the same population.')
print('Ha:The two sets of data do not come from the same population.\n')
print('Critical value for alpha = .01 is '+str(ks_critical))
print('The Test Statistic for the Kolmogorov-Smirnov Test is:'+str(end[0])+'\nThe P value is:'+str(end[1]))


#Anderson-Darling Test
end2 = stats.anderson_ksamp((bern_list,tru_geo))


print('\n')
print('The Test Statistic for the Anderson-Darling test is:'+str(end2[0]))
print('The Critical values for the Anderson Darling test are:')

significane = ['25%','10%','5%','2.5%','1%']

for x in range(len(significane)):
	print('\tFor '+significane[x]+' significane level: '+str(end2[1][x]))
print('We Reject Ho for both tests at alpha = .01 because the test statistic \nfor both tests are above associated the critical values.')
