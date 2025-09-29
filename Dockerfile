FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 4000
CMD ["python3","app.py"]
