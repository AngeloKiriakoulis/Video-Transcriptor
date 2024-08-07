import datetime
import time
import cv2 as cv
from ffpyplayer.player import MediaPlayer

def play(video_file, transcript=None):
  cap = cv.VideoCapture(video_file)
  cap.set(cv.CAP_PROP_BUFFERSIZE, 2)
  player = MediaPlayer(video_file)
  
  # Check if video capture is initialized
  if not cap.isOpened():
    print("Error: Could not open video file.")
    return

  start_time = datetime.datetime.now()
  i = 0
  font = cv.FONT_HERSHEY_COMPLEX

  while True:
    ret, frame = cap.read()
    audio_frame, val = player.get_frame()
    if not ret:
        print("End of Video")
        break

    
    # Retrieve the fps to show video on normal speed
    t = datetime.datetime.now() - start_time
    seconds = float(t.total_seconds())
    fps = cap.get(cv.CAP_PROP_FPS)

    # Add text to the frame if transcript is available
    if transcript is not None and not transcript.empty:
      try:
        if seconds <= transcript["end"][i]:
          text = transcript["word"][i]
          textsize = cv.getTextSize(text, font, 1, 2)[0]
          textX = int(frame.shape[1] / 2 - (textsize[0]/2))  # Corrected shape dimension
          textY = int(frame.shape[0] / 2)
          cv.putText(frame, text, (textX, textY), font, 1, (0, 0, 255), 1, cv.LINE_AA)
        else:
          i += 1
      except IndexError:
        pass  # Ignore if index goes out of bounds
    cv.imshow('frame', frame)
    if val != 'eof' and audio_frame is not None:
      img, t = audio_frame
    keypress = cv.waitKey(int(1000 / fps))
    if keypress & 0xFF == ord('q'):  # Check for 'q' key to quit
      break
    
    # Press "Q" to exit the window. waitKey waits 1000/fps milliseconds before showing next frame
    # keypress = cv.waitKey(int(1000 / fps))
    # if keypress >= 0 & 0xFF == ord('q'):              # a key is being pressed
    #     time.sleep(1 / fps) # wait for 1 / frame_rate seconds

  # Release the memory used for parsing the video.
  cap.release()
  cv.destroyAllWindows()
