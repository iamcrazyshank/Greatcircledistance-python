## Intercom
## take-home tests

from math import radians, degrees, sin, cos, asin, acos, sqrt
import json
import sys
import argparse


#Global Variable for Output file name
filename = ''
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

#Check validate latitude and longitude
def checkvalid_lat_long(lat, lng):
    if lat >= -90 and lat <= 90 and lng >= -180 and lng <= 180:
        return True
    else:
        return False


    
def great_circle(userdata):
    #Dublin office Lat Long
    Dub_off_Lat = 53.339428
    Dub_off_Long = -6.257664
    #local variables for user lat long
    lat=userdata.get_latitude()
    longi=userdata.get_longitude()
    #mapping to radians
    if checkvalid_lat_long(lat,longi):
             Dub_off_Long, Dub_off_Lat, lon2, lat2 = map(radians, [Dub_off_Long, Dub_off_Lat,longi,lat])
             #Applying great circle formula to return Bool
             return True if (6371 * ( acos(sin(Dub_off_Lat) * sin(lat2) + cos(Dub_off_Lat) * cos(lat2) * cos(Dub_off_Long - lon2)))) < 100 else False
    else :
        return False

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
    #writing the file in W+ mode, Create the file if not found
    with open(filename, 'w+') as f:
        #writing to the file
        for cust_data in cust_list:
            f.write("%s\n" % cust_data)
    

## function to read the file
def readfile(inputfile_name,output_filename):
    userObjList=[]
    global filename 
    filename = output_filename
    #Opening the file to read the user data
    try:
        for line in open(inputfile_name, 'r'):
                #making a json object for each user data and appending it
                users = []
                users.append(json.loads(line))
                for user in users:
                    userObjList.append(UserData(user['user_id'],user['name'],user['latitude'],user['longitude']))          
    except IOError:    
        #This means that the file does not exist 
        print ("Input File not found")

    getnearbycustomers(userObjList)


#Command line Arguments
def main(argv):   
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', help='Input file name')
    parser.add_argument('output_filename', help='Output file name')
    args = parser.parse_args()
    print("~ Input Filename: {}".format(args.input_filename))
    print("~ Output Filename: {}".format(args.output_filename))
    readfile(format(args.input_filename),format(args.output_filename))
   

if __name__ == "__main__":
   main(sys.argv[1:])
        

