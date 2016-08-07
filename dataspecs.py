"""
This Python script contains the names of datasets to be charted in Chart.js.
"""

data_dict = {'fill': False, 
			            'lineTension': 0.1,			            			      
			            'borderCapStyle': 'butt',
			            'borderDash': [],
			            'borderDashOffset': 0.0,
			            'borderJoinStyle': 'miter',
			            'pointBackgroundColor': "#fff",
			            'pointBorderWidth': 1,
			            'pointHoverRadius': 5,
			            'pointHoverBorderColor': "rgba(220,220,220,1)",
			            'pointHoverBorderWidth': 2,
			            'pointRadius': 1,
			            'pointHitRadius': 10,								
			            'spanGaps': False,
			        }


gdp = {
	'G': 'GDP', 'A': 'Private Final Consumption Expenditure', 'B': 'Government Final Consumption Expenditure',
	'C': 'Gross Fixed Capital Formation', 'D': 'Changes in Inventories', 'E': 'Exports of Goods and Services',
	'F': 'Imports of Goods and Services'	
}



industry = {
	'A': 'Agriculture, Forestry, Fishing, Animal Husbandry', 'B': 'Mining and Quarrying',
	'C': 'Manufacturing', 'D': 'Electricity and Gas Supply', 'E': 'Water Supply and Remediation Services',
	'F': 'Construction', 'G': 'Wholesale and Retail Trade', 'H': 'Transportation and Storage',
	'I': 'Accomodation and Food Storage', 'J': 'Information and Communication', 
	'K': 'Finance and Insurance', 'L': 'Real Estate and Ownership of Dwellings',
	'M': 'Professional, Scientific, Technical Services', 'N': 'Support Services',
	'O': 'Public Administration and Defense; Compulsory Social Security', 'P': 'Education', 
	'Q': 'Human, Health, Social Work Services', 'R': 'Arts, Entertainment, Recreation', 'S': 'Other Services'
}

activity = {
	'A': 'Total GDP', 'B': 'Total GDP (production approach)', 'C': 'Agriculture, Forestry, Fishing, Animal Husbandry', 'D': 'Mining and Quarrying',
	'E': 'Manufacturing', 'F': 'Electricity and Gas Supply', 'G': 'Water Supply and Remediation Services',
	'H': 'Construction', 'I': 'Wholesale and Retail Trade', 'J': 'Transportation and Storage',
	'K': 'Accomodation and Food Storage', 'L': 'Information and Communication', 
	'M': 'Finance and Insurance', 'N': 'Real Estate and Ownership of Dwellings',
	'O': 'Professional, Scientific, Technical Services', 'P': 'Support Services',
	'Q': 'Public Administration and Defense; Compulsory Social Security', 'R': 'Education', 
	'S': 'Human, Health, Social Work Services', 'T': 'Arts, Entertainment, Recreation', 'U': 'Other Services',
	'V': 'Import Duties', 'W': 'Value-Added Tax'
}

occupation = {
	'A': 'Total', 'B': 'Legislators, senior officials, managers', 'C': 'Professionals', 
	'D': 'Technicians and associate professionals', 'E': 'Clerical support workers', 'F': 'Service and sales workers',
	'G': 'Skilled agricultural, forestry, fishery workers', 'H': 'Craft & machine operation-related workers'
}

colors = {
	'A': 'rgba(96, 189, 104, %s)', 'B': 'rgba(93, 165, 218, %s)', 'C': 'rgba(77, 77, 77, %s)',
	'D': 'rgba(250, 164, 58, %s)', 'E': 'rgba(241, 124, 176, %s)', 'F': 'rgba(241, 88, 84, %s)',
	'G': 'rgba(178, 118, 178, %s)', 'H': 'rgba(222, 207, 63, %s)', 'I': 'rgba(178, 145, 47, %s)',
	'J': 'rgba(96, 189, 104, %s)', 'K': 'rgba(93, 165, 218, %s)', 'L': 'rgba(77, 77, 77, %s)',
	'M': 'rgba(250, 164, 58, %s)', 'N': 'rgba(241, 124, 176, %s)', 'O': 'rgba(241, 88, 84, %s)',
	'P': 'rgba(178, 118, 178, %s)', 'Q': 'rgba(96, 189, 104, %s)', 'R': 'rgba(93, 165, 218, %s)',
	'S': 'rgba(77, 77, 77, %s)', 'T': 'rgba(250, 164, 58, %s)', 'U': 'rgba(241, 124, 176, %s)',
	'V': 'rgba(241, 88, 84, %s)', 'W': 'rgba(178, 118, 178, %s)'
}

edu = {
	'A': 'Total', 'B': 'Male', 'C': 'Female', 'D': 'Primary school & below', 'E': 'Junior high', 
	'F': 'Senior high', 'G': 'Vocational', 'H': 'Junior college', 'I': 'University & graduate school'
}

age = {
	'A': 'Total', 'B': '15 ~ 19 years', 'C': '20 ~ 24 years', 'D': '25 ~ 29 years',
	'E': '30 ~ 34 years', 'F': '35 ~ 39 years', 'G': '40 ~ 44 years', 'H': '45 ~ 49 years', 
	'I': '50 ~ 54 years', 'J': '55 ~ 59 years', 'K': '60 ~ 64 years', 'L': '65 years & older'
}

labor_employ_class = {
	'A': 'Total', 'B': 'Employers', 'C': 'Own-account workers', 'D': 'Unpaid family workers', 
	'E': 'Paid employees - Private', 'F': 'Paid employees - Government'
}

labor_unemploy_reason = {
	'A': 'Total', 'B': 'New job seeker', 'C': 'Business shrunk or establishment closed', 'D': 'Not satisfied with job', 'E': 'Ill health',
	'F': 'Seasonal or temporary work completed', 'G': 'Female got married or gave birth', 'H': 'Retirement', 'I': 'Busy in housekeeping',
	'J': 'Other'
}

labor_notlaborforce = {
	'A': 'Total', 'B': 'Intend and available to work, but not seeking', 'C': 'Attending school or preparing for entrance exams',
	'D': 'Housekeeping', 'E': 'Old age & disabled', 'F': 'Other'
}

green_air ={
	'A': 'Total', 'B': 'TSP (including PM2.5)', 'C': 'PM2.5', 'D': 'SOx', 'E': 'NOx', 'F': 'NMHC', 'G': 'CO', 'H': 'Pb'
}

sex = {
	'A': 'Total', 'B': 'Male', 'C': 'Female'
}

sex_marriage = {
	'A': 'Male', 'B': 'Female'
}

price_index = {
	'A': 'Export Price Index', 'B': 'Construction Price Index', 'C': 'Consumer Price Index', 'D': 'Wholesale Price Index', 
	'E': 'Import Price Index' 
}

life_expectancy = {
	'A': '0 years', 'B': '10 years', 'C': '20 years', 'D': '30 years', 'E': '40 years', 'F': '50 years', 'G': '60 years',
	'H': '70 years', 'I': '80 years'
}

births = {
	'A': 'Total', 'B': 'Legitimate', 'C': 'Births outside marriage', 'D': 'Births outside marriage acknowledged by father',
	'E': 'Births outside marriage unacknowledged'
}

recycling = {
	'A': 'Total', 'B': 'Paper', 'C': 'Used clothing', 'D': 'Metal cans, aluminum cans, other metal products', 'E': 'Glass containers',
	'F': 'Aseptic containers', 'G': 'Paper containers', 'H': 'Agricultural chemicals containers, special environmental agents waste containers',
	'I': 'Plastic containers', 'J': 'Plastic packaging', 'K': 'Tires', 'L': 'Dry batteries', 'M': 'Lead-acid accumulators',
	'N': 'Home electrical appliances', 'O': 'Computers', 'P': 'Disc', 'Q': 'Mobile phone', 'R': 'Lighting', 'S': 'Cooking oil', 'T': 'Other'
}

water = {
	'A': 'BOD', 'B': 'COD', 'C': 'SS'
}

edu_enrollment = {
	'A': 'Primary education', 'B': 'Secondary education', 'C': 'Tertiary education'
}

edu_attainment = {
	'A': 'Junior high school and below', 'B': 'Senior high school and vocational school', 'C': 'Junior college and above'
}

deaths = {
	'A': 'Malignant neoplasms', 'B': 'Heart disease', 'C': 'Cerebro vascular disease', 'D': 'Diabetes mellitus', 'E': 'Pneumonia',
	'F': 'Accidents', 'G': 'Chronic lower respiratory diseases', 'H': 'Chronic liver disease & cirrhosis', 'I': 'Hypertensive disease',
	'J': 'Suicide', 'K': 'Nephritis, nephrotic syndrome, nephrosis'
}