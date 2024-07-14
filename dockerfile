# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Copy local code to the container image.
WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "main.py"]

