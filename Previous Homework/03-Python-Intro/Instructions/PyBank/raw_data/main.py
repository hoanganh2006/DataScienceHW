import os 
import csv
csv_file1 = os.path.join("budget_data_1.csv")
csv_file2 = os.path.join("budget_data_2.csv")
with open (csv_file1,'r' ,newline = "") as csvfile: 
	budget_data_1 = csv.reader(csvfile, delimiter = ",")
	next(budget_data_1)
	total_revenue = 0
	count = 0
	for row in budget_data_1:
		total_revenue += int(row[1])
		count += 1
	average = total_revenue/count
	print(count)
	print(average)
	print(total_revenue)