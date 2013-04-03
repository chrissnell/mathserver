# About
**mathserver** is a simple RESTful web service that serves up mathmetical computations.   At the present time, it includes the following functionality:
##Fibonacci Sequences
`GET /fibonacci/n` will return a Fibonacci sequence with *n* numbers, where *n* &gte; 0.  
Sequences are returned in XML format; see schemas/fibonacci.xsd for schema.   
For negative values of *n*, a `403 Forbidden` HTTP error code will be returned.

# Installation and Use
## Install pip if you don't already have it

For Ubuntu:
	$ sudo apt-get install python-pip

## Install Flask
	$ sudo pip install flask

## Fetch and run the server

	$ git clone https://github.com/chrissnell/mathserver.git
	$ cd mathserver
	$ python mathserver.py

## Generate a Fibonacci sequence

	$ curl http://localhost:5000/fibonacci/10


# Testing

## Install libxml

For Ubuntu:

	$ sudo apt-get install libxml2-utils

## Validate output against XSD

From the `mathserver` top-level directory...

	$ curl -s http://localhost:5000/fibonacci/10 | xmllint --noout --schema mathserver/schemas/fibonacci.xsd -

This should produce the following output if the retured XML is valid:

	- validates

