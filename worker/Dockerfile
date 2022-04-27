FROM python:alpine
RUN pip install requests
RUN pip install mysql-connector-python
RUN pip install Flask
COPY worker.py / 
CMD ["python", "worker.py"]
