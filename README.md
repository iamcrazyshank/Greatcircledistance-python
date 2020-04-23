# Intercom (great-circle-distance)
- Take home test Assessment
- Program to find the nearest customer(within 100kms) from the Intercomm Dublin Office

- Shashank Chandran

Pre-requisite
------------
- Python version 2.7 and above
- Pytest 3.0 and above (Ref for installation :https://docs.pytest.org/en/3.0.1/getting-started.html )
  - pip install -U pytest

Features
--------
- Using Great Circle Distance Formula(https://en.wikipedia.org/wiki/Great-circle_distance) finds the customer nearby the Intercom dublin office which is sorted by user ID
- Inputs Command line arguments
    1. Python File
    2. Input file (Customers.txt)
    3. Output file (Output_intercomm.txt)

Code Run Guide
------------
Running the code :
1. Go to terminal(After installing python globally), type 
    - python interview.py customers.txt output_intercom.txt 
  -  argument 1 input file containing all the customer details 
  -  argument 2 expected ouput file 
2. For usage/help type,  
   - python interview.py -h 
3. Output :
  - ~ Input Filename: customers.txt
  - ~ Output Filename: output_intercomm.txt

Testing Guide
------------

Testing the code:
1. Go to terminal(After installing pytest ), type 
    - python -m pytest interview_test.py customers.txt output_intercom.txt
  -  argument 1 input file containing all the customer details 
  -  argument 2 expected ouput file 

2. Output :
  - ~ Input Filename: customers.txt
  - ~ Output Filename: output_intercomm.txt
