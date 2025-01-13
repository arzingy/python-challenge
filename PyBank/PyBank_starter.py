# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
if not os.path.exists("analysis"):  # Check if the analysis folder exists
    os.makedirs("analysis")
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change
    first_row = next(reader)
    last_num = int(first_row[1])

    # Track the total and net change
    total = last_num
    net_change = []
    # Variables for greatest increase, decrease and their months
    greatest_increase = 0
    gr_in_month = ""
    greatest_decrease = 0
    gr_de_month = ""

    # Process each row of data
    for row in reader:

        # Track the total
        total += int(row[1])

        # Track current profit/loss
        curr_num = int(row[1])

        # Track net change
        curr_change = curr_num - last_num

        # Calculate the greatest increase in profits (month and amount)
        if curr_change > greatest_increase:
            greatest_increase = curr_change
            gr_in_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        elif curr_change < greatest_decrease:
            greatest_decrease = curr_change
            gr_de_month = row[0]

        # Add current net change to the list of net changes
        net_change.append(curr_change)
        # Now current profit/loss will be last profit/loss for next row
        last_num = curr_num


# Calculate the average net change across the months
average_net_change = round(sum(net_change) / len(net_change), 2)

# Write the results to a text file and print them to the terminal
with open(file_to_output, "w") as txt_file:

    output = []
    output.append(f"Financial Analysis")
    output.append("-----------------------------")
    output.append(f"Total Months: {len(net_change) + 1}") # Total months is the number of net changes + 1st month
    output.append(f"Total: ${total}")
    output.append(f"Average Change: ${average_net_change}")
    output.append(f"Greatest Increase in Profits: {gr_in_month} (${greatest_increase})")
    output.append(f"Greatest Decrease in Profits: {gr_de_month} (${greatest_decrease})")

    for str in output:
        print(str)
        txt_file.write(str + "\n")
