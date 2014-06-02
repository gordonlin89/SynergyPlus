
chart = {
	"chart": {"type":"line"},
	"title": {"text": 'Power Comparison'},
	"xAxis": {
		"categories": ['Jan', 'Feb', 'Mar'],
		"title": {"text":"Month"}
	},
	"yAxis": {
		"title": {"text":"Power (kW)"}
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

fooZones = [
	[(0, 0), (200, 0), (150, 40), (50, 40), (0, 0)]
]

def getChart():
	return chart

def getTimeInterval():
	return [1, 2, 3]

def getHeatingPower():
	return [1, 2, 3]

def getCoolingPower():
	return [1, 2, 3]

def getElectricalPower():
	return [1, 2, 3]

def getData():
	return zip(getTimeInterval(), getCoolingPower(), getHeatingPower(), getElectricalPower())

def getZoneOffset(zone, offset):
	return zones