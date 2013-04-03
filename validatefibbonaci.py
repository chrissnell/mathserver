from xml.dom import minidom
import sys
import re

xmldoc = minidom.parse(sys.stdin)

valuelist = xmldoc.getElementsByTagName('value')

data = valuelist[6].firstChild.nodeValue

value = re.search('\d+', data).group(0)

print "Server returned " + value + " as the fifth Fibonacci number."

if (int(value) == 8):
	print "Fibonacci sequence validated."
else:
	print "Invalid Fibonacci sequence."