#import required libraries
import json
from collections import defaultdict

"""
For each candidate, we will Generate the following reports:
1. Proportion of donations that are employed vs unemployed, vs retired
2. Of those employed, we will generate proportions of those that are employed in each industry

The file: industries.json contains the industry that each company is a part of
The file TrumpOutput.json and BidenOutput.json contain the details (in terms of contributions) for each candidate

"""
# Load the files for each candidate
bidenFile = open("output/BidenOutput.json", "r")
trumpFile = open("output/trumpOutput.json", "r")

bidenStats = json.load(bidenFile)
trumpStats = json.load(trumpFile)

#load the industries file
industriesFile = open("output/industries.json", "r")
industries = json.load(industriesFile)

"""
for each candidate, loop through the donations, from each company
each entry in the both files contains:
    i. a key - the name of the company and 
    ii. a value, that is an array [x,y] where x is the number of donations and y is the total sum of donations


"""
# Variables for trump stats
trumpEmploymentStats = defaultdict(list)
trumpIndustryShare = defaultdict(list)
trumpTotalContributions = 0
trumpNumberOfContributions = 0
# Biden stats
bidenEmploymentStats = defaultdict(list)
bidenIndustryShare = defaultdict(list)
bidenTotalContributions = 0
bidenNumberOfContributions = 0

# Get employment stats
# For Trump
for key in trumpStats:
    trumpNumberOfContributions += trumpStats[key][0]
    trumpTotalContributions += trumpStats[key][1]
    # Stats by industry
    if key.upper() in industries:
        if industries[key] in trumpEmploymentStats:
            trumpEmploymentStats[industries[key]][0]+=trumpStats[key][0]
            trumpEmploymentStats[industries[key]][1]+=trumpStats[key][1]
        else:
            trumpEmploymentStats[industries[key]] = trumpStats[key]
    elif key!='RETIRE' and key !='UNEMPLOYED':
        # includes those who are self-employed
        if 'Other' in trumpEmploymentStats:
            trumpEmploymentStats['Other'][0]+=trumpStats[key][0]
            trumpEmploymentStats['Other'][1]+=trumpStats[key][1]
        else:
            trumpEmploymentStats['Other'] = trumpStats[key]
# For Biden
for key in bidenStats:
    bidenNumberOfContributions += bidenStats[key][0]
    bidenTotalContributions += bidenStats[key][1]
    # Stats by industry
    if key.upper() in industries:
        if industries[key] in bidenEmploymentStats:
            bidenEmploymentStats[industries[key]][0]+=bidenStats[key][0]
            bidenEmploymentStats[industries[key]][1]+=bidenStats[key][1]
        else:
            bidenEmploymentStats[industries[key]] = bidenStats[key]
    elif key!='RETIRE' and key !='UNEMPLOYED':
        # includes those who are self-employed
        if 'Other' in bidenEmploymentStats:
            bidenEmploymentStats['Other'][0]+=bidenStats[key][0]
            bidenEmploymentStats['Other'][1]+=bidenStats[key][1]
        else:
            bidenEmploymentStats['Other'] = bidenStats[key]

# Write the output to a json file
output = defaultdict(list)

output['trump'] = {'TotalContributions':trumpTotalContributions,
                    'numberOfContributions':trumpNumberOfContributions,
                    'employmentStats':trumpEmploymentStats,
                    'retiredContributions':trumpStats['RETIRE'],
                    'unemployedContributions':trumpStats['UNEMPLOYED'],
                    'unspecifiedContributions':trumpStats['UNSPECIFIED']
                    }
output['hillary'] = {'TotalContributions':bidenTotalContributions,
                    'numberOfContributions':bidenNumberOfContributions,
                    'employmentStats':bidenEmploymentStats,
                    'retiredContributions':bidenStats['RETIRE'],
                    'unemployedContributions':bidenStats['UNEMPLOYED'],
                    'unspecifiedContributions':bidenStats['UNSPECIFIED']
                    }
# Write the output to a file
consolidatedOutput = open('output/consolidatedOutput16.json','w')
consolidatedOutput.write(json.dumps(output))