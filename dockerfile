FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt ./

# It looks like this is an open issue with pip freeze in version 20.1
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# These commands install the cv2 dependencies that are normally present on the local machine, but might be missing in your Docker container causing the issue.
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./src ./src

CMD ["python", "src/videos/transcript_video.py"]