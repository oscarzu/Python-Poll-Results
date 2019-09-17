
import os
import csv

#Declaring the variables
csvpath = os.path.join("Resources","Election_Data.csv")
Vote_Totals = 0
List_of_Candidates = []
List_of_Votes_Counted = []
Data_File_List = ["Resources/Election_Data.csv"]

#Opening the file and reading it
for file in Data_File_List:
    
    print(csvpath)
    
    with open(csvpath, newline = '') as csvfile:
        csvfile.readline()
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        for row in csvreader:
            Vote_Totals = Vote_Totals + 1
            candidate = row[2] 
            
            if not candidate in List_of_Candidates:
               List_of_Candidates.append(candidate)
               List_of_Votes_Counted.append(1)
            
            else:
                indexofCandidate =  List_of_Candidates.index(candidate)
                curVoteTally = List_of_Votes_Counted[indexofCandidate]
                List_of_Votes_Counted[indexofCandidate] = curVoteTally + 1
                        
#Declaring the output file with the results and doing the math ops
resultsfile = open( "Election Results.txt","w")

lines = []
lines.append("Election Results")
lines.append("__________________________")
lines.append("Total Votes: " + str(Vote_Totals))
lines.append("___________________________")
winningVotes = 0

for candidate in List_of_Candidates:
    votes = List_of_Votes_Counted[List_of_Candidates.index(candidate)]
    pctVotes = (votes/Vote_Totals) * 100
    if votes > winningVotes:
        winner = candidate
        winningVotes = votes
    lines.append(candidate + ": " + str(round(pctVotes,2)) + "% " + "(" + str(votes) + ")")

lines.append("___________________________")
lines.append("Winner: " + winner)

for line in lines:
    print(line)
    print(line, file = resultsfile)

resultsfile.close() 
