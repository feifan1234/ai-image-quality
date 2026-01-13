# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for OpenCV
# libgl1-mesa-glx and libglib2.0-0 are needed for cv2 even in headless mode sometimes
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY image_quality_system/requirements.txt .

# Install Python dependencies
# We use the headless version of opencv to avoid GUI issues
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY image_quality_system/backend /app/backend

# Create a non-root user to run the app (security best practice)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Expose port 9000 (Alibaba Cloud FC default port)
EXPOSE 9000

# Set the working directory to backend so imports work correctly
WORKDIR /app/backend

# Command to run the application
# Alibaba Cloud FC expects the app to run on port 9000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
