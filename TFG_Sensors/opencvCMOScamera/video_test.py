# import the opencv library
import cv2
from datetime import datetime
import uuid
import re
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
#set the width and height, and UNSUCCESSFULLY set the exposure time
#vid.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
#vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_EXPOSURE, 0.1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
  
    
    # outfile = '%s/%s.jpg' % (self.tgtdir, self.basename + str(uuid.uuid4()))
    # outfile = '%s.jpg' % (str(uuid.uuid4()))

    
    if cv2.waitKey(200) & 0xFF == ord("s"):  # Press 's' to capture the image
        # print(cv2.waitKey(200) & 0xFF)
        # print(str(datetime.now()))
        current_time = str(datetime.now())
        valid_filename = re.sub(r'[^\w\s-]', '', current_time).strip().replace(' ', '_')
        # print("valid_filename: ", valid_filename)
        outfile = f'{valid_filename}.jpg'
        # outfile = str(datetime.now())
        cv2.imwrite(outfile, frame)
        # cv2.imwrite("captured_image.jpg", frame)
        print("Image captured!", outfile)
    elif cv2.waitKey(200) & 0xFF == ord("q"):  # Press 'q' to quit the program
        break
  # if 0xFF == ord('c'):
  #           cv2.imwrite("image"+ str(datetime.now()) + ".png", frame)
  #       if 0xFF == ord('q'): 
  #           break   



# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
