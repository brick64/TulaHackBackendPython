# Use the official Python image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY pyproject.toml /app/
COPY src /app/src

# Install dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi


ENV PYTHONPATH=/app/src

# Expose the application port
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]