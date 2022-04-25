FROM python:3-alpine
RUN pip install Flask
RUN pip install Faker
COPY rng.py /
CMD ["python", "rng.py"]
EXPOSE 80
