# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /CPT

# Copy the current directory contents into the container at /app
COPY . /CPT

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uwsgi", "--ini", "uwsgi.ini"]
