FROM python:3.9-slim

LABEL author="Bùi Thanh Vũ"
LABEL mssv="2280603717"
LABEL description="Docker Bonus Point"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Chạy ứng dụng Flask trên port 5000
EXPOSE 5000
CMD ["python", "app.py"]