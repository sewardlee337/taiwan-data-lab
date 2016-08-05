from flask import Flask, render_template, request
import dataspecs, dataquery, urlparse

app = Flask(__name__)




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


####	National Accounts: GDP (nominal)
@app.route("/data/natlaccounts-ngdp")
def natlaccounts_ngdp():
	rows = dataquery.get_sqldata("select * from accounts_ngdp")
	return dataquery.chartjs_input(dataspecs.gdp, rows, "National Accounts: GDP (nominal)",
		"Million NT$, current prices", "/data/natlaccounts-ngdp/table")

@app.route("/data/natlaccounts-ngdp/table")
def natlaccounts_ngdp_tab():
	colnames = dataquery.get_colnames('accounts_ngdp', dataspecs.gdp)
	rows = dataquery.get_sqldata("select * from accounts_ngdp")
	return render_template('table.html', units = "Million NT$, current prices", colnames = colnames, rows = rows,
		title = "National Accounts: GDP (nominal)")


####	National Accounts: GDP (real)
@app.route("/data/natlaccounts-rgdp")
def natlaccounts_rgdp():
	rows = dataquery.get_sqldata("select * from accounts_rgdp")
	return dataquery.chartjs_input(dataspecs.gdp, rows, "National Accounts: GDP (real)",
		"Million NT$, chained 2011 dollars", "/data/natlaccounts-rgdp/table")

@app.route("/data/natlaccounts-rgdp/table")
def natlaccounts_rgdp_tab():
	colnames =dataquery.get_colnames('accounts_rgdp', dataspecs.gdp)
	rows = dataquery.get_sqldata("select * from accounts_rgdp")
	return render_template('table.html', units = "Million NT$, chained 2011 dollars", colnames = colnames, rows = rows,
		title = "National Accounts: GDP (real)")


####	National Accounts: GDP by Activity (nominal)
@app.route("/data/natlaccounts-ngdp-activity")
def natlaccounts_ngdp_activity():
	rows = dataquery.get_sqldata("select * from accounts_ngdp_activity")
	return dataquery.chartjs_input(dataspecs.activity, rows, "National Accounts: GDP by Activity (nominal)",
		"Million NT$, current prices", "/data/natlaccounts-ngdp-activity/table")

@app.route("/data/natlaccounts-ngdp-activity/table")
def natlaccounts_ngdp_activity_tab():
	colnames = dataquery.get_colnames('accounts_ngdp_activity', dataspecs.activity)
	rows = dataquery.get_sqldata("select * from accounts_ngdp_activity")
	return render_template('table.html', units = "Million NT$, current prices", colnames = colnames, rows = rows,
		title = "National Accounts: GDP by Activity (nominal)")


####	National Accounts: GDP by Activity (real)
@app.route("/data/natlaccounts-rgdp-activity")
def natlaccounts_rgdp_activity():
	rows = dataquery.get_sqldata("select * from accounts_rgdp_activity")
	return dataquery.chartjs_input(dataspecs.activity, rows, "National Accounts: GDP by Activity (real)",
		"Million NT$, chained 2011 dollars", "/data/natlaccounts-rgdp-activity/table")

@app.route("/data/natlaccounts-rgdp-activity/table")
def natlaccounts_rgdp_activity_tab():
	colnames = dataquery.get_colnames('accounts_rgdp_activity', dataspecs.activity)
	rows = dataquery.get_sqldata("select * from accounts_rgdp_activity")
	return render_template('table.html', units = "Million NT$, chained 2011 dollars", colnames = colnames, rows = rows,
		title = "National Accounts: GDP by Activity (real)")


####	Labor Force: Employment by Sex and Educational Attainment
@app.route("/data/labor-employment-edu")
def labor_employment_edu():
	rows = dataquery.get_sqldata("select * from labor_employ_edu where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.edu, rows, "Labor Force: Employment by Sex and Education Attainment", 
		"Thousands of persons", "/data/labor-employment-edu/table")

@app.route("/data/labor-employment-edu/table")
def labor_employment_edu_tab():
	colnames = dataquery.get_colnames('labor_employ_edu', dataspecs.edu)
	rows = dataquery.get_sqldata("select * from labor_employ_edu")
	return render_template('table.html', units = 'Thousands of persons', colnames = colnames, rows = rows, 
		title = "Labor Force: Employment by Sex and Education Attainment")


####	Labor Force: Employment by Age
@app.route("/data/labor-employment-age")
def labor_employment_age():
	rows = dataquery.get_sqldata("select * from labor_employ_age where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.age, rows, "Labor Force: Employment by Age", 
		"Thousands of persons", "/data/labor-employment-age/table")

@app.route("/data/labor-employment-age/table")
def labor_employment_age_tab():
	colnames = dataquery.get_colnames('labor_employ_age', dataspecs.age)
	rows = dataquery.get_sqldata("select * from labor_employ_age")
	return render_template('table.html', units = 'Thousands of persons', colnames = colnames, rows = rows,
		title = "Labor Force: Employment by Age")


####	Labor Force: Employment by Industry
@app.route("/data/labor-employment-industry")
def labor_employment_industry():
	rows = dataquery.get_sqldata("select * from labor_employ_industry where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.industry, rows, "Labor Force: Employment by Industry", 
		"Thousands of persons", "/data/labor-employment-industry/table")

@app.route("/data/labor-employment-industry/table")
def labor_employment_industry_tab():
	colnames = dataquery.get_colnames("labor_employ_industry", dataspecs.industry)
	rows = dataquery.get_sqldata("select * from labor_employ_industry")
	return render_template('table.html', units = 'Thousands of persons', colnames = colnames, rows = rows,
		title = "Labor Force: Employment by Industry")


####	Labor Force: Employment by Occupation
@app.route("/data/labor-employment-occupation")
def labor_employment_occupation():
	rows = dataquery.get_sqldata("select * from labor_employ_occupation where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.occupation, rows, "Labor Force: Employment by Occupation", 
		"Thousands of persons", "/data/labor-employment-occupation/table")	

@app.route("/data/labor-employment-occupation/table")
def labor_employment_occupation_tab():
	colnames = dataquery.get_colnames("labor_employ_occupation", dataspecs.occupation)
	rows = dataquery.get_sqldata("select * from labor_employ_occupation")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Employment by Occupation")


####	Labor Force: Employment by Class
@app.route("/data/labor-employment-class")
def labor_employment_class():
	rows = dataquery.get_sqldata("select * from labor_employ_class where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.labor_employ_class, rows, "Labor Force: Employment by Class of Workers", 
		"Thousands of persons", "/data/labor-employment-class/table")

@app.route("/data/labor-employment-class/table")
def labor_employment_class_tab():
	colnames = dataquery.get_colnames("labor_employ_class", dataspecs.labor_employ_class)
	rows = dataquery.get_sqldata("select * from labor_employ_class")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Employment by Class")


####	Labor Force: Unemployment by Sex and Education Attainment
@app.route("/data/labor-unemployment-edu")
def labor_unemployment_edu():
	rows = dataquery.get_sqldata("select * from labor_unemploy_edu where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.edu, rows, "Labor Force: Unemployment by Sex and Education Attainment", 
		"Thousands of persons", "/data/labor-unemployment-edu/table")

@app.route("/data/labor-unemployment-edu/table")
def labor_unemployment_edu_tab():
	colnames = dataquery.get_colnames("labor_employ_edu", dataspecs.edu)
	rows = dataquery.get_sqldata("select * from labor_employ_edu")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment by Sex and Education Attainment")


####	Labor Force: Unemployment by Age
@app.route("/data/labor-unemployment-age")
def labor_unemployment_age():
	rows = dataquery.get_sqldata("select * from labor_unemploy_age where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.age, rows, "Labor Force: Unemployment by Age", 
		"Thousands of persons", "/data/labor-unemployment-age/table")

@app.route("/data/labor-unemployment-age/table")
def labor_unemployment_age_tab():
	colnames = dataquery.get_colnames("labor_unemploy_age", dataspecs.age)
	rows = dataquery.get_sqldata("select * from labor_unemploy_age")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment by Age")


####	Labor Force: Unemployment by Reason
@app.route("/data/labor-unemployment-reason")
def labor_unemployment_reason():
	rows = dataquery.get_sqldata("select * from labor_unemploy_reason where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.labor_unemploy_reason, rows, "Labor Force: Unemployment by Reason", 
		"Thousands of persons", "/data/labor-unemployment-reason/table")

@app.route("/data/labor-unemployment-reason/table")
def labor_unemployment_reason_tab():
	colnames = dataquery.get_colnames("labor_unemploy_reason", dataspecs.labor_unemploy_reason)
	rows = dataquery.get_sqldata("select * from labor_unemploy_reason")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment by Reason")


####	Labor Force: Not in Labor Force
@app.route("/data/labor-notlaborforce")
def labor_notlaborforce():
	rows = dataquery.get_sqldata("select * from labor_notlaborforce where month ='Ave.'")
	return dataquery.chartjs_input(dataspecs.labor_notlaborforce, rows, "Labor Force: Not in Labor Force", 
		"Thousands of persons", "/data/labor-notlaborforce/table")

@app.route("/data/labor-notlaborforce/table")
def labor_notlaborforce_tab():
	colnames = dataquery.get_colnames("labor_notlaborforce", dataspecs.labor_notlaborforce)
	rows = dataquery.get_sqldata("select * from labor_notlaborforce")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Not in Labor Force")


####	Labor Force: Labor Force Participation Rate by Sex, Education Attainment
@app.route("/data/labor-participation-edu")
def labor_participation_edu():
	rows = dataquery.get_sqldata("select * from labor_participation_edu where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.edu, rows, "Labor Force: Labor Force Participation Rate by Sex, Education Attainment", 
		"Percent (%)", "/data/labor-participation-edu/table")

@app.route("/data/labor-participation-edu/table")
def labor_participation_edu_tab():
	colnames = dataquery.get_colnames("labor_participation_edu", dataspecs.edu)
	rows = dataquery.get_sqldata("select * from labor_participation_edu")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Labor Force Participation Rate by Sex, Education Attainment")


####	Labor Force: Labor Force Participation Rate by Age
@app.route("/data/labor-participation-age")
def labor_participation_age():
	rows = dataquery.get_sqldata("select * from labor_participation_age where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.age, rows, "Labor Force: Labor Force Participation Rate by Age", 
		"Percent (%)", "/data/labor-participation-age/table")

@app.route("/data/labor-participation-age/table")
def labor_participation_age_tab():
	colnames = dataquery.get_colnames("labor_participation_age", dataspecs.age)
	rows = dataquery.get_sqldata("select * from labor_participation_age")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Labor Force Participation by Age")


####	Labor Force: Unemployment Rate by Sex, Educational Attainment
@app.route("/data/labor-unemploymentrate-edu")
def labor_unemploymentrate_edu():
	rows = dataquery.get_sqldata("select * from labor_unemployrate_edu where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.edu, rows, "Labor Force: Unemployment Rate by Sex, Educational Attainment", 
		"Percent (%)", "/data/labor-unemploymentrate-edu/table")

@app.route("/data/labor-unemploymentrate-edu/table")
def labor_unemploymentrate_edu_tab():
	colnames = dataquery.get_colnames("labor_unemployrate_edu", dataspecs.edu)
	rows = dataquery.get_sqldata("select * from labor_unemployrate_edu")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment Rate by Sex, Educational Attainment")


####	Labor Force: Unemployment Rate by Age
@app.route("/data/labor-unemploymentrate-age")
def labor_unemploymentrate_age():
	rows = dataquery.get_sqldata("select * from labor_unemployrate_age where month = 'Ave.'")
	return dataquery.chartjs_input(dataspecs.age, rows, "Labor Force: Unemployment Rate by Age", 
		"Percent (%)", "/data/labor-unemploymentrate-age/table")

@app.route("/data/labor-unemploymentrate-age/table")
def labor_unemploymentrate_age_tab():
	colnames = dataquery.get_colnames("labor_unemployrate_age", dataspecs.age)
	rows = dataquery.get_sqldata("select * from labor_unemploy_age")
	return render_template('table.html', units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment Rate by Age")


####	Emission Account of Pollution
@app.route("/data/green-air")
def green_air():
	rows = dataquery.get_sqldata("select * from green_air")
	return dataquery.chartjs_input(dataspecs.green_air, rows, "Emmission Account of Pollution", 
		"Tons", "/data/green-air/table")

@app.route("/data/green-air/table")
def green_air_tab():
	colnames = dataquery.get_colnames("green_air", dataspecs.green_air)
	rows = dataquery.get_sqldata("select * from green_air")
	return render_template('table.html', units = "Tons", colnames = colnames, rows = rows,
		title = "Emission Account of Pollution")


####	Population Composition by Sex
@app.route("/data/social-population")
def social_population():
	rows = dataquery.get_sqldata("select * from social_pop")
	return dataquery.chartjs_input(dataspecs.sex, rows, "Population Composition by Sex", 
		"Thousands of persons", "/data/social-population/table")

@app.route("/data/social-population/table")
def social_population_tab():
	colnames = dataquery.get_colnames("social_pop", dataspecs.sex)
	rows = dataquery.get_sqldata("select * from social_pop")
	return render_template("table.html", units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Population Composition by Sex")


####	Price Indices (N.T.D. Basis)
@app.route("/data/price-index")
def price_index():
	rows = dataquery.get_sqldata("select * from price_index")
	return dataquery.chartjs_input(dataspecs.price_index, rows, "Price Indices (N.T.D. Basis)", 
		"Base Period: 2011 = 100", "/data/price-index/table")

@app.route("/data/price-index/table")
def price_index_tab():
	colnames = dataquery.get_colnames("price_index", dataspecs.price_index)
	rows = dataquery.get_sqldata("select * from price_index")
	return render_template("table.html", units = "Base Period: 2011 = 100", colnames = colnames, rows = rows,
		title = "Price Indices (N.T.D. Basis)")


####	Annual Change of Price Indices (N.T.D. Basis)
@app.route("/data/price-index-change")
def price_index_change():
	rows = dataquery.get_sqldata("select * from price_index_change")
	return dataquery.chartjs_input(dataspecs.price_index, rows, "Annual Change of Price Indices (N.T.D. Basis)", 
		"Percent (%)", "/data/price-index-change/table")

@app.route("/data/price-index-change/table")
def price_index_change_tab():
	colnames = dataquery.get_colnames("price_index_change", dataspecs.price_index)
	rows = dataquery.get_sqldata("select * from price_index_change")
	return render_template("table.html", units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Annual Change of Price Indices (N.T.D. Basis)")





if __name__ == "__main__":
	app.run()