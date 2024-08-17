# Use an official Fedora runtime as a parent image
FROM fedora:latest

# Update the package list and install dependencies
RUN dnf -y update && dnf -y install \
    python3-pip \
    # ffmpeg \
    # libsm6 \
    libXext \
    libglvnd-glx \
    wget \
    ImageMagick-libs \
    ImageMagick \
    && dnf clean all

# Download and install ImageMagick using rpm
# RUN wget https://imagemagick.org/archive/linux/CentOS/x86_64/ImageMagick-7.1.1-36.x86_64.rpm \
#     && wget https://imagemagick.org/archive/linux/CentOS/x86_64/ImageMagick-libs-7.1.1-36.x86_64.rpm \
#     && dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm \
#     && rpm -Uvh ImageMagick-7.1.1-36.x86_64.rpm \
#     && rpm -Uvh ImageMagick-libs-7.1.1-36.x86_64.rpm \
#     && rm -f ImageMagick-7.1.1-36.x86_64.rpm ImageMagick-libs-7.1.1-36.x86_64.rpm

# Install Python dependencies
RUN pip3 install Flask pytube opencv-python ffpyplayer openai-whisper pandas moviepy pygame ffmpeg

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Specify the command to run your Flask app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
