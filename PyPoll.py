# ----PyPoll Script----

# 1. Import data from csv
# 2. Loop through data, initializing dictionary for each unique candidate. Each key is the candidate, and their running sum of votes is value
# 3. Sum the number of votes, either by counting number of dictionaries OR by creating a running tally. Location is not important here...
# 4. Complete basic stats (total votes/candidate, % votes/candidate, candidate with most votes

# Dataset is stored in Resources/election_results.csv
# We will use a relative path "Resources/election_results.csv". If this was stored in Election_Analysis itself, the relative path would just be the file name "election_results.csv"

# ----------------------------------------------------------------
# import modules
import os
import csv

# assign the RELATIVE path of our data to the file_to_load variable
file_to_load = os.path.join("Resources","election_results.csv")

# initialize a variable to hold our analysis output file, file_to_save
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize an accumulator to count our total votes
total_votes = 0

# initialize an empty list with our candidate options
candidate_options = []

# initialize an empty dictionary to contain our candidate's votes
candidate_votes = {}

# Winning Candidate and Count tracker (initialize an empty string and integers, floats)
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open election results and read the file, storing data to election_data
with open(file_to_load) as election_data:

    # the reader() function from the csv module opens the specified file and returns an iterator object that can be looped through. Each record, or row, is iterated upon
    # the csv module realizes that values are tab-delimited and thus casts each record to a list
    # each column of the CSV is a separate, indexable-item in a list. Each row is one list.
    file_reader = csv.reader(election_data)

    # Print the header row. Since file_reader is an iterator, we can use the next() function to iterate through each row individually
    # Calling next() once starts the iterator and looks at the first value, the column headers
    headers = next(file_reader)
    print(headers)


    # Analyze data
    for row in file_reader:

        # += 1 is equal to 'total_votes = total_votes + 1'. Adds one to the accumulator for every row (vote) looped through
        total_votes += 1

        # assign the third column, indexed by row[2] to the candidate_name variable
        candidate_name = row[2]

        # uses the not in membership operator to check if the value of candidate_name is contained in the list candidate_options
        # if it is not already in candidate_options, we append the value to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # if the candidate name doesn't already exist in candidate_options (a unique candidate), add a dictionary entry with key candidate_name
            # and value 0
            candidate_votes[candidate_name] = 0
        
        # since the first time the for loop sees new candidates, it adds them to the empty dictionary with key candidate_name and value 0
        # for any subsequent row, we can add +1 to the key:value pair with key candidate_name in the dictionary candidate_votes
        candidate_votes[candidate_name] += 1


    print(total_votes)
    print(candidate_options)
    print(candidate_votes)

    # We want to report the percentage of votes each candidate had.
    # Loop through each item in the candidate_votes dictionary by calling the .items() method on it
    for candidate in candidate_votes.items():
        # Access the value of each key:value pair by calling its index on candidate, then dividing by total_votes to obtain the percentage
        vote_percentage = (candidate[1]/total_votes)*100        

        # Here we check to see if each candidate's votes are greater than the last's, stored in the winning_count variable, as well as percentage
        # If both conditions are satisfied, we re-assign the winning_count variable to the current candidate's votes, candidate[1]
        # We also assign the winning_percentage to the vote_percentage, and winning_candidate to candidate[0], the key (and candidate name) of each pair
        # Since we loop through each candidate, the first loop will automatically be considered a winner, but as the loop progresses a new winner MAY BE ASSIGNED
        if (candidate[1] > winning_count) and (candidate[1] > winning_percentage):
            winning_count = candidate[1]
            winning_percentage = vote_percentage
            winning_candidate = candidate[0]

        # Use f-string formatting to access the key of each pair (candidate[0]) and insert that, as well as vote percentage for each candidate
        # Print the statement
        print(f"{candidate[0]}: {vote_percentage:.1f}% ({candidate[1]:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)


# Using a context manager, open file_to_save in write mode. Will create a new file with filename above if it doesn't exist
with open(file_to_save, "w") as txt_file:

    # \n is an ESCAPE SEQUENCE to signify starting a new line
    txt_file.write("Counties in the Election\n------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

