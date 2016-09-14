## Face 'n Class Ver 1.0

Face 'n Class is a revolutionary way of taking class attendance for IEOR 171! First, all students in the class are invited to the class Facebook group. During a designated time in class, students take selfies of their groups and upload group selfies to Lecture events on the FB Group. All groups must tag each member in the photo. 

  The only thing the GSI has to do is to run the Python script in this repo, which pulls all the tags from all photos to create a CSV spreadsheet for attendance. 


## Installation

Make sure Python and pip are installed. In your terminal, run the following commands to install the Facebook SDK for Python: 

'''$ pip install requests
   $ pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
'''

Download facenclass.py to a desired location on your system. In the terminal, go to the directory where facenclass.py is located with the 'cd' command. 

'''$ cd path/to/file
'''

Run facenclass.py with the following command:

'''$ python facenclass.py
'''

The script should generate 171_Attendy.csv. Run facenclass.py again if you want to update the attendance spreadsheet. 