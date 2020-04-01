## Intercom
## take-home tests

from math import radians, degrees, sin, cos, asin, acos, sqrt
import json

#defining class object for user data
class UserData:

    def __init__(self, user_id, user_name, latitude, longitude):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__latitude = latitude
        self.__longitude = longitude
        
    def set_user_id(self, id):
        self.__user_id = id

    def get_user_id(self):
        return self.__user_id

    def set_user_name(self, name):
        self.__user_name = name

    def get_user_name(self):
        return self.__user_name

    def set_latitude(self, lat):
        self.__latitude = lat

    def get_latitude(self):
        return float(self.__latitude)

    def set_longitude(self, long):
        self.__longitude = long

    def get_longitude(self):
        return float(self.__longitude)

    def __str__(self):
        return ("Object: " + str(self.__latitude) + " " + str(self.__longitude) + " " + str(self.__user_name)+ " " + str(self.__user_id))


def great_circle(userdara):
    Dub_off_Lat = 53.339428
    Dub_off_Long = -6.257664
    lat=userdara.get_latitude()
    longi=userdara.get_longitude()
    Dub_off_Long, Dub_off_Lat, lon2, lat2 = map(radians, [Dub_off_Long, Dub_off_Lat,longi,lat])

    return True if (6371 * ( acos(sin(Dub_off_Lat) * sin(lat2) + cos(Dub_off_Lat) * cos(lat2) * cos(Dub_off_Long - lon2)))) < 100 else False


def getnearbycustomers():
    for user in userObjList:
            print(great_circle(user))

## function to read the file
def readfile():
    users = []
    for line in open('customers.txt', 'r'):
        users.append(json.loads(line))
    for user in users:
        userObjList.append(UserData(user['user_id'],user['name'],user['latitude'],user['longitude']))
    
    getnearbycustomers()


userObjList=[]
readfile()


        

