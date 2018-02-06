import os 
import csv
import string
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
employee_1 = os.path.join("employee_data1.csv")
with open (employee_1, 'r', newline = "") as csvfile: 
	employee_1 = csv.reader(csvfile, delimiter = ",")
	next(employee_1)
	employee_1 = list(employee_1)
	text_file_1 = open("Output_1.txt", "w")
	text_file_1.write("Emp ID,First Name,Last Name,DOB,SSN,State" + '\n')
	print("Emp ID,First Name,Last Name,DOB,SSN,State")
	for employee in employee_1: 
		employee[1] = employee[1].replace(" ", ",")
		employee[2] = ("/".join([employee[2][5:7], employee[2][8:10], employee[2][0:4]]))
		employee[3] = employee[3].replace(employee[3][0:6], "***-**")
		for key, value in states.items():
			if employee[4] == value:
				employee[4] = key
		print(employee[0] + "," + employee[1] + "," + employee[2] + "," + employee[3] + "," + employee[4])
		text_file_1.write(employee[0] + "," + employee[1] + "," + employee[2] + "," + employee[3] + "," + employee[4] + '\n')
	text_file_1.close()
csvfile.close()

#Open the second file and do the same things

employee_2 = os.path.join("employee_data2.csv")
with open (employee_2, 'r', newline = "") as csv_file: 
	employee_2 = csv.reader(csv_file, delimiter = ",")
	next(employee_2)
	employee_2 = list(employee_2)
	text_file_2 = open("Output_2.txt", "w")
	text_file_2.write("Emp ID,First Name,Last Name,DOB,SSN,State" + '\n')
	print("Emp ID,First Name,Last Name,DOB,SSN,State")
	for employee in employee_2: 
		employee[1] = employee[1].replace(" ", ",")
		employee[2] = ("/".join([employee[2][5:7], employee[2][8:10], employee[2][0:4]]))
		employee[3] = employee[3].replace(employee[3][0:6], "***-**")
		for key, value in states.items():
			if employee[4] == value:
				employee[4] = key
		print(employee[0] + "," + employee[1] + "," + employee[2] + "," + employee[3] + "," + employee[4])
		text_file_2.write(employee[0] + "," + employee[1] + "," + employee[2] + "," + employee[3] + "," + employee[4] + '\n')
	text_file_2.close()
csv_file.close()

