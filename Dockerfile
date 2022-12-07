FROM python:3.10-slim

WORKDIR /opt/synclink-server

COPY ./requirements.txt /opt/synclink-server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/synclink-server/requirements.txt

COPY ./ /opt/synclink-server

CMD ["python", "main.py"]
