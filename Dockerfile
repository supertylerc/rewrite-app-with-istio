FROM python:3.10-alpine3.15
WORKDIR /app
RUN pip3 install flask requests
COPY app.py .
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
