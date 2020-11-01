from collections import defaultdict
import json

indiv20 = open("indiv20/itcont.txt","r")
trumpFile = open("candidateInfo/TrumpCommittees.txt","r")
bidenFile = open("candidateInfo/HillaryCommittees.txt","r")

trumpCommittee = trumpFile.readline().split("|")[0]
bidenCommittee = bidenFile.readline().split("|")[0]
bidenCommittee2 = bidenFile.readline().split("|")[0]


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
    if(data[0]==trumpCommittee or data[15]==trumpCommittee):
        if occupation in trumpCareers:
            if int(data[14]>0):
                trumpCareers[occupation] = [trumpCareers[occupation][0]+1,trumpCareers[occupation][1]+int(data[14])]
            else:
                trumpCareers[occupation] = [trumpCareers[occupation][0]-1,trumpCareers[occupation][1]+int(data[14])]
        else:
            if int(data[14>0]):
                trumpCareers[occupation] = [1,int(data[14])]
            else:
                trumpCareers[occupation] = [-1,int(data[14])]
    elif data[0]==bidenCommittee or data[15]==bidenCommittee or data[15]==bidenCommittee2:
        print(data[15])
        if occupation in bidenCareers:
            if int(data[14>0]):
                bidenCareers[occupation] = [bidenCareers[occupation][0]+1,bidenCareers[occupation][1]+int(data[14])]
            else:
                bidenCareers[occupation] = [bidenCareers[occupation][0]-1,bidenCareers[occupation][1]+int(data[14])]
        else:
            if int(data[14>0]):
                bidenCareers[occupation] = [1,int(data[14])]
            else:
                bidenCareers[occupation] = [-1,int(data[14])]

output = defaultdict(list)

# Create a json file to hold the output
output['trump'] = trumpCareers
output['hillary'] = bidenCareers

# Write the file to output
consolidatedOutput = open('output/donationsbyCareer16.json','w')
consolidatedOutput.write(json.dumps(output))