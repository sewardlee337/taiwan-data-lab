from flask import Flask, render_template, request, url_for
import dataspecs, dataquery, urlparse

app = Flask(__name__)


####	CONSTRUCT PAGES		####


@app.route("/")
@app.route("/index")
def index():
	spark_gdp = dataquery.get_sqldata("select gdp_const_nt from imf_weo")
	spark_unemploy = dataquery.get_sqldata("select unemploy from imf_weo")
	spark_inf = dataquery.get_sqldata("select infavg_ann from imf_weo")
	spark_gdpworld = dataquery.get_sqldata("select gdpworld_ppp from imf_weo")
	return render_template('index.html', spark_gdp = spark_gdp, spark_unemploy = spark_unemploy, spark_inf = spark_inf, spark_gdpworld=spark_gdpworld)

@app.route("/thanks")
def thanks():
	spark_gdp = dataquery.get_sqldata("select A from accounts_rgdp")
	return render_template('thanks.html', spark_gdp = spark_gdp)

@app.route("/construction")
def construction():
	return render_template('construction.html')

@app.route("/directory")
def directory():
	return render_template('directory.html')

@app.route("/faqs")
def faqs():
	return render_template('faqs.html')

@app.route("/cluster")
def cluster():
	return render_template('cluster-overview.html')

@app.route("/cluster-info")
def cluster_info():
	return render_template('cluster-info.html')

@app.route("/cluster-charts")
def cluster_charts():
	return render_template('cluster-charts.html')


@app.route("/imf-weo")
def imf_weo():
	return render_template('imf-weo-intro.html')





####################################
# TEST
####################################


@app.route("/test")
def test():
	spark_gdp = dataquery.get_sqldata("select gdp_const_nt from imf_weo")
	spark_unemploy = dataquery.get_sqldata("select unemploy from imf_weo")
	spark_inf = dataquery.get_sqldata("select infavg_ann from imf_weo")
	spark_gdpworld = dataquery.get_sqldata("select gdpworld_ppp from imf_weo")
	return render_template('test.html', spark_gdp = spark_gdp, spark_unemploy = spark_unemploy, spark_inf = spark_inf, spark_gdpworld=spark_gdpworld)




import taiwandatalab.data


if __name__ == "__main__":
	app.run()