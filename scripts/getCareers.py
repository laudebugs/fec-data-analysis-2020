from collections import defaultdict
import json

indiv20 = open("indiv20/itcont.txt","r")
trumpFile = open("candidateInfo/TrumpCommittees.txt","r")
bidenFile = open("candidateInfo/BidenCommittees.txt","r")

trumpCommittee = trumpFile.readline().split("|")[0]
bidenCommittee = bidenFile.readline().split("|")[0]

# Loop through the file
careers = []
trumpCareers = {}
bidenCareers = {}
while True:
    line = indiv20.readline()

    if not line:
        break
    data = line.split("|")
    occupation = data[12]
    if(data[0]==trumpCommittee):
        if occupation in trumpCareers:
            trumpCareers[occupation] = [trumpCareers[occupation][0]+1,trumpCareers[occupation][1]+int(data[14])]
        else:
            trumpCareers[occupation] = [1,int(data[14])]
    elif data[0]==bidenCommittee or 'EARMARKED FOR BIDEN FOR PRESIDENT' in data[19]:
        if occupation in bidenCareers:
            bidenCareers[occupation] = [bidenCareers[occupation][0]+1,bidenCareers[occupation][1]+int(data[14])]
        else:
            bidenCareers[occupation] = [1,int(data[14])]

output = defaultdict(list)

# Create a json file to hold the output
output['trump'] = trumpCareers
output['biden'] = bidenCareers

# Write the file to output
consolidatedOutput = open('output/donationsbyCareer.json','w')
consolidatedOutput.write(json.dumps(output))