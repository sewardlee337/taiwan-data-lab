from flask import Flask, render_template, request
import sqlite3 as sql
import dataspecs, copy, urlparse

app = Flask(__name__)


####	FUNCTION FOR SQLITE DATABASE ACCESS	& MANAGEMENT	####

def get_sqldata(my_query):
	"""
	Function for preparing data from SQLite3 database for chart. 
	"""
	con = sql.connect('twdata')
	con.row_factory = sql.Row

	cur = con.cursor()
	query = my_query
	cur.execute(query) 

	return cur.fetchall()
	con.close()


def get_colnames(table, metrics_dict):
	"""
	Function for returning column names of SQLite3 table.
	"""
	colnames = list()

	con = sql.connect('twdata')
	cur = con.cursor()
	cur.execute('PRAGMA TABLE_INFO({})'.format(table))
	names = [tup[1] for tup in cur.fetchall()]

	for key in names:
		if key in metrics_dict:
			colnames.append(metrics_dict[key])
		else:
			colnames.append(key)
			
	return colnames
	con.close()


def chartjs_input(metrics_dict, sql_rows, chart_title, yaxis, table):
	"""
	Function for shaping SQLite output into form readable by Chart.js. Data from this function will be 
	converted to JSON format after being injected to HTML template via Jinja. 

	'metrics_dict' parameter is the dictionary from dataspecs module that contains reusable data charting parameters
		for Chart.js.

	'sql_rows' parameter is the output from function get_sqldata()

	'chart_title' parameter is the title of the chart created with Chart.js.

	'yaxis' parameter is label for y-axis of Chart.js chart.

	'table' parameter is the url for 'Data' tab.
	"""
	labels = list()
	for row in sql_rows:
		labels.append(row['year'])

	data = dict()								
	data['labels'] = labels
	all_datasets = list()

	for key in metrics_dict:

		dataset = list()
		for row in sql_rows:
			dataset.append(row[key])

		dataset_contents = dataspecs.data_dict						
		dataset_contents['label'] = metrics_dict[key]
		dataset_contents['backgroundColor'] = dataspecs.colors[key] % '0.4'
		dataset_contents['borderColor'] = dataspecs.colors[key] % '1'
		dataset_contents['pointBorderColor'] = dataspecs.colors[key] % '1'
		dataset_contents['pointHoverBackgroundColor'] = dataspecs.colors[key] %'1'
		dataset_contents['data'] = dataset					

		all_datasets.append(copy.copy(dataset_contents))

	data['datasets'] = all_datasets		

	return render_template('graph.html', data = data, chart_title = chart_title, yaxis = yaxis, table = table)


####	CONSTRUCT PAGES		####


@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/thanks")
def thanks():
	return render_template('thanks.html')

@app.route("/construction")
def construction():
	return render_template('construction.html')

@app.route("/data")
def datapage():
	description = "Access datasets available on Taiwan Data Lab with the menu to the right. New datasets will be periodically added."
	return render_template('data.html', description = description)


@app.route("/data/natl-accounts-figs")
def natl_accounts_figs():
	rows = get_sqldata('select year, round(ngdp / deflator, 0) as rgdp from accounts_figs')

	labels = list()
	for row in rows:
		labels.append(row['year'])

	rgdp = list()
	for row in rows:
		rgdp.append(row['rgdp'])

	data = dict()
	data['labels'] = labels
	dataset_contents = dataspecs.data_dict

	dataset_contents['label'] = "Real GDP at 2011 Prices"
	dataset_contents['data'] = rgdp
	data['datasets'] = [dataset_contents]

	return render_template('graph.html', data = data, chart_title = "National Accounts: Principal Figures", table = "/data/natl-accounts-figs/table")


@app.route("/data/natl-accounts-activity")
def national_accounts_activity():
	rows = get_sqldata("select * from accounts_activity where metric = 'rGDP'")
	return chartjs_input(dataspecs.industry, rows, "National Accounts: GDP by Production Activity", 
		"Chained (2011) Dollars, Millions NT$", "/data/natl-accounts-activity/table")




@app.route("/data/labor-employment-edu")
def labor_employment_edu():
	rows = get_sqldata("select * from labor_employ_edu where month = 'Ave.'")
	return chartjs_input(dataspecs.edu, rows, "Labor Force: Employment by Sex and Education Attainment", 
		"Thousands of persons", "/data/labor-employment-edu/table")

@app.route("/data/labor-employment-edu/table")
def labor_employment_edu_tab():
	colnames = get_colnames('labor_employ_edu', dataspecs.edu)
	rows = get_sqldata("select * from labor_employ_edu")
	return render_template('table.html', units = 'Thousands of persons', colnames = colnames, rows = rows)




@app.route("/data/labor-employment-age")
def labor_employment_age():
	rows = get_sqldata("select * from labor_employ_age where month = 'Ave.'")
	return chartjs_input(dataspecs.age, rows, "Labor Force: Employment by Age", 
		"Thousands of persons", "/data/labor-employment-age/table")

@app.route("/data/labor-employment-industry")
def labor_employment_industry():
	rows = get_sqldata("select * from labor_employ_industry where month = 'Ave.'")
	return chartjs_input(dataspecs.industry, rows, "Labor Force: Employment by Industry", 
		"Thousands of persons", "/data/labor-employment-industry/table")

@app.route("/data/labor-employment-occupation")
def labor_employment_occupation():
	rows = get_sqldata("select * from labor_employ_occupation where month = 'Ave.'")
	return chartjs_input(dataspecs.occupation, rows, "Labor Force: Employment by Occupation", 
		"Thousands of persons", "/data/labor-employment-occupation/table")	

@app.route("/data/labor-employment-class")
def labor_employment_class():
	rows = get_sqldata("select * from labor_employ_class where month = 'Ave.'")
	return chartjs_input(dataspecs.labor_employ_class, rows, "Labor Force: Employment by Class of Workers", 
		"Thousands of persons", "/data/labor-employment-class/table")

@app.route("/data/labor-unemployment-edu")
def labor_unemployment_edu():
	rows = get_sqldata("select * from labor_unemploy_edu where month = 'Ave.'")
	return chartjs_input(dataspecs.edu, rows, "Labor Force: Unemployment by Sex and Education Attainment", 
		"Thousands of persons", "/data/labor-unemployment-edu/table")

@app.route("/data/labor-unemployment-age")
def labor_unemployment_age():
	rows = get_sqldata("select * from labor_unemploy_age where month = 'Ave.'")
	return chartjs_input(dataspecs.age, rows, "Labor Force: Unemployment by Age", 
		"Thousands of persons", "/data/labor-unemployment-age/table")

@app.route("/data/labor-unemployment-reason")
def labor_unemployment_reason():
	rows = get_sqldata("select * from labor_unemploy_age where month = 'Ave.'")
	return chartjs_input(dataspecs.labor_unemploy_reason, rows, "Labor Force: Unemployment by Reason", 
		"Thousands of persons", "/data/labor-unemployment-reason/table")

@app.route("/data/labor-notlaborforce")
def labor_notlaborforce():
	rows = get_sqldata("select * from labor_notlaborforce where month ='Ave.'")
	return chartjs_input(dataspecs.labor_notlaborforce, rows, "Labor Force: Not in Labor Force", 
		"Thousands of persons", "/data/labor-notlaborforce/table")

@app.route("/data/labor-participation-edu")
def labor_participation_edu():
	rows = get_sqldata("select * from labor_participation_edu where month = 'Ave.'")
	return chartjs_input(dataspecs.edu, rows, "Labor Force: Labor Force Participation Rate by Sex, Education Attainment", 
		"Percent (%)", "/data/labor-participation-edu/table")

@app.route("/data/labor-participation-age")
def labor_participation_age():
	rows = get_sqldata("select * from labor_participation_age where month = 'Ave.'")
	return chartjs_input(dataspecs.age, rows, "Labor Force: Labor Force Participation Rate by Age", 
		"Percent (%)", "/data/labor-participation-age/table")

@app.route("/data/labor-unemploymentrate-edu")
def labor_unemploymentrate_edu():
	rows = get_sqldata("select * from labor_unemployrate_edu where month = 'Ave.'")
	return chartjs_input(dataspecs.edu, rows, "Labor Force: Unemployment Rate by Sex, Educational Attainment", 
		"Percent (%)", "/data/labor-unemploymentrate-edu/table")

@app.route("/data/labor-unemploymentrate-age")
def labor_unemploymentrate_age():
	rows = get_sqldata("select * from labor_unemployrate_age where month = 'Ave.'")
	return chartjs_input(dataspecs.age, rows, "Labor Force: Unemployment Rate by Age", 
		"Percent (%)", "/data/labor-unemploymentrate-age/table")

@app.route("/data/green-air")
def green_air():
	rows = get_sqldata("select * from green_air")
	return chartjs_input(dataspecs.green_air, rows, "Emmission Account of Pollution", 
		"Tons", "/data/green-air/table")

@app.route("/data/social-population")
def social_population():
	rows = get_sqldata("select * from social_pop")
	return chartjs_input(dataspecs.sex, rows, "Population Composition by Sex", 
		"Thousands of persons", "/data/social-population/table")

@app.route("/data/price-index")
def price_index():
	rows = get_sqldata("select * from price_index")
	return chartjs_input(dataspecs.price_index, rows, "Price Indices (N.T.D. Basis)", 
		"Base Period: 2011 = 100", "/data/price-index/table")

@app.route("/data/price-index-change")
def price_index_change():
	rows = get_sqldata("select * from price_index_change")
	return chartjs_input(dataspecs.price_index, rows, "Annual Change of Price Indices (N.T.D. Basis)", 
		"Percent (%)", "/data/price-index-change/table")






if __name__ == "__main__":
	app.run()