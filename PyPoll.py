# ----PyPoll Script----

# 1. Import data from csv
# 2. Loop through data, initializing dictionary for each unique candidate, paired with the location of the vote
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

# open election results and read the file, storing data to election_data
with open(file_to_load) as election_data:

    # the reader() function from the csv module opens the specified file and returns an iterator object that can be looped through. Each record, or row, is iterated upon
    # the csv module realizes that values are tab-delimited and thus casts each record to a list, with each column of the CSV a separate item
    file_reader = csv.reader(election_data)

    # Print the header row. Since file_reader is an iterator, we can use the next() function to iterate through each row individually
    # Calling next() once starts the iterator and looks at the first value, the column headers
    headers = next(file_reader)
    print(headers)


# Analyze data




# Using a context manager, open file_to_save in write mode. Will create a new file with filename above if it doesn't exist
with open(file_to_save, "w") as txt_file:

    # \n is an ESCAPE SEQUENCE to signify starting a new line
    txt_file.write("Counties in the Election\n------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

