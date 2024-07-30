import datetime
import cv2 as cv
import numpy as np

#Task 1: Let's first try to parse a video with OpenCV
def play(video_file, transcript = None):
  cap = cv.VideoCapture(video_file)
  print(transcript)
  start_time = datetime.datetime.now()
  img = np.zeros((600, 1000, 3), np.uint8)
  i = 0
  while True:
    ret, frame = cap.read()
    # Retrieve the fps to show video on normal speed
    fps = cap.get(cv.CAP_PROP_FPS)
    font = cv.FONT_HERSHEY_COMPLEX 
    time = datetime.datetime.now() - start_time
    seconds = float(time.total_seconds())

    # Use putText() method for inserting text on video 
    if transcript["start"][i]<=seconds<=transcript["end"][i]:
      text = transcript["text"][i]
      textsize = cv.getTextSize(text, font, 1, 2)[0]
      textX = (img.shape[1] - textsize[0]) / 2
      textY = (img.shape[0] + textsize[1]) / 2
      cv.putText(frame,  
          text,  
          (int(textX),int(textY)),  
          font, 1,  
          (255, 255, 255),  
          1,  
          cv.LINE_AA)
    else: 
      i+=1
    if not ret:
      break
    cv.imshow('Video', frame)
    # Press "Q" to exit the window. waitkey waits 1000/fps milliseconds before showing next frame
    if cv.waitKey(int(1000/fps)) & 0xFF == ord('q'):
      break
    
  # Release the memory used for parsing the video.
  cap.release()
  cv.destroyAllWindows()

