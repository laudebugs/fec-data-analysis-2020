"""

We will plot several graphs to visualize the results
1 a pie chart for each candidate showing proportions of employed to retired to unemployed
2. A pie chart of the major industry donations by percentage (of amount of money) and of number of donations
3. A bar chart showing the top sectors that contributed to each candidate

"""
import matplotlib.pyplot as plt 
import collections from defaultdict
#import the output file
consolidatedOutputFile = open('output/consolidatedOutput.json','r')
results = json.load(consolidatedOutputFile)
# A pie chart for each candidate
labels = 'employed', 'unemployed','retired'
trumpUnemployed = results['trump']['unemployedContributions']
trumpRetired = results['trump']['unemployedContributions']
trumpEmployed = [results['trump']['numberOfContributions']-(trumpUnemployed[0]+trumpRetired[0]),results['trump']['TotalContributions']-(trumpUnemployed[1]+trumpRetired[1],]
colors = ['#176E74','#FF7538','#504E4B']
explode = (0,0,0.1)

sizeByNoDonations = [trumpEmployed[0],trumpUnemployed[0],trumpUnemployed[0]]
sizeByDonationAmount = [trumpEmployed[1],trumpUnemployed[1],trumpUnemployed[1]]
plt.pie(sizeByDonationAmount,explode=explode,labels=labels, colors=colors)
plt2.pie(sizeByNoDonations,explode=explode,labels=labels, colors=colors)

autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

plt2.axis('equal')
plt2.show()

# show which industries gave the most to each candidate
trumpIndustries = (results['trump']['employmentStats'])
trumpIndustries = sorted(trumpIndustries[''], key=lambda x : x['percentage'], reverse=True)

trumpIndustries= { 'a':[3,50],'ab':[2,90],'abc':[1,99],'abcd':[0,0] }
print("Dictionary: ", trumpIndustries)
sort_dict= dict(sorted(trumpIndustries.items(), key=lambda item: item[1][1])) 
print("Sorted Dictionary by value: ", sort_dict)

# The top elements will be at the bottom