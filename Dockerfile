# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Collect static files (optional for dev)
RUN python manage.py collectstatic --noinput

# Set default command
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
