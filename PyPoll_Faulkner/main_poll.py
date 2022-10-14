#total number of votes cast
#complete list of candidates who received votes
#percentage of votes each candidate won
#total number of votes each candidate won
#winner of the election based on popular vote

# Formatted Appearance:
  #Election Results
  #-------------------------
  #Total Votes: 369711
  #-------------------------
  #Charles Casper Stockham: 23.049% (85213)
  #Diana DeGette: 73.812% (272892)
  #Raymon Anthony Doane: 3.139% (11606)
  #-------------------------
  #Winner: Diana DeGette
  #-------------------------

# Modules
import os
import csv

# define variables and set values
#the first column called ballot id = vote_count
vote_count = []
#the sum of all the votes of all the candidates = vote_total
vote_total = 0
count = 0
#container to put all three candidates' names in
candidates_list = []
candidates_names = []
#the number of votes in total for each candidate = total_candidate_votes
total_candidate_votes = {}
#an empty string to name the overall winner of the election
election_winner = ""


# Set paths for file to use and file to write
election_data = os.path.join("Resources", "election_data.csv")
output_data = os.path.join("Analysis", "election_analysis.txt")
# Open and read csv and read header row
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    #print(header) to check and see that the csv is readable, skip the header
   
    # Read through each row of data after the header
    for row in csv_reader:
      vote_count.append(row[0])
      candidates_names = row[2]
      count += 1
        #print(row), this overwrites the initial 0 I set the variable at
      vote_total = vote_total +1
    #print(vote_total)

    # count the votes for each
    if candidates_names not in candidates_list:
      candidates_list.append(candidates_names)
      total_candidate_votes[candidates_names] = 0
      total_candidate_votes[candidates_names] += 1
    else:
      total_candidate_votes[candidates_names] += 1



Output = ( 
f"Election Results\n"
f"  ----------------------------\n"
f"  Total Votes: {vote_total}\n"
f"  ----------------------------\n"
f""
f""
f""
f"  ----------------------------\n"
f"  Winner: {election_winner}\n"
f"  ----------------------------\n")
print(Output)

#write the .txt file for the final output
with open(output_data, "w") as output_file:
  output_file.write(Output)
