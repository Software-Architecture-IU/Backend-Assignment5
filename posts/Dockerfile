# Dockerfile for users microservice
FROM python:3.10

WORKDIR /posts

# Copy requirements.txt and sources
COPY requirements.txt .
COPY . /posts

# Set the Python path to the app directory
ENV PYTHONPATH=/

# Install python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port the app runs on
EXPOSE 8043

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8043"]
