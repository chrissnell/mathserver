from flask import Flask
from generators import fibonacci
from xml.etree.ElementTree import Element, SubElement, tostring, Comment
from xml.dom.minidom import parseString

app = Flask('__name__')

import server

