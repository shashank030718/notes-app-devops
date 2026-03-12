# Use slim image to keep size small (good practice)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies first (Docker layer caching — speeds up rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Don't run as root — security best practice
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Use gunicorn for production (not flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]