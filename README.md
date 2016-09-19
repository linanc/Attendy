## Face 'n Class Ver 2.0 - by 6S

Face 'n Class is a revolutionary way of taking class attendance for IEOR 171! First, all students in the class are invited to the class Facebook group. During a designated time in class, students take selfies of their groups and upload group selfies to Lecture events on the FB Group. All groups must tag each member in the photo. 

  The only thing the GSI (or designated student) has to do is to run the Python script in this repo. It will pull all the tags from all photos to create a CSV spreadsheet for attendance. The process should take about 15 minutes in total. 

## Facebook Setup and Usage

1. GSI must possess a Facebook account. 
  <br><i>Option A: Use personal Facebook account. 
  <br>Option B: Create a separate Facebook account.</i>
2. Students must possess a Facebook account. 
3. GSI creates a group on Facebook. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/creategroup.png "FB 3")
    
4. GSI names the group: IEOR 171. GSI adds students in IEOR 171 to this group. Lastly, GSI selects the closed group option. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/closedgroup.png "FB 4")
    
5. GSI then has the option to personalize the IEOR 171 group by choosing an icon.

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/personalizeicon.png "FB 5")
    
6. Congratulations! Your IEOR 171 close group has successfully been created. Feel free to upload a cover photo or choose an icon to personalize the IEOR 171 group, or add in a description of course objectives. 

    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/personalizepic.png "FB 6")

7. To take attendance, the GSI then creates an event for every lecture. For example, for lecture on 9/21/16, the GSI would create an event for that lecture. 
  
  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/createevent2.png "FB 7")
  
8.	During lecture, Professor announces that it’s time to take attendance. 
9.	Students take their group selfie, and one student from their group uploads it to the designated event. 
    
    ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/tagurself.png "FB 8")

10.	Students must then tag themselves in the selfie.
   
   ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/tagurself2.png "FB 9")

11. That's it for the GSI's activity on Facebook! Sit back and let your students take attendance/selfies. The only thing left for the GSI (or designated student) is to run the facenclass.py file in this repo at some later time. The script automatically pulls tags from all photos to create a CSV spreadsheet for attendance, saving lots of manual labbor. The process to install all necessary packages and run the script should take about 15 minutes in total. Below you will find directions on to use the facenclass.py script.  


## User Authentication

Because of Facebook's privacy settings, the GSI (or designated student helper) must first log in to Facebook and generate a user access token. To do so, visit:
<https://developers.facebook.com/tools/explorer/>, login, and generate a 2 hour user access token for user events and user managed groups. 

  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/fb1.png "FB 1")
  ![alt text](https://github.com/linanc/Attendy/blob/master/pictures/fb2.png "FB 2")

## Package Installation 

Make sure Python and pip are installed. In your terminal, run the following commands to install the Facebook SDK for Python: 

```$ pip install requests```

```$ pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk```

## Running the Script

Download facenclass.py to a desired location on your system. In the terminal, go to the directory where facenclass.py is located with the 'cd' command. 

```$ cd path/to/file```

  Run facenclass.py with the following command in the terminal:

```$ python facenclass.py```

Paste the access token and Facebook group ID into the terminal when asked. The script should generate 171_attendy.csv in the same location. 
  Run facenclass.py again later if you want to update the attendance spreadsheet with new lecture photos. 