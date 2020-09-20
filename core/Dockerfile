FROM python:3.7.6

COPY /requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    mkdir /workdir

WORKDIR /workdir