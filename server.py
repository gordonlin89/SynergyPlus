from bottle import *
import mediator
import json

#Static resources
@route('/css/<filename>')
def css(filename):
	return static_file(filename, root='./css')

@route('/js/<filename>')
def css(filename):
	return static_file(filename, root='./js')

#AJAX
@post('/chart')
def test():
	time.sleep(2)
	temperature = request.forms.get('temperature')
	return mediator.getChart()

#Data
@get('/<building>/<floor>/csv')
def csv(building, floor):
	response.content_type = 'text/plain; charset=UTF8'
	return "\r\n".join([",".join([str(i) for i in data]) for data in mediator.getData()])

#SynergyPlus Pages
@route('/<building>/<floor>')
def layout(building, floor):
	return jinja2_template('main.html', data=mediator.getData())

run(host='localhost', port=8080)
