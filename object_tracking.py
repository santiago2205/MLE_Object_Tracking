import logging
import cv2 as cv
import json
import sys
import messages


def tracking_objects(cap, myfile, track):
    # OpenCV object tracker implementations
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv.TrackerCSRT_create,
        "kcf": cv.TrackerKCF_create
    }
    # Initialize OpenCV's special multi-object tracker
    trackers = cv.MultiTracker_create()

    # Read first frame.
    try:
        ret, frame = cap.read()
        logging.info(messages.READFRAME)
    except cv.error:
        logging.error(messages.NOTREADFRAME)
        sys.exit()

    # Read json file
    data=myfile.read()

    # Load json file
    obj = json.loads(data)
    logging.info(messages.NUMOBJTOTRACK + str(len(obj)))

    # Take coordinate from json file
    for i in obj:
        # Read coordinates
        x, y, w, h = i['coordinates']

        # Define an initial bounding box
        bbox = (x, y, w, h)

        # Select te metod to track
        tracker = OPENCV_OBJECT_TRACKERS[track]()
        # Add the new bounding box to track
        trackers.add(tracker, frame, bbox)

    logging.info(messages.TYPEOFTRACK + str(track))
    logging.info(messages.STARTVIDEO)

    while True:
        # Start timer
        timer = cv.getTickCount()

        # Read new frame
        ret, frame = cap.read()

        # Update the position of bounding box
        success, boxes = trackers.update(frame)

        # Redraw with the new position of bounding box
        for index, box in enumerate(boxes):
            x, y, w, h = [int(v) for v in box]
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(frame, obj[index]['object'], (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        
        # Calculate Frames per second (FPS)
        fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

        # Display FPS on frame
        cv.putText(frame, "FPS : " + str(int(fps)), (100,50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2);

        # Display result
        try:
            cv.imshow("Frame", frame)
        except:
            break

        # Exit if ESC pressed
        key = cv.waitKey(1)
        if key == 27:
            logging.info(messages.EXITBYUSER)
            break

    cap.release()
    cv.destroyAllWindows()
    logging.info(messages.FINISHVIDEO)
