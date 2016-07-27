from flask import Flask, render_template, request, redirect, g
import sqlite3 as sql
import dataspecs, copy

app = Flask(__name__)


####	FUNCTION FOR SQLITE DATABASE ACCESS		####

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


####	DATA STRUCTURES FOR CHART.JS 		####

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


def chartjs_input(metrics_dict, sql_rows, chart_title, yaxis):
	"""
	Function for shaping SQLite output into form readable by Chart.js. Data from this function will be 
	converted to JSON format after being injected to HTML template via Jinja. 
	"""
	labels = list()
	for row in sql_rows:
		labels.append(row['year'])

	data = dict()								
	data['labels'] = labels
	all_datasets = list()

	for key in metrics_dict:								#	This for-loop extracts all the datasets that you want graphed

		dataset = list()
		for row in sql_rows:								#	Use loop to extract relevant dataset from SQL query output
			dataset.append(row[key])

		dataset_contents = data_dict						
		dataset_contents['label'] = metrics_dict[key]
		dataset_contents['backgroundColor'] = dataspecs.colors[key] % '0.4'
		dataset_contents['borderColor'] = dataspecs.colors[key] % '1'
		dataset_contents['pointBorderColor'] = dataspecs.colors[key] % '1'
		dataset_contents['pointHoverBackgroundColor'] = dataspecs.colors[key] %'1'
		dataset_contents['data'] = dataset					

		all_datasets.append(copy.copy(dataset_contents))	#	Append current dataset

	data['datasets'] = all_datasets		

	return render_template('graph.html', data = data, chart_title = chart_title, yaxis = yaxis)


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
	return render_template('data.html')


@app.route("/data/natl-accounts-figs/graph")				
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
	dataset_contents = data_dict

	dataset_contents['label'] = "Real GDP at 2011 Prices"
	dataset_contents['data'] = rgdp
	data['datasets'] = [dataset_contents]

	return render_template('graph.html', data = data, chart_title = "National Accounts: Principal Figures")



@app.route("/data/natl-accounts-activity/graph")
def national_accounts_activity():
	rows = get_sqldata("select * from accounts_activity where metric = 'rGDP'")

	return chartjs_input(dataspecs.industry, rows, "National Accounts: GDP by Production Activity", "Chained (2011) Dollars, Millions NT$")

@app.route("/data/labor-employment-edu/graph")
def labor_employment_edu():
	rows = get_sqldata("select * from labor_employ_edu where month = 'Ave.'")

	return chartjs_input(dataspecs.labor_employ_edu, rows, "Labor Force: Employment by Sex and Education Attainment", "Thousands of persons")

@app.route("/data/labor-employment-age/graph")
def labor_employment_age():
	rows = get_sqldata("select * from labor_employ_age where month = 'Ave.'")

	return chartjs_input(dataspecs.labor_employ_age, rows, "Labor Force: Employment by Age", "Thousands of persons")

@app.route("/data/labor-employment-industry/graph")
def labor_employment_industry():
	rows = get_sqldata("select * from labor_employ_industry where month = 'Ave.'")

	return chartjs_input(dataspecs.industry, rows, "Labor Force: Employment by Industry", "Thousands of persons")

@app.route("/data/labor-employment-occupation/graph")
def labor_employment_occupation():
	rows = get_sqldata("select * from labor_employ_occupation where month = 'Ave.'")

	return chartjs_input(dataspecs.occupation, rows, "Labor Force: Employment by Occupation", "Thousands of persons")	



if __name__ == "__main__":
	app.run()