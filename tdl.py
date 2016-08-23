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
	return dataquery.chartjs_input(dataspecs.gdp, rows, "National Accounts: GDP by Expenditure (nominal)",
		"Million NT$, current prices", "/data/natlaccounts-ngdp/table")

@app.route("/data/natlaccounts-ngdp/table")
def natlaccounts_ngdp_tab():
	colnames = dataquery.get_colnames('accounts_ngdp', dataspecs.gdp)
	rows = dataquery.get_sqldata("select * from accounts_ngdp")
	return render_template('table.html', units = "Million NT$, current prices", colnames = colnames, rows = rows,
		title = "National Accounts: GDP by Expenditure (nominal)", source = "http://bit.ly/2aFohZ5")


####	National Accounts: GDP (real)
@app.route("/data/natlaccounts-rgdp")
def natlaccounts_rgdp():
	rows = dataquery.get_sqldata("select * from accounts_rgdp")
	return dataquery.chartjs_input(dataspecs.gdp, rows, "National Accounts: GDP by Expenditure (real)",
		"Million NT$, chained 2011 dollars", "/data/natlaccounts-rgdp/table")

@app.route("/data/natlaccounts-rgdp/table")
def natlaccounts_rgdp_tab():
	colnames =dataquery.get_colnames('accounts_rgdp', dataspecs.gdp)
	rows = dataquery.get_sqldata("select * from accounts_rgdp")
	return render_template('table.html', units = "Million NT$, chained 2011 dollars", colnames = colnames, rows = rows,
		title = "National Accounts: GDP by Expenditure (real)", source = "http://bit.ly/2aFohZ5")


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
		title = "National Accounts: GDP by Activity (nominal)", source = "http://bit.ly/2aFohZ5")


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
		title = "National Accounts: GDP by Activity (real)", source = "http://bit.ly/2aFohZ5")


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
		title = "Labor Force: Employment by Sex and Education Attainment", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Employment by Age", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Employment by Industry", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Employment by Occupation", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Employment by Class", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Unemployment by Sex and Education Attainment", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Unemployment by Age", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Unemployment by Reason", source = "http://bit.ly/2b0r2qk")


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
		title = "Labor Force: Not in Labor Force", source = "http://bit.ly/2b0r2qk")


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
	return render_template('table.html', units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Labor Force: Labor Force Participation Rate by Sex, Education Attainment", source = "http://bit.ly/2b0r2qk")


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
	return render_template('table.html', units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Labor Force: Labor Force Participation by Age", source = "http://bit.ly/2b0r2qk")


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
	return render_template('table.html', units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment Rate by Sex, Educational Attainment", source = "http://bit.ly/2b0r2qk")


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
	return render_template('table.html', units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Labor Force: Unemployment Rate by Age", source = "http://bit.ly/2b0r2qk")


####	Emission Account of Pollution
@app.route("/data/green-air")
def green_air():
	rows = dataquery.get_sqldata("select * from green_air")
	return dataquery.chartjs_input(dataspecs.green_air, rows, "Environmental Indicators: Emmission Account of Air Pollution", 
		"Tons", "/data/green-air/table")

@app.route("/data/green-air/table")
def green_air_tab():
	colnames = dataquery.get_colnames("green_air", dataspecs.green_air)
	rows = dataquery.get_sqldata("select * from green_air")
	return render_template('table.html', units = "Tons", colnames = colnames, rows = rows,
		title = "Environmental Indicators: Emission Account of Air Pollution", source = "http://bit.ly/2aBC96j")


####	Population Composition by Sex
@app.route("/data/social-population")
def social_population():
	rows = dataquery.get_sqldata("select * from social_pop")
	return dataquery.chartjs_input(dataspecs.sex, rows, "Social Indicators: Population Composition by Sex", 
		"Thousands of persons", "/data/social-population/table")

@app.route("/data/social-population/table")
def social_population_tab():
	colnames = dataquery.get_colnames("social_pop", dataspecs.sex)
	rows = dataquery.get_sqldata("select * from social_pop")
	return render_template("table.html", units = "Thousands of persons", colnames = colnames, rows = rows,
		title = "Social Indicators: Population Composition by Sex", source = "http://bit.ly/2aoWjlE")


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
		title = "Price Indices (N.T.D. Basis)", source = "http://bit.ly/2b0rmVZ")


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
		title = "Annual Change of Price Indices (N.T.D. Basis)", source = "http://bit.ly/2b0rmVZ")


####	Median Age of First Marriage
@app.route("/data/social-marriage-age")
def social_marriage_age():
	rows = dataquery.get_sqldata("select * from social_marriage_age")
	return dataquery.chartjs_input(dataspecs.sex_marriage, rows, "Social Indicators: Median Age of First Marriage", "Years", 
		"/data/social-marriage-age/table")

@app.route("/data/social-marriage-age/table")
def social_marriage_age_tab():
	colnames = dataquery.get_colnames("social_marriage_age", dataspecs.sex_marriage)
	rows = dataquery.get_sqldata("select * from social_marriage_age")
	return render_template("table.html", units = "Years", colnames = colnames, rows = rows,
		title = "Social Indicators: Median Age of First Marriage", source = "http://bit.ly/2aoWjlE")


####	Life Expectancy by Age (male)
@app.route("/data/social-life-expectancy-male")
def social_life_expectancy_male():
	rows = dataquery.get_sqldata("select * from social_life_expect_male")
	return dataquery.chartjs_input(dataspecs.life_expectancy, rows, "Social Indicators: Life Expectancy by Age (male)", "Years",
		"/data/social-life-expectancy-male/table")

@app.route("/data/social-life-expectancy-male/table")
def social_life_expectancy_male_tab():
	colnames = dataquery.get_colnames("social_life_expect_male", dataspecs.life_expectancy)
	rows = dataquery.get_sqldata("select * from social_life_expect_male")
	return render_template("table.html", units = "Years", colnames = colnames, rows = rows,
		title = "Social Indicators: Life Expectancy by Age (male)", source = "http://bit.ly/2aoWjlE",
		notes = "1) Data prior to 1991 do not include Fujian Province. 2) Figures since 1996 calculated using new methodology.")


####	Life Expectancy by Age (female)
@app.route("/data/social-life-expectancy-female")
def social_life_expectancy_female():
	rows = dataquery.get_sqldata("select * from social_life_expect_female")
	return dataquery.chartjs_input(dataspecs.life_expectancy, rows, "Social Indicators: Life Expectancy by Age (female)", "Year",
		"/data/social-life-expectancy-female/table")

@app.route("/data/social-life-expectancy-female/table")
def social_life_expectancy_female_tab():
	colnames = dataquery.get_colnames("social_life_expect_female", dataspecs.life_expectancy)
	rows = dataquery.get_sqldata("select * from social_life_expect_female")
	return render_template("table.html", units = "Years", colnames = colnames, rows = rows,
		title = "Social Indicators: Life Expectancy by Age (female)", source = "http://bit.ly/2aoWjlE",
		notes = "1) Data prior to 1991 do not include Fujian Province. 2) Figures since 1996 calculated using new methodology.")


####	Number of Births
@app.route("/data/social-births")
def social_births():
	rows = dataquery.get_sqldata("select * from social_births")
	return dataquery.chartjs_input(dataspecs.births, rows, "Social Indicators: Number of Births", "No.", "/data/social-births/table")

@app.route("/data/social-births/table")
def social_births_tab():
	colnames = dataquery.get_colnames("social_births", dataspecs.births)
	rows = dataquery.get_sqldata("select * from social_births")
	return render_template("table.html", units = "No.", colnames = colnames, rows = rows, title = "Social Indicators Number of Births",
		source = "http://bit.ly/2aoWjlE")


####	Recycling
@app.route("/data/green-recycling")
def green_recycling():
	rows = dataquery.get_sqldata("select * from green_recycling")
	return dataquery.chartjs_input(dataspecs.recycling, rows, "Environmental Indicators: Recycling Account", "Tons", 
		"/data/green-recycling/table")

@app.route("/data/green-recycling/table")
def green_recycling_tab():
	colnames = dataquery.get_colnames("green_recycling", dataspecs.recycling)
	rows = dataquery.get_sqldata("select * from green_recycling")
	return render_template("table.html", units = "Tons", colnames = colnames, rows = rows, 
		title = "Environmental Indicators: Recycling Account", source = "http://bit.ly/2aBC96j")


####	Emission Account of Water Pollution
@app.route("/data/green-water")
def green_water():
	rows = dataquery.get_sqldata("select * from green_water")
	return dataquery.chartjs_input(dataspecs.water, rows, "Environmental Indicators: Emission Account of Water Pollution",
		"Tons", "/data/green-water/table")

@app.route("/data/green-water/table")
def green_water_tab():
	colnames = dataquery.get_colnames("green_water", dataspecs.water)
	rows = dataquery.get_sqldata("select * from green_water")
	return render_template("table.html", units = "Tons", colnames = colnames, rows = rows,
		title = "Environmental Indicators: Emission Account of Water Pollution", source = "http://bit.ly/2aBC96j")


####	Education Enrollment Rates
@app.route("/data/social-edu-enrollment")
def social_edu_enrollment():
	rows = dataquery.get_sqldata("select * from social_edu_enroll")
	return dataquery.chartjs_input(dataspecs.edu_enrollment, rows, "Social Indicators: Net Education Enrollment Rates",
		"Percent (%)", "/data/social-edu-enrollment/table")

@app.route("/data/social-edu-enrollment/table")
def social_edu_enrollment_tab():
	colnames = dataquery.get_colnames("social_edu_enroll", dataspecs.edu_enrollment)
	rows = dataquery.get_sqldata("select * from social_edu_enroll")
	return render_template("table.html", units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Social Indicators: Net Education Enrollment Rates", source = "http://bit.ly/2aoWjlE")


####	Education Attainment Rates
@app.route("/data/social-edu-attainment")
def social_edu_attainment():
	rows = dataquery.get_sqldata("select * from social_edu_attain")
	return dataquery.chartjs_input(dataspecs.edu_attainment, rows, "Social Indicators: Education Attainment of Population Aged 15+",
		"Percent (%)", "/data/social-edu-attainment/table")

@app.route("/data/social-edu-attainment/table")
def social_edu_attainment_tab():
	colnames = dataquery.get_colnames("social_edu_attain", dataspecs.edu_attainment)
	rows = dataquery.get_sqldata("select * from social_edu_attain")
	return render_template("table.html", units = "Percent (%)", colnames = colnames, rows = rows,
		title = "Social Indicators: Education Attainment of Population Aged 15+", source = "http://bit.ly/2aoWjlE")


####	Standardized Death Rates
@app.route("/data/social-death-rates")
def social_death_rates():
	rows = dataquery.get_sqldata("select * from social_deaths")
	return dataquery.chartjs_input(dataspecs.deaths, rows, 
		"Social Indicators: Standardized Death Rates of Leading Causes per 100,000 Population", "Rate", 
		"/data/social-death-rates/table")

@app.route("/data/social-death-rates/table")
def social_death_rates_tab():
	colnames = dataquery.get_colnames("social_deaths", dataspecs.deaths)
	rows = dataquery.get_sqldata("select * from social_deaths")
	return render_template("table.html", units = "Rate", colnames = colnames, rows = rows,
		title = "Social Indicators: Standardized Death Rates of Leading Causes per 100,000 Population",
		source = "http://bit.ly/2aoWjlE")

####	Cross Strait Affairs: Trade with China
@app.route("/data/cross-strait-cn-trade")
def cross_strait_cn_trade():
	rows = dataquery.get_sqldata("select * from strait_cntrade")
	return dataquery.chartjs_input(dataspecs.cn_trade, rows, 
		"Cross-Strait Affairs: Trade with Mainland China", "Million US$", 
		"/data/cross-strait-cn-trade/table")

@app.route("/data/cross-strait-cn-trade/table")
def cross_strait_cn_trade_tab():
	colnames = dataquery.get_colnames("strait_cntrade", dataspecs.cn_trade)
	rows = dataquery.get_sqldata("select * from strait_cntrade")
	return render_template("table.html", units = "Million US$", colnames = colnames, rows = rows,
		title = "Cross-Strait Affairs: Trade with Mainland China",
		source = "http://bit.ly/2bz8ZEw", notes = "1) 'Exports' indicates exportation from Taiwan to Mainland China. 'Imports' indicates importation from Mainland China to Taiwan. 2) ROC Customs Statistics from 2001 through 2016 have been revised based on General Trade System to conform to United Nations International Merchandise Trade Statistics.")

####	International Trade: Exports with Major Trading Partners
@app.route("/data/trade-exports")
def trade_exports():
	rows = dataquery.get_sqldata("select * from trade_exports")
	return dataquery.chartjs_input(dataspecs.trade_countries, rows,
		"International Trade: Exports with Major Trading Partners", "US$",
		"/data/trade-exports/table")

@app.route("/data/trade-exports/table")
def trade_exports_tab():
	colnames = dataquery.get_colnames("trade_exports", dataspecs.trade_countries)
	rows = dataquery.get_sqldata("select * from trade_exports")
	return render_template("table.html", units = "US$", colnames = colnames, rows = rows,
		title = "International Trade: Exports with Major Trading Partners",
		source = "http://bit.ly/2bw6PE8", notes = "1) Figures include re-exports. 2) Countries identified as 'Major Trading Partners' based on 'Cross-Strait Economic Statistics Monthly' published by Mainland Affairs Council")

####	International Trade: Imports with Major Trading Partners
@app.route("/data/trade-imports")
def trade_imports():
	rows = dataquery.get_sqldata("select * from trade_imports")
	return dataquery.chartjs_input(dataspecs.trade_countries, rows,
		"International Trade: Imports with Major Trading Partners", "US$",
		"/data/trade-imports/table")

@app.route("/data/trade-imports/table")
def trade_imports_tab():
	colnames = dataquery.get_colnames("trade_imports", dataspecs.trade_countries)
	rows = dataquery.get_sqldata("select * from trade_imports")
	return render_template("table.html", units = "US$", colnames = colnames, rows = rows,
		title = "International Trade: Imports with Major Trading Partners",
		source = "http://bit.ly/2bw6PE8", notes = "1) Figures include re-imports. 2) Countries identified as 'Major Trading Partners' based on 'Cross-Strait Economic Statistics Monthly' published by Mainland Affairs Council")

####	International Trade: Total Trade with Major Trading Partners
@app.route("/data/trade-total")
def trade_total():
	rows = dataquery.get_sqldata("select * from trade_total")
	return dataquery.chartjs_input(dataspecs.trade_countries, rows,
		"International Trade: Total Trade with Major Trading Partners", "US$",
		"/data/trade-total/table")

@app.route("/data/trade-total/table")
def trade_total_tab():
	colnames = dataquery.get_colnames("trade_total", dataspecs.trade_countries)
	rows = dataquery.get_sqldata("select * from trade_total")
	return render_template("table.html", units = "US$", colnames = colnames, rows = rows,
		title = "International Trade: Total Trade with Major Trading Partners",
		source = "http://bit.ly/2bw6PE8", notes = "Figures include re-exports and re-imports. 2) Countries identified as 'Major Trading Partners' based on 'Cross-Strait Economic Statistics Monthly' published by Mainland Affairs Council")

if __name__ == "__main__":
	app.run()