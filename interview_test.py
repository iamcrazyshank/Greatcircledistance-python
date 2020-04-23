import unittest
import sys
from interview import great_circle
from interview import checkvalid_lat_long
from interview import UserData
import random



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

    def test_file_directory(self):
        self.assertEqual(self.inputfile_name,"customers.txt"), "Input file found"
        
    def test_checkvalid_lat_long(self):
        assert checkvalid_lat_long(self.test_lat_1,self.test_long_1) == True
        assert checkvalid_lat_long(self.test_lat_2,self.test_long_2) == True

    def test_great_cirle_Pass(self):
        test_object = self.userData_testObj_2
        assert great_circle(test_object) == True, "Test User 1 PASS"

    def test_great_cirle_Fail(self):
        test_object = self.userData_testObj_1
        assert great_circle(test_object) == False, "Test User 2 FAIL"

if __name__ == '__main__':  
    unittest.main() 