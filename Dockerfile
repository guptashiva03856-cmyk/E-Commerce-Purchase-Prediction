# Base Image
FROM python:3.11-slim

# Set Working Directory
WORKDIR /app

# Copy Requirements
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Entire Project
COPY . .

# Expose Streamlit Port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0"]