FROM python:3.12
RUN mkdir /booking

WORKDIR  /booking

COPY requiremenets.txt .

RUN pip install -r requiremenets.txt

COPY . .
RUN chmod a+x /booking/docker/*.sh

CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]