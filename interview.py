## Intercom
## take-home tests

from math import radians, degrees, sin, cos, asin, acos, sqrt

def readfile():
    cust_file = open("customers.txt")
    for line in cust_file.readlines():
        print (line)

readfile()