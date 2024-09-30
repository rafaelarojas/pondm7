FROM python:3.12-slim

WORKDIR /src/frontend

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.host=0.0.0.0"]
