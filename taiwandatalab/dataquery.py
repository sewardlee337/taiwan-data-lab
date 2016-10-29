"""
This Python script contains functions to access and manipulate data stored in SQLite3 database.
"""
from flask import Flask, render_template, request
import sqlite3 as sql
import dataspecs, copy


def get_sqldata(my_query):
	"""
	Function for preparing data from SQLite3 database for chart. Returns an SQLite3 row object.

	'my_query' parameter is a valid SQL query to request data from SQLite3 database.
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

	'table' parameter is the SQLite3 table to query.

	'metrics_dict' parameter is the dictionary from dataspecs module that contains reusable data charting parameters
		for Chart.js.
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