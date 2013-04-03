from generators import fibonacci
from xml.etree.ElementTree import Element, SubElement, tostring, Comment
from xml.dom.minidom import parseString
from mathserver import app

@app.route('/fibonacci/<sequence>', methods=['GET'])

def app_fibonacci(sequence):
	return(PrettyXML(fibonacci.Fibonacci(sequence)))

def PrettyXML(elem):
	ugly = tostring(elem)
	pretty = parseString(ugly)
	return pretty.toprettyxml(indent="  ")