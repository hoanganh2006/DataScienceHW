import os
import csv
election_1 = os.path.join("election_data_1.csv")
with open (election_1, 'r', newline = "") as csvfile: 
	election_data_1 = csv.reader(csvfile, delimiter = ",")
	next(election_data_1)
	text_file_1 = open("Output_1.txt", "w")
	election_data_1 = list(election_data_1)
	total_votes = len(election_data_1)
	candidate = {}
	number_of_election = 0
	for row in election_data_1: 
		if row[2] not in candidate.keys():
			number_of_election = 0
			candidate.update({row[2]: number_of_election})
		if row[2] in candidate.keys(): 
			candidate[row[2]] += 1
	print("Election Results")
	text_file_1.write("Election Results" + '\n')
	print("-----------------------------------")
	text_file_1.write("-----------------------------------" + '\n')
	print("Total Votes: " + str(total_votes))
	text_file_1.write("Total Votes: " + str(total_votes) + '\n')
	print("-----------------------------------")
	text_file_1.write("-----------------------------------" + '\n')
	for keys, values in candidate.items():
		print(keys + " : " + str((values/total_votes)*100) +"%" + " (" + str(values) + ")")
		text_file_1.write(keys + " : " + str((values/total_votes)*100) +"%" + " (" + str(values) + ")" + '\n')
	print("-----------------------------------")
	text_file_1.write("-----------------------------------" + '\n')
	winner = max(candidate.values())
	for key, value in candidate.items():
		if winner == value: 
			print("Winner: " + key)
			text_file_1.write("Winner: " + key + '\n')
	print("-----------------------------------")
	text_file_1.write("-----------------------------------" + '\n')
text_file_1.close()
csvfile.close()

#Open the second file and do the same things

election_2 = os.path.join("election_data_2.csv")
with open (election_2, 'r', newline = "") as csvfile:
	election_data_2 = csv.reader(csvfile, delimiter = ",")
	next(election_data_2)
	text_file_2 = open("Output_2.txt", "w")
	election_data_2 = list(election_data_2)
	total_votes = len(election_data_2)
	candidate = {}
	number_of_election = 0
	for row in election_data_2: 
		if row[2] not in candidate.keys():
			number_of_election = 0
			candidate.update({row[2]: number_of_election})
		if row[2] in candidate.keys(): 
			candidate[row[2]] += 1
	print("Election Results")
	text_file_2.write("Election Results" + '\n')
	print("-----------------------------------")
	text_file_2.write("-----------------------------------" + '\n')
	print("Total Votes: " + str(total_votes))
	text_file_2.write("Total Votes: " + str(total_votes) + '\n')
	print("-----------------------------------")
	text_file_2.write("-----------------------------------" + '\n')
	for keys, values in candidate.items():
		print(keys + " : " + str((values/total_votes)*100) +"%" + " (" + str(values) + ")")
		text_file_2.write(keys + " : " + str((values/total_votes)*100) +"%" + " (" + str(values) + ")" + '\n')
	print("-----------------------------------")
	text_file_2.write("-----------------------------------" + '\n')
	winner = max(candidate.values())
	for key, value in candidate.items():
		if winner == value: 
			print("Winner: " + key)
			text_file_2.write("Winner: " + key + '\n')
	print("-----------------------------------")
	text_file_2.write("-----------------------------------" + '\n')
text_file_2.close()
csvfile.close()


