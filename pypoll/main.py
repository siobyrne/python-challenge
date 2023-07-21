#import csv module
import csv

# put csv in a variable
election_csv = "pypoll/resources/election_data.csv"


# declare variables to hold row data
voter_id = []
county = []
candidates = []

#open and read csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # store header row 
    header = next(csvfile)
    
    # iterate through rows and put data into assigned variables
    for row in csvreader:

        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
            


# get total number of votes
vote_total = len(voter_id) 

# get vote count and percentage of votes for each candidate
degette_total = candidates.count("Diana DeGette")
degette_percent = round((degette_total / vote_total) * 100, 3)
stockham_total = candidates.count("Charles Casper Stockham")
stockham_percent = round((stockham_total / vote_total) * 100, 3)
doane_total = candidates.count("Raymon Anthony Doane")
doane_percent = round((doane_total / vote_total) * 100, 3)

# print results
print(f'''
    Election Results\n
    ----------------------\n
    Total Votes: {vote_total}\n
    Charles Casper Stockham: {stockham_percent}% ({stockham_total})
    Diana DeGette: {degette_percent}% ({degette_total})
    Raymon Anthony Doane: {doane_percent}% ({doane_total})
    -----------------------
    Winner: Diana DeGette
    ''')