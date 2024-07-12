import cv2 as cv

"""Dependency Conflicts: conda and pip use different dependency resolution strategies. Conda tries to ensure that all installed packages are compatible with each other, whereas pip installs packages and their dependencies in isolation."""

#Task 1: Let's first try to parse a video with OpenCV
def play(video_file, transcript = None):
  cap = cv.VideoCapture(video_file)
  print(transcript)
  while True:
    ret, frame = cap.read()
    # Retrieve the fps to show video on normal speed
    fps = cap.get(cv.CAP_PROP_FPS)
    font = cv.FONT_HERSHEY_COMPLEX 
  
    # Use putText() method for inserting text on video 
    cv.putText(frame,  
              transcript,  
              (50, 50),  
              font, 1,  
              (255, 255, 255),  
              2,  
              cv.LINE_AA)
    if not ret:
      break
    cv.imshow('Video', frame)
    # Press "Q" to exit the window. waitkey waits 1000/fps milliseconds before showing next frame
    if cv.waitKey(int(1000/fps)) & 0xFF == ord('q'):
      break
    
  # Release the memory used for parsing the video.
  cap.release()
  cv.destroyAllWindows()

