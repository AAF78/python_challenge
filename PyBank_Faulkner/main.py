#calc total # months included in dataset
#calc net total amount of profit/losses over entire period
#calc change in profit/losses over entire period
#calc average of changes in profit/losses
#calc greatest increase in profits GPI (date and amt)
#calc greatest decrease in profits GPD (date and amt)

# Modules
import os
import csv

# define variables
month_tot = []
net_PL = 0
delta_PL = []
previous_row = 0
GPI = 0
GPD = 0
average_change = 0
GIM = ""
GDM = ""

# Set path for file
# C:\Users\msfte\Desktop\GT-VIRT-DATA-PT-09-2022-U-LOLC\Homeworks\03-Python\Instructions\PyBank\Resources\budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")
output_data = os.path.join("Analysis", "budget_analysis.txt")
# Open and read csv and read header row
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    #print(header)
    first_record = next(csv_reader)
    month_tot.append(first_record[0])
    net_PL += int(first_record[1])
    previous_row = int(first_record[1])
    # Read through each row of data after the header
    for row in csv_reader:
        month_tot.append(row[0])
        net_PL += int(row[1])
        change = int(row[1]) - previous_row
        delta_PL.append(change)
        previous_row = int(row[1])
# Greatest Profit Increase and Decrease calculations
    GPI = max(delta_PL)
    GPD = min(delta_PL)

    min_index = delta_PL.index(GPD)
    max_index = delta_PL.index(GPI)
# gives the correct corresponding month with GPI and GPD by adding 1 to the index
    GIM = month_tot[max_index +1]
    GDM = month_tot[min_index +1]
# change, accounting for rounding to the 100th place   
    average_change = round(sum(delta_PL)/len(delta_PL), 2)
# correct formatting so the output is understandable to the user
Output = ( 
f"Financial Analysis\n"
f"  ----------------------------\n"
f"  Total Months: {len(month_tot)}\n"
f"  Total: ${net_PL}\n"
f"  Average Change: ${average_change}\n"
f"  Greatest Increase in Profits: {GIM} (${GPI})\n"
f"  Greatest Decrease in Profits: {GDM} (${GPD})\n")
print(Output)
# write the .txt file for the final output
with open(output_data, "w") as output_file:
    output_file.write(Output)