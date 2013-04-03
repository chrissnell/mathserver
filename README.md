# About
mathserver is a simple RESTful web service that serves up mathmetical computations.   At the present time, it includes the following functionality:
##Fibonacci Sequences
`GET /fibonacci/n` will return a Fibonacci sequence with *n* numbers, where *n* &gte; 0.  For negative values of *n*, a `403 Forbidden` HTTP error code will be returned.
