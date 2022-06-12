#!/usr/bin/python3

""" The following code uploads the video and takes from a json
 file the number and initial position of the objects to be tracked.
 To run this code is necessary to put the following parameters in the terminal:
 -j = full path of json file
 -v = full path of video
 -t = type of tracking (csrt or kcf)

 @Author: Santiago Rivier
 @Dathe: 13/06/2022
 @Github: https://github.com/santiago2205/MLE_Object_Tracking
 """

import getopt
import sys
import cv2 as cv
import messages
import logging
import object_tracking

def loggingConfig():
    # Logg configuration
    logging.basicConfig(filename='track.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # Add the handler to the root logger
    logging.getLogger('').addHandler(console)

def main():
    json_dir = None
    video_dir = None
    type_track = None
    # Funtion to accept the parameter by terminal
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'j:v:t:')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for (op, ar) in opt:

        # If parameter is -j open a json file
        if op == '-j':

            json_dir = str(ar)
            try:
                myfile = open(json_dir, 'r')
                logging.info(messages.JSONFILEOPEN)
            except FileNotFoundError: 
                logging.error(messages.FILENOTFOUND)
                sys.exit()
        
        #If parameter is -v open a video file
        if op == '-v':

            video_dir = str(ar)
            try: 
                cap = cv.VideoCapture(video_dir)
                logging.info(messages.VIDEOFILEOPEN)
            except cv.error:
                logging.error(messages.VIDEOFILENOTFOUND)
                sys.exit()
        
        # If parameter is -t select the metod to track the objects
        if op == '-t':

            type_track = str(ar)
            if type_track in ('csrt', 'kcf'):
                logging.info(messages.CORRECTTRACK)
            else:
                logging.error(messages.ERRORTRACK)
                sys.exit()

    object_tracking.tracking_objects(cap, myfile, type_track)

if __name__=='__main__':
    loggingConfig()

    main()
