## Face 'n Class Ver 2.0 - by 6S

Face 'n Class is a revolutionary way of taking class attendance for IEOR 171! First, all students in the class are invited to the class Facebook group. During a designated time in class, students take selfies of their groups and upload group selfies to Lecture events on the FB Group. All groups must tag each member in the photo. 

  The only thing the GSI (or designated student) has to do is to run the Python script in this repo. It will pull all the tags from all photos to create a CSV spreadsheet for attendance. The process should take about 15 minutes in total. 

## User Authentication

Because of Facebook's privacy settings, the GSI (or designated student helper) must first log in to Facebook and generate a user access token. To do so, visit:
<https://developers.facebook.com/tools/explorer/>, login, and generate a 2 hour user access token for user events and user managed groups. 

  ![alt text](https://github.com/linanc/Attendy/blob/master/fb1.png "FB 1")
  ![alt text](https://github.com/linanc/Attendy/blob/master/fb2.png "FB 2")

## Package Installation 

Make sure Python and pip are installed. In your terminal, run the following commands to install the Facebook SDK for Python: 

```$ pip install requests```

```$ pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk```

## Running the Script

Download facenclass.py to a desired location on your system. Copy and paste the user access token generated earlier to line 5 of facenclass.py (using a text editor such as Notepad or Sublime Text). Now you are ready to run the file!

  In the terminal, go to the directory where facenclass.py is located with the 'cd' command. 

```$ cd path/to/file```

  Run facenclass.py with the following command in the terminal:

```$ python facenclass.py```

The script should generate 171_Attendy.csv in the same location. 
  Run facenclass.py again later if you want to update the attendance spreadsheet with new lecture photos. 
