FROM python:3.12

WORKDIR /app
COPY . /app/

RUN pip install .

CMD ["python", "-m", "found-poll-buddy"]