# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
if not os.path.exists("analysis"):  # Check if the analysis folder exists
    os.makedirs("analysis")
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define dictionary to track candidate names and vote counts
candidates = {}

# Variables for winning candidate
winning_perc = 0
winning_cand = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count by 1
        total_votes += 1

        # Get the candidate's name from the row
        cand_name = row[2]

        # If the candidate is already in the dictionary...
        if cand_name in candidates:
            candidates[cand_name] += 1  # Increment their vote count by 1
        else:  # Else...
            candidates[cand_name] = (
                1  # Add them to dictionary and give them one vote count
            )


# Open a text file to save the output
with open(file_to_output, "w+") as txt_file:

    output = []
    output.append("Election Results\n-------------------------")

    # Generate the total vote count line
    output.append(f"Total Votes: {total_votes}\n-------------------------")

    # Loop through the candidates to determine vote percentages and identify the winner
    for cand in candidates:

        # Get the vote count and calculate the percentage
        vote_count = candidates[cand]
        cand_perc = round(vote_count / total_votes * 100, 3)

        # Update the winning candidate if this one has more votes
        if winning_perc < cand_perc:
            winning_perc = cand_perc
            winning_cand = cand

        # Generate each candidate's vote count and percentage line
        output.append(f"{cand}: {cand_perc}% ({vote_count})")

    # Generate the winning candidate summary line
    output.append(
        f"-------------------------\nWinner: {winning_cand}\n-------------------------"
    )

    print("\n")
    # Print all the lines to the terminal and save them in .txt file
    for str in output:
        print(str)
        txt_file.write(str + "\n")
