FROM python:alpine3.7

RUN pip install --no-cache-dir flask colorhash

COPY webapp.py /webapp.py

EXPOSE 5000

CMD ["python", "/webapp.py"]
