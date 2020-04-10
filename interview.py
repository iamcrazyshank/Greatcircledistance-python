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
        #getter and setters
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
    #string function for write file
    def __str__(self):
        return ("User_id: " + str(self.__user_id) +  " Name:" + str(self.__user_name))


def great_circle(userdata):
    #Dublin office Lat Long
    Dub_off_Lat = 53.339428
    Dub_off_Long = -6.257664
    #local variables for user lat long
    lat=userdata.get_latitude()
    longi=userdata.get_longitude()
    #mapping to radians
    Dub_off_Long, Dub_off_Lat, lon2, lat2 = map(radians, [Dub_off_Long, Dub_off_Lat,longi,lat])
    #Applying great circle formula to return Bool
    return True if (6371 * ( acos(sin(Dub_off_Lat) * sin(lat2) + cos(Dub_off_Lat) * cos(lat2) * cos(Dub_off_Long - lon2)))) < 100 else False


def getnearbycustomers(userObjList):
   #declare Empty List
    near_by_cust_list=[]
    for user in userObjList:
            if great_circle(user):
                #find nearby users
                near_by_cust_list.append(user)
    #Sorting the list by userID            
    near_by_cust_list.sort(key=lambda x: x.get_user_id(), reverse=False)
    #write to the file
    write_to_file(near_by_cust_list)
    
#methon to write the nearby users to file "output_intercom.txt"
def write_to_file(cust_list) :
    with open('output_intercom.txt', 'w') as f:
        #writing to the file
        for cust_data in cust_list:
         f.write("%s\n" % cust_data)

## function to read the file
def readfile():
    users = []
    userObjList=[]
    #Opening the file to read the user data
    for line in open('customers.txt', 'r'):
        #making a json object for each user data and appending it
        users.append(json.loads(line))
    for user in users:
        userObjList.append(UserData(user['user_id'],user['name'],user['latitude'],user['longitude']))
    
    getnearbycustomers(userObjList)


#Program starts
readfile()


        

