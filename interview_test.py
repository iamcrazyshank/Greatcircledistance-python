## Intercom
## take-home tests
##Shashank Chandran
##shashankchandran1994@gmail.com

import unittest
import sys
from interview import great_circle
from interview import checkvalid_lat_long
from interview import UserData
from interview import readfile




class UserDataTest(unittest.TestCase):
    def setUp(self):
        self.inputfile_name = sys.argv[2]
        self.outputfile_name = sys.argv[3]
        self.userData_testObj_1 = UserData(1,"test_user1",53.2451022,-7.338335)
        self.userData_testObj_2 = UserData(2,"test_user2",54.133333,-6.433333)
        self.test_lat_1 = 123.25
        self.test_long_1 = -442.555545
        self.test_lat_2 = 53.2451022
        self.test_long_2 = -6.433333
    #Test 1 IO Error for input file name
    def test_file_directory(self):
        testfilename = "test_fail.txt"
        self.assertRaises(IOError, readfile(testfilename,self.outputfile_name))

    #Test 2 Valid Lat Long Fail
    def test_checkvalid_lat_long_Fail(self):
        assert checkvalid_lat_long(self.test_lat_1,self.test_long_1) == True

    #Test 3 Valid Lat Long Fail
    def test_checkvalid_lat_long_Pass(self):
        assert checkvalid_lat_long(self.test_lat_2,self.test_long_2) == True

    #Test 4 check distance great circle formula- Pass case
    def test_great_cirle_Pass(self):
        test_object = self.userData_testObj_2
        assert great_circle(test_object) == True, "Test User 1 PASS"
    #Test 5 check distance great circle formula- Fail Case
    def test_great_cirle_Fail(self):
        test_object = self.userData_testObj_1
        assert great_circle(test_object) == False, "Test User 2 FAIL"

if __name__ == '__main__':  
    unittest.main() 