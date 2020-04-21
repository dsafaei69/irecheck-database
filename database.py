#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic
import sqlite3
import rospy
from std_msgs.msg import String


def database():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('database', anonymous=True)

    # Initialize publishers/subscribers.
    pub = rospy.Publisher('chatter', String, queue_size=10)











    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():

        # read from database.
        # ...

        connection = sqlite3.connect('/home/chili/Documents/iReCHeCk/Database/iReCHeCk/iReCheCk.db')
        cursor = connection.cursor()
        dynamico_table = """CREATE TABLE IF NOT EXISTS dynamico ( 
        student_number INTEGER PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        gender TEXT, 
        left_right-handed TEXT,
        country TEXT,
        city TEXT,
        game TEXT,
        level int not null,
        result TEXT);"""

        sql_command = """INSERT INTO dynamico_table (fname, lname, gender, birth_date,left_right-handed, country, city, game, level ,result) VALUES ("Dorsa", "Safaei", "f", "1990-07-30", "r","iran", "tehran", "worm", 2, "w");"""

        sql_command = """
        select * from dynamico;"""    
        cursor.execute(sql_command)
        for row in cursor.fetchall():
            studentname = row[0]
            gameresult= row[8]
            #studetname = 'Dorsa'
            #gameresult = 'Win'
            message = '{} {}'.format(studentname, gameresult)
            #message = "hello world %s" % rospy.get_time()

            rospy.loginfo(message)
            pub.publish(message)

            rospy.sleep(10.) # sleep for 10 seconds

        rate.sleep()


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    database()
