# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install pandas

# Create input/output directories
RUN mkdir -p input output

# Set entrypoint
ENTRYPOINT ["python", "main.py"]
