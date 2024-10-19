FROM python:3.9-slim

WORKDIR /app

# Install system dependencies if necessary (for libraries that require compilation)
RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
