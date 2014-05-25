from bottle import *
import json

chart = {
	"chart": {"type":"line"},
	"title": {"text": 'Power Comparison'},
	"xAxis": {
		"categories": ['Jan', 'Feb', 'Mar'],
		"title": {"text":"Month"}
	},
	"yAxis": {
		"title": {"text":"Power"}
	},
	"series":[
		{
			"name": "Current",
			"data": [5, 10, 15]
		},
		{
			"name": "Predicted",
			"data": [2, 4, 13]
		}
	],
	"credits": {"enabled": False}
}

#Static resources
@route('/css/<filename>')
def css(filename):
	return static_file(filename, root='./css')

@route('/js/<filename>')
def css(filename):
	return static_file(filename, root='./js')

@route('/img/<filename>')
def css(filename):
	return static_file(filename, root='./img')

#AJAX
@post('/test')
def test():
	time.sleep(1)
	temperature = request.forms.get('temperature')
	return chart

#SynergyPlus Pages
@route('/<building>/layout')
def base(building):
	return jinja2_template('layout.html')

@route('/<building>/predict')
def base(building):
	return jinja2_template('predict.html', power=json.dumps(chart))

run(host='localhost', port=8080)
