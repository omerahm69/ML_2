FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    curl \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app


# Streamlit runs on port 8501 by default
EXPOSE $PORT

# Start server using Gunicorn
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
