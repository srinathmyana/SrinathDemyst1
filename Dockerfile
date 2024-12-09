# Use the official Python 3.8 slim image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container
COPY . /app

# Specify the default command to run your script
CMD ["python", "fixed_width_to_csv.py"]
