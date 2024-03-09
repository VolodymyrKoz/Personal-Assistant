FROM python:3.11

WORKDIR /app
COPY personal_assistant/ /app
RUN pip install -r requirements.txt 

CMD ["python", "main.py"]  