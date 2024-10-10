FROM python:3.10

WORKDIR /likes

# Copy requirements.txt and sources
COPY requirements.txt .
COPY . /likes

# Set the Python path to the app directory
ENV PYTHONPATH=/

# Install python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port the app runs on
EXPOSE 5888

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5888"]
