# Use an official Python runtime as a parent image
FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip install Flask pytube opencv-python ffpyplayer openai-whisper pandas --break-system-packages

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

ENV FLASK_APP=app.py

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
