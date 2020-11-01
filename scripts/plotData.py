"""

We will plot several graphs to visualize the results
1 a pie chart for each candidate showing proportions of employed to retired to unemployed
2. A pie chart of the major industry donations by percentage (of amount of money) and of number of donations
3. A bar chart showing the top sectors that contributed to each candidate

"""
import json
import matplotlib.pyplot as plt
import numpy as np 
from collections import defaultdict
#import the output file
consolidatedOutputFile = open('output/consolidatedOutput.json','r')
# careerOutput = json.load(open('output/donationsbyCareer.json','r'))

results = json.load(consolidatedOutputFile)

trumpTitle = "DONALD J. TRUMP FOR PRESIDENT, INC. (C00580100)"
bidenTitle = "BIDEN FOR PRESIDENT (C00431569)"
# A pie chart for each candidate
labels = 'employed','unemployed','retired', 'unspecified'
trumpUnemployed = results['trump']['unemployedContributions']
trumpRetired = results['trump']['retiredContributions']
trumpUnspecified = results['trump']['unspecifiedContributions']
trumpEmployed = [results['trump']['numberOfContributions']-(trumpUnemployed[0]+trumpRetired[0]),results['trump']['TotalContributions']-(trumpUnemployed[1]+trumpRetired[1])]
trumpSizeByNoDonations = [trumpEmployed[0],trumpUnemployed[0],trumpRetired[0], trumpUnspecified[0]]
trumpSizeByDonationAmount = [trumpEmployed[1],trumpUnemployed[1],trumpRetired[1],trumpUnspecified[1]]

#Get Biden Stats
bidenUnemployed = results['biden']['unemployedContributions']
bidenRetired = results['biden']['retiredContributions']
bidenUnspecified = results['biden']['unspecifiedContributions']
bidenEmployed = [results['biden']['numberOfContributions']-(bidenUnemployed[0]+bidenRetired[0]),results['biden']['TotalContributions']-(bidenUnemployed[1]+bidenRetired[1])]
bidenSizeByNoDonations = [bidenEmployed[0],bidenUnemployed[0],bidenRetired[0],bidenUnspecified[0]]
bidenSizeByDonationAmount = [bidenEmployed[1],bidenUnemployed[1],bidenRetired[1],bidenUnspecified[1]]

colors = ['#5E9918','#D3B1C2','#F3952F','#72D1CB']
explode = (0.1,0.1,0.1,0.1)

# wedge properties
wp = {'linewidth':1, 'edgecolor':"grey"}

def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n${:,d}".format(pct, absolute) 

# creating plot
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subtitle = "Donations Totals Amount"
wedges, texts, autotexts = ax1.pie(trumpSizeByDonationAmount,
                                autopct = lambda pct: func(pct, trumpSizeByDonationAmount), 
                                explode=explode,
                                shadow=True,
                                colors=colors,
                                startangle=0,
                                wedgeprops = wp,
                                textprops = dict(color ="#00221C"))
ax1.set_title(trumpTitle) 
ax1.legend(wedges, labels,
            title="key",
            loc="center left",
            bbox_to_anchor =(1,0,0.5,1))
wedges, texts, autotexts = ax2.pie(bidenSizeByDonationAmount,
                                autopct = lambda pct: func(pct, bidenSizeByDonationAmount), 
                                explode=explode,
                                shadow=True,
                                colors=colors,
                                startangle=0,
                                wedgeprops = wp,
                                textprops = dict(color ="#00221C"))
ax2.set_title(bidenTitle) 

# ax.legend(wedges, labels,
#             title="Donation Amount to DONALD J. TRUMP FOR PRESIDENT, INC. (C00580100)",
#             loc="center left",
#             bbox_to_anchor =(1,0,0.5,1))
# plt.setp(autotexts, size = 8, weight ="bold") 
  
# show plot 
# plt.show() 


# # show which industries gave the most to each candidate
# trumpIndustries = (results['trump']['employmentStats'])
# bidenIndustries = (results['hillary']['employmentStats'])

# # Sort based on amount
# trumpIndustries= (sorted(trumpIndustries.items(), key=lambda item: item[1][1], reverse=True))
# bidenIndustries= (sorted(bidenIndustries.items(), key=lambda item: item[1][1], reverse=True)) 

# bidenTop10 = []
# bidenTop10Amounts = []

# trumpTop10 = []
# trumpTop10Amounts = []

# for i in range(1,11):
#     bidenTop10.append(bidenIndustries[i][0])
#     bidenTop10Amounts.append(bidenIndustries[i][1][1])
#     trumpTop10.append(trumpIndustries[i][0])
#     trumpTop10Amounts.append(trumpIndustries[i][1][1])

# fig2, (ax1, ax2) = plt.subplots(1, 2)
# fig2.subtitle = "Top 10 industries by donation amount"
# wedges, texts, autotexts = ax1.pie(trumpTop10Amounts,
#                                 autopct = lambda pct: func(pct, trumpTop10Amounts), 
#                                 labels = trumpTop10,
#                                 shadow=True,
#                                 startangle=0,
#                                 wedgeprops = wp,
#                                 textprops = dict(color ="#00221C"))
# ax1.set_title("DONALD J. TRUMP FOR PRESIDENT, INC. (C00580100)") 


# wedges, texts, autotexts = ax2.pie(bidenTop10Amounts,
#                                 autopct = lambda pct: func(pct, bidenTop10Amounts), 
#                                 labels = bidenTop10,
#                                 shadow=True,
#                                 startangle=0,
#                                 wedgeprops = wp,
#                                 textprops = dict(color ="#00221C"))
# ax2.set_title(bidenTitle) 

# plt.setp(autotexts, size = 12, weight ="bold") 
  
# show plot 
# plt.show() 



# # Plot by top Careers
# trumpCareers = careerOutput['trump']
# bidenCareers = careerOutput['hillary']

# # Sort based on amount
# trumpCareers= (sorted(trumpCareers.items(), key=lambda item: item[1][1], reverse=True))
# bidenCareers= (sorted(bidenCareers.items(), key=lambda item: item[1][1], reverse=True)) 

# bidenTopCareerLabels= []
# bidenTopCareers = []

# trumpTopCareerLabels= []
# trumpTopCareers = []

# for i in range(9):
#     bidenTopCareerLabels.append(bidenCareers[i][0])
#     bidenTopCareers.append(bidenCareers[i][1][1])
# sumOther = 0;
# for i in range(9,len(bidenCareers)):
#     sumOther+=bidenCareers[i][1][1]
# bidenTopCareerLabels.append('other')
# bidenTopCareers.append(sumOther)
# for i in range(9):
#     trumpTopCareerLabels.append(trumpCareers[i][0])
#     trumpTopCareers.append(trumpCareers[i][1][1])
# sumOther = 0;
# for i in range(9,len(trumpCareers)):
#     sumOther+=trumpCareers[i][1][1]
# trumpTopCareerLabels.append('other')
# trumpTopCareers.append(sumOther)

# fig3, (ax3, ax4) = plt.subplots(1, 2)
# fig3.subtitle = "Top 10 Careers by donation amount"
# wedges, texts, autotexts = ax3.pie(trumpTopCareers,
#                                 autopct = lambda pct: func(pct, trumpTopCareers), 
#                                 labels = trumpTopCareerLabels,
#                                 shadow=True,
#                                 startangle=0,
#                                 wedgeprops = wp,
#                                 textprops = dict(color ="#00221C"))
# ax3.set_title(trumpTitle) 

# plt.setp(autotexts, size = 12, weight ="bold") 
  
# wedges, texts, autotexts = ax4.pie(bidenTopCareers,
#                                 autopct = lambda pct: func(pct, bidenTopCareers), 
#                                 labels=bidenTopCareerLabels,
#                                 shadow=True,
#                                 startangle=0,
#                                 wedgeprops = wp,
#                                 textprops = dict(color ="#00221C"))
# ax4.set_title(bidenTitle) 

# plt.setp(autotexts, size = 12, weight ="bold") 

# ax4.set_title(bidenTitle) 
# # ax4.legend(wedges, bidenTopCareerLabels,
# #             title=bidenTitle,
# #             loc="center left",
# #             bbox_to_anchor =(1,0,0.5,1))
# show plot 
plt.show() 
