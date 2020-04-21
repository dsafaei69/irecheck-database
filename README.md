# irecheck-database

please follow the instruction:


#In this project iReCHeCk.db is a data base which including name, gender, age, left-right-handed, country, city 
#for each student; the name of the game, level and the result of each episode are the rest of the information
#which store in data base. There are two ROS nodes first one send the data from db and the other one receive this 
#data from the defined topic and send an appropriate command according to the received data.

1) Make a catkin package 

2) Inside the caktin package we make a project named irecheck_test including scripts, include and src 

3) Put database and robot python file into the scripts folder

4) In terminal type this command "rosrun irecheck_test database.py" to run the database python file.
   database.py get the name of the student and the result of the game and send it to robot ros nodes.

5) In a new terminal type "rosrun irecheck_test robot.py" to see what this node receive and what send to the QT

6) the name of the topic here is "chatter" to see what is passing thwough this topic you can use this command "rostopic echo chatter"
