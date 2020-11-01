"""
This script splits the data into two dictionaries, one for each candidate
and outputs them into json files in the following format:
There are three predetermined keys: "RETIRE", "SELF" and "UNEMPLOYED"
the rest of the script adds all the donations from individuals working for a certain company, in the following format:
    "companyName":[totalNUmber, totalDonations]

Therefore, the output files for each candidate: BidenOutput.json and TrumpOutput.json have the following format:
{
    "RETIRE":[totalNUmber, totalDonations],
    "UNEMPLOYED":[totalNUmber, totalDonations],
    "SELF":[totalNUmber, totalDonations],
    "companyName":[totalNUmber, totalDonations]
}

"""


import requests
import re
import time
from collections import defaultdict
import json


# Get list of biden committees:
bidenCommitteeFile = open("candidateInfo/HillaryCommittees.txt")
trumpCommitteeFile = open("candidateInfo/TrumpCommittees.txt")

#An array of biden and trump committees
bidenCommittees = []
trumpCommittees = []
while True:
    line = bidenCommitteeFile.readline()
    if not line:
        break
    deets = line.split("|")
    bidenCommittees.append(deets[0])

while True:
    line = trumpCommitteeFile.readline()
    if not line:
        break
    deets = line.split("|")
    trumpCommittees.append(deets[0])
        
trumpDonations = defaultdict(list)
bidenDonations = defaultdict(list)

# A dictionary to store companies that have already been queried, to reduce api calls
companies = defaultdict(list)
industries = defaultdict(list)
# Make 500 api calls per minute

#Open the file:
indiDonationFile  = open("indiv16/itcont.txt", "r")
trumpOutputFile = open("output/trumpOutput16.json","w")
bidenOutputFile = open("output/hillaryOutput.json","w")

calls_remaining = 500
waiting_time = 50

while True:
    line = indiDonationFile.readline()

    #if reached the end of the file
    if not line:
        break
    
    #else, process the line: Split on slash "|"
    details = line.split("|")
    committee = details[0]
    
    donation_amount = int(details[14])
    company = details[11]


    if company.find(",")>0:
        company = company[:company.find(",")]
    company = re.sub("INC","",company)    
    
    occupation = details[12]

    if committee in trumpCommittees:
        # if company in list of companies, add the donation amount
        if (company == "SELF" or "SELF EMPLOY" in company or "SELF-EMPLOY" in company or "SELFEMPLOY" in company
            or occupation == "SELF" or "SELF EMPLOY" in occupation or "SELF-EMPLOY" in occupation or "SELFEMPLOY" in occupation):
            if "SELF" in trumpDonations:
                trumpDonations["SELF"][0] = trumpDonations["SELF"][0]+1 if donation_amount>0 else trumpDonations["SELF"][0]-1
                trumpDonations["SELF"][1] = trumpDonations["SELF"][1]+donation_amount
            else:
                trumpDonations["SELF"] = [0,0]
                trumpDonations["SELF"][0] = trumpDonations["SELF"][0]+1 if donation_amount>0 else trumpDonations["SELF"][0]-1
                trumpDonations["SELF"][1] = trumpDonations["SELF"][1]+donation_amount
        elif (company == "NOT EMPLOYED" or "UNEMPLOY" in company or "NOT WORK" in company
                or occupation == "NOT EMPLOYED" or "UNEMPLOY" in occupation or "NOT WORK" in occupation ):
            if "UNEMPLOYED" in trumpDonations:
                trumpDonations["UNEMPLOYED"][0] = trumpDonations["UNEMPLOYED"][0]+1 if donation_amount>0 else trumpDonations["UNEMPLOYED"][0]-1
                trumpDonations["UNEMPLOYED"][1] = trumpDonations["UNEMPLOYED"][1]+donation_amount
            else:
                trumpDonations["UNEMPLOYED"] = [0,0]
                trumpDonations["UNEMPLOYED"][0] = trumpDonations["UNEMPLOYED"][0]+1 if donation_amount>0 else trumpDonations["UNEMPLOYED"][0]-1
                trumpDonations["UNEMPLOYED"][1] = trumpDonations["UNEMPLOYED"][1]+donation_amount
        elif "RETIRE" in company or "RETIRE" in occupation  :
            if "RETIRE" in trumpDonations:
                trumpDonations["RETIRE"][0] = trumpDonations["RETIRE"][0]+1 if donation_amount>0 else trumpDonations["RETIRE"][0]-1
                trumpDonations["RETIRE"][1] = trumpDonations["RETIRE"][1]+donation_amount
            else:
                trumpDonations["RETIRE"] = [0,0]
                trumpDonations["RETIRE"][0] = trumpDonations["RETIRE"][0]+1 if donation_amount>0 else trumpDonations["RETIRE"][0]-1
                trumpDonations["RETIRE"][1] = trumpDonations["RETIRE"][1]+donation_amount
        else:  
            if len(company)>0:
                if company in trumpDonations:
                    trumpDonations[company][0] = trumpDonations[company][0]+1 if donation_amount>0 else trumpDonations[company][0]-1
                    trumpDonations[company][1] = trumpDonations[company][1]+donation_amount
                else:
                    trumpDonations[company] = [0,0]
                    trumpDonations[company][0] = trumpDonations[company][0]+1 if donation_amount>0 else trumpDonations[company][0]-1

                    trumpDonations[company][1] = trumpDonations[company][1]+donation_amount
            else :
                if "UNSPECIFIED" in trumpDonations:
                    trumpDonations["UNSPECIFIED"][0] = trumpDonations["UNSPECIFIED"][0]+1 if donation_amount>0 else trumpDonations["UNSPECIFIED"][0]-1
                    trumpDonations["UNSPECIFIED"][1] = trumpDonations["UNSPECIFIED"][1]+donation_amount
                else:
                    trumpDonations["UNSPECIFIED"] = [0,0]
                    trumpDonations["UNSPECIFIED"][0] = trumpDonations["UNSPECIFIED"][0]+1 if donation_amount>0 else trumpDonations["UNSPECIFIED"][0]-1
                    trumpDonations["UNSPECIFIED"][1] = trumpDonations["UNSPECIFIED"][1]+donation_amount
            
            
    elif committee in bidenCommittees:
        
        # Check the amount of donationw
        # if company in list of companies, add the donation amount
        if (company == "SELF" or "SELF EMPLOY" in company or "SELF-EMPLOY" in company or "SELFEMPLOY" in company
            or occupation == "SELF" or "SELF EMPLOY" in occupation or "SELF-EMPLOY" in occupation or "SELFEMPLOY" in occupation):
            if "SELF" in bidenDonations:
                bidenDonations["SELF"][0] = bidenDonations["SELF"][0]+1 if donation_amount>0 else bidenDonations["SELF"][0]+1
                bidenDonations["SELF"][1] = bidenDonations["SELF"][1]+donation_amount
            else:
                bidenDonations["SELF"] = [0,0]
                bidenDonations["SELF"][0] = bidenDonations["SELF"][0]+1 if donation_amount>0 else bidenDonations["SELF"][0]-1
                bidenDonations["SELF"][1] = bidenDonations["SELF"][1]+donation_amount
        elif (company == "NOT EMPLOYED" or "UNEMPLOY" in company or "NOT WORK" in company
                or occupation == "NOT EMPLOYED" or "UNEMPLOY" in occupation or "NOT WORK" in occupation):
            if "UNEMPLOYED" in bidenDonations:
                bidenDonations["UNEMPLOYED"][0] = bidenDonations["UNEMPLOYED"][0]+1 if donation_amount>0 else bidenDonations["UNEMPLOYED"][0]-1
                bidenDonations["UNEMPLOYED"][1] = bidenDonations["UNEMPLOYED"][1]+donation_amount
            else:
                bidenDonations["UNEMPLOYED"] = [0,0]
                bidenDonations["UNEMPLOYED"][0] = bidenDonations["UNEMPLOYED"][0]+1 if donation_amount>0 else bidenDonations["UNEMPLOYED"][0]-1
                bidenDonations["UNEMPLOYED"][1] = bidenDonations["UNEMPLOYED"][1]+donation_amount
        elif "RETIRE" in company or "RETIRE" in occupation  :
            if "RETIRE" in bidenDonations:
                bidenDonations["RETIRE"][0] = bidenDonations["RETIRE"][0]+1 if donation_amount>0 else bidenDonations["RETIRE"][0]-1
                bidenDonations["RETIRE"][1] = bidenDonations["RETIRE"][1]+donation_amount
            else:
                bidenDonations["RETIRE"] = [0,0]
                bidenDonations["RETIRE"][0] = bidenDonations["RETIRE"][0]+1 if donation_amount>0 else bidenDonations["RETIRE"][0]-1
                bidenDonations["RETIRE"][1] = bidenDonations["RETIRE"][1]+donation_amount
        else:
            if len(company)>0:
                if company in bidenDonations:
                    bidenDonations[company][0] = bidenDonations[company][0]+1
                    bidenDonations[company][1] = bidenDonations[company][1]+donation_amount
                else:
                    bidenDonations[company] = [0,0]
                    bidenDonations[company][0] = bidenDonations[company][0]+1
                    bidenDonations[company][1] = bidenDonations[company][1]+donation_amount
            else:
                if "UNSPECIFIED" in bidenDonations:
                    bidenDonations["UNSPECIFIED"][0] = bidenDonations["UNSPECIFIED"][0]+1 if donation_amount>0 else bidenDonations["UNSPECIFIED"][0]-1
                    bidenDonations["UNSPECIFIED"][1] = bidenDonations["UNSPECIFIED"][1]+donation_amount
                else:
                    bidenDonations["UNSPECIFIED"] = [0,0]
                    bidenDonations["UNSPECIFIED"][0] = bidenDonations["UNSPECIFIED"][0]+1 if donation_amount>0 else bidenDonations["UNSPECIFIED"][0]-1
                    bidenDonations["UNSPECIFIED"][1] = bidenDonations["UNSPECIFIED"][1]+donation_amount
            
    
trumpOutputFile.write(json.dumps(trumpDonations))
bidenOutputFile.write(json.dumps(bidenDonations))


# Get the number for each candidate who ie self-employed, unemployed and retured


"""
Read file 
for each contribution, determine whether it's a contribution for Joe Biden or Trump
if so, then check what the company that the person works for, call api to get the industry, 
Add the industry and amount to a dictionary that counts, for each industry, the total number of contributions and the total donations from that industry

"""
