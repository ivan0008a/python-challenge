import csv
import os

# Files to load and output
file_to_load = "election_data.csv"  # Input file path
file_to_output = "election_analysis.txt"  # Output file path
# Initialize variables t
total_votes = 0  # Track the tota number of votes cast
candidate_votes = {}  # Dictionary to store votes for each candidate
winning_candidate = ""  # Track a name of the winner
winning_count = 0  # Track the number of votes
winning_percentage = 0  # Track % of votes of the winner
# Open the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Skip the header row
    header = next(reader)
    # Loop through each row
    for row in reader:
        # Increment the total
        total_votes += 1
        # Get the candidate's name
        candidate_name = row[2]
        # If the candidate is not already  add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print and save the total vote count
    election_results = (
        "Election Results\n"
        "----------------------------\n"
        f"Total Votes: {total_votes}\n"
        "----------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)
    # Loop through the candidates
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage
        vote_percentage = (votes / total_votes) * 100
        # Check if this candidate is the winner
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)
    # Generate and print the winning summary
    winning_candidate_summary = (
        "----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        "----------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

