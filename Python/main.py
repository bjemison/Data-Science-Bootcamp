import os 
import csv
from collections import Counter
# import the csv
csvpath = os.path.join('election_data.csv')
# calculate the total number of votes and candidate votes
total_votes = 0
candidate_votes = []
with open (csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    next(csv_reader, None)
    for row in csv_reader:
        total_votes += 1
        candidate_votes.append(row[2])
        
   
total_votes
# distinct list of all candidates and their respective number of votes
c= Counter(candidate_votes)  
c= dict(c)
type(c)
# determine the percentage of total votes each candidate received
c_percent = {k:v / total for total in (sum(c.values()),) for k, v in c.items()}
c_percent
# determine winner based on popular vote
winner = max(c, key= lambda key: c[key])
winner
# merge the count dictionary and count percentage dictionary
ml = [c,c_percent]
md= {}
for k in c.keys():
    md[k] = tuple(md[k] for md in ml)
md

# print results using the specified format
print('Election Results')
print('Total Votes: {}'.format(total_votes))
for x,y in md.items():
    print("{}: {:0.0%} ({})".format(x,y[1],y[0]))
print('Winner: {}'.format(winner))    

pypoll_file = open("pypoll.txt", "w")

# writing the text file

pypoll_file.write("Election Results \n")

pybank_file.write("-------------------------------------------- \n")

pybank_file.write("Total Months: " + str(total_months) + "\n")

pybank_file.write("Total Revenue: $" + str(total_rev) + "\n")

pybank_file.write("Average Revenue Change: $" + str(average_change) + "\n")

pybank_file.write("Greatest Increase in Revenue: Sep-15  $" + str(greatest_increase) + "\n")

pybank_file.write("Greatest Decrease in Revenue: Aug-14 $" + str(greatest_decrease))
    